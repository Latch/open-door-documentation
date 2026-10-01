---
title: Migrating from Latch SDK v1 to OpenDOOR SDK v2
excerpt: >-
  Step-by-step guide for upgrading existing Latch SDK v1 (OpenKit) integrations
  to OpenDOOR SDK v2 on Android and iOS.
deprecated: false
hidden: false
icon: far fa-arrow-up-z-a
metadata:
  robots: index
---
This guide is for engineers whose app already integrates Latch SDK v1 (OpenKit) and is upgrading to OpenDOOR SDK v2. If you are building a new integration, use the [Android SDK tutorial](https://developers.door.com/docs/android-docs) or [iOS SDK docs](https://developers.door.com/docs/ios-docs) instead — they cover install and usage from scratch. Android migrators should keep the tutorial open alongside this guide; the tutorial is the current from-scratch reference, and this guide covers the v1-to-v2 deltas.

***

## Before you begin

1. Confirm coroutines (Android) or Swift Concurrency (iOS) is already wired into your app. v2 has no blocking or completion-handler façade. If you don't have a coroutine scope at the call sites today, add concurrency support in a separate PR before this one — mixing the two refactors makes the diff hard to review.
2. Inventory your SDK surface. Run a project-wide search for `LatchClient.`, `Latch.` (iOS), `import com.latch.android.sdk`, and `import LatchSDK`, and list the call sites. The migration is mechanical once you know the size of the diff.
3. Read [§ The three shifts](#the-three-shifts). The whole rewrite makes sense once you've internalized them.

***

## The three shifts

Almost everything else is mechanical search-and-replace once these click.

### Shift 1 — Async model

|             | v1                                          | v2                     |
| ----------- | ------------------------------------------- | ---------------------- |
| **Android** | `Single<T>` (RxJava)                        | `suspend fun … throws` |
| **iOS**     | completion handlers + ad-hoc `async throws` | mostly `async throws` (stream, listener, cancel and proximity calls are sync `throws`; `setLogLevel` doesn't throw) |

### Shift 2 — Outcome model

|          | v1                                                                                                         | v2                                                                                   |
| -------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Both** | Sealed `*Result` classes, where success and failure both flow as values (Android) / per-method error enums (iOS) | Typed exceptions thrown from the call site; the return value **is** the success type |

### Shift 3 — Streaming model

|          | v1                                               | v2                                                                                                                             |
| -------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| **Both** | 3-method dance: `start*` + `*Listener` + `stop*` | One observable: `Flow<T>` (Android) / `AsyncStream<T>` + Combine (iOS) — with optional listener overload for legacy call sites |

***

## Migration in five steps

One recommended order. Each step is a self-contained change — land them sequentially to keep diffs small.

### Step 1 — Swap the dependency

v1 Android was distributed as a zipped artifact that you unzipped into a local folder (e.g. `com/latch/sdk/1.5.0`) and consumed by adding that folder as a maven repository. v2 is published to Maven Central, so the unzip-and-host-it-yourself step goes away. v1 iOS was distributed as a local Swift Package added via Xcode → File → Add Packages → Add Local; v2 iOS is a remote SPM package. Use the exact current versions from the [Android SDK tutorial](https://developers.door.com/docs/android-docs) and the [iOS SDK docs](https://developers.door.com/docs/ios-docs).

Android (`app/build.gradle.kts`):

```kotlin
// Remove — v1 install
// The local-folder maven repo that pointed at the unzipped artifacts:
repositories {
    maven { url = uri("[your/path/to/unzipped-sdk]") }
}
implementation("com.latch:sdk:1.8.1")

// Add — v2 install
// settings.gradle.kts
dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()
    }
}
// Application module build.gradle.kts
implementation("com.door:opendoor.android:2.3")
```

You can also delete the unzipped SDK folder from your repo once the v2 dependency resolves cleanly.

iOS (Xcode):

```
Remove — v1 install
  File → Packages → remove the local "LatchSDK" package reference,
  then delete the LatchSDK folder you had checked into the repo.

Add — v2 install (Package.swift or Xcode "Add Package")
  .package(url: "https://github.com/Latch/opendoor-sdk-spm.git", from: "2.3.0")
```

If you were on CocoaPods (`pod 'LatchSDK'`), this is your forcing function to switch to SPM — v2 publishes only via SPM.

### Step 2 — Update imports & entry point

```bash
# Android — repo-wide (v2 public types live under core.api)
find . -type f \( -name "*.kt" -o -name "*.java" \) -print0 \
  | xargs -0 sed -i '' \
      -e 's/com\.latch\.android\.sdk\.core\.LatchClient/com.door.opendoor.android.core.api.OpenDOOR/g' \
      -e 's/com\.latch\.android\.sdk\.core/com.door.opendoor.android.core.api/g' \
      -e 's/com\.latch\.android\.sdk\.model/com.door.opendoor.android.core.api.model/g'

# iOS — repo-wide
find . -type f -name "*.swift" -print0 \
  | xargs -0 sed -i '' 's/import LatchSDK/import OpenDOORCore/g'
```

Then swap the entry point. Android first:

```kotlin
// v1
val client = LatchClient

// v2
val client = OpenDOOR.instance   // type: DoorClient
```

iOS:

```swift
// v1
let latch = try await Latch.initialize(withToken: token, loadAllAccesses: false)

// v2 — getInstance() is async because it lazily constructs internal state.
// Cache the returned client in your DI container; you only need to call it
// once per process.
let client = await OpenDOOR.getInstance()
try await client.setupWithToken(token: token, includeAllLocks: false)
```

### Step 3 — Convert request/response calls

Every `Single<T>.subscribe { result -> when }` block becomes a `try { … } catch (TypedException)` block; every iOS bespoke-error-enum `catch` becomes a typed-error `catch`. See [§ API-by-API migration](#api-by-api-migration) for one-to-one mappings.

The minimum-viable conversion pattern, Android:

```kotlin
// v1
LatchClient.fetchLocks().subscribe { result ->
    when (result) {
        is LocksResult.Success        -> render(result.locks)
        is LocksResult.NotInitialized -> showSetup()
        is LocksResult.Error          -> showError(result.description)
    }
}

// v2
viewModelScope.launch {
    try {
        render(client.fetchLocks())
    } catch (e: SDKException.SDKNotInitializedException) {
        showSetup()
    } catch (e: NetworkException) {
        showError(e.message)
    }
}
```

### Step 4 — Subscribe to event streams (the biggest behavioral change)

In v1, `unlock()` reported the outcome itself (an `UnlockResult` on Android, a thrown `UnlockError` on iOS). In v2, `unlock()` returns no outcome: on iOS it returns once the unlock starts, and on Android it suspends until the attempt ends. Outcomes arrive on `listenForUnlockEvents()`. Exceptions thrown from `unlock()` are pre-flight failures only (Bluetooth off, lock not in cache, etc.).

Wire the stream once, right after `setupWithToken` succeeds. Subscribing earlier throws, because the SDK is not initialized yet. On iOS, `clear()` ends open streams, so subscribe again after the next setup.

```kotlin
// Android — right after setupWithToken succeeds
appScope.launch {
    client.listenForUnlockEvents().collect { event ->
        unlockUiBus.emit(event)   // your own UI bus / state holder
    }
}
```

```swift
// iOS — same idea, right after setupWithToken succeeds
Task {
    for await event in try client.listenForUnlockEvents() {
        await unlockUIStore.handle(event)
    }
}
```

Then at each call site, stop expecting a return value:

```kotlin
// v1
val outcome = LatchClient.unlock(lockId).blockingGet()
when (outcome) { /* …Success / OutOfSchedule / LockNotFound handling… */ }

// v2 — observe the outcome elsewhere
try {
    client.unlock(lockId)   // returns no outcome; on Android it suspends until the attempt ends
} catch (e: BluetoothException.BluetoothDisabledException) {
    promptEnableBluetooth()
}
// outcome arrives on the stream you wired earlier
```

Apply the same pattern to proximity unlock — the unified `listenForUnlockEvents()` carries proximity events too, distinguished by `event.method`. See [§ Proximity unlock](#proximity-unlock).

### Step 5 — Update guest-invite call sites

The invite call no longer takes a `PasscodeType`. Use one of two top-level types that implement `InviteType` (a sealed interface on Android, a protocol on iOS): `InAppInvite` or `TemporaryDoorcodeInvite`. `PasscodeType` stays only as a read-only field on `GuestAccess`. See [§ Guest invitations](#guest-invitations) for the full mapping.

```kotlin
// v1
LatchClient.inviteGuests(
    firstName, lastName, email, phone,
    startTime, endTime,
    deviceUuids = listOf(lockId.toString()),
    passcodeType = PasscodeType.Permanent,
).subscribe { /* … */ }

// v2
client.inviteGuest(
    firstName = firstName,
    lastName  = lastName,
    email     = email,
    phone     = phone,
    lockIds   = listOf(lockId),
    inviteType = InAppInvite(
        startTime = startTime,   // java.time.Instant now; v1 took org.threeten.bp.LocalDateTime
        endTime   = endTime,
    ),
)
```

Translate your invite-form UI state into an `InviteType` at the boundary (the moment the user taps "Send"). Don't propagate a v1-shaped `PasscodeType` enum through your domain layer.

***

## Rename map (quick reference)

### Modules & entry points

|                     | v1                              | v2                                                                                            |
| ------------------- | ------------------------------- | --------------------------------------------------------------------------------------------- |
| Brand               | Latch SDK / OpenKit             | OpenDOOR                                                                                      |
| Android package     | `com.latch.android.sdk` (`.core`, `.model`) | `com.door.opendoor.android.core.api` (plus `.model`, `.exceptions`, `.listeners`)        |
| Android entry       | `LatchClient` (object)          | `OpenDOOR.instance: DoorClient`                                                               |
| Android model fields | `uuid`, `buildingUuid`, `GuestAccess.lockUuid`, `lock.access.*` | `id`, `buildingId`, `GuestAccess.lockId`, `lock.startTime` / `endTime` / `doorCode` |
| Android date-time type | `LocalDateTime`              | `java.time.Instant`                                                                           |
| Android `AccessLogResult` | `Success`, `NFCFailure`, … | `SUCCESS`, `NFC_FAILURE`, …                                                                  |
| iOS module          | `LatchSDK`                      | `OpenDOORCore` (importable library product; the SPM package directory is named `OpenDOORSDK`) |
| iOS entry           | `Latch.initialize(withToken:…)` | `await OpenDOOR.getInstance()` then `client.setupWithToken(...)`                              |
| iOS error protocol  | `LatchSDKError`                 | `OpenDOORSDKError`                                                                            |
| iOS access-log type | `LatchAccessLog`                | `AccessLog` (`uuid` → `id`, `guestUuid` → `guestUUID`, `lockUuid` → `lockUUID`)              |
| iOS `Lock`          | protocol: `accessStartDate`, `accessEndDate`, `doorcode`, `buildingId: String` | struct: `startTime`, `endTime`, `doorCode: String?`, `buildingID: UUID` |
| iOS `Guest`         | `uuid`, `accesses` (`deviceUUID`) | `id`, `guestAccesses` (`lockID`)                                                            |

### Method signatures (Android)

| v1                                                                                                 | v2                                                                                                  | Behavior change?                                                |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| `LatchClient.initialize(context)` + `LatchClient.setupWithToken(token, includeAllLocks).blockingGet(): SetupResult` | `client.setupWithToken(activity, token, includeAllLocks): Unit` (suspend, throws)                   | Single call. Now takes an `Activity`, not a `Context`.          |
| _(no v1 logout API)_                                                                               | `client.clear(): Unit` (suspend)                                                                    | New.                                                            |
| `LatchClient.fetchLocks(): Single<LocksResult>`                                                    | `client.fetchLocks(): List<Lock>` (suspend)                                                         | —                                                               |
| `LatchClient.locks(): Single<LocksResult>` (cache-only)                                            | **Removed.** Use `client.listenForLocks().first()`.                                                 | Removed.                                                        |
| _(no v1 stream)_                                                                                   | `client.listenForLocks(): Flow<List<Lock>>`                                                         | New.                                                            |
| `LatchClient.unlock(...): Single<UnlockResult>` (3 overloads)                                      | `client.unlock(lockId: UUID)` and `client.unlock(lock: Lock)` (suspend, throws)                     | **Outcome moved to event stream.**                              |
| `LatchClient.proximityUnlock(): Observable` + `proximityUnlockListener()`                          | `client.startProximityUnlock()` / `client.stopProximityUnlock()` + `client.listenForUnlockEvents()` | Three methods → two + stream. An explicit unlock pauses proximity and resumes it afterwards. |
| _(no v1 stream)_                                                                                   | `client.listenForUnlockEvents(): Flow<UnlockEvent>`                                                 | New.                                                            |
| `LatchClient.sync(lockUuid): Single<SyncResult>`                                                   | `client.sync(lockId: UUID)` (suspend, throws `SyncException`, `BluetoothException`, `NetworkException`) | Dedicated `SyncException`.                                  |
| `LatchClient.inviteGuests(... passcodeType: PasscodeType): Single<InviteGuestsResult>`             | `client.inviteGuest(..., lockIds: List<UUID>, inviteType: InviteType): Unit`                        | `Guest` no longer returned. Lock IDs are `UUID`s; failures are reported per lock. |
| `LatchClient.guests(): Single<GuestsResult>`                                                       | `client.guests(): List<Guest>`                                                                      | —                                                               |
| _(no v1 Android revoke)_                                                                           | `client.revokeGuestAllAccesses(guestId)` and `client.revokeGuestAccess(guestId, lockId)`            | New on Android.                                                 |
| `LatchClient.accessLogs(lockUuid): Single<AccessLogsResult>`                                       | `client.getAccessLogs(lockId): List<AccessLog>`                                                     | —                                                               |
| `LatchClient.setEnvironment(...)`                                                                  | **Removed.** No replacement.                                                                        | Removed. v2 always uses the production backend.                 |

### Method signatures (iOS)

| v1                                                            | v2                                                                                             | Behavior change?                                              |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `Latch.initialize(withToken:loadAllAccesses:)`                | `OpenDOOR.getInstance()` + `client.setupWithToken(token:includeAllLocks:)`                     | Singleton-vs-provider; lazy init is async.                    |
| _(no v1 logout API)_                                          | `client.clear()`                                                                               | New.                                                          |
| `latch.fetchLocks() -> [Lock]` (throws `FetchLocksError`)     | `client.fetchLocks() -> [Lock]` (throws `SDKError`, `NetworkError`)                            | Error type swap.                                              |
| _(no v1 stream)_                                              | `client.listenForLocks() -> AsyncStream<[Lock]>` (throws `SDKError`; `listenForLocksPublisher()` for Combine) | New.                                           |
| `latch.unlock(lockID: String)` (throws `UnlockError` 7 cases) | `client.unlock(lockID: UUID)` (throws `SDKError`, `BluetoothError`, `UnlockError`)             | UUID-typed; outcome moved to event stream.                    |
| `latch.proximityUnlockHandler` property                       | `client.listenForUnlockEvents()` (throws `SDKError`)                                           | Property gone — use stream filtered by `method = .proximity`. |
| `latch.sync(lockID: String)` (throws **`UnlockError`**)       | `client.sync(lockID: UUID)` (throws `SDKError`, `BluetoothError`, `NetworkError`, `SyncError`) | Dedicated `SyncError` (was conflated with `UnlockError`).     |
| `latch.inviteGuests(...passcodeType:...)` returns `Guest`     | `client.inviteGuest(...inviteType:...)` returns `Void`                                         | `Guest` no longer returned.                                   |
| `latch.guests() -> [Guest]`                                   | `client.guests() -> [Guest]`                                                                   | —                                                             |
| `latch.deleteGuest(guestID:)`                                 | `client.revokeGuestAllAccesses(guestID:)`                                                      | Renamed.                                                      |
| `latch.deleteGuest(guestID:, deviceID:)`                      | `client.revokeGuestAccess(guestID:, lockID:)`                                                  | Renamed; `deviceID` → `lockID`.                               |
| `latch.getAccessLogs(lockUuid:)`                              | `client.getAccessLogs(lockID:)`                                                                | —                                                             |

***

## API-by-API migration

### Setup & teardown

v2 has no separate `initialize(context)` call. `setupWithToken` does both SDK initialization and authentication; the Activity you pass carries the Application reference the SDK needs internally. `clear()` is new — v1 had no logout primitive.

```kotlin
// v1
LatchClient.initialize(context)
LatchClient.setupWithToken(token, includeAllLocks = false).blockingGet()

// v2 — one call; do not call a separate initialize
client.setupWithToken(activity, token, includeAllLocks = false)
// …later
client.clear()
```

Throws in v2: `SetupException.{InvalidTokenException, ConsentNotGrantedException, SetupInternalException}`, `NetworkException`, `IllegalArgumentException` (if the supplied Activity can't host UI).

Two gotchas. First, `setupWithToken` requires a live foreground Activity on Android — do not call it from a `Service` or background `WorkManager` worker. Second, setup doesn't survive a process restart, so keep the token in your app and call `setupWithToken` on every launch.

### Locks list

```kotlin
// v1 — manual polling
override fun onResume() {
    LatchClient.fetchLocks().subscribe { /* … */ }
}

// v2 — subscribe once, after setupWithToken succeeds
init {
    appScope.launch {
        client.listenForLocks().collect { _locks.value = it }
    }
}
```

Use `fetchLocks()` only for explicit user actions ("pull to refresh"). It does not prove the list is fresh: on a network error other than an invalid token, it returns cached locks when there are any.

### Unlock & event stream

In v1 you treated `unlock()` as a request-response RPC. In v2, the response (success, failure, cancellation) arrives on a stream. The exception thrown from `unlock()` is only the pre-flight check — Bluetooth off, lock not in cache, SDK not initialized.

Failure cases that move from `catch` to the stream (Android shape; iOS equivalents use `UnlockEvent` with `status = .canceled` or `.failed(reason)` — see [§ iOS error rename](#ios--v1--v2-error-rename)):

| v1 thrown                                | v2 stream event                                        |
| ---------------------------------------- | ------------------------------------------------------ |
| `UnlockError.concurrentUnlockInProgress` | None: a new unlock cancels the one in flight, which gets `UnlockEvent` with `status = Canceled` |
| `UnlockError.outOfSchedule`              | `UnlockEvent` with `status = Failed(reason = OutOfSchedule)` |
| `UnlockError.timeout`                    | `UnlockEvent` with `status = Failed(reason = LockNotFound)` (v2 has no `Timeout` reason) |

Failure cases that stay thrown:

| v1 thrown                       | v2 thrown                                                                                                                                |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `UnlockError.bluetoothDisabled` | `BluetoothException.BluetoothDisabledException` (Android) / `BluetoothError.disabled` (iOS)                                              |
| `UnlockError.lockNotFound(_)`   | `UnlockError.lockNotFound(_)` (iOS) / `UnlockException.LockNotFoundException` (Android), thrown before the unlock starts |

Android `UnlockEvent` is a data class: `UnlockEvent(lock: Lock?, method: UnlockEventMethod, status: UnlockEventStatus)`. `method` is `Explicit` or `Proximity`. `status` is a sealed class: `Started`, `ConnectForSetupSync(attempt)`, `SetupSync(attempt)`, `UpdateSyncPackage`, `ConnectForUnlock(attempt)`, `Unlock(attempt)`, `Failed(reason)`, `Canceled`, `Success`. `Failed` carries an `UnlockFailureReason`: `BluetoothDisabled`, `OutOfSchedule`, `LockNotFound`, `ConnectionFailed`, `AuthFailed(UnlockFailureError)`, or `Internal(UnlockFailureError)`. (`SetupSync` is new in SDK 2.1; emit a setup-sync UI state when you receive it. iOS has the same steps as `.connectForSetupSync(attempt:)` and `.setupSync(attempt:)`.)

iOS `UnlockEvent` is a struct: `UnlockEvent(lock: Lock?, method: UnlockEventMethod, status: UnlockEventStatus)`. `status` is an enum of `.started`, `.connectForSetupSync(attempt:)`, `.setupSync(attempt:)`, `.updateSyncPackage`, `.connectForUnlock(attempt:)`, `.unlock(attempt:)`, `.failed(UnlockFailureReason)`, `.canceled`, `.success`. iOS `UnlockFailureReason` cases: `.bluetoothDisabled`, `.outOfSchedule`, `.lockNotFound`, `.connectionFailed`, `.authFailed(UnlockFailureError)`, `.internal(UnlockFailureError)`.

### Proximity unlock

```kotlin
// v1
LatchClient.startProximityUnlock()
LatchClient.proximityUnlockListener().subscribe { status -> /* … */ }
// later
LatchClient.stopProximityUnlock()

// v2
client.startProximityUnlock()        // suspend on Android, sync throws on iOS — known parity gap
// later
client.stopProximityUnlock()
// proximity events arrive on listenForUnlockEvents() with method = Proximity
```

An explicit unlock pauses proximity unlock and resumes it when the explicit unlock finishes, as long as the same proximity session is still active. You don't need to call `startProximityUnlock()` again.

### Sync

```swift
// v1 iOS
do {
    try await latch.sync(lockID: id)
} catch let e as UnlockError { /* … */ }   // ← UnlockError was reused for sync

// v2 iOS
do {
    try await client.sync(lockID: id)
} catch let e as SyncError { /* dedicated type now */ }
```

Android `SyncException` cases: `LockNotFoundException`, `CanceledException`, `UnlockInProgressException`, `SyncInternalException`. iOS `SyncError` cases: `.lockNotFound(String)`, `.canceled`, `.unlockInProgress`, `.syncInternalError(String)`.

### Guest invitations

The v1 `passcodeType` argument splits into two types that implement `InviteType`:

| Use when…                                          | Constructor               | Required fields                                                         |
| -------------------------------------------------- | ------------------------- | ----------------------------------------------------------------------- |
| Guest is in the Door ecosystem and accepts in-app  | `InAppInvite`             | `startTime`, `endTime?` (null = permanent)                              |
| Guest is _not_ in the ecosystem; one-shot doorcode | `TemporaryDoorcodeInvite` | `duration` (`Limit15Minutes` / `FullDay`), `period` (`Today` / `Tomorrow`) |

Two non-obvious changes beyond the type swap:

1. The return type is `Unit` / `Void`. v1 returned the created `Guest`. To read it back, call `guests()` after the invite resolves.
2. One call still invites to multiple locks, now as `lockIds: List<UUID>` (Android) / `lockIDs: [UUID]` (iOS) instead of ID strings. Per-lock partial failures surface as `GuestInvitesException` / `GuestInvitesError`, which carries a per-lock outcome list — render that list, don't blanket-fail the operation.

### Guest listing & revocation

iOS rename:

```swift
// v1
try await latch.deleteGuest(guestID: id)
try await latch.deleteGuest(guestID: id, deviceID: deviceId)

// v2
try await client.revokeGuestAllAccesses(guestID: id)
try await client.revokeGuestAccess(guestID: id, lockID: lockId)
```

On Android, revoke is new in v2 — v1 had no public revoke API. If your Android app round-tripped through your own backend to revoke, switch to the SDK calls.

### Access logs

iOS `LatchAccessLog` → `AccessLog`. Android signature shape changes from sealed result to direct list. `AccessLogMethod` enum cases now match across iOS and Android in v2 — drop any per-platform translation layer you maintained for shared analytics.

***

## Error model: v1 → v2 mapping

### Android — v1 sealed `*Result` → v2 typed exceptions

| v1 outcome                                                                   | v2                                                                                    |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `*Result.Success(data)`                                                      | return value of the `suspend` call                                                    |
| `*Result.NotInitialized`                                                     | `SDKException.SDKNotInitializedException`                                             |
| `LocksResult.Error` / `GuestsResult.NetworkError` / `AccessLogsResult.NetworkError` | `NetworkException.{InvalidTokenException, InternalNetworkException, PayloadError}` |
| `SetupResult.InvalidToken`                                                   | `SetupException.InvalidTokenException`                                                |
| `SetupResult.UserConsentDenied`                                              | `SetupException.ConsentNotGrantedException`                                           |
| `SetupResult.Error`                                                          | `SetupException.SetupInternalException` / `NetworkException`                          |
| `UnlockResult.Success` / `OutOfSchedule` / `InternalError`                   | `UnlockEvent` with `status = Success` / `Failed(reason)` (stream)                     |
| `UnlockResult.BleDisabled`                                                   | `BluetoothException.BluetoothDisabledException` (thrown pre-flight)                   |
| `SyncResult.LockNotFound`                                                    | `SyncException.LockNotFoundException` (`CanceledException` and `UnlockInProgressException` are new) |
| `SyncResult.InternalError`                                                   | `SyncException.SyncInternalException` / `NetworkException`                            |
| `InviteGuestsResult.NetworkError(...)` / `InternalError`                     | `GuestInvitesException` (per-lock outcome list; a per-lock error can be an `InviteGuestException`) / `NetworkException` |

### iOS — v1 → v2 error rename

| v1 (iOS)                                     | v2 (iOS)                                                                             |
| -------------------------------------------- | ------------------------------------------------------------------------------------ |
| `FetchLocksError.invalidToken`               | `NetworkError.invalidToken`                                                          |
| `FetchLocksError.internalError(_, _)`        | `NetworkError.internalNetworkError(_)`                                               |
| `UnlockError.bluetoothDisabled`              | `BluetoothError.disabled`                                                            |
| `UnlockError.concurrentUnlockInProgress`     | None: a new unlock cancels the one in flight, which gets `status = .canceled` (stream) |
| `UnlockError.lockNotFound(_)`                | `UnlockError.lockNotFound(_)` (still thrown)                                         |
| `UnlockError.outOfSchedule` / `.timeout`     | `UnlockEvent` with `status = .failed(.outOfSchedule)` / `.failed(.lockNotFound)` or `.failed(.connectionFailed)` (stream) |
| `DeleteGuestError.passcodeTypeCantBeRevoked` | `RevokeGuestError.passcodeTypeCantBeRevoked`                                         |
| `DeleteGuestError.deviceNotFound`            | `RevokeGuestError.deviceNotFound`                                                    |
| `InviteGuestError.*`                         | `InviteGuestError.*` (same 7 cases, plus `.shareableAccessRequired`, `.sharingNotEnabled`, `.requestedTimeOutsideShareableAccess`), now per lock inside `GuestInvitesError.failedLockErrors` |
| `ConsentError.userConsentDenied`             | `SetupError.consentNotGranted`                                                       |

***

## What v2 removed

| Removed                                               | Replacement                                                                                          |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Android `LatchClient.locks(): Single<LocksResult>`    | `client.listenForLocks().first()`                                                                    |
| Android `LatchClient.proximityUnlock(): Observable`   | `client.startProximityUnlock()` + `client.listenForUnlockEvents().filter { it.method == Proximity }` |
| Android `proximityUnlockListener()`                   | `client.listenForUnlockEvents(listener)`                                                             |
| iOS `Latch.proximityUnlockHandler` property           | `client.listenForUnlockEvents()`                                                                     |
| Android `InitResult` (deprecated in late v1)          | gone — `setupWithToken` either returns or throws                                                     |
| Runtime environment switching (`setEnvironment(...)`) | None. v2 always uses the production backend.                                                         |
| GitHub-repo artifact channel                          | Maven (Android) / SPM (iOS) — see [Step 1](#step-1--swap-the-dependency)                             |

***

## See also

* [Android SDK tutorial](https://developers.door.com/docs/android-docs)
* [iOS SDK docs](https://developers.door.com/docs/ios-docs)
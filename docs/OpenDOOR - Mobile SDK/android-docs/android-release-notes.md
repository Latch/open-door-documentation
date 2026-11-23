---
title: Release notes
excerpt: Android SDK release notes
deprecated: false
hidden: false
metadata:
  robots: index
---
## What's new in SDK 2.3.1

**Requirements**

- ⚠️ **Breaking change:** 2.3.1 has new build requirements.
  - Turn on core library desugaring in your app module: set `isCoreLibraryDesugaringEnabled = true` in `compileOptions` and add `coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:2.0.4")` to `dependencies`.
  - Use Kotlin 2.1.0 or newer. Older Kotlin versions fail with "Module was compiled with an incompatible version of Kotlin".
  - Build with JDK 17 or newer. The SDK now targets Java 17.
  - minSdk 26 and compileSdk 35 or newer are unchanged.
- **Dependency updates.** The SDK now depends on newer versions of these libraries. If your app also uses them, check that your app works with these versions.
  - `org.jetbrains.kotlin:kotlin-stdlib` 2.1.0 → 2.2.20
  - `org.jetbrains.kotlinx:kotlinx-coroutines-android` and `kotlinx-coroutines-rx2` 1.8.1 → 1.10.2
  - `com.google.code.gson:gson` 2.8.9 → 2.10.1
  - `com.polidea.rxandroidble2:rxandroidble` 1.13.1 → 1.17.2
  - `net.zetetic:sqlcipher-android` 4.10.0 → 4.17.0

**New Features**

- **Remote unlock.** Unlock a door over the network through its intercom or a Door Scout. No Bluetooth is needed.
  - `Lock.remoteUnlockMethods` lists the `RemoteUnlockMethod` values the lock supports: `INTERCOM` and `DOOR_SCOUT`. It's empty when the lock supports neither.
  - `remoteUnlock(lockId, method)` starts the unlock and returns when it ends. Progress and the result arrive through `listenForUnlockEvents`: `Started`, then `Success` or `Failed`. These events carry the new `UnlockEventMethod` values `RemoteIntercom` and `RemoteDoorScout`.
  - A remote unlock runs separately from Bluetooth unlocks. `cancelUnlock()` doesn't stop it, and neither does cancelling the coroutine that called `remoteUnlock`. A second call for the same lock while one is running does nothing.
  - `remoteUnlock` throws `UnlockException.LockNotFoundException` for an unknown lock, and the new `UnlockException.RemoteUnlockNotSupportedException` when the lock doesn't support the method.
  - The new failure reason `UnlockFailureReason.RemoteUnlockNotAllowed` means the user can't unlock this door remotely. Other remote unlock failures are `Internal`, with a new `UnlockFailureCode`:
    - `REMOTE_UNLOCK_IN_PROGRESS`: a remote unlock of this door is already running.
    - `REMOTE_UNLOCK_FAILED`: the door reported that the unlock failed.
    - `REMOTE_UNLOCK_TIMED_OUT`: no result arrived within 20 seconds for an intercom, or 60 seconds for a Door Scout. The door may still open.
    - `NETWORK_ERROR`: the request failed. `context` holds the HTTP status when there is one.
  - ⚠️ **Breaking change:** `UnlockEventMethod`, `UnlockFailureCode`, `UnlockFailureReason` and `UnlockException` have new values. Add the new cases, or an `else` branch, to every exhaustive `when` over them.
- **Intercom call settings.** `getIntercomSettings()` returns one `IntercomSettings` per building the user lives in, with `buildingId`, `contactPreference` (`APP`, `PHONE` or `UNIT`) and `phoneNumber`. It returns an empty list when there are none.
  - `enableIntercomPhoneCalls(buildingId)` opts the user in to intercom calls by phone for one building and returns the updated settings. Pass `Lock.buildingId`.
  - It throws the new `IntercomSettingsException.NoPhoneNumberException` when the user has no phone number on file.
  - Opting out is only available in the DOOR App.
- **Lock timezone.** `Lock.timeZone` is the lock's IANA timezone, for example `Europe/Rome`. When DOOR has no timezone for the lock, it's the phone's timezone.
  - ⚠️ **Breaking change:** `Lock` has two new required constructor parameters, `timeZone` and `remoteUnlockMethods`. If your code creates `Lock` objects, for example in tests, pass both, such as `ZoneId.systemDefault().id` and `emptyList()`.

**Improvements**

- **Bluetooth errors are thrown before an unlock starts.** `unlock()`, `startProximityUnlock()` and `sync()` now throw `BluetoothException.BluetoothDisabledException` when Bluetooth is off, and `BluetoothException.BluetoothPermissionDeniedException` when the Bluetooth permission is missing (Nearby devices on Android 12 and newer, precise location on older versions).
  - ⚠️ **Breaking change:** With Bluetooth off, `unlock()` used to return and report `Failed(BluetoothDisabled)` on the event stream. Now `unlock()` and `startProximityUnlock()` throw and emit no unlock event. Catch `BluetoothException`, and call `startProximityUnlock()` again once Bluetooth is on. Bluetooth turning off during an unlock still ends in `Failed(BluetoothDisabled)`.
- **The consent prompt names DOOR.** It reads "By proceeding, I agree to DOOR's Terms of Service and Privacy Policy." Its links are "Terms of Service" and "Privacy Policy", and they open https://door.com/terms-of-service and https://door.com/privacy.

**Bug Fixes**

- Calling the SDK before `setupWithToken` in a new app process now throws `SDKException.SDKNotInitializedException`, as documented. Before, some calls threw `UninitializedPropertyAccessException`, which isn't an `SDKException`, and others threw `SDKException.InternalException`. `listenForUnlockEvents(listener)` now also throws it before setup and after `clear()`, like `listenForLocks(listener)`. Call `setupWithToken` on every app launch before other SDK calls.
- If the user denies the Bluetooth permission during `setupWithToken`, setup now completes. Locks, guests and access logs work, and the Bluetooth calls throw `BluetoothPermissionDeniedException`. Before, setup returned without loading the user's locks.
- Back or a tap outside the consent prompt no longer closes it without an answer, which left `setupWithToken` waiting. The user has to tap Agree or Disagree.
- Temporary doorcode invites now pick Today and Tomorrow in the lock's timezone, not the phone's. Before, a phone ahead of the lock could get a Tomorrow code that already worked today at the lock. When DOOR has no timezone for the lock, the phone's timezone is still used. For several locks, the first lock in `lockIds` with a timezone sets the day. App access (`InAppInvite`) still uses the exact start and end times you pass.

## What's new in SDK 2.3.0

**New Features**

- **Richer unlock progress events.** Unlock events now report each phase of an unlock (connecting, setup sync, sync package update, unlock) and whether it is the first or the recovery attempt, so your app can show accurate progress.
  - ⚠️ **Breaking change:** Unlock events and failure reasons are reshaped.
    - `UnlockEvent` is now a single type carrying the `Lock`, the unlock `method` and a `status`. It replaces the separate event subclasses (`UnlockStarted`, `SetupSync`, `UnlockFailed`, `UnlockCanceled`, `UnlockSuccess`).
    - New `UnlockEventStatus` values: `Started`, `ConnectForSetupSync`, `SetupSync`, `UpdateSyncPackage`, `ConnectForUnlock`, `Unlock`, `Failed`, `Canceled` and `Success`. The phased ones carry an `UnlockAttempt` (`First` or `Second`).
    - `UnlockFailureReason` is now a closed set: `BluetoothDisabled`, `OutOfSchedule`, `LockNotFound`, `ConnectionFailed`, `AuthFailed` and `Internal(code)`. `BluetoothError`, `Timeout`, `LockNotRecognized` and `InternalError` are removed. The specific cause is kept in the `code` of `Internal`.
    - `LocksListener.onError` is removed. Lock updates are now update-only.
  - Replace handling of the old event subclasses with a `when` over `event.status`, and update any `when` over the failure reasons.
- **Listener control.** `stopListenForLocks` and `stopListenForUnlockEvents` detach a listener synchronously.
- **Log level control.** `setLogLevel` (`DEBUG` or `ERROR`) sets SDK logging verbosity. You can call it before or after setup.
- **More access log results.** `AccessLogResult` adds `GUEST_SUCCESS` and `UNKNOWN_TIME_FAILURE`.

**Improvements**

- **More predictable Lock fetching.** `fetchLocks` always throws an invalid-token error for an invalid or expired token, even when cached Locks exist. For other network failures it returns cached Locks when available, and throws a network error when the cache is empty.
- **More predictable Lock listening.** `listenForLocks` emits cached state first, including an empty list, then refreshes in the background. Refresh failures are logged and are not delivered to your listener.
- **Clearer guest invite errors.** Sharing failures now say what to do, for example "User does not have permission to share access. Make sure the access was granted by the partner and is shareable." The new `SHAREABLE_ACCESS_REQUIRED`, `SHARING_NOT_ENABLED` and `REQUESTED_TIME_OUTSIDE_SHAREABLE_ACCESS` reasons on `InviteGuestException` describe why an invite was rejected. Guest invite and Lock action errors also include the lock IDs, counts and causes in their messages.
- **Safer proximity and explicit unlock handling.** An explicit unlock pauses proximity scanning. Scanning resumes afterward only if the same proximity session is still active. Calling `stopProximityUnlock` during an explicit unlock leaves the unlock running and keeps scanning stopped. Proximity unlock targets the closest eligible Lock within the SDK's range threshold, which was increased in 2.1.
- **Lock refresh also refreshes the data locks need for unlocking,** and retries failed refreshes.
- **Guest revocation** attempts every applicable revocation before reporting a single failure.
- **Dependency changes.** The SDK no longer bundles Datadog, and RxJava, RxAndroid and Koin are no longer exposed through the SDK's public dependencies. Add them to your app if you relied on them. Release builds no longer log HTTP request or response bodies, and the `Authorization` header is redacted in debug logs.

**Bug Fixes**

- Unlocks no longer fail on some Locks because of a mis-decoded signature. Previously about 1 in 120 attempts could be rejected with a Lock authentication error.
- Connection failures during unlock are retried more reliably. The SDK keeps the known Lock address and retries for up to 9 seconds before reporting a Bluetooth failure, instead of giving up after two retries.
- Locks that don't report `isShareable` are now treated as shareable.
- `InAppInvite` with an end time no longer fails because of an unsupported passcode type.
- A failed second unlock attempt now emits one final event. Cancelling an unlock no longer leaves the SDK in a busy state.
- A Lock rejecting an unlock with a granular authentication code is now reported as `AuthFailed` and not as a generic error.

## What's new in SDK 2.2.0

New Features

* Redesigned unlock event model with a full lifecycle. UnlockEvent is now a single type carrying the affected Lock, the unlock method, and a granular UnlockStatus. The lifecycle exposes every stage of an unlock — Started, ConnectForSetupSync, SetupSync, UpdateSyncPackage, ConnectForUnlock, Unlock, Failed, Canceled, and Success — and connect/sync/unlock stages report which UnlockAttempt they belong to (First or Second), so you can drive precise UI for the entire flow.
  * UnlockEvent changed from a sealed hierarchy (UnlockStarted, SetupSync, UnlockFailed, UnlockCanceled, UnlockSuccess, each exposing lockId: UUID?) to a single data class UnlockEvent(lock: Lock?, method: UnlockEventMethod, status: UnlockStatus). Code that pattern-matched the old subclasses or read lockId must migrate to reading status and lock.
* Richer, structured unlock failure reasons. UnlockFailureReason is now a sealed type that distinguishes the actual cause of a failed unlock, including new AuthFailed and ConnectionFailed cases and an Internal(code: String) case that surfaces a diagnostic code.
  * UnlockFailureReason changed from an enum to a sealed class. The old values BluetoothError, LockNotRecognized, Timeout, and InternalError were removed or folded into the new cases (ConnectionFailed, Internal(code)). Update exhaustive when statements accordingly.
* Stop-listening APIs. DoorClient now offers stopListenForLocks(listener) and stopListenForUnlockEvents(listener), so you can deregister observers symmetrically and avoid leaking listeners across screen lifecycles.
* Runtime log-level control. A new LogLevel enum (DEBUG, ERROR) and DoorClient.setLogLevel(level) let you adjust SDK logging verbosity at runtime

Improvements

* More reliable lock synchronization. The data locks need for unlocking now refreshes automatically after transient network errors and whenever you fetch the latest locks, so unlocks stay ready without a separate call.
* More precise guest-revocation and access-log results. Revoking a guest now reports a DEVICE_NOT_FOUND reason and preserves the underlying error message instead of collapsing to a generic network error, and the access-log result set gained GUEST_SUCCESS and UNKNOWN_TIME_FAILURE.

Bug Fixes

* In-app guest invites with an expiration time are no longer rejected. Sending an in-app invite with an end time previously failed with a server validation error because it was sent as a recurring (daily) credential. In-app invites are now always issued as a non-recurring credential that accepts an optional end time.
* Setup no longer crashes when the SDK's stored data can't be read, for example after a credential reset or device restore. The SDK now resets its stored data and retries automatically.
* A failed unlock now recovers on its own: an authentication failure or a stale setup transparently triggers a fresh sync-package download and setup, followed by a single retry, before reporting failure. Connection, setup, and unlock stages each have dedicated timeouts so a stalled lock fails fast instead of hanging.

## What's new in SDK 2.1.1

* **New modern API:** coroutine-first `suspend` functions, Flow listeners, callback listeners, and Activity-based setup for permission and consent UI.
* **Improved unlock:** explicit and proximity unlocks now share the same unlock event stream, with clearer progress, success, failure, and cancellation events.
* **Setup sync visibility during unlock:** `UnlockEvent.SetupSync` is emitted when the SDK needs to run setup sync before unlocking, such as the first time a user opens a door and the lock needs access data.
* **Unlock cancellation:** `cancelUnlock()` cancels the active explicit unlock or the current proximity unlock attempt and emits `UnlockEvent.UnlockCanceled`.
* **Increased proximity unlock range:** proximity unlock now supports a larger BLE trigger range than earlier SDK 2.0 builds while still selecting the closest eligible lock.
* **Finer-grained log levels**

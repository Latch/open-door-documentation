---
title: DoorClient
excerpt: Public OpenDOOR SDK Core Module.
hidden: true
---

*Package `com.door.opendoor.android.core.api`*

```kotlin
interface DoorClient
```

Public OpenDOOR SDK Core Module.

## Functions

| Name | Summary |
|---|---|
| cancelUnlock | abstract suspend fun cancelUnlock()<br>Cancels the active unlock attempt, if any. |
| clear | abstract suspend fun clear()<br>Clears SDK state and authentication. |
| fetchLocks | abstract suspend fun fetchLocks(): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[Lock](doc:android-ref-lock)&gt;<br>Fetches the current user's locks. |
| getAccessLogs | abstract suspend fun getAccessLogs(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[AccessLog](doc:android-ref-accesslog)&gt;<br>Retrieves access logs for a lock. |
| guests | abstract suspend fun guests(): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[Guest](doc:android-ref-guest)&gt;<br>Retrieves all guests with shared access, combining legacy and Blueprint invitations. |
| inviteGuest | abstract suspend fun inviteGuest(firstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), lastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), email: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, phone: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, lockIds: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)&gt;, inviteType: [InviteType](doc:android-ref-invitetype))<br>Grants a guest access to the requested locks. |
| listenForLocks | abstract fun listenForLocks(): Flow&lt;[List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[Lock](doc:android-ref-lock)&gt;&gt;<br>Returns an update-only stream of lock lists.<br>abstract fun listenForLocks(listener: [LocksListener](doc:android-ref-lockslistener))<br>Callback variant of listenForLocks. |
| listenForUnlockEvents | abstract fun listenForUnlockEvents(): Flow&lt;[UnlockEvent](doc:android-ref-unlockevent)&gt;<br>Returns unlock lifecycle events from explicit and proximity unlocks.<br>abstract fun listenForUnlockEvents(listener: [UnlockEventsListener](doc:android-ref-unlockeventslistener))<br>Callback variant of listenForUnlockEvents. |
| revokeGuestAccess | abstract suspend fun revokeGuestAccess(guestId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html))<br>Revokes one guest access. |
| revokeGuestAllAccesses | abstract suspend fun revokeGuestAllAccesses(guestId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html))<br>Revokes every access of a guest. |
| setLogLevel | abstract fun setLogLevel(level: [LogLevel](doc:android-ref-loglevel))<br>Sets the minimum SDK logging level. |
| setupWithToken | abstract suspend fun setupWithToken(activity: [Activity](https://developer.android.com/reference/kotlin/android/app/Activity.html), token: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), includeAllLocks: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html))<br>Authenticates and initializes the SDK. |
| startProximityUnlock | abstract suspend fun startProximityUnlock()<br>Starts proximity unlock scanning. |
| stopListenForLocks | abstract fun stopListenForLocks(listener: [LocksListener](doc:android-ref-lockslistener))<br>Stops delivering lock updates to the listener. |
| stopListenForUnlockEvents | abstract fun stopListenForUnlockEvents(listener: [UnlockEventsListener](doc:android-ref-unlockeventslistener))<br>Stops delivering unlock events to the listener. |
| stopProximityUnlock | abstract suspend fun stopProximityUnlock()<br>Stops proximity unlock scanning. |
| sync | abstract suspend fun sync(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html))<br>Runs active sync for a lock. |
| unlock | abstract suspend fun unlock(lock: [Lock](doc:android-ref-lock))<br>Android convenience overload accepting a current Lock model.<br>abstract suspend fun unlock(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html))<br>Starts an explicit unlock for the lock with the given identifier. |

## Details

### `cancelUnlock`

```kotlin
abstract suspend fun cancelUnlock()
```

Cancels the active unlock attempt, if any.

Emits an UnlockEvent with status Canceled for an in-flight attempt and completes silently otherwise. Proximity mode stays enabled; use stopProximityUnlock to disable it.

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |

### `clear`

```kotlin
abstract suspend fun clear()
```

Clears SDK state and authentication.

Deletes cached data and removes the stored token. After clear the client must be set up again with setupWithToken.

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if clearing state fails internally. |

### `fetchLocks`

```kotlin
abstract suspend fun fetchLocks(): List<Lock>
```

Fetches the current user's locks.

Refreshes locks from the network and updates the cache. An invalid or expired token always fails, even when cached locks exist. Other network failures return cached locks when available and fail only when the cache is empty.

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |
| [NetworkException](doc:android-ref-networkexception) | if the token is invalid or expired, and on other network failures only when the cache is empty. |

### `getAccessLogs`

```kotlin
abstract suspend fun getAccessLogs(lockId: UUID): List<AccessLog>
```

Retrieves access logs for a lock.

###### Parameters


| | |
|---|---|
| lockId | Identifier of the lock. |

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |
| [NetworkException](doc:android-ref-networkexception) | if the request fails or the token is invalid. |

### `guests`

```kotlin
abstract suspend fun guests(): List<Guest>
```

Retrieves all guests with shared access, combining legacy and Blueprint invitations.

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |
| [NetworkException](doc:android-ref-networkexception) | if fetching guests fails. |

### `inviteGuest`

```kotlin
abstract suspend fun inviteGuest(firstName: String, lastName: String, email: String?, phone: String?, lockIds: List<UUID>, inviteType: InviteType)
```

Grants a guest access to the requested locks.

Routes each lock to the legacy or Blueprint invite API based on its building type. For Blueprint invites the firstName parameter carries the user UUID.

###### Parameters


| | |
|---|---|
| firstName | First name of the guest, or the user UUID for Blueprint invites. |
| lastName | Last name of the guest. |
| email | Email of the guest; required for permanent invites. |
| phone | Phone number; legacy invites need email or phone. |
| lockIds | Locks to grant access to. |
| inviteType | Invite settings, InAppInvite or TemporaryDoorcodeInvite. |

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |
| [NetworkException](doc:android-ref-networkexception) | if the token is invalid or expired. |
| [GuestInvitesException](doc:android-ref-guestinvitesexception) | with per-lock results when any invite operation fails. |

### `listenForLocks`

```kotlin
abstract fun listenForLocks(): Flow<List<Lock>>
```

Returns an update-only stream of lock lists.

Initialization is checked when the stream is created. The stream emits cached state, including an empty list, and subsequent updates, and starts a best-effort refresh. Later refresh and observation failures are logged internally; the stream has no error channel.

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |

```kotlin
abstract fun listenForLocks(listener: LocksListener)
```

Callback variant of listenForLocks.

Initialization is checked before the listener is registered. Cached state, including an empty list, and subsequent updates are delivered through the listener; no error callback is provided.

###### Parameters


| | |
|---|---|
| listener | Listener receiving lock updates. |

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |

### `listenForUnlockEvents`

```kotlin
abstract fun listenForUnlockEvents(): Flow<UnlockEvent>
```

Returns unlock lifecycle events from explicit and proximity unlocks.

Carries progress and result events for every unlock operation. Handle status SetupSync to show progress when a first-time setup sync is required, and Canceled to react to cancelUnlock.

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |

```kotlin
abstract fun listenForUnlockEvents(listener: UnlockEventsListener)
```

Callback variant of listenForUnlockEvents.

Events are delivered through the listener; no error callback is provided.

###### Parameters


| | |
|---|---|
| listener | Listener receiving unlock events. |

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |

### `revokeGuestAccess`

```kotlin
abstract suspend fun revokeGuestAccess(guestId: UUID, lockId: UUID)
```

Revokes one guest access.

The lock identifier maps to the backend's device identifier.

###### Parameters


| | |
|---|---|
| guestId | Identifier of the guest whose access is revoked. |
| lockId | Identifier of the lock to revoke access to. |

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |
| [NetworkException](doc:android-ref-networkexception) | if the request fails or the token is invalid. |
| [RevokeGuestException](doc:android-ref-revokeguestexception) | if the passcode type cannot be revoked or the revocation fails. |

### `revokeGuestAllAccesses`

```kotlin
abstract suspend fun revokeGuestAllAccesses(guestId: UUID)
```

Revokes every access of a guest.

Attempts one bulk legacy revocation plus each distinct Blueprint assignment. Cancellation stops immediately; otherwise every operation is attempted and the first selected failure is reported, preferring invalid-token, revoke, network, then internal errors. Per-access results are not returned.

###### Parameters


| | |
|---|---|
| guestId | Identifier of the guest whose accesses are revoked. |

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |
| [NetworkException](doc:android-ref-networkexception) | if the token is invalid or expired. |
| [RevokeGuestException](doc:android-ref-revokeguestexception) | if the passcode type cannot be revoked or a revocation fails. |

### `setLogLevel`

```kotlin
abstract fun setLogLevel(level: LogLevel)
```

Sets the minimum SDK logging level.

DEBUG produces detailed output; ERROR restricts logs to important issues. Safe to call before setupWithToken.

###### Parameters


| | |
|---|---|
| level | Minimum log level that is recorded. |

### `setupWithToken`

```kotlin
abstract suspend fun setupWithToken(activity: Activity, token: String, includeAllLocks: Boolean)
```

Authenticates and initializes the SDK.

Initializes storage and network clients, then authenticates with the token. If the token's user differs from the stored user, all cached data is deleted first. The token is kept in memory only and never persisted. The includeAllLocks flag is stored and applied whenever locks are retrieved.

###### Parameters


| | |
|---|---|
| activity | Foreground Activity that can host setup UI. |
| token | User authentication token. |
| includeAllLocks | Whether non-partner locks are included. |

###### Throws

| | |
|---|---|
| [SetupException](doc:android-ref-setupexception) | if the token is invalid, consent is not granted, or setup fails internally. |
| [NetworkException](doc:android-ref-networkexception) | if no user is stored and the configuration cannot be fetched. |
| [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html) | if the Activity cannot host setup UI. |

### `startProximityUnlock`

```kotlin
abstract suspend fun startProximityUnlock()
```

Starts proximity unlock scanning.

Scans for nearby locks and automatically unlocks the closest eligible lock within the SDK's BLE range threshold.

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |
| [BluetoothException](doc:android-ref-bluetoothexception) | if Bluetooth is disabled or permissions are missing. |

### `stopListenForLocks`

```kotlin
abstract fun stopListenForLocks(listener: LocksListener)
```

Stops delivering lock updates to the listener.

The listener is detached before this method returns; calling with an unregistered listener is a no-op. One in-flight update that began before detachment may still complete.

###### Parameters


| | |
|---|---|
| listener | Listener to detach. |

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |

### `stopListenForUnlockEvents`

```kotlin
abstract fun stopListenForUnlockEvents(listener: UnlockEventsListener)
```

Stops delivering unlock events to the listener.

The listener is detached before this method returns; calling with an unregistered listener is a no-op. One in-flight event that began before detachment may still complete.

###### Parameters


| | |
|---|---|
| listener | Listener to detach. |

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |

### `stopProximityUnlock`

```kotlin
abstract suspend fun stopProximityUnlock()
```

Stops proximity unlock scanning.

If an explicit unlock has paused scanning, that unlock keeps running and scanning does not resume after it finishes.

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |

### `sync`

```kotlin
abstract suspend fun sync(lockId: UUID)
```

Runs active sync for a lock.

Synchronizes lock data with the backend and returns when the sync finishes.

###### Parameters


| | |
|---|---|
| lockId | Identifier of the lock to sync. |

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |
| [BluetoothException](doc:android-ref-bluetoothexception) | if Bluetooth is disabled or permissions are missing. |
| [NetworkException](doc:android-ref-networkexception) | if the sync packages cannot be fetched. |
| [SyncException](doc:android-ref-syncexception) | if the sync is canceled, an unlock is in progress, or syncing fails internally. |

### `unlock`

```kotlin
abstract suspend fun unlock(lockId: UUID)
```

Starts an explicit unlock for the lock with the given identifier.

Fails before any Bluetooth work when the identifier does not match a known lock. If proximity unlock is active, its current attempt and scan are paused; scanning resumes after this unlock finishes only while the same proximity session is still active. If the lock needs a setup sync first, an UnlockEvent with status SetupSync is emitted through listenForUnlockEvents.

###### Parameters


| | |
|---|---|
| lockId | Identifier of the lock to unlock. |

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |
| [BluetoothException](doc:android-ref-bluetoothexception) | if Bluetooth is disabled or permissions are missing. |
| [UnlockException](doc:android-ref-unlockexception) | if the identifier does not match a known lock. |

```kotlin
abstract suspend fun unlock(lock: Lock)
```

Android convenience overload accepting a current Lock model.

The lock is validated against the cache before Bluetooth work; a stale or unknown model emits an unlock failure event. Proximity pause and resume behave as in the identifier overload.

###### Parameters


| | |
|---|---|
| lock | Current lock model to unlock. |

###### Throws

| | |
|---|---|
| [SDKException](doc:android-ref-sdkexception) | if the SDK is not initialized. |
| [BluetoothException](doc:android-ref-bluetoothexception) | if Bluetooth is disabled or permissions are missing. |
| [UnlockException](doc:android-ref-unlockexception) | if the lock is not recognized. |

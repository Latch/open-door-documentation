---
title: DoorClient
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Public OpenDOOR SDK Core Module.

Setup flow:

1. Call setupWithToken() with a valid token to authenticate.
2. Use listenForLocks() or fetchLocks() to retrieve lock data.
3. Listen for unlock events, including setup sync progress, while unlocking.
4. Use unlock() or proximity unlock as needed.

## Declaration

```kotlin
interface DoorClient {
    suspend fun cancelUnlock()
    suspend fun clear()
    suspend fun enableIntercomPhoneCalls(buildingId: UUID): IntercomSettings
    suspend fun fetchLocks(): List<Lock>
    suspend fun getAccessLogs(lockId: UUID): List<AccessLog>
    suspend fun getIntercomSettings(): List<IntercomSettings>
    suspend fun guests(): List<Guest>
    suspend fun inviteGuest(firstName: String, lastName: String, email: String?, phone: String?, lockIds: List<UUID>, inviteType: InviteType)
    fun listenForLocks(): Flow<List<Lock>>
    fun listenForLocks(listener: LocksListener)
    fun listenForUnlockEvents(): Flow<UnlockEvent>
    fun listenForUnlockEvents(listener: UnlockEventsListener)
    suspend fun remoteUnlock(lockId: UUID, method: RemoteUnlockMethod)
    suspend fun revokeGuestAccess(guestId: UUID, lockId: UUID)
    suspend fun revokeGuestAllAccesses(guestId: UUID)
    fun setLogLevel(level: LogLevel)
    suspend fun setupWithToken(activity: Activity, token: String, includeAllLocks: Boolean)
    suspend fun startProximityUnlock()
    fun stopListenForLocks(listener: LocksListener)
    fun stopListenForUnlockEvents(listener: UnlockEventsListener)
    suspend fun stopProximityUnlock()
    suspend fun sync(lockId: UUID)
    suspend fun unlock(lockId: UUID)
    suspend fun unlock(lock: Lock)
}
```

## cancelUnlock()

Cancels the active unlock attempt, if any.

Emits an UnlockEvent with status Canceled for an in-flight attempt and completes silently otherwise. Proximity mode stays enabled; use stopProximityUnlock to disable it.

- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.

## clear()

Clears SDK state and authentication.

Deletes cached data and removes the stored token. After clear the client must be set up again with setupWithToken.

- **Throws:** [SDKException](doc:android-ref-sdkexception) if clearing state fails internally.

## enableIntercomPhoneCalls(buildingId)

Opts the user in to intercom calls by phone for one building.

Only the given building changes. Opting out is only available in the DOOR App.

- **`buildingId`** — Identifier of the building, as found on Lock.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [NetworkException](doc:android-ref-networkexception) if the request fails or the token is invalid.
- **Throws:** [IntercomSettingsException](doc:android-ref-intercomsettingsexception) if the user has no phone number on file.

## fetchLocks()

Fetches the current user's locks.

Refreshes locks from the network and updates the cache. An invalid or expired token always fails, even when cached locks exist. Other network failures return cached locks when available and fail only when the cache is empty.

- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [NetworkException](doc:android-ref-networkexception) if the token is invalid or expired, and on other network failures only when the cache is empty.

## getAccessLogs(lockId)

Retrieves access logs for a lock.

- **`lockId`** — Identifier of the lock.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [NetworkException](doc:android-ref-networkexception) if the request fails or the token is invalid.

## getIntercomSettings()

Retrieves the user's intercom call settings.

Returns one entry per building the user lives in, or an empty list when there are none.

- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [NetworkException](doc:android-ref-networkexception) if the request fails or the token is invalid.

## guests()

Retrieves all guests with shared access.

- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [NetworkException](doc:android-ref-networkexception) if fetching guests fails.

## inviteGuest(firstName, lastName, email, phone, lockIds, inviteType)

Grants a guest access to the requested locks.

- **`firstName`** — First name of the guest.
- **`lastName`** — Last name of the guest.
- **`email`** — Email of the guest; required for permanent invites.
- **`phone`** — Phone number of the guest; a temporary doorcode invite needs an email or a phone.
- **`lockIds`** — Locks to grant access to.
- **`inviteType`** — Invite settings, InAppInvite or TemporaryDoorcodeInvite.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [NetworkException](doc:android-ref-networkexception) if the token is invalid or expired.
- **Throws:** [GuestInvitesException](doc:android-ref-guestinvitesexception) with per-lock results when any invite operation fails.

## listenForLocks()

Returns an update-only stream of lock lists.

Initialization is checked when the stream is created. The stream emits cached state, including an empty list, and subsequent updates, and starts a best-effort refresh. Later refresh failures aren't reported; the stream has no error channel.

- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.

## listenForLocks(listener)

Callback variant of listenForLocks.

Initialization is checked before the listener is registered. Cached state, including an empty list, and subsequent updates are delivered through the listener; no error callback is provided.

- **`listener`** — Listener receiving lock updates.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.

## listenForUnlockEvents()

Returns unlock lifecycle events from explicit, proximity and remote unlocks.

Carries progress and result events for every unlock operation. Handle status SetupSync to show progress when a first-time setup sync is required, and Canceled to react to cancelUnlock.

- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.

## listenForUnlockEvents(listener)

Callback variant of listenForUnlockEvents.

Events are delivered through the listener; no error callback is provided.

- **`listener`** — Listener receiving unlock events.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.

## remoteUnlock(lockId, method)

Starts a remote unlock of the lock with the given method.

The method must be one of the lock's remoteUnlockMethods. Progress and the result are delivered through listenForUnlockEvents: started, then success or failed. A remote unlock runs independently of Bluetooth unlocks and cannot be canceled. If a remote unlock of the lock is already running, the call does nothing.

- **`lockId`** — Identifier of the lock to unlock.
- **`method`** — How the door is unlocked remotely.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [UnlockException](doc:android-ref-unlockexception) if the identifier does not match a known lock or the lock does not support the method.

## revokeGuestAccess(guestId, lockId)

Revokes one guest access.

- **`guestId`** — Identifier of the guest whose access is revoked.
- **`lockId`** — Identifier of the lock to revoke access to.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [NetworkException](doc:android-ref-networkexception) if the request fails or the token is invalid.
- **Throws:** [RevokeGuestException](doc:android-ref-revokeguestexception) if the passcode type cannot be revoked or the revocation fails.

## revokeGuestAllAccesses(guestId)

Revokes every access of a guest.

Attempts every applicable revocation. Cancellation stops immediately; otherwise every operation is attempted and the first selected failure is reported, preferring invalid-token, revoke, network, then internal errors. Per-access results are not returned.

- **`guestId`** — Identifier of the guest whose accesses are revoked.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [NetworkException](doc:android-ref-networkexception) if the token is invalid or expired.
- **Throws:** [RevokeGuestException](doc:android-ref-revokeguestexception) if the passcode type cannot be revoked or a revocation fails.

## setLogLevel(level)

Sets the minimum SDK logging level.

DEBUG produces detailed output; ERROR restricts logs to important issues. Safe to call before setupWithToken.

- **`level`** — Minimum log level that is recorded.

## setupWithToken(activity, token, includeAllLocks)

Authenticates and initializes the SDK.

If the token belongs to a different user than the last one, cached data is deleted first. The SDK stores the token on the device. Call setupWithToken on every app launch. The includeAllLocks flag is stored and applied whenever locks are retrieved.

- **`activity`** — Foreground Activity that can host setup UI.
- **`token`** — User authentication token.
- **`includeAllLocks`** — Whether non-partner locks are included.
- **Throws:** [SetupException](doc:android-ref-setupexception) if the token is invalid, consent is not granted, or setup fails internally.
- **Throws:** [NetworkException](doc:android-ref-networkexception) if no user is stored and the configuration cannot be fetched.
- **Throws:** `IllegalArgumentException` if the Activity cannot host setup UI.

## startProximityUnlock()

Starts proximity unlock scanning.

Scans for nearby locks and automatically unlocks the closest eligible lock within the SDK's BLE range threshold.

- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [BluetoothException](doc:android-ref-bluetoothexception) if Bluetooth is disabled or permissions are missing.

## stopListenForLocks(listener)

Stops delivering lock updates to the listener.

The listener is detached before this method returns; calling with an unregistered listener is a no-op. One in-flight update that began before detachment may still complete.

- **`listener`** — Listener to detach.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.

## stopListenForUnlockEvents(listener)

Stops delivering unlock events to the listener.

The listener is detached before this method returns; calling with an unregistered listener is a no-op. One in-flight event that began before detachment may still complete.

- **`listener`** — Listener to detach.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.

## stopProximityUnlock()

Stops proximity unlock scanning.

If an explicit unlock has paused scanning, that unlock keeps running and scanning does not resume after it finishes.

- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.

## sync(lockId)

Runs active sync for a lock.

Synchronizes lock data with DOOR and returns when the sync finishes.

- **`lockId`** — Identifier of the lock to sync.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [BluetoothException](doc:android-ref-bluetoothexception) if Bluetooth is disabled or permissions are missing.
- **Throws:** [NetworkException](doc:android-ref-networkexception) if the sync packages cannot be fetched.
- **Throws:** [SyncException](doc:android-ref-syncexception) if the sync is canceled, an unlock is in progress, or syncing fails internally.

## unlock(lockId)

Starts an explicit unlock for the lock with the given identifier.

Fails before any Bluetooth work when the identifier does not match a known lock. If proximity unlock is active, its current attempt and scan are paused; scanning resumes after this unlock finishes only while the same proximity session is still active. If the lock needs a setup sync first, an UnlockEvent with status SetupSync is emitted through listenForUnlockEvents.

- **`lockId`** — Identifier of the lock to unlock.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [BluetoothException](doc:android-ref-bluetoothexception) if Bluetooth is disabled or permissions are missing.
- **Throws:** [UnlockException](doc:android-ref-unlockexception) if the identifier does not match a known lock.

## unlock(lock)

Android convenience overload accepting a current Lock model.

Fails before any Bluetooth work when the model is stale or does not match a known lock. Proximity pause and resume behave as in the identifier overload.

- **`lock`** — Current lock model to unlock.
- **Throws:** [SDKException](doc:android-ref-sdkexception) if the SDK is not initialized.
- **Throws:** [BluetoothException](doc:android-ref-bluetoothexception) if Bluetooth is disabled or permissions are missing.
- **Throws:** [UnlockException](doc:android-ref-unlockexception) if the lock is not recognized.

## Related types

- [AccessLog](doc:android-ref-accesslog)
- [BluetoothException](doc:android-ref-bluetoothexception)
- [Guest](doc:android-ref-guest)
- [GuestInvitesException](doc:android-ref-guestinvitesexception)
- [IntercomSettings](doc:android-ref-intercomsettings)
- [IntercomSettingsException](doc:android-ref-intercomsettingsexception)
- [InviteType](doc:android-ref-invitetype)
- [Lock](doc:android-ref-lock)
- [LocksListener](doc:android-ref-lockslistener)
- [LogLevel](doc:android-ref-loglevel)
- [NetworkException](doc:android-ref-networkexception)
- [RemoteUnlockMethod](doc:android-ref-remoteunlockmethod)
- [RevokeGuestException](doc:android-ref-revokeguestexception)
- [SDKException](doc:android-ref-sdkexception)
- [SetupException](doc:android-ref-setupexception)
- [SyncException](doc:android-ref-syncexception)
- [UnlockEvent](doc:android-ref-unlockevent)
- [UnlockEventsListener](doc:android-ref-unlockeventslistener)
- [UnlockException](doc:android-ref-unlockexception)

Package: `com.door.opendoor.android.core.api`.

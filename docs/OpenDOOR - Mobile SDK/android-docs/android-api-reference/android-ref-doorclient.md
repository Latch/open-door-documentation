---
title: DoorClient
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Public OpenDOOR SDK Core Module.

Setup flow:
1. Call setupWithToken() with a valid token to authenticate
2. Use listenForLocks() or fetchLocks() to retrieve lock data
3. Listen for unlock events, including setup sync progress, while unlocking
4. Use unlock() or proximity unlock features as needed

## Declaration

```kotlin
interface DoorClient {

    @Throws(IllegalArgumentException::class, SetupException::class, NetworkException::class)
    suspend fun setupWithToken(
        activity: Activity,
        token: String,
        includeAllLocks: Boolean = false,
    ): Unit

    @Throws(SDKException::class)
    suspend fun clear(): Unit

    @Throws(SDKException::class, NetworkException::class)
    suspend fun fetchLocks(): List<Lock>

    @Throws(SDKException::class)
    fun listenForLocks(): kotlinx.coroutines.flow.Flow<List<Lock>>

    @Throws(SDKException::class)
    fun listenForLocks(listener: LocksListener): Unit

    @Throws(SDKException::class)
    fun stopListenForLocks(listener: LocksListener): Unit

    @Throws(SDKException::class, BluetoothException::class)
    suspend fun unlock(lockId: UUID): Unit

    @Throws(SDKException::class, BluetoothException::class)
    suspend fun unlock(lock: Lock): Unit

    @Throws(SDKException::class)
    suspend fun cancelUnlock(): Unit

    @Throws(SDKException::class, BluetoothException::class)
    suspend fun startProximityUnlock(): Unit

    @Throws(SDKException::class)
    suspend fun stopProximityUnlock(): Unit

    @Throws(SDKException::class)
    fun listenForUnlockEvents(): kotlinx.coroutines.flow.Flow<UnlockEvent>

    @Throws(SDKException::class)
    fun listenForUnlockEvents(listener: UnlockEventsListener): Unit

    @Throws(SDKException::class)
    fun stopListenForUnlockEvents(listener: UnlockEventsListener): Unit

    @Throws(
        SDKException::class,
        BluetoothException::class,
        NetworkException::class,
        SyncException::class,
    )
    suspend fun sync(lockId: UUID): Unit

    @Throws(SDKException::class, NetworkException::class)
    suspend fun getAccessLogs(lockId: UUID): List<AccessLog>

    @Throws(SDKException::class, NetworkException.InvalidTokenException::class,
        GuestInvitesException::class)
    suspend fun inviteGuest(
        firstName: String,
        lastName: String,
        email: String?,
        phone: String?,
        lockIds: List<UUID>,
        inviteType: InviteType,
    ): Unit

    @Throws(SDKException::class, NetworkException::class, RevokeGuestException::class)
    suspend fun revokeGuestAllAccesses(guestId: UUID): Unit

    @Throws(SDKException::class, NetworkException::class, RevokeGuestException::class)
    suspend fun revokeGuestAccess(
        guestId: UUID,
        lockId: UUID,
    ): Unit

    @Throws(SDKException::class, NetworkException::class)
    suspend fun guests(): List<Guest>

    fun setLogLevel(level: LogLevel)
}
```

## setupWithToken(activity, token, includeAllLocks)

Authenticates the SDK with the provided token and initializes services.

First part initializes the SDK (database, https clients, etc).
If the user from token is different from stored user, all cached data is deleted.
The token is stored in memory only (never persisted).
The includeAllLocks flag is stored and used when retrieving locks.

- **`activity`** — live foreground Activity for any setup UI and permission/consent flows
- **`token`** — the user authentication token.
- **`includeAllLocks`** — if true, include all locks; otherwise only partner locks.
- **Returns:** Completes when authentication and setup finishes.
- **Throws:** `IllegalArgumentException` if [activity] cannot host setup UI
- **Throws:** [SetupException](doc:android-ref-setupexception)
- **Throws:** [NetworkException](doc:android-ref-networkexception)

## clear()

Performs logout by clearing database and saved token.

This method clears all cached data and removes the authentication token.
After calling clear(), the client must be set up again with setupWithToken().

- **Returns:** Completes when all data has been cleared.
- **Throws:** [SDKException](doc:android-ref-sdkexception)

## fetchLocks()

Retrieves the locks of the current user.

Makes an API call to fetch the latest locks and updates the database.
Returns locks from the database (API results or cached values if API fails).

- **Returns:** List of locks available to the user.
- **Throws:** [SDKException](doc:android-ref-sdkexception)
- **Throws:** [NetworkException](doc:android-ref-networkexception)

## listenForLocks()

Returns a stream of lock list updates.

Connects to the database and emits updates whenever locks change.
Makes an initial API call to fetch locks and update the database.
As long as the listener is connected, will receive all lock updates.
The stream does not emit errors.

- **Returns:** a Flow of lock list updates.
- **Throws:** [SDKException](doc:android-ref-sdkexception)

## listenForLocks(listener)

Callback-based variant of listenForLocks.

- **`listener`** — Callback to receive `List<Lock>` updates
- **Returns:** Unit
- **Throws:** [SDKException](doc:android-ref-sdkexception)

## stopListenForLocks(listener)

Stops delivering lock updates to the provided listener.

Synchronous: the listener is detached from the registry before this method returns.
No-op when called with a listener that is not currently registered.

Note: cancellation of the underlying collector is cooperative. A single in-flight `onUpdate`
callback that began before cancellation propagated may still complete.

- **`listener`** — The listener to detach.
- **Throws:** [SDKException](doc:android-ref-sdkexception)

## unlock(lockId)

Starts an explicit unlock for a given lock.

Note: when running an explicit unlock, if proximity unlock is active,
it will be paused and resumed after the explicit unlock completes.
If the lock needs setup sync before unlock, a [UnlockEvent](doc:android-ref-unlockevent) with status
[UnlockStatus.SetupSync](doc:android-ref-unlockstatus) is
emitted through `listenForUnlockEvents`.

- **`lockId`** — the ID of the lock to unlock.
- **Returns:** Completes when the unlock request is initiated.
- **Throws:** [SDKException](doc:android-ref-sdkexception)
- **Throws:** [BluetoothException](doc:android-ref-bluetoothexception)

## unlock(lock)

Starts an explicit unlock for a given lock model.

The SDK validates the supplied lock against its current cache before starting BLE work.
If the model is stale or not present in cache, an unlock failure event is emitted with
[UnlockFailureReason.Internal](doc:android-ref-unlockfailurereason) (code `LOCK_NOT_RECOGNIZED`).

- **`lock`** — the lock model to unlock.
- **Returns:** Completes when the unlock request is initiated.
- **Throws:** [SDKException](doc:android-ref-sdkexception)
- **Throws:** [BluetoothException](doc:android-ref-bluetoothexception)

## cancelUnlock()

Cancels the active unlock attempt, if any.

Cancels an in-flight explicit unlock or proximity unlock attempt and emits a
[UnlockEvent](doc:android-ref-unlockevent) with status [UnlockStatus.Canceled](doc:android-ref-unlockstatus).
If no unlock attempt is active, this method completes without emitting an event.

This does not disable proximity unlock mode. Use `stopProximityUnlock` to stop
proximity unlock scanning.

- **Returns:** Completes when cancellation has been requested.
- **Throws:** [SDKException](doc:android-ref-sdkexception)

## startProximityUnlock()

Starts the proximity unlock process.

Begins scanning for nearby locks and will automatically unlock
the closest eligible lock found within the SDK's BLE range threshold.

- **Returns:** Completes when proximity unlock scanning starts.
- **Throws:** [SDKException](doc:android-ref-sdkexception)
- **Throws:** [BluetoothException](doc:android-ref-bluetoothexception)

## stopProximityUnlock()

Stops the proximity unlock process.

- **Returns:** Completes when proximity unlock is stopped.
- **Throws:** [SDKException](doc:android-ref-sdkexception)

## listenForUnlockEvents()

Returns a stream of unlock events from both explicit and proximity unlocks.

The stream contains progress and result events for all unlock operations.
Apps should handle status [UnlockStatus.SetupSync](doc:android-ref-unlockstatus)
to show progress when first-time setup sync is required before a door can unlock, and
[UnlockStatus.Canceled](doc:android-ref-unlockstatus) to react to `cancelUnlock()`.

- **Returns:** a Flow of unlock events.
- **Throws:** [SDKException](doc:android-ref-sdkexception)

## listenForUnlockEvents(listener)

Callback-based variant of listenForUnlockEvents.

- **`listener`** — Callback to receive UnlockEvent updates
- **Returns:** Unit
- **Throws:** [SDKException](doc:android-ref-sdkexception)

## stopListenForUnlockEvents(listener)

Stops delivering unlock events to the provided listener.

Synchronous: the listener is detached from the registry before this method returns.
No-op when called with a listener that is not currently registered.

Note: cancellation of the underlying collector is cooperative. A single in-flight `onNewEvent`
callback that began before cancellation propagated may still complete.

- **`listener`** — The listener to detach.
- **Throws:** [SDKException](doc:android-ref-sdkexception)

## sync(lockId)

Starts the active sync process for a lock.

Synchronizes lock data with the backend and returns when complete.

- **`lockId`** — ID of the lock to sync.
- **Returns:** Completes when synchronization finishes.
- **Throws:** [SDKException](doc:android-ref-sdkexception)
- **Throws:** [BluetoothException](doc:android-ref-bluetoothexception)
- **Throws:** [NetworkException](doc:android-ref-networkexception)
- **Throws:** [SyncException](doc:android-ref-syncexception)

## getAccessLogs(lockId)

Retrieves access logs for a specific lock.

Makes an API call to fetch the access logs for the given lock.

- **`lockId`** — ID of the lock.
- **Returns:** List of access log entries for the lock.
- **Throws:** [SDKException](doc:android-ref-sdkexception)
- **Throws:** [NetworkException](doc:android-ref-networkexception)

## inviteGuest(firstName, lastName, email, phone, lockIds, inviteType)

Shares access to specified locks (and the entire access path if lock is part of a BP building) with a guest using the provided settings.

This unified method automatically routes to the appropriate API based on lock type:
- For legacy locks: uses the legacy guest invite API
- For Blueprint locks: assigns guest role for the underlying directory item

Note: For Blueprint invites, the firstName parameter should contain the user UUID.

- **`firstName`** — first name of the guest (or user UUID for Blueprint invites).
- **`lastName`** — last name of the guest.
- **`email`** — email of the guest (nullable). Required for permanent invites.
- **`phone`** — phone number of the guest (nullable). At least one of email or phone must be provided for legacy invites.
- **`lockIds`** — list of lock UUIDs to grant access to.
- **`inviteType`** — type of invite (InAppInvite or TempDoorcodeInvite) with access settings.
- **Throws:** [SDKException](doc:android-ref-sdkexception)
- **Throws:** [NetworkException.InvalidTokenException](doc:android-ref-networkexception)
- **Throws:** [GuestInvitesException](doc:android-ref-guestinvitesexception)

## revokeGuestAllAccesses(guestId)

Revokes all accesses for a given guest.

- **`guestId`** — UUID of the guest whose accesses should be revoked.
- **Returns:** Completes when all accesses have been revoked.
- **Throws:** [SDKException](doc:android-ref-sdkexception)
- **Throws:** [NetworkException](doc:android-ref-networkexception)
- **Throws:** [RevokeGuestException](doc:android-ref-revokeguestexception)

## revokeGuestAccess(guestId, lockId)

Revokes a guest's access to a specific lock.

Note: `lockId` maps to the backend's `deviceUuid` path parameter.

- **`guestId`** — UUID of the guest whose access should be revoked.
- **`lockId`** — UUID of the lock/device to revoke access to.
- **Returns:** Completes when the access has been revoked.
- **Throws:** [SDKException](doc:android-ref-sdkexception)
- **Throws:** [NetworkException](doc:android-ref-networkexception)
- **Throws:** [RevokeGuestException](doc:android-ref-revokeguestexception)

## guests()

Gets information for all guests with shared access.

- **Returns:** List of all guests with shared access.
- **Throws:** [SDKException](doc:android-ref-sdkexception)
- **Throws:** [NetworkException](doc:android-ref-networkexception)

## setLogLevel(level)

Sets the logging verbosity.

Higher levels (e.g. [LogLevel.DEBUG](doc:android-ref-loglevel)) produce more detailed output, while lower
levels (e.g. [LogLevel.ERROR](doc:android-ref-loglevel)) restrict logs to important issues only. Safe to call
before or after `setupWithToken`; useful for tracing setup itself.

- **`level`** — The minimum log level that should be recorded.

## Related types

- [AccessLog](doc:android-ref-accesslog)
- [BluetoothException](doc:android-ref-bluetoothexception)
- [Guest](doc:android-ref-guest)
- [GuestInvitesException](doc:android-ref-guestinvitesexception)
- [InAppInvite](doc:android-ref-inappinvite)
- [InviteGuestException](doc:android-ref-inviteguestexception)
- [InviteType](doc:android-ref-invitetype)
- [Lock](doc:android-ref-lock)
- [LocksListener](doc:android-ref-lockslistener)
- [LogLevel](doc:android-ref-loglevel)
- [NetworkException](doc:android-ref-networkexception)
- [OpenDOOR](doc:android-ref-opendoor)
- [RevokeGuestException](doc:android-ref-revokeguestexception)
- [SDKException](doc:android-ref-sdkexception)
- [SetupException](doc:android-ref-setupexception)
- [SyncException](doc:android-ref-syncexception)
- [TempDoorcodeInvite](doc:android-ref-tempdoorcodeinvite)
- [UnlockEvent](doc:android-ref-unlockevent)
- [UnlockEventsListener](doc:android-ref-unlockeventslistener)
- [UnlockFailureReason](doc:android-ref-unlockfailurereason)
- [UnlockStatus](doc:android-ref-unlockstatus)

Package: `com.door.opendoor.android.core.api`.

---
title: DOORClient
excerpt: Public OpenDOOR SDK Core Module.
hidden: true
---

*Protocol*

```swift
protocol DOORClient
```

Public OpenDOOR SDK Core Module.

## Instance Methods

### `cancelUnlock()`

```swift
func cancelUnlock() throws
```

Cancels the active unlock attempt, if any.

##### Discussion

Emits an UnlockEvent with status Canceled for an in-flight attempt and completes silently otherwise. Proximity mode stays enabled; use stopProximityUnlock to disable it.

> **Throws:** - `SDKError` if the SDK is not initialized.


### `clear()`

```swift
func clear() async throws
```

Clears SDK state and authentication.

##### Discussion

Deletes cached data and removes the stored token. After clear the client must be set up again with setupWithToken.

> **Throws:** - `SDKError` if clearing state fails internally.


### `fetchLocks()`

```swift
func fetchLocks() async throws -> [Lock]
```

Fetches the current user’s locks.

##### Discussion

Refreshes locks from the network and updates the cache. An invalid or expired token always fails, even when cached locks exist. Other network failures return cached locks when available and fail only when the cache is empty.

> **Throws:** - `SDKError` if the SDK is not initialized.
> 
> - `NetworkError` if the token is invalid or expired, and on other network failures only when the cache is empty.


### `getAccessLogs(lockID:)`

```swift
func getAccessLogs(lockID: UUID) async throws -> [AccessLog]
```

Retrieves access logs for a lock.

#### Parameters

- **lockID** — Identifier of the lock.

##### Discussion

> **Throws:** - `SDKError` if the SDK is not initialized.
> 
> - `NetworkError` if the request fails or the token is invalid.


### `guests()`

```swift
func guests() async throws -> [Guest]
```

Retrieves all guests with shared access, combining legacy and Blueprint invitations.

##### Discussion

> **Throws:** - `SDKError` if the SDK is not initialized.
> 
> - `NetworkError` if fetching guests fails.


### `inviteGuest(firstName:lastName:email:phone:lockIDs:inviteType:)`

```swift
func inviteGuest(firstName: String, lastName: String, email: String?, phone: String?, lockIDs: [UUID], inviteType: any InviteType) async throws
```

Grants a guest access to the requested locks.

#### Parameters

- **firstName** — First name of the guest, or the user UUID for Blueprint invites.

- **lastName** — Last name of the guest.

- **email** — Email of the guest; required for permanent invites.

- **phone** — Phone number; legacy invites need email or phone.

- **lockIDs** — Locks to grant access to.

- **inviteType** — Invite settings, InAppInvite or TemporaryDoorcodeInvite.

##### Discussion

Routes each lock to the legacy or Blueprint invite API based on its building type. For Blueprint invites the firstName parameter carries the user UUID.

> **Throws:** - `SDKError` if the SDK is not initialized.
> 
> - `NetworkError` if the token is invalid or expired.
> 
> - `GuestInvitesError` with per-lock results when any invite operation fails.


### `listenForLocks()`

```swift
func listenForLocks() throws -> AsyncStream<[Lock]>
```

Returns an update-only stream of lock lists.

##### Discussion

Initialization is checked when the stream is created. The stream emits cached state, including an empty list, and subsequent updates, and starts a best-effort refresh. Later refresh and observation failures are logged internally; the stream has no error channel.

> **Throws:** - `SDKError` if the SDK is not initialized.


### `listenForLocks(listener:)`

```swift
func listenForLocks(listener: LocksListener) throws
```

Callback variant of listenForLocks.

#### Parameters

- **listener** — Listener receiving lock updates.

##### Discussion

Initialization is checked before the listener is registered. Cached state, including an empty list, and subsequent updates are delivered through the listener; no error callback is provided.

> **Throws:** - `SDKError` if the SDK is not initialized.


### `listenForLocksPublisher()`

```swift
func listenForLocksPublisher() throws -> AnyPublisher<[Lock], Never>
```

Combine publisher variant of listenForLocks.

##### Discussion

> **Throws:** - `SDKError` if the SDK is not initialized.


### `listenForUnlockEvents()`

```swift
func listenForUnlockEvents() throws -> AsyncStream<UnlockEvent>
```

Returns unlock lifecycle events from explicit and proximity unlocks.

##### Discussion

Carries progress and result events for every unlock operation. Handle status SetupSync to show progress when a first-time setup sync is required, and Canceled to react to cancelUnlock.

> **Throws:** - `SDKError` if the SDK is not initialized.


### `listenForUnlockEvents(listener:)`

```swift
func listenForUnlockEvents(listener: UnlockEventsListener) throws
```

Callback variant of listenForUnlockEvents.

#### Parameters

- **listener** — Listener receiving unlock events.

##### Discussion

Events are delivered through the listener; no error callback is provided.

> **Throws:** - `SDKError` if the SDK is not initialized.


### `revokeGuestAccess(guestID:lockID:)`

```swift
func revokeGuestAccess(guestID: UUID, lockID: UUID) async throws
```

Revokes one guest access.

#### Parameters

- **guestID** — Identifier of the guest whose access is revoked.

- **lockID** — Identifier of the lock to revoke access to.

##### Discussion

The lock identifier maps to the backend’s device identifier.

> **Throws:** - `SDKError` if the SDK is not initialized.
> 
> - `NetworkError` if the request fails or the token is invalid.
> 
> - `RevokeGuestError` if the passcode type cannot be revoked or the revocation fails.


### `revokeGuestAllAccesses(guestID:)`

```swift
func revokeGuestAllAccesses(guestID: UUID) async throws
```

Revokes every access of a guest.

#### Parameters

- **guestID** — Identifier of the guest whose accesses are revoked.

##### Discussion

Attempts one bulk legacy revocation plus each distinct Blueprint assignment. Cancellation stops immediately; otherwise every operation is attempted and the first selected failure is reported, preferring invalid-token, revoke, network, then internal errors. Per-access results are not returned.

> **Throws:** - `SDKError` if the SDK is not initialized.
> 
> - `NetworkError` if the token is invalid or expired.
> 
> - `RevokeGuestError` if the passcode type cannot be revoked or a revocation fails.


### `setLogLevel(_:)`

```swift
func setLogLevel(_ level: LogLevel)
```

Sets the minimum SDK logging level.

#### Parameters

- **level** — Minimum log level that is recorded.

##### Discussion

DEBUG produces detailed output; ERROR restricts logs to important issues. Safe to call before setupWithToken.


### `setupWithToken(token:includeAllLocks:)`

```swift
func setupWithToken(token: String, includeAllLocks: Bool) async throws
```

Authenticates and initializes the SDK.

#### Parameters

- **token** — User authentication token.

- **includeAllLocks** — Whether non-partner locks are included.

##### Discussion

Initializes storage and network clients, then authenticates with the token. If the token’s user differs from the stored user, all cached data is deleted first. The token is kept in memory only and never persisted. The includeAllLocks flag is stored and applied whenever locks are retrieved.

> **Throws:** - `SetupError` if the token is invalid, consent is not granted, or setup fails internally.
> 
> - `NetworkError` if no user is stored and the configuration cannot be fetched.


### `startProximityUnlock()`

```swift
func startProximityUnlock() throws
```

Starts proximity unlock scanning.

##### Discussion

Scans for nearby locks and automatically unlocks the closest eligible lock within the SDK’s BLE range threshold.

> **Throws:** - `SDKError` if the SDK is not initialized.
> 
> - `BluetoothError` if Bluetooth is disabled or permissions are missing.


### `stopListenForLocks(listener:)`

```swift
func stopListenForLocks(listener: LocksListener) throws
```

Stops delivering lock updates to the listener.

#### Parameters

- **listener** — Listener to detach.

##### Discussion

The listener is detached before this method returns; calling with an unregistered listener is a no-op. One in-flight update that began before detachment may still complete.

> **Throws:** - `SDKError` if the SDK is not initialized.


### `stopListenForUnlockEvents(listener:)`

```swift
func stopListenForUnlockEvents(listener: UnlockEventsListener) throws
```

Stops delivering unlock events to the listener.

#### Parameters

- **listener** — Listener to detach.

##### Discussion

The listener is detached before this method returns; calling with an unregistered listener is a no-op. One in-flight event that began before detachment may still complete.

> **Throws:** - `SDKError` if the SDK is not initialized.


### `stopProximityUnlock()`

```swift
func stopProximityUnlock() throws
```

Stops proximity unlock scanning.

##### Discussion

If an explicit unlock has paused scanning, that unlock keeps running and scanning does not resume after it finishes.

> **Throws:** - `SDKError` if the SDK is not initialized.


### `sync(lockID:)`

```swift
func sync(lockID: UUID) async throws
```

Runs active sync for a lock.

#### Parameters

- **lockID** — Identifier of the lock to sync.

##### Discussion

Synchronizes lock data with the backend and returns when the sync finishes.

> **Throws:** - `SDKError` if the SDK is not initialized.
> 
> - `BluetoothError` if Bluetooth is disabled or permissions are missing.
> 
> - `NetworkError` if the sync packages cannot be fetched.
> 
> - `SyncError` if the sync is canceled, an unlock is in progress, or syncing fails internally.


### `unlock(lockID:)`

```swift
func unlock(lockID: UUID) async throws
```

Starts an explicit unlock for the lock with the given identifier.

#### Parameters

- **lockID** — Identifier of the lock to unlock.

##### Discussion

Fails before any Bluetooth work when the identifier does not match a known lock. If proximity unlock is active, its current attempt and scan are paused; scanning resumes after this unlock finishes only while the same proximity session is still active. If the lock needs a setup sync first, an UnlockEvent with status SetupSync is emitted through listenForUnlockEvents.

> **Throws:** - `SDKError` if the SDK is not initialized.
> 
> - `BluetoothError` if Bluetooth is disabled or permissions are missing.
> 
> - `UnlockError` if the identifier does not match a known lock.


### `unlockEventsPublisher()`

```swift
func unlockEventsPublisher() throws -> AnyPublisher<UnlockEvent, Never>
```

Combine publisher variant of listenForUnlockEvents.

##### Discussion

> **Throws:** - `SDKError` if the SDK is not initialized.

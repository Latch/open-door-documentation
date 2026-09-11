---
title: DOORClient
excerpt: OpenDOOR iOS SDK 2.1.0 protocol reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

Public [OpenDOOR](doc:ios-ref-opendoor) SDK Core Module.

### Overview

Setup flow:

1. Call setupWithToken() with a valid token to authenticate
2. Use listenForLocks() or fetchLocks() to retrieve lock data
3. Use unlock() or proximity unlock features as needed



## Declaration

```swift
public protocol DOORClient {
  func setupWithToken(token: String, includeAllLocks: Bool) async throws
  func clear() async throws
  func fetchLocks() async throws -> [Lock]
  func listenForLocks() throws -> AsyncStream<[Lock]>
  func listenForLocksPublisher() throws -> AnyPublisher<[Lock], Never>
  func listenForLocks(listener: any LocksListener) throws
  func stopListenForLocks(listener: any LocksListener) throws
  func unlock(lockID: UUID) async throws
  func cancelUnlock() throws
  func startProximityUnlock() throws
  func stopProximityUnlock() throws
  func listenForUnlockEvents() throws -> AsyncStream<UnlockEvent>
  func unlockEventsPublisher() throws -> AnyPublisher<UnlockEvent, Never>
  func listenForUnlockEvents(listener: any UnlockEventsListener) throws
  func stopListenForUnlockEvents(listener: any UnlockEventsListener) throws
  func sync(lockID: UUID) async throws
  func getAccessLogs(lockID: UUID) async throws -> [AccessLog]
  func inviteGuest(firstName: String, lastName: String, email: String?, phone: String?, lockIDs: [UUID], inviteType: any InviteType) async throws
  func revokeGuestAllAccesses(guestID: UUID) async throws
  func revokeGuestAccess(guestID: UUID, lockID: UUID) async throws
  func guests() async throws -> [Guest]
  func setLogLevel(_ level: LogLevel)
}
```

## cancelUnlock()

```swift
func cancelUnlock() throws
```

Cancel the active unlock

### Discussion

**Throws:** [SDKError](doc:ios-ref-sdkerror)

## clear()

```swift
func clear() async throws
```

Performs logout by clearing database and saved token.

### Discussion

This method clears all cached data and removes the authentication token. After calling clear(), the client must be set up again with setupWithToken().

**Throws:** [SDKError](doc:ios-ref-sdkerror)

## fetchLocks()

```swift
func fetchLocks() async throws -> [Lock]
```

Retrieves the locks of the current user.

### Return Value

List of locks available to the user.


### Discussion

Makes an API call to fetch the latest locks and updates the database. Returns locks from the database (API results or cached values if API fails).

**Throws:** [SDKError](doc:ios-ref-sdkerror), [NetworkError](doc:ios-ref-networkerror)

## getAccessLogs(lockID:)

```swift
func getAccessLogs(lockID: UUID) async throws -> [AccessLog]
```

Retrieves access logs for a specific lock.

### Parameters


- `lockID`: ID of the lock.

### Return Value

List of access log entries for the lock.


### Discussion

Makes an API call to fetch the access logs for the given lock.

**Throws:** [SDKError](doc:ios-ref-sdkerror), [NetworkError](doc:ios-ref-networkerror)

## guests()

```swift
func guests() async throws -> [Guest]
```

Gets information for all guests with shared access.

### Return Value

List of all guests with shared access.


### Discussion

**Throws:** [SDKError](doc:ios-ref-sdkerror), [NetworkError](doc:ios-ref-networkerror)

## inviteGuest(firstName:lastName:email:phone:lockIDs:inviteType:)

```swift
func inviteGuest(firstName: String, lastName: String, email: String?, phone: String?, lockIDs: [UUID], inviteType: InviteType) async throws
```

Shares access to selected locks and to the entire path if building support this feature with a guest using the provided settings.

### Parameters


- `firstName`: First name of the guest.

- `lastName`: Last name of the guest.

- `email`: Email of the guest (optional). At least one of `email` or `phone` must be provided.

- `phone`: Phone number of the guest (optional). At least one of `email` or `phone` must be provided.

- `lockIDs`: UUIDs of the DOOR locks to add to the guest’s access.

- `inviteType`: Type of invite (e.g., `InAppInvite` or `TemporaryDoorcodeInvite`) with access settings.

### Discussion

Note: For email and phone parameters, at least one must be provided. If both are `nil`, a network error will be returned. This operation may partially succeed. See [GuestInvitesError](doc:ios-ref-guestinviteserror) for details about any locks that failed.

**Throws:** [SDKError](doc:ios-ref-sdkerror), [NetworkError](doc:ios-ref-networkerror), [GuestInvitesError](doc:ios-ref-guestinviteserror)

## listenForLocks()

```swift
func listenForLocks() throws -> AsyncStream<[Lock]>
```

Returns a stream of lock list updates.

### Return Value

A AsyncStream of lock list updates.


### Discussion

Connects to the database and emits updates whenever locks change. Makes an initial API call to fetch locks and update the database. As long as the listener is connected, will receive all lock updates. The stream does not emit errors.

**Throws:** [SDKError](doc:ios-ref-sdkerror)

## listenForLocks(listener:)

```swift
func listenForLocks(listener: LocksListener) throws
```

Callback-based variant of listenForLocks

### Parameters


- `listener`: Callback to receive [[Lock](doc:ios-ref-lock)] updates

### Discussion

**Throws:** [SDKError](doc:ios-ref-sdkerror)

## listenForLocksPublisher()

```swift
func listenForLocksPublisher() throws -> AnyPublisher<[Lock], Never>
```

Combine variant of listenForLocks

### Return Value

A Publisher of lock list updates.


### Discussion

**Throws:** [SDKError](doc:ios-ref-sdkerror)

## listenForUnlockEvents()

```swift
func listenForUnlockEvents() throws -> AsyncStream<UnlockEvent>
```

Returns a stream of unlock events from both explicit and proximity unlocks.

### Return Value

A AsyncStream of unlock events.


### Discussion

The stream will contain progress and result events for all unlock operations.

**Throws:** [SDKError](doc:ios-ref-sdkerror)

## listenForUnlockEvents(listener:)

```swift
func listenForUnlockEvents(listener: UnlockEventsListener) throws
```

Callback-based variant of listenForUnlockEvents

### Discussion

**Throws:** [SDKError](doc:ios-ref-sdkerror)

## revokeGuestAccess(guestID:lockID:)

```swift
func revokeGuestAccess(guestID: UUID, lockID: UUID) async throws
```

Revokes a guest’s access to a specific lock.

### Parameters


- `guestID`: UUID of the guest whose accesses will be revoked.

- `lockID`: UUID of the lock to revoke access to.

### Discussion

Use this to remove access to a single lock without affecting other locks the guest may have access to.

**Throws:** [SDKError](doc:ios-ref-sdkerror), [NetworkError](doc:ios-ref-networkerror), [RevokeGuestError](doc:ios-ref-revokeguesterror)

## revokeGuestAllAccesses(guestID:)

```swift
func revokeGuestAllAccesses(guestID: UUID) async throws
```

Revokes all accesses of a guest.

### Parameters


- `guestID`: UUID of the guest whose accesses will be revoked.

### Discussion

Use this to remove a guest’s ability to unlock any DOOR locks they previously had access to.

This operation may partially succeed.

**Throws:** [SDKError](doc:ios-ref-sdkerror), [NetworkError](doc:ios-ref-networkerror), [RevokeGuestError](doc:ios-ref-revokeguesterror)

## setLogLevel(_:)

```swift
func setLogLevel(_ level: LogLevel)
```

Sets the logging verbosity

### Parameters


- `level`: The minimum log level that should be recorded. Defaults to `.info`.

### Discussion

Use this to control how much diagnostic information the SDK logs. Higher levels (e.g. `.debug`) produce more detailed output, while lower levels (e.g. `.error`) restrict logs to important issues only.

## setupWithToken(token:includeAllLocks:)

```swift
func setupWithToken(token: String, includeAllLocks: Bool) async throws
```

Authenticates the SDK with the provided token and initializes services.

### Parameters


- `token`: The user authentication token.

- `includeAllLocks`: If true, include all locks; otherwise only partner locks.

### Discussion

First part initializes the SDK (database, https clients, etc). If the user from token is different from stored user, all cached data is deleted. The token is stored in memory only (never persisted). The includeAllLocks flag is stored and used when retrieving locks.

**Throws:** [SetupError](doc:ios-ref-setuperror), [NetworkError](doc:ios-ref-networkerror)

## startProximityUnlock()

```swift
func startProximityUnlock() throws
```

Starts the proximity unlock process.

### Discussion

Begins scanning for nearby locks and will automatically unlock the first eligible lock found within range.

**Throws:** [SDKError](doc:ios-ref-sdkerror), [BluetoothError](doc:ios-ref-bluetootherror)

## stopListenForLocks(listener:)

```swift
func stopListenForLocks(listener: LocksListener) throws
```

Stops delivering lock updates to the provided listener.

### Discussion

**Throws:** [SDKError](doc:ios-ref-sdkerror)

## stopListenForUnlockEvents(listener:)

```swift
func stopListenForUnlockEvents(listener: UnlockEventsListener) throws
```

Stops delivering unlock events to the provided listener.

### Discussion

**Throws:** [SDKError](doc:ios-ref-sdkerror)

## stopProximityUnlock()

```swift
func stopProximityUnlock() throws
```

Stops the proximity unlock process.

### Discussion

**Throws:** [SDKError](doc:ios-ref-sdkerror)

## sync(lockID:)

```swift
func sync(lockID: UUID) async throws
```

Starts the active sync process for a lock.

### Parameters


- `lockID`: ID of the lock to sync.

### Discussion

Synchronizes lock data with the backend and returns when complete.

**Throws:** [SDKError](doc:ios-ref-sdkerror), [BluetoothError](doc:ios-ref-bluetootherror), [NetworkError](doc:ios-ref-networkerror), [SyncError](doc:ios-ref-syncerror)

## unlock(lockID:)

```swift
func unlock(lockID: UUID) async throws
```

Starts an explicit unlock for a given lock.

### Parameters


- `lockID`: The ID of the lock to unlock.

### Discussion

Note: when running an explicit unlock, if proximity unlock is active, it will be cancelled. Unlock status is published through the unlock event stream APIs: listenForUnlockEvents, unlockEventsPublisher, and the callback-based listenForUnlockEvents.

**Throws:** [SDKError](doc:ios-ref-sdkerror), [BluetoothError](doc:ios-ref-bluetootherror), [UnlockError](doc:ios-ref-unlockerror)

## unlockEventsPublisher()

```swift
func unlockEventsPublisher() throws -> AnyPublisher<UnlockEvent, Never>
```

Combine variant of listenForUnlockEvents

### Return Value

A Publisher of unlock events.


### Discussion

**Throws:** [SDKError](doc:ios-ref-sdkerror)

## Related types

[AccessLog](doc:ios-ref-accesslog) · [Guest](doc:ios-ref-guest) · [InviteType](doc:ios-ref-invitetype) · [Lock](doc:ios-ref-lock) · [LocksListener](doc:ios-ref-lockslistener) · [LogLevel](doc:ios-ref-loglevel) · [UnlockEvent](doc:ios-ref-unlockevent) · [UnlockEventsListener](doc:ios-ref-unlockeventslistener)

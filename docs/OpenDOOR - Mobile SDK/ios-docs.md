---
title: iOS SDK
excerpt: >-
  The SDK provides APIs to view, unlock and sync DOOR-supported locks and to
  manage guests accesses. This tutorial corresponds with version 2.1.0 of the
  SDK.
deprecated: false
hidden: false
metadata:
  robots: index
---
## What's new in SDK 2.1.0

* **New modern API:** Swift concurrency APIs with uniform errors
  * Lock and unlock events now use stream-based listeners instead of polling. 
  * Unified unlock event pipeline for both explicit unlock and proximity unlock.
* **Setup sync visibility during unlock:** `UnlockEvent.SetupSync` is emitted when the SDK needs to run setup sync before unlocking, such as the first time a user opens a door and the lock needs access data.
* **Unlock cancellation:** `cancelUnlock()` cancels the active explicit unlock or the current proximity unlock attempt
* Finer-grained log levels

## Setup

1. [Add OpenDOOR SDK as a dependency](https://developers.door.com/docs/ios-docs#add-opendoor-sdk-as-a-dependency)
2. [Initialize the library](https://developers.door.com/docs/ios-docs#initialize-the-library)
3. [Sign out](https://developers.door.com/docs/ios-docs#sign-out)
4. [Get locks](https://developers.door.com/docs/ios-docs#get-locks)
5. [Unlock](https://developers.door.com/docs/ios-docs#unlock)
6. [Sync](https://developers.door.com/docs/ios-docs#sync)
7. [Access logs](https://developers.door.com/docs/ios-docs#access-logs)
8. [Guest Access](https://developers.door.com/docs/ios-docs#guest-access)
9. [Log level](https://developers.door.com/docs/ios-docs#log-level)

<br />

### Add OpenDOOR SDK as a dependency

1. In Xcode, select “File” → “Add Packages...”
2. Enter [https://github.com/Latch/opendoor-sdk-spm.git](https://github.com/Latch/opendoor-sdk-spm.git)
3. Select OpenDOORCore library product

Or you can add the following dependency to your Package.swift:

```swift iOS
.package(url: "https://github.com/Latch/opendoor-sdk-spm.git", from: "2.1.0")
```

and add it to your target like this:

```swift iOS
dependencies: [
  .product(name: "OpenDOORCore", package: "OpenDOORSDK")
]
```

### Initialize the library

Use your Auth0 token retrieved from DOOR's Auth endpoint, get an instance of OpenDOOR, and call `setupWithToken()` with parameters:

token - Auth0 token

includeAllLocks - determines whether we should load all locks that user can access (partner and non-partner) or only partner-managed locks.

```swift iOS
 import OpenDOORCore

 let client = await OpenDOOR.getInstance()
 do {
    try await client.setupWithToken(token: token, includeAllLocks: true)
 } catch let error as SetupError {
     // Handle setup errors
 } catch let error as NetworkError {
  // Handle network errors
 }

```

Note:

1. Attempting to call any OpenDOOR SDK function before initialization will throw SDKError.sdkNotInitialized.

2. All OpenDOOR SDK APIs are not guaranteed to return on the main thread. If you use the result to update UI, you are responsible for dispatching back to the main thread.

3. Ensure your app declares the required Bluetooth permissions in Info.plist and enables Bluetooth backgrounds modes.

### Sign out

To clear all cached data and remove authentication token call `clear()`. After calling `clear()`, the client must be set up again with setupWithToken().

```swift iOS
 import OpenDOORCore

 let client = await OpenDOOR.getInstance()
 do {
    try await client.clear()
 } catch let error as SDKError {
     // Handle sdk general errors
 } 

```

### Get locks

You can retrieve locks in two ways: fetch them once with `fetchLocks()`, or listen for continuous updates with `listenForLocks()` variants. These methods have different behaviors:

* **`fetchLocks()`**: Waits for the server call to complete before returning. Does not return until the network request finishes (or fails). Use this when you need fresh data and can wait for the network call. Returns API results or cached values if API fails. If the API request fails with token expired, an error will be thrown even if there is cached data.

* **`listenForLocks`**: Returns cached data immediately, then attempts to refresh from the server in the background. Cached locks are emitted first, then updated locks when the server refresh completes. Use this when you want to show data quickly and update it when fresh data arrives. `listenForLocks` variants do not emit errors from the stream, but the call itself can throw (e.g., SDK not initialized). They can be used to work offline.

Note:

Whenever locks are retrieved from the server, configuration data is also synchronized in the background.

**Option 1: Fetch locks**

```swift iOS
 import OpenDOORCore

 do {
    try await client.fetchLocks()
 } catch let error as SDKError {
     // Handle sdk general errors
 } catch let error as NetworkError {
     // Handle network errors
 }
```

**Option 2: Listen for locks updates (AsyncStream)**

```swift iOS
 import OpenDOORCore

 do {
    let stream = try client.listenForLocks()
    for await locks in stream {
        // Use locks list
    }
 } catch let error as SDKError {
    // Handle SDK errors
 } 
```

**Option 3: Listen for locks updates (Combine Publisher)**

```swift iOS
 import OpenDOORCore

 do {
    // Keep a strong reference to the subscription.
    locksSubscription = try client.listenForLocksPublisher()
                .receive(on: DispatchQueue.main)
                .sink(
                    receiveValue: { locks in
                       // Use locks list
                    }
                )
 } catch let error as SDKError {
    // Handle SDK errors
 } 
```

**Option 4: Listen for locks updates (Callback listener)**

Note:

The listener is weakly retained by the SDK. Keep a strong reference (for example, a stored property) or it may be deallocated. If you explicitly want to stop listening to locks updates, call `stopListenForLocks`.

```swift iOS
 import OpenDOORCore

 let listener = LockStreamListener()
 do {
    try client.listenForLocks(listener: listener)
 } catch let error as SDKError {
    // Handle SDK errors
 } 

 // stop listening
 do {
    try client.stopListenForLocks(listener: listener)
 } catch let error as SDKError {
   // Handle SDK errors
 }
```

## Unlock

Unlocking a door can be done in two ways: explicitly (by calling `unlock()`) or using proximity unlock.

One unlock at a time can be done, with mention that explicit unlock has precedence over proximity unlock.

Unlock events can be tracked using different variants for publishing them, described later in this section.

### Explicit unlock

```swift iOS
 import OpenDOORCore

 let lockID = lock.id
 
 do {
    try await client.unlock(lockID: lockID)
 } catch let error as SDKError {
    // Handle SDK errors
 } catch let error as BluetoothError {
    // Handle Bluetooth errors
 } catch let error as UnlockError {
    // Handle unlock errors
 }
```

### Proximity unlock

Proximity unlock continuously scans for nearby locks after it is started. It will automatically attempt to unlock an eligible lock only when the phone is very close to the lock, similar to how proximity unlock works in the app.

This is intended for close-range unlocks, typically when the phone is within a few inches of the lock, not from several feet or meters away. For example, the phone may need to be roughly less than 3 inches from the lock before an unlock is triggered.

```swift iOS
 import OpenDOORCore
 
 do {
    try await client.startProximityUnlock()
 } catch let error as SDKError {
    // Handle SDK errors
 } catch let error as BluetoothError {
    // Handle Bluetooth errors
 }
```

Proximity unlock scanning can be stopped when needed by calling `stopProximityUnlock`.

```swift iOS
 import OpenDOORCore

 do {
    try await client.stopProximityUnlock()
 } catch let error as SDKError {
    // Handle SDK errors
 }
```

### Unlock events

Unlock events from both explicit unlocks and proximity are published through the unlock event stream APIs: listenForUnlockEvents, unlockEventsPublisher, and the callback-based listenForUnlockEvents.

**Option 1: Listen for unlock events (AsyncStream)**

```swift iOS
 import OpenDOORCore

 do {
    let stream = try client.listenForUnlockEvents()
    for await unlockEvent in stream {
        // Use unlock event
         switch unlockEvent {
         case .started:
           // Unlock process has started
         case .setupSync:
					 // The lock is being set up
         case .success:
             // Lock is unlocked!
         case .failed:
              // Unlock failed
         case .canceled:
             // Unlock was canceled
        }
    }
 } catch let error as SDKError {
    // Handle SDK errors
 } 
```

**Option 2: Listen for unlock events (Combine Publisher)**

```swift iOS
 import OpenDOORCore

 do {
     // Keep a strong reference to the subscription.
      unlockEventsSubscription = try client.unlockEventsPublisher()
                .receive(on: DispatchQueue.main)
                .sink { unlockEvent in
                    // Use unlock event
                     switch unlockEvent {
                     case .started:
                       // Unlock process has started
										 case .setupSync:
					 						// The lock is being set up
                     case .success:
                        // Lock is unlocked!
                     case .failed:
                        // Unlock failed
                     case .canceled:
                        // Unlock was canceled
                     }
                }

 } catch let error as SDKError {
        // Handle SDK errors
 }
```

**Option 3: Listen for unlock events (Callback listener)**

Note:

The listener is weakly retained by the SDK. Keep a strong reference (for example, a stored property) or it may be deallocated. If you explicitly want to stop listening to unlock events, call `stopListenForUnlockEvents`.

```swift iOS
 import OpenDOORCore

 let listener = UnlockEventListener()
 
 do {
    try client.listenForUnlockEvents(listener: listener)
 } catch let error as SDKError {
    // Handle SDK errors
 } 
  
 // stop listening
 do {
    try client.stopListenForUnlockEvents(listener: listener)
 } catch let error as SDKError {
   // Handle SDK errors
 }
```

<br />

### Cancel unlock

Cancel the active unlock.

```swift iOS
import OpenDOORCore

 do {
    try client.cancelUnlock()
 } catch let error as SDKError {
    // Handle SDK errors
 } 
```

## Sync

Sync allows your mobile client to act as a bridge to the DOOR backend for uplink and downlink data requests, including battery, timestamp, activity logs, and engineering logs. In times of troubleshooting, a sync is recommended to either resolve the issue or provide DOOR with full information around the issue.

After each unlock, the SDK will passively sync data with the DOOR ecosystem to keep user data as up to date as possible. Explicitly calling `sync()` will initiate a longer sync operation that attempts to sync all critical data, including the data synced after unlock, along with non-critical data.

The `sync()` operation takes about 10 seconds on average and will cancel any passive sync operations initiated after the unlock operation.

```swift iOS
 import OpenDOORCore

 let lockID = lock.id
 do {
    try await client.sync(lockID: lockID)
 } catch let error as SDKError {
    // Handle SDK errors
 } catch let error as BluetoothError {
    // Handle Bluetooth errors
 } catch let error as NetworkError {
    // Handle network errors
 } catch let error as SyncError {
    // Handle sync errors
 }
```

## Access logs

Retrieve access logs for a lock.

```swift iOS
 import OpenDOORCore

 let lockID = lock.id
 do {
    try await client.getAccessLogs(lockID: lockID)
 } catch let error as SDKError {
    // Handle SDK errors
 } catch let error as NetworkError {
    // Handle network errors
 }
```

## Guest Access

### Invite guests

To share access to the selected list of eligible locks (`isSharable == true`) and to the entire path if the building supports this feature, use `inviteGuest`.

A guest invitation can be created with temporary door code access or in-app access with time-based restrictions.

This operation may partially succeed. See GuestInvitesError for details about any locks that failed.

```swift iOS
 import OpenDOORCore

 let lockIDs: [UUID] = <array of lock IDs where isSharable == true>
 do {
    try await client.inviteGuest(
                    firstName: "John",
                    lastName: "Doe",
                    email: "john@example.com",
                    phone: "+1234567890",
                    lockIDs: lockIDs,
                    inviteType: inviteType
                )
 } catch let error as SDKError {
    // Handle SDK errors
 } catch let error as NetworkError {
    // Handle network errors
 } catch let error as GuestInvitesError {
   // Handle invites guest errors: 
   // error.successfulLockIDs - ids of locks with successful invite.
   // error.failedLockIDs - ids of locks with failed invite.
   // error.failedLockErrors - errors encountered for each lock that failed. 
 }
```

### Revoke a guest's access

To remove access to a single lock, without affecting other locks the guest may have access to, call `revokeGuestAccess`.

```swift iOS
 import OpenDOORCore

 let guestID = guest.id
 let lockID = lock.id
 do {
    let guests = try await client.revokeGuestAccess(guestID: guestID, lockID: lockID)
 } catch let error as SDKError {
    // Handle SDK errors
 } catch let error as NetworkError {
    // Handle network errors
 } catch let error as RevokeGuestError {
    // Handle revoke guest errors
 }
```

### Revoke all guest's accesses

To remove a guest's ability to unlock any DOOR lock call `revokeGuestAllAccesses`.

This method performs a best-effort operation. If some revocations fail, the operation may partially succeed and throws the first error encountered.

```swift iOS
 import OpenDOORCore

 let guestID = guest.id
 do {
    let guests = try await client.revokeGuestAllAccesses(guestID: guestID)
 } catch let error as SDKError {
    // Handle SDK errors
 } catch let error as NetworkError {
    // Handle network errors
 } catch let error as RevokeGuestError {
    // Handle revoke guest errors
 }
```

### Retrieve guest list

To get information for all guests with shared access call `guests`.

```swift iOS
 import OpenDOORCore

 do {
    let guests = try await client.guests()
 } catch let error as SDKError {
    // Handle SDK errors
 } catch let error as NetworkError {
    // Handle network errors
 }
```

## Log level

To control how much diagnostic information the SDK logs, call `setLogLevel`. It supports 4 levels:

1. `debug` - produce more detailed output. Includes debug, info, warning and error logs.
2. `info` - Includes info, warning and error logs.
3. `warning` - Includes warning and error logs.
4. `error` - restrict logs to important issues only. Includes only error logs.

<br />

Default log level is error.

```swift iOS
 import OpenDOORCore
 
 let logLevel = LogLevel.debug
 client.setLogLevel(logLevel)
```

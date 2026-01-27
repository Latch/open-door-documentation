---
title: OpenDOOR iOS SDK
excerpt: The SDK allows you to initialize and unlock a DOOR-supported lock.
deprecated: false
hidden: false
metadata:
  robots: index
---
## Setup

1. [Add OpenDOOR SDK as a dependency](https://opendoor-uwel.readme.io/docs/opendoor-ios-sdk#add-opendoor-sdk-as-a-dependency)
2. [Initialize the library](https://opendoor-uwel.readme.io/docs/opendoor-ios-sdk#initialize-the-library)
3. [Sign out](https://opendoor-uwel.readme.io/docs/opendoor-ios-sdk#sign-out)
4. [Get locks](https://opendoor-uwel.readme.io/docs/opendoor-ios-sdk#get-locks)
5. [Unlock](https://opendoor-uwel.readme.io/docs/opendoor-ios-sdk#unlock)
6. [Sync](https://opendoor-uwel.readme.io/docs/opendoor-ios-sdk#sync)
7. [Access logs](https://opendoor-uwel.readme.io/docs/opendoor-ios-sdk#access-logs)
8. [Guest Access](https://opendoor-uwel.readme.io/docs/opendoor-ios-sdk#guest-access)
9. [Log level](https://opendoor-uwel.readme.io/docs/opendoor-ios-sdk#log-level)

### Add OpenDOOR SDK as a dependency

1. In Xcode, select “File” → “Add Packages...”
2. Enter [https://github.com/Latch/opendoor-sdk-spm.git](https://github.com/Latch/opendoor-sdk-spm.git) or [git@github.com](mailto:git@github.com):Latch/opendoor-sdk-spm.git
3. Select OpenDOORCore library product

or you can add the following dependency to your Package.swift:

```swift iOS
.package(url: " https://github.com/Latch/opendoor-sdk-spm.git", from: "2.0.0")
```
```
```

and add it to your target like this:

```swift iOS
dependencies: [
  .product(name: "OpenDOORCore", package: "OpenDOORSDK")
]
```

### Initialize the library

Use your Auth0 token retrieved from DOOR's Auth endpoint, get an instance of OpenDOOR and call `setupWithToken()` with parameters:

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

Trying to call any function on OpenDOOR will throw SDKError.sdkNotInitialized error if this step is not done.

### Sign out

To clear all cached data and remove authentication token call `clear()`.
After calling `clear()`, the client must be set up again with setupWithToken().

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

* **`fetchLocks()`**: Waits for the server call to complete before returning. Does not return until the network request finishes (or fails). Use this when you need fresh data and can wait for the network call. Returns API results or cached values if API fails.
  If API request fails with token expired, a error will be thrown even if there is cached data.

* **`listenForLocks`**: Returns cached data immediately, then attempts to refresh from the server in the background. First are emitted cached locks, then updated locks when the server refresh completes. Use this when you want to show data quickly and update it when fresh data arrives. `listenForLocks` variants don't emit errors. They can be used to work offline.

Note:

Whenever the locks are retrieved from the server, also sync config data is synchronized in the background with the server.

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
The listner is weakly retained by the SDK. If you explitcly want to stop listening to locks updates, call `stopListenForLocks`.

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

Once it is started, it will continuously scan for nearby locks and will automatically unlock the first eligible lock found within range.

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
    }
 } catch let error as SDKError {
    // Handle SDK errors
 } 
```

**Option 2: Listen for unlock events (Combine Publisher)**

```swift iOS
 import OpenDOORCore

 do {
      unlockEventsSubscription = try client.unlockEventsPublisher()
                .receive(on: DispatchQueue.main)
                .sink { event in
                    // Use unlock event
                }

 } catch let error as SDKError {
        // Handle SDK errors
 }
```

**Option 3: Listen for unlock events (Callback listener)**

Note:
The listner is weakly retained by the SDK. If you explitcly want to stop listening to unlock events, call `stopListenForUnlockEvents`.

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

To shares access to the selected list of elligible locks (sharable) and to the entire path if building support this feature, with a guest, use `inviteGuest`.

A guest invitation can be created with temporary door code access or
in-app access with time-based restrictions.

```swift iOS
 import OpenDOORCore

 let lockIDs: [UUID] = <array of lock's ids with isSharable = true>
 do {
    try await client.inviteGuest(
                    firstName: "John",
                    lastName: Doe",
                    email: "john@example.com",
                    phone: "+1234567890",
                    lockIDs: lockIDs,
                    inviteType: inviteType
                )
 } catch let error as SDKError {
    // Handle SDK errors
 } catch let error as NetworkError {
    // Handle network errors
 } catch let error as InviteGuestError {
    // Handle invite guest errors
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

To remove a guest's ability to unlock any Door lock call `revokeGuestAllAccesses`.

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

To control how much diagnostic information the SDK logs, call `setLogLevel`.
It supports two levels:

1. `debug` - produce more detailed output.
2. `error` - restrict logs to important issues only.

Default log level is error.

```swift iOS
 import OpenDOORCore
 
 let logLevel = LogLevel.debug
 client.setLogLevel(logLevel)
```

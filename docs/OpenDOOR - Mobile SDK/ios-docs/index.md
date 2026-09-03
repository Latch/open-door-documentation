---
title: iOS SDK
excerpt: >-
  The SDK provides APIs to view, unlock and sync DOOR-supported locks and to
  manage guests accesses.
deprecated: false
hidden: false
icon: fab fa-apple
metadata:
  robots: index
---
## [Release notes](https://developers.door.com/docs/ios-release-notes)

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
.package(url: "https://github.com/Latch/opendoor-sdk-spm.git", from: "2.2.0")
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
          /// Unlock process has started.
          case started
          /// BLE connection established for setup sync.
          case connectForSetupSync(attempt: UnlockAttempt)
          /// Setup sync task completed (success or failure).
          case setupSync(attempt: UnlockAttempt)
          /// Sync package fetched from the network in the recovery flow.
          case updateSyncPackage
          /// BLE connection established for unlock.
          case connectForUnlock(attempt: UnlockAttempt)
          /// Unlocking task (firts attempt or recovery) in progress.
          case unlock(attempt: UnlockAttempt)
          /// Unlock failed.
          case failed(UnlockFailureReason)
          /// Unlock was canceled (e.g., when starting unlock for another lock).
          case canceled
          /// Lock was successfully unlocked.
          case success
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
                    /// Unlock process has started.
                    case started
                    /// BLE connection established for setup sync.
                    case connectForSetupSync(attempt: UnlockAttempt)
                    /// Setup sync task completed (success or failure).
                    case setupSync(attempt: UnlockAttempt)
                    /// Sync package fetched from the network in the recovery flow.
                    case updateSyncPackage
                    /// BLE connection established for unlock.
                    case connectForUnlock(attempt: UnlockAttempt)
                    /// Unlocking task (firts attempt or recovery) in progress.
                    case unlock(attempt: UnlockAttempt)
                    /// Unlock failed.
                    case failed(UnlockFailureReason)
                    /// Unlock was canceled (e.g., when starting unlock for another lock).
                    case canceled
                    /// Lock was successfully unlocked.
                    case success
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
    let accessLogs = try await client.getAccessLogs(lockID: lockID)
 } catch let error as SDKError {
    // Handle SDK errors
 } catch let error as NetworkError {
    // Handle network errors
 }
```

The list is returned in a single response. There are no paging or date-filter parameters.

### The AccessLog object

| Field | Type | Description |
| --- | --- | --- |
| `id` | `UUID` | Unique identifier of the log entry |
| `epochTimeForEntryAttempt` | `Int64` | Time of the event as a Unix timestamp in **seconds** |
| `method` | `AccessLogMethod` | How the lock/unlock was performed — see [Method values](#method-values) |
| `result` | `AccessLogResult` | Outcome of the attempt — see [Result values](#result-values) |
| `fullName` | `String?` | Display name associated with the credential used |
| `userFirstName` | `String?` | First name of the user, when the credential maps to a known user |
| `userLastName` | `String?` | Last name of the user |
| `userNickname` | `String?` | Nickname of the user, when one is set |
| `guestUUID` | `UUID?` | Identifier of the guest whose credential was used, when the event was guest-initiated |
| `lockUUID` | `UUID?` | Identifier of the lock the event occurred on |
| `photoAvailability` | `String?` | Whether an entry photo exists for the event — see [Photo availability](#photo-availability) |
| `imageFileName` | `String?` | File name of the entry photo, when one was captured |
| `imageToken` | `String?` | Token associated with the entry photo |

`id`, `epochTimeForEntryAttempt`, `method` and `result` are always present. Every other field can be `nil` on any entry: machine-generated events (scheduled locks, automatic re-locks) carry no identity fields, and failed attempts with no matching credential carry none either. Parse defensively.

### Method values

| Value | Meaning |
| --- | --- |
| `.ble` | Unlock over Bluetooth from a mobile app. Explicit unlock and proximity unlock both record this value — access logs do not distinguish them |
| `.bleLock` | Lock command over Bluetooth |
| `.nfc` | Unlock with an NFC credential (iOS) |
| `.androidNFC` | Unlock with an NFC credential (Android) |
| `.desfire` | Unlock with a DESFire keycard |
| `.passcode` | Unlock with a door code on the keypad |
| `.mko` | Unlock with a mechanical key override |
| `.tapToLock` | Lock triggered by tapping the keypad |
| `.mechanicalLock` | Manually/mechanically locked |
| `.scheduledUnlock` | Unlock triggered by a schedule |
| `.scheduledLock` | Lock triggered by a schedule |
| `.unknown` | Any method the SDK does not distinguish — includes manual unlocks at the device, inside-handle unlocks, automatic re-locks, diagnostic events, and methods newer than your SDK version |

### Result values

| Value | Meaning |
| --- | --- |
| `.success` | Successful unlock |
| `.guestSuccess` | Successful unlock using a guest credential |
| `.lockSuccess` | Successful lock — covers manual, Bluetooth, and automatic re-lock variants |
| `.incorrect` | Invalid credential (e.g. wrong door code) |
| `.deadboltApplied` | Entry blocked because the deadbolt/privacy mode was engaged |
| `.outsideQualifiedAccess` | Attempt outside the credential's allowed access window |
| `.unknownTimeFailure` | Rejected because the device could not verify the current time |
| `.nfcFailure` | NFC read/authentication failure |
| `.unknown` | Any outcome the SDK does not distinguish. This includes several lock-side failure states, so treat it as "outcome unavailable" — do not display it as a success or a failure |

### Photo availability

`photoAvailability` indicates whether an entry photo exists for the event. The SDK does not currently provide an API to download entry photos.

| Value | Meaning |
| --- | --- |
| `AVAILABLE` | An entry photo was captured |
| `UNAVAILABLE` | No photo available |
| `UNAVAILABLE_SETTINGS` | Photo capture disabled by device/property settings |
| `UNAVAILABLE_USER_DISABLED` | Photo capture disabled by the user |
| `UNAVAILABLE_LOW_POWER` | Photo skipped because the device battery was low |
| `UNAVAILABLE_NFC` | Photo not captured for this NFC interaction |

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

<br />
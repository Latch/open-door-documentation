---
title: Release notes
excerpt: iOS SDK release notes
deprecated: false
hidden: false
metadata:
  robots: index
---
## What's new in SDK 2.3.0

Android and iOS now share the same public API: the same types, methods, fields and error cases on both platforms. Only platform conventions differ: coroutines and `Flow` on Android, async/await and Combine on iOS, the `Activity` that Android setup takes, Android's `unlock(lock)` overload, and each platform's naming and error types.

**Breaking Changes**

* `AccessType` is removed, along with `accessType` on `InviteType`, `InAppInvite` and `TemporaryDoorcodeInvite`, and `InAppInvite.showDoorcodes`. Use `InAppInvite(startTime:endTime:)` and `TemporaryDoorcodeInvite(duration:period:)`. `endTime` no longer has a default value, so pass `nil` for an invite with no end time.
* `BluetoothError.bluetoothDisabled` is renamed to `.disabled`, and `.bluetoothPermissionDenied` to `.permissionDenied`.
* `AccessLogMethod.mechanical` is renamed to `.mechanicalLock`.
* `UnlockFailureReason.authFailed` and `.internal` now carry an `UnlockFailureError` with `code`, `message` and `context`. `.internal` no longer has a string payload, and `UnlockFailureReason` no longer conforms to `Error`.
* `PasscodeType` no longer has string raw values or `allCases`.
* Model properties on `Lock`, `Guest`, `GuestAccess`, `AccessLog`, `UnlockEvent`, `InAppInvite` and `TemporaryDoorcodeInvite` are now `let`. The initializers changed order to `UnlockEvent(lock:method:status:)`, `Lock(id:name:buildingID:startTime:endTime:doorCode:isShareable:)` and `GuestAccess(lockID:lockName:inviteType:passcodeType:startTime:endTime:)`.
* `InviteGuestError` adds `.shareableAccessRequired`, `.sharingNotEnabled` and `.requestedTimeOutsideShareableAccess`. Update exhaustive `switch` statements.

## What's new in SDK 2.2.0

**New Features**

* Redesigned unlock status reporting. The unlock flow now reports fine-grained, real-time status as an unlock progresses, with more specific success and failure outcomes.

  * now the UnlockEventStatus and UnlockFailureReason types have been reshaped to support this.

* Consumers observing unlock events will need to update their handling. Bounded timeout for sync downloads during unlock. Sync-package downloads performed as part of an unlock are now bounded by a timeout, so a slow or unresponsive network can no longer stall the unlock.

**Improvements**

* Skip unnecessary connections during unlock. An unlock no longer opens a BLE connection for setup sync when there is no lock data to sync, avoiding a wasted connection and making those unlocks faster.
* Faster failure handling. A failed or cancelled BLE operation now resolves immediately instead of waiting on a system timeout, removing a delay of several seconds before the outcome is reported.

**Bug Fixes**

* Fixed proximity (touch-to-unlock) scanning using a stale set of locks; the scan now stays in sync as the user's accessible locks change
* Fixed a case where one background lock sync could interrupt another, leaving a sync incomplete.

## What's new in SDK 2.1.0

* **New modern API:** Swift concurrency APIs with uniform errors
  * Lock and unlock events now use stream-based listeners instead of polling.
  * Unified unlock event pipeline for both explicit unlock and proximity unlock.
* **Setup sync visibility during unlock:** `UnlockEvent.SetupSync` is emitted when the SDK needs to run setup sync before unlocking, such as the first time a user opens a door and the lock needs access data.
* **Unlock cancellation:** `cancelUnlock()` cancels the active explicit unlock or the current proximity unlock attempt
* **Finer-grained log levels**

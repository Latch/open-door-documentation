---
title: Release notes
excerpt: iOS SDK release notes
deprecated: false
hidden: false
metadata:
  robots: index
---
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
- **Lock refresh also refreshes sync configuration,** and retries failed refreshes.
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

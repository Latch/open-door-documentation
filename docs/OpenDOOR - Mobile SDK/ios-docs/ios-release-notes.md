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

- **Shared cross-platform public contract.** The iOS public API now matches the OpenDOOR v2 contract shared with Android, so both SDKs expose the same models, errors and listeners.
  - ⚠️ **Breaking change:** Public models are reshaped.
    - `AccessLog`, `Guest`, `GuestAccess`, `InAppInvite` and similar types are now immutable (`let` instead of `var`).
    - `GuestAccess` now exposes `passcodeType` and `endTime`.
    - `AccessLogMethod.mechanical` is renamed `mechanicalLock`.
    - `BluetoothError.bluetoothDisabled` and `.bluetoothPermissionDenied` are renamed `.disabled` and `.permissionDenied`.
    - New unlock failure types are added: `UnlockFailureCode` and `UnlockFailureError`.
    - `AccessType`, the `accessType` property on `InviteType`, `InAppInvite` and `TemporaryDoorcodeInvite`, `showDoorcodes` and `GuestAccess.invitationID` are removed.
  - Recompile against 2.3.0 and update any switches over the renamed cases.

**Improvements**

- **More predictable Lock fetching.** `fetchLocks` now throws for an invalid or expired token. For other network failures it returns cached Locks when available, and throws the mapped network error when the cache is empty. Cancellation is preserved.
- **Clearer guest invite errors.** Sharing failures now say what to do: "User does not have permission to share access. Make sure the access was granted by the partner and is shareable." The new `shareableAccessRequired`, `sharingNotEnabled` and `requestedTimeOutsideShareableAccess` cases on `InviteGuestError` describe why an invite was rejected.
- **Remote logging backend changed.** The SDK no longer depends on Datadog. Diagnostic logs are sent over OpenTelemetry (OTLP/HTTP), with credentials, tokens and phone numbers scrubbed and log size capped. Consumers' dependency graphs drop the Datadog packages and gain `opentelemetry-swift` and `swift-protobuf`.

**Bug Fixes**

- Sync confirmations the server permanently rejects are no longer retried on every later sync. Previously a rejected confirmation was re-sent indefinitely.

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

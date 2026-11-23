---
title: Release notes
excerpt: iOS SDK release notes
deprecated: false
hidden: false
metadata:
  robots: index
---
## What's new in SDK 2.3.1

**Requirements**

- ⚠️ **Breaking change:** The SDK now requires iOS 16 or later. SDK 2.3.0 supported iOS 13.
  - Set your app's minimum deployment target to iOS 16 before you update.
- The Swift package still has no dependencies of its own, so updating adds nothing new to resolve.

**New Features**

- **Remote unlock.** Your app can now unlock a door remotely, through its intercom or a Door Scout.
  - `Lock.remoteUnlockMethods` lists the methods a Lock supports: `.intercom` and `.doorScout`. It's empty when the Lock supports neither.
  - `remoteUnlock(lockID:method:)` starts the unlock and returns right away. Progress and the result arrive through `listenForUnlockEvents()`, like other unlocks, with the method `.remoteIntercom` or `.remoteDoorScout`: `.started`, then `.success` or `.failed`.
  - The call throws `UnlockError.remoteUnlockNotSupported` when the Lock doesn't support the method, and `UnlockError.lockNotFound` when the Lock isn't known.
  - A remote unlock can't be canceled, and it runs independently of Bluetooth unlocks. A second call for the same Lock while one is running does nothing. `clear()` stops a running remote unlock.
  - The new failure reason `UnlockFailureReason.remoteUnlockNotAllowed` means the user can't unlock this door remotely.
  - Other failures arrive as `.internal`, with one of these new `UnlockFailureCode` values in the error's `code`: `remoteUnlockInProgress` (a remote unlock of this door is already running), `remoteUnlockFailed` (the door reported a failure), `remoteUnlockTimedOut` (no result within 20 seconds for an intercom or 60 seconds for a Door Scout; the door may still open) or `networkError`.
- **Intercom call settings.**
  - `getIntercomSettings()` returns one `IntercomSettings` per building the user lives in, with `buildingID`, `contactPreference` (`.app`, `.phone` or `.unit`) and `phoneNumber`.
  - `enableIntercomPhoneCalls(buildingID:)` turns on intercom calls by phone for one building and returns that building's updated settings. Pass `Lock.buildingID`. It throws `IntercomSettingsError.noPhoneNumber` when the user has no phone number on file. Users can turn phone calls off only in the DOOR App.
- **Lock timezone.** `Lock.timeZone` is the Lock's IANA timezone ID, such as `America/New_York`. It's the phone's timezone when DOOR has no timezone for the Lock, and for every Lock when you set up the SDK with `includeAllLocks: false`.
- **Updated public types.**
  - ⚠️ **Breaking change:** Existing public types gain new members.
    - `Lock`'s initializer now requires `timeZone` and `remoteUnlockMethods`.
    - `DOORClient` adds `remoteUnlock(lockID:method:)`, `getIntercomSettings()` and `enableIntercomPhoneCalls(buildingID:)`.
    - New enum cases: `UnlockEventMethod.remoteIntercom` and `.remoteDoorScout`, `UnlockFailureReason.remoteUnlockNotAllowed`, `UnlockError.remoteUnlockNotSupported`, and `UnlockFailureCode.networkError`, `.remoteUnlockInProgress`, `.remoteUnlockFailed` and `.remoteUnlockTimedOut`.
  - Pass both new values wherever you create a `Lock`, for example in tests. Add the three methods to any type of your own that conforms to `DOORClient`, such as a test double. Handle the new cases in any `switch` over these enums.

**Improvements**

- **Clearer network error text.** The description of `NetworkError.payloadError` now reads "Network error with a message from the server", followed by the server's message.

**Bug Fixes**

- `clear()` and `setupWithToken` no longer delete passwords or tokens that your app saved on the device. Only the SDK's own sign-in data is removed.
- Temporary doorcode invites for Today or Tomorrow now follow the Lock's day, not the phone's. Before, when the phone's timezone was ahead of the Lock's, a Tomorrow code could already work today at the Lock. For an invite to several Locks, the first shareable Lock in `lockIDs` sets the day. When `Lock.timeZone` is the phone's timezone, the phone's day is used, as before. `InAppInvite` is unchanged: it still uses the exact start and end times you pass.
- Tapping Terms of Service or Privacy Policy in the consent prompt now only opens the page. When the user comes back, the prompt is still open, and only Agree or Disagree closes it. Before, the tap counted as Disagree and `setupWithToken` threw `SetupError.consentNotGranted`.
- If the consent prompt can't be shown, or your app closes it before the user answers, `setupWithToken` now throws `SetupError.consentNotGranted`. Before, it never returned.
- The SDK now waits for the user to accept the terms before it links analytics and diagnostic data to that user. Before, a user who declined, or whose consent request failed, was already linked.
- `OpenDOOR.getInstance()` no longer crashes when the SDK's resource bundle is missing from your app. `setupWithToken` throws `SetupError.setupInternalError` instead, and the other calls throw `SDKError.sdkInternalError`.

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

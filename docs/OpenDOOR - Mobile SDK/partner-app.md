---
title: Partner App
excerpt: Responsible for hosting the DOOR IOS/ADR SDK.
deprecated: false
hidden: false
icon: far fa-mobile-arrow-down
metadata:
  robots: index
---
## User Consent

To utilize DOOR Services, all users must adhere to and accept DOOR Terms of Service and Privacy Policies. This applies to users of the DOOR App on all platforms including users of any Partner App that utilizes the DOOR SDK.

During setup, the OpenDOOR SDK will display its own dialog requesting the user’s consent to the DOOR [Terms of Service](https://www.door.com/terms-of-service)  and [Privacy Policy](https://www.door.com/privacy-policy) . The dialog will provide links to [door.com](http://door.com/)  where the user can review the Terms of Service and Privacy Policy. The user will have the opportunity to Agree or Disagree with the DOOR terms. If the user agrees to the terms the SDK will continue to function as intended and provide the ability to Unlock. If the user disagrees, `setupWithToken` throws `SetupException.ConsentNotGrantedException` (Android) or `SetupError.consentNotGranted` (iOS).

The user’s acceptance will be needed by the OpenDOOR SDK where it will be securely stored and transmitted to the DOOR BE for permanent persistence. The SDK will look for the user’s acceptance and consent either locally or from the DOOR BE and will not fulfill any requests from the Partner App until the User Acceptance has been provided or retrieved from persistence.

> The consent will be gathered only once from the End User, not per device.

| ![Devices](https://files.readme.io/384935a6b1ae5dc022bdd82a53d426e0e5ff82594b71aba960f22468893016c4-consent_android.png) | ![Devices](https://files.readme.io/59fb6e0ed1fa1758269a852dc8729755c994e0a5047df8e357cbe955c55da5d8-consent_ios.png) |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Android dialog                                                                                                           | iOS dialog                                                                                                           |

## Supported Platforms

The OpenDOOR SDKs will support the following versions of IOS and Android. Post the Beta period, all versions of IOS/Android currently supported by the DOOR App will also be supported.

| Platform | SDK Beta          |
| -------- | ----------------- |
| iOS      | Current to iOS 13 |
| Android  | Current to ADR 8  |

## Communications

The DOOR  SDK will execute its own communication protocol with DOOR services and fetch the relevant information to allow Partner Apps to build a list of Doors and Locks. All fetched information will be directly stored in the mobile storage. The OpenDOOR SDK will internally manage its own encrypted database storage. Typical storage needs for the OpenDOOR SDK should not exceed 10MB.

## Bluetooth

Beyond standard internet-based connectivity requirements, the OpenDOOR SDK heavily utilizes Bluetooth protocols to communicate with DOOR Lock devices. The Partner App will not need to implement BT on its own as the OpenDOOR SDK will encapsulate all necessary protocols and be responsible for scanning for a device, connecting to a device, setting up a device, and unlocking a device.

The Partner App however will need to ensure users have granted appropriate permissions to Bluetooth (iOS and Android) for the Partner App. Without these permissions granted, the OpenDOOR SDK will not be able to function.

## Permissions

The OpenDOOR SDK requires specific permissions from the user in order to function properly. The SDK will ask for these permissions upon initialization. On Android it asks during `setupWithToken`. On iOS the system shows the Bluetooth prompt when the App first calls `OpenDOOR.getInstance()`. As an example, if the user denies the Bluetooth permission, `unlock` throws `BluetoothException.BluetoothPermissionDeniedException` (Android) or `BluetoothError.permissionDenied` (iOS) for the App to handle. At this point, on Android the App can call `setupWithToken` again so permissions can be requested by the SDK. On iOS the system asks only once, so the user has to allow Bluetooth for the App in Settings.

The following are a list of permissions that the SDK requests from the user:

* Bluetooth
* Location service (for older Android versions)

## Setup and Initialization

```
setupWithToken(activity, token, includeAllLocks)   // Android
setupWithToken(token:includeAllLocks:)             // iOS
```

Authenticates and initializes the OpenDOOR SDK. Call it on the shared client: `OpenDOOR.instance` on Android, `await OpenDOOR.getInstance()` on iOS. The OpenDOOR SDK requires the current user to agree to DOOR's Terms & Conditions and Privacy Policy. If the current user hasn't agreed yet, the SDK presents its own consent dialog.

**Parameters**

* `activity` (Android only): Foreground `Activity` that can host the setup UI.
* `token`: Authorization token for the current user.
* `includeAllLocks`: `true` loads all locks the user can access, partner and non-partner. `false` loads only partner-managed locks.

**Returns**

* On success returns Void. Otherwise, throws an error.

  All additional SDK functions require that `setupWithToken(...)` has completed with a valid token. If it hasn't, requests to the SDK throw `SDKException.SDKNotInitializedException` (Android) or `SDKError.sdkNotInitialized` (iOS). If the token is invalid or expired, calls such as `fetchLocks()` throw `NetworkException.InvalidTokenException` (Android) or `NetworkError.invalidToken` (iOS). Partner App can receive the error, supply a new token to `setupWithToken(...)`, and then continue to use the SDK functions.

  **Errors**

  | Android                                     | iOS                             | Description                                                          |
  | ------------------------------------------- | ------------------------------- | -------------------------------------------------------------------- |
  | `SetupException.InvalidTokenException`      | `SetupError.invalidToken`       | The supplied authorization token is invalid and should be refreshed. |
  | `SetupException.ConsentNotGrantedException` | `SetupError.consentNotGranted`  | The current user didn't agree to DOOR's terms.                       |
  | `SetupException.SetupInternalException`     | `SetupError.setupInternalError` | Setup failed internally.                                             |
  | `NetworkException`                          | `NetworkError`                  | No user is stored yet and the configuration can't be fetched.        |
  | `IllegalArgumentException`                  | n/a                             | Android only: the `activity` can't host the setup UI.                |

## Doors and Locks

```
fetchLocks()
listenForLocks()
```

Retrieve all locks accessible to the current user. This list can be used to build out a UI/UX flow however the Partner deems necessary.

* `fetchLocks()` refreshes the locks from the network and updates the cache. An invalid or expired token always fails. Other network failures return the cached locks, and fail only when the cache is empty.
* `listenForLocks()` emits the cached locks first, even an empty list, then every update, and starts a refresh in the background. The stream has no error channel. Both platforms also have a listener variant, and iOS has `listenForLocksPublisher()` for Combine.

**Returns**

* On success `fetchLocks()` returns a collection of `Lock`. Otherwise, throws an error. `listenForLocks()` returns a stream of `Lock` collections (`Flow` on Android, `AsyncStream` on iOS).

  `Lock`

  | Name   | Type   | Description           |
  | ------ | ------ | --------------------- |
  | `id`   | UUID   | Unique Identifier     |
  | `name` | String | Name of the lock/door |

**Errors**

| Android                                   | iOS                          | Description                                                                         |
| ----------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------- |
| `SDKException.SDKNotInitializedException` | `SDKError.sdkNotInitialized` | `setupWithToken(...)` hasn't completed.                                             |
| `NetworkException.InvalidTokenException`  | `NetworkError.invalidToken`  | `fetchLocks()` only: the token is invalid or expired, even when cached locks exist. |
| `NetworkException`                        | `NetworkError`               | `fetchLocks()` only: any other network failure while the cache is empty.            |

## Unlock

```
unlock(lockId)    // Android, also unlock(lock)
unlock(lockID:)   // iOS
```

Use BLE to scan for a specific DOOR device and explicitly unlock the device.

Performing BLE operations requires the user to grant the app permission to use native Bluetooth APIs. This will result in a system modal to be presented on first use.

**Parameters**

* `lockId` (iOS: `lockID`): The `id` of the Lock (device) to start scanning for and Unlock.

**Returns**

Nothing. Progress and the result arrive as unlock events from `listenForUnlockEvents()`, so start listening before you call `unlock`. The result is reported in the event `status`: `Success`, `Failed` with an `UnlockFailureReason`, or `Canceled` (iOS: `.success`, `.failed`, `.canceled`).

**Remarks**

On Android, `unlock(lock)` also accepts the current `Lock` model. iOS has only `unlock(lockID:)`.

Only one unlock runs at a time. A new `unlock` call cancels the one in progress.

**Errors**

Thrown by `unlock`:

| Android                                                 | iOS                               | Description                                                                |
| ------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------- |
| `SDKException.SDKNotInitializedException`               | `SDKError.sdkNotInitialized`      | `setupWithToken(...)` hasn't completed.                                    |
| `BluetoothException.BluetoothDisabledException`         | `BluetoothError.disabled`         | The current device does not have Bluetooth enabled.                        |
| `BluetoothException.BluetoothPermissionDeniedException` | `BluetoothError.permissionDenied` | User denied OpenDOOR SDK access to use the device's Bluetooth.             |
| `UnlockException.LockNotFoundException`                 | `UnlockError.lockNotFound`        | Failed to find a lock with a unique identifier matching the given lock ID. |

Reported on the unlock event stream as the `Failed` reason:

| Android             | iOS                  | Description                                                       |
| ------------------- | -------------------- | ----------------------------------------------------------------- |
| `BluetoothDisabled` | `.bluetoothDisabled` | Bluetooth is turned off on the device.                            |
| `OutOfSchedule`     | `.outOfSchedule`     | Access was attempted outside the lock's access schedule.          |
| `LockNotFound`      | `.lockNotFound`      | No lock matching the requested ID was discovered.                 |
| `ConnectionFailed`  | `.connectionFailed`  | The lock was discovered but a connection couldn't be established. |
| `AuthFailed(error)` | `.authFailed(error)` | The lock rejected the credential, or recovery sync failed.        |
| `Internal(error)`   | `.internal(error)`   | Any other failure. `error.code` gives the cause.                  |
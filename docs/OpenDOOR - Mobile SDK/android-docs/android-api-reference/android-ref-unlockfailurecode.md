---
title: UnlockFailureCode
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Cause of an unlock failure that has no more specific reason.

## Declaration

```kotlin
enum class UnlockFailureCode {

    BLUETOOTH_UNAVAILABLE,
    DEVICE_NOT_SUPPORTED,
    KEY_FETCH_FAILED,
    SETUP_SYNC_FAILED,
    TRANSPORT_ERROR,
    UNEXPECTED,
    NETWORK_ERROR,
    REMOTE_UNLOCK_IN_PROGRESS,
    REMOTE_UNLOCK_FAILED,
    REMOTE_UNLOCK_TIMED_OUT,
}
```

## BLUETOOTH_UNAVAILABLE

The device has no usable Bluetooth hardware.

## DEVICE_NOT_SUPPORTED

The lock model does not support BLE unlock.

## KEY_FETCH_FAILED

The signed key could not be fetched before the unlock started.

## SETUP_SYNC_FAILED

Setup sync did not complete.

## TRANSPORT_ERROR

A Bluetooth operation failed, with no more specific classification.

## UNEXPECTED

A failure the SDK does not account for.

## NETWORK_ERROR

A network request failed or returned an error.

## REMOTE_UNLOCK_IN_PROGRESS

A remote unlock of this door is already in progress.

## REMOTE_UNLOCK_FAILED

The door reported that the remote unlock failed.

## REMOTE_UNLOCK_TIMED_OUT

No remote unlock result arrived in time. The door may still open.

Package: `com.door.opendoor.android.core.api.model`.

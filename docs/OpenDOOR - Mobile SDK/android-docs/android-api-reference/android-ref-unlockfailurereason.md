---
title: UnlockFailureReason
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Reasons why an unlock can fail

## Declaration

```kotlin
enum class UnlockFailureReason {
    BluetoothDisabled,

    BluetoothError,

    LockNotFound,

    LockNotRecognized,

    OutOfSchedule,

    Timeout,

    InternalError
}
```

## BluetoothError

Bluetooth error occurred (e.g., GATT 133)

## LockNotFound

Failed to find a lock with a unique identifier matching the given lock ID.

## LockNotRecognized

The supplied lock model is not recognized by the current SDK cache.

## OutOfSchedule

Access attempted outside of device access schedule

## Timeout

Unlock failed to complete in a reasonable amount of time.

## InternalError

An internal error occurred

Package: `com.door.opendoor.android.core.api.model`.

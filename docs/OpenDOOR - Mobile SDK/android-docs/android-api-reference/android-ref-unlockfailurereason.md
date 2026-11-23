---
title: UnlockFailureReason
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Canonical reason an in-flight unlock failed.

## Declaration

```kotlin
sealed class UnlockFailureReason {
    data class AuthFailed(val error: UnlockFailureError) : UnlockFailureReason
    data object BluetoothDisabled : UnlockFailureReason
    data object ConnectionFailed : UnlockFailureReason
    data class Internal(val error: UnlockFailureError) : UnlockFailureReason
    data object LockNotFound : UnlockFailureReason
    data object OutOfSchedule : UnlockFailureReason
    data object RemoteUnlockNotAllowed : UnlockFailureReason
}
```

## AuthFailed

The lock rejected the credential, or recovery sync failed. The payload carries the cause.

## BluetoothDisabled

Bluetooth is turned off on the device.

## ConnectionFailed

The lock was discovered but a connection could not be established.

## Internal

A failure with no more specific reason. The payload carries the cause.

## LockNotFound

No lock matching the requested identifier was discovered.

## OutOfSchedule

Access was attempted outside the access schedule for the lock.

## RemoteUnlockNotAllowed

The user can't unlock this door remotely.

## Related types

- [UnlockFailureError](doc:android-ref-unlockfailureerror)

Package: `com.door.opendoor.android.core.api.model`.

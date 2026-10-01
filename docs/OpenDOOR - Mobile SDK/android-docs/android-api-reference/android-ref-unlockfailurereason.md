---
title: UnlockFailureReason
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Canonical reason an in-flight unlock failed.

## Declaration

```kotlin
sealed class UnlockFailureReason {

    data object BluetoothDisabled : UnlockFailureReason()

    data object OutOfSchedule : UnlockFailureReason()

    data object LockNotFound : UnlockFailureReason()

    data object ConnectionFailed : UnlockFailureReason()

    data class AuthFailed(val error: UnlockFailureError) : UnlockFailureReason()

    data class Internal(val error: UnlockFailureError) : UnlockFailureReason()
}
```

## BluetoothDisabled

Bluetooth is turned off on the device.

## OutOfSchedule

Access was attempted outside the access schedule for the lock.

## LockNotFound

No lock matching the requested identifier was discovered.

## ConnectionFailed

The lock was discovered but a connection could not be established.

## AuthFailed

The lock rejected the credential, or recovery sync failed. The payload carries the cause.

## Internal

A failure with no more specific reason. The payload carries the cause.

## Related types

- [UnlockEventStatus](doc:android-ref-unlockeventstatus)
- [UnlockFailureError](doc:android-ref-unlockfailureerror)

Package: `com.door.opendoor.android.core.api.model`.

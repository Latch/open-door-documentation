---
title: BluetoothException
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Bluetooth access failure.

## Declaration

```kotlin
sealed class BluetoothException(message: String, throwable: Throwable? = null) : Exception(message, throwable) {

    class BluetoothDisabledException(message: String = "Bluetooth is disabled", throwable: Throwable? = null) : BluetoothException(message, throwable)

    class BluetoothPermissionDeniedException(message: String = "Bluetooth permission was denied", throwable: Throwable? = null) : BluetoothException(message, throwable)
}
```

## BluetoothDisabledException

The current device does not have Bluetooth enabled

## BluetoothPermissionDeniedException

User denied OpenDOOR SDK access to use the device's Bluetooth

## Related types

- [OpenDOOR](doc:android-ref-opendoor)

Package: `com.door.opendoor.android.core.api.exceptions`.

---
title: BluetoothException
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Bluetooth access failure.

## Declaration

```kotlin
sealed class BluetoothException(message: String, throwable: Throwable? = null) : Exception {
    class BluetoothDisabledException(message: String = "Bluetooth is disabled", throwable: Throwable? = null) : BluetoothException
    class BluetoothPermissionDeniedException(message: String = "Bluetooth permission was denied", throwable: Throwable? = null) : BluetoothException
}
```

## BluetoothDisabledException

Bluetooth is disabled.

## BluetoothPermissionDeniedException

Bluetooth permission was denied.

Package: `com.door.opendoor.android.core.api.exceptions`.

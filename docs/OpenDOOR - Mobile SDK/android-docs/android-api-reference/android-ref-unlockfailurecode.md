---
title: UnlockFailureCode
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Cause of an unlock failure that has no more specific reason.

- **`BLUETOOTH_UNAVAILABLE`** — The device has no usable Bluetooth hardware.
- **`DEVICE_NOT_SUPPORTED`** — The lock model does not support BLE unlock.
- **`KEY_FETCH_FAILED`** — The signed key could not be fetched before the unlock started.
- **`SETUP_SYNC_FAILED`** — Setup sync did not complete.
- **`TRANSPORT_ERROR`** — A Bluetooth operation failed, with no more specific classification.
- **`UNEXPECTED`** — A failure the SDK does not account for.

## Declaration

```kotlin
enum class UnlockFailureCode(val value: String) {
    BLUETOOTH_UNAVAILABLE("BLUETOOTH_UNAVAILABLE"),
    DEVICE_NOT_SUPPORTED("DEVICE_NOT_SUPPORTED"),
    KEY_FETCH_FAILED("KEY_FETCH_FAILED"),
    SETUP_SYNC_FAILED("SETUP_SYNC_FAILED"),
    TRANSPORT_ERROR("TRANSPORT_ERROR"),
    UNEXPECTED("UNEXPECTED"),
}
```

Package: `com.door.opendoor.android.core.api.model`.

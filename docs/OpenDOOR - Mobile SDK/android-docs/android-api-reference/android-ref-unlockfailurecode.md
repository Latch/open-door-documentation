---
title: UnlockFailureCode
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Cause of an unlock failure that has no more specific reason.

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

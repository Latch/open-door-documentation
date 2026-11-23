---
title: UnlockFailureError
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Detail for an unlock failure.

- **`code`** — Cause of the failure.
- **`message`** — Human-readable description of the failure.
- **`context`** — Platform error code, such as a lock response code, a GATT status or an HTTP status.

## Declaration

```kotlin
data class UnlockFailureError(
    val code: UnlockFailureCode,
    val message: String,
    val context: String?,
)
```

## Related types

- [UnlockFailureCode](doc:android-ref-unlockfailurecode)

Package: `com.door.opendoor.android.core.api.model`.

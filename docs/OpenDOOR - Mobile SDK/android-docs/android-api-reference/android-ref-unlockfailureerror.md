---
title: UnlockFailureError
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Detail for an unlock failure.

## Declaration

```kotlin
data class UnlockFailureError(
    val code: UnlockFailureCode,
    val message: String,
    val context: String?,
) {
    override fun toString(): String
}
```

## Related types

- [UnlockFailureCode](doc:android-ref-unlockfailurecode)

Package: `com.door.opendoor.android.core.api.model`.

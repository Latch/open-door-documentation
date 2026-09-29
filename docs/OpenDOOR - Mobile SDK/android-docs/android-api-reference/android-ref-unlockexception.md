---
title: UnlockException
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Explicit unlock request failure before an attempt starts.

## Declaration

```kotlin
sealed class UnlockException(message: String, throwable: Throwable? = null) : Exception(message, throwable) {

    class LockNotFoundException(val identifier: String, message: String = "Lock not found before unlock starts: $identifier", throwable: Throwable? = null) : UnlockException(message, throwable)
}
```

## Related types

- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.exceptions`.

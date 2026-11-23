---
title: UnlockException
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Explicit unlock request failure before an attempt starts.

## Declaration

```kotlin
sealed class UnlockException(message: String, throwable: Throwable? = null) : Exception {
    class LockNotFoundException(val identifier: String, message: String = "Lock not found before unlock starts: ", throwable: Throwable? = null) : UnlockException
    class RemoteUnlockNotSupportedException(val identifier: String, message: String = "The lock does not support the requested remote unlock method: ", throwable: Throwable? = null) : UnlockException
}
```

## LockNotFoundException

Lock not found before unlock starts.

## RemoteUnlockNotSupportedException

The lock does not support the requested remote unlock method.

## Related types

- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.exceptions`.

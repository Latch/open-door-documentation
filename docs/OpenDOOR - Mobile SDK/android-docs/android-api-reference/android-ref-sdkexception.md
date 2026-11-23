---
title: SDKException
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

General SDK access failure.

## Declaration

```kotlin
sealed class SDKException(message: String, throwable: Throwable? = null) : Exception {
    class InternalException(message: String, throwable: Throwable? = null) : SDKException
    class SDKNotInitializedException(message: String = "The SDK has not been initialized with setupWithToken", throwable: Throwable? = null) : SDKException
}
```

## InternalException

An internal SDK error occurred.

## SDKNotInitializedException

The SDK has not been initialized with setupWithToken.

Package: `com.door.opendoor.android.core.api.exceptions`.

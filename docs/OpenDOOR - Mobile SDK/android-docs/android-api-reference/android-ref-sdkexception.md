---
title: SDKException
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Base exception for SDK failures

## Declaration

```kotlin
sealed class SDKException(message: String, throwable: Throwable? = null) : Exception(message, throwable) {

    class SDKNotInitializedException(message: String, throwable: Throwable? = null) : SDKException(message, throwable)

    class InternalException(message: String, throwable: Throwable? = null) : SDKException(message, throwable)
}
```

## SDKNotInitializedException

The SDK has not been initialized with setupWithToken

## InternalException

An internal error occurred

Package: `com.door.opendoor.android.core.api.exceptions`.

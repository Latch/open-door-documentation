---
title: NetworkException
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Network access failure.

## Declaration

```kotlin
sealed class NetworkException(message: String, throwable: Throwable? = null) : Exception {
    class InternalNetworkException(message: String, throwable: Throwable? = null) : NetworkException
    class InvalidTokenException(message: String = "The supplied token is invalid or expired", throwable: Throwable? = null) : NetworkException
    class PayloadError(message: String, throwable: Throwable? = null) : NetworkException
}
```

## InternalNetworkException

Internal network error.

## InvalidTokenException

The supplied token is invalid or expired.

## PayloadError

Network error with a message from the server.

Package: `com.door.opendoor.android.core.api.exceptions`.

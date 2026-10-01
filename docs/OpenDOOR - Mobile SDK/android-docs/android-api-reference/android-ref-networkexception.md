---
title: NetworkException
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Network access failure.

## Declaration

```kotlin
sealed class NetworkException(message: String, throwable: Throwable? = null) : Exception(message, throwable) {

    class InvalidTokenException(message: String = "The supplied token is invalid or expired", throwable: Throwable? = null) : NetworkException(message, throwable)

    class PayloadError(message: String, throwable: Throwable? = null) : NetworkException(message, throwable)

    class InternalNetworkException(message: String, throwable: Throwable? = null) : NetworkException(message, throwable)
}
```

## InvalidTokenException

The supplied authorization token is invalid and should be refreshed.

## PayloadError

Network error with a message from the server.

## InternalNetworkException

Internal network error (404, parsing errors, etc)

Package: `com.door.opendoor.android.core.api.exceptions`.

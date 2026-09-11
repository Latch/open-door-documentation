---
title: NetworkException
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Base exception for network failures

## Declaration

```kotlin
sealed class NetworkException(message: String, throwable: Throwable? = null) : Exception(message, throwable) {

    class PayloadError(message: String, throwable: Throwable? = null) : NetworkException(message, throwable)

    class InternalNetworkException(message: String, throwable: Throwable? = null) : NetworkException(message, throwable)

    class InvalidTokenException(message: String, throwable: Throwable? = null) : NetworkException(message, throwable)
}
```

## PayloadError

Network error with message from backend

## InternalNetworkException

Internal network error (404, parsing errors, etc)

## InvalidTokenException

The supplied authorization token is invalid and should be refreshed.

## Related types

- [PayloadError](doc:android-ref-payloaderror)

Package: `com.door.opendoor.android.core.api.exceptions`.

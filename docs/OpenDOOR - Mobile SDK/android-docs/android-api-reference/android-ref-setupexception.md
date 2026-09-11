---
title: SetupException
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Base exception for setup failures

## Declaration

```kotlin
sealed class SetupException(message: String, throwable: Throwable? = null) : Exception(message, throwable) {

    class InvalidTokenException(message: String, throwable: Throwable? = null) : SetupException(message, throwable)

    class ConsentNotGrantedException(message: String, throwable: Throwable? = null) : SetupException(message, throwable)

    class SetupInternalException(message: String, throwable: Throwable? = null) : SetupException(message, throwable)
}
```

## InvalidTokenException

The supplied authorization token is invalid and should be refreshed.

## ConsentNotGrantedException

User consent not granted

## SetupInternalException

An internal error occurred

Package: `com.door.opendoor.android.core.api.exceptions`.

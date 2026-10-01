---
title: SetupException
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Setup failure.

## Declaration

```kotlin
sealed class SetupException(message: String, throwable: Throwable? = null) : Exception(message, throwable) {

    class InvalidTokenException(message: String = "The supplied token is invalid or expired", throwable: Throwable? = null) : SetupException(message, throwable)

    class ConsentNotGrantedException(message: String = "User consent was not granted", throwable: Throwable? = null) : SetupException(message, throwable)

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

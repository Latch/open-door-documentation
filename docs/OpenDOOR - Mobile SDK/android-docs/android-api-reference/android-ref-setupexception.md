---
title: SetupException
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Setup failure.

## Declaration

```kotlin
sealed class SetupException(message: String, throwable: Throwable? = null) : Exception {
    class ConsentNotGrantedException(message: String = "User consent was not granted", throwable: Throwable? = null) : SetupException
    class InvalidTokenException(message: String = "The supplied token is invalid or expired", throwable: Throwable? = null) : SetupException
    class SetupInternalException(message: String, throwable: Throwable? = null) : SetupException
}
```

## ConsentNotGrantedException

User consent was not granted.

## InvalidTokenException

The supplied token is invalid or expired.

## SetupInternalException

An internal setup error occurred.

Package: `com.door.opendoor.android.core.api.exceptions`.

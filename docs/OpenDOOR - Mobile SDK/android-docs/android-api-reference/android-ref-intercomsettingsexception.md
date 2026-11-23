---
title: IntercomSettingsException
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Intercom settings failure.

## Declaration

```kotlin
sealed class IntercomSettingsException(message: String, throwable: Throwable? = null) : Exception {
    class NoPhoneNumberException(message: String = "The user has no phone number on file", throwable: Throwable? = null) : IntercomSettingsException
}
```

## NoPhoneNumberException

The user has no phone number on file.

Package: `com.door.opendoor.android.core.api.exceptions`.

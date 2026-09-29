---
title: RevokeGuestException
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Guest-access revocation failure.

## Declaration

```kotlin
sealed class RevokeGuestException(message: String, throwable: Throwable? = null) : Exception(message, throwable) {

    class PasscodeTypeCantBeRevokedException(message: String = "This passcode type cannot be revoked", throwable: Throwable? = null) : RevokeGuestException(message, throwable)

    class DeviceNotFoundException(message: String = "Device was not found", throwable: Throwable? = null) : RevokeGuestException(message, throwable)

    class InternalException(message: String, throwable: Throwable? = null) : RevokeGuestException(message, throwable)
}
```

Package: `com.door.opendoor.android.core.api.exceptions`.

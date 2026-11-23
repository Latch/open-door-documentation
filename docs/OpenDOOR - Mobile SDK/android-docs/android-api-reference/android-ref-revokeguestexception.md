---
title: RevokeGuestException
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Guest-access revocation failure.

## Declaration

```kotlin
sealed class RevokeGuestException(message: String, throwable: Throwable? = null) : Exception {
    class DeviceNotFoundException(message: String = "Device was not found", throwable: Throwable? = null) : RevokeGuestException
    class InternalException(message: String, throwable: Throwable? = null) : RevokeGuestException
    class PasscodeTypeCantBeRevokedException(message: String = "This passcode type cannot be revoked", throwable: Throwable? = null) : RevokeGuestException
}
```

## DeviceNotFoundException

Device was not found.

## InternalException

Internal revocation error.

## PasscodeTypeCantBeRevokedException

This passcode type cannot be revoked.

Package: `com.door.opendoor.android.core.api.exceptions`.

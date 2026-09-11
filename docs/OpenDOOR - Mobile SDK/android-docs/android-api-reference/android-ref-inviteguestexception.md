---
title: InviteGuestException
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Exception thrown when inviting a guest fails due to a known business rule.

## Declaration

```kotlin
class InviteGuestException(
    val reason: Reason,
    message: String = reason.message,
    cause: Throwable? = null,
) : Exception(message, cause) {
    enum class Reason(val message: String) {
        EMAIL_REQUIRED_FOR_PERMANENT("Email is required for permanent access"),
        EMAIL_OR_PHONE_REQUIRED("Either email or phone number must be provided"),
        EMAIL_AND_PHONE_PROVIDED("Both email and phone cannot be provided. Please provide only one."),
        INVALID_PHONE("Invalid phone number format"),
        INVALID_START_TIME("Invalid start time provided"),
        END_TIME_NOT_SUPPORTED("End time is not supported for this invite type"),
        USER_CAN_NOT_SHARE("User does not have permission to share access"),
    }
}
```

Package: `com.door.opendoor.android.core.api.exceptions`.

---
title: InviteGuestException
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Guest invitation business-rule failure.

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
        USER_CAN_NOT_SHARE(
            "User does not have permission to share access. " +
                "Make sure the access was granted by the partner and is shareable.",
        ),
        SHAREABLE_ACCESS_REQUIRED(
            "No active shareable access to this lock. " +
                "Make sure the user's access is active and shareable.",
        ),
        SHARING_NOT_ENABLED(
            "Sharing is not enabled for this access. " +
                "Ask the partner to grant the access with sharing enabled.",
        ),
        REQUESTED_TIME_OUTSIDE_SHAREABLE_ACCESS(
            "The requested guest time range is outside the user's shareable access window. " +
                "Choose a time range the user's access covers.",
        ),
    }
}
```

Package: `com.door.opendoor.android.core.api.exceptions`.

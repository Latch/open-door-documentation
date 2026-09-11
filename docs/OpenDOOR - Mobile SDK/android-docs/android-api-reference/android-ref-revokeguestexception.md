---
title: RevokeGuestException
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Exception thrown when revoking guest access fails due to a known business rule.

## Declaration

```kotlin
class RevokeGuestException(
    val reason: Reason,
    message: String = "Failed to revoke guest access: ${reason.name}",
    cause: Throwable? = null,
) : Exception(message, cause) {
    enum class Reason {
        PASSCODE_TYPE_CANT_BE_REVOKED,
        UNKNOWN,
    }
}
```

Package: `com.door.opendoor.android.core.api.exceptions`.

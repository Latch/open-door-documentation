---
title: InviteGuestException
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Guest invitation business-rule failure.

## Declaration

```kotlin
class InviteGuestException(
    val reason: InviteGuestException.Reason,
    message: String = reason.message,
    cause: Throwable? = null,
) : Exception {
    enum Reason : Enum<InviteGuestException.Reason>
}
```

## Reason

Package: `com.door.opendoor.android.core.api.exceptions`.

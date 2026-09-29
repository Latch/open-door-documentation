---
title: GuestInvitesException
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Partial or complete guest-invitation failure.

## Declaration

```kotlin
class GuestInvitesException(
    val failedLockErrors: List<LockActionException>,
    val successfulLockIds: List<UUID>,
    message: String = buildMessage(failedLockErrors, successfulLockIds),
) : Exception(message) {
    val failedLockIds: List<UUID>
}
```

## Related types

- [LockActionException](doc:android-ref-lockactionexception)

Package: `com.door.opendoor.android.core.api.exceptions`.

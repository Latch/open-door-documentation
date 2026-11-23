---
title: GuestInvitesException
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Partial or complete guest-invitation failure.

- **`failedLockErrors`** — One error for each lock that failed.
- **`successfulLockIds`** — Identifiers of the locks where the guest invite succeeded.
- **`failedLockIds`** — Identifiers of the locks that failed, taken from failedLockErrors.

## Declaration

```kotlin
class GuestInvitesException(
    val failedLockErrors: List<LockActionException>,
    val successfulLockIds: List<UUID>,
    message: String = buildMessage(failedLockErrors, successfulLockIds),
) : Exception
```

## Related types

- [LockActionException](doc:android-ref-lockactionexception)

Package: `com.door.opendoor.android.core.api.exceptions`.

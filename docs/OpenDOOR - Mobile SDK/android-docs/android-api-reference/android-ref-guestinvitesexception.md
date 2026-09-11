---
title: GuestInvitesException
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Exception thrown when a guest invitation operation partially or fully fails. Carries
the list of per-lock failures and the list of locks that succeeded. The default message
embeds both counts for easier diagnostics; callers can override with richer context.

## Declaration

```kotlin
class GuestInvitesException(
    val failedLocks: List<LockActionException>,
    val successfulLocks: List<UUID>,
    message: String = "Guest invite failed for ${failedLocks.size} lock(s); ${successfulLocks.size} succeeded",
) : Exception(message) {
    val failedLockIds: List<UUID>
}
```

## Related types

- [Guest](doc:android-ref-guest)
- [LockActionException](doc:android-ref-lockactionexception)

Package: `com.door.opendoor.android.core.api.exceptions`.

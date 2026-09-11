---
title: GuestInvitesException
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Exception thrown when inviting a guest fails due to a known business rule.

## Declaration

```kotlin
class GuestInvitesException(
    val failedLocks: List<LockActionException>,
    val successfulLocks: List<UUID>,
) : Exception() {
    val failedLockIds: List<UUID>
}
```

## Related types

- [LockActionException](doc:android-ref-lockactionexception)

Package: `com.door.opendoor.android.core.api.exceptions`.

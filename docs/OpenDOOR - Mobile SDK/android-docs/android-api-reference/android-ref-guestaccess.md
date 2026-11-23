---
title: GuestAccess
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Access granted to a guest on a specific lock.

- **`lockId`** — Target lock ID.
- **`lockName`** — Target lock name.
- **`inviteType`** — Invite type for this access.
- **`passcodeType`** — Credential type granted.
- **`startTime`** — Start of the allowed window.
- **`endTime`** — End of the allowed window.

## Declaration

```kotlin
data class GuestAccess(
    val lockId: UUID,
    val lockName: String,
    val inviteType: InviteType,
    val passcodeType: PasscodeType,
    val startTime: Instant,
    val endTime: Instant?,
)
```

## Related types

- [InviteType](doc:android-ref-invitetype)
- [PasscodeType](doc:android-ref-passcodetype)

Package: `com.door.opendoor.android.core.api.model`.

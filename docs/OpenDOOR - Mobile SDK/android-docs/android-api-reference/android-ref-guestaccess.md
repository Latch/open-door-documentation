---
title: GuestAccess
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Access granted to a guest on a specific lock

- **`invitationId`** — Invitation ID (non-null only for BP buildings - roleAssignmentId)
- **`lockId`** — Target lock ID
- **`lockName`** — Lock name resolved from locks list
- **`inviteType`** — Invite type for this access
- **`passcodeType`** — Credential type granted
- **`startTime`** — Start of the allowed window
- **`endTime`** — End of the allowed window (nullable)

## Declaration

```kotlin
data class GuestAccess(
    val invitationId: UUID?,
    val lockId: UUID,
    val lockName: String,
    val inviteType: InviteType?,
    val passcodeType: PasscodeType,
    val startTime: Instant,
    val endTime: Instant?
)
```

## Related types

- [InviteType](doc:android-ref-invitetype)
- [Lock](doc:android-ref-lock)
- [PasscodeType](doc:android-ref-passcodetype)

Package: `com.door.opendoor.android.core.api.model`.

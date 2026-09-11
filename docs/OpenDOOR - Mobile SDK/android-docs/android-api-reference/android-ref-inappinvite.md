---
title: InAppInvite
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Invite type for in-app access with time-based restrictions.

- **`accessType`** — The type of access granted (Enter or Reach). Only used for Blueprint invites, null for Legacy invites.
- **`startTime`** — Start time of the requested access.
- **`endTime`** — End time of the requested access (nullable). If not set, access will be permanent until revoked.
- **`showDoorcodes`** — Whether to show doorcodes to the guest.

## Declaration

```kotlin
data class InAppInvite(
    override val accessType: AccessType?,
    val startTime: Instant,
    val endTime: Instant?,
    val showDoorcodes: Boolean,
) : InviteType
```

## Related types

- [AccessType](doc:android-ref-accesstype)
- [InviteType](doc:android-ref-invitetype)

Package: `com.door.opendoor.android.core.api.model`.

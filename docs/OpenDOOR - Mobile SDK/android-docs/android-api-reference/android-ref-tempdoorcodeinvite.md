---
title: TempDoorcodeInvite
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Invite type for temporary doorcode access.

- **`accessType`** — The type of access granted (Enter or Reach). Only used for Blueprint invites, null for Legacy invites.
- **`duration`** — Duration of the temporary access (Limit15Minutes or FullDay).
- **`period`** — Period when the access is valid (Today or Tomorrow).

## Declaration

```kotlin
data class TempDoorcodeInvite(
    override val accessType: AccessType?,
    val duration: Duration,
    val period: Period,
) : InviteType
```

## Related types

- [AccessType](doc:android-ref-accesstype)
- [Duration](doc:android-ref-duration)
- [InviteType](doc:android-ref-invitetype)
- [Period](doc:android-ref-period)

Package: `com.door.opendoor.android.core.api.model`.

---
title: InAppInvite
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

In-app access with time-based restrictions.

- **`startTime`** — Start time of the requested access.
- **`endTime`** — End time of the requested access. If not set, access is permanent until revoked.

## Declaration

```kotlin
data class InAppInvite(val startTime: Instant, val endTime: Instant?) : InviteType
```

## Related types

- [InviteType](doc:android-ref-invitetype)

Package: `com.door.opendoor.android.core.api.model`.

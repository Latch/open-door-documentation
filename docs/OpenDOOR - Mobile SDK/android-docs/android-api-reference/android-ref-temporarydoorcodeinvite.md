---
title: TemporaryDoorcodeInvite
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Temporary doorcode access.

- **`duration`** — Duration of the temporary access (Limit15Minutes or FullDay).
- **`period`** — Period when the access is valid (Today or Tomorrow).

## Declaration

```kotlin
data class TemporaryDoorcodeInvite(
    val duration: Duration,
    val period: Period,
) : InviteType
```

## Related types

- [Duration](doc:android-ref-duration)
- [InviteType](doc:android-ref-invitetype)
- [Period](doc:android-ref-period)

Package: `com.door.opendoor.android.core.api.model`.

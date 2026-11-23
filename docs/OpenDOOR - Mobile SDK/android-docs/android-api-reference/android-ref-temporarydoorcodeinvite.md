---
title: TemporaryDoorcodeInvite
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Temporary doorcode access.

- **`duration`** — How long the doorcode works on the chosen day: all day, or until 15 minutes after its first use.
- **`period`** — Period when the access is valid: today or tomorrow.

## Declaration

```kotlin
data class TemporaryDoorcodeInvite(val duration: Duration, val period: Period) : InviteType
```

## Related types

- [Duration](doc:android-ref-duration)
- [InviteType](doc:android-ref-invitetype)
- [Period](doc:android-ref-period)

Package: `com.door.opendoor.android.core.api.model`.

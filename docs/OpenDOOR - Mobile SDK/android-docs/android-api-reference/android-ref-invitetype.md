---
title: InviteType
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Sealed interface for invite types that define how a guest will receive access.

- **`accessType`** — The type of access granted (Enter or Reach). Only used for Blueprint invites, null for Legacy invites.

## Declaration

```kotlin
sealed interface InviteType {
    val accessType: AccessType?
}
```

## Related types

- [AccessType](doc:android-ref-accesstype)

Package: `com.door.opendoor.android.core.api.model`.

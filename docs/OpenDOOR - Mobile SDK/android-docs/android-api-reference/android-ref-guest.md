---
title: Guest
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Person with shared access to one or more locks

- **`id`** — Unique guest identifier
- **`firstName`** — Guest's first name
- **`lastName`** — Guest's last name
- **`email`** — Guest's email address
- **`phone`** — Guest's phone number
- **`guestAccesses`** — Lock-specific access entries

## Declaration

```kotlin
data class Guest(
    val id: UUID,
    val firstName: String,
    val lastName: String?,
    val email: String?,
    val phone: String?,
    val guestAccesses: List<GuestAccess>
)
```

## Related types

- [GuestAccess](doc:android-ref-guestaccess)
- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.model`.

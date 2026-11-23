---
title: Lock
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

User-visible lock information.

- **`id`** — Unique lock identifier.
- **`name`** — Human-readable lock name.
- **`buildingId`** — Building identifier.
- **`startTime`** — Start of access window.
- **`endTime`** — End of access window.
- **`doorCode`** — Door access code, if available.
- **`isShareable`** — Indicates whether this lock can be shared with guests.
- **`timeZone`** — IANA timezone of the lock, such as Europe/Rome. The phone's timezone when the lock has none.
- **`remoteUnlockMethods`** — Remote unlock methods the lock supports. Empty when it supports none.

## Declaration

```kotlin
data class Lock(
    val id: UUID,
    val name: String,
    val buildingId: UUID,
    val startTime: Instant,
    val endTime: Instant?,
    val doorCode: String?,
    val isShareable: Boolean,
    val timeZone: String,
    val remoteUnlockMethods: List<RemoteUnlockMethod>,
)
```

## Related types

- [RemoteUnlockMethod](doc:android-ref-remoteunlockmethod)

Package: `com.door.opendoor.android.core.api.model`.

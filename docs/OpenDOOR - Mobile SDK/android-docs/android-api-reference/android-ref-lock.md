---
title: Lock
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

User-visible lock information

- **`id`** — Unique lock identifier
- **`name`** — Human-readable lock name
- **`buildingId`** — Building identifier
- **`startTime`** — Start of access window
- **`endTime`** — End of access window (nullable)
- **`doorCode`** — Door access code if available
- **`propertyName`** — Property name. For Blueprint locks, this is the space name. For legacy locks, this is the lock name (same as `name`).
- **`isShareable`** — Indicates if this lock can be shared with guests.

## Declaration

```kotlin
data class Lock(
    val id: UUID,
    val name: String,
    val buildingId: UUID,
    val startTime: Instant,
    val endTime: Instant?,
    val doorCode: String?,
    val propertyName: String,
    val isShareable: Boolean,
)
```

Package: `com.door.opendoor.android.core.api.model`.

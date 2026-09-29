---
title: Lock
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

User-visible lock information.

- **`id`** — Unique lock identifier
- **`name`** — Human-readable lock name
- **`buildingId`** — Building identifier
- **`startTime`** — Start of access window
- **`endTime`** — End of access window (nullable)
- **`doorCode`** — Door access code if available
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
    val isShareable: Boolean,
)
```

Package: `com.door.opendoor.android.core.api.model`.
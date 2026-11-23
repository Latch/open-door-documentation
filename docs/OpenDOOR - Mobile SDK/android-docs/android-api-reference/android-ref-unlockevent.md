---
title: UnlockEvent
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Event emitted during explicit, proximity and remote unlock operations.

- **`lock`** — Lock the event relates to, if known. The SDK resolves the full lock from its own lock data, so consumers never have to supply or trust a caller-provided identifier.
- **`method`** — Method used for this unlock attempt.
- **`status`** — Current lifecycle status of the unlock operation.

## Declaration

```kotlin
data class UnlockEvent(
    val lock: Lock?,
    val method: UnlockEventMethod,
    val status: UnlockEventStatus,
)
```

## Related types

- [Lock](doc:android-ref-lock)
- [UnlockEventMethod](doc:android-ref-unlockeventmethod)
- [UnlockEventStatus](doc:android-ref-unlockeventstatus)

Package: `com.door.opendoor.android.core.api.model`.

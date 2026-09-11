---
title: UnlockEvent
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Event emitted during explicit and proximity unlock operations.

Conforms to the OpenDOOR SDK spec: a single event type carrying the `lock`, the
unlock `method`, and a lifecycle `status`. SDK v2 emits a stream of these as
the SDK progresses through the unlock pipeline (started → setup-sync →
connect → unlock → terminal).

- **`lock`** — Lock the event relates to (null if not yet bound to a specific lock). The SDK resolves the full lock from its cache, so consumers never have to supply or trust a caller-provided identifier.
- **`method`** — Method used for this unlock attempt
- **`status`** — Current lifecycle status of the unlock operation

## Declaration

```kotlin
data class UnlockEvent(
    val lock: Lock?,
    val method: UnlockEventMethod,
    val status: UnlockStatus,
)
```

## Related types

- [Lock](doc:android-ref-lock)
- [OpenDOOR](doc:android-ref-opendoor)
- [UnlockEventMethod](doc:android-ref-unlockeventmethod)
- [UnlockStatus](doc:android-ref-unlockstatus)

Package: `com.door.opendoor.android.core.api.model`.

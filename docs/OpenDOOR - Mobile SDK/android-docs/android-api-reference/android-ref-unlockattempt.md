---
title: UnlockAttempt
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Which pass through the unlock flow produced an event.

- `First` = initial pass (optional cached setup-sync + first unlock attempt).
- `Second` = recovery pass (post-failure setup + second unlock attempt).

## Declaration

```kotlin
enum class UnlockAttempt {
    First,
    Second,
}
```

## Related types

- [UnlockEventStatus](doc:android-ref-unlockeventstatus)

Package: `com.door.opendoor.android.core.api.model`.

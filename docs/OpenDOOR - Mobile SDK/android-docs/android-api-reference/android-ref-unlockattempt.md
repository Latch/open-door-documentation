---
title: UnlockAttempt
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Which pass through the unlock flow produced an event.

- `First` = initial pass (optional cached setup-sync + first unlock attempt).
- `Second` = recovery pass (post-failure setup + second unlock attempt).

Modeled as an enum (not a raw `phase: Int`) per the OpenDOOR SDK spec. Carried by the
phased [UnlockStatus](doc:android-ref-unlockstatus) variants — [UnlockStatus.SetupSync](doc:android-ref-unlockstatus), [UnlockStatus.ConnectForSetupSync](doc:android-ref-unlockstatus),
[UnlockStatus.ConnectForUnlock](doc:android-ref-unlockstatus), and [UnlockStatus.Unlock](doc:android-ref-unlockstatus) — so consumers can distinguish
first-pass from recovery-pass events.

## Declaration

```kotlin
enum class UnlockAttempt {
    First,
    Second,
}
```

## Related types

- [OpenDOOR](doc:android-ref-opendoor)
- [UnlockStatus](doc:android-ref-unlockstatus)

Package: `com.door.opendoor.android.core.api.model`.

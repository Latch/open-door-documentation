---
title: UnlockEvent
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Events emitted during explicit and proximity unlock operations.

SDK 2.1 adds [SetupSync](doc:android-ref-unlockevent) so apps can show setup/sync progress when the SDK
needs to provision lock access data before an unlock can finish. This commonly
appears the first time a user opens a door and setup sync is required.

## Declaration

```kotlin
sealed class UnlockEvent {

    data class UnlockStarted(
        val lockId: UUID?,
        val method: UnlockEventMethod,
    ) : UnlockEvent()

    data class SetupSync(
        val lockId: UUID?,
        val method: UnlockEventMethod,
    ) : UnlockEvent()

    data class UnlockFailed(
        val lockId: UUID?,
        val failReason: UnlockFailureReason,
        val method: UnlockEventMethod,
    ) : UnlockEvent()

    data class UnlockCanceled(
        val lockId: UUID?,
        val method: UnlockEventMethod,
    ) : UnlockEvent()

    data class UnlockSuccess(
        val lockId: UUID?,
        val method: UnlockEventMethod,
    ) : UnlockEvent()
}
```

## UnlockStarted

Unlock process has started

- **`lockId`** — Lock being unlocked
- **`method`** — Method used for this unlock attempt

## SetupSync

Setup sync process has started before unlock.

Use this event to show progress while the SDK writes required access data
to the lock. It can be emitted during explicit unlock or proximity unlock.

- **`lockId`** — Lock being set up before unlock
- **`method`** — Method used for this unlock attempt

## UnlockFailed

Unlock failed

- **`lockId`** — Lock that failed to unlock (null if not associated with a specific lock)
- **`failReason`** — Reason for failure
- **`method`** — Method used for this unlock attempt

## UnlockCanceled

Unlock was canceled.

This is emitted when an active explicit unlock or current proximity unlock
attempt is canceled through `cancelUnlock()` or superseded by another
unlock attempt.

- **`lockId`** — Lock that was canceled (null if not associated with a specific lock)
- **`method`** — Method used for this unlock attempt

## UnlockSuccess

Lock was successfully unlocked

- **`lockId`** — Lock that was unlocked (null if not associated with a specific lock)
- **`method`** — Method used for this unlock attempt

## Related types

- [Lock](doc:android-ref-lock)
- [UnlockEventMethod](doc:android-ref-unlockeventmethod)
- [UnlockFailureReason](doc:android-ref-unlockfailurereason)

Package: `com.door.opendoor.android.core.api.model`.

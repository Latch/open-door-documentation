---
title: UnlockEventStatus
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Lifecycle status carried by an unlock event.

## Declaration

```kotlin
sealed class UnlockEventStatus {
    data object Canceled : UnlockEventStatus
    data class ConnectForSetupSync(val attempt: UnlockAttempt) : UnlockEventStatus
    data class ConnectForUnlock(val attempt: UnlockAttempt) : UnlockEventStatus
    data class Failed(val reason: UnlockFailureReason) : UnlockEventStatus
    data class SetupSync(val attempt: UnlockAttempt) : UnlockEventStatus
    data object Started : UnlockEventStatus
    data object Success : UnlockEventStatus
    data class Unlock(val attempt: UnlockAttempt) : UnlockEventStatus
    data object UpdateSyncPackage : UnlockEventStatus
}
```

## Canceled

Unlock was canceled, for example by cancelUnlock or by starting an unlock for another lock.

## ConnectForSetupSync

BLE connect phase before the setup sync.

Emitted when the SDK starts connecting to the lock to send it a setup sync.

## ConnectForUnlock

BLE connect phase before unlocking.

Follows ConnectForSetupSync and SetupSync when a setup sync runs first. Otherwise it's the first connection of the attempt.

## Failed

Unlock failed.

## SetupSync

Setup sync before unlock.

Emitted after the setup connection is established, before the sync package is sent. Explicit and proximity unlocks can both emit it.

## Started

Unlock process has started.

## Success

Lock was successfully unlocked.

## Unlock

Unlock phase after the BLE connection is established.

Emitted before the unlock is sent to the lock, so the final Success or Failed status isn't known yet.

## UpdateSyncPackage

Sync package download in progress (recovery path).

Emitted when the recovery attempt downloads a fresh sync package before retrying the setup sync and the unlock. It carries no attempt because it only occurs in the recovery attempt.

## Related types

- [UnlockAttempt](doc:android-ref-unlockattempt)
- [UnlockFailureReason](doc:android-ref-unlockfailurereason)

Package: `com.door.opendoor.android.core.api.model`.

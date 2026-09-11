---
title: UnlockStatus
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Lifecycle status carried by [UnlockEvent.status](doc:android-ref-unlockevent).

Conforms to the OpenDOOR SDK spec: the SDK emits a stream of statuses as it
progresses through the unlock pipeline (started → setup-sync → connect →
unlock → terminal). Phased statuses carry [UnlockAttempt](doc:android-ref-unlockattempt) to distinguish the
first pass from the second-attempt recovery pass.

## Declaration

```kotlin
sealed class UnlockStatus {

    data object Started : UnlockStatus()

    data class ConnectForSetupSync(val attempt: UnlockAttempt) : UnlockStatus()

    data class SetupSync(val attempt: UnlockAttempt) : UnlockStatus()

    data object UpdateSyncPackage : UnlockStatus()

    data class ConnectForUnlock(val attempt: UnlockAttempt) : UnlockStatus()

    data class Unlock(val attempt: UnlockAttempt) : UnlockStatus()

    data class Failed(val reason: UnlockFailureReason) : UnlockStatus()

    data object Canceled : UnlockStatus()

    data object Success : UnlockStatus()
}
```

## Started

Unlock process has started.

## ConnectForSetupSync

BLE connect phase before SETUP SYNC.

Emitted when the SDK enters the connection phase that precedes a
setup-sync push to the lock.

## SetupSync

Setup sync process before unlock.

Emitted after the BLE setup connection is established, before the sync
package is transmitted. It can be emitted during explicit or proximity unlock.

## UpdateSyncPackage

Sync package download in progress (recovery path).

Emitted when a recovery flow begins fetching a fresh sync package over
the network before retrying SETUP SYNC and UNLOCK. Carries no attempt — it
only ever occurs on the second-attempt recovery pass.

## ConnectForUnlock

Emitted when the SDK enters the BLE connection phase before unlocking.

May follow [ConnectForSetupSync](doc:android-ref-unlockstatus) + [SetupSync](doc:android-ref-unlockstatus), or be the first connect
when no setup sync is required.

## Unlock

Unlock phase after the BLE connection is established.

Emitted after the BLE connection is established, before the unlock
operation is transmitted and before the terminal [Success](doc:android-ref-unlockstatus) / [Failed](doc:android-ref-unlockstatus) is known.

## Failed

Unlock failed.

## Canceled

Unlock was canceled — e.g. through `cancelUnlock()` or because it was
superseded by an unlock for another lock.

## Success

Lock was successfully unlocked.

## Related types

- [Lock](doc:android-ref-lock)
- [OpenDOOR](doc:android-ref-opendoor)
- [UnlockAttempt](doc:android-ref-unlockattempt)
- [UnlockEvent](doc:android-ref-unlockevent)
- [UnlockFailureReason](doc:android-ref-unlockfailurereason)

Package: `com.door.opendoor.android.core.api.model`.

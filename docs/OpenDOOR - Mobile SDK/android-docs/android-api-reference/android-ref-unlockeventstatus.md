---
title: UnlockEventStatus
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Lifecycle status carried by an unlock event.

## Declaration

```kotlin
sealed class UnlockEventStatus {

    data object Started : UnlockEventStatus()

    data class ConnectForSetupSync(val attempt: UnlockAttempt) : UnlockEventStatus()

    data class SetupSync(val attempt: UnlockAttempt) : UnlockEventStatus()

    data object UpdateSyncPackage : UnlockEventStatus()

    data class ConnectForUnlock(val attempt: UnlockAttempt) : UnlockEventStatus()

    data class Unlock(val attempt: UnlockAttempt) : UnlockEventStatus()

    data class Failed(val reason: UnlockFailureReason) : UnlockEventStatus()

    data object Canceled : UnlockEventStatus()

    data object Success : UnlockEventStatus()
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

May follow [ConnectForSetupSync](doc:android-ref-unlockeventstatus) + [SetupSync](doc:android-ref-unlockeventstatus), or be the first connect
when no setup sync is required.

## Unlock

Unlock phase after the BLE connection is established.

Emitted after the BLE connection is established, before the unlock
operation is transmitted and before the terminal [Success](doc:android-ref-unlockeventstatus) / [Failed](doc:android-ref-unlockeventstatus) is known.

## Failed

Unlock failed.

## Canceled

Unlock was canceled — e.g. through `cancelUnlock()` or because it was
superseded by an unlock for another lock.

## Success

Lock was successfully unlocked.

## Related types

- [Lock](doc:android-ref-lock)
- [UnlockAttempt](doc:android-ref-unlockattempt)
- [UnlockEvent](doc:android-ref-unlockevent)
- [UnlockFailureReason](doc:android-ref-unlockfailurereason)

Package: `com.door.opendoor.android.core.api.model`.

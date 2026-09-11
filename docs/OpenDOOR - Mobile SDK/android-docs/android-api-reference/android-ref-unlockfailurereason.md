---
title: UnlockFailureReason
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Reason an unlock failed, carried by [UnlockStatus.Failed](doc:android-ref-unlockstatus).

Conforms to the OpenDOOR SDK spec's canonical failure set. Causes the internal
pipeline distinguishes more finely are folded into these; where a fold would
lose information, the specific underlying cause is preserved in [Internal.code](doc:android-ref-unlockfailurereason).

## Declaration

```kotlin
sealed class UnlockFailureReason {

    data object BluetoothDisabled : UnlockFailureReason()

    data object OutOfSchedule : UnlockFailureReason()

    data object LockNotFound : UnlockFailureReason()

    data object ConnectionFailed : UnlockFailureReason()

    data object AuthFailed : UnlockFailureReason()

    data class Internal(val code: String) : UnlockFailureReason()
}
```

## BluetoothDisabled

Bluetooth is disabled or BLE was turned off mid-unlock.

Note: when Bluetooth is already off *before* an unlock starts, the unlock
call throws `BluetoothException` instead — this reason covers the in-flight
guard when BLE is disabled during an unlock.

## OutOfSchedule

Access attempted outside of the device access schedule.

## LockNotFound

No lock matching the requested id could be found or discovered.

## ConnectionFailed

BLE link to the lock could not be established (connect failed, timed out, or BT error).

## AuthFailed

Authentication failed — the lock rejected the user's credentials, or the
second-attempt recovery sync/download could not authenticate the user.

## Internal

Any other failure not covered above.

- **`code`** — Stable identifier for the underlying cause (e.g. `"UNLOCK_REJECTED"`, `"LOCK_NOT_RECOGNIZED"`, `"BLUETOOTH_DISABLED"`).

## Related types

- [BluetoothException](doc:android-ref-bluetoothexception)
- [OpenDOOR](doc:android-ref-opendoor)
- [UnlockStatus](doc:android-ref-unlockstatus)

Package: `com.door.opendoor.android.core.api.model`.

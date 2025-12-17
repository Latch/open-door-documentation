---
title: UnlockEvent
---
---
title: UnlockEvent
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.model](../index.html)/[UnlockEvent](index.html)



# UnlockEvent

sealed class [UnlockEvent](index.html)

#### Inheritors


| |
|---|
| [BleDisabled](-ble-disabled/index.html) |
| [BleNotAvailable](-ble-not-available/index.html) |
| [ConcurrentUnlockInProgress](-concurrent-unlock-in-progress/index.html) |
| [InternalError](-internal-error/index.html) |
| [BluetoothError](-bluetooth-error/index.html) |
| [LockNotFound](-lock-not-found/index.html) |
| [NotInitialized](-not-initialized/index.html) |
| [OutOfSchedule](-out-of-schedule/index.html) |
| [Success](-success/index.html) |
| [Cancelled](-cancelled/index.html) |
| [Connecting](-connecting/index.html) |
| [SettingUp](-setting-up/index.html) |
| [Scanning](-scanning/index.html) |
| [Unlocking](-unlocking/index.html) |


## Types


| Name | Summary |
|---|---|
| [BleDisabled](-ble-disabled/index.html) | [androidJvm]<br>data class [BleDisabled](-ble-disabled/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html) |
| [BleNotAvailable](-ble-not-available/index.html) | [androidJvm]<br>data class [BleNotAvailable](-ble-not-available/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html) |
| [BluetoothError](-bluetooth-error/index.html) | [androidJvm]<br>data class [BluetoothError](-bluetooth-error/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html) |
| [Cancelled](-cancelled/index.html) | [androidJvm]<br>data class [Cancelled](-cancelled/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html) |
| [ConcurrentUnlockInProgress](-concurrent-unlock-in-progress/index.html) | [androidJvm]<br>data class [ConcurrentUnlockInProgress](-concurrent-unlock-in-progress/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html)<br>Only one unlock operation is allowed to execute at one time. |
| [Connecting](-connecting/index.html) | [androidJvm]<br>data class [Connecting](-connecting/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html) |
| [InternalError](-internal-error/index.html) | [androidJvm]<br>data class [InternalError](-internal-error/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html) |
| [LockNotFound](-lock-not-found/index.html) | [androidJvm]<br>data class [LockNotFound](-lock-not-found/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html) |
| [NotInitialized](-not-initialized/index.html) | [androidJvm]<br>data class [NotInitialized](-not-initialized/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html) |
| [OutOfSchedule](-out-of-schedule/index.html) | [androidJvm]<br>data class [OutOfSchedule](-out-of-schedule/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html) |
| [Scanning](-scanning/index.html) | [androidJvm]<br>data class [Scanning](-scanning/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html) |
| [SettingUp](-setting-up/index.html) | [androidJvm]<br>data class [SettingUp](-setting-up/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html) |
| [Success](-success/index.html) | [androidJvm]<br>data class [Success](-success/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)) : [UnlockEvent](index.html) |
| [Unlocking](-unlocking/index.html) | [androidJvm]<br>data class [Unlocking](-unlocking/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html) |

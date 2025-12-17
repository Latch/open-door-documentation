---
title: ProximityUnlockStatus
---
---
title: ProximityUnlockStatus
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.model](../index.html)/[ProximityUnlockStatus](index.html)



# ProximityUnlockStatus

sealed class [ProximityUnlockStatus](index.html)

#### Inheritors


| |
|---|
| [BleDisabled](-ble-disabled/index.html) |
| [BleNotAvailable](-ble-not-available/index.html) |
| [ConcurrentUnlockInProgress](-concurrent-unlock-in-progress/index.html) |
| [InternalError](-internal-error/index.html) |
| [NotInitialized](-not-initialized/index.html) |
| [OutOfSchedule](-out-of-schedule/index.html) |
| [Success](-success/index.html) |
| [Unlocking](-unlocking/index.html) |
| [Cancelled](-cancelled/index.html) |


## Types


| Name | Summary |
|---|---|
| [BleDisabled](-ble-disabled/index.html) | [androidJvm]<br>object [BleDisabled](-ble-disabled/index.html) : [ProximityUnlockStatus](index.html) |
| [BleNotAvailable](-ble-not-available/index.html) | [androidJvm]<br>object [BleNotAvailable](-ble-not-available/index.html) : [ProximityUnlockStatus](index.html) |
| [Cancelled](-cancelled/index.html) | [androidJvm]<br>object [Cancelled](-cancelled/index.html) : [ProximityUnlockStatus](index.html) |
| [ConcurrentUnlockInProgress](-concurrent-unlock-in-progress/index.html) | [androidJvm]<br>object [ConcurrentUnlockInProgress](-concurrent-unlock-in-progress/index.html) : [ProximityUnlockStatus](index.html)<br>Only one unlock operation is allowed to execute at one time. |
| [InternalError](-internal-error/index.html) | [androidJvm]<br>object [InternalError](-internal-error/index.html) : [ProximityUnlockStatus](index.html) |
| [NotInitialized](-not-initialized/index.html) | [androidJvm]<br>object [NotInitialized](-not-initialized/index.html) : [ProximityUnlockStatus](index.html) |
| [OutOfSchedule](-out-of-schedule/index.html) | [androidJvm]<br>object [OutOfSchedule](-out-of-schedule/index.html) : [ProximityUnlockStatus](index.html) |
| [Success](-success/index.html) | [androidJvm]<br>data class [Success](-success/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)) : [ProximityUnlockStatus](index.html) |
| [Unlocking](-unlocking/index.html) | [androidJvm]<br>data class [Unlocking](-unlocking/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)) : [ProximityUnlockStatus](index.html) |

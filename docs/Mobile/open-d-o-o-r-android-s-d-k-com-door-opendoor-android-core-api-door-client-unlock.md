---
title: unlock
---
---
title: unlock
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api](../index.html)/[DoorClient](index.html)/[unlock](unlock.html)



# unlock



[androidJvm]\
abstract suspend fun [unlock](unlock.html)(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html))



Starts an explicit unlock for a given lock.



Note: when running an explicit unlock, if proximity unlock is active, it will be paused and resumed after the explicit unlock completes.



#### Return



Completes when the unlock request is initiated.



#### Parameters


androidJvm

| | |
|---|---|
| lockId | the ID of the lock to unlock. |



#### Throws


| |
|---|
| [SDKException](../../com.door.opendoor.android.core.api.exceptions/-s-d-k-exception/index.html) |
| [BluetoothException](../../com.door.opendoor.android.core.api.exceptions/-bluetooth-exception/index.html) |



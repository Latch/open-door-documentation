---
title: sync
---
---
title: sync
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api](../index.html)/[DoorClient](index.html)/[sync](sync.html)



# sync



[androidJvm]\
abstract suspend fun [sync](sync.html)(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html))



Starts the active sync process for a lock.



Synchronizes lock data with the backend and returns when complete.



#### Return



Completes when synchronization finishes.



#### Parameters


androidJvm

| | |
|---|---|
| lockId | ID of the lock to sync. |



#### Throws


| |
|---|
| [SDKException](../../com.door.opendoor.android.core.api.exceptions/-s-d-k-exception/index.html) |
| [BluetoothException](../../com.door.opendoor.android.core.api.exceptions/-bluetooth-exception/index.html) |
| [NetworkException](../../com.door.opendoor.android.core.api.exceptions/-network-exception/index.html) |
| [SyncException](../../com.door.opendoor.android.core.api.exceptions/-sync-exception/index.html) |



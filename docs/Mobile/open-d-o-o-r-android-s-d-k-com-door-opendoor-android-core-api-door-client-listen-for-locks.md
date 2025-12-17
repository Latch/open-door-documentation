---
title: listenForLocks
---
---
title: listenForLocks
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api](../index.html)/[DoorClient](index.html)/[listenForLocks](listen-for-locks.html)



# listenForLocks



[androidJvm]\
abstract fun [listenForLocks](listen-for-locks.html)(): Flow&lt;[List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[Lock](../../com.door.opendoor.android.core.api.model/-lock/index.html)&gt;&gt;



Returns a stream of lock list updates.



Connects to the database and emits updates whenever locks change. Makes an initial API call to fetch locks and update the database. As long as the listener is connected, will receive all lock updates. The stream does not emit errors.



#### Return



a Flow/Combine/AsyncStream of lock list updates.



#### Throws


| |
|---|
| [SDKException](../../com.door.opendoor.android.core.api.exceptions/-s-d-k-exception/index.html) |




[androidJvm]\
abstract fun [listenForLocks](listen-for-locks.html)(listener: [LocksListener](../../com.door.opendoor.android.core.api.listeners/-locks-listener/index.html))



Callback-based variant of listenForLocks.



#### Return



Unit



#### Parameters


androidJvm

| | |
|---|---|
| listener | Callback to receive list<Lock> updates |



#### Throws


| |
|---|
| [SDKException](../../com.door.opendoor.android.core.api.exceptions/-s-d-k-exception/index.html) |



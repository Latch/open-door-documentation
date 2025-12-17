---
title: listenForUnlockEvents
---
---
title: listenForUnlockEvents
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api](../index.html)/[DoorClient](index.html)/[listenForUnlockEvents](listen-for-unlock-events.html)



# listenForUnlockEvents



[androidJvm]\
abstract fun [listenForUnlockEvents](listen-for-unlock-events.html)(): Flow&lt;[UnlockEvent](../../com.door.opendoor.android.core.api.model/-unlock-event/index.html)&gt;



Returns a stream of unlock events from both explicit and proximity unlocks.



The stream will contain progress and result events for all unlock operations.



#### Return



a Flow/Combine/AsyncStream of unlock events.



#### Throws


| |
|---|
| [SDKException](../../com.door.opendoor.android.core.api.exceptions/-s-d-k-exception/index.html) |




[androidJvm]\
abstract fun [listenForUnlockEvents](listen-for-unlock-events.html)(listener: [UnlockEventsListener](../../com.door.opendoor.android.core.api.listeners/-unlock-events-listener/index.html))



Callback-based variant of listenForUnlockEvents.



#### Return



Unit



#### Parameters


androidJvm

| | |
|---|---|
| listener | Callback to receive UnlockEvent updates |



#### Throws


| |
|---|
| [SDKException](../../com.door.opendoor.android.core.api.exceptions/-s-d-k-exception/index.html) |



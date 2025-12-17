---
title: UnlockCanceled
---
---
title: UnlockCanceled
---
//[OpenDOOR Android SDK](../../../../index.html)/[com.door.opendoor.android.core.api.model](../../index.html)/[UnlockEvent](../index.html)/[UnlockCanceled](index.html)



# UnlockCanceled



[androidJvm]\
data class [UnlockCanceled](index.html)(val lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](../index.html)

Unlock was canceled (e.g., when starting unlock for another lock)



## Constructors


| | |
|---|---|
| [UnlockCanceled](-unlock-canceled.html) | [androidJvm]<br>constructor(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) |


## Properties


| Name | Summary |
|---|---|
| [lockId](lock-id.html) | [androidJvm]<br>val [lockId](lock-id.html): [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?<br>Lock that was canceled (null if not associated with a specific lock) |

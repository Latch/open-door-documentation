---
title: UnlockSuccess
---
---
title: UnlockSuccess
---
//[OpenDOOR Android SDK](../../../../index.html)/[com.door.opendoor.android.core.api.model](../../index.html)/[UnlockEvent](../index.html)/[UnlockSuccess](index.html)



# UnlockSuccess



[androidJvm]\
data class [UnlockSuccess](index.html)(val lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](../index.html)

Lock was successfully unlocked



## Constructors


| | |
|---|---|
| [UnlockSuccess](-unlock-success.html) | [androidJvm]<br>constructor(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) |


## Properties


| Name | Summary |
|---|---|
| [lockId](lock-id.html) | [androidJvm]<br>val [lockId](lock-id.html): [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?<br>Lock that was unlocked (null if not associated with a specific lock) |

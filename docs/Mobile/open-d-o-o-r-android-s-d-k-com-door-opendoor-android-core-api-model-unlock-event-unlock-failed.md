---
title: UnlockFailed
---
---
title: UnlockFailed
---
//[OpenDOOR Android SDK](../../../../index.html)/[com.door.opendoor.android.core.api.model](../../index.html)/[UnlockEvent](../index.html)/[UnlockFailed](index.html)



# UnlockFailed



[androidJvm]\
data class [UnlockFailed](index.html)(val lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?, val failReason: [UnlockFailureReason](../../-unlock-failure-reason/index.html)) : [UnlockEvent](../index.html)

Unlock failed



## Constructors


| | |
|---|---|
| [UnlockFailed](-unlock-failed.html) | [androidJvm]<br>constructor(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?, failReason: [UnlockFailureReason](../../-unlock-failure-reason/index.html)) |


## Properties


| Name | Summary |
|---|---|
| [failReason](fail-reason.html) | [androidJvm]<br>val [failReason](fail-reason.html): [UnlockFailureReason](../../-unlock-failure-reason/index.html)<br>Reason for failure |
| [lockId](lock-id.html) | [androidJvm]<br>val [lockId](lock-id.html): [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?<br>Lock that failed to unlock (null if not associated with a specific lock) |

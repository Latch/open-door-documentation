---
title: UnlockEvent
---
---
title: UnlockEvent
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.model](../index.html)/[UnlockEvent](index.html)



# UnlockEvent

sealed class [UnlockEvent](index.html)

Events emitted during unlock operations



#### Inheritors


| |
|---|
| [UnlockStarted](-unlock-started/index.html) |
| [UnlockFailed](-unlock-failed/index.html) |
| [UnlockCanceled](-unlock-canceled/index.html) |
| [UnlockSuccess](-unlock-success/index.html) |


## Types


| Name | Summary |
|---|---|
| [UnlockCanceled](-unlock-canceled/index.html) | [androidJvm]<br>data class [UnlockCanceled](-unlock-canceled/index.html)(val lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html)<br>Unlock was canceled (e.g., when starting unlock for another lock) |
| [UnlockFailed](-unlock-failed/index.html) | [androidJvm]<br>data class [UnlockFailed](-unlock-failed/index.html)(val lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?, val failReason: [UnlockFailureReason](../-unlock-failure-reason/index.html)) : [UnlockEvent](index.html)<br>Unlock failed |
| [UnlockStarted](-unlock-started/index.html) | [androidJvm]<br>data class [UnlockStarted](-unlock-started/index.html)(val lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html)<br>Unlock process has started |
| [UnlockSuccess](-unlock-success/index.html) | [androidJvm]<br>data class [UnlockSuccess](-unlock-success/index.html)(val lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?) : [UnlockEvent](index.html)<br>Lock was successfully unlocked |

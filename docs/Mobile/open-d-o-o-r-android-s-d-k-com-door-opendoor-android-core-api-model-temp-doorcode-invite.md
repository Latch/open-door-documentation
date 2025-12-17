---
title: TempDoorcodeInvite
---
---
title: TempDoorcodeInvite
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.model](../index.html)/[TempDoorcodeInvite](index.html)



# TempDoorcodeInvite



[androidJvm]\
sealed interface [TempDoorcodeInvite](index.html) : [InviteType](../-invite-type/index.html)

Sealed interface for temporary doorcode invite types.



## Properties


| Name | Summary |
|---|---|
| [accessType](../-invite-type/access-type.html) | [androidJvm]<br>abstract val [accessType](../-invite-type/access-type.html): [AccessType](../-access-type/index.html)<br>The type of access granted (Enter or Reach). |
| [duration](duration.html) | [androidJvm]<br>abstract val [duration](duration.html): [Duration](../-duration/index.html)<br>Duration of the temporary access (Limit15Minutes or FullDay). |
| [period](period.html) | [androidJvm]<br>abstract val [period](period.html): [Period](../-period/index.html)<br>Period when the access is valid (Today or Tomorrow). |

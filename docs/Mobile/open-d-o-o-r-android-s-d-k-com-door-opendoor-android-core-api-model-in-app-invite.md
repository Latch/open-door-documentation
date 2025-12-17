---
title: InAppInvite
---
---
title: InAppInvite
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.model](../index.html)/[InAppInvite](index.html)



# InAppInvite



[androidJvm]\
data class [InAppInvite](index.html)(val accessType: [AccessType](../-access-type/index.html), val startTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html), val endTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)?, val showDoorcodes: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)) : [InviteType](../-invite-type/index.html)

Invite type for in-app access with time-based restrictions.



## Constructors


| | |
|---|---|
| [InAppInvite](-in-app-invite.html) | [androidJvm]<br>constructor(accessType: [AccessType](../-access-type/index.html), startTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html), endTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)?, showDoorcodes: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)) |


## Properties


| Name | Summary |
|---|---|
| [accessType](access-type.html) | [androidJvm]<br>open override val [accessType](access-type.html): [AccessType](../-access-type/index.html)<br>The type of access granted (Enter or Reach). |
| [endTime](end-time.html) | [androidJvm]<br>val [endTime](end-time.html): [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)?<br>End time of the requested access (nullable). If not set, access will be permanent until revoked. |
| [showDoorcodes](show-doorcodes.html) | [androidJvm]<br>val [showDoorcodes](show-doorcodes.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)<br>Whether to show doorcodes to the guest. |
| [startTime](start-time.html) | [androidJvm]<br>val [startTime](start-time.html): [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)<br>Start time of the requested access. |

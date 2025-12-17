---
title: GuestAccess
---
---
title: GuestAccess
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.model](../index.html)/[GuestAccess](index.html)



# GuestAccess



[androidJvm]\
data class [GuestAccess](index.html)(val lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), val passcodeType: [PasscodeType](../-passcode-type/index.html), val startTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html), val endTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)?)

Access granted to a guest on a specific lock



## Constructors


| | |
|---|---|
| [GuestAccess](-guest-access.html) | [androidJvm]<br>constructor(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), passcodeType: [PasscodeType](../-passcode-type/index.html), startTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html), endTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)?) |


## Properties


| Name | Summary |
|---|---|
| [endTime](end-time.html) | [androidJvm]<br>val [endTime](end-time.html): [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)?<br>End of the allowed window (nullable) |
| [lockId](lock-id.html) | [androidJvm]<br>val [lockId](lock-id.html): [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)<br>Target lock ID |
| [passcodeType](passcode-type.html) | [androidJvm]<br>val [passcodeType](passcode-type.html): [PasscodeType](../-passcode-type/index.html)<br>Credential type granted |
| [startTime](start-time.html) | [androidJvm]<br>val [startTime](start-time.html): [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)<br>Start of the allowed window |

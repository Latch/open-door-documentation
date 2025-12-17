---
title: Lock
---
---
title: Lock
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.model](../index.html)/[Lock](index.html)



# Lock



[androidJvm]\
data class [Lock](index.html)(val id: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val buildingId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), val startTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html), val endTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)?, val doorCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?)

User-visible lock information



## Constructors


| | |
|---|---|
| [Lock](-lock.html) | [androidJvm]<br>constructor(id: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), buildingId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), startTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html), endTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)?, doorCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?) |


## Properties


| Name | Summary |
|---|---|
| [buildingId](building-id.html) | [androidJvm]<br>val [buildingId](building-id.html): [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)<br>Building identifier |
| [doorCode](door-code.html) | [androidJvm]<br>val [doorCode](door-code.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?<br>Door access code if available |
| [endTime](end-time.html) | [androidJvm]<br>val [endTime](end-time.html): [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)?<br>End of access window (nullable) |
| [id](id.html) | [androidJvm]<br>val [id](id.html): [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)<br>Unique lock identifier |
| [name](name.html) | [androidJvm]<br>val [name](name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)<br>Human-readable lock name |
| [startTime](start-time.html) | [androidJvm]<br>val [startTime](start-time.html): [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)<br>Start of access window |

---
title: AccessLogsResult
---
---
title: AccessLogsResult
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.model](../index.html)/[AccessLogsResult](index.html)



# AccessLogsResult

sealed class [AccessLogsResult](index.html)

#### Inheritors


| |
|---|
| [Success](-success/index.html) |
| [NetworkError](-network-error/index.html) |
| [NotInitialized](-not-initialized/index.html) |
| [InternalError](-internal-error/index.html) |


## Types


| Name | Summary |
|---|---|
| [InternalError](-internal-error/index.html) | [androidJvm]<br>object [InternalError](-internal-error/index.html) : [AccessLogsResult](index.html) |
| [NetworkError](-network-error/index.html) | [androidJvm]<br>data class [NetworkError](-network-error/index.html)(val reason: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) : [AccessLogsResult](index.html) |
| [NotInitialized](-not-initialized/index.html) | [androidJvm]<br>object [NotInitialized](-not-initialized/index.html) : [AccessLogsResult](index.html) |
| [Success](-success/index.html) | [androidJvm]<br>data class [Success](-success/index.html)(val accessLogs: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[AccessLog](../-access-log/index.html)&gt;) : [AccessLogsResult](index.html) |

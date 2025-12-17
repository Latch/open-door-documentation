---
title: LocksResult
---
---
title: LocksResult
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.model](../index.html)/[LocksResult](index.html)



# LocksResult

sealed class [LocksResult](index.html)

#### Inheritors


| |
|---|
| [Success](-success/index.html) |
| [NotInitialized](-not-initialized/index.html) |
| [Error](-error/index.html) |


## Types


| Name | Summary |
|---|---|
| [Error](-error/index.html) | [androidJvm]<br>data class [Error](-error/index.html)(val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) : [LocksResult](index.html) |
| [NotInitialized](-not-initialized/index.html) | [androidJvm]<br>object [NotInitialized](-not-initialized/index.html) : [LocksResult](index.html) |
| [Success](-success/index.html) | [androidJvm]<br>data class [Success](-success/index.html)(val locks: [Collection](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html)&lt;[Lock](../-lock/index.html)&gt;) : [LocksResult](index.html) |

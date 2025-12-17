---
title: GuestsResult
---
---
title: GuestsResult
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.model](../index.html)/[GuestsResult](index.html)



# GuestsResult

sealed interface [GuestsResult](index.html)

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
| [InternalError](-internal-error/index.html) | [androidJvm]<br>object [InternalError](-internal-error/index.html) : [GuestsResult](index.html) |
| [NetworkError](-network-error/index.html) | [androidJvm]<br>object [NetworkError](-network-error/index.html) : [GuestsResult](index.html) |
| [NotInitialized](-not-initialized/index.html) | [androidJvm]<br>object [NotInitialized](-not-initialized/index.html) : [GuestsResult](index.html) |
| [Success](-success/index.html) | [androidJvm]<br>data class [Success](-success/index.html)(val guests: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[Guest](../-guest/index.html)&gt;) : [GuestsResult](index.html) |

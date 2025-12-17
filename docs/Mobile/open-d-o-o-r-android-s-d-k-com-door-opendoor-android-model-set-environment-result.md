---
title: SetEnvironmentResult
---
---
title: SetEnvironmentResult
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.model](../index.html)/[SetEnvironmentResult](index.html)



# SetEnvironmentResult

sealed interface [SetEnvironmentResult](index.html)

Represents the result of setting the environment in which the SDK will work.



#### Inheritors


| |
|---|
| [Completed](-completed/index.html) |
| [EnvironmentAlreadySet](-environment-already-set/index.html) |
| [Failed](-failed/index.html) |
| [ClientNotInitialized](-client-not-initialized/index.html) |


## Types


| Name | Summary |
|---|---|
| [ClientNotInitialized](-client-not-initialized/index.html) | [androidJvm]<br>object [ClientNotInitialized](-client-not-initialized/index.html) : [SetEnvironmentResult](index.html) |
| [Completed](-completed/index.html) | [androidJvm]<br>object [Completed](-completed/index.html) : [SetEnvironmentResult](index.html) |
| [EnvironmentAlreadySet](-environment-already-set/index.html) | [androidJvm]<br>object [EnvironmentAlreadySet](-environment-already-set/index.html) : [SetEnvironmentResult](index.html) |
| [Failed](-failed/index.html) | [androidJvm]<br>data class [Failed](-failed/index.html)(val ex: [Exception](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-exception/index.html)) : [SetEnvironmentResult](index.html) |

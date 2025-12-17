---
title: SDKException
---
---
title: SDKException
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.exceptions](../index.html)/[SDKException](index.html)



# SDKException

sealed class [SDKException](index.html) : [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)

Base exception for SDK failures



#### Inheritors


| |
|---|
| [SDKNotInitializedException](-s-d-k-not-initialized-exception/index.html) |
| [InternalException](-internal-exception/index.html) |


## Types


| Name | Summary |
|---|---|
| [InternalException](-internal-exception/index.html) | [androidJvm]<br>class [InternalException](-internal-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [SDKException](index.html)<br>An internal error occurred |
| [SDKNotInitializedException](-s-d-k-not-initialized-exception/index.html) | [androidJvm]<br>class [SDKNotInitializedException](-s-d-k-not-initialized-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [SDKException](index.html)<br>The SDK has not been initialized with setupWithToken |


## Properties


| Name | Summary |
|---|---|
| [cause](../-sync-exception/-sync-internal-exception/index.html#-654012527%2FProperties%2F-1404661416) | [androidJvm]<br>open val [cause](../-sync-exception/-sync-internal-exception/index.html#-654012527%2FProperties%2F-1404661416): [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| [message](../-sync-exception/-sync-internal-exception/index.html#1824300659%2FProperties%2F-1404661416) | [androidJvm]<br>open val [message](../-sync-exception/-sync-internal-exception/index.html#1824300659%2FProperties%2F-1404661416): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

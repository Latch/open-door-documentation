---
title: NetworkException
---
---
title: NetworkException
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.exceptions](../index.html)/[NetworkException](index.html)



# NetworkException

sealed class [NetworkException](index.html) : [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)

Base exception for network failures



#### Inheritors


| |
|---|
| [PayloadError](-payload-error/index.html) |
| [InternalNetworkException](-internal-network-exception/index.html) |
| [InvalidTokenException](-invalid-token-exception/index.html) |


## Types


| Name | Summary |
|---|---|
| [InternalNetworkException](-internal-network-exception/index.html) | [androidJvm]<br>class [InternalNetworkException](-internal-network-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [NetworkException](index.html)<br>Internal network error (404, parsing errors, etc) |
| [InvalidTokenException](-invalid-token-exception/index.html) | [androidJvm]<br>class [InvalidTokenException](-invalid-token-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [NetworkException](index.html)<br>The supplied authorization token is invalid and should be refreshed. |
| [PayloadError](-payload-error/index.html) | [androidJvm]<br>class [PayloadError](-payload-error/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [NetworkException](index.html)<br>Network error with message from backend |


## Properties


| Name | Summary |
|---|---|
| [cause](../-sync-exception/-sync-internal-exception/index.html#-654012527%2FProperties%2F-1404661416) | [androidJvm]<br>open val [cause](../-sync-exception/-sync-internal-exception/index.html#-654012527%2FProperties%2F-1404661416): [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| [message](../-sync-exception/-sync-internal-exception/index.html#1824300659%2FProperties%2F-1404661416) | [androidJvm]<br>open val [message](../-sync-exception/-sync-internal-exception/index.html#1824300659%2FProperties%2F-1404661416): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

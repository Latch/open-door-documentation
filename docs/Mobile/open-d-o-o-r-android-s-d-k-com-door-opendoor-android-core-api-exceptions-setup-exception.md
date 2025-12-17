---
title: SetupException
---
---
title: SetupException
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.exceptions](../index.html)/[SetupException](index.html)



# SetupException

sealed class [SetupException](index.html) : [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)

Base exception for setup failures



#### Inheritors


| |
|---|
| [InvalidTokenException](-invalid-token-exception/index.html) |
| [ConsentNotGrantedException](-consent-not-granted-exception/index.html) |
| [SetupInternalException](-setup-internal-exception/index.html) |


## Types


| Name | Summary |
|---|---|
| [ConsentNotGrantedException](-consent-not-granted-exception/index.html) | [androidJvm]<br>class [ConsentNotGrantedException](-consent-not-granted-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [SetupException](index.html)<br>User consent not granted |
| [InvalidTokenException](-invalid-token-exception/index.html) | [androidJvm]<br>class [InvalidTokenException](-invalid-token-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [SetupException](index.html)<br>The supplied authorization token is invalid and should be refreshed. |
| [SetupInternalException](-setup-internal-exception/index.html) | [androidJvm]<br>class [SetupInternalException](-setup-internal-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [SetupException](index.html)<br>An internal error occurred |


## Properties


| Name | Summary |
|---|---|
| [cause](../-sync-exception/-sync-internal-exception/index.html#-654012527%2FProperties%2F-1404661416) | [androidJvm]<br>open val [cause](../-sync-exception/-sync-internal-exception/index.html#-654012527%2FProperties%2F-1404661416): [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| [message](../-sync-exception/-sync-internal-exception/index.html#1824300659%2FProperties%2F-1404661416) | [androidJvm]<br>open val [message](../-sync-exception/-sync-internal-exception/index.html#1824300659%2FProperties%2F-1404661416): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

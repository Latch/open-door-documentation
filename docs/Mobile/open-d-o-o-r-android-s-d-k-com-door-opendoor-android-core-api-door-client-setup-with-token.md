---
title: setupWithToken
---
---
title: setupWithToken
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api](../index.html)/[DoorClient](index.html)/[setupWithToken](setup-with-token.html)



# setupWithToken



[androidJvm]\
abstract suspend fun [setupWithToken](setup-with-token.html)(context: [Context](https://developer.android.com/reference/kotlin/android/content/Context.html), token: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), includeAllLocks: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false)



Authenticates the SDK with the provided token and initializes services.



First part initializes the SDK (database, https clients, etc). If the user from token is different from stored user, all cached data is deleted. The token is stored in memory only (never persisted). The includeAllLocks flag is stored and used when retrieving locks.



#### Return



Completes when authentication and setup finishes.



#### Parameters


androidJvm

| | |
|---|---|
| context | Android application context |
| token | the user authentication token. |
| includeAllLocks | if true, include all locks; otherwise only partner locks. |



#### Throws


| |
|---|
| [SetupException](../../com.door.opendoor.android.core.api.exceptions/-setup-exception/index.html) |
| [NetworkException](../../com.door.opendoor.android.core.api.exceptions/-network-exception/index.html) |



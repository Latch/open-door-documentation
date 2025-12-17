---
title: SyncException
---
---
title: SyncException
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.exceptions](../index.html)/[SyncException](index.html)



# SyncException

sealed class [SyncException](index.html) : [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)

Base exception for sync failures



#### Inheritors


| |
|---|
| [LockNotFoundException](-lock-not-found-exception/index.html) |
| [CanceledException](-canceled-exception/index.html) |
| [UnlockInProgressException](-unlock-in-progress-exception/index.html) |
| [SyncInternalException](-sync-internal-exception/index.html) |


## Types


| Name | Summary |
|---|---|
| [CanceledException](-canceled-exception/index.html) | [androidJvm]<br>class [CanceledException](-canceled-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [SyncException](index.html)<br>Sync operation was canceled |
| [LockNotFoundException](-lock-not-found-exception/index.html) | [androidJvm]<br>class [LockNotFoundException](-lock-not-found-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [SyncException](index.html)<br>Lock not found during sync |
| [SyncInternalException](-sync-internal-exception/index.html) | [androidJvm]<br>class [SyncInternalException](-sync-internal-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [SyncException](index.html)<br>An internal error occurred |
| [UnlockInProgressException](-unlock-in-progress-exception/index.html) | [androidJvm]<br>class [UnlockInProgressException](-unlock-in-progress-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [SyncException](index.html)<br>Unlock operation is in progress |


## Properties


| Name | Summary |
|---|---|
| [cause](-sync-internal-exception/index.html#-654012527%2FProperties%2F-1404661416) | [androidJvm]<br>open val [cause](-sync-internal-exception/index.html#-654012527%2FProperties%2F-1404661416): [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| [message](-sync-internal-exception/index.html#1824300659%2FProperties%2F-1404661416) | [androidJvm]<br>open val [message](-sync-internal-exception/index.html#1824300659%2FProperties%2F-1404661416): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

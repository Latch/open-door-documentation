---
title: fetchLocks
---
---
title: fetchLocks
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api](../index.html)/[DoorClient](index.html)/[fetchLocks](fetch-locks.html)



# fetchLocks



[androidJvm]\
abstract suspend fun [fetchLocks](fetch-locks.html)(): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[Lock](../../com.door.opendoor.android.core.api.model/-lock/index.html)&gt;



Retrieves the locks of the current user.



Makes an API call to fetch the latest locks and updates the database. Returns locks from the database (API results or cached values if API fails).



#### Return



List of locks available to the user.



#### Throws


| |
|---|
| [SDKException](../../com.door.opendoor.android.core.api.exceptions/-s-d-k-exception/index.html) |
| [NetworkException](../../com.door.opendoor.android.core.api.exceptions/-network-exception/index.html) |



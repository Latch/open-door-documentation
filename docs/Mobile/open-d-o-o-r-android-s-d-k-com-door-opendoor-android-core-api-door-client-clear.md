---
title: clear
---
---
title: clear
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api](../index.html)/[DoorClient](index.html)/[clear](clear.html)



# clear



[androidJvm]\
abstract suspend fun [clear](clear.html)()



Performs logout by clearing database and saved token.



This method clears all cached data and removes the authentication token. After calling clear(), the client must be set up again with setupWithToken().



#### Return



Completes when all data has been cleared.



#### Throws


| |
|---|
| [SDKException](../../com.door.opendoor.android.core.api.exceptions/-s-d-k-exception/index.html) |



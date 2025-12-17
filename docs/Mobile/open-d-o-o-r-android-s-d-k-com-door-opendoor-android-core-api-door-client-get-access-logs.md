---
title: getAccessLogs
---
---
title: getAccessLogs
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api](../index.html)/[DoorClient](index.html)/[getAccessLogs](get-access-logs.html)



# getAccessLogs



[androidJvm]\
abstract suspend fun [getAccessLogs](get-access-logs.html)(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[AccessLog](../../com.door.opendoor.android.core.api.model/-access-log/index.html)&gt;



Retrieves access logs for a specific lock.



Makes an API call to fetch the access logs for the given lock.



#### Return



List of access log entries for the lock.



#### Parameters


androidJvm

| | |
|---|---|
| lockId | ID of the lock. |



#### Throws


| |
|---|
| [SDKException](../../com.door.opendoor.android.core.api.exceptions/-s-d-k-exception/index.html) |
| [NetworkException](../../com.door.opendoor.android.core.api.exceptions/-network-exception/index.html) |



---
title: inviteGuests
---
---
title: inviteGuests
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api](../index.html)/[DoorClient](index.html)/[inviteGuests](invite-guests.html)



# inviteGuests



[androidJvm]\
abstract suspend fun [inviteGuests](invite-guests.html)(firstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), lastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), email: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, phone: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, startTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html), endTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)?, deviceUuids: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)&gt;, passcodeType: [PasscodeType](../../com.door.opendoor.android.core.api.model/-passcode-type/index.html)): [Guest](../../com.door.opendoor.android.core.api.model/-guest/index.html)



Shares access to selected locks with a guest through the selected passcode type.



Note: For email and phone parameters, at least one must be provided. If both are null, a network error will be returned. If no endTime is set, the guest access will be permanent until revoked.



#### Return



Guest object with created/updated access.



#### Parameters


androidJvm

| | |
|---|---|
| firstName | first name of the guest. |
| lastName | last name of the guest. |
| email | email of the guest (nullable). At least one of email or phone must be provided. |
| phone | phone number of the guest (nullable). At least one of email or phone must be provided. |
| startTime | start time of the requested access. |
| endTime | end time of the requested access (nullable). If not set, access will be permanent until revoked. |
| deviceUuids | UUIDs of the Door locks to add to the guest's access. |
| passcodeType | type of access to grant. |



#### Throws


| |
|---|
| [SDKException](../../com.door.opendoor.android.core.api.exceptions/-s-d-k-exception/index.html) |
| [NetworkException](../../com.door.opendoor.android.core.api.exceptions/-network-exception/index.html) |



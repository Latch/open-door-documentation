---
title: inviteGuestsV2
---
---
title: inviteGuestsV2
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api](../index.html)/[DoorClient](index.html)/[inviteGuestsV2](invite-guests-v2.html)



# inviteGuestsV2



[androidJvm]\
abstract suspend fun [inviteGuestsV2](invite-guests-v2.html)(firstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), lastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), email: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, phone: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), inviteType: [InviteType](../../com.door.opendoor.android.core.api.model/-invite-type/index.html)): [Guest](../../com.door.opendoor.android.core.api.model/-guest/index.html)



Shares access to entire path to the selected lock from a BP building with a guest using the provided settings.



Note: For email and phone parameters, at least one must be provided. If both are null, a network error will be returned.



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
| lockId | UUID of the lock to grant access to. |
| inviteType | type of invite (InAppInvite or TempDoorcodeInvite) with access settings. |



#### Throws


| |
|---|
| [SDKException](../../com.door.opendoor.android.core.api.exceptions/-s-d-k-exception/index.html) |
| [NetworkException](../../com.door.opendoor.android.core.api.exceptions/-network-exception/index.html) |



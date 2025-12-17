---
title: DoorClient
---
---
title: DoorClient
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api](../index.html)/[DoorClient](index.html)



# DoorClient



[androidJvm]\
interface [DoorClient](index.html)

Public OpenDOOR SDK Core Module.



Setup flow:



1. 
   Call setupWithToken() with a valid token to authenticate
2. 
   Use listenForLocks() or fetchLocks() to retrieve lock data
3. 
   Use unlock() or proximity unlock features as needed




All methods marked async perform work on background threads.



## Functions


| Name | Summary |
|---|---|
| [clear](clear.html) | [androidJvm]<br>abstract suspend fun [clear](clear.html)()<br>Performs logout by clearing database and saved token. |
| [fetchLocks](fetch-locks.html) | [androidJvm]<br>abstract suspend fun [fetchLocks](fetch-locks.html)(): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[Lock](../../com.door.opendoor.android.core.api.model/-lock/index.html)&gt;<br>Retrieves the locks of the current user. |
| [getAccessLogs](get-access-logs.html) | [androidJvm]<br>abstract suspend fun [getAccessLogs](get-access-logs.html)(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[AccessLog](../../com.door.opendoor.android.core.api.model/-access-log/index.html)&gt;<br>Retrieves access logs for a specific lock. |
| [guests](guests.html) | [androidJvm]<br>abstract suspend fun [guests](guests.html)(): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[Guest](../../com.door.opendoor.android.core.api.model/-guest/index.html)&gt;<br>Gets information for all guests with shared access. |
| [inviteGuests](invite-guests.html) | [androidJvm]<br>abstract suspend fun [inviteGuests](invite-guests.html)(firstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), lastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), email: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, phone: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, startTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html), endTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)?, deviceUuids: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)&gt;, passcodeType: [PasscodeType](../../com.door.opendoor.android.core.api.model/-passcode-type/index.html)): [Guest](../../com.door.opendoor.android.core.api.model/-guest/index.html)<br>Shares access to selected locks with a guest through the selected passcode type. |
| [inviteGuestsV2](invite-guests-v2.html) | [androidJvm]<br>abstract suspend fun [inviteGuestsV2](invite-guests-v2.html)(firstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), lastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), email: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, phone: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), inviteType: [InviteType](../../com.door.opendoor.android.core.api.model/-invite-type/index.html)): [Guest](../../com.door.opendoor.android.core.api.model/-guest/index.html)<br>Shares access to entire path to the selected lock from a BP building with a guest using the provided settings. |
| [listenForLocks](listen-for-locks.html) | [androidJvm]<br>abstract fun [listenForLocks](listen-for-locks.html)(): Flow&lt;[List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[Lock](../../com.door.opendoor.android.core.api.model/-lock/index.html)&gt;&gt;<br>Returns a stream of lock list updates.<br>[androidJvm]<br>abstract fun [listenForLocks](listen-for-locks.html)(listener: [LocksListener](../../com.door.opendoor.android.core.api.listeners/-locks-listener/index.html))<br>Callback-based variant of listenForLocks. |
| [listenForUnlockEvents](listen-for-unlock-events.html) | [androidJvm]<br>abstract fun [listenForUnlockEvents](listen-for-unlock-events.html)(): Flow&lt;[UnlockEvent](../../com.door.opendoor.android.core.api.model/-unlock-event/index.html)&gt;<br>Returns a stream of unlock events from both explicit and proximity unlocks.<br>[androidJvm]<br>abstract fun [listenForUnlockEvents](listen-for-unlock-events.html)(listener: [UnlockEventsListener](../../com.door.opendoor.android.core.api.listeners/-unlock-events-listener/index.html))<br>Callback-based variant of listenForUnlockEvents. |
| [setupWithToken](setup-with-token.html) | [androidJvm]<br>abstract suspend fun [setupWithToken](setup-with-token.html)(context: [Context](https://developer.android.com/reference/kotlin/android/content/Context.html), token: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), includeAllLocks: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false)<br>Authenticates the SDK with the provided token and initializes services. |
| [startProximityUnlock](start-proximity-unlock.html) | [androidJvm]<br>abstract suspend fun [startProximityUnlock](start-proximity-unlock.html)()<br>Starts the proximity unlock process. |
| [stopProximityUnlock](stop-proximity-unlock.html) | [androidJvm]<br>abstract suspend fun [stopProximityUnlock](stop-proximity-unlock.html)()<br>Stops the proximity unlock process. |
| [sync](sync.html) | [androidJvm]<br>abstract suspend fun [sync](sync.html)(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html))<br>Starts the active sync process for a lock. |
| [unlock](unlock.html) | [androidJvm]<br>abstract suspend fun [unlock](unlock.html)(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html))<br>Starts an explicit unlock for a given lock. |

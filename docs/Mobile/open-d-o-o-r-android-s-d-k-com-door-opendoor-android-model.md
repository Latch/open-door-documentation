---
title: com.door.opendoor.android.model
---
---
title: com.door.opendoor.android.model
---
//[OpenDOOR Android SDK](../../index.html)/[com.door.opendoor.android.model](index.html)



# Package-level declarations



## Types


| Name | Summary |
|---|---|
| [Access](-access/index.html) | [androidJvm]<br>data class [Access](-access/index.html)(val startTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html), val endTime: [LocalDateTime](https://developer.android.com/reference/kotlin/java/time/LocalDateTime.html)?, val doorCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) |
| [AccessLog](-access-log/index.html) | [androidJvm]<br>data class [AccessLog](-access-log/index.html)(val uuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), val epochTimeForEntryAttempt: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html), val imageFileName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val imageToken: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val guestUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?, val fullName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val method: [AccessLogMethod](-access-log-method/index.html)?, val result: [AccessLogResult](-access-log-result/index.html)?, val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?, val photoAvailability: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val userFirstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val userLastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val userNickname: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?) |
| [AccessLogMethod](-access-log-method/index.html) | [androidJvm]<br>enum [AccessLogMethod](-access-log-method/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)&lt;[AccessLogMethod](-access-log-method/index.html)&gt; |
| [AccessLogResult](-access-log-result/index.html) | [androidJvm]<br>enum [AccessLogResult](-access-log-result/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)&lt;[AccessLogResult](-access-log-result/index.html)&gt; |
| [AccessLogsResult](-access-logs-result/index.html) | [androidJvm]<br>sealed class [AccessLogsResult](-access-logs-result/index.html) |
| [DeviceApiVersion](-device-api-version/index.html) | [androidJvm]<br>sealed class [DeviceApiVersion](-device-api-version/index.html) |
| [DeviceType](-device-type/index.html) | [androidJvm]<br>enum [DeviceType](-device-type/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)&lt;[DeviceType](-device-type/index.html)&gt; |
| [Guest](-guest/index.html) | [androidJvm]<br>data class [Guest](-guest/index.html)(val uuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), val firstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val lastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val email: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val phone: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val guestAccesses: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[GuestAccess](-guest-access/index.html)&gt;) |
| [GuestAccess](-guest-access/index.html) | [androidJvm]<br>data class [GuestAccess](-guest-access/index.html)(val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), val passcodeType: [PasscodeType](-passcode-type/index.html), val startTime: LocalDateTime, val endTime: LocalDateTime?) |
| [GuestsResult](-guests-result/index.html) | [androidJvm]<br>sealed interface [GuestsResult](-guests-result/index.html) |
| [InitResult](-init-result/index.html) | [androidJvm]<br>sealed class [~~InitResult~~](-init-result/index.html) |
| [InviteGuestsResult](-invite-guests-result/index.html) | [androidJvm]<br>sealed class [InviteGuestsResult](-invite-guests-result/index.html) |
| [Lock](-lock/index.html) | [androidJvm]<br>data class [Lock](-lock/index.html)(val uuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val deviceTypeDto: [DeviceType](-device-type/index.html), val deviceApiVersionDto: [DeviceApiVersion](-device-api-version/index.html), val access: [Access](-access/index.html), val buildingUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)) |
| [LocksResult](-locks-result/index.html) | [androidJvm]<br>sealed class [LocksResult](-locks-result/index.html) |
| [PasscodeType](-passcode-type/index.html) | [androidJvm]<br>enum [PasscodeType](-passcode-type/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)&lt;[PasscodeType](-passcode-type/index.html)&gt; |
| [ProximityUnlockStatus](-proximity-unlock-status/index.html) | [androidJvm]<br>sealed class [ProximityUnlockStatus](-proximity-unlock-status/index.html) |
| [SetEnvironmentResult](-set-environment-result/index.html) | [androidJvm]<br>sealed interface [SetEnvironmentResult](-set-environment-result/index.html)<br>Represents the result of setting the environment in which the SDK will work. |
| [SetupResult](-setup-result/index.html) | [androidJvm]<br>sealed class [SetupResult](-setup-result/index.html)<br>Result class that signalizes the completion of the setup process of the Latch SDK. |
| [SyncResult](-sync-result/index.html) | [androidJvm]<br>sealed class [SyncResult](-sync-result/index.html) |
| [UnlockEvent](-unlock-event/index.html) | [androidJvm]<br>sealed class [UnlockEvent](-unlock-event/index.html) |

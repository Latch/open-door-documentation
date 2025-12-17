---
title: AccessLog
---
---
title: AccessLog
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.model](../index.html)/[AccessLog](index.html)



# AccessLog



[androidJvm]\
data class [AccessLog](index.html)(val uuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), val epochTimeForEntryAttempt: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html), val imageFileName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val imageToken: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val guestUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?, val fullName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val method: [AccessLogMethod](../-access-log-method/index.html)?, val result: [AccessLogResult](../-access-log-result/index.html)?, val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?, val photoAvailability: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val userFirstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val userLastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val userNickname: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?)

Record of an access attempt on a lock



## Constructors


| | |
|---|---|
| [AccessLog](-access-log.html) | [androidJvm]<br>constructor(uuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), epochTimeForEntryAttempt: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html), imageFileName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, imageToken: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, guestUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?, fullName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, method: [AccessLogMethod](../-access-log-method/index.html)?, result: [AccessLogResult](../-access-log-result/index.html)?, lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?, photoAvailability: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, userFirstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, userLastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, userNickname: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?) |


## Properties


| Name | Summary |
|---|---|
| [epochTimeForEntryAttempt](epoch-time-for-entry-attempt.html) | [androidJvm]<br>val [epochTimeForEntryAttempt](epoch-time-for-entry-attempt.html): [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)<br>Timestamp of the attempt (epoch millis) |
| [fullName](full-name.html) | [androidJvm]<br>val [fullName](full-name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?<br>Full name of the person who attempted access |
| [guestUuid](guest-uuid.html) | [androidJvm]<br>val [guestUuid](guest-uuid.html): [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?<br>Guest UUID if applicable |
| [imageFileName](image-file-name.html) | [androidJvm]<br>val [imageFileName](image-file-name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?<br>Image file name if available |
| [imageToken](image-token.html) | [androidJvm]<br>val [imageToken](image-token.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?<br>Image token if available |
| [lockUuid](lock-uuid.html) | [androidJvm]<br>val [lockUuid](lock-uuid.html): [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?<br>Lock UUID for the access attempt |
| [method](method.html) | [androidJvm]<br>val [method](method.html): [AccessLogMethod](../-access-log-method/index.html)?<br>Method used to attempt entry |
| [photoAvailability](photo-availability.html) | [androidJvm]<br>val [photoAvailability](photo-availability.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?<br>Photo availability status |
| [result](result.html) | [androidJvm]<br>val [result](result.html): [AccessLogResult](../-access-log-result/index.html)?<br>Outcome of the attempt |
| [userFirstName](user-first-name.html) | [androidJvm]<br>val [userFirstName](user-first-name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?<br>First name of the user |
| [userLastName](user-last-name.html) | [androidJvm]<br>val [userLastName](user-last-name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?<br>Last name of the user |
| [userNickname](user-nickname.html) | [androidJvm]<br>val [userNickname](user-nickname.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?<br>Nickname of the user |
| [uuid](uuid.html) | [androidJvm]<br>val [uuid](uuid.html): [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)<br>Unique log identifier |

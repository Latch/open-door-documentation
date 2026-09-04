---
title: AccessLog
excerpt: Record of an access attempt on a lock.
hidden: true
---

*Package `com.door.opendoor.android.core.api.model`*

```kotlin
data class AccessLog(val id: UUID, val epochTimeForEntryAttempt: Long, val imageFileName: String?, val imageToken: String?, val guestUuid: UUID?, val fullName: String?, val method: AccessLogMethod, val result: AccessLogResult, val lockUuid: UUID?, val photoAvailability: String?, val userFirstName: String?, val userLastName: String?, val userNickname: String?)
```

Record of an access attempt on a lock.

## Constructors

| | |
|---|---|
| AccessLog | constructor(id: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), epochTimeForEntryAttempt: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html), imageFileName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, imageToken: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, guestUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?, fullName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, method: [AccessLogMethod](doc:android-ref-accesslogmethod), result: [AccessLogResult](doc:android-ref-accesslogresult), lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?, photoAvailability: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, userFirstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, userLastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, userNickname: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?) |

## Properties

| Name | Summary |
|---|---|
| epochTimeForEntryAttempt | val epochTimeForEntryAttempt: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html) |
| fullName | val fullName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |
| guestUuid | val guestUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)? |
| id | val id: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html) |
| imageFileName | val imageFileName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |
| imageToken | val imageToken: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |
| lockUuid | val lockUuid: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)? |
| method | val method: [AccessLogMethod](doc:android-ref-accesslogmethod) |
| photoAvailability | val photoAvailability: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |
| result | val result: [AccessLogResult](doc:android-ref-accesslogresult) |
| userFirstName | val userFirstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |
| userLastName | val userLastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |
| userNickname | val userNickname: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

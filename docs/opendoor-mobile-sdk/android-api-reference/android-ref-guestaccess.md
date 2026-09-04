---
title: GuestAccess
excerpt: Access granted to a guest on a specific lock.
hidden: true
---

*Package `com.door.opendoor.android.core.api.model`*

```kotlin
data class GuestAccess(val invitationId: UUID?, val lockId: UUID, val lockName: String, val inviteType: InviteType, val passcodeType: PasscodeType, val startTime: Instant, val endTime: Instant?)
```

Access granted to a guest on a specific lock.

## Constructors

| | |
|---|---|
| GuestAccess | constructor(invitationId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)?, lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), lockName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), inviteType: [InviteType](doc:android-ref-invitetype), passcodeType: [PasscodeType](doc:android-ref-passcodetype), startTime: [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html), endTime: [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html)?) |

## Properties

| Name | Summary |
|---|---|
| endTime | val endTime: [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html)? |
| invitationId | val invitationId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)? |
| inviteType | val inviteType: [InviteType](doc:android-ref-invitetype) |
| lockId | val lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html) |
| lockName | val lockName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| passcodeType | val passcodeType: [PasscodeType](doc:android-ref-passcodetype) |
| startTime | val startTime: [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html) |

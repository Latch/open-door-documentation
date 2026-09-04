---
title: GuestInvitesException
excerpt: Partial or complete guest-invitation failure.
hidden: true
---

*Package `com.door.opendoor.android.core.api.exceptions`*

```kotlin
class GuestInvitesException(val failedLockErrors: List<LockActionException>, val successfulLockIds: List<UUID>, message: String = buildMessage(failedLockErrors, successfulLockIds)) : Exception
```

Partial or complete guest-invitation failure.

## Constructors

| | |
|---|---|
| GuestInvitesException | constructor(failedLockErrors: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[LockActionException](doc:android-ref-lockactionexception)&gt;, successfulLockIds: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)&gt;, message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = buildMessage(failedLockErrors, successfulLockIds)) |

## Types

| Name | Summary |
|---|---|
| Companion | object Companion |

## Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| failedLockErrors | val failedLockErrors: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[LockActionException](doc:android-ref-lockactionexception)&gt; |
| failedLockIds | val failedLockIds: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)&gt; |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |
| successfulLockIds | val successfulLockIds: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)&gt; |

## `Companion`

```kotlin
object Companion
```

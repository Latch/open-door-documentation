---
title: Guest
excerpt: Person with shared access to one or more locks.
hidden: true
---

*Package `com.door.opendoor.android.core.api.model`*

```kotlin
data class Guest(val id: UUID, val firstName: String, val lastName: String?, val email: String?, val phone: String?, val guestAccesses: List<GuestAccess>)
```

Person with shared access to one or more locks.

## Constructors

| | |
|---|---|
| Guest | constructor(id: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), firstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), lastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, email: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, phone: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, guestAccesses: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[GuestAccess](doc:android-ref-guestaccess)&gt;) |

## Properties

| Name | Summary |
|---|---|
| email | val email: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |
| firstName | val firstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| guestAccesses | val guestAccesses: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[GuestAccess](doc:android-ref-guestaccess)&gt; |
| id | val id: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html) |
| lastName | val lastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |
| phone | val phone: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

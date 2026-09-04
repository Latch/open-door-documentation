---
title: Lock
excerpt: User-visible lock information.
hidden: true
---

*Package `com.door.opendoor.android.core.api.model`*

```kotlin
data class Lock(val id: UUID, val name: String, val buildingId: UUID, val startTime: Instant, val endTime: Instant?, val doorCode: String?, val isShareable: Boolean)
```

User-visible lock information.

## Constructors

| | |
|---|---|
| Lock | constructor(id: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), buildingId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), startTime: [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html), endTime: [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html)?, doorCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, isShareable: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)) |

## Properties

| Name | Summary |
|---|---|
| buildingId | val buildingId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html) |
| doorCode | val doorCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |
| endTime | val endTime: [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html)? |
| id | val id: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html) |
| isShareable | val isShareable: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) |
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| startTime | val startTime: [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html) |

---
title: InAppInvite
excerpt: In-app access with time-based restrictions.
hidden: true
---

*Package `com.door.opendoor.android.core.api.model`*

```kotlin
data class InAppInvite(val accessType: AccessType?, val startTime: Instant, val endTime: Instant?, val showDoorcodes: Boolean?) : InviteType
```

In-app access with time-based restrictions.

## Constructors

| | |
|---|---|
| InAppInvite | constructor(accessType: [AccessType](doc:android-ref-accesstype)?, startTime: [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html), endTime: [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html)?, showDoorcodes: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)?) |

## Properties

| Name | Summary |
|---|---|
| accessType | open override val accessType: [AccessType](doc:android-ref-accesstype)? |
| endTime | val endTime: [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html)? |
| showDoorcodes | val showDoorcodes: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? |
| startTime | val startTime: [Instant](https://developer.android.com/reference/kotlin/java/time/Instant.html) |

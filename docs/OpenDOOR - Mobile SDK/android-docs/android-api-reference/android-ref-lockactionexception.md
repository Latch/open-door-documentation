---
title: LockActionException
excerpt: Failure while acting on one lock.
hidden: true
---

*Package `com.door.opendoor.android.core.api.exceptions`*

```kotlin
class LockActionException(val lockId: UUID, val error: Exception, message: String = &quot;Lock action failed for &quot;) : Exception
```

Failure while acting on one lock.

## Constructors

| | |
|---|---|
| LockActionException | constructor(lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), error: [Exception](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-exception/index.html), message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;Lock action failed for &quot;) |

## Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| error | val error: [Exception](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-exception/index.html) |
| lockId | val lockId: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html) |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

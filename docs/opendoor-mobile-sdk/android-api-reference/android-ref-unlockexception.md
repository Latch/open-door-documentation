---
title: UnlockException
excerpt: Explicit unlock request failure before an attempt starts.
hidden: true
---

*Package `com.door.opendoor.android.core.api.exceptions`*

```kotlin
sealed class UnlockException(message: String, throwable: Throwable? = null) : Exception
```

Explicit unlock request failure before an attempt starts.

#### Inheritors

| |
|---|
| LockNotFoundException |

## Constructors

| | |
|---|---|
| UnlockException | protected constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

## Types

| Name | Summary |
|---|---|
| LockNotFoundException | class LockNotFoundException(val identifier: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;Lock not found before unlock starts: &quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : UnlockException |

## Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `LockNotFoundException`

```kotlin
class LockNotFoundException(val identifier: String, message: String = &quot;Lock not found before unlock starts: &quot;, throwable: Throwable? = null) : UnlockException
```

### Constructors

| | |
|---|---|
| LockNotFoundException | constructor(identifier: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;Lock not found before unlock starts: &quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| identifier | val identifier: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

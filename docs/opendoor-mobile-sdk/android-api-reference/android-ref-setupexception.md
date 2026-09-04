---
title: SetupException
excerpt: Setup failure.
hidden: true
---

*Package `com.door.opendoor.android.core.api.exceptions`*

```kotlin
sealed class SetupException(message: String, throwable: Throwable? = null) : Exception
```

Setup failure.

#### Inheritors

| |
|---|
| InvalidTokenException |
| ConsentNotGrantedException |
| SetupInternalException |

## Constructors

| | |
|---|---|
| SetupException | protected constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

## Types

| Name | Summary |
|---|---|
| ConsentNotGrantedException | class ConsentNotGrantedException(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;User consent was not granted&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : SetupException |
| InvalidTokenException | class InvalidTokenException(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;The supplied token is invalid or expired&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : SetupException |
| SetupInternalException | class SetupInternalException(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : SetupException |

## Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `ConsentNotGrantedException`

```kotlin
class ConsentNotGrantedException(message: String = &quot;User consent was not granted&quot;, throwable: Throwable? = null) : SetupException
```

### Constructors

| | |
|---|---|
| ConsentNotGrantedException | constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;User consent was not granted&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `InvalidTokenException`

```kotlin
class InvalidTokenException(message: String = &quot;The supplied token is invalid or expired&quot;, throwable: Throwable? = null) : SetupException
```

### Constructors

| | |
|---|---|
| InvalidTokenException | constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;The supplied token is invalid or expired&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `SetupInternalException`

```kotlin
class SetupInternalException(message: String, throwable: Throwable? = null) : SetupException
```

### Constructors

| | |
|---|---|
| SetupInternalException | constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

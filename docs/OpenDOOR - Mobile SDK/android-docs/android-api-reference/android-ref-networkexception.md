---
title: NetworkException
excerpt: Network access failure.
hidden: true
---

*Package `com.door.opendoor.android.core.api.exceptions`*

```kotlin
sealed class NetworkException(message: String, throwable: Throwable? = null) : Exception
```

Network access failure.

#### Inheritors

| |
|---|
| InvalidTokenException |
| PayloadError |
| InternalNetworkException |

## Constructors

| | |
|---|---|
| NetworkException | protected constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

## Types

| Name | Summary |
|---|---|
| InternalNetworkException | class InternalNetworkException(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : NetworkException |
| InvalidTokenException | class InvalidTokenException(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;The supplied token is invalid or expired&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : NetworkException |
| PayloadError | class PayloadError(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : NetworkException |

## Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `InternalNetworkException`

```kotlin
class InternalNetworkException(message: String, throwable: Throwable? = null) : NetworkException
```

### Constructors

| | |
|---|---|
| InternalNetworkException | constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `InvalidTokenException`

```kotlin
class InvalidTokenException(message: String = &quot;The supplied token is invalid or expired&quot;, throwable: Throwable? = null) : NetworkException
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

## `PayloadError`

```kotlin
class PayloadError(message: String, throwable: Throwable? = null) : NetworkException
```

### Constructors

| | |
|---|---|
| PayloadError | constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

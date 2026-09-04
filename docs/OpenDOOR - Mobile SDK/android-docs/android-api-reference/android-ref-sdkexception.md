---
title: SDKException
excerpt: General SDK access failure.
hidden: true
---

*Package `com.door.opendoor.android.core.api.exceptions`*

```kotlin
sealed class SDKException(message: String, throwable: Throwable? = null) : Exception
```

General SDK access failure.

#### Inheritors

| |
|---|
| SDKNotInitializedException |
| InternalException |

## Constructors

| | |
|---|---|
| SDKException | protected constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

## Types

| Name | Summary |
|---|---|
| InternalException | class InternalException(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : SDKException |
| SDKNotInitializedException | class SDKNotInitializedException(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;The SDK has not been initialized with setupWithToken&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : SDKException |

## Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `InternalException`

```kotlin
class InternalException(message: String, throwable: Throwable? = null) : SDKException
```

### Constructors

| | |
|---|---|
| InternalException | constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `SDKNotInitializedException`

```kotlin
class SDKNotInitializedException(message: String = &quot;The SDK has not been initialized with setupWithToken&quot;, throwable: Throwable? = null) : SDKException
```

### Constructors

| | |
|---|---|
| SDKNotInitializedException | constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;The SDK has not been initialized with setupWithToken&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

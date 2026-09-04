---
title: SyncException
excerpt: Active sync failure.
hidden: true
---

*Package `com.door.opendoor.android.core.api.exceptions`*

```kotlin
sealed class SyncException(message: String, throwable: Throwable? = null) : Exception
```

Active sync failure.

#### Inheritors

| |
|---|
| LockNotFoundException |
| CanceledException |
| UnlockInProgressException |
| SyncInternalException |

## Constructors

| | |
|---|---|
| SyncException | protected constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

## Types

| Name | Summary |
|---|---|
| CanceledException | class CanceledException(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;Sync was canceled&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : SyncException |
| LockNotFoundException | class LockNotFoundException(val identifier: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;Lock not found during sync: &quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : SyncException |
| SyncInternalException | class SyncInternalException(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : SyncException |
| UnlockInProgressException | class UnlockInProgressException(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;An unlock is already in progress&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : SyncException |

## Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `CanceledException`

```kotlin
class CanceledException(message: String = &quot;Sync was canceled&quot;, throwable: Throwable? = null) : SyncException
```

### Constructors

| | |
|---|---|
| CanceledException | constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;Sync was canceled&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `LockNotFoundException`

```kotlin
class LockNotFoundException(val identifier: String, message: String = &quot;Lock not found during sync: &quot;, throwable: Throwable? = null) : SyncException
```

### Constructors

| | |
|---|---|
| LockNotFoundException | constructor(identifier: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;Lock not found during sync: &quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| identifier | val identifier: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `SyncInternalException`

```kotlin
class SyncInternalException(message: String, throwable: Throwable? = null) : SyncException
```

### Constructors

| | |
|---|---|
| SyncInternalException | constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `UnlockInProgressException`

```kotlin
class UnlockInProgressException(message: String = &quot;An unlock is already in progress&quot;, throwable: Throwable? = null) : SyncException
```

### Constructors

| | |
|---|---|
| UnlockInProgressException | constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;An unlock is already in progress&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

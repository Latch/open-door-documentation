---
title: BluetoothException
excerpt: Bluetooth access failure.
hidden: true
---

*Package `com.door.opendoor.android.core.api.exceptions`*

```kotlin
sealed class BluetoothException(message: String, throwable: Throwable? = null) : Exception
```

Bluetooth access failure.

#### Inheritors

| |
|---|
| BluetoothDisabledException |
| BluetoothPermissionDeniedException |

## Constructors

| | |
|---|---|
| BluetoothException | protected constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

## Types

| Name | Summary |
|---|---|
| BluetoothDisabledException | class BluetoothDisabledException(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;Bluetooth is disabled&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : BluetoothException |
| BluetoothPermissionDeniedException | class BluetoothPermissionDeniedException(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;Bluetooth permission was denied&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : BluetoothException |

## Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `BluetoothDisabledException`

```kotlin
class BluetoothDisabledException(message: String = &quot;Bluetooth is disabled&quot;, throwable: Throwable? = null) : BluetoothException
```

### Constructors

| | |
|---|---|
| BluetoothDisabledException | constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;Bluetooth is disabled&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

## `BluetoothPermissionDeniedException`

```kotlin
class BluetoothPermissionDeniedException(message: String = &quot;Bluetooth permission was denied&quot;, throwable: Throwable? = null) : BluetoothException
```

### Constructors

| | |
|---|---|
| BluetoothPermissionDeniedException | constructor(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = &quot;Bluetooth permission was denied&quot;, throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

### Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

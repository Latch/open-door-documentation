---
title: UnlockFailureReason
excerpt: Canonical reason an in-flight unlock failed.
hidden: true
---

*Package `com.door.opendoor.android.core.api.model`*

```kotlin
sealed class UnlockFailureReason
```

Canonical reason an in-flight unlock failed.

#### Inheritors

| |
|---|
| BluetoothDisabled |
| OutOfSchedule |
| LockNotFound |
| ConnectionFailed |
| AuthFailed |
| Internal |

## Constructors

| | |
|---|---|
| UnlockFailureReason | protected constructor() |

## Types

| Name | Summary |
|---|---|
| AuthFailed | data object AuthFailed : UnlockFailureReason |
| BluetoothDisabled | data object BluetoothDisabled : UnlockFailureReason |
| ConnectionFailed | data object ConnectionFailed : UnlockFailureReason |
| Internal | data class Internal(val code: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) : UnlockFailureReason |
| LockNotFound | data object LockNotFound : UnlockFailureReason |
| OutOfSchedule | data object OutOfSchedule : UnlockFailureReason |

## `AuthFailed`

```kotlin
data object AuthFailed : UnlockFailureReason
```

## `BluetoothDisabled`

```kotlin
data object BluetoothDisabled : UnlockFailureReason
```

## `ConnectionFailed`

```kotlin
data object ConnectionFailed : UnlockFailureReason
```

## `Internal`

```kotlin
data class Internal(val code: String) : UnlockFailureReason
```

### Constructors

| | |
|---|---|
| Internal | constructor(code: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) |

### Properties

| Name | Summary |
|---|---|
| code | val code: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |

## `LockNotFound`

```kotlin
data object LockNotFound : UnlockFailureReason
```

## `OutOfSchedule`

```kotlin
data object OutOfSchedule : UnlockFailureReason
```

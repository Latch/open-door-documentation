---
title: UnlockEventStatus
excerpt: Lifecycle status carried by an unlock event.
hidden: true
---

*Package `com.door.opendoor.android.core.api.model`*

```kotlin
sealed class UnlockEventStatus
```

Lifecycle status carried by an unlock event.

#### Inheritors

| |
|---|
| Started |
| ConnectForSetupSync |
| SetupSync |
| UpdateSyncPackage |
| ConnectForUnlock |
| Unlock |
| Failed |
| Canceled |
| Success |

## Constructors

| | |
|---|---|
| UnlockEventStatus | protected constructor() |

## Types

| Name | Summary |
|---|---|
| Canceled | data object Canceled : UnlockEventStatus |
| ConnectForSetupSync | data class ConnectForSetupSync(val attempt: [UnlockAttempt](doc:android-ref-unlockattempt)) : UnlockEventStatus |
| ConnectForUnlock | data class ConnectForUnlock(val attempt: [UnlockAttempt](doc:android-ref-unlockattempt)) : UnlockEventStatus |
| Failed | data class Failed(val reason: [UnlockFailureReason](doc:android-ref-unlockfailurereason)) : UnlockEventStatus |
| SetupSync | data class SetupSync(val attempt: [UnlockAttempt](doc:android-ref-unlockattempt)) : UnlockEventStatus |
| Started | data object Started : UnlockEventStatus |
| Success | data object Success : UnlockEventStatus |
| Unlock | data class Unlock(val attempt: [UnlockAttempt](doc:android-ref-unlockattempt)) : UnlockEventStatus |
| UpdateSyncPackage | data object UpdateSyncPackage : UnlockEventStatus |

## `Canceled`

```kotlin
data object Canceled : UnlockEventStatus
```

## `ConnectForSetupSync`

```kotlin
data class ConnectForSetupSync(val attempt: UnlockAttempt) : UnlockEventStatus
```

### Constructors

| | |
|---|---|
| ConnectForSetupSync | constructor(attempt: [UnlockAttempt](doc:android-ref-unlockattempt)) |

### Properties

| Name | Summary |
|---|---|
| attempt | val attempt: [UnlockAttempt](doc:android-ref-unlockattempt) |

## `ConnectForUnlock`

```kotlin
data class ConnectForUnlock(val attempt: UnlockAttempt) : UnlockEventStatus
```

### Constructors

| | |
|---|---|
| ConnectForUnlock | constructor(attempt: [UnlockAttempt](doc:android-ref-unlockattempt)) |

### Properties

| Name | Summary |
|---|---|
| attempt | val attempt: [UnlockAttempt](doc:android-ref-unlockattempt) |

## `Failed`

```kotlin
data class Failed(val reason: UnlockFailureReason) : UnlockEventStatus
```

### Constructors

| | |
|---|---|
| Failed | constructor(reason: [UnlockFailureReason](doc:android-ref-unlockfailurereason)) |

### Properties

| Name | Summary |
|---|---|
| reason | val reason: [UnlockFailureReason](doc:android-ref-unlockfailurereason) |

## `SetupSync`

```kotlin
data class SetupSync(val attempt: UnlockAttempt) : UnlockEventStatus
```

### Constructors

| | |
|---|---|
| SetupSync | constructor(attempt: [UnlockAttempt](doc:android-ref-unlockattempt)) |

### Properties

| Name | Summary |
|---|---|
| attempt | val attempt: [UnlockAttempt](doc:android-ref-unlockattempt) |

## `Started`

```kotlin
data object Started : UnlockEventStatus
```

## `Success`

```kotlin
data object Success : UnlockEventStatus
```

## `Unlock`

```kotlin
data class Unlock(val attempt: UnlockAttempt) : UnlockEventStatus
```

### Constructors

| | |
|---|---|
| Unlock | constructor(attempt: [UnlockAttempt](doc:android-ref-unlockattempt)) |

### Properties

| Name | Summary |
|---|---|
| attempt | val attempt: [UnlockAttempt](doc:android-ref-unlockattempt) |

## `UpdateSyncPackage`

```kotlin
data object UpdateSyncPackage : UnlockEventStatus
```

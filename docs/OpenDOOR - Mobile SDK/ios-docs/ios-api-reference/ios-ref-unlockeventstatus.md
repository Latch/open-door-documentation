---
title: UnlockEventStatus
excerpt: Lifecycle status carried by an unlock event.
hidden: true
---

*Enumeration*

```swift
enum UnlockEventStatus
```

Lifecycle status carried by an unlock event.

## Enumeration Cases

### `UnlockEventStatus.canceled`

```swift
case canceled
```

### `UnlockEventStatus.connectForSetupSync(attempt:)`

```swift
case connectForSetupSync(attempt: UnlockAttempt)
```

### `UnlockEventStatus.connectForUnlock(attempt:)`

```swift
case connectForUnlock(attempt: UnlockAttempt)
```

### `UnlockEventStatus.failed(_:)`

```swift
case failed(UnlockFailureReason)
```

### `UnlockEventStatus.setupSync(attempt:)`

```swift
case setupSync(attempt: UnlockAttempt)
```

### `UnlockEventStatus.started`

```swift
case started
```

### `UnlockEventStatus.success`

```swift
case success
```

### `UnlockEventStatus.unlock(attempt:)`

```swift
case unlock(attempt: UnlockAttempt)
```

### `UnlockEventStatus.updateSyncPackage`

```swift
case updateSyncPackage
```

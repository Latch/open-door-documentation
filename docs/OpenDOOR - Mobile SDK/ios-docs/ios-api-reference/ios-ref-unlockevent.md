---
title: UnlockEvent
excerpt: Event emitted during explicit and proximity unlock operations.
hidden: true
---

*Structure*

```swift
struct UnlockEvent
```

Event emitted during explicit and proximity unlock operations.

## Initializers

### `init(lock:method:status:)`

```swift
init(lock: Lock?, method: UnlockEventMethod, status: UnlockEventStatus)
```

## Instance Properties

### `lock`

```swift
let lock: Lock?
```

### `method`

```swift
let method: UnlockEventMethod
```

### `status`

```swift
let status: UnlockEventStatus
```

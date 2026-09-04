---
title: LockActionError
excerpt: Failure while acting on one lock.
hidden: true
---

*Structure*

```swift
struct LockActionError
```

Failure while acting on one lock.

## Initializers

### `init(lockID:error:)`

```swift
init(lockID: UUID, error: any OpenDOORSDKError)
```

## Instance Properties

### `description`

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

### `error`

```swift
let error: any OpenDOORSDKError
```

### `lockID`

```swift
let lockID: UUID
```

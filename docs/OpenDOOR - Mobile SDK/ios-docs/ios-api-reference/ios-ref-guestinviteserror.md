---
title: GuestInvitesError
excerpt: Partial or complete guest-invitation failure.
hidden: true
---

*Structure*

```swift
struct GuestInvitesError
```

Partial or complete guest-invitation failure.

## Initializers

### `init(failedLockErrors:successfulLockIDs:)`

```swift
init(failedLockErrors: [LockActionError], successfulLockIDs: [UUID])
```

## Instance Properties

### `description`

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

### `failedLockErrors`

```swift
let failedLockErrors: [LockActionError]
```

### `failedLockIDs`

```swift
var failedLockIDs: [UUID] { get }
```

### `successfulLockIDs`

```swift
let successfulLockIDs: [UUID]
```

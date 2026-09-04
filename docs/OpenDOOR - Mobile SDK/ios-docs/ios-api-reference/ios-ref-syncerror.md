---
title: SyncError
excerpt: Active sync failure.
hidden: true
---

*Enumeration*

```swift
enum SyncError
```

Active sync failure.

## Enumeration Cases

### `SyncError.canceled`

```swift
case canceled
```

Sync was canceled.

### `SyncError.lockNotFound(_:)`

```swift
case lockNotFound(String)
```

Lock not found during sync.

### `SyncError.syncInternalError(_:)`

```swift
case syncInternalError(String)
```

Internal sync error.

### `SyncError.unlockInProgress`

```swift
case unlockInProgress
```

An unlock is already in progress.

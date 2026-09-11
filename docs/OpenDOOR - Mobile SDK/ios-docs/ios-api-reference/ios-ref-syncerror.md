---
title: SyncError
excerpt: OpenDOOR iOS SDK 2.1.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

Sync access error

## Declaration

```swift
public enum SyncError : OpenDOORSDKError {
  case lockNotFound(String)
  case canceled
  case unlockInProgress
  case syncInternalError(String)
}

extension SyncError {
  public var description: String {
    get
  }
}
```

## SyncError.canceled

```swift
case canceled
```

Sync operation was canceled

## description

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

## SyncError.lockNotFound(_:)

```swift
case lockNotFound(String)
```

[Lock](doc:ios-ref-lock) not found during sync

## SyncError.syncInternalError(_:)

```swift
case syncInternalError(String)
```

An internal error occurred

## SyncError.unlockInProgress

```swift
case unlockInProgress
```

Unlock operation is in progress

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

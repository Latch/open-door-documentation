---
title: SyncError
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Active sync failure.

## Declaration

```swift
public enum SyncError : OpenDOORCore::OpenDOORSDKError {
  case lockNotFound(Swift::String)
  case canceled
  case unlockInProgress
  case syncInternalError(Swift::String)
}
```

## SyncError.canceled

```swift
case canceled
```

Sync was canceled.

## SyncError.lockNotFound(_:)

```swift
case lockNotFound(String)
```

Lock not found during sync.

## SyncError.syncInternalError(_:)

```swift
case syncInternalError(String)
```

Internal sync error.

## SyncError.unlockInProgress

```swift
case unlockInProgress
```

An unlock is already in progress.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

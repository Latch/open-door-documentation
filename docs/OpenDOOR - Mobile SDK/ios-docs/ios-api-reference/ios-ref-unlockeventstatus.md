---
title: UnlockEventStatus
excerpt: OpenDOOR iOS SDK 2.1.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

Events emitted during unlock operations

## Declaration

```swift
public enum UnlockEventStatus : Equatable {
  case started
  case setupSync
  case failed(UnlockFailureReason)
  case canceled
  case success
  public static func == (a: UnlockEventStatus, b: UnlockEventStatus) -> Bool
}
```

## UnlockEventStatus.canceled

```swift
case canceled
```

Unlock was canceled (e.g., when starting unlock for another lock)

## UnlockEventStatus.failed(_:)

```swift
case failed(UnlockFailureReason)
```

Unlock failed

## UnlockEventStatus.setupSync

```swift
case setupSync
```

The lock is being set up.

## UnlockEventStatus.started

```swift
case started
```

Unlock process has started

## UnlockEventStatus.success

```swift
case success
```

[Lock](doc:ios-ref-lock) was successfully unlocked

## Related types

[UnlockFailureReason](doc:ios-ref-unlockfailurereason)

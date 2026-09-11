---
title: UnlockEventStatus
excerpt: OpenDOOR iOS SDK 2.2.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Events emitted during unlock operations.

## Declaration

```swift
public enum UnlockEventStatus : Equatable {
  case started
  case connectForSetupSync(attempt: UnlockAttempt)
  case setupSync(attempt: UnlockAttempt)
  case updateSyncPackage
  case connectForUnlock(attempt: UnlockAttempt)
  case unlock(attempt: UnlockAttempt)
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

Unlock was canceled (e.g., when starting unlock for another lock).

## UnlockEventStatus.connectForSetupSync(attempt:)

```swift
case connectForSetupSync(attempt: UnlockAttempt)
```

BLE connection established for setup sync.

## UnlockEventStatus.connectForUnlock(attempt:)

```swift
case connectForUnlock(attempt: UnlockAttempt)
```

BLE connection established for unlock.

## UnlockEventStatus.failed(_:)

```swift
case failed(UnlockFailureReason)
```

Unlock failed.

## UnlockEventStatus.setupSync(attempt:)

```swift
case setupSync(attempt: UnlockAttempt)
```

Setup sync task completed (success or failure).

## UnlockEventStatus.started

```swift
case started
```

Unlock process has started.

## UnlockEventStatus.success

```swift
case success
```

[Lock](doc:ios-ref-lock) was successfully unlocked.

## UnlockEventStatus.unlock(attempt:)

```swift
case unlock(attempt: UnlockAttempt)
```

Unlock task completed (success or failure).

## UnlockEventStatus.updateSyncPackage

```swift
case updateSyncPackage
```

Sync package fetched from the network in the recovery flow.

## Related types

[UnlockAttempt](doc:ios-ref-unlockattempt) · [UnlockFailureReason](doc:ios-ref-unlockfailurereason)

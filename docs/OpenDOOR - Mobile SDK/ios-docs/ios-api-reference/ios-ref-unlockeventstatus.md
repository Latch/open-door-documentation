---
title: UnlockEventStatus
excerpt: OpenDOOR iOS SDK 2.3.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Lifecycle status carried by an unlock event.

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

## UnlockEventStatus.connectForUnlock(attempt:)

```swift
case connectForUnlock(attempt: UnlockAttempt)
```

## UnlockEventStatus.failed(_:)

```swift
case failed(UnlockFailureReason)
```

Unlock failed.

## UnlockEventStatus.setupSync(attempt:)

```swift
case setupSync(attempt: UnlockAttempt)
```

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

## UnlockEventStatus.updateSyncPackage

```swift
case updateSyncPackage
```

## Related types

[UnlockAttempt](doc:ios-ref-unlockattempt) · [UnlockFailureReason](doc:ios-ref-unlockfailurereason)

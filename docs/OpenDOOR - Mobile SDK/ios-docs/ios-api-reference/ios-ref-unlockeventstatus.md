---
title: UnlockEventStatus
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Lifecycle status carried by an unlock event.

## Declaration

```swift
public enum UnlockEventStatus : Swift::Equatable {
  case started
  case connectForSetupSync(attempt: OpenDOORCore::UnlockAttempt)
  case setupSync(attempt: OpenDOORCore::UnlockAttempt)
  case updateSyncPackage
  case connectForUnlock(attempt: OpenDOORCore::UnlockAttempt)
  case unlock(attempt: OpenDOORCore::UnlockAttempt)
  case failed(OpenDOORCore::UnlockFailureReason)
  case canceled
  case success
  public static func == (a: OpenDOORCore::UnlockEventStatus, b: OpenDOORCore::UnlockEventStatus) -> Swift::Bool
}
```

## UnlockEventStatus.canceled

```swift
case canceled
```

Unlock was canceled, for example by cancelUnlock or by starting an unlock for another lock.

## UnlockEventStatus.connectForSetupSync(attempt:)

```swift
case connectForSetupSync(attempt: UnlockAttempt)
```

BLE connect phase before the setup sync.

### Discussion

Emitted when the SDK starts connecting to the lock to send it a setup sync.

## UnlockEventStatus.connectForUnlock(attempt:)

```swift
case connectForUnlock(attempt: UnlockAttempt)
```

BLE connect phase before unlocking.

### Discussion

Follows ConnectForSetupSync and SetupSync when a setup sync runs first. Otherwise it’s the first connection of the attempt.

## UnlockEventStatus.failed(_:)

```swift
case failed(UnlockFailureReason)
```

Unlock failed.

## UnlockEventStatus.setupSync(attempt:)

```swift
case setupSync(attempt: UnlockAttempt)
```

Setup sync before unlock.

### Discussion

Emitted after the setup connection is established, before the sync package is sent. Explicit and proximity unlocks can both emit it.

## UnlockEventStatus.started

```swift
case started
```

Unlock process has started.

## UnlockEventStatus.success

```swift
case success
```

Lock was successfully unlocked.

## UnlockEventStatus.unlock(attempt:)

```swift
case unlock(attempt: UnlockAttempt)
```

Unlock phase after the BLE connection is established.

### Discussion

Emitted before the unlock is sent to the lock, so the final Success or Failed status isn’t known yet.

## UnlockEventStatus.updateSyncPackage

```swift
case updateSyncPackage
```

Sync package download in progress (recovery path).

### Discussion

Emitted when the recovery attempt downloads a fresh sync package before retrying the setup sync and the unlock. It carries no attempt because it only occurs in the recovery attempt.

## Related types

[UnlockAttempt](doc:ios-ref-unlockattempt) · [UnlockFailureReason](doc:ios-ref-unlockfailurereason)

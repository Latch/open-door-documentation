---
title: UnlockFailureReason
excerpt: OpenDOOR iOS SDK 2.1.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

Reasons why an unlock can fail

## Declaration

```swift
public enum UnlockFailureReason : Error, Equatable {
  case bluetoothDisabled
  case outOfSchedule
  case timeout(String)
  case unlockInternalError(String)
  public static func == (a: UnlockFailureReason, b: UnlockFailureReason) -> Bool
}

extension UnlockFailureReason : CustomStringConvertible {
  public var description: String {
    get
  }
}
```

## UnlockFailureReason.bluetoothDisabled

```swift
case bluetoothDisabled
```

The current device does not have Bluetooth enabled.

## description

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

## UnlockFailureReason.outOfSchedule

```swift
case outOfSchedule
```

Access attempted outside of device access schedule

## UnlockFailureReason.timeout(_:)

```swift
case timeout(String)
```

Unlock failed to complete in a reasonable amount of time.

## UnlockFailureReason.unlockInternalError(_:)

```swift
case unlockInternalError(String)
```

An internal error occurred

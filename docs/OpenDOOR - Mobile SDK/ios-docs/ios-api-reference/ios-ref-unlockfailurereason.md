---
title: UnlockFailureReason
excerpt: OpenDOOR iOS SDK 2.2.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Reasons why an unlock can fail.

## Declaration

```swift
public enum UnlockFailureReason : Error, Equatable {
  case bluetoothDisabled
  case outOfSchedule
  case lockNotFound
  case connectionFailed
  case authFailed
  case `internal`(String)
  public static func == (a: UnlockFailureReason, b: UnlockFailureReason) -> Bool
}

extension UnlockFailureReason : CustomStringConvertible {
  public var description: String {
    get
  }
}
```

## UnlockFailureReason.authFailed

```swift
case authFailed
```

Recovery sync or download failure.

## UnlockFailureReason.bluetoothDisabled

```swift
case bluetoothDisabled
```

Bluetooth is off OR Bluetooth permission denied.

## UnlockFailureReason.connectionFailed

```swift
case connectionFailed
```

BLE connection failed OR timed out.

## description

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

## UnlockFailureReason.internal(_:)

```swift
case `internal`(String)
```

Any other failure — message is a human-readable description.

## UnlockFailureReason.lockNotFound

```swift
case lockNotFound
```

BLE scan found no peripheral.

## UnlockFailureReason.outOfSchedule

```swift
case outOfSchedule
```

Access attempted outside of door access schedule.

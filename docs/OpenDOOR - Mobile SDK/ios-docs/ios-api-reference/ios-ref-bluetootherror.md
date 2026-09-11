---
title: BluetoothError
excerpt: OpenDOOR iOS SDK 2.1.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

Bluetooth access error

## Declaration

```swift
public enum BluetoothError : OpenDOORSDKError {
  case bluetoothDisabled
  case bluetoothPermissionDenied
  public static func == (a: BluetoothError, b: BluetoothError) -> Bool
  public func hash(into hasher: inout Hasher)
  public var hashValue: Int {
    get
  }
}

extension BluetoothError {
  public var description: String {
    get
  }
}

extension BluetoothError : Equatable {}

extension BluetoothError : Hashable {}
```

## BluetoothError.bluetoothDisabled

```swift
case bluetoothDisabled
```

The current device does not have Bluetooth enabled

## BluetoothError.bluetoothPermissionDenied

```swift
case bluetoothPermissionDenied
```

User denied [OpenDOOR](doc:ios-ref-opendoor) SDK access to use the device’s Bluetooth

## description

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

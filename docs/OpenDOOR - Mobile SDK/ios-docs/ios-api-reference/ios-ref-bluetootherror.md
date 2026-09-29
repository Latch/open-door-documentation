---
title: BluetoothError
excerpt: OpenDOOR iOS SDK 2.3.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Bluetooth access failure.

## Declaration

```swift
public enum BluetoothError : OpenDOORSDKError {
  case disabled
  case permissionDenied
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

## description

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

## BluetoothError.disabled

```swift
case disabled
```

Bluetooth is disabled.

## BluetoothError.permissionDenied

```swift
case permissionDenied
```

Bluetooth permission was denied.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

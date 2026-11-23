---
title: BluetoothError
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Bluetooth access failure.

## Declaration

```swift
public enum BluetoothError : OpenDOORCore::OpenDOORSDKError {
  case disabled
  case permissionDenied
  public static func == (a: OpenDOORCore::BluetoothError, b: OpenDOORCore::BluetoothError) -> Swift::Bool
  public func hash(into hasher: inout Swift::Hasher)
  public var hashValue: Swift::Int {
    get
  }
}
```

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

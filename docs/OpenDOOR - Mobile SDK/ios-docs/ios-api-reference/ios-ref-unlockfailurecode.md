---
title: UnlockFailureCode
excerpt: OpenDOOR iOS SDK 2.3.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Cause of an unlock failure that has no more specific reason.

## Declaration

```swift
public enum UnlockFailureCode : String, Equatable {
  case bluetoothUnavailable
  case deviceNotSupported
  case keyFetchFailed
  case setupSyncFailed
  case transportError
  case unexpected
  public init?(rawValue: String)
  public typealias RawValue = String
  public var rawValue: String {
    get
  }
}

extension UnlockFailureCode : Hashable {}

extension UnlockFailureCode : RawRepresentable {}
```

## UnlockFailureCode.bluetoothUnavailable

```swift
case bluetoothUnavailable
```

The device has no usable Bluetooth hardware.

## UnlockFailureCode.deviceNotSupported

```swift
case deviceNotSupported
```

The lock model does not support BLE unlock.

## init(rawValue:)

```swift
init?(rawValue: String)
```

Inherited from `RawRepresentable.init(rawValue:)`.

## UnlockFailureCode.keyFetchFailed

```swift
case keyFetchFailed
```

The signed key could not be fetched before the unlock started.

## UnlockFailureCode.setupSyncFailed

```swift
case setupSyncFailed
```

Setup sync did not complete.

## UnlockFailureCode.transportError

```swift
case transportError
```

A Bluetooth operation failed, with no more specific classification.

## UnlockFailureCode.unexpected

```swift
case unexpected
```

A failure the SDK does not account for.

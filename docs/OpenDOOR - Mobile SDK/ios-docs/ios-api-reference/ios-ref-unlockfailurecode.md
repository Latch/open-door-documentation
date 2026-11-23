---
title: UnlockFailureCode
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Cause of an unlock failure that has no more specific reason.

## Declaration

```swift
public enum UnlockFailureCode : Swift::String, Swift::Equatable {
  case bluetoothUnavailable
  case deviceNotSupported
  case keyFetchFailed
  case setupSyncFailed
  case transportError
  case unexpected
  case networkError
  case remoteUnlockInProgress
  case remoteUnlockFailed
  case remoteUnlockTimedOut
  public init?(rawValue: Swift::String)
  public typealias RawValue = Swift::String
  public var rawValue: Swift::String {
    get
  }
}
```

## init(rawValue:)

```swift
init?(rawValue: String)
```

Inherited from `RawRepresentable.init(rawValue:)`.

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

## UnlockFailureCode.keyFetchFailed

```swift
case keyFetchFailed
```

The signed key could not be fetched before the unlock started.

## UnlockFailureCode.networkError

```swift
case networkError
```

A network request failed or returned an error.

## UnlockFailureCode.remoteUnlockFailed

```swift
case remoteUnlockFailed
```

The door reported that the remote unlock failed.

## UnlockFailureCode.remoteUnlockInProgress

```swift
case remoteUnlockInProgress
```

A remote unlock of this door is already in progress.

## UnlockFailureCode.remoteUnlockTimedOut

```swift
case remoteUnlockTimedOut
```

No remote unlock result arrived in time. The door may still open.

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

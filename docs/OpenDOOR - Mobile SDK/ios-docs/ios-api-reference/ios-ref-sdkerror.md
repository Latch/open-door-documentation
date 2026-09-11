---
title: SDKError
excerpt: OpenDOOR iOS SDK 2.1.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

SDK access error

## Declaration

```swift
public enum SDKError : OpenDOORSDKError {
  case sdkNotInitialized
  case sdkInternalError(String)
}

extension SDKError {
  public var description: String {
    get
  }
}
```

## description

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

## SDKError.sdkInternalError(_:)

```swift
case sdkInternalError(String)
```

An internal error occurred

## SDKError.sdkNotInitialized

```swift
case sdkNotInitialized
```

The SDK has not been initialized with setupWithToken

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

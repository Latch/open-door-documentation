---
title: NetworkError
excerpt: OpenDOOR iOS SDK 2.3.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Network access failure.

## Declaration

```swift
public enum NetworkError : OpenDOORSDKError {
  case invalidToken
  case payloadError(String)
  case internalNetworkError(String)
}

extension NetworkError {
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

## NetworkError.internalNetworkError(_:)

```swift
case internalNetworkError(String)
```

Internal network error.

## NetworkError.invalidToken

```swift
case invalidToken
```

The supplied token is invalid or expired.

## NetworkError.payloadError(_:)

```swift
case payloadError(String)
```

Backend payload error.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

---
title: NetworkError
excerpt: OpenDOOR iOS SDK 2.2.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Network access error

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

Internal network error (404, parsing errors, etc)

## NetworkError.invalidToken

```swift
case invalidToken
```

The supplied authorization token is invalid and should be refreshed.

## NetworkError.payloadError(_:)

```swift
case payloadError(String)
```

Network error with message from backend

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

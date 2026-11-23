---
title: NetworkError
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Network access failure.

## Declaration

```swift
public enum NetworkError : OpenDOORCore::OpenDOORSDKError {
  case invalidToken
  case payloadError(Swift::String)
  case internalNetworkError(Swift::String)
}
```

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

Network error with a message from the server.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

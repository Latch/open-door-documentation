---
title: SetupError
excerpt: OpenDOOR iOS SDK 2.2.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Setup access error

## Declaration

```swift
public enum SetupError : OpenDOORSDKError {
  case invalidToken
  case consentNotGranted
  case setupInternalError(String)
}

extension SetupError {
  public var description: String {
    get
  }
}
```

## SetupError.consentNotGranted

```swift
case consentNotGranted
```

User consent not granted

## description

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

## SetupError.invalidToken

```swift
case invalidToken
```

The supplied authorization token is invalid and should be refreshed.

## SetupError.setupInternalError(_:)

```swift
case setupInternalError(String)
```

An internal error occurred

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

---
title: RevokeGuestError
excerpt: OpenDOOR iOS SDK 2.1.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)



## Declaration

```swift
public enum RevokeGuestError : OpenDOORSDKError {
  case passcodeTypeCantBeRevoked
  case deviceNotFound
  case `internal`(String)
}

extension RevokeGuestError {
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

## RevokeGuestError.deviceNotFound

```swift
case deviceNotFound
```

Failed to find a device

## RevokeGuestError.internal(_:)

```swift
case `internal`(String)
```

An unexpected error occured.

## RevokeGuestError.passcodeTypeCantBeRevoked

```swift
case passcodeTypeCantBeRevoked
```

The [Guest](doc:ios-ref-guest) must have only PERMANENT Passcode Type access to this Device (aka App Access) to be able to revoke access

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

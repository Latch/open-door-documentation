---
title: RevokeGuestError
excerpt: OpenDOOR iOS SDK 2.3.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

[Guest](doc:ios-ref-guest)-access revocation failure.

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

Device was not found.

## RevokeGuestError.internal(_:)

```swift
case `internal`(String)
```

Internal revocation error.

## RevokeGuestError.passcodeTypeCantBeRevoked

```swift
case passcodeTypeCantBeRevoked
```

This passcode type cannot be revoked.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

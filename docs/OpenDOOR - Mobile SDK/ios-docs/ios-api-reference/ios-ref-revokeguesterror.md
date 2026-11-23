---
title: RevokeGuestError
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Guest-access revocation failure.

## Declaration

```swift
public enum RevokeGuestError : OpenDOORCore::OpenDOORSDKError {
  case passcodeTypeCantBeRevoked
  case deviceNotFound
  case `internal`(Swift::String)
}
```

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

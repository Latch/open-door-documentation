---
title: InviteGuestError
excerpt: OpenDOOR iOS SDK 2.1.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)



## Declaration

```swift
public enum InviteGuestError : String, OpenDOORSDKError {
  case emailRequired
  case emailOrPhoneRequired
  case emailAndPhoneProvided
  case invalidPhone
  case invalidStartTime
  case endTimeNotSupported
  case userCanNotShare
  public init?(rawValue: String)
  public typealias RawValue = String
  public var rawValue: String {
    get
  }
}

extension InviteGuestError {
  public var description: String {
    get
  }
}

extension InviteGuestError : Equatable {}

extension InviteGuestError : Hashable {}

extension InviteGuestError : RawRepresentable {}
```

## description

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

## InviteGuestError.emailAndPhoneProvided

```swift
case emailAndPhoneProvided
```

Both an email and phone was provided for the temporary guest.

## InviteGuestError.emailOrPhoneRequired

```swift
case emailOrPhoneRequired
```

An email or phone is required for the temporary guest.

## InviteGuestError.emailRequired

```swift
case emailRequired
```

An email is required for the permanent guest.

## InviteGuestError.endTimeNotSupported

```swift
case endTimeNotSupported
```

The end time is prior to the start time or too far in the future.

## init(rawValue:)

```swift
init?(rawValue: String)
```

Inherited from `RawRepresentable.init(rawValue:)`.

## InviteGuestError.invalidPhone

```swift
case invalidPhone
```

An invalid phone was provided.

## InviteGuestError.invalidStartTime

```swift
case invalidStartTime
```

The start time is either in the past or too far in the future.

## InviteGuestError.userCanNotShare

```swift
case userCanNotShare
```

The user does not have sharable access to the devices provided.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

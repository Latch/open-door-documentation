---
title: InviteGuestError
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Guest invitation business-rule failure.

## Declaration

```swift
public enum InviteGuestError : Swift::String, OpenDOORCore::OpenDOORSDKError {
  case emailRequired
  case emailOrPhoneRequired
  case emailAndPhoneProvided
  case invalidPhone
  case invalidStartTime
  case endTimeNotSupported
  case userCanNotShare
  case shareableAccessRequired
  case sharingNotEnabled
  case requestedTimeOutsideShareableAccess
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

## InviteGuestError.emailAndPhoneProvided

```swift
case emailAndPhoneProvided
```

Both an email and phone were provided for the temporary guest.

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

## InviteGuestError.requestedTimeOutsideShareableAccess

```swift
case requestedTimeOutsideShareableAccess
```

The requested guest window falls outside the user’s own shareable access window.

## InviteGuestError.shareableAccessRequired

```swift
case shareableAccessRequired
```

The user holds no active shareable access to this lock.

## InviteGuestError.sharingNotEnabled

```swift
case sharingNotEnabled
```

The access exists but was granted without sharing enabled.

## InviteGuestError.userCanNotShare

```swift
case userCanNotShare
```

The user may not share access at all.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

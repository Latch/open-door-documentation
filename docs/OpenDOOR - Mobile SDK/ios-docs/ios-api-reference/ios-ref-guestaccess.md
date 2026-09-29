---
title: GuestAccess
excerpt: OpenDOOR iOS SDK 2.3.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Access granted to a guest on a specific lock.

## Declaration

```swift
public struct GuestAccess : Equatable {
  public let lockID: UUID
  public let lockName: String
  public let inviteType: any InviteType
  public let passcodeType: PasscodeType
  public let startTime: Date
  public let endTime: Date?
  public init(lockID: UUID, lockName: String, inviteType: any InviteType, passcodeType: PasscodeType, startTime: Date, endTime: Date?)
}

extension GuestAccess {
  public static func == (lhs: GuestAccess, rhs: GuestAccess) -> Bool
}
```

## ==(_:_:)

```swift
static func == (lhs: GuestAccess, rhs: GuestAccess) -> Bool
```

Inherited from `Equatable.==(_:_:)`.

## endTime

```swift
let endTime: Date?
```

End of the allowed window, or nil.

## init(lockID:lockName:inviteType:passcodeType:startTime:endTime:)

```swift
init(lockID: UUID, lockName: String, inviteType: any InviteType, passcodeType: PasscodeType, startTime: Date, endTime: Date?)
```

## inviteType

```swift
let inviteType: any InviteType
```

Invite type for this access.

## lockID

```swift
let lockID: UUID
```

Target lock ID

## lockName

```swift
let lockName: String
```

Target lock name

## passcodeType

```swift
let passcodeType: PasscodeType
```

Credential type granted.

## startTime

```swift
let startTime: Date
```

Start of the allowed window.

## Related types

[InviteType](doc:ios-ref-invitetype) · [PasscodeType](doc:ios-ref-passcodetype)

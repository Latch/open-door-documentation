---
title: GuestAccess
excerpt: OpenDOOR iOS SDK 2.3.1 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Access granted to a guest on a specific lock.

## Declaration

```swift
public struct GuestAccess : Swift::Equatable {
  public let lockID: Foundation::UUID
  public let lockName: Swift::String
  public let inviteType: any OpenDOORCore::InviteType
  public let passcodeType: OpenDOORCore::PasscodeType
  public let startTime: Foundation::Date
  public let endTime: Foundation::Date?
  public init(lockID: Foundation::UUID, lockName: Swift::String, inviteType: any OpenDOORCore::InviteType, passcodeType: OpenDOORCore::PasscodeType, startTime: Foundation::Date, endTime: Foundation::Date?)
}
```

## endTime

```swift
let endTime: Date?
```

End of the allowed window.

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

Target lock ID.

## lockName

```swift
let lockName: String
```

Target lock name.

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

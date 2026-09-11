---
title: GuestAccess
excerpt: OpenDOOR iOS SDK 2.1.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

Access granted to a guest on a specific lock

## Declaration

```swift
public struct GuestAccess : Equatable {
  public var lockID: UUID
  public var lockName: String
  public var startTime: Date
  public var inviteType: any InviteType
  public init(lockID: UUID, lockName: String, startTime: Date, inviteType: any InviteType)
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

## init(lockID:lockName:startTime:inviteType:)

```swift
init(lockID: UUID, lockName: String, startTime: Date, inviteType: any InviteType)
```

## lockID

```swift
var lockID: UUID
```

Target lock ID

## lockName

```swift
var lockName: String
```

Target lock name

## startTime

```swift
var startTime: Date
```

Start of the allowed window.

## Related types

[InviteType](doc:ios-ref-invitetype)

---
title: TemporaryDoorcodeInvite
excerpt: OpenDOOR iOS SDK 2.2.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Invite type for temporary doorcode invite type.

## Declaration

```swift
public struct TemporaryDoorcodeInvite : InviteType {
  public var accessType: AccessType?
  public var duration: Duration
  public var period: Period
  public init(accessType: AccessType?, duration: Duration, period: Period)
}

extension TemporaryDoorcodeInvite : Equatable {
  public static func == (a: TemporaryDoorcodeInvite, b: TemporaryDoorcodeInvite) -> Bool
}
```

## accessType

```swift
var accessType: AccessType?
```

Inherited from `InviteType.accessType`.

## init(accessType:duration:period:)

```swift
init(accessType: AccessType?, duration: Duration, period: Period)
```

## Related types

[AccessType](doc:ios-ref-accesstype) · [Duration](doc:ios-ref-duration) · [InviteType](doc:ios-ref-invitetype) · [Period](doc:ios-ref-period)

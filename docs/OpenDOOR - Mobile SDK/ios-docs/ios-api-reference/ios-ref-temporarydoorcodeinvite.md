---
title: TemporaryDoorcodeInvite
excerpt: OpenDOOR iOS SDK 2.1.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

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

The type of access granted to the guest (e.g., enter or reach).

## init(accessType:duration:period:)

```swift
init(accessType: AccessType?, duration: Duration, period: Period)
```

## Related types

[AccessType](doc:ios-ref-accesstype) · [Duration](doc:ios-ref-duration) · [InviteType](doc:ios-ref-invitetype) · [Period](doc:ios-ref-period)

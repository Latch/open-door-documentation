---
title: InAppInvite
excerpt: OpenDOOR iOS SDK 2.2.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Invite type for in-app access with time-based restrictions.

## Declaration

```swift
public struct InAppInvite : InviteType {
  public var accessType: AccessType?
  public var startTime: Date
  public var endTime: Date?
  public var showDoorcodes: Bool?
  public init(accessType: AccessType?, startTime: Date, endTime: Date? = nil, showDoorcodes: Bool?)
}

extension InAppInvite : Equatable {
  public static func == (a: InAppInvite, b: InAppInvite) -> Bool
}
```

## accessType

```swift
var accessType: AccessType?
```

Inherited from `InviteType.accessType`.

## init(accessType:startTime:endTime:showDoorcodes:)

```swift
init(accessType: AccessType?, startTime: Date, endTime: Date? = nil, showDoorcodes: Bool?)
```

## Related types

[AccessType](doc:ios-ref-accesstype) · [InviteType](doc:ios-ref-invitetype)

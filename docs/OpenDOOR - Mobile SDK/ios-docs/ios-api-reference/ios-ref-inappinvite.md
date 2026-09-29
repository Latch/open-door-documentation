---
title: InAppInvite
excerpt: OpenDOOR iOS SDK 2.3.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

In-app access with time-based restrictions.

## Declaration

```swift
public struct InAppInvite : InviteType, Equatable {
  public let startTime: Date
  public let endTime: Date?
  public init(startTime: Date, endTime: Date?)
  public static func == (a: InAppInvite, b: InAppInvite) -> Bool
}
```

## init(startTime:endTime:)

```swift
init(startTime: Date, endTime: Date?)
```

## Related types

[InviteType](doc:ios-ref-invitetype)

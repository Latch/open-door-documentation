---
title: InAppInvite
excerpt: OpenDOOR iOS SDK 2.3.1 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

In-app access with time-based restrictions.

## Declaration

```swift
public struct InAppInvite : OpenDOORCore::InviteType, Swift::Equatable {
  public let startTime: Foundation::Date
  public let endTime: Foundation::Date?
  public init(startTime: Foundation::Date, endTime: Foundation::Date?)
  public static func == (a: OpenDOORCore::InAppInvite, b: OpenDOORCore::InAppInvite) -> Swift::Bool
}
```

## endTime

```swift
let endTime: Date?
```

End time of the requested access. If not set, access is permanent until revoked.

## init(startTime:endTime:)

```swift
init(startTime: Date, endTime: Date?)
```

## startTime

```swift
let startTime: Date
```

Start time of the requested access.

## Related types

[InviteType](doc:ios-ref-invitetype)

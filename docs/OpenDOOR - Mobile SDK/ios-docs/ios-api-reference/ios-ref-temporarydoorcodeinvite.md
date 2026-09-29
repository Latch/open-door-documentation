---
title: TemporaryDoorcodeInvite
excerpt: OpenDOOR iOS SDK 2.3.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Temporary doorcode access.

## Declaration

```swift
public struct TemporaryDoorcodeInvite : InviteType, Equatable {
  public let duration: Duration
  public let period: Period
  public init(duration: Duration, period: Period)
  public static func == (a: TemporaryDoorcodeInvite, b: TemporaryDoorcodeInvite) -> Bool
}
```

## init(duration:period:)

```swift
init(duration: Duration, period: Period)
```

## Related types

[Duration](doc:ios-ref-duration) · [InviteType](doc:ios-ref-invitetype) · [Period](doc:ios-ref-period)

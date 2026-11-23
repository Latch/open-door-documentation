---
title: TemporaryDoorcodeInvite
excerpt: OpenDOOR iOS SDK 2.3.1 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Temporary doorcode access.

## Declaration

```swift
public struct TemporaryDoorcodeInvite : OpenDOORCore::InviteType, Swift::Equatable {
  public let duration: OpenDOORCore::Duration
  public let period: OpenDOORCore::Period
  public init(duration: OpenDOORCore::Duration, period: OpenDOORCore::Period)
  public static func == (a: OpenDOORCore::TemporaryDoorcodeInvite, b: OpenDOORCore::TemporaryDoorcodeInvite) -> Swift::Bool
}
```

## duration

```swift
let duration: Duration
```

How long the doorcode works on the chosen day: all day, or until 15 minutes after its first use.

## init(duration:period:)

```swift
init(duration: Duration, period: Period)
```

## period

```swift
let period: Period
```

Period when the access is valid: today or tomorrow.

## Related types

[Duration](doc:ios-ref-duration) · [InviteType](doc:ios-ref-invitetype) · [Period](doc:ios-ref-period)

---
title: InviteType
excerpt: OpenDOOR iOS SDK 2.2.0 protocol reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Invite types that define how a guest will receive access.

## Declaration

```swift
public protocol InviteType {
  var accessType: AccessType? { get set }
}
```

## accessType

```swift
var accessType: AccessType? { get set }
```

The type of access granted to the guest (e.g., enter or reach).

## Related types

[AccessType](doc:ios-ref-accesstype)

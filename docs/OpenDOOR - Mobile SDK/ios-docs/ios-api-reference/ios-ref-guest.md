---
title: Guest
excerpt: OpenDOOR iOS SDK 2.3.1 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Person with shared access to one or more locks.

## Declaration

```swift
public struct Guest : Swift::Equatable {
  public let id: Foundation::UUID
  public let firstName: Swift::String
  public let lastName: Swift::String?
  public let email: Swift::String?
  public let phone: Swift::String?
  public let guestAccesses: [OpenDOORCore::GuestAccess]
  public init(id: Foundation::UUID, firstName: Swift::String, lastName: Swift::String?, email: Swift::String?, phone: Swift::String?, guestAccesses: [OpenDOORCore::GuestAccess])
  public static func == (a: OpenDOORCore::Guest, b: OpenDOORCore::Guest) -> Swift::Bool
}
```

## email

```swift
let email: String?
```

Guest’s email address.

## firstName

```swift
let firstName: String
```

Guest’s first name.

## guestAccesses

```swift
let guestAccesses: [GuestAccess]
```

Lock-specific access entries.

## id

```swift
let id: UUID
```

Unique guest identifier.

## init(id:firstName:lastName:email:phone:guestAccesses:)

```swift
init(id: UUID, firstName: String, lastName: String?, email: String?, phone: String?, guestAccesses: [GuestAccess])
```

## lastName

```swift
let lastName: String?
```

Guest’s last name.

## phone

```swift
let phone: String?
```

Guest’s phone number.

## Related types

[GuestAccess](doc:ios-ref-guestaccess)

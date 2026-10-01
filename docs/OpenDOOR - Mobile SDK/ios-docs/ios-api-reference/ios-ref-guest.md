---
title: Guest
excerpt: OpenDOOR iOS SDK 2.3.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Person with shared access to one or more locks.

## Declaration

```swift
public struct Guest : Equatable {
  public let id: UUID
  public let firstName: String
  public let lastName: String?
  public let email: String?
  public let phone: String?
  public let guestAccesses: [GuestAccess]
  public init(id: UUID, firstName: String, lastName: String?, email: String?, phone: String?, guestAccesses: [GuestAccess])
  public static func == (a: Guest, b: Guest) -> Bool
}
```

## email

```swift
let email: String?
```

[Guest](doc:ios-ref-guest)’s email address

## firstName

```swift
let firstName: String
```

[Guest](doc:ios-ref-guest)’s first name

## guestAccesses

```swift
let guestAccesses: [GuestAccess]
```

[Lock](doc:ios-ref-lock)-specific access entries

## id

```swift
let id: UUID
```

Unique guest identifier

## init(id:firstName:lastName:email:phone:guestAccesses:)

```swift
init(id: UUID, firstName: String, lastName: String?, email: String?, phone: String?, guestAccesses: [GuestAccess])
```

## lastName

```swift
let lastName: String?
```

[Guest](doc:ios-ref-guest)’s last name

## phone

```swift
let phone: String?
```

[Guest](doc:ios-ref-guest)’s phone number

## Related types

[GuestAccess](doc:ios-ref-guestaccess)

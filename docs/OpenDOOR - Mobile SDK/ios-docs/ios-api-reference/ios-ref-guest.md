---
title: Guest
excerpt: OpenDOOR iOS SDK 2.2.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Person with shared access to one or more locks

## Declaration

```swift
public struct Guest : Equatable {
  public var id: UUID
  public var firstName: String
  public var lastName: String?
  public var email: String?
  public var phone: String?
  public var guestAccesses: [GuestAccess]
  public init(id: UUID, firstName: String, lastName: String?, email: String?, phone: String?, guestAccesses: [GuestAccess])
  public static func == (a: Guest, b: Guest) -> Bool
}
```

## email

```swift
var email: String?
```

[Guest](doc:ios-ref-guest)’s email address

## firstName

```swift
var firstName: String
```

[Guest](doc:ios-ref-guest)’s first name

## guestAccesses

```swift
var guestAccesses: [GuestAccess]
```

[Lock](doc:ios-ref-lock)-specific access entries

## id

```swift
var id: UUID
```

Unique guest identifier

## init(id:firstName:lastName:email:phone:guestAccesses:)

```swift
init(id: UUID, firstName: String, lastName: String?, email: String?, phone: String?, guestAccesses: [GuestAccess])
```

## lastName

```swift
var lastName: String?
```

[Guest](doc:ios-ref-guest)’s last name

## phone

```swift
var phone: String?
```

[Guest](doc:ios-ref-guest)’s phone number

## Related types

[GuestAccess](doc:ios-ref-guestaccess)

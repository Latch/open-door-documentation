---
title: Guest
excerpt: Person with shared access to one or more locks.
hidden: true
---

*Structure*

```swift
struct Guest
```

Person with shared access to one or more locks.

## Initializers

### `init(id:firstName:lastName:email:phone:guestAccesses:)`

```swift
init(id: UUID, firstName: String, lastName: String?, email: String?, phone: String?, guestAccesses: [GuestAccess])
```

## Instance Properties

### `email`

```swift
let email: String?
```

### `firstName`

```swift
let firstName: String
```

### `guestAccesses`

```swift
let guestAccesses: [GuestAccess]
```

### `id`

```swift
let id: UUID
```

### `lastName`

```swift
let lastName: String?
```

### `phone`

```swift
let phone: String?
```

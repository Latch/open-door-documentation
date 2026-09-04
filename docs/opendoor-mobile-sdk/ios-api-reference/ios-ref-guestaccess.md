---
title: GuestAccess
excerpt: Access granted to a guest on a specific lock.
hidden: true
---

*Structure*

```swift
struct GuestAccess
```

Access granted to a guest on a specific lock.

## Initializers

### `init(invitationID:lockID:lockName:inviteType:passcodeType:startTime:endTime:)`

```swift
init(invitationID: UUID?, lockID: UUID, lockName: String, inviteType: any InviteType, passcodeType: PasscodeType, startTime: Date, endTime: Date?)
```

## Instance Properties

### `endTime`

```swift
let endTime: Date?
```

### `invitationID`

```swift
let invitationID: UUID?
```

### `inviteType`

```swift
let inviteType: any InviteType
```

### `lockID`

```swift
let lockID: UUID
```

### `lockName`

```swift
let lockName: String
```

### `passcodeType`

```swift
let passcodeType: PasscodeType
```

### `startTime`

```swift
let startTime: Date
```

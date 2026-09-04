---
title: AccessLog
excerpt: Record of an access attempt on a lock.
hidden: true
---

*Structure*

```swift
struct AccessLog
```

Record of an access attempt on a lock.

## Initializers

### `init(id:epochTimeForEntryAttempt:imageFileName:imageToken:guestUUID:fullName:method:result:lockUUID:photoAvailability:userFirstName:userLastName:userNickname:)`

```swift
init(id: UUID, epochTimeForEntryAttempt: Int64, imageFileName: String?, imageToken: String?, guestUUID: UUID?, fullName: String?, method: AccessLogMethod, result: AccessLogResult, lockUUID: UUID?, photoAvailability: String?, userFirstName: String?, userLastName: String?, userNickname: String?)
```

## Instance Properties

### `epochTimeForEntryAttempt`

```swift
let epochTimeForEntryAttempt: Int64
```

Attempt timestamp in epoch milliseconds.

### `fullName`

```swift
let fullName: String?
```

### `guestUUID`

```swift
let guestUUID: UUID?
```

### `id`

```swift
let id: UUID
```

Unique log identifier.

### `imageFileName`

```swift
let imageFileName: String?
```

### `imageToken`

```swift
let imageToken: String?
```

### `lockUUID`

```swift
let lockUUID: UUID?
```

### `method`

```swift
let method: AccessLogMethod
```

### `photoAvailability`

```swift
let photoAvailability: String?
```

### `result`

```swift
let result: AccessLogResult
```

### `userFirstName`

```swift
let userFirstName: String?
```

### `userLastName`

```swift
let userLastName: String?
```

### `userNickname`

```swift
let userNickname: String?
```

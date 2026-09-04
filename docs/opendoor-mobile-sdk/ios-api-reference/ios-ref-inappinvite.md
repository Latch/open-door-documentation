---
title: InAppInvite
excerpt: In-app access with time-based restrictions.
hidden: true
---

*Structure*

```swift
struct InAppInvite
```

In-app access with time-based restrictions.

## Initializers

### `init(accessType:startTime:endTime:showDoorcodes:)`

```swift
init(accessType: AccessType?, startTime: Date, endTime: Date?, showDoorcodes: Bool?)
```

## Instance Properties

### `accessType`

```swift
let accessType: AccessType?
```

Inherited from `InviteType.accessType`.

### `endTime`

```swift
let endTime: Date?
```

### `showDoorcodes`

```swift
let showDoorcodes: Bool?
```

### `startTime`

```swift
let startTime: Date
```

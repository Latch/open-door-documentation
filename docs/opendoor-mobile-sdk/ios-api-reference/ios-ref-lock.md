---
title: Lock
excerpt: User-visible lock information.
hidden: true
---

*Structure*

```swift
struct Lock
```

User-visible lock information.

## Initializers

### `init(id:name:buildingID:startTime:endTime:doorCode:isShareable:)`

```swift
init(id: UUID, name: String, buildingID: UUID, startTime: Date, endTime: Date?, doorCode: String?, isShareable: Bool)
```

## Instance Properties

### `buildingID`

```swift
let buildingID: UUID
```

### `doorCode`

```swift
let doorCode: String?
```

### `endTime`

```swift
let endTime: Date?
```

### `id`

```swift
let id: UUID
```

### `isShareable`

```swift
let isShareable: Bool
```

### `name`

```swift
let name: String
```

### `startTime`

```swift
let startTime: Date
```

---
title: Lock
excerpt: OpenDOOR iOS SDK 2.3.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

User-visible lock information.

## Declaration

```swift
public struct Lock : Equatable {
  public let id: UUID
  public let name: String
  public let buildingID: UUID
  public let startTime: Date
  public let endTime: Date?
  public let doorCode: String?
  public let isShareable: Bool
  public init(id: UUID, name: String, buildingID: UUID, startTime: Date, endTime: Date?, doorCode: String?, isShareable: Bool)
  public static func == (a: Lock, b: Lock) -> Bool
}
```

## buildingID

```swift
let buildingID: UUID
```

Building identifier

## doorCode

```swift
let doorCode: String?
```

Door access code if available

## endTime

```swift
let endTime: Date?
```

End of access window

## id

```swift
let id: UUID
```

Unique lock identifier

## init(id:name:buildingID:startTime:endTime:doorCode:isShareable:)

```swift
init(id: UUID, name: String, buildingID: UUID, startTime: Date, endTime: Date?, doorCode: String?, isShareable: Bool)
```

## isShareable

```swift
let isShareable: Bool
```

Indicates whether this lock can be shared with guests

## name

```swift
let name: String
```

Human-readable lock name

## startTime

```swift
let startTime: Date
```

Start of access window

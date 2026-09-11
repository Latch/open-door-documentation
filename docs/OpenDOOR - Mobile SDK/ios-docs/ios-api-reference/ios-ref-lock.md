---
title: Lock
excerpt: OpenDOOR iOS SDK 2.1.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

User-visible lock information

## Declaration

```swift
public struct Lock : Equatable {
  public var id: UUID
  public var name: String
  public var buildingID: UUID
  public var isShareable: Bool
  public var startTime: Date
  public var endTime: Date?
  public var doorCode: String?
  public init(id: UUID, name: String, buildingID: UUID, isShareable: Bool, startTime: Date, endTime: Date?, doorCode: String?)
  public static func == (a: Lock, b: Lock) -> Bool
}
```

## buildingID

```swift
var buildingID: UUID
```

Building identifier

## doorCode

```swift
var doorCode: String?
```

Door access code if available

## endTime

```swift
var endTime: Date?
```

End of access window

## id

```swift
var id: UUID
```

Unique lock identifier

## init(id:name:buildingID:isShareable:startTime:endTime:doorCode:)

```swift
init(id: UUID, name: String, buildingID: UUID, isShareable: Bool, startTime: Date, endTime: Date?, doorCode: String?)
```

## isShareable

```swift
var isShareable: Bool
```

Indicates whether this lock can be shared with guests

## name

```swift
var name: String
```

Human-readable lock name

## startTime

```swift
var startTime: Date
```

Start of access window

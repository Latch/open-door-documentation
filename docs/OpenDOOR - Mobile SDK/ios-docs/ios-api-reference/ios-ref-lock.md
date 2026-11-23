---
title: Lock
excerpt: OpenDOOR iOS SDK 2.3.1 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

User-visible lock information.

## Declaration

```swift
public struct Lock : Swift::Equatable {
  public let id: Foundation::UUID
  public let name: Swift::String
  public let buildingID: Foundation::UUID
  public let startTime: Foundation::Date
  public let endTime: Foundation::Date?
  public let doorCode: Swift::String?
  public let isShareable: Swift::Bool
  public let timeZone: Swift::String
  public let remoteUnlockMethods: [OpenDOORCore::RemoteUnlockMethod]
  public init(id: Foundation::UUID, name: Swift::String, buildingID: Foundation::UUID, startTime: Foundation::Date, endTime: Foundation::Date?, doorCode: Swift::String?, isShareable: Swift::Bool, timeZone: Swift::String, remoteUnlockMethods: [OpenDOORCore::RemoteUnlockMethod])
  public static func == (a: OpenDOORCore::Lock, b: OpenDOORCore::Lock) -> Swift::Bool
}
```

## buildingID

```swift
let buildingID: UUID
```

Building identifier.

## doorCode

```swift
let doorCode: String?
```

Door access code, if available.

## endTime

```swift
let endTime: Date?
```

End of access window.

## id

```swift
let id: UUID
```

Unique lock identifier.

## init(id:name:buildingID:startTime:endTime:doorCode:isShareable:timeZone:remoteUnlockMethods:)

```swift
init(id: UUID, name: String, buildingID: UUID, startTime: Date, endTime: Date?, doorCode: String?, isShareable: Bool, timeZone: String, remoteUnlockMethods: [RemoteUnlockMethod])
```

## isShareable

```swift
let isShareable: Bool
```

Indicates whether this lock can be shared with guests.

## name

```swift
let name: String
```

Human-readable lock name.

## remoteUnlockMethods

```swift
let remoteUnlockMethods: [RemoteUnlockMethod]
```

Remote unlock methods the lock supports. Empty when it supports none.

## startTime

```swift
let startTime: Date
```

Start of access window.

## timeZone

```swift
let timeZone: String
```

IANA timezone of the lock, such as Europe/Rome. The phone’s timezone when the lock has none.

## Related types

[RemoteUnlockMethod](doc:ios-ref-remoteunlockmethod)

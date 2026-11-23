---
title: AccessLog
excerpt: OpenDOOR iOS SDK 2.3.1 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Record of an access attempt on a lock.

## Declaration

```swift
public struct AccessLog : Swift::Equatable {
  public let id: Foundation::UUID
  public let epochTimeForEntryAttempt: Swift::Int64
  public let imageFileName: Swift::String?
  public let imageToken: Swift::String?
  public let guestUUID: Foundation::UUID?
  public let fullName: Swift::String?
  public let method: OpenDOORCore::AccessLogMethod
  public let result: OpenDOORCore::AccessLogResult
  public let lockUUID: Foundation::UUID?
  public let photoAvailability: Swift::String?
  public let userFirstName: Swift::String?
  public let userLastName: Swift::String?
  public let userNickname: Swift::String?
  public init(id: Foundation::UUID, epochTimeForEntryAttempt: Swift::Int64, imageFileName: Swift::String?, imageToken: Swift::String?, guestUUID: Foundation::UUID?, fullName: Swift::String?, method: OpenDOORCore::AccessLogMethod, result: OpenDOORCore::AccessLogResult, lockUUID: Foundation::UUID?, photoAvailability: Swift::String?, userFirstName: Swift::String?, userLastName: Swift::String?, userNickname: Swift::String?)
  public static func == (a: OpenDOORCore::AccessLog, b: OpenDOORCore::AccessLog) -> Swift::Bool
}
```

## epochTimeForEntryAttempt

```swift
let epochTimeForEntryAttempt: Int64
```

Attempt timestamp in epoch seconds.

## fullName

```swift
let fullName: String?
```

Full name of the person who attempted access.

## guestUUID

```swift
let guestUUID: UUID?
```

Guest UUID, if applicable.

## id

```swift
let id: UUID
```

Unique log identifier.

## imageFileName

```swift
let imageFileName: String?
```

Image file name, if available.

## imageToken

```swift
let imageToken: String?
```

Image token, if available.

## init(id:epochTimeForEntryAttempt:imageFileName:imageToken:guestUUID:fullName:method:result:lockUUID:photoAvailability:userFirstName:userLastName:userNickname:)

```swift
init(id: UUID, epochTimeForEntryAttempt: Int64, imageFileName: String?, imageToken: String?, guestUUID: UUID?, fullName: String?, method: AccessLogMethod, result: AccessLogResult, lockUUID: UUID?, photoAvailability: String?, userFirstName: String?, userLastName: String?, userNickname: String?)
```

## lockUUID

```swift
let lockUUID: UUID?
```

Lock UUID for the access attempt.

## method

```swift
let method: AccessLogMethod
```

Method used to attempt entry.

## photoAvailability

```swift
let photoAvailability: String?
```

Photo availability status.

## result

```swift
let result: AccessLogResult
```

Outcome of the attempt.

## userFirstName

```swift
let userFirstName: String?
```

First name of the user.

## userLastName

```swift
let userLastName: String?
```

Last name of the user.

## userNickname

```swift
let userNickname: String?
```

Nickname of the user.

## Related types

[AccessLogMethod](doc:ios-ref-accesslogmethod) · [AccessLogResult](doc:ios-ref-accesslogresult)

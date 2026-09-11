---
title: AccessLog
excerpt: OpenDOOR iOS SDK 2.2.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Record of an access attempt on a lock

## Declaration

```swift
public struct AccessLog : Equatable {
  public var id: UUID
  public var epochTimeForEntryAttempt: Int64
  public var imageFileName: String?
  public var imageToken: String?
  public var guestUUID: UUID?
  public var fullName: String?
  public var method: AccessLogMethod
  public var result: AccessLogResult
  public var lockUUID: UUID?
  public var photoAvailability: String?
  public var userFirstName: String?
  public var userLastName: String?
  public var userNickname: String?
  public init(id: UUID, epochTimeForEntryAttempt: Int64, imageFileName: String?, imageToken: String?, guestUUID: UUID?, fullName: String?, method: AccessLogMethod, result: AccessLogResult, lockUUID: UUID?, photoAvailability: String?, userFirstName: String?, userLastName: String?, userNickname: String?)
  public static func == (a: AccessLog, b: AccessLog) -> Bool
}
```

## epochTimeForEntryAttempt

```swift
var epochTimeForEntryAttempt: Int64
```

Timestamp recorded for the entry attempt.

## fullName

```swift
var fullName: String?
```

Full name of the person who attempted access

## guestUUID

```swift
var guestUUID: UUID?
```

[Guest](doc:ios-ref-guest) UUID if applicable

## id

```swift
var id: UUID
```

Unique log identifier

## imageFileName

```swift
var imageFileName: String?
```

Image file name if available

## imageToken

```swift
var imageToken: String?
```

Image token if available

## init(id:epochTimeForEntryAttempt:imageFileName:imageToken:guestUUID:fullName:method:result:lockUUID:photoAvailability:userFirstName:userLastName:userNickname:)

```swift
init(id: UUID, epochTimeForEntryAttempt: Int64, imageFileName: String?, imageToken: String?, guestUUID: UUID?, fullName: String?, method: AccessLogMethod, result: AccessLogResult, lockUUID: UUID?, photoAvailability: String?, userFirstName: String?, userLastName: String?, userNickname: String?)
```

## lockUUID

```swift
var lockUUID: UUID?
```

[Lock](doc:ios-ref-lock) UUID for the access attempt

## method

```swift
var method: AccessLogMethod
```

Method used to attempt entry

## photoAvailability

```swift
var photoAvailability: String?
```

Photo availability status

## result

```swift
var result: AccessLogResult
```

Outcome of the attempt

## userFirstName

```swift
var userFirstName: String?
```

First name of the user

## userLastName

```swift
var userLastName: String?
```

Last name of the user

## userNickname

```swift
var userNickname: String?
```

Nickname of the user

## Related types

[AccessLogMethod](doc:ios-ref-accesslogmethod) · [AccessLogResult](doc:ios-ref-accesslogresult)

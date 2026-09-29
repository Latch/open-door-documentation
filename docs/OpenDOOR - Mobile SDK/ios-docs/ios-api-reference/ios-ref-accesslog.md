---
title: AccessLog
excerpt: OpenDOOR iOS SDK 2.3.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Record of an access attempt on a lock.

## Declaration

```swift
public struct AccessLog : Equatable {
  public let id: UUID
  public let epochTimeForEntryAttempt: Int64
  public let imageFileName: String?
  public let imageToken: String?
  public let guestUUID: UUID?
  public let fullName: String?
  public let method: AccessLogMethod
  public let result: AccessLogResult
  public let lockUUID: UUID?
  public let photoAvailability: String?
  public let userFirstName: String?
  public let userLastName: String?
  public let userNickname: String?
  public init(id: UUID, epochTimeForEntryAttempt: Int64, imageFileName: String?, imageToken: String?, guestUUID: UUID?, fullName: String?, method: AccessLogMethod, result: AccessLogResult, lockUUID: UUID?, photoAvailability: String?, userFirstName: String?, userLastName: String?, userNickname: String?)
  public static func == (a: AccessLog, b: AccessLog) -> Bool
}
```

## epochTimeForEntryAttempt

```swift
let epochTimeForEntryAttempt: Int64
```

Attempt timestamp in epoch milliseconds.

## fullName

```swift
let fullName: String?
```

Full name of the person who attempted access

## guestUUID

```swift
let guestUUID: UUID?
```

[Guest](doc:ios-ref-guest) UUID if applicable

## id

```swift
let id: UUID
```

Unique log identifier.

## imageFileName

```swift
let imageFileName: String?
```

Image file name if available

## imageToken

```swift
let imageToken: String?
```

Image token if available

## init(id:epochTimeForEntryAttempt:imageFileName:imageToken:guestUUID:fullName:method:result:lockUUID:photoAvailability:userFirstName:userLastName:userNickname:)

```swift
init(id: UUID, epochTimeForEntryAttempt: Int64, imageFileName: String?, imageToken: String?, guestUUID: UUID?, fullName: String?, method: AccessLogMethod, result: AccessLogResult, lockUUID: UUID?, photoAvailability: String?, userFirstName: String?, userLastName: String?, userNickname: String?)
```

## lockUUID

```swift
let lockUUID: UUID?
```

[Lock](doc:ios-ref-lock) UUID for the access attempt

## method

```swift
let method: AccessLogMethod
```

Method used to attempt entry

## photoAvailability

```swift
let photoAvailability: String?
```

Photo availability status

## result

```swift
let result: AccessLogResult
```

Outcome of the attempt

## userFirstName

```swift
let userFirstName: String?
```

First name of the user

## userLastName

```swift
let userLastName: String?
```

Last name of the user

## userNickname

```swift
let userNickname: String?
```

Nickname of the user

## Related types

[AccessLogMethod](doc:ios-ref-accesslogmethod) · [AccessLogResult](doc:ios-ref-accesslogresult)

---
title: UnlockFailureError
excerpt: OpenDOOR iOS SDK 2.3.1 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Detail for an unlock failure.

## Declaration

```swift
public struct UnlockFailureError : Swift::Equatable, Swift::CustomStringConvertible {
  public let code: OpenDOORCore::UnlockFailureCode
  public let message: Swift::String
  public let context: Swift::String?
  public init(code: OpenDOORCore::UnlockFailureCode, message: Swift::String, context: Swift::String?)
  public static func == (a: OpenDOORCore::UnlockFailureError, b: OpenDOORCore::UnlockFailureError) -> Swift::Bool
}
```

## code

```swift
let code: UnlockFailureCode
```

Cause of the failure.

## context

```swift
let context: String?
```

Platform error code, such as a lock response code, a GATT status or an HTTP status.

## init(code:message:context:)

```swift
init(code: UnlockFailureCode, message: String, context: String?)
```

## message

```swift
let message: String
```

Human-readable description of the failure.

## Related types

[UnlockFailureCode](doc:ios-ref-unlockfailurecode)

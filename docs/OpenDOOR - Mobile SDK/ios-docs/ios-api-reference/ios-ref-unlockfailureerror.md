---
title: UnlockFailureError
excerpt: OpenDOOR iOS SDK 2.3.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Detail for an unlock failure.

## Declaration

```swift
public struct UnlockFailureError : Equatable, CustomStringConvertible {
  public let code: UnlockFailureCode
  public let message: String
  public let context: String?
  public init(code: UnlockFailureCode, message: String, context: String?)
  public static func == (a: UnlockFailureError, b: UnlockFailureError) -> Bool
}

extension UnlockFailureError {
  public var description: String {
    get
  }
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

Platform error code, such as a lock response code or a GATT status.

## description

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

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

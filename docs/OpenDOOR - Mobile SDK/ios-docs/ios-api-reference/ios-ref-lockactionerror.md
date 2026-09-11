---
title: LockActionError
excerpt: OpenDOOR iOS SDK 2.1.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

An error describing a failure while performing an action on a specific lock.

## Declaration

```swift
public struct LockActionError : OpenDOORSDKError {
  public let lockID: UUID
  public let error: any OpenDOORSDKError
  public init(lockID: UUID, error: any OpenDOORSDKError)
}

extension LockActionError {
  public var description: String {
    get
  }
}
```

## description

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

## error

```swift
let error: OpenDOORSDKError
```

The underlying error that caused the action to fail.

## init(lockID:error:)

```swift
init(lockID: UUID, error: OpenDOORSDKError)
```

## lockID

```swift
let lockID: UUID
```

The unique identifier of the lock on which the action failed.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

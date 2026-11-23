---
title: LockActionError
excerpt: OpenDOOR iOS SDK 2.3.1 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Failure while acting on one lock.

## Declaration

```swift
public struct LockActionError : OpenDOORCore::OpenDOORSDKError {
  public let lockID: Foundation::UUID
  public let error: any OpenDOORCore::OpenDOORSDKError
  public init(lockID: Foundation::UUID, error: any OpenDOORCore::OpenDOORSDKError)
  public var description: Swift::String {
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
let error: any OpenDOORSDKError
```

Underlying error that caused the action to fail.

## init(lockID:error:)

```swift
init(lockID: UUID, error: any OpenDOORSDKError)
```

## lockID

```swift
let lockID: UUID
```

Identifier of the lock on which the action failed.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

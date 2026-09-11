---
title: GuestInvitesError
excerpt: OpenDOOR iOS SDK 2.1.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

An error that represents a partial or complete failure when inviting a guest to multiple locks. Use this error to inspect which locks succeeded and which failed.

## Declaration

```swift
public struct GuestInvitesError : OpenDOORSDKError {
  public let failedLockErrors: [LockActionError]
  public let successfulLockIDs: [UUID]
  public var failedLockIDs: [UUID] {
    get
  }
}

extension GuestInvitesError {
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

## failedLockErrors

```swift
let failedLockErrors: [LockActionError]
```

Errors encountered for each lock that failed.

## failedLockIDs

```swift
var failedLockIDs: [UUID] { get }
```

Convenience accessor for the IDs of locks that failed.

## successfulLockIDs

```swift
let successfulLockIDs: [UUID]
```

IDs of locks where the guest invite succeeded.

## Related types

[LockActionError](doc:ios-ref-lockactionerror) · [OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

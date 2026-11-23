---
title: GuestInvitesError
excerpt: OpenDOOR iOS SDK 2.3.1 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Partial or complete guest-invitation failure.

## Declaration

```swift
public struct GuestInvitesError : OpenDOORCore::OpenDOORSDKError {
  public let failedLockErrors: [OpenDOORCore::LockActionError]
  public let successfulLockIDs: [Foundation::UUID]
  public var failedLockIDs: [Foundation::UUID] {
    get
  }
  public init(failedLockErrors: [OpenDOORCore::LockActionError], successfulLockIDs: [Foundation::UUID])
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

## failedLockErrors

```swift
let failedLockErrors: [LockActionError]
```

One error for each lock that failed.

## failedLockIDs

```swift
var failedLockIDs: [UUID] { get }
```

Identifiers of the locks that failed, taken from failedLockErrors.

## init(failedLockErrors:successfulLockIDs:)

```swift
init(failedLockErrors: [LockActionError], successfulLockIDs: [UUID])
```

## successfulLockIDs

```swift
let successfulLockIDs: [UUID]
```

Identifiers of the locks where the guest invite succeeded.

## Related types

[LockActionError](doc:ios-ref-lockactionerror) · [OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

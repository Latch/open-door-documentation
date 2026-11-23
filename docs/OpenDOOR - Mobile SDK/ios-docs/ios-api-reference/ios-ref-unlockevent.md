---
title: UnlockEvent
excerpt: OpenDOOR iOS SDK 2.3.1 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Event emitted during explicit, proximity and remote unlock operations.

## Declaration

```swift
public struct UnlockEvent : Swift::Equatable {
  public let lock: OpenDOORCore::Lock?
  public let method: OpenDOORCore::UnlockEventMethod
  public let status: OpenDOORCore::UnlockEventStatus
  public init(lock: OpenDOORCore::Lock?, method: OpenDOORCore::UnlockEventMethod, status: OpenDOORCore::UnlockEventStatus)
  public static func == (a: OpenDOORCore::UnlockEvent, b: OpenDOORCore::UnlockEvent) -> Swift::Bool
}
```

## init(lock:method:status:)

```swift
init(lock: Lock?, method: UnlockEventMethod, status: UnlockEventStatus)
```

## lock

```swift
let lock: Lock?
```

Lock the event relates to, if known. The SDK resolves the full lock from its own lock data, so consumers never have to supply or trust a caller-provided identifier.

## method

```swift
let method: UnlockEventMethod
```

Method used for this unlock attempt.

## status

```swift
let status: UnlockEventStatus
```

Current lifecycle status of the unlock operation.

## Related types

[Lock](doc:ios-ref-lock) · [UnlockEventMethod](doc:ios-ref-unlockeventmethod) · [UnlockEventStatus](doc:ios-ref-unlockeventstatus)

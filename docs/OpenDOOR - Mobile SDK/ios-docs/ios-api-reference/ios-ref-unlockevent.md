---
title: UnlockEvent
excerpt: OpenDOOR iOS SDK 2.3.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Event emitted during explicit and proximity unlock operations.

## Declaration

```swift
public struct UnlockEvent : Equatable {
  public let lock: Lock?
  public let method: UnlockEventMethod
  public let status: UnlockEventStatus
  public init(lock: Lock?, method: UnlockEventMethod, status: UnlockEventStatus)
  public static func == (a: UnlockEvent, b: UnlockEvent) -> Bool
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

[Lock](doc:ios-ref-lock) being unlocked

## method

```swift
let method: UnlockEventMethod
```

Method used for unlock

## status

```swift
let status: UnlockEventStatus
```

Status of the unlock operation

## Related types

[Lock](doc:ios-ref-lock) · [UnlockEventMethod](doc:ios-ref-unlockeventmethod) · [UnlockEventStatus](doc:ios-ref-unlockeventstatus)

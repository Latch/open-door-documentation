---
title: UnlockEvent
excerpt: OpenDOOR iOS SDK 2.2.0 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Events emitted while performing an unlock operation.

## Declaration

```swift
public struct UnlockEvent : Equatable {
  public var lock: Lock?
  public var status: UnlockEventStatus
  public var method: UnlockEventMethod
  public init(lock: Lock?, status: UnlockEventStatus, method: UnlockEventMethod)
  public static func == (a: UnlockEvent, b: UnlockEvent) -> Bool
}
```

## init(lock:status:method:)

```swift
init(lock: Lock?, status: UnlockEventStatus, method: UnlockEventMethod)
```

## lock

```swift
var lock: Lock?
```

[Lock](doc:ios-ref-lock) being unlocked

## method

```swift
var method: UnlockEventMethod
```

Method used for unlock

## status

```swift
var status: UnlockEventStatus
```

Status of the unlock operation

## Related types

[Lock](doc:ios-ref-lock) · [UnlockEventMethod](doc:ios-ref-unlockeventmethod) · [UnlockEventStatus](doc:ios-ref-unlockeventstatus)

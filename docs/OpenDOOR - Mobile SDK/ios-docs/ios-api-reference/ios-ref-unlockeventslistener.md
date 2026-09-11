---
title: UnlockEventsListener
excerpt: OpenDOOR iOS SDK 2.2.0 protocol reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Listener for unlock events

## Declaration

```swift
public protocol UnlockEventsListener : AnyObject {
  func onNewEvent(event: UnlockEvent)
}
```

## onNewEvent(event:)

```swift
func onNewEvent(event: UnlockEvent)
```

### Parameters


- `event`: New unlock event

## Related types

[UnlockEvent](doc:ios-ref-unlockevent)

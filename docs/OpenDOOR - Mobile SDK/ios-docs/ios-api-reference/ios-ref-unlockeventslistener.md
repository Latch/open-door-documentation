---
title: UnlockEventsListener
excerpt: OpenDOOR iOS SDK 2.3.1 protocol reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Listener for unlock lifecycle events.

## Declaration

```swift
public protocol UnlockEventsListener : AnyObject {
  func onNewEvent(event: OpenDOORCore::UnlockEvent)
}
```

## onNewEvent(event:)

```swift
func onNewEvent(event: UnlockEvent)
```

Called with each new unlock event.

### Parameters

- `event`: New unlock event.

## Related types

[UnlockEvent](doc:ios-ref-unlockevent)

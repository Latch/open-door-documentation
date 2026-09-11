---
title: LocksListener
excerpt: OpenDOOR iOS SDK 2.2.0 protocol reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Listener for lock list updates

## Declaration

```swift
public protocol LocksListener : AnyObject {
  func onUpdate(locks: [Lock])
}
```

## onUpdate(locks:)

```swift
func onUpdate(locks: [Lock])
```

### Parameters


- `locks`: Updated list of locks

## Related types

[Lock](doc:ios-ref-lock)

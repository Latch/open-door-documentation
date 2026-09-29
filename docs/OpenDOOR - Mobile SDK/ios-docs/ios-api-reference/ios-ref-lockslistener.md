---
title: LocksListener
excerpt: OpenDOOR iOS SDK 2.3.0 protocol reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Listener for update-only lock lists.

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

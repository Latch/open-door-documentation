---
title: UnlockEventMethod
excerpt: OpenDOOR iOS SDK 2.2.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Method used for unlock

## Declaration

```swift
public enum UnlockEventMethod : Equatable {
  case explicit
  case proximity
  public static func == (a: UnlockEventMethod, b: UnlockEventMethod) -> Bool
  public func hash(into hasher: inout Hasher)
  public var hashValue: Int {
    get
  }
}

extension UnlockEventMethod : Hashable {}
```

## UnlockEventMethod.explicit

```swift
case explicit
```

## UnlockEventMethod.proximity

```swift
case proximity
```

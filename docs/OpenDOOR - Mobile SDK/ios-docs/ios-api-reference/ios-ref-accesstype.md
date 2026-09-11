---
title: AccessType
excerpt: OpenDOOR iOS SDK 2.2.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Type of access granted to a guest.

## Declaration

```swift
public enum AccessType {
  case enter
  case reach
  public static func == (a: AccessType, b: AccessType) -> Bool
  public func hash(into hasher: inout Hasher)
  public var hashValue: Int {
    get
  }
}

extension AccessType : Equatable {}

extension AccessType : Hashable {}
```

## AccessType.enter

```swift
case enter
```

Enter access - allows guest to enter through the lock.

## AccessType.reach

```swift
case reach
```

Reach access - allows guest to reach the lock area.

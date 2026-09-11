---
title: Period
excerpt: OpenDOOR iOS SDK 2.1.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

[Period](doc:ios-ref-period) for temporary doorcode access.

## Declaration

```swift
public enum Period {
  case today
  case tomorrow
  public static func == (a: Period, b: Period) -> Bool
  public func hash(into hasher: inout Hasher)
  public var hashValue: Int {
    get
  }
}

extension Period : Equatable {}

extension Period : Hashable {}
```

## Period.today

```swift
case today
```

Access valid today.

## Period.tomorrow

```swift
case tomorrow
```

Access valid tomorrow.

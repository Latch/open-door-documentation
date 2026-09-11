---
title: Duration
excerpt: OpenDOOR iOS SDK 2.2.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

[Duration](doc:ios-ref-duration) for temporary doorcode access.

## Declaration

```swift
public enum Duration {
  case limit15Minutes
  case fullDay
  public static func == (a: Duration, b: Duration) -> Bool
  public func hash(into hasher: inout Hasher)
  public var hashValue: Int {
    get
  }
}

extension Duration : Equatable {}

extension Duration : Hashable {}
```

## Duration.fullDay

```swift
case fullDay
```

Access for the full day.

## Duration.limit15Minutes

```swift
case limit15Minutes
```

Access limited to 15 minutes.

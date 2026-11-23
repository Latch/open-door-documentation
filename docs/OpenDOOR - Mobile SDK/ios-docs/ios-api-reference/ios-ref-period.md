---
title: Period
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Period for temporary doorcode access.

## Declaration

```swift
public enum Period : Swift::Equatable {
  case today
  case tomorrow
  public static func == (a: OpenDOORCore::Period, b: OpenDOORCore::Period) -> Swift::Bool
  public func hash(into hasher: inout Swift::Hasher)
  public var hashValue: Swift::Int {
    get
  }
}
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

---
title: Duration
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Duration for temporary doorcode access.

## Declaration

```swift
public enum Duration : Swift::Equatable {
  case limit15Minutes
  case fullDay
  public static func == (a: OpenDOORCore::Duration, b: OpenDOORCore::Duration) -> Swift::Bool
  public func hash(into hasher: inout Swift::Hasher)
  public var hashValue: Swift::Int {
    get
  }
}
```

## Duration.fullDay

```swift
case fullDay
```

A doorcode that works for the whole chosen day.

## Duration.limit15Minutes

```swift
case limit15Minutes
```

A doorcode that works for the chosen day and expires 15 minutes after its first use.

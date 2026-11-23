---
title: UnlockAttempt
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Which pass through the unlock flow produced an event.

## Declaration

```swift
public enum UnlockAttempt : Swift::Equatable {
  case first
  case second
  public static func == (a: OpenDOORCore::UnlockAttempt, b: OpenDOORCore::UnlockAttempt) -> Swift::Bool
  public func hash(into hasher: inout Swift::Hasher)
  public var hashValue: Swift::Int {
    get
  }
}
```

## UnlockAttempt.first

```swift
case first
```

First attempt: an optional setup sync from cached data, then the unlock.

## UnlockAttempt.second

```swift
case second
```

Recovery attempt that runs after the first attempt fails: a setup sync when needed, then a second unlock.

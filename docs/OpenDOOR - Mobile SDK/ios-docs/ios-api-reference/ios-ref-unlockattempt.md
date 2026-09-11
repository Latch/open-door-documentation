---
title: UnlockAttempt
excerpt: OpenDOOR iOS SDK 2.2.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Identifies which attempt of a two-phase unlock flow produced an event.

## Declaration

```swift
public enum UnlockAttempt : Equatable {
  case first
  case second
  public static func == (a: UnlockAttempt, b: UnlockAttempt) -> Bool
  public func hash(into hasher: inout Hasher)
  public var hashValue: Int {
    get
  }
}

extension UnlockAttempt : Hashable {}
```

## UnlockAttempt.first

```swift
case first
```

First attempt.

## UnlockAttempt.second

```swift
case second
```

Recovery attempt that runs after the first attempt fails.

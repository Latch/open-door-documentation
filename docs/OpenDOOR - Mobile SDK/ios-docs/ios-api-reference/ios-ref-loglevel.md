---
title: LogLevel
excerpt: OpenDOOR iOS SDK 2.3.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Minimum SDK logging level.

## Declaration

```swift
public enum LogLevel : Equatable {
  case debug
  case info
  case warning
  case error
  public static func == (a: LogLevel, b: LogLevel) -> Bool
  public func hash(into hasher: inout Hasher)
  public var hashValue: Int {
    get
  }
}

extension LogLevel : Hashable {}
```

## LogLevel.debug

```swift
case debug
```

## LogLevel.error

```swift
case error
```

## LogLevel.info

```swift
case info
```

## LogLevel.warning

```swift
case warning
```

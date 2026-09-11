---
title: LogLevel
excerpt: OpenDOOR iOS SDK 2.1.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)



## Declaration

```swift
public enum LogLevel {
  case debug
  case error
  case info
  case warning
  public static func == (a: LogLevel, b: LogLevel) -> Bool
  public func hash(into hasher: inout Hasher)
  public var hashValue: Int {
    get
  }
}

extension LogLevel : Equatable {}

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

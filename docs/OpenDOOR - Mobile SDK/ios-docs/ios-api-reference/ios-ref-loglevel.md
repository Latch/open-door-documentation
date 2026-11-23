---
title: LogLevel
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Minimum SDK logging level.

## Declaration

```swift
public enum LogLevel : Swift::Equatable {
  case debug
  case info
  case warning
  case error
  public static func == (a: OpenDOORCore::LogLevel, b: OpenDOORCore::LogLevel) -> Swift::Bool
  public func hash(into hasher: inout Swift::Hasher)
  public var hashValue: Swift::Int {
    get
  }
}
```

## LogLevel.debug

```swift
case debug
```

Verbose logging suitable for development and adopters debugging integration issues.

## LogLevel.error

```swift
case error
```

Only errors are emitted.

## LogLevel.info

```swift
case info
```

Info messages, warnings and errors are emitted.

## LogLevel.warning

```swift
case warning
```

Warnings and errors are emitted.

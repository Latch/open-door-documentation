---
title: AccessLogResult
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Result of an access attempt.

## Declaration

```swift
public enum AccessLogResult : Swift::Equatable {
  case unknown
  case success
  case guestSuccess
  case lockSuccess
  case outsideQualifiedAccess
  case unknownTimeFailure
  case nfcFailure
  case deadboltApplied
  case incorrect
  public static func == (a: OpenDOORCore::AccessLogResult, b: OpenDOORCore::AccessLogResult) -> Swift::Bool
  public func hash(into hasher: inout Swift::Hasher)
  public var hashValue: Swift::Int {
    get
  }
}
```

## AccessLogResult.deadboltApplied

```swift
case deadboltApplied
```

Deadbolt was applied.

## AccessLogResult.guestSuccess

```swift
case guestSuccess
```

Guest access was successful.

## AccessLogResult.incorrect

```swift
case incorrect
```

Access was incorrect.

## AccessLogResult.lockSuccess

```swift
case lockSuccess
```

Lock action was successful.

## AccessLogResult.nfcFailure

```swift
case nfcFailure
```

NFC attempt failed.

## AccessLogResult.outsideQualifiedAccess

```swift
case outsideQualifiedAccess
```

Access was outside the allowed schedule.

## AccessLogResult.success

```swift
case success
```

Access was successful.

## AccessLogResult.unknown

```swift
case unknown
```

Unknown access result.

## AccessLogResult.unknownTimeFailure

```swift
case unknownTimeFailure
```

Access failed due to unknown time.

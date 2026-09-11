---
title: AccessLogResult
excerpt: OpenDOOR iOS SDK 2.1.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

Result of an access attempt

## Declaration

```swift
public enum AccessLogResult {
  case success
  case lockSuccess
  case guestSuccess
  case outsideQualifiedAccess
  case unknownTimeFailure
  case nfcFailure
  case incorrect
  case deadboltApplied
  case unknown
  public static func == (a: AccessLogResult, b: AccessLogResult) -> Bool
  public func hash(into hasher: inout Hasher)
  public var hashValue: Int {
    get
  }
}

extension AccessLogResult : Equatable {}

extension AccessLogResult : Hashable {}
```

## AccessLogResult.deadboltApplied

```swift
case deadboltApplied
```

Deadbolt was applied

## AccessLogResult.guestSuccess

```swift
case guestSuccess
```

[Guest](doc:ios-ref-guest) access was successful

## AccessLogResult.incorrect

```swift
case incorrect
```

Access was incorrect

## AccessLogResult.lockSuccess

```swift
case lockSuccess
```

[Lock](doc:ios-ref-lock) was successful

## AccessLogResult.nfcFailure

```swift
case nfcFailure
```

NFC attempt failed

## AccessLogResult.outsideQualifiedAccess

```swift
case outsideQualifiedAccess
```

Access was out of schedule

## AccessLogResult.success

```swift
case success
```

Access was successful

## AccessLogResult.unknown

```swift
case unknown
```

Unknown access result

## AccessLogResult.unknownTimeFailure

```swift
case unknownTimeFailure
```

Access failed due to unknown time

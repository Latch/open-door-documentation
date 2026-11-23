---
title: PasscodeType
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Type of access credential granted to a guest.

## Declaration

```swift
public enum PasscodeType : Swift::Equatable {
  case permanent
  case daily
  case dailySingleUse
  public static func == (a: OpenDOORCore::PasscodeType, b: OpenDOORCore::PasscodeType) -> Swift::Bool
  public func hash(into hasher: inout Swift::Hasher)
  public var hashValue: Swift::Int {
    get
  }
}
```

## PasscodeType.daily

```swift
case daily
```

A doorcode that works for the entire calendar day in the lock’s timezone.

## PasscodeType.dailySingleUse

```swift
case dailySingleUse
```

A doorcode that works for the entire calendar day in the lock’s timezone, but expires 15 minutes after first use.

## PasscodeType.permanent

```swift
case permanent
```

Access through the partner app, using the OpenDOOR SDK.

---
title: PasscodeType
excerpt: OpenDOOR iOS SDK 2.3.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Type of access credential granted to a guest.

## Declaration

```swift
public enum PasscodeType : Equatable {
  case permanent
  case daily
  case dailySingleUse
  public static func == (a: PasscodeType, b: PasscodeType) -> Bool
  public func hash(into hasher: inout Hasher)
  public var hashValue: Int {
    get
  }
}

extension PasscodeType : Hashable {}
```

## PasscodeType.daily

```swift
case daily
```

A doorcode that works for the entire calendar day set to the timezone of the device.

## PasscodeType.dailySingleUse

```swift
case dailySingleUse
```

A doorcode that works for the entire calendar day set to the timezone of the device, but expires 15 minutes after first use.

## PasscodeType.permanent

```swift
case permanent
```

Access partner app via [OpenDOOR](doc:ios-ref-opendoor) SDK

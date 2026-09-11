---
title: PasscodeType
excerpt: OpenDOOR iOS SDK 2.2.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Type of access credential granted to a guest.

## Declaration

```swift
public enum PasscodeType : String, CaseIterable {
  case permanent
  case daily
  case dailySingleUse
  public init?(rawValue: String)
  public typealias AllCases = [PasscodeType]
  public typealias RawValue = String
  nonisolated public static var allCases: [PasscodeType] {
    get
  }
  public var rawValue: String {
    get
  }
}

extension PasscodeType : Equatable {}

extension PasscodeType : Hashable {}

extension PasscodeType : RawRepresentable {}
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

## init(rawValue:)

```swift
init?(rawValue: String)
```

Inherited from `RawRepresentable.init(rawValue:)`.

## PasscodeType.permanent

```swift
case permanent
```

Access partner app via [OpenDOOR](doc:ios-ref-opendoor) SDK

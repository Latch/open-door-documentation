---
title: IntercomContactPreference
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

How the user receives intercom calls.

## Declaration

```swift
public enum IntercomContactPreference : Swift::Equatable {
  case app
  case phone
  case unit
  public static func == (a: OpenDOORCore::IntercomContactPreference, b: OpenDOORCore::IntercomContactPreference) -> Swift::Bool
  public func hash(into hasher: inout Swift::Hasher)
  public var hashValue: Swift::Int {
    get
  }
}
```

## IntercomContactPreference.app

```swift
case app
```

## IntercomContactPreference.phone

```swift
case phone
```

## IntercomContactPreference.unit

```swift
case unit
```

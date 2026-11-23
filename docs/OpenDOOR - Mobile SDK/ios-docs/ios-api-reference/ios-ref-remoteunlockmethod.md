---
title: RemoteUnlockMethod
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

How a door is unlocked remotely.

## Declaration

```swift
public enum RemoteUnlockMethod : Swift::Equatable {
  case intercom
  case doorScout
  public static func == (a: OpenDOORCore::RemoteUnlockMethod, b: OpenDOORCore::RemoteUnlockMethod) -> Swift::Bool
  public func hash(into hasher: inout Swift::Hasher)
  public var hashValue: Swift::Int {
    get
  }
}
```

## RemoteUnlockMethod.doorScout

```swift
case doorScout
```

Through a Door Scout near the door.

## RemoteUnlockMethod.intercom

```swift
case intercom
```

Through the door’s intercom.

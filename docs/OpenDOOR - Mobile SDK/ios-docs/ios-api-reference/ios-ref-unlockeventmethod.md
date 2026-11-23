---
title: UnlockEventMethod
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Method used for unlock.

## Declaration

```swift
public enum UnlockEventMethod : Swift::Equatable {
  case explicit
  case proximity
  case remoteIntercom
  case remoteDoorScout
  public static func == (a: OpenDOORCore::UnlockEventMethod, b: OpenDOORCore::UnlockEventMethod) -> Swift::Bool
  public func hash(into hasher: inout Swift::Hasher)
  public var hashValue: Swift::Int {
    get
  }
}
```

## UnlockEventMethod.explicit

```swift
case explicit
```

Unlock started explicitly by calling unlock.

## UnlockEventMethod.proximity

```swift
case proximity
```

Unlock started by proximity unlock.

## UnlockEventMethod.remoteDoorScout

```swift
case remoteDoorScout
```

Remote unlock through a Door Scout.

## UnlockEventMethod.remoteIntercom

```swift
case remoteIntercom
```

Remote unlock through the door’s intercom.

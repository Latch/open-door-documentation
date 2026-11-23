---
title: UnlockError
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Explicit unlock request failure before an attempt starts.

## Declaration

```swift
public enum UnlockError : OpenDOORCore::OpenDOORSDKError {
  case lockNotFound(Swift::String)
  case remoteUnlockNotSupported(Swift::String)
}
```

## UnlockError.lockNotFound(_:)

```swift
case lockNotFound(String)
```

Lock not found before unlock starts.

## UnlockError.remoteUnlockNotSupported(_:)

```swift
case remoteUnlockNotSupported(String)
```

The lock does not support the requested remote unlock method.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

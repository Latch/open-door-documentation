---
title: UnlockError
excerpt: OpenDOOR iOS SDK 2.3.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Explicit unlock request failure before an attempt starts.

## Declaration

```swift
public enum UnlockError : OpenDOORSDKError {
  case lockNotFound(String)
}

extension UnlockError {
  public var description: String {
    get
  }
}
```

## description

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

## UnlockError.lockNotFound(_:)

```swift
case lockNotFound(String)
```

[Lock](doc:ios-ref-lock) not found before unlock starts.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

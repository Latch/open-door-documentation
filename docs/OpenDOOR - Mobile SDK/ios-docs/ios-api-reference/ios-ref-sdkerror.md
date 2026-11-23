---
title: SDKError
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

General SDK access failure.

## Declaration

```swift
public enum SDKError : OpenDOORCore::OpenDOORSDKError {
  case sdkNotInitialized
  case sdkInternalError(Swift::String)
}
```

## SDKError.sdkInternalError(_:)

```swift
case sdkInternalError(String)
```

An internal SDK error occurred.

## SDKError.sdkNotInitialized

```swift
case sdkNotInitialized
```

The SDK has not been initialized with setupWithToken.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

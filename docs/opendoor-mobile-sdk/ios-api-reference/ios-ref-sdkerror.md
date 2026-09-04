---
title: SDKError
excerpt: General SDK access failure.
hidden: true
---

*Enumeration*

```swift
enum SDKError
```

General SDK access failure.

## Enumeration Cases

### `SDKError.sdkInternalError(_:)`

```swift
case sdkInternalError(String)
```

An internal SDK error occurred.

### `SDKError.sdkNotInitialized`

```swift
case sdkNotInitialized
```

The SDK has not been initialized with setupWithToken.

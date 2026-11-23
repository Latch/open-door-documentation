---
title: OpenDOORSDKError
excerpt: OpenDOOR iOS SDK 2.3.1 protocol reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Common protocol for errors exposed by the OpenDOOR SDK.

### Overview

Types conforming to `OpenDOORSDKError` must provide a human-readable description via `CustomStringConvertible`.

Conforming to this protocol ensures:

- `localizedDescription` returns a meaningful, user-facing message
- Error messaging behavior is consistent across the OpenDOOR SDK

This protocol is intended for errors defined by the OpenDOOR SDK. Consumers should only adopt it if they want the same behavior for their own errors.

## Declaration

```swift
public protocol OpenDOORSDKError : Foundation::LocalizedError, Swift::CustomStringConvertible {
}
```

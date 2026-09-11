---
title: OpenDOORSDKError
excerpt: OpenDOOR iOS SDK 2.1.0 protocol reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.1.0** (`OpenDOORCore`)

A protocol that defines user-presentable errors produced by the [OpenDOOR](doc:ios-ref-opendoor) SDK.

### Overview

Types conforming to `OpenDOORSDKError` must provide a human-readable description via `CustomStringConvertible`.

Conforming to this protocol ensures:

- `localizedDescription` returns a meaningful, user-facing message
- Error messaging behavior is consistent across the [OpenDOOR](doc:ios-ref-opendoor) SDK

This protocol is intended for errors defined by the [OpenDOOR](doc:ios-ref-opendoor) SDK. Consumers should only adopt it if they want the same behavior for their own errors.

## Declaration

```swift
public protocol OpenDOORSDKError : LocalizedError, CustomStringConvertible {
}

extension OpenDOORSDKError {
  public var errorDescription: String? {
    get
  }
}
```

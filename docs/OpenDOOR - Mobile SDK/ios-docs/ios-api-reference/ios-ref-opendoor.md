---
title: OpenDOOR
excerpt: Enumeration OpenDOOR
hidden: true
---

*Enumeration*

```swift
enum OpenDOOR
```

## Type Methods

### `getInstance()`

```swift
static func getInstance() async -> DOORClient
```

Returns the shared, lazily initialized client.

### `getInstance(internalSettings:)`

```swift
static func getInstance(internalSettings: [String : Any]) async -> DOORClient
```

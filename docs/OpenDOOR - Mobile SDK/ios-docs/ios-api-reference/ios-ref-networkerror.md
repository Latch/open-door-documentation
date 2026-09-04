---
title: NetworkError
excerpt: Network access failure.
hidden: true
---

*Enumeration*

```swift
enum NetworkError
```

Network access failure.

## Enumeration Cases

### `NetworkError.internalNetworkError(_:)`

```swift
case internalNetworkError(String)
```

Internal network error.

### `NetworkError.invalidToken`

```swift
case invalidToken
```

The supplied token is invalid or expired.

### `NetworkError.payloadError(_:)`

```swift
case payloadError(String)
```

Backend payload error.

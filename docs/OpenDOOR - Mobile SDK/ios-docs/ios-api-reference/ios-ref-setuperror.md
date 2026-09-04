---
title: SetupError
excerpt: Setup failure.
hidden: true
---

*Enumeration*

```swift
enum SetupError
```

Setup failure.

## Enumeration Cases

### `SetupError.consentNotGranted`

```swift
case consentNotGranted
```

User consent was not granted.

### `SetupError.invalidToken`

```swift
case invalidToken
```

The supplied token is invalid or expired.

### `SetupError.setupInternalError(_:)`

```swift
case setupInternalError(String)
```

An internal setup error occurred.

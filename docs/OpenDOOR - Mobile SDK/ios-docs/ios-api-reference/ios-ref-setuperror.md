---
title: SetupError
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Setup failure.

## Declaration

```swift
public enum SetupError : OpenDOORCore::OpenDOORSDKError {
  case invalidToken
  case consentNotGranted
  case setupInternalError(Swift::String)
}
```

## SetupError.consentNotGranted

```swift
case consentNotGranted
```

User consent was not granted.

## SetupError.invalidToken

```swift
case invalidToken
```

The supplied token is invalid or expired.

## SetupError.setupInternalError(_:)

```swift
case setupInternalError(String)
```

An internal setup error occurred.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

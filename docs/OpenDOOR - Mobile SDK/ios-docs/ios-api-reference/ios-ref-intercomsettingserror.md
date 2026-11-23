---
title: IntercomSettingsError
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Intercom settings failure.

## Declaration

```swift
public enum IntercomSettingsError : OpenDOORCore::OpenDOORSDKError {
  case noPhoneNumber
  public static func == (a: OpenDOORCore::IntercomSettingsError, b: OpenDOORCore::IntercomSettingsError) -> Swift::Bool
  public func hash(into hasher: inout Swift::Hasher)
  public var hashValue: Swift::Int {
    get
  }
}
```

## IntercomSettingsError.noPhoneNumber

```swift
case noPhoneNumber
```

The user has no phone number on file.

## Related types

[OpenDOORSDKError](doc:ios-ref-opendoorsdkerror)

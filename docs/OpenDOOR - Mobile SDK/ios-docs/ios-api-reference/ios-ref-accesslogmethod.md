---
title: AccessLogMethod
excerpt: OpenDOOR iOS SDK 2.2.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.2.0** (`OpenDOORCore`)

Method used during the access attempt

## Declaration

```swift
public enum AccessLogMethod {
  case mko
  case ble
  case passcode
  case nfc
  case androidNFC
  case desfire
  case scheduledLock
  case scheduledUnlock
  case mechanical
  case tapToLock
  case bleLock
  case unknown
  public static func == (a: AccessLogMethod, b: AccessLogMethod) -> Bool
  public func hash(into hasher: inout Hasher)
  public var hashValue: Int {
    get
  }
}

extension AccessLogMethod : Equatable {}

extension AccessLogMethod : Hashable {}
```

## AccessLogMethod.androidNFC

```swift
case androidNFC
```

NFC unlock

## AccessLogMethod.ble

```swift
case ble
```

Smartphone unlock

## AccessLogMethod.bleLock

```swift
case bleLock
```

Smartphone lock

## AccessLogMethod.desfire

```swift
case desfire
```

Keycard unlock

## AccessLogMethod.mechanical

```swift
case mechanical
```

Physical key

## AccessLogMethod.mko

```swift
case mko
```

Physical key

## AccessLogMethod.nfc

```swift
case nfc
```

Keycard unlock

## AccessLogMethod.passcode

```swift
case passcode
```

Doorcode unlock

## AccessLogMethod.scheduledLock

```swift
case scheduledLock
```

Scheduled lock

## AccessLogMethod.scheduledUnlock

```swift
case scheduledUnlock
```

Scheduled unlock

## AccessLogMethod.tapToLock

```swift
case tapToLock
```

Tap to lock

## AccessLogMethod.unknown

```swift
case unknown
```

Unknown method

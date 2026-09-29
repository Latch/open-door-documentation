---
title: AccessLogMethod
excerpt: OpenDOOR iOS SDK 2.3.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Method used during an access attempt.

## Declaration

```swift
public enum AccessLogMethod : Equatable {
  case unknown
  case nfc
  case passcode
  case ble
  case mko
  case desfire
  case scheduledLock
  case scheduledUnlock
  case mechanicalLock
  case tapToLock
  case bleLock
  case androidNFC
  public static func == (a: AccessLogMethod, b: AccessLogMethod) -> Bool
  public func hash(into hasher: inout Hasher)
  public var hashValue: Int {
    get
  }
}

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

## AccessLogMethod.mechanicalLock

```swift
case mechanicalLock
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

---
title: AccessLogMethod
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Method used during an access attempt.

## Declaration

```swift
public enum AccessLogMethod : Swift::Equatable {
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
  public static func == (a: OpenDOORCore::AccessLogMethod, b: OpenDOORCore::AccessLogMethod) -> Swift::Bool
  public func hash(into hasher: inout Swift::Hasher)
  public var hashValue: Swift::Int {
    get
  }
}
```

## AccessLogMethod.androidNFC

```swift
case androidNFC
```

NFC unlock from an Android phone.

## AccessLogMethod.ble

```swift
case ble
```

Smartphone unlock over Bluetooth.

## AccessLogMethod.bleLock

```swift
case bleLock
```

Smartphone lock over Bluetooth.

## AccessLogMethod.desfire

```swift
case desfire
```

Keycard unlock with a DESFire card.

## AccessLogMethod.mechanicalLock

```swift
case mechanicalLock
```

Mechanical lock.

## AccessLogMethod.mko

```swift
case mko
```

Physical key unlock.

## AccessLogMethod.nfc

```swift
case nfc
```

Keycard unlock over NFC.

## AccessLogMethod.passcode

```swift
case passcode
```

Doorcode unlock.

## AccessLogMethod.scheduledLock

```swift
case scheduledLock
```

Scheduled lock.

## AccessLogMethod.scheduledUnlock

```swift
case scheduledUnlock
```

Scheduled unlock.

## AccessLogMethod.tapToLock

```swift
case tapToLock
```

Tap to lock.

## AccessLogMethod.unknown

```swift
case unknown
```

Unknown method.

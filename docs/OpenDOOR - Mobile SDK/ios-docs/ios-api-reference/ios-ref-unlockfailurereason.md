---
title: UnlockFailureReason
excerpt: OpenDOOR iOS SDK 2.3.0 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.0** (`OpenDOORCore`)

Canonical reason an in-flight unlock failed.

## Declaration

```swift
public enum UnlockFailureReason : Equatable, CustomStringConvertible {
  case bluetoothDisabled
  case outOfSchedule
  case lockNotFound
  case connectionFailed
  case authFailed(UnlockFailureError)
  case `internal`(UnlockFailureError)
  public static func == (a: UnlockFailureReason, b: UnlockFailureReason) -> Bool
}

extension UnlockFailureReason {
  public var description: String {
    get
  }
}
```

## UnlockFailureReason.authFailed(_:)

```swift
case authFailed(UnlockFailureError)
```

The lock rejected the credential, or recovery sync failed. The payload carries the cause.

## UnlockFailureReason.bluetoothDisabled

```swift
case bluetoothDisabled
```

Bluetooth is turned off on the device.

## UnlockFailureReason.connectionFailed

```swift
case connectionFailed
```

The lock was discovered but a connection could not be established.

## description

```swift
var description: String { get }
```

Inherited from `CustomStringConvertible.description`.

## UnlockFailureReason.internal(_:)

```swift
case `internal`(UnlockFailureError)
```

A failure with no more specific reason. The payload carries the cause.

## UnlockFailureReason.lockNotFound

```swift
case lockNotFound
```

No lock matching the requested identifier was discovered.

## UnlockFailureReason.outOfSchedule

```swift
case outOfSchedule
```

Access was attempted outside the access schedule for the lock.

## Related types

[UnlockFailureError](doc:ios-ref-unlockfailureerror)

---
title: UnlockFailureReason
excerpt: OpenDOOR iOS SDK 2.3.1 enum reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Canonical reason an in-flight unlock failed.

## Declaration

```swift
public enum UnlockFailureReason : Swift::Equatable, Swift::CustomStringConvertible {
  case bluetoothDisabled
  case outOfSchedule
  case lockNotFound
  case connectionFailed
  case authFailed(OpenDOORCore::UnlockFailureError)
  case `internal`(OpenDOORCore::UnlockFailureError)
  case remoteUnlockNotAllowed
  public static func == (a: OpenDOORCore::UnlockFailureReason, b: OpenDOORCore::UnlockFailureReason) -> Swift::Bool
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

## UnlockFailureReason.remoteUnlockNotAllowed

```swift
case remoteUnlockNotAllowed
```

The user can’t unlock this door remotely.

## Related types

[UnlockFailureError](doc:ios-ref-unlockfailureerror)

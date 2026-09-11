---
title: AccessLogMethod
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Method used during the access attempt

## Declaration

```kotlin
enum class AccessLogMethod {

    UNKNOWN,

    NFC,

    PASSCODE,

    BLE,

    MKO,

    DESFIRE,

    SCHEDULED_LOCK,

    SCHEDULED_UNLOCK,

    MECHANICAL_LOCK,

    TAP_TO_LOCK,

    BLE_LOCK,

    ANDROID_NFC,
}
```

## UNKNOWN

Unknown method

## NFC

NFC Tag Unlock

## PASSCODE

Passcode Unlock for Guests

## BLE

Bluetooth Unlock

## MKO

Physical Key Unlock

## DESFIRE

Desfire

## SCHEDULED_LOCK

Scheduled Lock

## SCHEDULED_UNLOCK

Scheduled Unlock

## MECHANICAL_LOCK

Mechanical Lock

## TAP_TO_LOCK

Tap to Lock

## BLE_LOCK

BLE Lock

## ANDROID_NFC

Android NFC

## Related types

- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.model`.

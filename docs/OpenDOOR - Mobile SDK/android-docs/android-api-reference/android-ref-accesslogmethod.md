---
title: AccessLogMethod
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Method used during an access attempt.

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

Unknown method.

## NFC

Keycard unlock over NFC.

## PASSCODE

Doorcode unlock.

## BLE

Smartphone unlock over Bluetooth.

## MKO

Physical key unlock.

## DESFIRE

Keycard unlock with a DESFire card.

## SCHEDULED_LOCK

Scheduled lock.

## SCHEDULED_UNLOCK

Scheduled unlock.

## MECHANICAL_LOCK

Mechanical lock.

## TAP_TO_LOCK

Tap to lock.

## BLE_LOCK

Smartphone lock over Bluetooth.

## ANDROID_NFC

NFC unlock from an Android phone.

Package: `com.door.opendoor.android.core.api.model`.

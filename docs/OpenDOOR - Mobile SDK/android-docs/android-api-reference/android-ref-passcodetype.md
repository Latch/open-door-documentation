---
title: PasscodeType
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Type of access credential granted to a guest.

## Declaration

```kotlin
enum class PasscodeType {

    Permanent,

    Daily,

    DailySingleUse
}
```

## Permanent

Access partner app via OpenDOOR SDK

## Daily

A doorcode that works for the entire calendar day set to the timezone of the device.

## DailySingleUse

A doorcode that works for the entire calendar day set to the timezone of the device, but expires 15 minutes after first use.

## Related types

- [OpenDOOR](doc:android-ref-opendoor)

Package: `com.door.opendoor.android.core.api.model`.

---
title: PasscodeType
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Type of access credential granted to a guest.

## Declaration

```kotlin
enum class PasscodeType {

    Permanent,
    Daily,
    DailySingleUse,
}
```

## Permanent

Access through the partner app, using the OpenDOOR SDK.

## Daily

A doorcode that works for the entire calendar day in the lock's timezone.

## DailySingleUse

A doorcode that works for the entire calendar day in the lock's timezone, but expires 15 minutes after first use.

Package: `com.door.opendoor.android.core.api.model`.

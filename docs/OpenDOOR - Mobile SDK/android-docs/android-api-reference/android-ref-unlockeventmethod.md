---
title: UnlockEventMethod
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Method used for unlock.

## Declaration

```kotlin
enum class UnlockEventMethod {

    Explicit,
    Proximity,
    RemoteIntercom,
    RemoteDoorScout,
}
```

## Explicit

Unlock started explicitly by calling unlock.

## Proximity

Unlock started by proximity unlock.

## RemoteIntercom

Remote unlock through the door's intercom.

## RemoteDoorScout

Remote unlock through a Door Scout.

Package: `com.door.opendoor.android.core.api.model`.

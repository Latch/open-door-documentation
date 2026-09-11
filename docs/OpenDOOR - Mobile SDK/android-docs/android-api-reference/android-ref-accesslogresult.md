---
title: AccessLogResult
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Result of an access attempt

## Declaration

```kotlin
enum class AccessLogResult {

    UNKNOWN,

    SUCCESS,

    LOCK_SUCCESS,

    OUTSIDE_QUALIFIED_ACCESS,

    NFC_FAILURE,

    DEADBOLT_APPLIED,

    INCORRECT,
}
```

## UNKNOWN

Access result was unknown

## SUCCESS

Access was successful

## LOCK_SUCCESS

Lock was successful

## OUTSIDE_QUALIFIED_ACCESS

Access was outside qualified time

## NFC_FAILURE

NFC access failed

## DEADBOLT_APPLIED

Deadbolt was applied

## INCORRECT

Access was incorrect

## Related types

- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.model`.

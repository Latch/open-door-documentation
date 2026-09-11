---
title: AccessLogResult
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Result of an access attempt

## Declaration

```kotlin
enum class AccessLogResult {

    UNKNOWN,

    SUCCESS,

    GUEST_SUCCESS,

    LOCK_SUCCESS,

    OUTSIDE_QUALIFIED_ACCESS,

    UNKNOWN_TIME_FAILURE,

    NFC_FAILURE,

    DEADBOLT_APPLIED,

    INCORRECT,
}
```

## UNKNOWN

Access result was unknown

## SUCCESS

Access was successful

## GUEST_SUCCESS

Guest access was successful

## LOCK_SUCCESS

Lock was successful

## OUTSIDE_QUALIFIED_ACCESS

Access was outside qualified time

## UNKNOWN_TIME_FAILURE

Access failed due to unknown time

## NFC_FAILURE

NFC access failed

## DEADBOLT_APPLIED

Deadbolt was applied

## INCORRECT

Access was incorrect

## Related types

- [Guest](doc:android-ref-guest)
- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.model`.

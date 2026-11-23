---
title: AccessLogResult
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Result of an access attempt.

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

Unknown access result.

## SUCCESS

Access was successful.

## GUEST_SUCCESS

Guest access was successful.

## LOCK_SUCCESS

Lock action was successful.

## OUTSIDE_QUALIFIED_ACCESS

Access was outside the allowed schedule.

## UNKNOWN_TIME_FAILURE

Access failed due to unknown time.

## NFC_FAILURE

NFC attempt failed.

## DEADBOLT_APPLIED

Deadbolt was applied.

## INCORRECT

Access was incorrect.

Package: `com.door.opendoor.android.core.api.model`.

---
title: AccessLog
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Record of an access attempt on a lock

- **`uuid`** — Unique log identifier
- **`epochTimeForEntryAttempt`** — Timestamp of the attempt, as returned by the backend.
- **`imageFileName`** — Image file name if available
- **`imageToken`** — Image token if available
- **`guestUuid`** — Guest UUID if applicable
- **`fullName`** — Full name of the person who attempted access
- **`method`** — Method used to attempt entry
- **`result`** — Outcome of the attempt
- **`lockUuid`** — Lock UUID for the access attempt
- **`photoAvailability`** — Photo availability status
- **`userFirstName`** — First name of the user
- **`userLastName`** — Last name of the user
- **`userNickname`** — Nickname of the user

## Declaration

```kotlin
data class AccessLog(
    val uuid: UUID,
    val epochTimeForEntryAttempt: Long,
    val imageFileName: String?,
    val imageToken: String?,
    val guestUuid: UUID?,
    val fullName: String?,
    val method: AccessLogMethod,
    val result: AccessLogResult,
    val lockUuid: UUID?,
    val photoAvailability: String?,
    val userFirstName: String?,
    val userLastName: String?,
    val userNickname: String?,
)
```

## Related types

- [AccessLogMethod](doc:android-ref-accesslogmethod)
- [AccessLogResult](doc:android-ref-accesslogresult)
- [Guest](doc:android-ref-guest)
- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.model`.

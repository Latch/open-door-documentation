---
title: LockActionException
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Failure while acting on one lock.

## Declaration

```kotlin
class LockActionException(
    val lockId: UUID,
    val error: Exception,
    message: String = "Lock action failed for $lockId: ${error.message.orEmpty()}",
) : Exception(message, error)
```

## Related types

- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.exceptions`.

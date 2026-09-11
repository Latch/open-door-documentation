---
title: LockActionException
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Exception thrown when an action against a specific lock fails. Carries the lock UUID
and the underlying cause; the default message embeds both for easier diagnostics.

## Declaration

```kotlin
class LockActionException(
    val lockId: UUID,
    cause: Throwable,
    message: String = "Lock action failed for $lockId: ${cause.message.orEmpty()}",
) : Exception(message, cause)
```

## Related types

- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.exceptions`.

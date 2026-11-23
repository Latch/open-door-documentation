---
title: LockActionException
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Failure while acting on one lock.

- **`lockId`** — Identifier of the lock on which the action failed.
- **`error`** — Underlying error that caused the action to fail.

## Declaration

```kotlin
class LockActionException(
    val lockId: UUID,
    val error: Exception,
    message: String = "Lock action failed for ",
) : Exception
```

## Related types

- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.exceptions`.

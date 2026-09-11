---
title: LockActionException
excerpt: OpenDOOR Android SDK 2.1.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.1.1** (2.1 series).

Exception thrown when inviting a guest fails due to a known business rule.

## Declaration

```kotlin
class LockActionException(
    val lockId: UUID,
    cause: Throwable,
) : Exception(cause)
```

Package: `com.door.opendoor.android.core.api.exceptions`.

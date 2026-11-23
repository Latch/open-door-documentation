---
title: SyncException
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Active sync failure.

## Declaration

```kotlin
sealed class SyncException(message: String, throwable: Throwable? = null) : Exception {
    class CanceledException(message: String = "Sync was canceled", throwable: Throwable? = null) : SyncException
    class LockNotFoundException(val identifier: String, message: String = "Lock not found during sync: ", throwable: Throwable? = null) : SyncException
    class SyncInternalException(message: String, throwable: Throwable? = null) : SyncException
    class UnlockInProgressException(message: String = "An unlock is already in progress", throwable: Throwable? = null) : SyncException
}
```

## CanceledException

Sync was canceled.

## LockNotFoundException

Lock not found during sync.

## SyncInternalException

Internal sync error.

## UnlockInProgressException

An unlock is already in progress.

## Related types

- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.exceptions`.

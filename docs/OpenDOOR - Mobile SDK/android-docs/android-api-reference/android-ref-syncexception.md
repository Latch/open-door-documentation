---
title: SyncException
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Active sync failure.

## Declaration

```kotlin
sealed class SyncException(message: String, throwable: Throwable? = null) : Exception(message, throwable) {

    class LockNotFoundException(val identifier: String, message: String = "Lock not found during sync: $identifier", throwable: Throwable? = null) : SyncException(message, throwable)

    class CanceledException(message: String = "Sync was canceled", throwable: Throwable? = null) : SyncException(message, throwable)

    class UnlockInProgressException(message: String = "An unlock is already in progress", throwable: Throwable? = null) : SyncException(message, throwable)

    class SyncInternalException(message: String, throwable: Throwable? = null) : SyncException(message, throwable)
}
```

## LockNotFoundException

Lock not found during sync

## CanceledException

Sync operation was canceled

## UnlockInProgressException

Unlock operation is in progress

## SyncInternalException

An internal error occurred

## Related types

- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.exceptions`.

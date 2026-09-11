---
title: LocksListener
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Listener for lock list updates

## Declaration

```kotlin
interface LocksListener {

    fun onUpdate(locks: List<Lock>)

    fun onError(error: Throwable)
}
```

## onUpdate(locks)



- **`locks`** — Updated list of locks

## onError(error)

Called when an error occurs while listening for locks.

- **`error`** — The exception that occurred

## Related types

- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.listeners`.

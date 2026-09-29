---
title: LocksListener
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Listener for update-only lock lists.

## Declaration

```kotlin
interface LocksListener {

    fun onUpdate(locks: List<Lock>)
}
```

## onUpdate(locks)



- **`locks`** — Updated list of locks

## Related types

- [Lock](doc:android-ref-lock)

Package: `com.door.opendoor.android.core.api.listeners`.

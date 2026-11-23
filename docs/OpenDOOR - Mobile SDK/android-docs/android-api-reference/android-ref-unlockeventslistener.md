---
title: UnlockEventsListener
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Listener for unlock lifecycle events.

## Declaration

```kotlin
interface UnlockEventsListener {
    fun onNewEvent(event: UnlockEvent)
}
```

## onNewEvent(event)

Called with each new unlock event.

- **`event`** — New unlock event.

## Related types

- [UnlockEvent](doc:android-ref-unlockevent)

Package: `com.door.opendoor.android.core.api.listeners`.

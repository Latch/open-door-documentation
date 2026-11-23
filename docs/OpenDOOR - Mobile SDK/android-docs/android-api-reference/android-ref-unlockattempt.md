---
title: UnlockAttempt
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Which pass through the unlock flow produced an event.

## Declaration

```kotlin
enum class UnlockAttempt {

    First,
    Second,
}
```

## First

First attempt: an optional setup sync from cached data, then the unlock.

## Second

Recovery attempt that runs after the first attempt fails: a setup sync when needed, then a second unlock.

Package: `com.door.opendoor.android.core.api.model`.

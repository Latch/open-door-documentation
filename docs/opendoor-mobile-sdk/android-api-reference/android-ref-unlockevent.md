---
title: UnlockEvent
excerpt: Event emitted during explicit and proximity unlock operations.
hidden: true
---

*Package `com.door.opendoor.android.core.api.model`*

```kotlin
data class UnlockEvent(val lock: Lock?, val method: UnlockEventMethod, val status: UnlockEventStatus)
```

Event emitted during explicit and proximity unlock operations.

## Constructors

| | |
|---|---|
| UnlockEvent | constructor(lock: [Lock](doc:android-ref-lock)?, method: [UnlockEventMethod](doc:android-ref-unlockeventmethod), status: [UnlockEventStatus](doc:android-ref-unlockeventstatus)) |

## Properties

| Name | Summary |
|---|---|
| lock | val lock: [Lock](doc:android-ref-lock)? |
| method | val method: [UnlockEventMethod](doc:android-ref-unlockeventmethod) |
| status | val status: [UnlockEventStatus](doc:android-ref-unlockeventstatus) |

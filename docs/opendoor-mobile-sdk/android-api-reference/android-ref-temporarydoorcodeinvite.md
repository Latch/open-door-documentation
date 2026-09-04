---
title: TemporaryDoorcodeInvite
excerpt: Temporary doorcode access.
hidden: true
---

*Package `com.door.opendoor.android.core.api.model`*

```kotlin
data class TemporaryDoorcodeInvite(val accessType: AccessType?, val duration: Duration, val period: Period) : InviteType
```

Temporary doorcode access.

## Constructors

| | |
|---|---|
| TemporaryDoorcodeInvite | constructor(accessType: [AccessType](doc:android-ref-accesstype)?, duration: [Duration](doc:android-ref-duration), period: [Period](doc:android-ref-period)) |

## Properties

| Name | Summary |
|---|---|
| accessType | open override val accessType: [AccessType](doc:android-ref-accesstype)? |
| duration | val duration: [Duration](doc:android-ref-duration) |
| period | val period: [Period](doc:android-ref-period) |

---
title: Duration
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Duration for temporary doorcode access.

## Declaration

```kotlin
enum class Duration {

    Limit15Minutes,
    FullDay,
}
```

## Limit15Minutes

A doorcode that works for the chosen day and expires 15 minutes after its first use.

## FullDay

A doorcode that works for the whole chosen day.

Package: `com.door.opendoor.android.core.api.model`.

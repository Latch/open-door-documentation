---
title: LogLevel
excerpt: OpenDOOR Android SDK 2.3 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3** (2.3 release).

Minimum SDK logging level.

## Declaration

```kotlin
enum class LogLevel {

    DEBUG,

    INFO,

    WARNING,

    ERROR,
}
```

## DEBUG

Verbose logging suitable for development and adopters debugging integration issues.

## ERROR

Only errors are emitted; default for release builds.

## Related types

- [DoorClient](doc:android-ref-doorclient)

Package: `com.door.opendoor.android.core.api.model`.

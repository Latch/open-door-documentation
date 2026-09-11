---
title: LogLevel
excerpt: OpenDOOR Android SDK 2.2 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.2** (2.2 release).

Controls how much diagnostic information the SDK logs.

Higher levels (e.g. `DEBUG`) produce more detailed output; lower levels (e.g. `ERROR`)
restrict logs to important issues only. Adopters set this via [DoorClient.setLogLevel](doc:android-ref-doorclient).

## Declaration

```kotlin
enum class LogLevel {

    DEBUG,

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

---
title: IntercomSettings
excerpt: OpenDOOR Android SDK 2.3.1 API reference
hidden: false
---

[Android API Reference](doc:android-api-reference)

OpenDOOR Android SDK **2.3.1** (2.3.1 release).

Intercom call settings for one building.

- **`phoneNumber`** — Phone number used for intercom phone calls. Not set when the user has no phone number on file for this building; phone calls can't be enabled until one is added.

## Declaration

```kotlin
data class IntercomSettings(
    val buildingId: UUID,
    val contactPreference: IntercomContactPreference,
    val phoneNumber: String?,
)
```

## Related types

- [IntercomContactPreference](doc:android-ref-intercomcontactpreference)

Package: `com.door.opendoor.android.core.api.model`.

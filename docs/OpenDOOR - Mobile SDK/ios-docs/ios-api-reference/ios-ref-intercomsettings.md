---
title: IntercomSettings
excerpt: OpenDOOR iOS SDK 2.3.1 struct reference.
hidden: false
---

[iOS API Reference](doc:ios-api-reference) · OpenDOOR iOS SDK **2.3.1** (`OpenDOORCore`)

Intercom call settings for one building.

## Declaration

```swift
public struct IntercomSettings : Swift::Equatable {
  public let buildingID: Foundation::UUID
  public let contactPreference: OpenDOORCore::IntercomContactPreference
  public let phoneNumber: Swift::String?
  public init(buildingID: Foundation::UUID, contactPreference: OpenDOORCore::IntercomContactPreference, phoneNumber: Swift::String?)
  public static func == (a: OpenDOORCore::IntercomSettings, b: OpenDOORCore::IntercomSettings) -> Swift::Bool
}
```

## buildingID

```swift
let buildingID: UUID
```

## contactPreference

```swift
let contactPreference: IntercomContactPreference
```

## init(buildingID:contactPreference:phoneNumber:)

```swift
init(buildingID: UUID, contactPreference: IntercomContactPreference, phoneNumber: String?)
```

## phoneNumber

```swift
let phoneNumber: String?
```

Phone number used for intercom phone calls. Not set when the user has no phone number on file for this building; phone calls can’t be enabled until one is added.

## Related types

[IntercomContactPreference](doc:ios-ref-intercomcontactpreference)

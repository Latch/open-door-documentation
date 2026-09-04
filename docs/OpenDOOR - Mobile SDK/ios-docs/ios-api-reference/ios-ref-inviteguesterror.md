---
title: InviteGuestError
excerpt: Guest invitation business-rule failure.
hidden: true
---

*Enumeration*

```swift
enum InviteGuestError
```

Guest invitation business-rule failure.

## Enumeration Cases

### `InviteGuestError.emailAndPhoneProvided`

```swift
case emailAndPhoneProvided
```

Both an email and phone was provided for the temporary guest.

### `InviteGuestError.emailOrPhoneRequired`

```swift
case emailOrPhoneRequired
```

An email or phone is required for the temporary guest.

### `InviteGuestError.emailRequired`

```swift
case emailRequired
```

An email is required for the permanent guest.

### `InviteGuestError.endTimeNotSupported`

```swift
case endTimeNotSupported
```

The end time is prior to the start time or too far in the future.

### `InviteGuestError.invalidPhone`

```swift
case invalidPhone
```

An invalid phone was provided.

### `InviteGuestError.invalidStartTime`

```swift
case invalidStartTime
```

The start time is either in the past or too far in the future.

### `InviteGuestError.userCanNotShare`

```swift
case userCanNotShare
```

User does not have permission to share access. Make sure the access was granted by the partner and is shareable.

## Initializers

### `init(rawValue:)`

```swift
init?(rawValue: String)
```

Inherited from `RawRepresentable.init(rawValue:)`.

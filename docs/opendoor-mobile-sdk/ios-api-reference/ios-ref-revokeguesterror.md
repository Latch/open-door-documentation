---
title: RevokeGuestError
excerpt: Guest-access revocation failure.
hidden: true
---

*Enumeration*

```swift
enum RevokeGuestError
```

Guest-access revocation failure.

## Enumeration Cases

### `RevokeGuestError.deviceNotFound`

```swift
case deviceNotFound
```

Device was not found.

### `RevokeGuestError.internal(_:)`

```swift
case `internal`(String)
```

Internal revocation error.

### `RevokeGuestError.passcodeTypeCantBeRevoked`

```swift
case passcodeTypeCantBeRevoked
```

This passcode type cannot be revoked.

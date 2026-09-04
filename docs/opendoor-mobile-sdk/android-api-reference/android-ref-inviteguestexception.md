---
title: InviteGuestException
excerpt: Guest invitation business-rule failure.
hidden: true
---

*Package `com.door.opendoor.android.core.api.exceptions`*

```kotlin
class InviteGuestException(val reason: InviteGuestException.Reason, message: String = reason.message, cause: Throwable? = null) : Exception
```

Guest invitation business-rule failure.

## Constructors

| | |
|---|---|
| InviteGuestException | constructor(reason: InviteGuestException.Reason, message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = reason.message, cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) |

## Types

| Name | Summary |
|---|---|
| Reason | enum Reason : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)&lt;InviteGuestException.Reason&gt; |

## Properties

| Name | Summary |
|---|---|
| cause | open val cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| message | open val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |
| reason | val reason: InviteGuestException.Reason |

## `Reason`

```kotlin
enum Reason : Enum<InviteGuestException.Reason>
```

### Entries

| | |
|---|---|
| EMAIL_REQUIRED_FOR_PERMANENT | EMAIL_REQUIRED_FOR_PERMANENT |
| EMAIL_OR_PHONE_REQUIRED | EMAIL_OR_PHONE_REQUIRED |
| EMAIL_AND_PHONE_PROVIDED | EMAIL_AND_PHONE_PROVIDED |
| INVALID_PHONE | INVALID_PHONE |
| INVALID_START_TIME | INVALID_START_TIME |
| END_TIME_NOT_SUPPORTED | END_TIME_NOT_SUPPORTED |
| USER_CAN_NOT_SHARE | USER_CAN_NOT_SHARE |

### Properties

| Name | Summary |
|---|---|
| entries | val entries: [EnumEntries](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html)&lt;InviteGuestException.Reason&gt;<br>Returns a representation of an immutable list of all enum entries, in the order they're declared. |
| message | val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

### Functions

| Name | Summary |
|---|---|
| valueOf | fun valueOf(value: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): InviteGuestException.Reason<br>Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) |
| values | fun values(): [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)&lt;InviteGuestException.Reason&gt;<br>Returns an array containing the constants of this enum type, in the order they're declared. |

### Details

#### `entries`

```kotlin
val entries: EnumEntries<InviteGuestException.Reason>
```

Returns a representation of an immutable list of all enum entries, in the order they're declared.

This method may be used to iterate over the enum entries.

#### `valueOf`

```kotlin
fun valueOf(value: String): InviteGuestException.Reason
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

###### Throws

| | |
|---|---|
| [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html) | if this enum type has no constant with the specified name |

#### `values`

```kotlin
fun values(): Array<InviteGuestException.Reason>
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

### `EMAIL_AND_PHONE_PROVIDED`

EMAIL_AND_PHONE_PROVIDED

#### Properties

| Name | Summary |
|---|---|
| message | val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

### `EMAIL_OR_PHONE_REQUIRED`

EMAIL_OR_PHONE_REQUIRED

#### Properties

| Name | Summary |
|---|---|
| message | val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

### `EMAIL_REQUIRED_FOR_PERMANENT`

EMAIL_REQUIRED_FOR_PERMANENT

#### Properties

| Name | Summary |
|---|---|
| message | val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

### `END_TIME_NOT_SUPPORTED`

END_TIME_NOT_SUPPORTED

#### Properties

| Name | Summary |
|---|---|
| message | val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

### `INVALID_PHONE`

INVALID_PHONE

#### Properties

| Name | Summary |
|---|---|
| message | val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

### `INVALID_START_TIME`

INVALID_START_TIME

#### Properties

| Name | Summary |
|---|---|
| message | val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

### `USER_CAN_NOT_SHARE`

USER_CAN_NOT_SHARE

#### Properties

| Name | Summary |
|---|---|
| message | val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

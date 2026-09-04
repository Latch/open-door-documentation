---
title: AccessLogResult
excerpt: Result of an access attempt.
hidden: true
---

*Package `com.door.opendoor.android.core.api.model`*

```kotlin
enum AccessLogResult : Enum<AccessLogResult> 
```

Result of an access attempt.

## Entries

| | |
|---|---|
| UNKNOWN | UNKNOWN |
| SUCCESS | SUCCESS |
| GUEST_SUCCESS | GUEST_SUCCESS |
| LOCK_SUCCESS | LOCK_SUCCESS |
| OUTSIDE_QUALIFIED_ACCESS | OUTSIDE_QUALIFIED_ACCESS |
| UNKNOWN_TIME_FAILURE | UNKNOWN_TIME_FAILURE |
| NFC_FAILURE | NFC_FAILURE |
| DEADBOLT_APPLIED | DEADBOLT_APPLIED |
| INCORRECT | INCORRECT |

## Properties

| Name | Summary |
|---|---|
| entries | val entries: [EnumEntries](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html)&lt;AccessLogResult&gt;<br>Returns a representation of an immutable list of all enum entries, in the order they're declared. |
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## Functions

| Name | Summary |
|---|---|
| valueOf | fun valueOf(value: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): AccessLogResult<br>Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) |
| values | fun values(): [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)&lt;AccessLogResult&gt;<br>Returns an array containing the constants of this enum type, in the order they're declared. |

## Details

### `entries`

```kotlin
val entries: EnumEntries<AccessLogResult>
```

Returns a representation of an immutable list of all enum entries, in the order they're declared.

This method may be used to iterate over the enum entries.

### `valueOf`

```kotlin
fun valueOf(value: String): AccessLogResult
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

###### Throws

| | |
|---|---|
| [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html) | if this enum type has no constant with the specified name |

### `values`

```kotlin
fun values(): Array<AccessLogResult>
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

## `DEADBOLT_APPLIED`

DEADBOLT_APPLIED

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## `GUEST_SUCCESS`

GUEST_SUCCESS

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## `INCORRECT`

INCORRECT

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## `LOCK_SUCCESS`

LOCK_SUCCESS

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## `NFC_FAILURE`

NFC_FAILURE

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## `OUTSIDE_QUALIFIED_ACCESS`

OUTSIDE_QUALIFIED_ACCESS

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## `SUCCESS`

SUCCESS

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## `UNKNOWN`

UNKNOWN

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## `UNKNOWN_TIME_FAILURE`

UNKNOWN_TIME_FAILURE

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

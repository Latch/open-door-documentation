---
title: Duration
excerpt: Duration for temporary doorcode access.
hidden: true
---

*Package `com.door.opendoor.android.core.api.model`*

```kotlin
enum Duration : Enum<Duration> 
```

Duration for temporary doorcode access.

## Entries

| | |
|---|---|
| Limit15Minutes | Limit15Minutes |
| FullDay | FullDay |

## Properties

| Name | Summary |
|---|---|
| entries | val entries: [EnumEntries](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html)&lt;Duration&gt;<br>Returns a representation of an immutable list of all enum entries, in the order they're declared. |
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## Functions

| Name | Summary |
|---|---|
| valueOf | fun valueOf(value: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): Duration<br>Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) |
| values | fun values(): [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)&lt;Duration&gt;<br>Returns an array containing the constants of this enum type, in the order they're declared. |

## Details

### `entries`

```kotlin
val entries: EnumEntries<Duration>
```

Returns a representation of an immutable list of all enum entries, in the order they're declared.

This method may be used to iterate over the enum entries.

### `valueOf`

```kotlin
fun valueOf(value: String): Duration
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

###### Throws

| | |
|---|---|
| [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html) | if this enum type has no constant with the specified name |

### `values`

```kotlin
fun values(): Array<Duration>
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

## `FullDay`

FullDay

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## `Limit15Minutes`

Limit15Minutes

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

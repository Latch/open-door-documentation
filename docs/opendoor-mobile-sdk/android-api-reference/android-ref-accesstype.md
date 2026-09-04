---
title: AccessType
excerpt: Type of access granted to a guest.
hidden: true
---

*Package `com.door.opendoor.android.core.api.model`*

```kotlin
enum AccessType : Enum<AccessType> 
```

Type of access granted to a guest.

## Entries

| | |
|---|---|
| Enter | Enter |
| Reach | Reach |

## Properties

| Name | Summary |
|---|---|
| entries | val entries: [EnumEntries](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html)&lt;AccessType&gt;<br>Returns a representation of an immutable list of all enum entries, in the order they're declared. |
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## Functions

| Name | Summary |
|---|---|
| valueOf | fun valueOf(value: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): AccessType<br>Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) |
| values | fun values(): [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)&lt;AccessType&gt;<br>Returns an array containing the constants of this enum type, in the order they're declared. |

## Details

### `entries`

```kotlin
val entries: EnumEntries<AccessType>
```

Returns a representation of an immutable list of all enum entries, in the order they're declared.

This method may be used to iterate over the enum entries.

### `valueOf`

```kotlin
fun valueOf(value: String): AccessType
```

Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

###### Throws

| | |
|---|---|
| [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html) | if this enum type has no constant with the specified name |

### `values`

```kotlin
fun values(): Array<AccessType>
```

Returns an array containing the constants of this enum type, in the order they're declared.

This method may be used to iterate over the constants.

## `Enter`

Enter

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

## `Reach`

Reach

### Properties

| Name | Summary |
|---|---|
| name | val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| ordinal | val ordinal: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |

---
title: UnlockFailureReason
---
---
title: UnlockFailureReason
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.model](../index.html)/[UnlockFailureReason](index.html)



# UnlockFailureReason



[androidJvm]\
enum [UnlockFailureReason](index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)&lt;[UnlockFailureReason](index.html)&gt; 

Reasons why an unlock can fail



## Entries


| | |
|---|---|
| [BluetoothDisabled](-bluetooth-disabled/index.html) | [androidJvm]<br>[BluetoothDisabled](-bluetooth-disabled/index.html) |
| [BluetoothError](-bluetooth-error/index.html) | [androidJvm]<br>[BluetoothError](-bluetooth-error/index.html)<br>Bluetooth error occurred (e.g., GATT 133) |
| [LockNotFound](-lock-not-found/index.html) | [androidJvm]<br>[LockNotFound](-lock-not-found/index.html)<br>Failed to find a lock with a unique identifier matching the given lock ID. |
| [OutOfSchedule](-out-of-schedule/index.html) | [androidJvm]<br>[OutOfSchedule](-out-of-schedule/index.html)<br>Access attempted outside of device access schedule |
| [Timeout](-timeout/index.html) | [androidJvm]<br>[Timeout](-timeout/index.html)<br>Unlock failed to complete in a reasonable amount of time. |
| [InternalError](-internal-error/index.html) | [androidJvm]<br>[InternalError](-internal-error/index.html)<br>An internal error occurred |


## Properties


| Name | Summary |
|---|---|
| [entries](entries.html) | [androidJvm]<br>val [entries](entries.html): [EnumEntries](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html)&lt;[UnlockFailureReason](index.html)&gt;<br>Returns a representation of an immutable list of all enum entries, in the order they're declared. |
| [name](../../com.door.opendoor.android.model/-passcode-type/-daily-single-use/index.html#-372974862%2FProperties%2F-1404661416) | [androidJvm]<br>val [name](../../com.door.opendoor.android.model/-passcode-type/-daily-single-use/index.html#-372974862%2FProperties%2F-1404661416): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| [ordinal](../../com.door.opendoor.android.model/-passcode-type/-daily-single-use/index.html#-739389684%2FProperties%2F-1404661416) | [androidJvm]<br>val [ordinal](../../com.door.opendoor.android.model/-passcode-type/-daily-single-use/index.html#-739389684%2FProperties%2F-1404661416): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |


## Functions


| Name | Summary |
|---|---|
| [valueOf](value-of.html) | [androidJvm]<br>fun [valueOf](value-of.html)(value: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [UnlockFailureReason](index.html)<br>Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) |
| [values](values.html) | [androidJvm]<br>fun [values](values.html)(): [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)&lt;[UnlockFailureReason](index.html)&gt;<br>Returns an array containing the constants of this enum type, in the order they're declared. |

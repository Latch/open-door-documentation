---
title: PasscodeType
---
---
title: PasscodeType
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.model](../index.html)/[PasscodeType](index.html)



# PasscodeType



[androidJvm]\
enum [PasscodeType](index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)&lt;[PasscodeType](index.html)&gt; 

Type of access credential granted to a guest.



## Entries


| | |
|---|---|
| [Permanent](-permanent/index.html) | [androidJvm]<br>[Permanent](-permanent/index.html)<br>Access partner app via OpenDOOR SDK |
| [Daily](-daily/index.html) | [androidJvm]<br>[Daily](-daily/index.html)<br>A doorcode that works for the entire calendar day set to the timezone of the device. |
| [DailySingleUse](-daily-single-use/index.html) | [androidJvm]<br>[DailySingleUse](-daily-single-use/index.html)<br>A doorcode that works for the entire calendar day set to the timezone of the device, but expires 15 minutes after first use. |


## Properties


| Name | Summary |
|---|---|
| [entries](entries.html) | [androidJvm]<br>val [entries](entries.html): [EnumEntries](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html)&lt;[PasscodeType](index.html)&gt;<br>Returns a representation of an immutable list of all enum entries, in the order they're declared. |
| [name](../../com.door.opendoor.android.model/-passcode-type/-daily-single-use/index.html#-372974862%2FProperties%2F-1404661416) | [androidJvm]<br>val [name](../../com.door.opendoor.android.model/-passcode-type/-daily-single-use/index.html#-372974862%2FProperties%2F-1404661416): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) |
| [ordinal](../../com.door.opendoor.android.model/-passcode-type/-daily-single-use/index.html#-739389684%2FProperties%2F-1404661416) | [androidJvm]<br>val [ordinal](../../com.door.opendoor.android.model/-passcode-type/-daily-single-use/index.html#-739389684%2FProperties%2F-1404661416): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) |


## Functions


| Name | Summary |
|---|---|
| [valueOf](value-of.html) | [androidJvm]<br>fun [valueOf](value-of.html)(value: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [PasscodeType](index.html)<br>Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.) |
| [values](values.html) | [androidJvm]<br>fun [values](values.html)(): [Array](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html)&lt;[PasscodeType](index.html)&gt;<br>Returns an array containing the constants of this enum type, in the order they're declared. |

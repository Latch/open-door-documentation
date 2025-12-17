---
title: Guest
---
---
title: Guest
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.model](../index.html)/[Guest](index.html)



# Guest



[androidJvm]\
data class [Guest](index.html)(val id: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), val firstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val lastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val email: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val phone: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, val guestAccesses: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[GuestAccess](../-guest-access/index.html)&gt;)

Person with shared access to one or more locks



## Constructors


| | |
|---|---|
| [Guest](-guest.html) | [androidJvm]<br>constructor(id: [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html), firstName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), lastName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, email: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, phone: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?, guestAccesses: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[GuestAccess](../-guest-access/index.html)&gt;) |


## Properties


| Name | Summary |
|---|---|
| [email](email.html) | [androidJvm]<br>val [email](email.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?<br>Guest's email address |
| [firstName](first-name.html) | [androidJvm]<br>val [firstName](first-name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)<br>Guest's first name |
| [guestAccesses](guest-accesses.html) | [androidJvm]<br>val [guestAccesses](guest-accesses.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)&lt;[GuestAccess](../-guest-access/index.html)&gt;<br>Lock-specific access entries |
| [id](id.html) | [androidJvm]<br>val [id](id.html): [UUID](https://developer.android.com/reference/kotlin/java/util/UUID.html)<br>Unique guest identifier |
| [lastName](last-name.html) | [androidJvm]<br>val [lastName](last-name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?<br>Guest's last name |
| [phone](phone.html) | [androidJvm]<br>val [phone](phone.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?<br>Guest's phone number |

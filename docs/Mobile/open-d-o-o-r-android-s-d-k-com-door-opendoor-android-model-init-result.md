---
title: InitResult
---
---
title: InitResult
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.model](../index.html)/[InitResult](index.html)



# InitResult

sealed class [~~InitResult~~](index.html)---

### Deprecated



Use SetupResult instead



#### Replace with

```kotlin
import com.door.android.sdk.model.SetupResult

```
```kotlin
SetupResult
```
---


#### Inheritors


| |
|---|
| [Success](-success/index.html) |
| [InvalidToken](-invalid-token/index.html) |
| [PermissionDenied](-permission-denied/index.html) |
| [UserConsentDenied](-user-consent-denied/index.html) |
| [Error](-error/index.html) |


## Types


| Name | Summary |
|---|---|
| [Error](-error/index.html) | [androidJvm]<br>data class [Error](-error/index.html)(val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) : [InitResult](index.html) |
| [InvalidToken](-invalid-token/index.html) | [androidJvm]<br>object [InvalidToken](-invalid-token/index.html) : [InitResult](index.html) |
| [PermissionDenied](-permission-denied/index.html) | [androidJvm]<br>object [PermissionDenied](-permission-denied/index.html) : [InitResult](index.html) |
| [Success](-success/index.html) | [androidJvm]<br>object [Success](-success/index.html) : [InitResult](index.html) |
| [UserConsentDenied](-user-consent-denied/index.html) | [androidJvm]<br>object [UserConsentDenied](-user-consent-denied/index.html) : [InitResult](index.html) |

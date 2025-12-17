---
title: SetupResult
---
---
title: SetupResult
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.model](../index.html)/[SetupResult](index.html)



# SetupResult

sealed class [SetupResult](index.html)

Result class that signalizes the completion of the setup process of the Latch SDK.



#### Inheritors


| |
|---|
| [Success](-success/index.html) |
| [InvalidToken](-invalid-token/index.html) |
| [PermissionDenied](-permission-denied/index.html) |
| [UserConsentDenied](-user-consent-denied/index.html) |
| [ClientNotInitialized](-client-not-initialized/index.html) |
| [Error](-error/index.html) |


## Types


| Name | Summary |
|---|---|
| [ClientNotInitialized](-client-not-initialized/index.html) | [androidJvm]<br>object [ClientNotInitialized](-client-not-initialized/index.html) : [SetupResult](index.html)<br>Signalizes the unsuccessful completion of the setup process due to DoorClient not being initialized first. |
| [Error](-error/index.html) | [androidJvm]<br>data class [Error](-error/index.html)(val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) : [SetupResult](index.html)<br>Signalizes the unsuccessful completion of the setup process due to an unknown error detected. |
| [InvalidToken](-invalid-token/index.html) | [androidJvm]<br>object [InvalidToken](-invalid-token/index.html) : [SetupResult](index.html)<br>Signalizes the unsuccessful completion of the setup process due to an invalid token provided by the client. |
| [PermissionDenied](-permission-denied/index.html) | [androidJvm]<br>object [PermissionDenied](-permission-denied/index.html) : [SetupResult](index.html)<br>Signalizes the unsuccessful completion of the setup process due to the user not provided BLE permissions. |
| [Success](-success/index.html) | [androidJvm]<br>object [Success](-success/index.html) : [SetupResult](index.html)<br>Signalizes the successful completion of the setup process. |
| [UserConsentDenied](-user-consent-denied/index.html) | [androidJvm]<br>object [UserConsentDenied](-user-consent-denied/index.html) : [SetupResult](index.html)<br>Signalizes the unsuccessful completion of the setup process due to the user rejecting the required user consent. |

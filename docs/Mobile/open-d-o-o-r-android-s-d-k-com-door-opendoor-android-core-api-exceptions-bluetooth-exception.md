---
title: BluetoothException
---
---
title: BluetoothException
---
//[OpenDOOR Android SDK](../../../index.html)/[com.door.opendoor.android.core.api.exceptions](../index.html)/[BluetoothException](index.html)



# BluetoothException

sealed class [BluetoothException](index.html) : [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)

Base exception for Bluetooth failures in the OpenDOOR SDK



#### Inheritors


| |
|---|
| [BluetoothDisabledException](-bluetooth-disabled-exception/index.html) |
| [BluetoothPermissionDeniedException](-bluetooth-permission-denied-exception/index.html) |


## Types


| Name | Summary |
|---|---|
| [BluetoothDisabledException](-bluetooth-disabled-exception/index.html) | [androidJvm]<br>class [BluetoothDisabledException](-bluetooth-disabled-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [BluetoothException](index.html)<br>The current device does not have Bluetooth enabled |
| [BluetoothPermissionDeniedException](-bluetooth-permission-denied-exception/index.html) | [androidJvm]<br>class [BluetoothPermissionDeniedException](-bluetooth-permission-denied-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), throwable: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [BluetoothException](index.html)<br>User denied OpenDOOR SDK access to use the device's Bluetooth |


## Properties


| Name | Summary |
|---|---|
| [cause](../-sync-exception/-sync-internal-exception/index.html#-654012527%2FProperties%2F-1404661416) | [androidJvm]<br>open val [cause](../-sync-exception/-sync-internal-exception/index.html#-654012527%2FProperties%2F-1404661416): [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? |
| [message](../-sync-exception/-sync-internal-exception/index.html#1824300659%2FProperties%2F-1404661416) | [androidJvm]<br>open val [message](../-sync-exception/-sync-internal-exception/index.html#1824300659%2FProperties%2F-1404661416): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? |

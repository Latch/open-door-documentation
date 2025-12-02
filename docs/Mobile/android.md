---
title: Android
excerpt: >-
  The Android SDK allows you to initialize and unlock a DOOR-supported lock.
  This tutorial corresponds with version 2.0.0 of the SDK.
deprecated: false
hidden: false
metadata:
  robots: index
---
## Setup

1. Declare SDK as a dependency
2. Initialize the library
3. View the locks and select one to unlock

### Declare SDK as a dependency

Add **Maven Central** to your repositories (if not already present), then declare the dependency in your **application module's** `build.gradle.kts`:

```kotlin
repositories {
    google()
    mavenCentral()
}

dependencies {
  implementation('com.door.opendoor.android:2.0.0')
  //(...)
}
```

### Initialize the library

Use your Auth0 token retrieved from DOOR's Auth endpoint, call `setupWithToken()`.

The OpenDOOR SDK uses Kotlin Coroutines to perform actions asynchronously. All SDK functions are `suspend` functions that can be called from a coroutine scope, or you can use Flow-based streams for reactive updates.

Note that `context` here must not be the `applicationContext`.

```kotlin
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import com.door.opendoor.android.core.api.OpenDOOR
import com.door.opendoor.android.core.api.exceptions.SetupException
import com.door.opendoor.android.core.api.exceptions.NetworkException

val client = OpenDOOR.instance

CoroutineScope(Dispatchers.Main).launch {
    try {
        client.setupWithToken(
            context = context,
            token = token,
            includeAllLocks = true
        )
        // SDK is ready
    } catch (e: SetupException.InvalidTokenException) {
        // Handle invalid token - refresh and retry
    } catch (e: SetupException) {
        // Handle other setup errors
    } catch (e: NetworkException) {
        // Handle network errors
    }
}
```

The `includeAllLocks` parameter determines whether to show:

* `true`: All locks that user can access (partner and non-partner)
* `false`: Only partner-managed locks

### View the locks and select one to unlock

You can retrieve locks in two ways: get them once with `getLocks()`, or listen for continuous updates with `listenForLocks()`. Both approaches use the same implementation underneath - choose the one that fits your use case.

**Option 1: Get locks once**

```kotlin
import com.door.opendoor.android.core.api.exceptions.SDKException
import com.door.opendoor.android.core.api.exceptions.NetworkException

CoroutineScope(Dispatchers.Main).launch {
    try {
        val locks = client.getLocks()
        // Use locks list
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: NetworkException) {
        // Handle network errors
    }
}
```

**Option 2: Listen for lock updates (Flow)**

```kotlin
import kotlinx.coroutines.flow.collect

CoroutineScope(Dispatchers.Main).launch {
    try {
        client.listenForLocks().collect { locks ->
            // This will be called whenever locks are updated
            // Use locks list
        }
    } catch (e: SDKException) {
        // Handle SDK errors
    }
}
```

**Option 3: Listen for lock updates (Callback)**

```kotlin
import com.door.opendoor.android.core.api.listeners.LocksListener
import com.door.opendoor.android.core.api.model.Lock

client.listenForLocks(object : LocksListener {
    override fun onUpdate(locks: List<Lock>) {
        // This will be called whenever locks are updated
        // Use locks list
    }
})
```

With the locks retrieved, we can now call `unlock()` to unlock a DOOR lock.

## Unlock

To unlock a lock, call `unlock()` and listen for unlock events to track the progress and result.

```kotlin
import kotlinx.coroutines.flow.collect
import com.door.opendoor.android.core.api.exceptions.BluetoothException
import com.door.opendoor.android.core.api.exceptions.SDKException
import com.door.opendoor.android.core.api.model.UnlockEvent
import java.util.UUID

val lockId: UUID = lock.uuid

// Start listening for unlock events first
CoroutineScope(Dispatchers.Main).launch {
    client.listenForUnlockEvents().collect { event ->
        when (event) {
            is UnlockEvent.UnlockStarted -> {
                // Unlock process has started
            }
            is UnlockEvent.UnlockSuccess -> {
                // Lock is unlocked! event.lockId contains the lock UUID
            }
            is UnlockEvent.UnlockFailed -> {
                // Unlock failed - check event.failReason for details
                // event.lockId contains the lock UUID
            }
            is UnlockEvent.UnlockCanceled -> {
                // Unlock was canceled
            }
        }
    }
}

// Then initiate the unlock
CoroutineScope(Dispatchers.Main).launch {
    try {
        client.unlock(lockId)
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: BluetoothException) {
        // Handle Bluetooth errors
    }
}
```

**Alternative: Using callback listener**

```kotlin
import com.door.opendoor.android.core.api.exceptions.BluetoothException
import com.door.opendoor.android.core.api.exceptions.SDKException
import com.door.opendoor.android.core.api.listeners.UnlockEventsListener
import com.door.opendoor.android.core.api.model.UnlockEvent

client.listenForUnlockEvents(object : UnlockEventsListener {
    override fun onNewEvent(event: UnlockEvent) {
        when (event) {
            is UnlockEvent.UnlockStarted -> {
                // Unlock process has started
            }
            is UnlockEvent.UnlockSuccess -> {
                // Lock is unlocked!
            }
            is UnlockEvent.UnlockFailed -> {
                // Unlock failed
            }
            is UnlockEvent.UnlockCanceled -> {
                // Unlock was canceled
            }
        }
    }
})

CoroutineScope(Dispatchers.Main).launch {
    try {
        client.unlock(lockId)
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: BluetoothException) {
        // Handle Bluetooth errors
    }
}
```

Your DOOR lock should be unlocked now!

## Unlock the closest lock that's available

Another way to unlock the door is through "Proximity Unlock". It will continuously unlock the closest lock that's available.

First, set up a listener for unlock events. Then start proximity unlock, and stop it when needed.

**Using Flow:**

```kotlin
import kotlinx.coroutines.flow.collect
import com.door.opendoor.android.core.api.exceptions.BluetoothException
import com.door.opendoor.android.core.api.exceptions.SDKException
import com.door.opendoor.android.core.api.model.UnlockEvent

// Set up the listener first
val unlockJob = CoroutineScope(Dispatchers.Main).launch {
    client.listenForUnlockEvents().collect { event ->
        when (event) {
            is UnlockEvent.UnlockSuccess -> {
                // The unlocked door can be identified with event.lockId
            }
            is UnlockEvent.UnlockFailed -> {
                // Handle unlock failure
            }
            is UnlockEvent.UnlockCanceled -> {
                // Handle unlock cancellation
            }
            is UnlockEvent.UnlockStarted -> {
                // Unlock process started
            }
        }
    }
}

// Start proximity unlock
CoroutineScope(Dispatchers.Main).launch {
    try {
        client.startProximityUnlock()
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: BluetoothException) {
        // Handle Bluetooth errors
    }
}

// Stop proximity unlock when done
CoroutineScope(Dispatchers.Main).launch {
    try {
        client.stopProximityUnlock()
        unlockJob.cancel() // Cancel the listener job
    } catch (e: SDKException) {
        // Handle SDK errors
    }
}
```

**Using callback listener:**

```kotlin
import com.door.opendoor.android.core.api.exceptions.BluetoothException
import com.door.opendoor.android.core.api.exceptions.SDKException
import com.door.opendoor.android.core.api.listeners.UnlockEventsListener
import com.door.opendoor.android.core.api.model.UnlockEvent

// Set up the listener
client.listenForUnlockEvents(object : UnlockEventsListener {
    override fun onNewEvent(event: UnlockEvent) {
        when (event) {
            is UnlockEvent.UnlockSuccess -> {
                // The unlocked door can be identified with event.lockId
            }
            is UnlockEvent.UnlockFailed -> {
                // Handle unlock failure
            }
            is UnlockEvent.UnlockCanceled -> {
                // Handle unlock cancellation
            }
            is UnlockEvent.UnlockStarted -> {
                // Unlock process started
            }
        }
    }
})

// Start proximity unlock
CoroutineScope(Dispatchers.Main).launch {
    try {
        client.startProximityUnlock()
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: BluetoothException) {
        // Handle Bluetooth errors
    }
}

// Stop proximity unlock when done
CoroutineScope(Dispatchers.Main).launch {
    try {
        client.stopProximityUnlock()
    } catch (e: SDKException) {
        // Handle SDK errors
    }
}
```

Note: After stopping proximity unlock, you can set up a new listener and start it again if needed. The listener will continue to receive events from both explicit unlocks and proximity unlocks as long as it's active.

## Sync

Sync allows your mobile client to act as a bridge to the DOOR backend for uplink and downlink data requests, including battery, timestamp, activity logs, and engineering logs. In times of troubleshooting, a sync is recommended to either resolve the issue or provide DOOR with full information around the issue.

After each unlock, the SDK will passively sync data with the DOOR ecosystem to keep user data as up to date as possible. Explicitly calling `sync()` will initiate a longer sync operation that attempts to sync all critical data, including the data synced after unlock, along with non-critical data. The `sync()` operation takes about 10 seconds on average and will cancel any passive sync operations initiated after the unlock operation.

```kotlin
import com.door.opendoor.android.core.api.exceptions.BluetoothException
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.SDKException
import com.door.opendoor.android.core.api.exceptions.SyncException

CoroutineScope(Dispatchers.Main).launch {
    try {
        client.sync(lockId)
        // Sync completed successfully
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: BluetoothException) {
        // Handle Bluetooth errors
    } catch (e: NetworkException) {
        // Handle network errors
    } catch (e: SyncException) {
        // Handle sync-specific errors
    }
}
```

Your DOOR lock is synced now!

## Access logs

Retrieve access logs for a lock.

```kotlin
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.SDKException

CoroutineScope(Dispatchers.Main).launch {
    try {
        val accessLogs = client.getAccessLogs(lockId)
        // Use accessLogs list
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: NetworkException) {
        // Handle network errors
    }
}
```

## Guest Access

### Invite guests

```kotlin
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.SDKException
import com.door.opendoor.android.core.api.model.PasscodeType
import java.time.LocalDateTime

CoroutineScope(Dispatchers.Main).launch {
    try {
        val guest = client.inviteGuests(
            firstName = "John",
            lastName = "Doe",
            email = "john@example.com",
            phone = "+1234567890",
            startTime = LocalDateTime.now(),
            endTime = null, // No expiration
            deviceUuids = listOf(lockId),
            passcodeType = PasscodeType.PERMANENT
        )
        // Guest invitation successful - use guest object
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: NetworkException) {
        // Handle network errors
    }
}
```

### Retrieve guest list

```kotlin
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.SDKException

CoroutineScope(Dispatchers.Main).launch {
    try {
        val guestList = client.guests()
        // Use guestList
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: NetworkException) {
        // Handle network errors
    }
}
```

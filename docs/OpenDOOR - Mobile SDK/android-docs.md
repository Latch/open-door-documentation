---
title: Android SDK
excerpt: >-
  The Android SDK allows you to initialize and unlock a DOOR-supported lock.
  This tutorial corresponds with version 2.1.1 of the SDK.
deprecated: false
hidden: false
metadata:
  robots: index
---
## What's new in SDK 2.1.1

* **New modern API:** coroutine-first `suspend` functions, Flow listeners, callback listeners, and Activity-based setup for permission and consent UI.
* **Improved unlock:** explicit and proximity unlocks now share the same unlock event stream, with clearer progress, success, failure, and cancellation events.
* **Setup sync visibility during unlock:** `UnlockEvent.SetupSync` is emitted when the SDK needs to run setup sync before unlocking, such as the first time a user opens a door and the lock needs access data.
* **Unlock cancellation:** `cancelUnlock()` cancels the active explicit unlock or the current proximity unlock attempt and emits `UnlockEvent.UnlockCanceled`.
* **Increased proximity unlock range:** proximity unlock now supports a larger BLE trigger range than earlier SDK 2.0 builds while still selecting the closest eligible lock.
* Finer-grained log levels

## Setup

1. Declare SDK as a dependency
2. Initialize the library
3. View the locks and select one to unlock
4. Code reference: [Browse the latest API docs](https://opendoor-developer-android.netlify.app/)

### Declare SDK as a dependency

Add **Maven Central** to your repositories (if not already present), then declare the dependency in your **application module's** `build.gradle.kts`:

```kotlin
repositories {
    google()
    mavenCentral()
}

dependencies {
  implementation('com.door.opendoor.android:2.1.1')
  //(...)
}
```

### Initialize the library

Use your Auth0 token retrieved from DOOR's Auth endpoint, call `setupWithToken()`.

The OpenDOOR SDK uses Kotlin Coroutines to perform actions asynchronously. All SDK functions are `suspend` functions that can be called from a coroutine scope, or you can use Flow-based streams for reactive updates.

**Important:** `setupWithToken()` must be called from the main thread because it takes a live `Activity` for permission and consent UI.

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
            activity = activity,
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

### Thread Requirements

The SDK has specific thread requirements for different operations:

**Must be called from the main thread:**

* `unlock()`
* `cancelUnlock()`
* `sync()`
* `startProximityUnlock()`
* `stopProximityUnlock()`

All BLE operations must be called from the main thread.

**Can be called from any thread:**

* `fetchLocks()`
* `getAccessLogs()`
* `inviteGuests()`
* `guests()`
* `revokeGuestAllAccesses()`
* `revokeGuestAccess()`
* `setupWithToken()`

All examples in this tutorial use `Dispatchers.Main`.

### View the locks and select one to unlock

You can retrieve locks in two ways: fetch them once with `fetchLocks()`, or listen for continuous updates with `listenForLocks()`. These methods have different behaviors:

* **`fetchLocks()`**: Waits for the server call to complete before returning. Does not return until the network request finishes (or fails). Use this when you need fresh data and can wait for the network call.

* **`listenForLocks()`**: Returns cached data immediately, then attempts to refresh from the server in the background. The Flow will emit cached locks first, then emit updated locks when the server refresh completes. Use this when you want to show data quickly and update it when fresh data arrives.

**Option 1: Fetch locks once**

```kotlin
import com.door.opendoor.android.core.api.exceptions.SDKException
import com.door.opendoor.android.core.api.exceptions.NetworkException

CoroutineScope(Dispatchers.Main).launch {
    try {
        val locks = client.fetchLocks()
        // Use locks list - this will only return after server call completes
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
            // First call will have cached data immediately, then updated data when server refresh completes
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

**Important:** `unlock()` must be called from the main thread as it performs BLE operations.

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
            is UnlockEvent.SetupSync -> {
                // The lock needs setup sync before unlock.
                // Show setup/sync progress here if this is the user's first unlock for this door.
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

To cancel an active explicit unlock attempt, call `cancelUnlock()`. Cancellation is reported through `UnlockEvent.UnlockCanceled`. If no unlock is active, `cancelUnlock()` completes without emitting an event.

```kotlin
CoroutineScope(Dispatchers.Main).launch {
    try {
        client.cancelUnlock()
    } catch (e: SDKException) {
        // Handle SDK errors
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
            is UnlockEvent.SetupSync -> {
                // The lock needs setup sync before unlock.
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

Another way to unlock the door is through "Proximity Unlock". It continuously scans for nearby locks and unlocks the closest eligible lock when it is within the SDK's BLE range threshold.

SDK 2.1 increases the proximity unlock trigger range compared with earlier SDK 2.0 builds. Real-world range still depends on phone model, lock type, installation, and local BLE conditions, so use unlock events to drive UI state instead of assuming a fixed distance.

**Important:** `startProximityUnlock()` and `stopProximityUnlock()` must be called from the main thread as they perform BLE operations.

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
            is UnlockEvent.SetupSync -> {
                // The selected lock needs setup sync before proximity unlock can finish.
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

Use `cancelUnlock()` to cancel only the current proximity unlock attempt. Proximity unlock mode remains active and can continue scanning. Use `stopProximityUnlock()` when you want to stop proximity unlock mode.

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
            is UnlockEvent.SetupSync -> {
                // The selected lock needs setup sync before proximity unlock can finish.
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

**Important:** `sync()` must be called from the main thread as it performs BLE operations.

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

### Revoke guest access

Revoke operations are network-backed. After revoking, call `guests()` again to refresh local state.

**Revoke a guest's access to a single lock:**

```kotlin
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.RevokeGuestException
import com.door.opendoor.android.core.api.exceptions.SDKException

CoroutineScope(Dispatchers.Main).launch {
    try {
        val guestList = client.guests()
        val guest = guestList.first()
        val guestId = guest.id

        val lockId = guest.guestAccesses.first().lockId

        client.revokeGuestAccess(
            guestId = guestId,
            lockId = lockId
        )

        // Optionally refresh guests after revoke
        val refreshedGuests = client.guests()
    } catch (e: RevokeGuestException) {
        when (e.reason) {
            RevokeGuestException.Reason.PASSCODE_TYPE_CANT_BE_REVOKED -> {
                // The passcode type can't be revoked for this guest access
            }
            else -> {
                // Handle other revoke failures
            }
        }
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: NetworkException) {
        // Handle network errors
    }
}
```

**Revoke all of a guest's accesses:**

```kotlin
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.RevokeGuestException
import com.door.opendoor.android.core.api.exceptions.SDKException

CoroutineScope(Dispatchers.Main).launch {
    try {
        val guestList = client.guests()
        val guestId = guestList.first().id

        client.revokeGuestAllAccesses(guestId)

        // Optionally refresh guests after revoke
        val refreshedGuests = client.guests()
    } catch (e: RevokeGuestException) {
        when (e.reason) {
            RevokeGuestException.Reason.PASSCODE_TYPE_CANT_BE_REVOKED -> {
                // The passcode type can't be revoked for one or more guest accesses
            }
            else -> {
                // Handle other revoke failures
            }
        }
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: NetworkException) {
        // Handle network errors
    }
}
```

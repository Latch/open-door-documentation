---
title: Android SDK
excerpt: >-
  The SDK provides APIs to view, unlock and sync DOOR-supported locks and to
  manage guest access. This tutorial corresponds with version 2.2 of the SDK
deprecated: false
hidden: false
metadata:
  robots: index
---
<br />

## [Release notes](https://developers.door.com/docs/android-release-notes)

## Setup

1. [Declare SDK as a dependency](https://developers.door.com/docs/android-docs#declare-sdk-as-a-dependency)
2. [Initialize the library](https://developers.door.com/docs/android-docs#initialize-the-library)
3. [Clear SDK state](https://developers.door.com/docs/android-docs#clear-sdk-state)
4. Code reference: [Browse the latest API docs](https://opendoor-developer-android.netlify.app/)
5. [Thread Requirements](https://developers.door.com/docs/android-docs#thread-requirements)
6. [View the locks and select one to unlock](https://developers.door.com/docs/android-docs#view-the-locks-and-select-one-to-unlock)
7. [Unlock](https://developers.door.com/docs/android-docs#unlock)
8. [Unlock the closest lock that's available](https://developers.door.com/docs/android-docs#unlock-the-closest-lock-thats-available)
9. [Sync](https://developers.door.com/docs/android-docs#sync)
10. [Access Logs](https://developers.door.com/docs/android-docs#access-logs)
11. [Guest Access](https://developers.door.com/docs/android-docs#guest-access)
12. [Log Level](https://developers.door.com/docs/android-docs#log-level)

<br />

### Declare SDK as a dependency

Add **Maven Central** to your repositories (if not already present), then declare the dependency in your **application module's** `build.gradle.kts`:

```kotlin
repositories {
    google()
    mavenCentral()
}

dependencies {
    implementation("com.door:opendoor.android:2.2")
}
```

### Initialize the library

Use your Auth0 token retrieved from DOOR's Auth endpoint, then call `setupWithToken()`.

The OpenDOOR SDK uses Kotlin coroutines to perform actions asynchronously. SDK operations are exposed as `suspend` functions, `Flow` streams, or callback listeners depending on the use case.

**Important:** `setupWithToken()` must be called from the main thread because it takes a live `Activity` for permission and consent UI.

Note that `activity` must be a foreground `Activity`, not the `applicationContext`.

```kotlin
import com.door.opendoor.android.core.api.OpenDOOR
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.SetupException
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

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

The `includeAllLocks` parameter determines whether the SDK loads:

* `true`: all locks that the user can access, including partner and non-partner locks
* `false`: only partner-managed locks

### Clear SDK state

To sign out, clear cached SDK data, and remove the current in-memory token, call `clear()`. After calling `clear()`, call `setupWithToken()` again before using other SDK APIs.

```kotlin
import com.door.opendoor.android.core.api.exceptions.SDKException
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

CoroutineScope(Dispatchers.Main).launch {
    try {
        client.clear()
    } catch (e: SDKException) {
        // Handle SDK errors
    }
}
```

### Thread Requirements

The SDK has specific thread requirements for BLE and setup operations.

**Must be called from the main thread:**

* `setupWithToken()`
* `unlock()`
* `cancelUnlock()`
* `sync()`
* `startProximityUnlock()`
* `stopProximityUnlock()`

**Can be called from any thread:**

* `fetchLocks()`
* `listenForLocks()`
* `stopListenForLocks()`
* `listenForUnlockEvents()`
* `stopListenForUnlockEvents()`
* `getAccessLogs()`
* `inviteGuest()`
* `guests()`
* `revokeGuestAllAccesses()`
* `revokeGuestAccess()`
* `setLogLevel()`

All examples in this tutorial use `Dispatchers.Main`.

### View the locks and select one to unlock

You can retrieve locks in two ways: fetch them once with `fetchLocks()`, or listen for continuous updates with `listenForLocks()`.

* **`fetchLocks()`** waits for the server request to complete before returning. Use this when you need fresh data and can wait for the network request.
* **`listenForLocks()`** emits cached data immediately, then refreshes from the server in the background. Use this when you want to show available locks quickly and update the list when fresh data arrives.

**Option 1: Fetch locks once**

```kotlin
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.SDKException
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

CoroutineScope(Dispatchers.Main).launch {
    try {
        val locks = client.fetchLocks()
        // Use locks list
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: NetworkException) {
        // Handle network errors
    }
}
```

**Option 2: Listen for lock updates with Flow**

```kotlin
import com.door.opendoor.android.core.api.exceptions.SDKException
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.collect
import kotlinx.coroutines.launch

val locksJob = CoroutineScope(Dispatchers.Main).launch {
    try {
        client.listenForLocks().collect { locks ->
            // First emission may be cached data.
            // Later emissions contain refreshed lock data.
        }
    } catch (e: SDKException) {
        // Handle SDK errors
    }
}

// Stop collecting Flow updates when the UI no longer needs them.
locksJob.cancel()
```

**Option 3: Listen for lock updates with a callback**

```kotlin
import com.door.opendoor.android.core.api.listeners.LocksListener
import com.door.opendoor.android.core.api.model.Lock

val locksListener = object : LocksListener {
    override fun onUpdate(locks: List<Lock>) {
        // Use locks list
    }

    override fun onError(error: Throwable) {
        // Handle listener error
    }
}

client.listenForLocks(locksListener)

// Stop callback updates when the UI no longer needs them.
client.stopListenForLocks(locksListener)
```

With the locks retrieved, call `unlock()` to unlock a DOOR lock.

## Unlock

To unlock a lock, call `unlock()` and listen for unlock events to track progress and the final result.

**Important:** `unlock()` must be called from the main thread as it performs BLE operations.

```kotlin
import com.door.opendoor.android.core.api.model.UnlockStatus
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.collect
import kotlinx.coroutines.launch

// Start listening for unlock events first.
val unlockEventsJob = CoroutineScope(Dispatchers.Main).launch {
    client.listenForUnlockEvents().collect { event ->
        when (val status = event.status) {
            UnlockStatus.Started -> {
                // Unlock process has started.
            }
            UnlockStatus.Success -> {
                val unlockedLock = event.lock
                // Lock is unlocked.
            }
            is UnlockStatus.Failed -> {
                handleUnlockFailure(status.reason)
            }
            UnlockStatus.Canceled -> {
                // Unlock was canceled.
            }
            is UnlockStatus.ConnectForSetupSync,
            is UnlockStatus.SetupSync,
            UnlockStatus.UpdateSyncPackage,
            is UnlockStatus.ConnectForUnlock,
            is UnlockStatus.Unlock -> {
                // Optional progress status. Retry phases expose attempt.
            }
        }
    }
}
```

`UnlockStatus.Failed` carries an `UnlockFailureReason`:

```kotlin
import com.door.opendoor.android.core.api.model.UnlockFailureReason

fun handleUnlockFailure(reason: UnlockFailureReason) {
    when (reason) {
        UnlockFailureReason.BluetoothDisabled -> {
            // Bluetooth was disabled during unlock.
        }
        UnlockFailureReason.OutOfSchedule -> {
            // The user is outside the allowed access schedule.
        }
        UnlockFailureReason.LockNotFound -> {
            // The requested lock could not be found nearby.
        }
        UnlockFailureReason.ConnectionFailed -> {
            // BLE connection to the lock failed.
        }
        UnlockFailureReason.AuthFailed -> {
            // Credentials were rejected or could not be refreshed.
        }
        is UnlockFailureReason.Internal -> {
            // Handle any other SDK failure. reason.code is stable for diagnostics.
        }
    }
}
```

Then initiate the unlock:

```kotlin
import com.door.opendoor.android.core.api.exceptions.BluetoothException
import com.door.opendoor.android.core.api.exceptions.SDKException
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

CoroutineScope(Dispatchers.Main).launch {
    try {
        client.unlock(lock.id)
        // You can also call client.unlock(lock) if you already have the Lock model.
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: BluetoothException) {
        // Handle Bluetooth errors
    }
}
```

To cancel an active explicit unlock attempt, call `cancelUnlock()`. Cancellation is reported through `UnlockStatus.Canceled`. If no unlock is active, `cancelUnlock()` completes without emitting an event.

```kotlin
import com.door.opendoor.android.core.api.exceptions.SDKException
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

CoroutineScope(Dispatchers.Main).launch {
    try {
        client.cancelUnlock()
    } catch (e: SDKException) {
        // Handle SDK errors
    }
}
```

**Using a callback listener**

```kotlin
import com.door.opendoor.android.core.api.listeners.UnlockEventsListener
import com.door.opendoor.android.core.api.model.UnlockEvent
import com.door.opendoor.android.core.api.model.UnlockStatus

val unlockEventsListener = object : UnlockEventsListener {
    override fun onNewEvent(event: UnlockEvent) {
        when (event.status) {
            UnlockStatus.Success -> {
                // Lock is unlocked.
            }
            is UnlockStatus.Failed -> {
                // Unlock failed. Check event.status.reason.
            }
            UnlockStatus.Canceled -> {
                // Unlock was canceled.
            }
            else -> {
                // Handle in-progress statuses.
            }
        }
    }
}

client.listenForUnlockEvents(unlockEventsListener)

// Stop callback updates when the UI no longer needs them.
client.stopListenForUnlockEvents(unlockEventsListener)
```

Your DOOR lock should be unlocked now.

## Unlock the closest lock that's available

Another way to unlock is through proximity unlock. Proximity unlock continuously scans for nearby locks and unlocks the closest eligible lock when it is within the SDK's BLE range threshold.

Real-world range depends on phone model, lock type, installation, and local BLE conditions, so use unlock events to drive UI state instead of assuming a fixed distance.

**Important:** `startProximityUnlock()` and `stopProximityUnlock()` must be called from the main thread as they perform BLE operations.

First, set up an unlock event listener. Then start proximity unlock, and stop it when needed.

```kotlin
import com.door.opendoor.android.core.api.exceptions.BluetoothException
import com.door.opendoor.android.core.api.exceptions.SDKException
import com.door.opendoor.android.core.api.model.UnlockStatus
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.collect
import kotlinx.coroutines.launch

val proximityEventsJob = CoroutineScope(Dispatchers.Main).launch {
    client.listenForUnlockEvents().collect { event ->
        when (event.status) {
            UnlockStatus.Success -> {
                val unlockedLock = event.lock
                // The closest eligible lock was unlocked.
            }
            is UnlockStatus.Failed -> {
                // Handle unlock failure.
            }
            UnlockStatus.Canceled -> {
                // Handle unlock cancellation.
            }
            else -> {
                // Handle in-progress statuses.
            }
        }
    }
}

CoroutineScope(Dispatchers.Main).launch {
    try {
        client.startProximityUnlock()
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: BluetoothException) {
        // Handle Bluetooth errors
    }
}

CoroutineScope(Dispatchers.Main).launch {
    try {
        client.stopProximityUnlock()
        proximityEventsJob.cancel()
    } catch (e: SDKException) {
        // Handle SDK errors
    }
}
```

Use `cancelUnlock()` to cancel only the current proximity unlock attempt. Proximity unlock mode remains active and can continue scanning. Use `stopProximityUnlock()` when you want to stop proximity unlock mode.

## Sync

Sync allows your mobile client to act as a bridge to the DOOR backend for uplink and downlink data requests, including battery, timestamp, activity logs, and engineering logs. In times of troubleshooting, a sync is recommended to either resolve the issue or provide DOOR with full information around the issue.

After each unlock, the SDK will passively sync data with the DOOR ecosystem to keep user data as up to date as possible. Explicitly calling `sync()` will initiate a longer sync operation that attempts to sync all critical data, including the data synced after unlock, along with non-critical data. The `sync()` operation takes about 10 seconds on average and will cancel any passive sync operations initiated after the unlock operation.

**Important:** `sync()` must be called from the main thread as it performs BLE operations.

```kotlin
import com.door.opendoor.android.core.api.exceptions.BluetoothException
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.SDKException
import com.door.opendoor.android.core.api.exceptions.SyncException
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

CoroutineScope(Dispatchers.Main).launch {
    try {
        client.sync(lock.id)
        // Sync completed successfully.
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

Your DOOR lock is synced now.

## Access Logs

Retrieve access logs for a lock.

```kotlin
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.SDKException
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

CoroutineScope(Dispatchers.Main).launch {
    try {
        val accessLogs = client.getAccessLogs(lock.id)
        // Use accessLogs list.
    } catch (e: SDKException) {
        // Handle SDK errors
    } catch (e: NetworkException) {
        // Handle network errors
    }
}
```

## Guest Access

### Invite guests

Use `inviteGuest()` with an `InviteType` that describes the access you want to grant.

**In-app access**

```kotlin
import com.door.opendoor.android.core.api.exceptions.GuestInvitesException
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.SDKException
import com.door.opendoor.android.core.api.model.InAppInvite
import java.time.Instant
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

CoroutineScope(Dispatchers.Main).launch {
    try {
        client.inviteGuest(
            firstName = "John",
            lastName = "Doe",
            email = "john@example.com",
            phone = null,
            lockIds = listOf(lock.id),
            inviteType = InAppInvite(
                accessType = null,
                startTime = Instant.now(),
                endTime = null,
                showDoorcodes = true
            )
        )
        // Guest invitation successful.
    } catch (e: GuestInvitesException) {
        // Handle invite-specific errors.
    } catch (e: SDKException) {
        // Handle SDK errors.
    } catch (e: NetworkException) {
        // Handle network errors.
    }
}
```

**Temporary doorcode access**

```kotlin
import com.door.opendoor.android.core.api.model.Duration as DoorcodeDuration
import com.door.opendoor.android.core.api.model.Period
import com.door.opendoor.android.core.api.model.TempDoorcodeInvite

CoroutineScope(Dispatchers.Main).launch {
    try {
        client.inviteGuest(
            firstName = "John",
            lastName = "Doe",
            email = "john@example.com",
            phone = null,
            lockIds = listOf(lock.id),
            inviteType = TempDoorcodeInvite(
                accessType = null,
                duration = DoorcodeDuration.FullDay,
                period = Period.Today
            )
        )
        // Temporary doorcode invitation successful.
    } catch (e: GuestInvitesException) {
        // Handle invite-specific errors.
    } catch (e: SDKException) {
        // Handle SDK errors.
    } catch (e: NetworkException) {
        // Handle network errors.
    }
}
```

### Retrieve guest list

```kotlin
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.SDKException
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

CoroutineScope(Dispatchers.Main).launch {
    try {
        val guestList = client.guests()
        // Use guestList.
    } catch (e: SDKException) {
        // Handle SDK errors.
    } catch (e: NetworkException) {
        // Handle network errors.
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
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

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

        val refreshedGuests = client.guests()
    } catch (e: RevokeGuestException) {
        when (e.reason) {
            RevokeGuestException.Reason.PASSCODE_TYPE_CANT_BE_REVOKED -> {
                // The passcode type cannot be revoked for this guest access.
            }
            else -> {
                // Handle other revoke failures.
            }
        }
    } catch (e: SDKException) {
        // Handle SDK errors.
    } catch (e: NetworkException) {
        // Handle network errors.
    }
}
```

**Revoke all of a guest's accesses:**

```kotlin
import com.door.opendoor.android.core.api.exceptions.NetworkException
import com.door.opendoor.android.core.api.exceptions.RevokeGuestException
import com.door.opendoor.android.core.api.exceptions.SDKException
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

CoroutineScope(Dispatchers.Main).launch {
    try {
        val guestList = client.guests()
        val guestId = guestList.first().id

        client.revokeGuestAllAccesses(guestId)

        val refreshedGuests = client.guests()
    } catch (e: RevokeGuestException) {
        when (e.reason) {
            RevokeGuestException.Reason.PASSCODE_TYPE_CANT_BE_REVOKED -> {
                // The passcode type cannot be revoked for one or more guest accesses.
            }
            else -> {
                // Handle other revoke failures.
            }
        }
    } catch (e: SDKException) {
        // Handle SDK errors.
    } catch (e: NetworkException) {
        // Handle network errors.
    }
}
```

## Log Level

Set the SDK log level to control diagnostic output. `LogLevel.ERROR` is appropriate for most release builds. `LogLevel.DEBUG` can be useful while developing or troubleshooting an integration.

```kotlin
import com.door.opendoor.android.core.api.model.LogLevel

client.setLogLevel(LogLevel.DEBUG)
```

```kotlin
import com.door.opendoor.android.core.api.model.LogLevel

client.setLogLevel(LogLevel.DEBUG)
```

Set the SDK log level to control diagnostic output. `LogLevel.ERROR` is appropriate for most release builds. `LogLevel.DEBUG` can be useful while developing or troubleshooting an integration.

```kotlin
import com.door.opendoor.android.core.api.model.LogLevel

client.setLogLevel(LogLevel.DEBUG)
```

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

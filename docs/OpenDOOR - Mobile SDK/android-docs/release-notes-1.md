---
title: Release notes
excerpt: Android SDK release notes
deprecated: false
hidden: false
metadata:
  robots: index
---
## What's new in SDK 2.2.0

New Features

* Redesigned unlock event model with a full lifecycle. UnlockEvent is now a single type carrying the affected Lock, the unlock method, and a granular UnlockStatus. The lifecycle exposes every stage of an unlock — Started, ConnectForSetupSync, SetupSync, UpdateSyncPackage, ConnectForUnlock, Unlock, Failed, Canceled, and Success — and connect/sync/unlock stages report which UnlockAttempt they belong to (First or Second), so you can drive precise UI for the entire flow.
  * UnlockEvent changed from a sealed hierarchy (UnlockStarted, SetupSync, UnlockFailed, UnlockCanceled, UnlockSuccess, each exposing lockId: UUID?) to a single data class UnlockEvent(lock: Lock?, method: UnlockEventMethod, status: UnlockStatus). Code that pattern-matched the old subclasses or read lockId must migrate to reading status and lock.
* Richer, structured unlock failure reasons. UnlockFailureReason is now a sealed type that distinguishes the actual cause of a failed unlock, including new AuthFailed and ConnectionFailed cases and an Internal(code: String) case that surfaces a diagnostic code.
  * UnlockFailureReason changed from an enum to a sealed class. The old values BluetoothError, LockNotRecognized, Timeout, and InternalError were removed or folded into the new cases (ConnectionFailed, Internal(code)). Update exhaustive when statements accordingly.
* Stop-listening APIs. DoorClient now offers stopListenForLocks(listener) and stopListenForUnlockEvents(listener), so you can deregister observers symmetrically and avoid leaking listeners across screen lifecycles.
* Runtime log-level control. A new LogLevel enum (DEBUG, ERROR) and DoorClient.setLogLevel(level) let you adjust SDK logging verbosity at runtime

Improvements

* More reliable lock synchronization. Sync-configuration refresh now retries automatically on transient network errors and also runs whenever you fetch the latest locks, keeping unlock readiness aligned with the server without a separate call.
* More precise guest-revocation and access-log results. Revoking a guest now reports a DEVICE_NOT_FOUND reason and preserves the underlying error message instead of collapsing to a generic network error, and the access-log result set gained GUEST_SUCCESS and UNKNOWN_TIME_FAILURE.

Bug Fixes

* In-app guest invites with an expiration time are no longer rejected. Sending an in-app invite with an end time previously failed with a server validation error because it was sent as a recurring (daily) credential. In-app invites are now always issued as a non-recurring credential that accepts an optional end time.
* Setup no longer crashes on an unreadable encrypted store. If the SDK's encrypted storage could no longer be decrypted (for example after an Android Keystore key was invalidated by a credential reset or device restore), setup crashed. The SDK now detects this, resets and regenerates its encrypted store, and retries automatically.
* A failed unlock now recovers on its own: an authentication failure or a stale setup transparently triggers a fresh sync-package download and setup, followed by a single retry, before reporting failure. Connection, setup, and unlock stages each have dedicated timeouts so a stalled lock fails fast instead of hanging.

## What's new in SDK 2.1.1

* **New modern API:** coroutine-first `suspend` functions, Flow listeners, callback listeners, and Activity-based setup for permission and consent UI.
* **Improved unlock:** explicit and proximity unlocks now share the same unlock event stream, with clearer progress, success, failure, and cancellation events.
* **Setup sync visibility during unlock:** `UnlockEvent.SetupSync` is emitted when the SDK needs to run setup sync before unlocking, such as the first time a user opens a door and the lock needs access data.
* **Unlock cancellation:** `cancelUnlock()` cancels the active explicit unlock or the current proximity unlock attempt and emits `UnlockEvent.UnlockCanceled`.
* **Increased proximity unlock range:** proximity unlock now supports a larger BLE trigger range than earlier SDK 2.0 builds while still selecting the closest eligible lock.
* **Finer-grained log levels**

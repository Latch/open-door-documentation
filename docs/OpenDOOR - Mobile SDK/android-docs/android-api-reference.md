---
title: Android API Reference
excerpt: Public API reference for the OpenDOOR Android SDK.
hidden: true
---

Generated from the Kotlin sources (Dokka). One page per public type; members are listed inline.

## Types

- [AccessLog](doc:android-ref-accesslog) — Record of an access attempt on a lock.
- [AccessLogMethod](doc:android-ref-accesslogmethod) — Method used during an access attempt.
- [AccessLogResult](doc:android-ref-accesslogresult) — Result of an access attempt.
- [AccessType](doc:android-ref-accesstype) — Type of access granted to a guest.
- [BluetoothException](doc:android-ref-bluetoothexception) — Bluetooth access failure.
- [DoorClient](doc:android-ref-doorclient) — Public OpenDOOR SDK Core Module.
- [Duration](doc:android-ref-duration) — Duration for temporary doorcode access.
- [Guest](doc:android-ref-guest) — Person with shared access to one or more locks.
- [GuestAccess](doc:android-ref-guestaccess) — Access granted to a guest on a specific lock.
- [GuestInvitesException](doc:android-ref-guestinvitesexception) — Partial or complete guest-invitation failure.
- [InAppInvite](doc:android-ref-inappinvite) — In-app access with time-based restrictions.
- [InviteGuestException](doc:android-ref-inviteguestexception) — Guest invitation business-rule failure.
- [InviteType](doc:android-ref-invitetype) — Invite types that define how a guest receives access.
- [Lock](doc:android-ref-lock) — User-visible lock information.
- [LockActionException](doc:android-ref-lockactionexception) — Failure while acting on one lock.
- [LocksListener](doc:android-ref-lockslistener) — Listener for update-only lock lists.
- [LogLevel](doc:android-ref-loglevel) — Minimum SDK logging level.
- [NetworkException](doc:android-ref-networkexception) — Network access failure.
- [OpenDOOR](doc:android-ref-opendoor) — OpenDOOR (com.door.opendoor.android.core.api)
- [PasscodeType](doc:android-ref-passcodetype) — Type of access credential granted to a guest.
- [Period](doc:android-ref-period) — Period for temporary doorcode access.
- [RevokeGuestException](doc:android-ref-revokeguestexception) — Guest-access revocation failure.
- [SDKException](doc:android-ref-sdkexception) — General SDK access failure.
- [SetupException](doc:android-ref-setupexception) — Setup failure.
- [SyncException](doc:android-ref-syncexception) — Active sync failure.
- [TemporaryDoorcodeInvite](doc:android-ref-temporarydoorcodeinvite) — Temporary doorcode access.
- [UnlockAttempt](doc:android-ref-unlockattempt) — Which pass through the unlock flow produced an event.
- [UnlockEvent](doc:android-ref-unlockevent) — Event emitted during explicit and proximity unlock operations.
- [UnlockEventMethod](doc:android-ref-unlockeventmethod) — Method used for unlock.
- [UnlockEventsListener](doc:android-ref-unlockeventslistener) — Listener for unlock lifecycle events.
- [UnlockEventStatus](doc:android-ref-unlockeventstatus) — Lifecycle status carried by an unlock event.
- [UnlockException](doc:android-ref-unlockexception) — Explicit unlock request failure before an attempt starts.
- [UnlockFailureReason](doc:android-ref-unlockfailurereason) — Canonical reason an in-flight unlock failed.

---
title: iOS API Reference
excerpt: Public API reference for the OpenDOOR iOS SDK.
hidden: true
---

Generated from the Swift sources (DocC). One page per public type; members are listed inline.

## Types

- [AccessLog](doc:ios-ref-accesslog) — Record of an access attempt on a lock.
- [AccessLogMethod](doc:ios-ref-accesslogmethod) — Method used during an access attempt.
- [AccessLogResult](doc:ios-ref-accesslogresult) — Result of an access attempt.
- [AccessType](doc:ios-ref-accesstype) — Type of access granted to a guest.
- [BluetoothError](doc:ios-ref-bluetootherror) — Bluetooth access failure.
- [DOORClient](doc:ios-ref-doorclient) — Public OpenDOOR SDK Core Module.
- [Duration](doc:ios-ref-duration) — Duration for temporary doorcode access.
- [Guest](doc:ios-ref-guest) — Person with shared access to one or more locks.
- [GuestAccess](doc:ios-ref-guestaccess) — Access granted to a guest on a specific lock.
- [GuestInvitesError](doc:ios-ref-guestinviteserror) — Partial or complete guest-invitation failure.
- [InAppInvite](doc:ios-ref-inappinvite) — In-app access with time-based restrictions.
- [InternalSettingsKey](doc:ios-ref-internalsettingskey) — Enumeration InternalSettingsKey
- [InviteGuestError](doc:ios-ref-inviteguesterror) — Guest invitation business-rule failure.
- [InviteType](doc:ios-ref-invitetype) — Invite types that define how a guest receives access.
- [Lock](doc:ios-ref-lock) — User-visible lock information.
- [LockActionError](doc:ios-ref-lockactionerror) — Failure while acting on one lock.
- [LocksListener](doc:ios-ref-lockslistener) — Listener for update-only lock lists.
- [LogLevel](doc:ios-ref-loglevel) — Minimum SDK logging level.
- [NetworkError](doc:ios-ref-networkerror) — Network access failure.
- [OpenDOOR](doc:ios-ref-opendoor) — Enumeration OpenDOOR
- [OpenDOORSDKError](doc:ios-ref-opendoorsdkerror) — Common protocol for errors exposed by the OpenDOOR SDK.
- [PasscodeType](doc:ios-ref-passcodetype) — Type of access credential granted to a guest.
- [Period](doc:ios-ref-period) — Period for temporary doorcode access.
- [RevokeGuestError](doc:ios-ref-revokeguesterror) — Guest-access revocation failure.
- [SDKError](doc:ios-ref-sdkerror) — General SDK access failure.
- [SetupError](doc:ios-ref-setuperror) — Setup failure.
- [SyncError](doc:ios-ref-syncerror) — Active sync failure.
- [TemporaryDoorcodeInvite](doc:ios-ref-temporarydoorcodeinvite) — Temporary doorcode access.
- [UnlockAttempt](doc:ios-ref-unlockattempt) — Which pass through the unlock flow produced an event.
- [UnlockError](doc:ios-ref-unlockerror) — Explicit unlock request failure before an attempt starts.
- [UnlockEvent](doc:ios-ref-unlockevent) — Event emitted during explicit and proximity unlock operations.
- [UnlockEventMethod](doc:ios-ref-unlockeventmethod) — Method used for unlock.
- [UnlockEventsListener](doc:ios-ref-unlockeventslistener) — Listener for unlock lifecycle events.
- [UnlockEventStatus](doc:ios-ref-unlockeventstatus) — Lifecycle status carried by an unlock event.
- [UnlockFailureReason](doc:ios-ref-unlockfailurereason) — Canonical reason an in-flight unlock failed.

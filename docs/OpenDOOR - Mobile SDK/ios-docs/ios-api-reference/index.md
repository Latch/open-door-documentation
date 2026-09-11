---
title: iOS API Reference
excerpt: Public OpenDOOR iOS SDK 2.1.0 API reference.
hidden: false
---

This reference describes the public API of **OpenDOOR iOS SDK 2.1.0**, imported as `OpenDOORCore`.

Start with [OpenDOOR](doc:ios-ref-opendoor) to obtain a [DOORClient](doc:ios-ref-doorclient), then authenticate with `setupWithToken(token:includeAllLocks:)`.

The declarations below match the [2.1.0 release](https://github.com/Latch/opendoor-sdk-spm/tree/2.1.0). Use the [iOS SDK guide](doc:ios-docs) for installation and integration examples.

## Types

| Type | Kind |
| --- | --- |
| [AccessLog](doc:ios-ref-accesslog) | struct |
| [AccessLogMethod](doc:ios-ref-accesslogmethod) | enum |
| [AccessLogResult](doc:ios-ref-accesslogresult) | enum |
| [AccessType](doc:ios-ref-accesstype) | enum |
| [BluetoothError](doc:ios-ref-bluetootherror) | enum |
| [DOORClient](doc:ios-ref-doorclient) | protocol |
| [Duration](doc:ios-ref-duration) | enum |
| [Guest](doc:ios-ref-guest) | struct |
| [GuestAccess](doc:ios-ref-guestaccess) | struct |
| [GuestInvitesError](doc:ios-ref-guestinviteserror) | struct |
| [InAppInvite](doc:ios-ref-inappinvite) | struct |
| [InviteGuestError](doc:ios-ref-inviteguesterror) | enum |
| [InviteType](doc:ios-ref-invitetype) | protocol |
| [Lock](doc:ios-ref-lock) | struct |
| [LockActionError](doc:ios-ref-lockactionerror) | struct |
| [LocksListener](doc:ios-ref-lockslistener) | protocol |
| [LogLevel](doc:ios-ref-loglevel) | enum |
| [NetworkError](doc:ios-ref-networkerror) | enum |
| [OpenDOOR](doc:ios-ref-opendoor) | enum |
| [OpenDOORSDKError](doc:ios-ref-opendoorsdkerror) | protocol |
| [PasscodeType](doc:ios-ref-passcodetype) | enum |
| [Period](doc:ios-ref-period) | enum |
| [RevokeGuestError](doc:ios-ref-revokeguesterror) | enum |
| [SDKError](doc:ios-ref-sdkerror) | enum |
| [SetupError](doc:ios-ref-setuperror) | enum |
| [SyncError](doc:ios-ref-syncerror) | enum |
| [TemporaryDoorcodeInvite](doc:ios-ref-temporarydoorcodeinvite) | struct |
| [UnlockError](doc:ios-ref-unlockerror) | enum |
| [UnlockEvent](doc:ios-ref-unlockevent) | struct |
| [UnlockEventMethod](doc:ios-ref-unlockeventmethod) | enum |
| [UnlockEventsListener](doc:ios-ref-unlockeventslistener) | protocol |
| [UnlockEventStatus](doc:ios-ref-unlockeventstatus) | enum |
| [UnlockFailureReason](doc:ios-ref-unlockfailurereason) | enum |

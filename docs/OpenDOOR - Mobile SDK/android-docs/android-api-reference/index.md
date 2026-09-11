---
title: Android API Reference
excerpt: Public API for OpenDOOR Android SDK 2.1.1
hidden: false
---

Reference for **OpenDOOR Android SDK 2.1.1**, the published Android artifact in the 2.1 series.

```kotlin
implementation("com.door:opendoor.android:2.1.1")
```

Start with [OpenDOOR](doc:android-ref-opendoor) and [DoorClient](doc:android-ref-doorclient). Authenticate the shared client with `setupWithToken`, then retrieve locks and observe unlock events.

## Client

- [DoorClient](doc:android-ref-doorclient)
- [OpenDOOR](doc:android-ref-opendoor)

## Models and events

- [AccessLog](doc:android-ref-accesslog)
- [AccessLogMethod](doc:android-ref-accesslogmethod)
- [AccessLogResult](doc:android-ref-accesslogresult)
- [AccessType](doc:android-ref-accesstype)
- [Duration](doc:android-ref-duration)
- [Guest](doc:android-ref-guest)
- [GuestAccess](doc:android-ref-guestaccess)
- [InAppInvite](doc:android-ref-inappinvite)
- [InviteType](doc:android-ref-invitetype)
- [Lock](doc:android-ref-lock)
- [PasscodeType](doc:android-ref-passcodetype)
- [Period](doc:android-ref-period)
- [TempDoorcodeInvite](doc:android-ref-tempdoorcodeinvite)
- [UnlockEvent](doc:android-ref-unlockevent)
- [UnlockEventMethod](doc:android-ref-unlockeventmethod)
- [UnlockFailureReason](doc:android-ref-unlockfailurereason)

## Listeners

- [LocksListener](doc:android-ref-lockslistener)
- [UnlockEventsListener](doc:android-ref-unlockeventslistener)

## Exceptions

- [BluetoothException](doc:android-ref-bluetoothexception)
- [GuestInvitesException](doc:android-ref-guestinvitesexception)
- [InviteGuestException](doc:android-ref-inviteguestexception)
- [LockActionException](doc:android-ref-lockactionexception)
- [NetworkException](doc:android-ref-networkexception)
- [PayloadError](doc:android-ref-payloaderror)
- [RevokeGuestException](doc:android-ref-revokeguestexception)
- [SDKException](doc:android-ref-sdkexception)
- [SetupException](doc:android-ref-setupexception)
- [SyncException](doc:android-ref-syncexception)

This reference covers the public `core.api` surface of the release artifact. Nested event variants and exception reasons appear on their parent type pages.

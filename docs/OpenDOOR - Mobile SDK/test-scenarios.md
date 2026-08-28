---
title: Test Scenarios
excerpt: >-
  This document outlines best practices for testing the mobile application under
  poor or unstable network conditions to ensure resilience, proper error
  handling and good user experience.
deprecated: false
hidden: false
icon: far fa-magnifying-glass-waveform
metadata:
  robots: index
---
**Objectives**

* Verify the app behaves correctly under slow, unstable or offline conditions.
* Ensure proper loading states and user feedback.
* Confirm graceful error handling (timeouts, 401, 500, no connectivity).
* Validate caching and retry mechanisms.
* Ensure no crashes occur due to network failures.

**Scenarios to Test**

* Slow network connection
* High latency network
* Packet loss
* Complete offline mode
* Switching between WiFi and cellular
* Background → foreground during active request
* Token expiration (401 Unauthorized response)

**Testing on iOS (Using Network Link Conditioner)**

Network Link Conditioner allows simulation of various network conditions directly on iOS devices or simulators.
Enable Network Link Conditioner On iOS Device: **Settings → Developer → Network Link Conditioner**.

* Enable Network Link Conditioner.
* Select a profile such as: 3G, Edge, High Latency DNS, Very Bad Network or create a custom profile.

Recommended profiles for testing:

* Very Bad Network
* 3G
* 100% Loss (for offline simulation)

**Testing on Android**

Android OS doesn’t provide reliable, built-in bandwidth/latency throttling on real devices.

However, one tool that can be used for this is [Charles proxy](https://www.charlesproxy.com/documentation/welcome/). Instructions for [throttling settings](https://www.charlesproxy.com/documentation/proxying/throttling/). Steps for this:

* Put your Android device on the same Wi-Fi.
* Configure the phone’s Wi-Fi to use a manual proxy pointing to your Mac (host + port).
* Install the proxy’s certificate for HTTPS inspection.
* Run your app and test flows under throttled conditions (3G/Edge/High latency/packet loss if supported).

Android Emulator provides built-in network throttling options.

* Open Android Emulator.
* Click Extended Controls (⋮).
* Go to Cellular → Set Network Type (Edge, HSPA, LTE).
* Adjust Speed and Latency manually if needed.
* Use Airplane mode to simulate offline state.

**What to Verify During Testing**

* Loading indicators appear and disappear correctly.
* Retry mechanisms function as expected.
* User receives clear and actionable error messages.
* **401** responses properly trigger logout flow.
* Cached data is shown when available.
* No duplicate API calls on retry.
* App remains responsive (no UI freeze).
* Analytics/logging capture network errors.
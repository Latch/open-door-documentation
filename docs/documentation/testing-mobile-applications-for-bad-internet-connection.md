---
title: Testing mobile applications for various Internet connection
excerpt: >-
  This document outlines best practices for testing the mobile application under
  poor or unstable network conditions to ensure resilience, proper error
  handling, and good user experience.
deprecated: false
hidden: false
metadata:
  robots: index
---
**Objectives**

* Verify the app behaves correctly under slow, unstable, or offline conditions.
* Ensure proper loading states and user feedback.
* Confirm graceful error handling (timeouts, 401, 500, no connectivity).
* Validate caching and retry mechanisms.
* Ensure no crashes occur due to network failures.

<br />

**Scenarios to Test**

* Slow 3G connection
* High latency network
* Packet loss
* Complete offline mode
* Switching between WiFi and cellular
* Background → foreground during active request
* Token expiration (401 Unauthorized response)

<br />

**Testing on iOS (Using Network Link Conditioner)**
Network Link Conditioner allows simulation of various network conditions directly on iOS devices or simulators.
Enable Network Link Conditioner On iOS Device: **Settings → Developer → Network Link Conditioner**.

* Enable Network Link Conditioner.
* Select a profile such as: 3G, Edge, High Latency DNS, Very Bad Network, or create a custom profile.

Recommended profiles for testing:

* Very Bad Network
* 3G
* 100% Loss (for offline simulation)

<br />

**Testing on Android**
Android OS doesn’t provide reliable, built-in bandwidth/latency throttling on real devices. Android Emulator provides built-in network throttling options.

* Open Android Emulator.
* Click Extended Controls (⋮). 
* Go to Cellular → Set Network Type (Edge, HSPA, LTE).
* Adjust Speed and Latency manually if needed.
* Use Airplane mode to simulate offline state.

<br />

**What to Verify During Testing**

* Loading indicators appear and disappear correctly.
* Retry mechanisms function as expected.
* User receives clear and actionable error messages.
* **401** responses properly trigger logout flow.
* Cached data is shown when available.
* No duplicate API calls on retry.
* App remains responsive (no UI freeze).
* Analytics/logging capture network errors.

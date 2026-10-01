---
title: Good Practices
excerpt: Guideline for good practices on using our OpenDOOR Mobile SDK
deprecated: false
hidden: false
icon: far fa-list-check
metadata:
  robots: index
---
[**Cache first strategy**]()

Our mobile SDK is designed for offline first scenario, therefore the integration application can take advantage of this by using a `cache first - network after` data strategy. This means listening for locks via the `listenForLocks` function: it emits the cached locks right away, refreshes them from the network in the background, and then emits the new locks. The stream doesn't report errors, so also call the `fetchLocks` function: it refreshes the locks from the network and fails on an invalid or expired token, even when cached locks exist.

#### iOS code snippet

```swift
let token = /* token fetched from Auth0 */
let client = await OpenDOOR.getInstance()
do {
  try await client.setupWithToken(token: token, includeAllLocks: true)

  // emits the cached locks first, then the refreshed locks
  let locksStream = try client.listenForLocks()
  Task {
    for await locks in locksStream {
      // display locks on UI
    }
  }

  do {
    let fetchedLocks = try await client.fetchLocks()
    // display fetchedLocks on UI
  } catch {
    // show error
    // if error is 401, user should be logged out
    // NetworkError.invalidToken is the 401 error
  }
} catch {
  // show error
  // if error is 401, user should be logged out
  // 401 errors: SetupError.invalidToken, NetworkError.invalidToken
}
```

#### Android code snippet

```kotlin
val token: String = /* token fetched from Auth0 */
val client = OpenDOOR.instance
CoroutineScope(Dispatchers.Main).launch {
  try {
    client.setupWithToken(activity, token, includeAllLocks = true)

    // emits the cached locks first, then the refreshed locks
    launch {
      client.listenForLocks().collect { locks ->
        // display locks on UI
      }
    }

    try {
      val fetchedLocks = client.fetchLocks()
      // display fetchedLocks on UI
    } catch (e: Exception) {
      // show error
      // if error is 401, user should be logged out
      // NetworkException.InvalidTokenException is the 401 error
    }
  } catch (e: Exception) {
    // show error
    // if error is 401, user should be logged out
    // 401 errors: SetupException.InvalidTokenException, NetworkException.InvalidTokenException
  }
}
```
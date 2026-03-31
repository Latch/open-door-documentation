---
title: Good Practices
excerpt: Guideline for good practices on using our OpenDOOR Mobile SDK
deprecated: false
hidden: false
metadata:
  robots: index
---
[**Cache first strategy**]()

Our mobile SDK is designed for offline first scenario, therefore the integration application can take advantage of this by using a `cache first - network after` data strategy. This means usage of data from the SDK cache via the `locks` function and in the background get the new locks via the `fetchLocks` function.

#### iOS code snippet

```swift
let token = /* token fetched from Auth0 */
do {
  let latch = try await Latch.initialize(withToken: token)
  
  let cachedLocks = await latch.locks()
  // display cachedLocks on UI

  do {
    let fetchedLocks = try await latch.fetchLocks()
    // display fetchedLocks on UI
  } catch {
    // show error
    // if error is 401, user should be logged out
    // FetchLocksError.invalidToken is the 401 error
  }
} catch {
  // show error
  // if error is 401, user should be logged out
  // 401 errors: NetworkError.invalidToken, FetchLocksError.invalidToken
}
```

#### Android code snippet

```kotlin
val token: String = /* token fetched from Auth0 */
try {
  val latch = Latch.initialize(token)
	
  val cachedLocks = latch.locks()
  // display cachedLocks on UI

  try {
    val fetchedLocks = latch.fetchLocks()
    // display fetchedLocks on UI  (note: fetchedLocks, not cachedLocks)
  } catch (e: Exception) {
    // show error
    // if error is 401, user should be logged out
    // LocksResult.Error will contain 401
  }
} catch (e: Exception) {
  // show error
  // if error is 401, user should be logged out
  // 401 errors: SetupResult.InvalidToken, LocksResult.Error will contain 401
}
```
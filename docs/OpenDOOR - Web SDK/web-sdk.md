---
title: Web SDK
deprecated: false
hidden: true
metadata:
  robots: index
---
The OpenDOOR Web SDK allows your web application to retrieve the doors a user can unlock and display any available door codes.

This SDK is **data/API-only**. It does **not** render UI for you. Your application is responsible for:

* Authenticating the user
* Rendering the user experience
* Passing a valid JWT access token into the SDK
* Handling token refresh through your backend

**_PLEASE NOTE:_** Partner domains, where the SDK is used, must be registered with our DevOps to whitelist

***

## How It Works

The SDK runs in the browser. Authentication must be handled by your backend because it requires confidential credentials.

At a high level:

1. Your backend sends the user a one-time passcode (OTP)
2. Your backend verifies the OTP and exchanges it for an access token
3. Your backend stores the refresh token securely
4. Your backend returns the access token to the frontend
5. The frontend initializes the SDK with that access token
6. The frontend calls the Devices methods to retrieve locks and door codes
7. When the token expires, the frontend asks your backend for a new access token

```text
Frontend -> Your Backend -> Latch Auth
Frontend -> OpenDOOR Web SDK -> Configured API Base
```

### Important Browser Networking Note

Many web integrations use a same-origin backend proxy in front of the upstream API. This avoids browser cross-origin issues and gives you a controlled integration point in your own environment.

If your deployment is configured to allow your browser origin to call the target API origin directly, the SDK can use its default production API base without additional proxying.

Authentication endpoints must always go through your backend because they require confidential credentials.

***

## Installation

Install the package:

```markdown


// https://www.npmjs.com/package/@dooraccess/opendoor-web-sdk
npm install @dooraccess/opendoor-web-sdk
```

Import the SDK in your frontend application:

```javascript
import { OpenDOORClient } from '@dooraccess/opendoor-web-sdk';
```

***

## Backend Integration

Your backend is responsible for the authentication flow. Do **not** expose confidential credentials such as `client_id`, `client_secret`, or `refresh_token` in browser code.

The examples below assume your application uses server-side session middleware or another secure server-side storage mechanism. Adapt them to your own backend architecture.

### Step 1: Send OTP

Your backend calls the passwordless start endpoint.

```javascript
app.post('/api/door/send-otp', async (req, res) => {
  const response = await fetch('https://auth.prod.latch.com/passwordless/start', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      client_id: process.env.LATCH_CLIENT_ID,
      client_secret: process.env.LATCH_CLIENT_SECRET,
      connection: 'email',
      send: 'code',
      email: req.body.email,
    }),
  });

  if (!response.ok) {
    const body = await response.text();
    return res.status(response.status).send(body);
  }

  res.status(204).send();
});
```

### Step 2: Verify OTP and Exchange for Access Token

Your backend verifies the OTP and exchanges it for an access token.

```javascript
app.post('/api/door/verify-otp', async (req, res) => {
  const response = await fetch('https://auth.prod.latch.com/oauth/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      grant_type: 'http://auth0.com/oauth/grant-type/passwordless/otp',
      client_id: process.env.LATCH_CLIENT_ID,
      client_secret: process.env.LATCH_CLIENT_SECRET,
      username: req.body.email,
      otp: req.body.code,
      realm: 'email',
      audience: 'https://rest.latchaccess.com/access/sdk',
      scope: 'openid profile email offline_access',
    }),
  });

  const data = await response.json();

  if (!response.ok) {
    return res.status(response.status).json(data);
  }

  req.session.refreshToken = data.refresh_token;

  res.json({
    token: data.access_token,
  });
});
```

### Step 3: Refresh Access Token

When the frontend needs a new token, your backend uses the stored refresh token.

```javascript
app.post('/api/door/refresh-token', async (req, res) => {
  const refreshToken = req.session.refreshToken;

  if (!refreshToken) {
    return res.status(401).json({
      error: 'No refresh token available',
    });
  }

  const response = await fetch('https://auth.prod.latch.com/oauth/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      grant_type: 'refresh_token',
      client_id: process.env.LATCH_CLIENT_ID,
      client_secret: process.env.LATCH_CLIENT_SECRET,
      refresh_token: refreshToken,
      audience: 'https://rest.latchaccess.com/access/sdk',
    }),
  });

  const data = await response.json();

  if (!response.ok) {
    return res.status(response.status).json(data);
  }

  if (data.refresh_token) {
    req.session.refreshToken = data.refresh_token;
  }

  res.json({
    token: data.access_token,
  });
});
```

### Backend Responsibilities

Your backend should:

* Send the OTP
* Verify the OTP
* Exchange the OTP for an access token
* Store the refresh token securely
* Refresh the access token when needed
* Return only the access token to the browser

Your backend should **not**:

* Expose `client_secret` in browser code
* Expose `refresh_token` in browser code
* Assume the SDK performs authentication for you

***

## Frontend Setup

Once your frontend receives an access token from your backend, it can initialize the SDK.

### Basic Setup

```javascript
import { OpenDOORClient } from '@dooraccess/opendoor-web-sdk';

const client = new OpenDOORClient({
  token,
});
```

### Recommended Setup with Automatic Token Refresh

```javascript
import { OpenDOORClient } from '@dooraccess/opendoor-web-sdk';

const client = new OpenDOORClient({
  token,
  onTokenExpired: async () => {
    const response = await fetch('/api/door/refresh-token', {
      method: 'POST',
      credentials: 'include',
    });

    if (!response.ok) {
      throw new Error('Failed to refresh token');
    }

    const data = await response.json();
    return data.token;
  },
});
```

If your `onTokenExpired` callback returns a new token, the SDK retries the failed request automatically. If your callback throws or rejects, that error is propagated back to your application so your UI can decide whether to re-authenticate the user or show an error state.

### Optional Configuration

```javascript
const client = new OpenDOORClient({
  token,
  onTokenExpired: async () => {
    const response = await fetch('/api/door/refresh-token', {
      method: 'POST',
      credentials: 'include',
    });

    if (!response.ok) {
      throw new Error('Failed to refresh token');
    }

    const data = await response.json();
    return data.token;
  },
  timeout: 15000,
  maxRetries: 2,
  includeAllDevices: false,
});
```

***

## Devices

The Devices methods return the doors the user can unlock and any available door codes.

### `getLocks()`

Returns all locks available to the current user according to the configured access scope.

```javascript
const locks = await client.getLocks();
```

Example response shape:

```javascript
[
  {
    id: 'device-001',
    name: 'Building Main Entrance',
    buildingId: 'building-123',
    startTime: new Date('2026-04-01T15:00:00.000Z'),
    endTime: new Date('2026-04-04T11:00:00.000Z'),
    doorCode: '4829103',
  },
]
```

### `getLock(lockId)`

Returns a single lock by device UUID.

```javascript
const lock = await client.getLock('device-001');
```

`getLock(lockId)` derives its result from the current device list rather than a dedicated single-lock endpoint. In practice, it performs the same underlying device fetch as `getLocks()` and then selects the matching lock from that result.

### `includeAllDevices`

By default, the SDK retrieves only the credentials generated from accesses granted by the Partner that retrieved the user’s JWT token.

```javascript
const client = new OpenDOORClient({
  token,
});
```

If `includeAllDevices` is `true`, the SDK retrieves all of the user’s credentials for all doors the user can unlock.

```javascript
const client = new OpenDOORClient({
  token,
  includeAllDevices: true,
});
```

### Lock Object

Each lock returned by the SDK has this shape:

```javascript
{
  id: 'device-001',
  name: 'Building Main Entrance',
  buildingId: 'building-123',
  startTime: new Date('2026-04-01T15:00:00.000Z'),
  endTime: new Date('2026-04-04T11:00:00.000Z'),
  doorCode: '4829103',
}
```

Field details:

* `id`: device UUID
* `name`: device name
* `buildingId`: building UUID
* `startTime`: access window start
* `endTime`: access window end, or `null` if no end date is available
* `doorCode`: door code PIN, or `null` if no code is available

***

## Token Management

### `onTokenExpired`

Called when the SDK needs a fresh token.

Your implementation should call your backend and return a new access token.

```javascript
const client = new OpenDOORClient({
  token,
  onTokenExpired: async () => {
    const response = await fetch('/api/door/refresh-token', {
      method: 'POST',
      credentials: 'include',
    });

    if (!response.ok) {
      throw new Error('Failed to refresh token');
    }

    const data = await response.json();
    return data.token;
  },
});
```

### `updateToken(newToken)`

Replaces the current token manually.

```javascript
client.updateToken(newToken);
```

Use this if your application already refreshed the token outside the SDK and wants to update the client directly.

### `isAuthenticated()`

Returns `true` if the current token is still valid according to its `exp` claim.

```javascript
const authenticated = client.isAuthenticated();
```

### `destroy()`

Destroys the client instance. After calling this method, the client should no longer be used.

```javascript
client.destroy();
```

***

## Error Handling

All SDK-specific errors extend `SDKError`.

### `AuthError`

Thrown when authentication fails, the token is invalid, or the SDK cannot automatically refresh an expired token.

### `APIError`

Thrown when the API returns a non-success HTTP response.

### `NetworkError`

Thrown for timeouts, connectivity failures, or other network-level issues.

### `NotFoundError`

Thrown when `getLock(lockId)` cannot find a matching lock in the returned device list.

### `ConfigError`

Thrown when SDK configuration is invalid.

### Example

```javascript
import {
  AuthError,
  APIError,
  ConfigError,
  NetworkError,
  NotFoundError,
  OpenDOORClient,
} from '@dooraccess/opendoor-web-sdk';

try {
  const locks = await client.getLocks();
} catch (error) {
  if (error instanceof AuthError) {
    console.error('Authentication failed or token refresh was not possible');
  } else if (error instanceof APIError) {
    console.error('The API returned an error response');
  } else if (error instanceof NetworkError) {
    console.error('A network or timeout error occurred');
  } else if (error instanceof NotFoundError) {
    console.error('The requested lock was not found');
  } else if (error instanceof ConfigError) {
    console.error('SDK configuration is invalid');
  } else {
    console.error('Unexpected error', error);
  }
}
```

***

## Recommended Integration Pattern

A typical web integration looks like this.

### Backend

* Send OTP
* Verify OTP
* Store refresh token securely
* Refresh access token when needed
* Return only access tokens to the frontend

### Frontend

* Request an access token from your backend
* Initialize `OpenDOORClient`
* Call `getLocks()` or `getLock(lockId)`
* Provide `onTokenExpired` so the SDK can refresh automatically

```javascript
const tokenResponse = await fetch('/api/door/session', {
  credentials: 'include',
});

if (!tokenResponse.ok) {
  throw new Error('Failed to load door session');
}

const tokenData = await tokenResponse.json();

const client = new OpenDOORClient({
  token: tokenData.token,
  onTokenExpired: async () => {
    const refreshResponse = await fetch('/api/door/refresh-token', {
      method: 'POST',
      credentials: 'include',
    });

    if (!refreshResponse.ok) {
      throw new Error('Failed to refresh token');
    }

    const refreshData = await refreshResponse.json();
    return refreshData.token;
  },
});

const locks = await client.getLocks();
```

***

## Security Notes

* Do not expose `client_secret` in browser code
* Do not expose `refresh_token` in browser code
* Store refresh tokens securely on the backend
* Return only access tokens to the frontend
* Treat access tokens as user session credentials
* Use HTTPS in production

***

<br />

## Optional: Generate a Local Reference App with AI

Use this prompt to generate a local mock integration that preserves the real browser/backend architecture required by the OpenDOOR Web SDK.

<Callout icon="💡" theme="info">
  Use this prompt for local prototyping and architecture exploration. Keep the auth and device flows mocked unless you are intentionally replacing the mock backend with your real partner integration.

  The second prompts gives a more robust prototype that includes server side code, with an assumption of close approximation, with actual api calls. Of course, as a prototype, you need to make sure it aligns and meets your due diligence.
</Callout>

<Accordion title="Expand the AI coding prompt: Simple" icon="fa-code">
  <pre>
    Build a compact, production-style reference app that demonstrates how a partner would integrate the OpenDOOR Web SDK using a browser frontend plus a backend layer, but use mocked backend behavior and mocked lock data so the app runs locally with no real credentials, no external API calls, and no CORS issues.

    Use this documentation as reference context:
    [https://opendoor-uwel.readme.io/docs/web-sdk](https://opendoor-uwel.readme.io/docs/web-sdk)

    Do not rely on the URL alone. Follow the constraints in this prompt as the primary source of truth.

    If you cannot access or reliably read that documentation, do not guess. Ask me to paste the relevant sections first. Specifically request:

    1. Installation/import section
    2. SDKConfig/options section
    3. Devices methods section
    4. Token management methods section
    5. Error handling section
    6. Lock object/type shape
    7. Backend auth flow guidance

    Do not generate code that assumes undocumented APIs.

    This should feel like it was written by a strong senior engineer: clean architecture, small modules, minimal surface area, readable code, clear naming, no unnecessary abstractions, no filler, no generated-looking code, no giant files, and no tutorial-style clutter. Optimize for maintainability and clarity.

    Stack:

    * Frontend: React + Vite
    * Backend: Node.js + Express
    * Language: JavaScript
    * Styling: lightweight CSS, clean and intentional, no UI library
    * Keep dependencies minimal

    Primary goal:
    Create a partner-facing starter/reference implementation that models the real browser/backend split required for the OpenDOOR Web SDK, while mocking the auth/token/device flows locally.

    Important constraints:

    * Do not use or teach `baseUrl`
    * Do not call any real external services
    * Do not require real Auth0, real Latch APIs, or real npm publishing setup
    * Mock everything locally
    * Add concise comments only at the replacement points where a partner would swap mock logic for real integration logic
    * The app should teach architecture, not environment-specific wiring

    Functional requirements:

    1. click Send OTP
    2. Backend mocks the OTP send flow
    3. User enters OTP and verifies it
    4. Backend returns a fake access token and stores fake refresh/session state in memory
    5. Frontend transitions into an authenticated state
    6. Frontend fetches mocked locks from the backend
    7. UI supports filtering by:
       * all
       * active
       * expired
    8. UI renders:
       * lock name
       * building ID
       * door code or fallback text
       * access status
       * formatted start/end timestamps
    9. Include loading, empty, and error states
    10. Include token/session status in the UI for demo visibility
    11. Include a mock refresh token endpoint and wire the frontend to use it

    Architecture expectations:

    * Do not build a monolith
    * Separate frontend UI components from API utilities and domain helpers
    * Separate backend routes from mock services/data helpers
    * Keep the folder structure obvious and unsurprising
    * Prefer pure helper functions for data formatting and access-status logic
    * No Redux, no complex state libraries, no unnecessary context usage
    * No class-heavy architecture unless there is a strong reason
    * No magic strings scattered everywhere; centralize constants where appropriate

    Frontend structure should look roughly like this:

    * src/components/AuthPanel.jsx
    * src/components/OtpForm.jsx
    * src/components/LockFilters.jsx
    * src/components/LockList.jsx
    * src/components/LockCard.jsx
    * src/components/StatusBadge.jsx
    * src/lib/api.js
    * src/lib/lock-status.js
    * src/lib/format.js
    * src/App.jsx

    Backend structure should look roughly like this:

    * server/index.js
    * server/routes/auth.js
    * server/routes/locks.js
    * server/services/mock-auth.js
    * server/services/mock-locks.js
    * server/data/locks.js

    Implementation details:

    * Use in-memory state only
    * Do not persist anything
    * Mock OTP rule:
      * any email is accepted
      * OTP value "123456" succeeds
      * anything else returns a clear error
    * Mock refresh flow:
      * if a session exists, return a new fake token
      * otherwise return 401
    * Mock locks endpoint should return a realistic array with:
      * active lock
      * expired lock
      * indefinite-access lock (`endTime: null`)
      * lock with no door code (`doorCode: null`)
    * Date formatting should be human-readable, for example:
      * Apr 23, 2026, 10:30 AM
    * Access status rules:
      * if now is before startTime => upcoming
      * if endTime exists and now is after endTime => expired
      * otherwise => active
    * It is acceptable to expose an "Upcoming" visual state even if the main filters are all / active / expired

    Design expectations:

    * Clean, calm UI
    * Not flashy
    * Strong spacing and hierarchy
    * Avoid default browser-looking forms/buttons
    * Responsive for common laptop widths
    * Simple but polished card layout
    * Status colors should be restrained and legible
    * Use a small set of CSS variables
    * Avoid overdesigned gradients or gimmicks

    Code quality expectations:

    * Comments should be sparse and useful
    * Add comments only where a partner would benefit from understanding what to replace in a real integration
    * Avoid obvious comments
    * Handle failure states explicitly
    * Avoid nested conditional messes
    * Prefer straightforward control flow
    * Keep components focused and easy to scan
    * Do not overfit for extensibility beyond this use case

    Important integration framing:
    This is not just a mock app. It should clearly teach the correct architecture:

    * browser UI does not own confidential auth credentials
    * backend handles OTP/token flows
    * frontend receives an access token
    * frontend then fetches lock data through backend-controlled endpoints in this mock version
    * in a real integration, the mocked auth/token logic would be replaced with real partner backend logic
    * real deployments may require same-origin backend routing or controlled proxying depending on environment and browser networking constraints

    README requirements:
    Write a short, strong README that includes:

    * what this project demonstrates
    * how to run frontend
    * how to run backend
    * mock credentials/OTP behavior
    * available endpoints
    * how this maps to a real OpenDOOR integration
    * exactly which files a partner would replace when moving from mock to real auth/device flows

    Also include a section titled:
    "Swap Mock Logic for Real Integration"

    This section should point to the backend auth/token services and backend lock service as the intended replacement points.

    At the end of the README, add a "Run It" section that explicitly tells the user which commands to run to start the backend server and the frontend dev server.

    Output requirements:

    * Return the full codebase
    * Keep files concise
    * Avoid placeholder TODO spam
    * Make sure the app actually hangs together coherently
    * Prefer code that looks hand-written by an experienced engineer over code that looks generated
  </pre>
</Accordion>
<Accordion title="Expand the AI Coding Prompt: Advanced" icon="fa-code">
  <pre>
    Build a production-ready app that integrates the OpenDOOR Web SDK using a browser frontend and backend layer. This app hits real Latch/Auth0 APIs and uses the real SDK. User substitutes their own
    credentials to run it.

    Use this documentation as reference context:\
    [https://opendoor-uwel.readme.io/docs/web-sdk](https://opendoor-uwel.readme.io/docs/web-sdk)

    Do not rely on the URL alone. Follow the constraints in this prompt as the primary source of truth.

    If you cannot access or reliably read that documentation, do not guess. Ask me to paste the relevant sections first. Specifically request:

    * Installation/import section
    * SDKConfig/options section
    * Devices methods section
    * Token management methods section
    * Error handling section
    * Lock object/type shape
    * Backend auth flow guidance

    Do not generate code that assumes undocumented APIs.

    Stack

    * Frontend: React + Vite
    * Backend: Node.js + Express
    * Language: JavaScript
    * Styling: lightweight CSS, clean and intentional, no UI library
    * Dependencies: minimal (dotenv, express, cors on backend; react, @dooraccess/opendoor-web-sdk on frontend)

    Credentials

    Backend reads LATCH\_CLIENT\_ID and LATCH\_CLIENT\_SECRET from environment variables via dotenv.

    No .env.example file. README documents required variables. Server validates on startup and exits with clear error if missing.

    .gitignore must include .env.

    Primary Goal

    A production-ready implementation that a partner can clone, add credentials, and run against real Latch APIs immediately.

    Constraints

    * No mocks. All auth and device flows hit real APIs.
    * Backend hits real Latch auth endpoints.
    * Frontend uses real @dooraccess/opendoor-web-sdk package.
    * Do not use or teach baseUrl.
    * Comments should be sparse and useful—only where a partner benefits from understanding integration points or error handling rationale.

    Backend Responsibilities

    All routes return JSON. All errors return \{ error: string } with appropriate status codes.

    Endpoints\
    ┌────────┬─────────────────────────┬─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐\
    │ Method │          Path           │                                                         Description                                                         │\
    ├────────┼─────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤\
    │ POST   │ /api/auth/send-otp      │ Calls [https://auth.prod.latch.com/passwordless/start](https://auth.prod.latch.com/passwordless/start)                                                                        │\
    ├────────┼─────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤\
    │ POST   │ /api/auth/verify-otp    │ Calls [https://auth.prod.latch.com/oauth/token](https://auth.prod.latch.com/oauth/token) (passwordless grant). Stores refresh token server-side. Returns access token. │\
    ├────────┼─────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤\
    │ POST   │ /api/auth/refresh-token │ Calls [https://auth.prod.latch.com/oauth/token](https://auth.prod.latch.com/oauth/token) (refresh\_token grant). Returns new access token.                              │\
    ├────────┼─────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤\
    │ POST   │ /api/auth/logout        │ Clears stored refresh token.                                                                                                │\
    └────────┴─────────────────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘\
    Error Handling Requirements

    * Validate request body before calling Latch APIs.
    * Handle Latch API errors: parse response, return meaningful error messages.
    * Handle network failures: timeout, DNS, connection refused.
    * Handle rate limiting: surface retry-after if present.
    * Never expose client\_secret or refresh\_token to browser.
    * Log errors server-side with context (no secrets in logs).

    Startup Validation

    On startup, check for LATCH\_CLIENT\_ID and LATCH\_CLIENT\_SECRET. If missing, print clear message and exit:

    Error: Missing required environment variables.\
    Create server/.env with:\
    LATCH\_CLIENT\_ID=your\_client\_id\
    LATCH\_CLIENT\_SECRET=your\_client\_secret

    Frontend Responsibilities

    * Auth flow UI: email input, send OTP, OTP input, verify
    * On successful auth, initialize OpenDOORClient from @dooraccess/opendoor-web-sdk
    * Wire onTokenExpired to call backend /api/auth/refresh-token
    * Call client.getLocks() to fetch locks from Latch APIs
    * Render locks with filtering: all / active / expired
    * Handle SDK errors by type:
      * AuthError: logout, return to login
      * APIError: display error message
      * NetworkError: display connectivity error
      * NotFoundError: handle gracefully

    Functional Requirements

    * User enters email, clicks Send OTP
    * Backend sends OTP via Latch API
    * User enters OTP, clicks Verify
    * Backend exchanges OTP for tokens, returns access token
    * Frontend initializes OpenDOORClient with token
    * Frontend calls client.getLocks()
    * UI filters: all, active, expired
    * UI displays: lock name, building ID, door code (or "Not available"), access status badge, formatted start/end timestamps
    * States: loading, empty, error
    * Session/token status visible in UI
    * Refresh token flow wired and working

    Access Status Logic

    * now \< startTime: upcoming
    * endTime !== null && now > endTime: expired
    * otherwise: active

    Filters:

    * "all": show everything
    * "active": show active + upcoming
    * "expired": show expired only

    Date Formatting

    Human-readable: Apr 23, 2026, 10:30 AM

    Frontend Structure

    src/\
    components/\
    AuthPanel.jsx\
    OtpForm.jsx\
    LockFilters.jsx\
    LockList.jsx\
    LockCard.jsx\
    StatusBadge.jsx\
    lib/\
    api.js\
    sdk.js\
    lock-status.js\
    format.js\
    App.jsx\
    App.css\
    index.css\
    main.jsx

    Backend Structure

    server/\
    index.js\
    routes/auth.js\
    services/latch.js\
    lib/session.js\
    lib/config.js

    Code Quality

    * Expert-level, concise
    * Small modules, single responsibility
    * Robust error handling with clear messages
    * No nested conditional messes
    * Pure helper functions where possible
    * Constants centralized, no magic strings
    * Comments only where they add value for integration understanding

    .gitignore

    Must include:

    node\_modules\
    dist\
    .DS\_Store\
    \*.log\
    .env

    README Requirements

    * What this project is
    * Prerequisites: Node 18+, npm, Latch partner credentials
    * Setup: how to create .env with required variables
    * Run: commands for backend and frontend
    * Endpoints: table of available API routes
    * Architecture: brief explanation of browser/backend split and why
    * SDK usage: how frontend initializes and uses OpenDOORClient
    * Getting credentials: "Contact your Latch partner representative" or relevant portal link if known

    Run It

    1. Configure credentials

    Create server/.env with:

    LATCH\_CLIENT\_ID=your\_client\_id\
    LATCH\_CLIENT\_SECRET=your\_client\_secret

    2. Start backend

    cd server && npm install && npm start

    Runs at [http://localhost:3001](http://localhost:3001)

    3. Start frontend

    npm install && npm run dev

    Runs at [http://localhost:5173](http://localhost:5173)

    4. Use the app

    * Enter your email
    * Check email for OTP
    * Enter OTP to authenticate
    * View and filter your locks

    Output Requirements

    * Full codebase, all files
    * Concise, no filler
    * Production-ready error handling
    * Code that looks hand-written by an expert, not generated
  </pre>
</Accordion>

<br />

<br />

<br />

<br />

## Summary

To integrate the OpenDOOR Web SDK successfully:

1. Build the authentication flow on your backend
2. Return an access token to the frontend
3. Initialize the SDK in the browser
4. Call the Devices methods to retrieve locks and door codes
5. Implement automatic token refresh through `onTokenExpired`

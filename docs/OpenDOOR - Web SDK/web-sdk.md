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

```javascript
Frontend -> Your Backend -> Latch Auth
Frontend -> OpenDOOR Web SDK -> Configured API Base
```

### Important Browser Networking Note

The SDK makes its device/lock requests from the browser to the configured API base.

In the standard production setup, that is the Latch API. This works only if the target origin allows the browser origin that is hosting your application.

If your browser origin is not allowed to call the target API origin directly, you must route SDK traffic through a same-origin backend proxy instead.

Authentication endpoints must always go through your backend because they require confidential credentials.

***

## Installation

Install the package:

```javascript
npm install @dooraccess/opendoor-web-sdk
```

Import the SDK in your frontend application:

```javascript
import { OpenDOORClient } from '@dooraccess/opendoor-web-sdk';
```

***

## Backend Integration

Your backend is responsible for the authentication flow. Do **not** expose confidential credentials such as `client_id`, `client_secret`, or `refresh_token` in browser code.

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

```js
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

### `includeAllDevices`

The `includeAllDevices` option controls which credentials are returned.

If `includeAllDevices` is `true`, the SDK retrieves **all** of the user’s credentials for all doors the user can unlock.

```javascript
const client = new OpenDOORClient({
  token,
  includeAllDevices: true,
});
```

If `includeAllDevices` is `false`, the SDK retrieves only the credentials generated from accesses granted by the Partner that retrieved the user’s JWT token.

```javascript
const client = new OpenDOORClient({
  token,
  includeAllDevices: false,
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
try {
  const locks = await client.getLocks();
} catch (error) {
  if (error.name === 'AuthError') {
    console.error('Authentication failed or token refresh was not possible');
  } else if (error.name === 'APIError') {
    console.error('The API returned an error response');
  } else if (error.name === 'NetworkError') {
    console.error('A network or timeout error occurred');
  } else if (error.name === 'NotFoundError') {
    console.error('The requested lock was not found');
  } else if (error.name === 'ConfigError') {
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

## Summary

To integrate the OpenDOOR Web SDK successfully:

1. Build the authentication flow on your backend
2. Return an access token to the frontend
3. Initialize the SDK in the browser
4. Call the Devices methods to retrieve locks and door codes
5. Implement automatic token refresh through `onTokenExpired`

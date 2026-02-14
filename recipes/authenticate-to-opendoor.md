---
title: Authenticate to OpenDOOR
description: Recipe Description
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```json JSON
curl --request POST \
  --url https://api.prod.door.com/door-api/v1/auth/token \
  --header 'User-Agent: OpenDoor/1.0' \
  --header 'Content-Type: application/json' \
  --data '{"email": "YOUR.EMAIL@EXAMPLE.COM", "password": "YOUR-PASSWORD"}'

```

```json Response Example
{
  "accessToken": "YOUR-ACCESS-TOKEN-HERE",
  "refreshToken": "YOUR-REFRESH-TOKEN-HERE",
  "sessionUser": {
    "uuid": "YOUR-USER-ID",
    "email":"YOUR.EMAIL@EXAMPLE.COM",
    "firstName": "FIRSTNAME",
    "lastName": "LASTNAME",
    "phoneNumber": "PHONE",
    "isPhoneNumberVerified":true,
    "profileUrl":""
  }
}

```

# Log In Programatically

<!-- json@ -->

Run this command to log in to the OpenDOOR API. The response will include both an an access token and a refresh token.

# Extract the Access Token

<!-- json@ -->


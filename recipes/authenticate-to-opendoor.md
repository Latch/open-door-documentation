---
title: Authenticate to OpenDOOR
description: Recipe Description
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```shell Shell
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

# Programatically Log In

<!-- shell@ -->

Run this command to log in to the OpenDOOR API. The response will include both an an access token and a refresh token.
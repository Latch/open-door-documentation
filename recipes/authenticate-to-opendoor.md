---
title: Authenticate to OpenDOOR
description: >-
  The easiest way to log in to the OpenDOOR API is to log in to Door OS and copy
  the token from the "Authorization" header, using the Dev Tools in your
  browser.


  Once done with experimentation, however, it is important to automate this
  step. This can be done by sending a request to the token endpoint.
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
  --data '{"email": "YOUR.EMAIL@EXAMPLE.COM", "password": "YOUR-PASSWORD"}' |
jq -r .accessToken
```

```json Response Example
# curl output:
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

# jq output:
YOUR-ACCESS-TOKEN-HERE

```

# Log In Programatically

<!-- shell@1-5 -->

Run this command to log in to the OpenDOOR API. The response will include both an an access token and a refresh token.

# Extract the Access Token using jq

<!-- shell@6 -->

Install the jq command line tool to automatically extract the access token.
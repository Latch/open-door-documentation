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
{"success":true}
```

# Obtain an Access Token

<!-- shell@ -->


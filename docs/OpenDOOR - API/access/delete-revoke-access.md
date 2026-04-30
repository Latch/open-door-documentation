---
title: Revoke Access
excerpt: >-
  Partners can revoke user access to given doors. This will be done by using a
  partner-scoped token from the BE.
deprecated: false
hidden: false
metadata:
  robots: index
---
<br />

<Callout icon="circle-info" theme="info">
  Revoking a key that contains multiple doors will revoke access to all door.
</Callout>

### Request

DELETE from the Partner BE to the Latch BE with an empty body request.

```
DELETE https://rest.latchaccess.com/access/sdk/v1/users/:user/doors/:door
```

HTTP Headers

```
Authorization: Bearer {{access_token}}
```

HTTP Request Body

```
<empty>
```

### Response

HTTP Response Body

```
<empty>
```

If the request was successful, the Partner BE will receive an HTTP 200 and an empty body response. In case of an error, the API will return the following error responses:

* `404 Not Found`: invalid user or door UUIDs.

  ⇒ Check the user and door identifiers.

* `401 Unauthorized`: missing or invalid access token.

  ⇒ Check the token hasn't expired and refresh the token if needed.

* `500 Internal Server Error`: there was an unexpected error.

  ⇒ Contact Latch Support

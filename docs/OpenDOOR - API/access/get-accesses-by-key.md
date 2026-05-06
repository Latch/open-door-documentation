---
title: Get Accesses By Key
deprecated: false
hidden: false
metadata:
  robots: index
---
<br />

### Prerequisites - Setup Keys

You will need the `keyUuid` for the key you want to inspect.  
This value can be retrieved from the **List Keys** endpoint. You can also create the key in **DOOR OS** and mark it as enabled for this partner.

### Request

Partners can fetch all accesses associated with a specific key using a **partner-scoped token** from their backend.

GET request from the Partner BE to the Open Door with an empty body request.

```http
GET https://rest.latchaccess.com/access/sdk/v1/keys/{keyUuid}/accesses
```

HTTP Path Parameters

```text
keyUuid: "<string>"            (required key UUID)
```

HTTP Headers

```text
Authorization: Bearer {{access_token}}
```

### Response

HTTP Response Body

```json
{
  "accesses": [
    {
      "keyUuid": "<string>",
      "userUuid": "<string>",
      "passcodeType": "<string>",
      "role": "<string>",
      "shareable": false,
      "startTime": "<datetime>",   // e.g. "2022-09-30T15:11:02.537Z"
      "endTime": "<datetime>",     // e.g. "2022-09-30T15:11:02.537Z"
      "granter": {
        "type": "<string>",
        "uuid": "<string>"
      },
      "doors": [
        {
          "sdkDoorUuid": "<string>",
          "doorcode": {
            "code": "<string>",
            "description": "<string>"
          }
        }
      ]
    }
  ]
}
```

If the request was successful, the Partner BE will receive an HTTP `200` with:

* `accesses`: List of accesses on the specified key.
* Each access includes the user, time window, passcode type, who granted the access, and per-door data in `doors`.

In case of an error, the API may return:

* `400 Bad Request`: Invalid `keyUuid` or malformed request.

  ⇒ Verify the UUID format and request path.

* `401 Unauthorized`: Missing or invalid access token.

  ⇒ Check token validity/expiration and refresh if needed.

* `500 Internal Server Error`: Unexpected backend error.

  ⇒ Retry and contact Door Support if persistent.

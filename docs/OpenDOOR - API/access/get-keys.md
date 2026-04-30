---
title: Get Keys
deprecated: false
hidden: false
metadata:
  robots: index
---
<br />

### Prerequisites - Setup Keys

Before calling this endpoint, the property manager must make specific keys eligible for your partner in DOOR OS.

A key typically represents access rules to one or more doors in a building. Only keys that are enabled for your partner will be returned.

### Request

Partners can fetch the list of keys enabled for them using a **partner-scoped token** from their backend.  
Results can be filtered by `buildingUuid` and paginated.

GET request from the Partner BE to the Latch BE with an empty body request.

```
GET https://rest.latchaccess.com/access/sdk/v1/keys
```

HTTP Query Parameters

```
pageSize: <integer>            (default returns all keys)
pageToken: "<string>"          (default first page)
buildingUuid: "<string>"       (optional filter by building UUID)
```

HTTP Headers

```
Authorization: Bearer {{access_token}}
```

### Response

HTTP Response Body

```
{
  "keys": [
    {
      "uuid": "<string>",
      "keyType": "<string>",
      "name": "<string>",
      "buildingUuid": "<string>",
      "accountUuid": "<string>",
      "startTime": "2019-08-23T21:51:07.587Z",
      "endTime": null

    }
  ],
  "nextPageToken": "<string>"
}
```

If the request was successful, the Partner BE will receive an HTTP `200` with:

* `keys`: List of partner-enabled keys and metadata.
* `nextPageToken`: Token for next page. `null` means no more pages.

In case of an error, the API may return:

* `401 Unauthorized`: Missing or invalid access token.

  ⇒ Check token validity/expiration and refresh if needed.

* `500 Internal Server Error`: Unexpected backend error.

  ⇒ Retry and contact Latch Support if persistent.

<br />

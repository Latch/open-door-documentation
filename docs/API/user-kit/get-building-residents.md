---
title: GET Building Residents
excerpt: >-
  ### Request  Partners can fetch a list of users in a building that are
  residents with active accesses. This will be done by using a partner-scoped
  token from the BE.
deprecated: false
hidden: false
metadata:
  robots: index
---
### Request

GET residents request from the Partner BE to the Latch BE

```
GET https://rest.latchaccess.com/access/sdk/v1/buildings/:building/residents
```

HTTP Query Parameters

```
pageSize: <integer> (default is 100)
pageToken: "<string>" (default is "0", first page)
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
{
  "residents": [
    {
      "email": "<string>",
      "firstName": "<string>",
      "lastName": "<string>",
      "userUuid": "<string>",
      "phone": "<string>"
    },
    ...
  ],
  "nextPageToken": "<string>"
}
```

If the request was successful, the Partner BE will receive an HTTP 200 containing a list of Resident objects, with the following fields:

* `email`: Email address associated with the user.
* `firstName`: First name of the user.
* `lastName`: Last name of the user.
* `userUuid`: Unique identifier of the user.
* `phone`: Phone number of the user. Nullable field.
* `nextPageToken`: Token to fetch the next page. Expected value is `null` when there is no next page.

In case of an error, the API will return the following error responses:

* `401 Unauthorized`: missing or invalid access token.

  ⇒ Check the token hasn't expired and refresh the token if needed.

* `500 Internal Server Error`: there was an unexpected error.

  ⇒ Contact Latch Support

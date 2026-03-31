---
title: Get Buildings
excerpt: >-
  Partners can fetch a list of their Buildings. This will be done by using a
  partner-scoped token from the BE.
deprecated: false
hidden: false
metadata:
  robots: index
---
### Request

GET request from the Partner BE to the Latch BE with an empty body request

```
GET https://rest.latchaccess.com/access/sdk/v1/buildings
```

HTTP Headers

```
Authorization: Bearer {{access_token}}
```

HTTP Request Body

```
<empty>
```

HTTP Response Body

```
{
    "buildings": [
      {
         "uuid": "<string>",
         "name": "<string>",
         "address": {
           "addressLine1": "<string>",
           "addressLine2": "<string>",
           "addressLine3": "<string>",
           "city": "<string>",
           "country": "<string>",
           "postalCode": "<string>",
           "state": "<string>",
           "portfolio": {
             "uuid": "<string>",
             "name": "<string>"
           },
           "timezone": "<string>"
         }
      },
      ...
    ]
}
```

### Response

If the request was successful, the Partner BE will receive an HTTP 200 with the following fields:

* `buildings`: List of "buildings" and their metadata. Each entry will include:
  * `uuid`: Unique-identifier of the building.
  * `name`: Name of the building.
  * `address`: Location the building is located.
  * `portfolio`: Includes the name and uuid of the portfolio the building is part of.
  * `timezone`: Timezone the building is in. Format is "Area/Location" (e.g. "America/New_York") based on the TZ identifier from [https://en.wikipedia.org/wiki/List_of_tz_database_time_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

In case of an error, the API will return the following error responses:

* `401 Unauthorized`: missing or invalid access token.

  ⇒ Check the token hasn't expired and refresh the token if needed.

* `500 Internal Server Error`: there was an unexpected error.

  ⇒ Contact Latch Support

---
title: GET Doors
deprecated: false
hidden: false
metadata:
  robots: index
---
### Prerequisites - Setup Doors

The first step is for the customer to select which "doors" (as presented in DOOR OS) can be eligible to be used programmatically by a given partner.

After selecting a door, the property manager will select the partner from the dropdown, making it eligible for partners to use it via the APIs.

### Request

Partners can fetch a list of all the doors that are enabled for them, by using a partner-scoped token from the BE.
It is possible to filter results by Building UUID.

GET request from the Partner BE to the Latch BE with an empty body request

```
GET https://rest.latchaccess.com/access/sdk/v1/doors
```

HTTP Query Parameters

```
pageSize: <integer>   (by default returns all doors)
pageToken: "<string>" (default is "1", first page)
buildingUuid: "<string>" (for filtering results by the Building UUID)
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
  "doors": [
    {
        "uuid": "<string>",
        "name": "<string>",
        "type": "DOOR" | "ELEVATOR",
        "buildingUuid": "<string>",
        "accessibilityType": "COMMUNAL | "PRIVATE",
        "isConnected": <boolean>,
        "device": {
            "serialNumber": "<string>",
            "type": "<string>",
            "battery": {
                "percentage": <int32>,
                "lastUpdated": <int64>
            }
        }
    },
    ...
  ],
  "nextPageToken": "<string>"
}
```

If the request was successful, the Partner BE will receive an HTTP 200 with the following fields:

* `doors`: List of "doors" and their metadata. Each entry will include:
  * `uuid`: Unique-identifier of the door.
  * `name`: Name of the door.
  * `type`: Type of door. Possible values: "DOOR" or "ELEVATOR".
  * `buildingUuid`: Unique-identifier of the building where the door is located.
  * `accessibilityType`: Indicates whether its a communal (entrance, amenities, etc.) or private door (e.g. unit)
  * `isConnected`: Indicates connection status of the door. If internet or hub connected, field is set to `true`.
  * `device`: Includes additional metadata about the physical lock device. **If null, it indicates the door is not yet activated.**
    * `serialNumber`: Serial number of the device.
    * `type`: Type of device. Possible values: 'M', 'R', 'R2', 'C', 'G'
    * `battery`: Battery information with the following fields:
      * `percentage`: Estimated percentage of battery left on the device.
      * `lastUpdated`: Indicates the last time the battery percentage was updated.
* `nextPageToken`: Token to fetch the next page. Expected value is `null` when there is no next page.

In case of an error, the API will return the following error responses:

* `401 Unauthorized`: missing or invalid access token.

  ⇒ Check the token hasn't expired and refresh the token if needed.

* `500 Internal Server Error`: there was an unexpected error.

  ⇒ Contact Latch Support
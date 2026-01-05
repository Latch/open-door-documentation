---
title: 2. Directory Locks Setup
excerpt: POST Lock to Directory Associations.
deprecated: false
hidden: false
metadata:
  robots: index
---
Associate a Cortex Lock to an OpenDOOR Directory Item.

#### Request definition:

| **Method** | **Host**                                               | **Path**                     |
| ---------- | ------------------------------------------------------ | ---------------------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/access/v1/directory-locks` |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: TBD
* **`Content-Type`**: `application/json`

**Request Body:**

Should have the following two JSON properties:

* `directoryItemId`: the target OpenDOOR Directory Item, identified through OpenDOOR ID, the Lock will be assigned to
* `lockId`: the Cortex Lock ID

<Callout icon="📝" theme="default">
  **Note:** `lockId` must not be used in another Lock → Directory Item association already, for a successful current request.
</Callout>

```json Request Body
{
  "directoryItemId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "lockId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

### Example Usage

We'll be using data from [1. Directory Setup → Property Setup → Individual Property Creation → Step 4: Retrieve the entire Directory Subtree](https://opendoor-uwel.readme.io/docs/individual-property-creation#step-4-retrieve-the-entire-directory-subtree):

* `directoryItemId` = `640cb5fe-8d15-4cf0-a632-8f40e11db7f5` (Parking Lot Entrance)
* `lockId` = `AF2D7307-377C-416F-94BD-C81DB311DE19`

#### Request:

```curl cURL
curl -X 'POST' \
  'https://api.blueprint.qa.door.com/access/v1/directory-locks' \
  -H 'accept: */*' \
  -H 'x-door-auth: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
  "directoryItemId": "640cb5fe-8d15-4cf0-a632-8f40e11db7f5",
  "lockId": "AF2D7307-377C-416F-94BD-C81DB311DE19"
}'
```

#### Response:

Status code should be HTTP 200 and Response Body should be the same as the Request Body.

```json Response Body
{
  "directoryItemId": "640cb5fe-8d15-4cf0-a632-8f40e11db7f5",
  "lockId": "af2d7307-377c-416f-94bd-c81db311de19"
}
```

---
title: 2. Directory Locks Setup
excerpt: POST Lock to Directory Associations.
deprecated: false
hidden: false
metadata:
  robots: index
---
<Callout icon="📝" theme="info">
  **Step 1/5 of Granting User Access to Doors:** This step is part of the process to grant users access to open doors within the property. User Access to Door Directory Items is determined by Directory Locks, Access Paths, Permission Sets, Roles and Role Assignments.
</Callout>

Associate physical Latch Cortex Locks with OpenDOOR Directory Items of `ENTRANCE` type, that represent Doors within the property.

#### Request definition:

| **Method** | **Host**                                               | **Path**                     |
| ---------- | ------------------------------------------------------ | ---------------------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/access/v1/directory-locks` |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: Bearer Token
* **`Content-Type`**: `application/json`

**Request Body:**

The Request Body should include the following JSON properties:

* `directoryItemId`: The target OpenDOOR Directory Item, identified through OpenDOOR ID, to which the Lock will be assigned.
* `lockId`: The Latch Cortex Lock ID.

<Callout icon="📝" theme="default">
  **Note:** The `lockId` must not be used in another Lock → Directory Item associationfor the current request to be successful.
</Callout>

```json Request Body Structure
{
  "directoryItemId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "lockId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

### Example Usage

We'll use as an example data from [1. Directory Setup → Property Setup → Individual Property Creation → Step 4: Retrieve the entire Directory Subtree](https://opendoor-uwel.readme.io/docs/individual-property-creation#step-4-retrieve-the-entire-directory-subtree):

* `directoryItemId` = `640cb5fe-8d15-4cf0-a632-8f40e11db7f5` (Parking Lot Entrance)
* `lockId` = `AF2D7307-377C-416F-94BD-C81DB311DE19`

#### Request

```curl cURL
curl -X 'POST' \
  'https://api.prod.door.com/access/v1/directory-locks' \
  -H 'accept: */*' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
  "directoryItemId": "640cb5fe-8d15-4cf0-a632-8f40e11db7f5",
  "lockId": "AF2D7307-377C-416F-94BD-C81DB311DE19"
}'
```

#### Response

The status code should be HTTP 200, and the Response Body should match the Request Body.

```json Response Body
{
  "directoryItemId": "640cb5fe-8d15-4cf0-a632-8f40e11db7f5",
  "lockId": "af2d7307-377c-416f-94bd-c81db311de19"
}
```
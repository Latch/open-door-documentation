---
title: 5. Permission Sets Setup
excerpt: POST Permission Set.
deprecated: false
hidden: false
metadata:
  robots: index
---
<br />

<Callout icon="📝" theme="default">
  **Step 3/5 of Granting User Access To Doors:** This step is part of the process to grant users access to open doors. User access is determined by Permission Sets, access to the associated Directory Item,  Access Paths, Roles and Role Assignments.
</Callout>

Create Sets of Permissions that define the capabilities Roles will have.

#### Request definition:

| **Method** | **Host**                                               | **Path**                   |
| ---------- | ------------------------------------------------------ | -------------------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/rbac/v1/permission-sets` |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: Bearer Token
* **`Content-Type`**: `application/json`

**Request Body:**

Include the following JSON properties:

* `locationDirectoryItemId`: Directory Item ID where the Permission Set is applicable. It can be your Root Directory Item, allowing application to sub-Directories.
* `name`: Name of the Permission Set.
* `permissions`: A String array containing OpenDOOR Permissions.

```json Request Body Structure
{
  "locationDirectoryItemId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "string",
  "permissions": [
    "MANAGE_DIRECTORY"
  ]
}
```

### Example Usage

Using Root Directory Item `OpenDOOR Client Account` (ID `e43f4017-da92-4c4a-87ff-5c5f418c3cf6`) from [1. Directory Setup → Property Setup → Individual Property Creation → Step 4: Retrieve the entire Directory Subtree](https://opendoor-uwel.readme.io/docs/individual-property-creation#step-4-retrieve-the-entire-directory-subtree-1) as `locationDirectoryItemId`, we'll create a Staff level Permission Set with Permissions for:

* Reaching, Entering and Accessing Spaces
* Viewing Units
* Viewing Directories
* Inviting, Viewing and Revoking Guest Access
* Viewing Resident Assignments

#### Request

```curl
curl -X 'POST' \
  'https://api.prod.door.com/rbac/v1/permission-sets' \
  -H 'accept: */*' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
  "locationDirectoryItemId": "e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
  "name": "OpenDOOR Staff Permission Set",
  "permissions": [
    "ENTER_SPACE",
    "ACCESS_SPACE",
    "REACH_SPACE",
    "ACCESS",
    "VIEW_DIRECTORY",
    "VIEW_UNIT",
    "INVITE_REVOKE_GUEST",
    "VIEW_GUEST_ROLE_ASSIGNMENTS",
    "VIEW_RESIDENT_ROLE_ASSIGNMENTS",
    "REVOKE_ANY_GUEST"
  ]
}'
```

#### Response

The status code should be HTTP 200 and Response Body match the Request Body, but with an additional `id` property.

```json Response Body
{
  "id": "d67d8a3e-4f10-4e4d-86ae-031c0ee2229e",
  "locationDirectoryItemId": "e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
  "name": "OpenDOOR Staff Permission Set",
  "permissions": [
    "ENTER_SPACE",
    "ACCESS_SPACE",
    "REACH_SPACE",
    "ACCESS",
    "VIEW_DIRECTORY",
    "VIEW_UNIT",
    "INVITE_REVOKE_GUEST",
    "VIEW_GUEST_ROLE_ASSIGNMENTS",
    "VIEW_RESIDENT_ROLE_ASSIGNMENTS",
    "REVOKE_ANY_GUEST"
  ]
}
```

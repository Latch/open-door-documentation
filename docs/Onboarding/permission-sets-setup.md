---
title: 4. Permission Sets Setup
excerpt: POST Custom Permission Set.
deprecated: false
hidden: false
metadata:
  robots: index
---
Creates custom Permission Sets.

#### Request definition:

| **Method** | **Host**                                               | **Path**                   |
| ---------- | ------------------------------------------------------ | -------------------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/rbac/v1/permission-sets` |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: TBD
* **`Content-Type`**: `application/json`

**Request Body:**

Should have the following three JSON properties:

* `locationDirectoryItemId`: Directory Item ID the Permission Set will be usable in. It can your Root Directory Item, so Permission Set can be applied to the sub-Directories.
* `name`: Name of the Permission Set.
* `permissions`: A String array containing OpenDOOR Permissions.

```json Request Body
{
  "locationDirectoryItemId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "string",
  "permissions": [
    "MANAGE_DIRECTORY"
  ]
}
```

### Example Usage

We'll be using Root Directory Item `OpenDOOR Client Account` (ID `e43f4017-da92-4c4a-87ff-5c5f418c3cf6`) from [1. Directory Setup → Property Setup → Individual Property Creation → Step 4: Retrieve the entire Directory Subtree](https://opendoor-uwel.readme.io/docs/individual-property-creation#step-4-retrieve-the-entire-directory-subtree-1) as `locationDirectoryItemId`.

We'll be creating a Staff level Permission Set with Permissions for:

* Viewing & Managing Directory
* Configuring Access
* Inviting, Viewing and Revoking Guests, Residents and Vendors
* View & Manage Locks
* Manage Roles

#### Request

```curl
curl -X 'POST' \
  'https://api.blueprint.qa.door.com/rbac/v1/permission-sets' \
  -H 'accept: */*' \
  -H 'x-door-auth: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
  "locationDirectoryItemId": "e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
  "name": "OpenDOOR Property Manager Permission Set",
  "permissions": [
    "MANAGE_DIRECTORY",
    "VIEW_DIRECTORY",
    "CONFIGURE_ACCESS",
    "INVITE_REVOKE_GUEST",
    "INVITE_REVOKE_RESIDENT",
    "INVITE_REVOKE_VENDOR",
    "VIEW_GUEST_ROLE_ASSIGNMENTS",
    "VIEW_RESIDENT_ROLE_ASSIGNMENTS",
    "VIEW_VENDOR_ROLE_ASSIGNMENTS",
    "REVOKE_ANY_GUEST",
    "REVOKE_ANY_RESIDENT",
    "REVOKE_ANY_VENDOR",
    "VIEW_LOCKS",
    "MANAGE_LOCKS",
    "MANAGE_ROLES"
  ]
}'
```

#### Response

Status code should be HTTP 200 and Response Body should be the same as the Request Body, but with an additional JSON property, `id`.

```json Response Body
{
  "id": "d67d8a3e-4f10-4e4d-86ae-031c0ee2229e",
  "locationDirectoryItemId": "e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
  "name": "OpenDOOR Property Manager Permission Set",
  "permissions": [
    "MANAGE_DIRECTORY",
    "VIEW_DIRECTORY",
    "CONFIGURE_ACCESS",
    "INVITE_REVOKE_GUEST",
    "INVITE_REVOKE_RESIDENT",
    "INVITE_REVOKE_VENDOR",
    "VIEW_GUEST_ROLE_ASSIGNMENTS",
    "VIEW_RESIDENT_ROLE_ASSIGNMENTS",
    "VIEW_VENDOR_ROLE_ASSIGNMENTS",
    "REVOKE_ANY_GUEST",
    "REVOKE_ANY_RESIDENT",
    "REVOKE_ANY_VENDOR",
    "VIEW_LOCKS",
    "MANAGE_LOCKS",
    "MANAGE_ROLES"
  ]
}
```

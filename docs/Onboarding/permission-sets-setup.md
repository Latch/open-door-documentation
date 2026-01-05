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

| **Method** | **Host**                                               | **Path**                    |
| ---------- | ------------------------------------------------------ | --------------------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/access/v1/paths/segments` |

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

<br />

### Example Usage:

We'll be using Root Directory Item `OpenDOOR Client Account` (ID `e43f4017-da92-4c4a-87ff-5c5f418c3cf6`) from [1. Directory Setup → Property Setup → Individual Property Creation → Step 4: Retrieve the entire Directory Subtree](https://opendoor-uwel.readme.io/docs/individual-property-creation#step-4-retrieve-the-entire-directory-subtree-1) as `locationDirectoryItemId`.

<br />

<br />

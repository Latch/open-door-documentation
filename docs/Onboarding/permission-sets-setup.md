---
title: 4. Permission Sets Setup
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

<br />

sd

```json Request Body
{
  "locationDirectoryItemId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "string",
  "permissions": [
    "MANAGE_DIRECTORY"
  ]
}
```

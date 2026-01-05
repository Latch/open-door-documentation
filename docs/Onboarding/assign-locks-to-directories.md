---
title: 2. Directory Locks Setup
excerpt: POST Lock to Directory Assignments.
deprecated: false
hidden: false
metadata:
  robots: index
---
This request assigns a Cortex Lock to an OpenDOOR Directory Item.

#### Request definition:

| **Method** | **Host**                                               | **Path**                     |
| ---------- | ------------------------------------------------------ | ---------------------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/access/v1/directory-locks` |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: TBD
* **`Content-Type`**: `multipart/form-data`

**Request Body:**

Should contain the two JSON properties:

* `directoryItemId`: the target OpenDOOR Directory Item, identified through OpenDOOR ID, the Lock will be assigned to
* `lockId`: the Cortex Lock ID

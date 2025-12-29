---
title: Individual Property Creation
excerpt: POST Directory Item(s).
deprecated: false
hidden: false
metadata:
  robots: index
---
**Request Definitions:**

| **Method** | **Host**                                               | **Path**                      | Details                                                           |
| :--------- | :----------------------------------------------------- | :---------------------------- | :---------------------------------------------------------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/items`         | Create a Directory Item and its subtree.                          |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/items/{scope}` | Create a Directory Item under the given `scope` (Directory Item). |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: TBD
* **`Content-Type`**: `multipart/form-data`

<br />

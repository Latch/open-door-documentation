---
title: Individual Property Creation
excerpt: POST Directory Item(s).
deprecated: false
hidden: false
metadata:
  robots: index
next:
  pages:
    - slug: assign-locks-to-directories
      title: 2. Directory Locks Setup
      type: basic
---
<br />

<Callout icon="📝" theme="default">
  **How to use below endpoints:**

  1. `/directory/v1/items` to create the initial Directory structure, can even be complete at the moment.
  2. `/directory/v1/items/{scope}` to create additional Directory Items and append them to an existing Item, identified by `scope`.  Can be used to bring additions or complete existing Directory.
</Callout>

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

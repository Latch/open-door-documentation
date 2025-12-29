---
title: Update Directory Items
excerpt: PATCH Directory Item.
deprecated: false
hidden: false
metadata:
  robots: index
---
Request for when you need to update a Directory Item's data, `name` and `tags`:

| **Method** | **Host**                                               | **Path**                     | Details                                               |
| :--------- | :----------------------------------------------------- | :--------------------------- | :---------------------------------------------------- |
| PATCH      | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/items/{uuid}` | Update Directory Item data, identified by its `uuid`. |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: TBD

**Request Body:**

### Example Usage

We'll be using as example `uuid = 972e4151-0f73-4cd5-913e-70dd5fc8ad45` (`ODC Portfolio 1` Directory Item) from [Bulk Import Property Data → Step 3. Validate Response](doc:https://opendoor-uwel.readme.io/docs/migrate-from-legacy-property#step-3-validate-response).

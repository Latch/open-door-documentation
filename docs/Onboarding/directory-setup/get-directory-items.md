---
title: Retrieve Directory Data
deprecated: false
hidden: false
metadata:
  robots: index
---
Below you can find endpoints for retrieving existing Directory data and understanding the current structure of your Directory:

| **Method** | **Host**                                               | **Path**                        | Details                                                       |
| :--------- | :----------------------------------------------------- | :------------------------------ | :------------------------------------------------------------ |
| GET        | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/items/{uuid}`    | Retrieve a single Directory Item using its `uuid`.            |
| GET        | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/subtree`         | Retrieves all Directory Items starting from the root.         |
| GET        | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/subtree/{scope}` | Retrieves all Directory Items starting from the `scope` root. |

**URL parameters (applicable only for listing endpoints `/directory/v1/subtree` and `/directory/v1/subtree/{scope}`):**

* `pageSize`:
* `pageToken`:

**Headers:**

* **Authorization**: TBD
* **Content-Type**: `multipart/form-data`

### Example Usages

We'll be using as example `uuid = 972e4151-0f73-4cd5-913e-70dd5fc8ad45` (`ODC Portfolio 1` Directory Item) from [Bulk Import Property Data → Step 3. Validate Response](doc:https://opendoor-uwel.readme.io/docs/migrate-from-legacy-property#step-3-validate-response).

#### `GET /directory/v1/items/{uuid}` endpoint to retrieve information about a known Directory Item:

**Request:**

```bash
curl -X GET 'https://api.prod.door.com/directory/v1/items/972e4151-0f73-4cd5-913e-70dd5fc8ad45' \
  -H 'Authorization: Bearer {token}' \
  -H 'Accept: */*'
```

**Response:**

```json Response Body
{
  "id": "972e4151-0f73-4cd5-913e-70dd5fc8ad45",
  "name": "ODC Portfolio 1",
  "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45",
  "tags": {
    "space:PORTFOLIO": "",
    "item:SPACE": "",
    "cortex:ACCOUNT": "936037B4-9250-4778-BC81-57660C3A011B"
  },
  "createdAt": "2025-12-22T17:26:19Z",
  "createdBy": {
    "authorType": "USER",
    "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
  }
}
```

#### `GET /directory/v1/subtree/{scope}` endpoint to retrieve information about a known Directory Item:

**Request:**

```bash
curl -X GET 'https://api.prod.door.com/directory/v1/subtree/972e4151-0f73-4cd5-913e-70dd5fc8ad45' \
  -H 'Authorization: Bearer {token}' \
  -H 'Accept: */*'
```

**Response:**

```json Response Body
```

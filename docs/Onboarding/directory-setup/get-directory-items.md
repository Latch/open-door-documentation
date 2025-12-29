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

* `pageSize`: Specify the number of items to be returned in a single page of results when listing Directory Items. It helps control the amount of data retrieved in one request, allowing for efficient data handling and navigation through large datasets.
* `pageToken`: Specify the starting point (ID/UUID) for the next page of data in a paginated list. When combined with pageSize, it allows for efficient navigation through large datasets by fetching subsequent pages of results.

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
curl -X GET 'https://api.prod.door.com/directory/v1/subtree/972e4151-0f73-4cd5-913e-70dd5fc8ad45?pageSize=10' \
  -H 'Authorization: Bearer {token}' \
  -H 'Accept: */*'
```

**Response:**

```json Response Body
{
  "items": [
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
    },
    {
      "id": "2e4a1982-3f4f-4227-8932-77b42a0c524f",
      "name": "ODCP1 Property 2",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::2e4a1982-3f4f-4227-8932-77b42a0c524f",
      "tags": {
        "space:PROPERTY": "",
        "item:SPACE": "",
        "cortex:BUILDING": "251FEC1A-8B28-487C-9D57-E2B843AC51FF"
      },
      "createdAt": "2025-12-22T17:26:19Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "ea41ad14-3e2b-495b-b76a-a194217961cc",
      "name": "ODCP1 Property 1",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc",
      "tags": {
        "space:PROPERTY": "",
        "item:SPACE": "",
        "cortex:BUILDING": "1765CB13-36D6-461A-9ACB-59D1A2CE9BF6"
      },
      "createdAt": "2025-12-22T17:26:19Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9",
      "name": "Residential Building",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9",
      "tags": {
        "space:BUILDING": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-22T17:26:19Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "17cde9b1-0986-4869-a81b-5797cc7480ef",
      "name": "Floor 3",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::17cde9b1-0986-4869-a81b-5797cc7480ef",
      "tags": {
        "space:FLOOR": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-22T17:26:19Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "86a4196a-c754-4531-8532-21c2c0854edc",
      "name": "Floor 3 - Unit 301",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::17cde9b1-0
```

<br />

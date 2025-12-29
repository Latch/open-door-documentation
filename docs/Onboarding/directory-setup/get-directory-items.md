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

### Example Usages

#### `GET /directory/v1/items/{uuid}` endpoint to retrieve information about a known Directory Item:

**Request:**

```bash
curl -X GET 'https://api.prod.door.com/directory/v1/items/{uuid}' \
  -H 'Authorization: Bearer {token}' \
  -H 'Accept: application/json'
```

**Response:**

```json Response Body
```

#### `GET /directory/v1/subtree/{scope}` endpoint to retrieve information about a known Directory Item:

**Request:**

```bash
curl -X GET 'https://api.prod.door.com/directory/v1/subtree/{scope}' \
  -H 'Authorization: Bearer {token}' \
  -H 'Accept: application/json'
```

**Response:**

<br />

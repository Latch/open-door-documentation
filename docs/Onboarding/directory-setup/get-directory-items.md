---
title: Retrieve Directory Data
deprecated: false
hidden: false
metadata:
  robots: index
---
Below you can find endpoints for retrieving existing Directory data and understanding the current structure of your Directory:

1. **GET /directory/accounts**: Retrieve a list of all accounts in the Directory.
2. **GET /directory/portfolios**: Access information about all portfolios.
3. **GET /directory/properties**: Fetch details of properties within a portfolio.
4. **GET /directory/buildings**: Obtain data on buildings associated with a property.
5. **GET /directory/units**: Get information on individual units within a building.

<br />

| **Method** | **Host**                                               | **Path**                        | Details                                                       |
| :--------- | :----------------------------------------------------- | :------------------------------ | :------------------------------------------------------------ |
| GET        | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/items/{uuid}`    | Retrieve a single Directory Item using its `uuid`             |
| GET        | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/subtree`         | Retrieves all Directory Items starting from the root.         |
| GET        | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/subtree/{scope}` | Retrieves all Directory Items starting from the `scope` root. |

### Example Usages

#### `GET /directory/v1/items/{uuid}` endpoint to retrieve information about a known Directory Item: 

Request: 

```bash
curl -X GET 'https://api.prod.door.com/directory/accounts' \
  -H 'Authorization: Bearer {token}' \
  -H 'Accept: application/json'
```

Response:

```json Response Body
```

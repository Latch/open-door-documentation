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
* **`Authorization`**: Bearer Token
* **`Content-Type`**: `application/json`

**Request Body:** Specify the data you want to update: `name`, `tags` or both, in JSON format.

### Example Usage

We'll be using as an example `Floor 2 - Unit 201` Directory Item (ID `ca461e44-715b-46ce-8056-a68693584a07`) from [1. Directory Setup → Property Setup → Automate Property Creation with the API → Create Entire Directory Structure in One Request → Step 3. Validate Response](doc:https://opendoor-uwel.readme.io/docs/migrate-from-legacy-property#step-3-validate-response).

#### 1. Request

```curl
curl -X 'PATCH' \
  'https://api.prod.door.com/directory/v1/items/ca461e44-715b-46ce-8056-a68693584a07' \
  -H 'accept: */*' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "[UPDATED] Floor 2 - Unit 201",
  "tags": {
    "vacancy:OCCUPIED": "Indefinitely occupied"
  }
}'
```

#### 2. Response

The status code should be HTTP 200, with the following Response Body:

```json Response Body
{
  "id": "ca461e44-715b-46ce-8056-a68693584a07",
  "name": "[UPDATED] Floor 2 - Unit 201",
  "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::75fbca56-8160-475c-9cac-46d06f1091ba::ca461e44-715b-46ce-8056-a68693584a07",
  "tags": {
    "space:UNIT": "",
    "item:SPACE": "",
    "cortex:UNIT": "831440",
    "vacancy:OCCUPIED": "Indefinitely occupied"
  },
  "createdAt": "2025-12-22T17:26:20Z",
  "createdBy": {
    "authorType": "USER",
    "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
  }
}
```

<br />

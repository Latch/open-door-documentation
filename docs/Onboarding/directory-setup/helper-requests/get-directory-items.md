---
title: Retrieve Directory Data
excerpt: GET Directory Item(s).
deprecated: false
hidden: false
metadata:
  robots: index
---
Below you can find endpoints for retrieving existing Directory data and understanding the current structure of your Directory:

| **Method** | **Host**                                               | **Path**                        | Details                                                       |
| :--------- | :----------------------------------------------------- | :------------------------------ | :------------------------------------------------------------ |
| GET        | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/items/{uuid}`    | Retrieve a single Directory Item data using its `uuid`.       |
| GET        | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/subtree/{scope}` | Retrieves all Directory Items starting from the `scope` root. |

**URL parameters:**

<Callout icon="📝" theme="default">
  **Note:** These parameters apply only to the listing endpoint `/directory/v1/subtree/{scope}`. See usage examples in [`GET /directory/v1/subtree/{scope}` endpoint to retrieve information about a known Directory Item](https://opendoor-uwel.readme.io/docs/get-directory-items#2-get-directoryv1subtreescope-endpoint-to-retrieve-information-about-a-known-directory-item-1).
</Callout>

* `pageSize`: Specifies the number of Directory Items to be returned in a single page of results. This helps control the amount of data retrieved in one request, allowing for efficient data handling and navigation through large datasets.
* `pageToken`: Specifies the starting point (ID/UUID) for the next page of data in a paginated list. When combined with pageSize, it allows for efficient navigation through large datasets by fetching subsequent pages of results.

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: Bearer Token

### Example Usages

We'll use as an example `ODC Portfolio 1` Directory Item (ID `972e4151-0f73-4cd5-913e-70dd5fc8ad45`) from [1. Directory Setup → Property Setup → Bulk Import Property Data → Step 3. Validate Response](doc:https://opendoor-uwel.readme.io/docs/migrate-from-legacy-property#step-3-validate-response).

#### 1. `GET /directory/v1/items/{uuid}` Endpoint to Retrieve Information About a Known Directory Item

##### Request

```curl
curl -X GET 'https://api.prod.door.com/directory/v1/items/972e4151-0f73-4cd5-913e-70dd5fc8ad45' \
  -H 'Authorization: Bearer {token}' \
  -H 'accept: */*'
```

##### Response

The status code should be HTTP 200, with the following Response Body:

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

#### 2. `GET /directory/v1/subtree/{scope}` Endpoint to Retrieve Information About Directory Items from a Known Subtree

##### Request

```curl
curl -X GET 'https://api.prod.door.com/directory/v1/subtree/972e4151-0f73-4cd5-913e-70dd5fc8ad45?pageSize=10' \
  -H 'Authorization: Bearer {token}' \
  -H 'accept: */*'
```

##### Response

The status code should be HTTP 200, with the following Response Body:

```json Response Body
{
  "items": [
    {
      "id": "75fbca56-8160-475c-9cac-46d06f1091ba",
      "name": "Floor 2",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::75fbca56-8160-475c-9cac-46d06f1091ba",
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
    },
    {
      "id": "fa16cef9-ca45-43cf-ba08-0d305764f412",
      "name": "Floor 2 - Unit 201 Door",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::75fbca56-8160-475c-9cac-46d06f1091ba::ca461e44-715b-46ce-8056-a68693584a07::fa16cef9-ca45-43cf-ba08-0d305764f412",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "7E8CC077-B07E-4A44-AAA1-1DB05F6D48D2"
      },
      "createdAt": "2025-12-22T17:26:20Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "f8f46e51-1804-4342-b649-5054753e284e",
      "name": "Floor 2 - Unit 210",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::75fbca56-8160-475c-9cac-46d06f1091ba::f8f46e51-1804-4342-b649-5054753e284e",
      "tags": {
        "space:UNIT": "",
        "item:SPACE": "",
        "cortex:UNIT": "831442"
      },
      "createdAt": "2025-12-22T17:26:20Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "bc4ef7ac-c042-4c7a-922a-9909a5a0a25f",
      "name": "Floor 2 - Unit 210 Door",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::75fbca56-8160-475c-9cac-46d06f1091ba::f8f46e51-1804-4342-b649-5054753e284e::bc4ef7ac-c042-4c7a-922a-9909a5a0a25f",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "1DFAC8E4-1192-48C9-B6CD-243C21C47265"
      },
      "createdAt": "2025-12-22T17:26:20Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "b3f10a8b-3cce-49ca-b470-92d0c6e4c656",
      "name": "Common Areas",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656",
      "tags": {
        "space:COMMON_GROUP": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-22T17:26:20Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "76b3cfc1-91b5-483b-b7c3-0daf78a4c7d1",
      "name": "Elevator 2",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::76b3cfc1-91b5-483b-b7c3-0daf78a4c7d1",
      "tags": {
        "space:COMMON_AREA": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-22T17:26:20Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "c3e9f3be-99d3-426e-8678-623da8e28e95",
      "name": "Package Room",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::c3e9f3be-99d3-426e-8678-623da8e28e95",
      "tags": {
        "space:STORAGE_GROUP": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-22T17:26:20Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "1af9dff9-1d1e-4b9e-bcda-ffac894e69c4",
      "name": "Delivery Service Door",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::c3e9f3be-99d3-426e-8678-623da8e28e95::1af9dff9-1d1e-4b9e-bcda-ffac894e69c4",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "C44B0BA4-F048-44EF-85FF-97CDFC7106EF"
      },
      "createdAt": "2025-12-22T17:26:20Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "2bdcdc74-f531-4c78-a4f8-8726c35b05e7",
      "name": "Lockbox 310",
      "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::c3e9f3be-99d3-426e-8678-623da8e28e95::2bdcdc74-f531-4c78-a4f8-8726c35b05e7",
      "tags": {
        "space:STORAGE_SLOT": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-22T17:26:20Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    }
  ],
  "nextPageToken": "eyJTSyI6Ik1FVEFEQVRBIiwiR1NJNVBLIjoiREkjOjoiLCJQSyI6IjJiZGNkYzc0LWY1MzEtNGM3OC1hNGY4LTg3MjZjMzViMDVlNyIsIkdTSTVTSyI6Ijo6OjoyMDE4Yjk0Yi05ZGY1LTQ0NTYtOWM1ZC05ZTk4NDk5M2FmZWU6Ojk3MmU0MTUxLTBmNzMtNGNkNS05MTNlLTcwZGQ1ZmM4YWQ0NTo6ZWE0MWFkMTQtM2UyYi00OTViLWI3NmEtYTE5NDIxNzk2MWNjOjo2MmY1ZjdmMy0wYzAzLTRlNWYtODI5OS0yNWM2ZTNhNGZmZjk6OmIzZjEwYThiLTNjY2UtNDljYS1iNDcwLTkyZDBjNmU0YzY1Njo6YzNlOWYzYmUtOTlkMy00MjZlLTg2NzgtNjIzZGE4ZTI4ZTk1OjoyYmRjZGM3NC1mNTMxLTRjNzgtYTRmOC04NzI2YzM1YjA1ZTcifQ=="
}
```

#### 3. Navigate through Response pages

<Callout icon="📋" theme="info">
  Use `pageSize` and `nextPageToken` to efficiently navigate through paginated response pages. The  `nextPageToken` can be obtained from the above response body and will retrieve you the next page. **Here's how to use it:**

  ```curl
  curl -X 'GET' \
    'https://api.prod.door.com/directory/v1/subtree/972e4151-0f73-4cd5-913e-70dd5fc8ad45?pageToken=eyJTSyI6Ik1FVEFEQVRBIiwiR1NJNVBLIjoiREkjOjoiLCJQSyI6IjRlNWE1YjEwLTBlZDUtNGFjYS1hZmFlLTJhOTRmZDNkMTI3NyIsIkdTSTVTSyI6Ijo6OjoyMDE4Yjk0Yi05ZGY1LTQ0NTYtOWM1ZC05ZTk4NDk5M2FmZWU6Ojk3MmU0MTUxLTBmNzMtNGNkNS05MTNlLTcwZGQ1ZmM4YWQ0NTo6ZWE0MWFkMTQtM2UyYi00OTViLWI3NmEtYTE5NDIxNzk2MWNjOjo2MmY1ZjdmMy0wYzAzLTRlNWYtODI5OS0yNWM2ZTNhNGZmZjk6OjRlNWE1YjEwLTBlZDUtNGFjYS1hZmFlLTJhOTRmZDNkMTI3NyJ9&pageSize=10' \
    -H 'accept: */*' \
    -H 'Authorization: Bearer {token}'
  ```
</Callout>

<br />

---
title: 3. Access Paths Setup
excerpt: POST Access Paths.
deprecated: false
hidden: false
metadata:
  robots: index
---
Creates Access Paths segments/connections between Directory Items.

#### Request definition:

| **Method** | **Host**                                               | **Path**                    |
| ---------- | ------------------------------------------------------ | --------------------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/access/v1/paths/segments` |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: TBD
* **`Content-Type`**: `application/json`

**Request Body:**

Should contain a JSON array, `segments`, made of Objects with two properties:

* `ancestorId`: Ancestor OpenDOOR Directory Item, identified through OpenDOOR ID
* `descendantId`: Descendant OpenDOOR Directory Item, identified through OpenDOOR ID

<Callout icon="📝" theme="default">
  **Note:** While setting up Access Path Segments, be aware that creating cyclic dependencies is not allowed by the system. For instance, attempting to connect `Directory 1000` to `Directory 1010` and then back from `1010` to `1000` will be prevented. Ensure your configurations are free of such loops to comply with system constraints.
</Callout>

```json Request Body
{
  "segments": [
    {
      "ancestorId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "descendantId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ]
}
```

### Example Usages

We'll be using data from [1. Directory Setup → Property Setup → Individual Property Creation → Step 4: Retrieve the entire Directory Subtree](https://opendoor-uwel.readme.io/docs/individual-property-creation#step-4-retrieve-the-entire-directory-subtree-1) to set up Access Path Segments as `Ancestor → Descendant` associations:

1. **`Parking Lot Entrance` (Ancestor) → `Residential Building Entrance` (Descendant):**
   1. `ancestorId` = `640cb5fe-8d15-4cf0-a632-8f40e11db7f5`
   2. `descendantId` = `AF2D7307-377C-416F-94BD-C81DB311DE19`

<Accordion title="1. Segment 1: `Parking Lot Entrance` (Ancestor) → `Residential Building Entrance` (Descendant)" icon="angle-down">
  <ul>
    <li>ancestorId = Directory 1000</li>
    <li>descendantId = Directory 1010</li>
  </ul>
</Accordion>

<Accordion title="2. Segment 2" icon="angle-down">
  <ul>
    <li>ancestorId = Directory 1010</li>
    <li>descendantId = Directory 1000</li>
  </ul>
</Accordion>

#### Request:

```curl
curl -X 'POST' \
  'https://api.blueprint.qa.door.com/access/v1/directory-locks' \
  -H 'accept: */*' \
  -H 'x-door-auth: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
  "directoryItemId": "640cb5fe-8d15-4cf0-a632-8f40e11db7f5",
  "lockId": "AF2D7307-377C-416F-94BD-C81DB311DE19"
}'
```

#### Response:

Status code should be HTTP 200 and Response Body should be the same as the Request Body.

```json Response Body
{
  "directoryItemId": "640cb5fe-8d15-4cf0-a632-8f40e11db7f5",
  "lockId": "af2d7307-377c-416f-94bd-c81db311de19"
}
```

---
title: 4. Access Paths Setup
excerpt: POST Access Path(s).
deprecated: false
hidden: false
metadata:
  robots: index
---
<br />

<Callout icon="📝" theme="default">
  **Step 2/5 of Granting User Access To Doors:** This step is part of the process to grant users access to open doors. User access is determined by Permission Sets, access to the associated Directory Item,  Access Paths, Roles and Role Assignments.
</Callout>

Create Access Paths (segments/connections) between Directory Items and specify Entrance Routes in a Property.

#### Request definition:

| **Method** | **Host**                                               | **Path**                    |
| ---------- | ------------------------------------------------------ | --------------------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/access/v1/paths/segments` |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: Bearer Token
* **`Content-Type`**: `application/json`

**Request Body:**

Should contain a JSON array, `segments`, made of Objects with two properties:

* `ancestorId`: Ancestor OpenDOOR Directory Item, identified through OpenDOOR ID
* `descendantId`: Descendant OpenDOOR Directory Item, identified through OpenDOOR ID

<Callout icon="📝" theme="default">
  **Note:** The system prevents the creation of cyclic dependencies when setting up Access Path Segments. For example, connecting `Directory 1000` to `Directory 1010` and then back from `1010` to `1000` will be blocked. Ensure configurations are free of loops to comply with system constraints.
</Callout>

```json Request Body Structure
{
  "segments": [
    {
      "ancestorId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "descendantId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }
  ]
}
```

### Example Usage

We'll be using data from [1. Directory Setup → Property Setup → Individual Property Creation → Step 4: Retrieve the entire Directory Subtree](https://opendoor-uwel.readme.io/docs/individual-property-creation#step-4-retrieve-the-entire-directory-subtree-1) to set up Access Path Segments as `Ancestor → Descendant` associations:

<Accordion title="Segment 1: Parking Lot Entrance → Residential Building Entrance" icon="angle-down">
  <ul>
    <li>ancestorId = 640cb5fe-8d15-4cf0-a632-8f40e11db7f5</li>
    <li>descendantId = 3a6f60c4-278c-442c-91c7-1731a2482a71</li>
  </ul>
</Accordion>

<Accordion title="Segment 2: Residential Building Entrance → Lobby" icon="angle-down">
  <ul>
    <li>ancestorId = 3a6f60c4-278c-442c-91c7-1731a2482a71</li>
    <li>descendantId = 6996ddfc-4e47-4dd0-bbc2-5a42ddd4597a</li>
  </ul>
</Accordion>

<Accordion title="Segment 3: Residential Building Entrance → Elevator 1" icon="angle-down">
  <ul>
    <li>ancestorId = 3a6f60c4-278c-442c-91c7-1731a2482a71</li>
    <li>descendantId = ec2677fa-b3b4-4f33-ad55-f39cabc63ed8</li>
  </ul>
</Accordion>

<Accordion title="Segment 4: Residential Building Entrance → Elevator 2" icon="angle-down">
  <ul>
    <li>ancestorId = 3a6f60c4-278c-442c-91c7-1731a2482a71</li>
    <li>descendantId = 064fd175-31a0-4611-8269-2ef43f725a2f</li>
  </ul>
</Accordion>

<Accordion title="Segment 5: Residential Building Entrance → Floor 1" icon="angle-down">
  <ul>
    <li>ancestorId = 3a6f60c4-278c-442c-91c7-1731a2482a71</li>
    <li>descendantId = 7cd7cd3c-08f8-4688-8ec8-ea36c9c06082</li>
  </ul>
</Accordion>

<Accordion title="Segment 6: Floor 1 → Floor 1 - Unit 101" icon="angle-down">
  <ul>
    <li>ancestorId = 7cd7cd3c-08f8-4688-8ec8-ea36c9c06082</li>
    <li>descendantId = 6056d246-1cde-46ce-9933-c612a01198b4</li>
  </ul>
</Accordion>

<Accordion title="Segment 7: Floor 1 - Unit 101 → Parking Lot Residents Slot 101" icon="angle-down">
  <ul>
    <li>ancestorId = 6056d246-1cde-46ce-9933-c612a01198b4</li>
    <li>descendantId = 244e5691-acbb-40df-9014-053886e4a97b</li>
  </ul>
</Accordion>

<Accordion title="Segment 8: Floor 1 - Unit 101 → Package Room Lockbox 101" icon="angle-down">
  <ul>
    <li>ancestorId = 6056d246-1cde-46ce-9933-c612a01198b4</li>
    <li>descendantId = 06245e70-ed58-4bcf-ad70-77286313b70f</li>
  </ul>
</Accordion>

<Accordion title="Segment 9: Floor 1 - Unit 101 → Amenities Entrance" icon="angle-down">
  <ul>
    <li>ancestorId = 6056d246-1cde-46ce-9933-c612a01198b4</li>
    <li>descendantId = 049313c6-d483-491d-8429-19129dfb181f</li>
  </ul>
</Accordion>

<Accordion title="Segment 10: Floor 1 - Unit 101 → Gym Door" icon="angle-down">
  <ul>
    <li>ancestorId = 6056d246-1cde-46ce-9933-c612a01198b4</li>
    <li>descendantId = 5af43e29-cd9a-4a74-a815-c8d1ff0b6384</li>
  </ul>
</Accordion>

<Accordion title="Segment 11: Delivery Service Door → Package Room" icon="angle-down">
  <ul>
    <li>ancestorId = 701d9dea-e1d2-4784-9fe7-3577f3e8b628</li>
    <li>descendantId = 4b15f3d0-83c5-41dc-a0dc-fed33afba6c4</li>
  </ul>
</Accordion>

#### Request

```curl
curl -X 'POST' \
  'https://api.prod.door.com/access/v1/paths/segments' \
  -H 'accept: */*' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
  "segments": [
    {
      "ancestorId": "640cb5fe-8d15-4cf0-a632-8f40e11db7f5",
      "descendantId": "3a6f60c4-278c-442c-91c7-1731a2482a71"
    },
    {
      "ancestorId": "3a6f60c4-278c-442c-91c7-1731a2482a71",
      "descendantId": "6996ddfc-4e47-4dd0-bbc2-5a42ddd4597a"
    },
    {
      "ancestorId": "3a6f60c4-278c-442c-91c7-1731a2482a71",
      "descendantId": "ec2677fa-b3b4-4f33-ad55-f39cabc63ed8"
    },
    {
      "ancestorId": "3a6f60c4-278c-442c-91c7-1731a2482a71",
      "descendantId": "064fd175-31a0-4611-8269-2ef43f725a2f"
    },
    {
      "ancestorId": "3a6f60c4-278c-442c-91c7-1731a2482a71",
      "descendantId": "7cd7cd3c-08f8-4688-8ec8-ea36c9c06082"
    },
    {
      "ancestorId": "7cd7cd3c-08f8-4688-8ec8-ea36c9c06082",
      "descendantId": "6056d246-1cde-46ce-9933-c612a01198b4"
    },
    {
      "ancestorId": "6056d246-1cde-46ce-9933-c612a01198b4",
      "descendantId": "244e5691-acbb-40df-9014-053886e4a97b"
    },
    {
      "ancestorId": "6056d246-1cde-46ce-9933-c612a01198b4",
      "descendantId": "06245e70-ed58-4bcf-ad70-77286313b70f"
    },
    {
      "ancestorId": "6056d246-1cde-46ce-9933-c612a01198b4",
      "descendantId": "049313c6-d483-491d-8429-19129dfb181f"
    },
    {
      "ancestorId": "6056d246-1cde-46ce-9933-c612a01198b4",
      "descendantId": "5af43e29-cd9a-4a74-a815-c8d1ff0b6384"
    },
    {
      "ancestorId": "701d9dea-e1d2-4784-9fe7-3577f3e8b628",
      "descendantId": "4b15f3d0-83c5-41dc-a0dc-fed33afba6c4"
    }
  ]
}'
```

#### Response

The status code should be HTTP 200 and Response Body should match the Request Body.

```json Response Body
{
  "segments": [
    {
      "ancestorId": "640cb5fe-8d15-4cf0-a632-8f40e11db7f5",
      "descendantId": "3a6f60c4-278c-442c-91c7-1731a2482a71"
    },
    {
      "ancestorId": "3a6f60c4-278c-442c-91c7-1731a2482a71",
      "descendantId": "6996ddfc-4e47-4dd0-bbc2-5a42ddd4597a"
    },
    {
      "ancestorId": "3a6f60c4-278c-442c-91c7-1731a2482a71",
      "descendantId": "ec2677fa-b3b4-4f33-ad55-f39cabc63ed8"
    },
    {
      "ancestorId": "3a6f60c4-278c-442c-91c7-1731a2482a71",
      "descendantId": "064fd175-31a0-4611-8269-2ef43f725a2f"
    },
    {
      "ancestorId": "3a6f60c4-278c-442c-91c7-1731a2482a71",
      "descendantId": "7cd7cd3c-08f8-4688-8ec8-ea36c9c06082"
    },
    {
      "ancestorId": "7cd7cd3c-08f8-4688-8ec8-ea36c9c06082",
      "descendantId": "6056d246-1cde-46ce-9933-c612a01198b4"
    },
    {
      "ancestorId": "6056d246-1cde-46ce-9933-c612a01198b4",
      "descendantId": "244e5691-acbb-40df-9014-053886e4a97b"
    },
    {
      "ancestorId": "6056d246-1cde-46ce-9933-c612a01198b4",
      "descendantId": "06245e70-ed58-4bcf-ad70-77286313b70f"
    },
    {
      "ancestorId": "6056d246-1cde-46ce-9933-c612a01198b4",
      "descendantId": "049313c6-d483-491d-8429-19129dfb181f"
    },
    {
      "ancestorId": "6056d246-1cde-46ce-9933-c612a01198b4",
      "descendantId": "5af43e29-cd9a-4a74-a815-c8d1ff0b6384"
    },
    {
      "ancestorId": "701d9dea-e1d2-4784-9fe7-3577f3e8b628",
      "descendantId": "4b15f3d0-83c5-41dc-a0dc-fed33afba6c4"
    }
  ]
}
```

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

<Callout icon="⚠️" theme="warning">
  **Important Note:** If you've provided Lock ID/UUIDs and they appear in successful responses body (end of this page), you don't have to complete [2. Directory Locks Setup](doc:assign-locks-to-directories) for them anymore, the Lock is assigned to the created Directory.
</Callout>

<Callout icon="📝" theme="default">
  **How to use below endpoints:**

  1. `/directory/v1/items` to create the initial Directory structure, can even be complete at the moment.
  2. `/directory/v1/items/{scope}` to create additional Directory Items and link them to an existing Item, identified by `scope`.
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

**Request Body:** uses below structure . `children` JSON property can accommodate an entire nested Directory structure, so the Directory can be built in one request.

```json Request Body Structure
{
  "name": "string",
  "tags": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "children": [
    "string"
  ]
}
```

### Create Entire Directory Structure in One Request

#### Step 1: Prepare JSON Request Body

We'll be using Directory structure from [Property Setup](doc:property-setup) as an example. It contains sample data that will be used in the subsequent guide pages. We're leaving out some Lock Assignments/Associations to Directories and some Directory items, that will be used in later Steps.

```json Request Body
```

#### Step 2: Send Request!

#### Step 3: Validate Response

### Create Directory Structure in Batches

#### Step 1: Break it into JSON batches

#### Step 2: Send Request!

#### Step 3: Validate Response

#### Step 4: Repeat until there are no more batches

<br />

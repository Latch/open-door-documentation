---
title: 5. Roles Setup
excerpt: POST Role.
deprecated: false
hidden: false
metadata:
  robots: index
---
Create custom Roles.

#### Request definition:

| **Method** | **Host**                                               | **Path**         |
| ---------- | ------------------------------------------------------ | ---------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/rbac/v1/roles` |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: TBD
* **`Content-Type`**: `application/json`

**Request Body:**

The request body should include the following properties:

* **`name`**: The name of the Role.
* **`type`**: Must be one of the five predefined Role Types (`ROLE_TYPE_GUEST`, `ROLE_TYPE_RESIDENT`, `ROLE_TYPE_VENDOR`, `ROLE_TYPE_STAFF` and `ROLE_TYPE_ADMIN`).
* **`clauses`**: An array of Clause Objects that define the specific behaviors and permissions a Role can have. Each Clause includes a `permissionSetId` and optional conditions that specify constraints such as date ranges, time intervals, and directory item tags. The `directoryScopeSelector` determines whether the Clause is statically or dynamically scoped, allowing for flexible role configurations.

<Accordion title="Clauses Details" icon="angle-down">
  * **`permissionSetId`**: ID of the Permission Set.
  * **`conditions`**: An optional array of Condition Objects.
    * **`dateIntervalCondition`**: Specifies the date range.
    * **`weekdayTimeIntervalCondition`**: Specifies the time intervals for weekdays.
    * **`directoryItemTagCondition`**: Filters based on Directory Item Tags.
    * **`accessPermissionTypeCondition`**: Defines access type (`REACH` or `ACCESS`).
    * **`accessShowDoorCodesCondition`**: Boolean to show Door Codes.
  * **`directoryScopeSelector`**: Determines if the Clause is statically or dynamically scoped.
    * **`directoryItemId`**: ID for static scoping.
    * **`directoryItemTag`**: Tags for dynamic scoping.
    * **`staticallyScoped`**: Boolean indicating static scope.
</Accordion>

* **`scopeDirectoryItemId`**: ID for the scope directory item.

```json Request Body
{
  "name": "string",
  "type": "ROLE_TYPE_GUEST",
  "clauses": [
    {
      "permissionSetId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "conditions": [
        {
          "dateIntervalCondition": {
            "startDate": 0,
            "endDate": 0
          },
          "weekdayTimeIntervalCondition": {
            "intervals": [
              {
                "weekday": 0,
                "startTime": "string",
                "endTime": "string"
              }
            ]
          },
          "directoryItemTagCondition": {
            "tags": [
              {
                "itemType": "ROOT",
                "spaceType": "BUILDING_GROUP",
                "featureFlag": "BLUEPRINT_ENABLED",
                "vacancy": "VACANT",
                "cortex": "ACCOUNT"
              }
            ]
          },
          "accessPermissionTypeCondition": "REACH",
          "accessShowDoorCodesCondition": true
        }
      ],
      "directoryScopeSelector": {
        "directoryItemId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "directoryItemTag": {
          "itemType": "ROOT",
          "spaceType": "BUILDING_GROUP",
          "featureFlag": "BLUEPRINT_ENABLED",
          "vacancy": "VACANT",
          "cortex": "ACCOUNT"
        },
        "staticallyScoped": true
      }
    }
  ],
  "scopeDirectoryItemId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

### Example Usage

We'll create a Role for an On-Site Property Manager with the following Clauses, that will grant selective permissions through the Permission Sets:

1. **Manage a Property:**
   1. Allows the manager to oversee and administer property operations.
   2. Will be granted access on any `PROPERTY` Directory item from `OpenDOOR Client Account` (ID `e43f4017-da92-4c4a-87ff-5c5f418c3cf6`) from [1. Directory Setup → Property Setup → Individual Property Creation → Step 4: Retrieve the entire Directory Subtree](https://opendoor-uwel.readme.io/docs/individual-property-creation#step-4-retrieve-the-entire-directory-subtree-1) through **dynamic** Clause associated with `OpenDOOR Property Manager Permission Set` (ID `d67d8a3e-4f10-4e4d-86ae-031c0ee2229e`) from [4. Permission Sets Setup → Example Usage → Response](https://opendoor-uwel.readme.io/docs/permission-sets-setup#response).
2. **Be a Resident in that Property:** As an on-site manager, this role includes residential privileges within the property, for vacant `UNIT` spaces. Will be granted through **dynamic** Clause associated with:
   ```json OpenDOOR Resident Permission Set
   {
       "id": "604334f0-ac54-4d32-b1ab-2f25143713ed",
       "locationDirectoryItemId": "e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
       "name": "OpenDOOR Resident Permission Set",
       "permissions": [
         "OCCUPY",
         "ENTER_SPACE",
         "ACCESS_SPACE",
         "ACCESS",
         "REACH_SPACE",
         "VIEW_UNIT",
         "INVITE_REVOKE_GUEST"
       ]
   }
   ```
3. **Access Amenities outside work hours:** This grants the manager access to amenities outside working hours through **static** Clause associated with:
   ```json OpenDOOR Amenities User Permission Set
   {
       "id": "4520f04b-583e-4b57-a1ba-7a3e7f3cc688",
       "locationDirectoryItemId": "e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
       "name": "OpenDOOR All Amenities User Permission Set",
       "permissions": [
         "ENTER_SPACE",
         "ACCESS_SPACE",
         "ACCESS",
         "REACH_SPACE"
       ]
   }
   ```

<br />

#### Request

```curl
```

#### Response

Status code should be HTTP 200 and Response Body like below example:

```json Response Body
```

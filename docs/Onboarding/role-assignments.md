---
title: 6. Role Assignments
excerpt: POST Role To User Assignment.
deprecated: false
hidden: false
metadata:
  robots: index
---
This is the final Step in granting a User permissions to Directory Items by assigning a Role to it.

#### Request definition:

| **Method** | **Host**                                               | **Path**                         |
| ---------- | ------------------------------------------------------ | -------------------------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/rbac/v1/roles/{roleId}/assign` |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: TBD
* **`Content-Type`**: `application/json`

**Request Body:**

The request body should include the following properties:

* **`name`**: The name of the Role Assignment.
* **`locationDirectoryItemId`**: Directory Item ID under which the Role Assignment Scope is located. Can be 1st or nth level Parent.
* **`scopeDefinitions`**: An array of Scope Definition Objects that specifies what behavior is assigned to a User and what Scopes (Directory Items) it applies to. Each Scope Definition includes a `roleClauseId`, `scopeDirectoryItemId` and optional conditions that specify constraints such as date ranges, time intervals, and directory item tags.

<Accordion title="Scope Definitions Details" icon="angle-down">
  * **`roleClauseId`**: ID of the Role Clause.
    * **`scopeDirectoryItemId`**: ID of the Scope Directory Item where the Assignment is created on.
  * **`conditions`**: An optional array of Condition Objects.
    * **`dateIntervalCondition`**: Specifies the date range.
    * **`weekdayTimeIntervalCondition`**: Specifies the time intervals for weekdays.
    * **`directoryItemTagCondition`**: Filters based on Directory Item Tags.
    * **`accessPermissionTypeCondition`**: Defines access type (`REACH` or `ACCESS`).
    * **`accessShowDoorCodesCondition`**: Boolean to show Door Codes.
</Accordion>

* **`subject`**: Identify the User we assign the Role to through `idSource` and `id` (User's UUID from Latch Cortex).

```json Request Body
{
  "name": "string",
  "locationDirectoryItemId": "string",
  "scopeDefinitions": [
    {
      "roleClauseId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "scopeDirectoryItemId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
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
          "accessAssignDoorCodesCondition": true
        }
      ]
    }
  ],
  "subject": {
    "idSource": "DOOR_USER_IDP",
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  }
}
```

### Example Usage

We'll assign Role `OpenDOOR Staff Role` (ID `cd748a08-52aa-4768-9f9b-fff08c5336f2`) from [5. Roles Setup → Example Usage → Response](https://opendoor-uwel.readme.io/docs/roles-setup#response) to User identified through Latch Cortex UUID `ED1BBEB6-5563-4AB3-87DA-5E1A0FB2FC33`, thus granting Staff Employee permissions to the User.

#### Request

```curl
curl -X 'POST' \
  'https://api.prod.door.com/rbac/v1/roles/cd748a08-52aa-4768-9f9b-fff08c5336f2/assign' \
  -H 'accept: */*' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "OpenDOOR Staff Role Assignment",
  "locationDirectoryItemId": "e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
  "scopeDefinitions": [
    {
      "roleClauseId": "6594cc24-eba6-4c39-8bd3-cca7ba71a3f3",
      "scopeDirectoryItemId": "8ae57cb5-206e-4f2b-9f71-879024309ea1"
    }
  ],
  "subject": {
    "idSource": "DOOR_USER_IDP",
    "id": "ED1BBEB6-5563-4AB3-87DA-5E1A0FB2FC33"
  }
}'
```

#### Response

Status code should be HTTP 200 and Response Body like in below example:

```json Response Body
{
  "roleAssignmentId": "000db09b-dc36-48ed-8f9e-e921247b488f",
  "name": "OpenDOOR Staff Role Assignment",
  "subject": {
    "idSource": "DOOR_USER_IDP",
    "id": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
  },
  "clauses": [
    {
      "id": "6594cc24-eba6-4c39-8bd3-cca7ba71a3f3",
      "permissionSet": {
        "id": "d67d8a3e-4f10-4e4d-86ae-031c0ee2229e",
        "locationDirectoryItemId": null,
        "name": "OpenDOOR Staff Permission Set",
        "permissions": [
          "ENTER_SPACE",
          "ACCESS_SPACE",
          "REACH_SPACE",
          "ACCESS",
          "VIEW_DIRECTORY",
          "VIEW_UNIT",
          "INVITE_REVOKE_GUEST",
          "VIEW_GUEST_ROLE_ASSIGNMENTS",
          "VIEW_RESIDENT_ROLE_ASSIGNMENTS",
          "REVOKE_ANY_GUEST"
        ]
      },
      "directoryItemIdScope": "8ae57cb5-206e-4f2b-9f71-879024309ea1",
      "conditions": [],
      "active": true,
      "provisioningStatus": null
    }
  ],
  "roleId": "cd748a08-52aa-4768-9f9b-fff08c5336f2",
  "scopeDirectoryItemPath": "00000000-0000-0000-0000-000000000000/e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
  "scopeDirectoryItemId": "e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
  "active": true,
  "createdBy": {
    "idSource": "DOOR_USER_IDP",
    "id": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
  },
  "createdAt": 1768250078291,
  "provisioningStatus": "PROVISIONING_STATUS_SUCCESS",
  "type": "ROLE_TYPE_STAFF"
}
```

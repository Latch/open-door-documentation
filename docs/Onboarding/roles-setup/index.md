---
title: 3. Roles Setup
excerpt: POST Role.
deprecated: false
hidden: false
metadata:
  robots: index
---
<Callout icon="📝" theme="info">
  **Step 2/5 of Granting User Access to Doors:** This step is part of the process to grant users access to open doors within the property. User Access to Door Directory Items is determined by Directory Locks, Access Paths, Permission Sets, Roles and Role Assignments.
</Callout>

Specify the Roles and their types available in the building, what actions can they do (based on Permission Sets) and where they are applicable (Scopes).

#### Request definition:

| **Method** | **Host**                                               | **Path**         |
| ---------- | ------------------------------------------------------ | ---------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/rbac/v1/roles` |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: Bearer Token
* **`Content-Type`**: `application/json`

**Request Body:**

The request body should include the following properties:

* **`name`**: The name of the Role.
* **`type`**: Must be one of the five predefined Role Types (`ROLE_TYPE_GUEST`, `ROLE_TYPE_RESIDENT`, `ROLE_TYPE_VENDOR`, `ROLE_TYPE_STAFF` and `ROLE_TYPE_ADMIN`).
* **`clauses`**: An array of Clause Objects that define the specific permissions a Role can have. Each Clause includes:
  * a `permissionSetId` identifying the permission set that will be granted (i.e. **WHAT** the user can do);
  * a `directoryScopeSelector` that identifies **WHERE** the user can perform those actions. It determines whether the Clause is _statically scoped_, targeting a **fixed** directory item for all users who will be assigned to this role, or _dynamically scoped_, allowing the selection of a different directory item for each user when this role is assigned.
  * optional conditions that specify constraints such as date ranges, time intervals, and directory item tags that the permissions will apply to **after** the role is assigned.
    * The crucial distinction between the scope **selector** and directory **conditions**: the selector only applies at role assignment time, limiting where the role clause can be applied (example: "Select **one** unit in the building"); whereas the conditions apply forever to all directories that match (example: "**All** units in the building").

<Accordion title="Clauses Details" icon="angle-down">
  * **`permissionSetId`**: ID of the Permission Set.
  * **`conditions`**: Additional conditions of various types. *Each* condition type is optional, as is the entire `conditions` field; it is also possible to set up more than one condition type.
    * **`dateIntervalCondition`**: Specifies the date range.
    * **`weekdayTimeIntervalCondition`**: Specifies the time intervals for weekdays.
    * **`directoryItemTagCondition`**: Filters based on Directory Item Tags.
    * **`accessPermissionTypeCondition`**: Defines access type (`REACH` or `ACCESS`).
    * **`accessShowDoorCodesCondition`**: Boolean to show Door Codes.
  * **`directoryScopeSelector`**: Defines the Scope. The system will determine if the Clause is statically or dynamically scoped based on this.
    * **`directoryItemId`**: The directory item where this clause will apply.
    * **`directoryItemTag`**: Selectable tags; including this field will make the clause **dynamically scoped**.
</Accordion>

<Callout icon="📝" theme="default">
  Role Clauses can be either **Statically Scoped**, indicated through `directoryItemId` JSON property or **Dynamically Scoped**, indicated by `directoryItemTag`, in `directoryScopeSelector` JSON Object property.
</Callout>

<Callout icon="⚠️" theme="warning">
  **Important Note:** The Permissions for a Role are defined within Permission Sets. Ensure that the Permission Set specified for each Role is limited to the maximum allowable permissions for each individual role type. For example, you may not use an "admin" permission set for a resident role! For more details, refer to [5. Roles Setup → Maximum Allowed Permissions for Each Role Type Type](https://opendoor-uwel.readme.io/update/docs/essential-permissions-for-each-role-type).
</Callout>

<br />

```json Request Body
{
  "name": "string",
  "type": "ROLE_TYPE_GUEST",
  "clauses": [
    {
      "permissionSetId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "conditions": {
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
      },
      "directoryScopeSelector": {
        "directoryItemId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "directoryItemTag": {
          "itemType": "ROOT",
          "spaceType": "BUILDING_GROUP",
          "featureFlag": "BLUEPRINT_ENABLED",
          "vacancy": "VACANT",
          "cortex": "ACCOUNT"
        }
      }
    }
  ],
  "scopeDirectoryItemId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

### Example Usage

We'll create a Role for Staff employees that will selectively grant access on any `PROPERTY` Directory Item from `OpenDOOR Client Account` (ID `e43f4017-da92-4c4a-87ff-5c5f418c3cf6`) from [1. Directory Setup → Property Setup → Automate Property Creation with the API → Create Entire Directory Structure in One Request → Step 4: Retrieve the entire Directory Subtree](https://opendoor-uwel.readme.io/docs/individual-property-creation#step-4-retrieve-the-entire-directory-subtree-1) through **dynamic** Clause associated with `OpenDOOR Staff Permission Set` (ID `d67d8a3e-4f10-4e4d-86ae-031c0ee2229e`) from [4. Permission Sets Setup → Example Usage → Response](https://opendoor-uwel.readme.io/docs/permission-sets-setup#response):

1. **Enter and Access Spaces:** Staff are authorized to enter and access various spaces within the property, ensuring they can perform their duties effectively.
2. **Reach Spaces:** Staff can navigate through different areas, ensuring they can reach any part of the property as needed.
3. **Revoke Any Guest:** Staff have the authority to revoke access for any guest, ensuring security and compliance with property policies.

#### Request

```curl
curl -X 'POST' \
  'https://api.prod.door.com/rbac/v1/roles' \
  -H 'accept: */*' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "OpenDOOR Staff Role",
    "type": "ROLE_TYPE_STAFF",
    "clauses": [
        {
            "permissionSetId": "d67d8a3e-4f10-4e4d-86ae-031c0ee2229e",
            "conditions": [],
            "directoryScopeSelector": {
                "directoryItemTag": {
                    "spaceType": "SPACE_PROPERTY"
                }
            }
        }
    ],
    "scopeDirectoryItemId": "e43f4017-da92-4c4a-87ff-5c5f418c3cf6"
}'
```

#### Response

Status code should be HTTP 200 and Response Body like in below example:

```json Response Body
{
  "id": "cd748a08-52aa-4768-9f9b-fff08c5336f2",
  "name": "OpenDOOR Staff Role",
  "type": "ROLE_TYPE_STAFF",
  "clauses": [
    {
      "id": "6594cc24-eba6-4c39-8bd3-cca7ba71a3f3",
      "permissionSetId": "d67d8a3e-4f10-4e4d-86ae-031c0ee2229e",
      "conditions": [],
      "directoryScopeSelector": {
        "directoryItemTag": {
          "spaceType": "SPACE_PROPERTY"
        },
        "staticallyScoped": false
      },
      "staticallyScoped": false
    }
  ],
  "scopeDirectoryItemId": "e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
  "scopeDirectoryPath": "00000000-0000-0000-0000-000000000000/e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
  "createdAt": 1768248694721,
  "createdBy": {
    "idSource": "DOOR_USER_IDP",
    "id": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
  },
  "staticallyScoped": false
}
```

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

* `name`: Name of the Role
* `type`: Value should be one of the predefined Role types (`ROLE_TYPE_GUEST`, `ROLE_TYPE_RESIDENT`, `ROLE_TYPE_VENDOR`, `ROLE_TYPE_STAFF` and `ROLE_TYPE_ADMIN`)
* `clauses`:  An array of Clause Objects that define different behaviors a Role can have. A Clause is made of:
  * `permissionSetId`: ID of the Permission Set
  * `conditions`: An optional array of Condition Objects defining how the Clause applies. A Condition is made of:
    * `dateIntervalCondition`: Date Clause Condition.
    * `weekdayTimeIntervalCondition`: Weekday Clause Condition.
    * `directoryItemTagCondition`:  Contains `tags` array that can specify to what Directory Items Condition applies based on tag filtering. It can take one or multiple of these Directory Item Tag properties: `itemType`, `spaceType`, `featureFlag`, `vacancy` and `cortex`.
    * `accessPermissionTypeCondition`: It specifies if Directory Item access Permission type is `REACH` or `ACCESS`.
    * `accessShowDoorCodesCondition`: Boolean specifying if Door Codes should be shown for the Directory Item.
  * `directoryScopeSelector`: Object where we decide if the Clause is **Statically** or **Dynamically Scoped**
    * `directoryItemId`: ID of a Directory Item. It shows the Clause is defined as **Statically Scoped**. Role can be assigned to Users only on the Directory Item itself or its sub-Directory.
    * `directoryItemTag`: Object that can take one or multiple of these Directory Item Tag properties: `itemType`, `spaceType`, `featureFlag`, `vacancy` and `cortex`. It shows the Clause is defined as **Dynamically Scoped**, filtering possible Directory Items on Role Assignment based on the tags.
    * `staticallyScoped`: Optional Boolean property that shows if the Clause is static or not. It's automatically determined at creation time, regardless of what value it might have in the Request Body.

<br />

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

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
* **`type`**: Must be one of the five predefined Role Types.

<Accordion title="Clauses" icon="angle-down">
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

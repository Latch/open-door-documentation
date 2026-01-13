---
title: 6. Role Assignments
excerpt: POST Role Assignment.
deprecated: false
hidden: false
metadata:
  robots: index
---
Assign Role to User.

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

* **`name`**: The name of the Role.
* **`type`**: Must be one of the five predefined Role Types (`ROLE_TYPE_GUEST`, `ROLE_TYPE_RESIDENT`, `ROLE_TYPE_VENDOR`, `ROLE_TYPE_STAFF` and `ROLE_TYPE_ADMIN`).
* **`clauses`**: An array of Clause Objects that define the specific behaviors and permissions a Role can have. Each Clause includes a `permissionSetId` and optional conditions that specify constraints such as date ranges, time intervals, and directory item tags. The `directoryScopeSelector` determines whether the Clause is statically or dynamically scoped, allowing for flexible role configurations.

<Callout icon="⚠️" theme="warning">
  **Important Note:** Role Clauses can be either **Statically Scoped**, indicated through `directoryItemId` JSON property or **Dynamically Scoped**, indicated by `directoryItemTag`, in `directoryScopeSelector` JSON Object property.
</Callout>

<Accordion title="Clauses Details" icon="angle-down">
  * **`permissionSetId`**: ID of the Permission Set.
  * **`conditions`**: An optional array of Condition Objects.
    * **`dateIntervalCondition`**: Specifies the date range.
    * **`weekdayTimeIntervalCondition`**: Specifies the time intervals for weekdays.
    * **`directoryItemTagCondition`**: Filters based on Directory Item Tags.
    * **`accessPermissionTypeCondition`**: Defines access type (`REACH` or `ACCESS`).
    * **`accessShowDoorCodesCondition`**: Boolean to show Door Codes.
  * **`directoryScopeSelector`**: Determines the Scope and if the Clause is statically or dynamically scoped.
    * **`directoryItemId`**: ID for static scoping.
    * **`directoryItemTag`**: Tags for dynamic scoping.
    * **`staticallyScoped`**: Optional Boolean indicating static scope.
</Accordion>

* **`scopeDirectoryItemId`**: ID for the scope directory item.

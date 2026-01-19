---
title: Essential Permissions for Each Role Type
excerpt: >-
  Mapping of minimum required Permission Sets to Role Type for effective user
  functionality.
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
## Minimum Permission Set Requirements for Each Role Type

This section outlines the minimum required permission sets for each role type within the system. These permissions ensure that users can perform their designated functions effectively.

### Role Type and Permission Mapping

| **Role Type**            | **Permissions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`ROLE_TYPE_GUEST`**    | `ENTER_SPACE`, `ACCESS_SPACE`, `ACCESS`, `REACH_SPACE`, `VIEW_UNIT`                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **`ROLE_TYPE_RESIDENT`** | `OCCUPY`, `ENTER_SPACE`, `ACCESS_SPACE`, `ACCESS`, `REACH_SPACE`, `VIEW_DIRECTORY`, `VIEW_UNIT`, `INVITE_REVOKE_GUEST`, `VIEW_GUEST_ROLE_ASSIGNMENTS`, `VIEW_RESIDENT_ROLE_ASSIGNMENTS`, `REVOKE_ANY_GUEST`                                                                                                                                                                                                                                                                                                                 |
| **`ROLE_TYPE_VENDOR`**   | `ENTER_SPACE`, `ACCESS_SPACE`, `ACCESS`, `REACH_SPACE`, `VIEW_DIRECTORY`, `VIEW_UNIT`                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **`ROLE_TYPE_STAFF`**    | `ENTER_SPACE`, `ACCESS_SPACE`, `ACCESS`, `REACH_SPACE`, `VIEW_DIRECTORY`, `VIEW_UNIT`, `INVITE_REVOKE_GUEST`, `VIEW_GUEST_ROLE_ASSIGNMENTS`, `VIEW_RESIDENT_ROLE_ASSIGNMENTS`, `REVOKE_ANY_GUEST`                                                                                                                                                                                                                                                                                                                           |
| **`ROLE_TYPE_ADMIN`**    | `MANAGE_DIRECTORY`, `ENTER_SPACE`, `ACCESS_SPACE`, `ACCESS`, `REACH_SPACE`, `VIEW_DIRECTORY`, `VIEW_UNIT`, `CONFIGURE_ACCESS`, `INVITE_REVOKE_GUEST`, `INVITE_REVOKE_RESIDENT`, `INVITE_REVOKE_STAFF`, `INVITE_REVOKE_VENDOR`, `INVITE_REVOKE_ADMIN`, `VIEW_GUEST_ROLE_ASSIGNMENTS`, `VIEW_RESIDENT_ROLE_ASSIGNMENTS`, `VIEW_STAFF_ROLE_ASSIGNMENTS`, `VIEW_VENDOR_ROLE_ASSIGNMENTS`, `VIEW_ADMIN_ROLE_ASSIGNMENTS`, `REVOKE_ANY_GUEST`, `REVOKE_ANY_RESIDENT`, `REVOKE_ANY_STAFF`, `REVOKE_ANY_VENDOR`, `REVOKE_ANY_ADMIN` |

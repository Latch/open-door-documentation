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

Below is the mapping of minimum required permissions for each role type:

| **Role Type** | **Permissions** |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Guest**     | `ENTER_SPACE`, `ACCESS_SPACE`, `ACCESS`, `REACH_SPACE`, `VIEW_UNIT` |
| **Resident**  | `OCCUPY`, `ENTER_SPACE`, `ACCESS_SPACE`, `ACCESS`, `REACH_SPACE`, `VIEW_DIRECTORY`, `VIEW_UNIT`, `INVITE_REVOKE_GUEST`, `VIEW_GUEST_ROLE_ASSIGNMENTS`, `VIEW_RESIDENT_ROLE_ASSIGNMENTS`, `REVOKE_ANY_GUEST` |
| **Staff**     | `ENTER_SPACE`, `ACCESS_SPACE`, `ACCESS`, `REACH_SPACE`, `VIEW_DIRECTORY`, `VIEW_UNIT`, `INVITE_REVOKE_GUEST`, `VIEW_GUEST_ROLE_ASSIGNMENTS`, `VIEW_RESIDENT_ROLE_ASSIGNMENTS`, `REVOKE_ANY_GUEST` |
| **Vendor**    | `ENTER_SPACE`, `ACCESS_SPACE`, `ACCESS`, `REACH_SPACE`, `VIEW_DIRECTORY`, `VIEW_UNIT` |
| **Admin**     | `MANAGE_DIRECTORY`, `ENTER_SPACE`, `ACCESS_SPACE`, `ACCESS`, `REACH_SPACE`, `VIEW_DIRECTORY`, `VIEW_UNIT`, `CONFIGURE_ACCESS`, `INVITE_REVOKE_GUEST`, `INVITE_REVOKE_RESIDENT`, `INVITE_REVOKE_STAFF`, `INVITE_REVOKE_VENDOR`, `INVITE_REVOKE_ADMIN`, `VIEW_GUEST_ROLE_ASSIGNMENTS`, `VIEW_RESIDENT_ROLE_ASSIGNMENTS`, `VIEW_STAFF_ROLE_ASSIGNMENTS`, `VIEW_VENDOR_ROLE_ASSIGNMENTS`, `VIEW_ADMIN_ROLE_ASSIGNMENTS`, `REVOKE_ANY_GUEST`, `REVOKE_ANY_RESIDENT`, `REVOKE_ANY_STAFF`, `REVOKE_ANY_VENDOR`, `REVOKE_ANY_ADMIN` |
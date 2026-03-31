---
title: Customers and Service Partners
deprecated: false
hidden: false
metadata:
  robots: index
---
DOOR is focused on building great solutions to serve both our customers and our partners.

For customers, we provide industry-leading, DOOR-enabled hardware and intuitive software to provide the best end-user experience. For example, with DOOR app, property managers can easily administer and remotely control all the DOOR devices within their properties.

For partners, we are building world-class SDKs and APIs to support mutual customers by enabling DOOR features for different management platforms, resident experiences, and building services. Through our SDKs and APIs, we can deliver new products to end-users by leveraging a combination of partner and DOOR systems to manage DOOR hardware.

| Type             | Function                                                          |
| ---------------- | ----------------------------------------------------------------- |
| End User         | Utilizes the Partner App with OpenDOORSDK to Unlock DOOR devices. |
| Customer         | Purchases and manages DOOR devices.                               |
| Partner          | Utilizes the OpenDOOR API & SDK.                                  |
| Customer Partner | Purchases DOOR devices and utilizes the OpenDOOR API & SDK.       |

## Responsibilities

When utilizing the OpenDOOR API & SDK, Partners work together with DOOR to provide a great user experience to their customers and end-users. Below is a listing of some of the customer and partner responsibilities. Customer Partner responsibilities are the sum of customer and partner responsibilities.

| Customer                      | Partner                                       | DOOR                                           |
| ----------------------------- | --------------------------------------------- | ---------------------------------------------- |
| Manage Physical Devices       | Build client and server integration with DOOR | Provide access to APIs, SDKs and documentation |
| Setup Doors and Keys          | User Authentication                           | Partner / User Authorization                   |
| Assign Doors/Keys to Partners | User Management                               | JWT Token Provider                             |
|                               | JWT Token retrieval from DOOR BE              | Native IOS/Android SDKs                        |
|                               | Host App for DOOR SDK                         | Secure SDK storage and communication           |
|                               | Renew JWT Token                               | Provide and Cache Device Credentials           |
|                               | Provide a great UI/UX                         | Encapsulate all BLE Interactivity              |
|                               | Gather Bluetooth Permissions                  | Provide a list of Doors and Devices to App     |
|                               |                                               | Gather User Consent                            |
|                               |                                               | Traffic Monitoring                             |

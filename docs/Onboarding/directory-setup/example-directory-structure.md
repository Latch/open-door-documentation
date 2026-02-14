---
title: Example Directory Structure
deprecated: false
hidden: false
metadata:
  robots: index
next:
  description: >-
    Use this example to consider your own directory structure. With this
    structure in mind, set up your first property: either provide information
    about the property to your DOOR Sales Representative, who will review it and
    can also create it for you, or create the directory items yourself using the
    API.
---
### Directory Structure

<Callout icon="📝" theme="default">
  **Note:** This directory structure will be used as an **example** throughout the guide. It is designed to showcase some of the key features of OpenDOOR. Your own directory structure may be simpler or more complicated, depending on your requirements.
</Callout>

```toml Directory Structure and Hierarchy
[ACCOUNT] OpenDOOR Client Account
├── [PORTFOLIO] ODC Portfolio 1
│   ├── [PROPERTY] ODCP1 Property 1
│   │   ├── [BUILDING] Parking Lot
│   │   │   ├── [ENTRANCE] Parking Lot Entrance
│   │   │   ├── [PARKING_GROUP] Staff Parking
│   │   │   │   └── [PARKING_SLOT] Staff Slot 1 -> 10
│   │   │   └── [PARKING_GROUP] Residents Parking
│   │   │       └── [PARKING_SLOT] Residents Slot 101 -> 310
│   │   ├── [BUILDING] Residential Building
│   │   │   ├── [ENTRANCE] Residential Building Entrance
│   │   │   ├── [COMMON_GROUP] Common Areas
│   │   │   │   ├── [COMMON_AREA] Lobby
│   │   │   │   ├── [STORAGE_GROUP] Package Room
│   │   │   │   │   └── [SERVICE] Delivery Service Door
│   │   │   │   │   └── [STORAGE_SLOT] Lockbox 101 -> 310
│   │   │   │   ├── [COMMON_AREA] Elevator 1
│   │   │   │   ├── [COMMON_AREA] Elevator 2
│   │   │   │   └── [COMMON_GROUP] Amenities
│   │   │   │       ├── [ENTRANCE] Amenities Entrance
│   │   │   │       ├── [COMMON_AREA] Spa
│   │   │   │       │   └── [ENTRANCE] Spa Door
│   │   │   │       ├── [COMMON_AREA] Gym
│   │   │   │       │   └── [ENTRANCE] Gym Door
│   │   │   │       └── [COMMON_AREA] Meeting Rooms
│   │   │   │           ├── [ENTRANCE] Meeting Rooms Door
│   │   │   │           └── [ROOM] Room 1 -> 6
│   │   │   ├── [FLOOR] Floor 1
│   │   │   │   └── [UNIT] Unit 101 -> 110
│   │   │   │       └── [ENTRANCE] Unit 101 -> 110 Door
│   │   │   ├── [FLOOR] Floor 2
│   │   │   │   └── [UNIT] Unit 201 -> 210
│   │   │   │       └── [ENTRANCE] Unit 201 -> 210 Door
│   │   │   └── [FLOOR] Floor 3
│   │   │       └── [UNIT] Unit 301 -> 310
│   │   │           └── [ENTRANCE] Unit 301 -> 310 Door
│   └── [PROPERTY] ODCP1 Property 2 -> X
└── [PORTFOLIO] ODC Portfolio 2 -> X
```

<Image align="center" border={true} src="https://files.readme.io/e6f40ae787086fee60fcd3b890081359079630e2a66dd6957a02eaf7ab7b3724-221225_Directory_tree.drawio.png" className="border" />
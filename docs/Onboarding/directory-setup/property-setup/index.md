---
title: Property Setup
deprecated: false
hidden: false
metadata:
  robots: index
next:
  description: >-
    Choose one of the two options: prepare the information required by your DOOR
    Sales Representative (strongly recommended), or proceed with using the API
    directly.
  pages:
    - slug: migrate-from-legacy-property
      title: Bulk Import Property Data
      type: basic
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

#### To set up your directory, choose one of the following options:

* **[Bulk Import Property Data](doc:migrate-from-legacy-property) :** This user-friendly approach involves designing your preferred directory structure and adding it to a template CSV file, which you will then send to your DOOR Sales Representative. They will be reviewing and creating the directory structure you have submitted on your behalf.
* **[Individual Property Creation](doc:individual-property-creation) :** Once you have established a clear use case and already have multiple OpenDOOR enabled buildings in active use, you may choose to use the OpenDOOR API to create the directory items for a new property, without relying on your DOOR Sales Representative. This provides you with full ownership of your directory structure, which does allow the possibility of automation, but with the significant downside of not receiving immediate assistance from your DOOR Sales Representative. Choosing this option means you are taking charge of the validity and fitness for purpose of your directory structure. We only recommend you do so once you already have an established and proven directory structure for your other properties.
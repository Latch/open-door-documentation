---
title: Property Setup
deprecated: false
hidden: false
metadata:
  robots: index
---
### Directory Structure

#### NOTE: This Directory tree will be used as example throughout the guide

```plaintext
[ACCOUNT] OpenDOOR Client Account
├── [PORTFOLIO] ODC Portfolio 1
│   ├── [PROPERTY] ODCP1 Property 1
│   │   ├── [BUILDING] Parking Lot
│   │   │   ├── [ENTRANCE] Parking Lot Entrance
│   │   │   ├── [PARKING_GROUP] Staff
│   │   │   │   └── [PARKING_SLOT] Slot 01 -> 10
│   │   │   └── [PARKING_GROUP] Residents
│   │   │       └── [PARKING_SLOT] Slot 101 -> 310
│   │   ├── [BUILDING] Residential Building
│   │   │   ├── [ENTRANCE] Residential Building Entrance
│   │   │   ├── [COMMON_GROUP] Common Areas
│   │   │   │   ├── [COMMON_AREA] Lobby
│   │   │   │   ├── [STORAGE_GROUP] Package Room
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
│   │   │   │   └── [UNIT] Unit 101 -> 109
│   │   │   │       └── [ENTRANCE] Unit 101 -> 109 Door
│   │   │   ├── [FLOOR] Floor 2
│   │   │   │   └── [UNIT] Unit 201 - 210
│   │   │   │       └── [ENTRANCE] Unit 201 -> 210 Door
│   │   │   └── [FLOOR] Floor 3
│   │   │       └── [UNIT] Unit 301 -> 310
│   │   │           └── [ENTRANCE] Unit 301 -> 310 Door
│   └── [PROPERTY] ODCP1 Property 2 -> X
└── [PORTFOLIO] ODC Portfolio 2 -> X
```

<br />

### Can be done in two ways:

* **[Bulk Import Property Data](doc:migrate-from-legacy-property) :** This is the more user-friendly approach. DOOR Client Account data detailing the Properties hierarchy and structure is organized into a templated CSV file that will be passed as input to a dedicated API endpoint.
* **[Individual Property Creation](doc:individual-property-creation) :** Requires making individual API requests to define the Directory tree hierarchy and structure. DOOR Client Account data must be structured and passed in the request body of each API call. This method offers granular control but requires more development effort and API knowledge.

<br />

---
title: Property Setup
deprecated: false
hidden: false
metadata:
  robots: index
---
### Directory Tree Structure

#### NOTE: This Directory tree will be used as example throughout this guide

```plaintext
OpenDOOR Client Account
├── ODC Portfolio 1
│   ├── ODCP1 Property 1
│   │   ├── Parking Lot
│   │   │   ├── Staff
│   │   │   │   ├── Slot 01
│   │   │   │   ├── ...
│   │   │   │   └── Slot 10
│   │   │   └── Residents
│   │   │       ├── Slot 101
│   │   │       ├── ...
│   │   │       └── Slot 310
│   │   ├── Residential Building
│   │   │   ├── Entrance
│   │   │   ├── Common Areas
│   │   │   │   ├── Lobby
│   │   │   │   ├── Package Room
│   │   │   │   │   ├── Lockbox 101
│   │   │   │   │   │   └── Lockbox 101 Door
│   │   │   │   │   ├── ...
│   │   │   │   │   └── Lockbox 310
│   │   │   │   │       └── Lockbox 310 Door
│   │   │   │   ├── Elevator 1
│   │   │   │   └── Elevator 2
│   │   │   ├── Floor 1
│   │   │   │   ├── Unit 101
│   │   │   │   │   └── Unit 101 Door
│   │   │   │   ├── ...
│   │   │   │   └── Unit 109
│   │   │   │       └── Unit 109 Door
│   │   │   ├── Floor 2
│   │   │   │   ├── Unit 201
│   │   │   │   │   └── Unit 201 Door
│   │   │   │   ├── ...
│   │   │   │   └── Unit 210
│   │   │   │       └── Unit 210 Door
│   │   │   └── Floor 3
│   │   │       ├── Unit 301
│   │   │       │   └── Unit 301 Door
│   │   │       ├── ...
│   │   │       └── Unit 310
│   │   │           └── Unit 310 Door
│   │   └── Amenities
│   │       ├── Entrance
│   │       ├── Spa
│   │       │   └── Spa Door
│   │       ├── Gym
│   │       │   └── Gym Door
│   │       └── Meeting Rooms
│   │           ├── Meeting Rooms Door
│   │           ├── Room 1
│   │           ├── ...
│   │           └── Room 6
│   ├── ODCP1 Property 2
│   ├── ...
│   └── ODCP1 Property X
├── ODC Portfolio 2
├── ...
└── ODC Portfolio X
```

<br />

### Can be done in two ways:

* **Bulk Import Property Data:** This is the more user-friendly approach. DOOR Client Account data detailing the Properties hierarchy and structure is organized into a templated CSV file that will be passed as input to a dedicated API endpoint.
* **Individual Property Creation:** Requires making individual API requests to define the Directory tree hierarchy and structure. DOOR Client Account data must be structured and passed in the request body of each API call. This method offers granular control but requires more development effort and API knowledge.

<br />

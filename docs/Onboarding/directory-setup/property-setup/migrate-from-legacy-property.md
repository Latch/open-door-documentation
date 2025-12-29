---
title: Bulk Import Property Data
deprecated: false
hidden: false
metadata:
  robots: index
---
### Step 1: Organize DOOR Client Account data in a CSV file

CSV file should have the following header: `SPACE TYPE,BP SPACE NAME,BP SPACE PARENT NAME,LATCH UUID / ID`.

<Accordion title="CSV Format Guidelines" icon="list">
  1. `SPACE TYPE`:
     1. Type of Space represented by the row (future Directory Item) in the Client Directory tree. It should be the same type as in the DOOR Client Account.
     2. **Possible values:** `ACCOUNT`, `PORTFOLIO`, `PROPERTY`, `BUILDING`, `FLOOR`, `UNIT`, `ROOM`, `PARKING_GROUP`, `PARKING_SLOT`, `STORAGE_GROUP`, `STORAGE_SLOT`, `COMMON_GROUP`, `COMMON_AREA`, `PRIVATE_GROUP`, `PRIVATE_AREA` and `ENTRANCE`
  2. `BP SPACE NAME`: Directory Item name. It should be the same as the DOOR Client Account entity name.
  3. `BP SPACE PARENT NAME`: Name of the Parent Directory Item. It should be from a previous row and should be a perfect String match.
  4. `LATCH UUID / ID`: Latch UUID of the entity, be it Portfolio, Property, Unit, Door/Lock, and so on. It can be obtained from DoorOS or AdminTool.
</Accordion>

#### Create your CSV file and populate it with import data

<Callout icon="📝" theme="default">
  **Tip:** You can use Google Sheets to create your import data and export it as a CSV file by selecting **File → Download → Comma Separated Values (.csv)**. Google Sheets makes it easy to validate your data format before importing.
</Callout>

#### Example CSV File

To help you get started, we've provided an example CSV file, based on structure from [Property Setup](doc:property-setup) . This file contains sample data that will be used in the subsequent guide pages.

##### NOTE: Door Client Data that can be associated with OpenDoor data entities

* DOOR data type `ACCOUNT` (PORTFOLIO) → OpenDOOR data type `PORTFOLIO`
* DOOR data type `BUILDING` → OpenDOOR data type `PROPERTY`
* DOOR data type `UNIT` → OpenDOOR data type `UNIT`
* DOOR data type `DOOR` → OpenDOOR data type `ENTRANCE`

```Text import-into-OpenDOOR.csv
SPACE TYPE,BP SPACE NAME,BP SPACE PARENT NAME,LATCH UUID / ID
ACCOUNT,OpenDOOR Client Account,,
PORTFOLIO,ODC Portfolio 1,OpenDOOR Client Account,936037B4-9250-4778-BC81-57660C3A011B
PROPERTY,ODCP1 Property 1,ODC Portfolio 1,1765CB13-36D6-461A-9ACB-59D1A2CE9BF6
BUILDING,Parking Lot,ODCP1 Property 1,
ENTRANCE,Parking Lot Entrance,Parking Lot,91CB0934-83F0-447C-A1CA-2DE3C6E2C059
PARKING_GROUP,Staff Parking,Parking Lot,
PARKING_SLOT,Staff Slot 1,Staff Parking,
PARKING_SLOT,Staff Slot 10,Staff Parking,
PARKING_GROUP,Residents Parking,Parking Lot,
PARKING_SLOT,Residents Slot 1,Staff Parking,
PARKING_SLOT,Residents Slot 10,Staff Parking,
BUILDING,Residential Building,ODCP1 Property 1,
ENTRANCE,Residential Building Entrance,Residential Building,D7EE4D4D-3991-4D76-AD8A-7C1FA9B52459
COMMON_GROUP,Common Areas,Residential Building,
COMMON_AREA,Lobby,Common Areas,B54DCB51-7133-45AC-827E-80ABDF5D2B81
STORAGE_GROUP,Package Room,Common Areas,0DE7F460-0D2A-4181-94E6-EE3091ED311A
SERVICE,Delivery Service Door,Package Room,C44B0BA4-F048-44EF-85FF-97CDFC7106EF
STORAGE_SLOT,Lockbox 101,Package Room,
STORAGE_SLOT,Lockbox 310,Package Room,
COMMON_AREA,Elevator 1,Common Areas,E2331488-1E4A-4D0E-BE99-3CC5BE62431E
COMMON_AREA,Elevator 2,Common Areas,5EEDC7A7-CCDD-44EA-AC8D-9A8C505657E2
COMMON_GROUP,Amenities,Common Areas,C53D0577-E842-45E2-8459-F16A6C175A7B
ENTRANCE,Amenities Entrance,Amenities,FB7F93D5-514D-4B05-89FC-96F981788526
COMMON_AREA,Spa,Amenities,
ENTRANCE,Spa Door,Spa,172D2A44-971D-4653-AE2F-4B2B2E7BF456
COMMON_AREA,Gym,Amenities,
ENTRANCE,Gym Door,Gym,CFBE6B75-4B9A-4FCC-939D-538B51FBCB58
COMMON_AREA,Meeting Rooms,Amenities,
ENTRANCE,Meeting Rooms Door,Meeting Rooms,FABE83D5-2A4F-48DA-8B1A-33779F9C79D8
ROOM,Room 1,Meeting Rooms,
ROOM,Room 6,Meeting Rooms,
FLOOR,Floor 1,Residential Building,
UNIT,Floor 1 - Unit 101,Floor 1,831436
ENTRANCE,Floor 1 - Unit 101 Door,Floor 1 - Unit 101,AA58FE86-B93F-416B-B653-91ABE67C49B4
UNIT,Floor 1 - Unit 110,Floor 1,831438
ENTRANCE,Floor 1 - Unit 110 Door,Floor 1 - Unit 110,20BF8AE3-0CAC-487C-928F-82A4F344D0FC
FLOOR,Floor 2,Residential Building,
UNIT,Floor 2 - Unit 201,Floor 2,831440
ENTRANCE,Floor 2 - Unit 201 Door,Floor 2 - Unit 201,7E8CC077-B07E-4A44-AAA1-1DB05F6D48D2
UNIT,Floor 2 - Unit 210,Floor 2,831442
ENTRANCE,Floor 2 - Unit 210 Door,Floor 2 - Unit 210,1DFAC8E4-1192-48C9-B6CD-243C21C47265
FLOOR,Floor 3,Residential Building,
UNIT,Floor 3 - Unit 301,Floor 3,831444
ENTRANCE,Floor 3 - Unit 301 Door,Floor 3 - Unit 301,1E3ECFA4-18E2-4B17-9699-D262C2AC6A2B
UNIT,Floor 3 - Unit 310,Floor 3,831446
ENTRANCE,Floor 3 - Unit 310 Door,Floor 3 - Unit 310,2FA9AA99-7C67-4EA7-889E-ED96F039C23D
PROPERTY,ODCP1 Property 2,ODC Portfolio 1,251FEC1A-8B28-487C-9D57-E2B843AC51FF
PORTFOLIO,ODC Portfolio 2,OpenDOOR Client Account,0517C840-086B-4423-BE9E-2F021CB328B3
```

### Step 2: Prepare and Send Request!

#### Request definition:

<Callout icon="📋" theme="info">
  Here's how to structure your API request for importing CSV data.
</Callout>

<br />

| **Method** | **Host**                                               | **Path**                                  |
| ---------- | ------------------------------------------------------ | ----------------------------------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/blueprint-internal/v1/items/import-csv` |

**Headers:**

* **Authorization**: TBD
* **Content-Type**: `multipart/form-data`
* **Authorization** TBD

**File:**

* Name of your CSV file. For this example, we've used `import-into-OpenDOOR.csv` [Example CSV File](https://opendoor-uwel.readme.io/docs/migrate-from-legacy-property#example-csv-file).

```curl
curl -X 'POST' \
  'https://api.prod.door.com/blueprint-internal/v1/items/import-csv' \
  -H 'accept: */*' \
  -H 'x-door-auth: Bearer {token}' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@import-into-OpenDOOR.csv;type=text/csv'
```

### Step 3: Validate Response

Expected response is HTTP 200 and body containing the entire Directory tree structure and data from the input file.

```json Response
[
  {
    "id": "2018b94b-9df5-4456-9c5d-9e984993afee",
    "name": "OpenDOOR Client Account",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee",
    "tags": {
      "space:ACCOUNT": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:19Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "86fbee46-c57e-4f04-b584-e657e92521d2",
    "name": "ODC Portfolio 2",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::86fbee46-c57e-4f04-b584-e657e92521d2",
    "tags": {
      "space:PORTFOLIO": "",
      "item:SPACE": "",
      "cortex:ACCOUNT": "0517C840-086B-4423-BE9E-2F021CB328B3"
    },
    "createdAt": "2025-12-22T17:26:19Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "972e4151-0f73-4cd5-913e-70dd5fc8ad45",
    "name": "ODC Portfolio 1",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45",
    "tags": {
      "space:PORTFOLIO": "",
      "item:SPACE": "",
      "cortex:ACCOUNT": "936037B4-9250-4778-BC81-57660C3A011B"
    },
    "createdAt": "2025-12-22T17:26:19Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "2e4a1982-3f4f-4227-8932-77b42a0c524f",
    "name": "ODCP1 Property 2",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::2e4a1982-3f4f-4227-8932-77b42a0c524f",
    "tags": {
      "space:PROPERTY": "",
      "item:SPACE": "",
      "cortex:BUILDING": "251FEC1A-8B28-487C-9D57-E2B843AC51FF"
    },
    "createdAt": "2025-12-22T17:26:19Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "ea41ad14-3e2b-495b-b76a-a194217961cc",
    "name": "ODCP1 Property 1",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc",
    "tags": {
      "space:PROPERTY": "",
      "item:SPACE": "",
      "cortex:BUILDING": "1765CB13-36D6-461A-9ACB-59D1A2CE9BF6"
    },
    "createdAt": "2025-12-22T17:26:19Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "87d8db2a-669c-4013-956d-24f14a484db2",
    "name": "Parking Lot",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::87d8db2a-669c-4013-956d-24f14a484db2",
    "tags": {
      "space:BUILDING": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:19Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "ce118cfb-1a90-48fb-bf24-d0be22d66fa6",
    "name": "Residents Parking",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::87d8db2a-669c-4013-956d-24f14a484db2::ce118cfb-1a90-48fb-bf24-d0be22d66fa6",
    "tags": {
      "space:PARKING_GROUP": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "591ee5a3-e02a-4c86-a757-d1568ccd176b",
    "name": "Parking Lot Entrance",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::87d8db2a-669c-4013-956d-24f14a484db2::591ee5a3-e02a-4c86-a757-d1568ccd176b",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "91CB0934-83F0-447C-A1CA-2DE3C6E2C059"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "e617bf3a-97d3-4093-b7c5-023efeecbc0c",
    "name": "Staff Parking",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::87d8db2a-669c-4013-956d-24f14a484db2::e617bf3a-97d3-4093-b7c5-023efeecbc0c",
    "tags": {
      "space:PARKING_GROUP": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "61e6bb93-e566-4537-b2ed-5590f16b5a32",
    "name": "Residents Slot 10",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::87d8db2a-669c-4013-956d-24f14a484db2::e617bf3a-97d3-4093-b7c5-023efeecbc0c::61e6bb93-e566-4537-b2ed-5590f16b5a32",
    "tags": {
      "space:PARKING_SLOT": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "daa5b085-0830-4ac7-ae0f-b0b4669425fa",
    "name": "Staff Slot 1",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::87d8db2a-669c-4013-956d-24f14a484db2::e617bf3a-97d3-4093-b7c5-023efeecbc0c::daa5b085-0830-4ac7-ae0f-b0b4669425fa",
    "tags": {
      "space:PARKING_SLOT": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "3e494e3a-e1de-408a-a5aa-022d98f9e336",
    "name": "Staff Slot 10",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::87d8db2a-669c-4013-956d-24f14a484db2::e617bf3a-97d3-4093-b7c5-023efeecbc0c::3e494e3a-e1de-408a-a5aa-022d98f9e336",
    "tags": {
      "space:PARKING_SLOT": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "b4e18528-360a-47a3-b794-fa11dcb429bb",
    "name": "Residents Slot 1",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::87d8db2a-669c-4013-956d-24f14a484db2::e617bf3a-97d3-4093-b7c5-023efeecbc0c::b4e18528-360a-47a3-b794-fa11dcb429bb",
    "tags": {
      "space:PARKING_SLOT": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9",
    "name": "Residential Building",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9",
    "tags": {
      "space:BUILDING": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:19Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "4e5a5b10-0ed5-4aca-afae-2a94fd3d1277",
    "name": "Residential Building Entrance",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::4e5a5b10-0ed5-4aca-afae-2a94fd3d1277",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "D7EE4D4D-3991-4D76-AD8A-7C1FA9B52459"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "17cde9b1-0986-4869-a81b-5797cc7480ef",
    "name": "Floor 3",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::17cde9b1-0986-4869-a81b-5797cc7480ef",
    "tags": {
      "space:FLOOR": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:19Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "86a4196a-c754-4531-8532-21c2c0854edc",
    "name": "Floor 3 - Unit 301",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::17cde9b1-0986-4869-a81b-5797cc7480ef::86a4196a-c754-4531-8532-21c2c0854edc",
    "tags": {
      "space:UNIT": "",
      "item:SPACE": "",
      "cortex:UNIT": "831444"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "fbd9efd0-3651-4b0d-9fb4-8d4181e3fb2f",
    "name": "Floor 3 - Unit 301 Door",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::17cde9b1-0986-4869-a81b-5797cc7480ef::86a4196a-c754-4531-8532-21c2c0854edc::fbd9efd0-3651-4b0d-9fb4-8d4181e3fb2f",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "1E3ECFA4-18E2-4B17-9699-D262C2AC6A2B"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "b1682021-9643-494a-b632-29258b58bf5d",
    "name": "Floor 3 - Unit 310",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::17cde9b1-0986-4869-a81b-5797cc7480ef::b1682021-9643-494a-b632-29258b58bf5d",
    "tags": {
      "space:UNIT": "",
      "item:SPACE": "",
      "cortex:UNIT": "831446"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "6cdc0378-9cc0-4998-880e-f77551d47166",
    "name": "Floor 3 - Unit 310 Door",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::17cde9b1-0986-4869-a81b-5797cc7480ef::b1682021-9643-494a-b632-29258b58bf5d::6cdc0378-9cc0-4998-880e-f77551d47166",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "2FA9AA99-7C67-4EA7-889E-ED96F039C23D"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "75fbca56-8160-475c-9cac-46d06f1091ba",
    "name": "Floor 2",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::75fbca56-8160-475c-9cac-46d06f1091ba",
    "tags": {
      "space:FLOOR": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:19Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "ca461e44-715b-46ce-8056-a68693584a07",
    "name": "Floor 2 - Unit 201",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::75fbca56-8160-475c-9cac-46d06f1091ba::ca461e44-715b-46ce-8056-a68693584a07",
    "tags": {
      "space:UNIT": "",
      "item:SPACE": "",
      "cortex:UNIT": "831440"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "fa16cef9-ca45-43cf-ba08-0d305764f412",
    "name": "Floor 2 - Unit 201 Door",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::75fbca56-8160-475c-9cac-46d06f1091ba::ca461e44-715b-46ce-8056-a68693584a07::fa16cef9-ca45-43cf-ba08-0d305764f412",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "7E8CC077-B07E-4A44-AAA1-1DB05F6D48D2"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "f8f46e51-1804-4342-b649-5054753e284e",
    "name": "Floor 2 - Unit 210",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::75fbca56-8160-475c-9cac-46d06f1091ba::f8f46e51-1804-4342-b649-5054753e284e",
    "tags": {
      "space:UNIT": "",
      "item:SPACE": "",
      "cortex:UNIT": "831442"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "bc4ef7ac-c042-4c7a-922a-9909a5a0a25f",
    "name": "Floor 2 - Unit 210 Door",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::75fbca56-8160-475c-9cac-46d06f1091ba::f8f46e51-1804-4342-b649-5054753e284e::bc4ef7ac-c042-4c7a-922a-9909a5a0a25f",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "1DFAC8E4-1192-48C9-B6CD-243C21C47265"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "d9a86461-ecdc-4e0c-97fc-444ec130de73",
    "name": "Floor 1",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::d9a86461-ecdc-4e0c-97fc-444ec130de73",
    "tags": {
      "space:FLOOR": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "a4ae3ccc-6c7e-41f5-bfd4-72f65b3ca482",
    "name": "Floor 1 - Unit 101",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::d9a86461-ecdc-4e0c-97fc-444ec130de73::a4ae3ccc-6c7e-41f5-bfd4-72f65b3ca482",
    "tags": {
      "space:UNIT": "",
      "item:SPACE": "",
      "cortex:UNIT": "831436"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "96a975b8-b0a4-4eed-898f-3d65c6e361d0",
    "name": "Floor 1 - Unit 101 Door",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::d9a86461-ecdc-4e0c-97fc-444ec130de73::a4ae3ccc-6c7e-41f5-bfd4-72f65b3ca482::96a975b8-b0a4-4eed-898f-3d65c6e361d0",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "AA58FE86-B93F-416B-B653-91ABE67C49B4"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "7a1ad0e3-f2a9-4dd8-aaf7-c1f27b245820",
    "name": "Floor 1 - Unit 110",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::d9a86461-ecdc-4e0c-97fc-444ec130de73::7a1ad0e3-f2a9-4dd8-aaf7-c1f27b245820",
    "tags": {
      "space:UNIT": "",
      "item:SPACE": "",
      "cortex:UNIT": "831438"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "0b4adfe7-ca53-4c14-a048-e3bd81a44e52",
    "name": "Floor 1 - Unit 110 Door",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::d9a86461-ecdc-4e0c-97fc-444ec130de73::7a1ad0e3-f2a9-4dd8-aaf7-c1f27b245820::0b4adfe7-ca53-4c14-a048-e3bd81a44e52",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "20BF8AE3-0CAC-487C-928F-82A4F344D0FC"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "b3f10a8b-3cce-49ca-b470-92d0c6e4c656",
    "name": "Common Areas",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656",
    "tags": {
      "space:COMMON_GROUP": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "cbc0341f-bf91-42c3-bab7-becb5927461e",
    "name": "Lobby",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::cbc0341f-bf91-42c3-bab7-becb5927461e",
    "tags": {
      "space:COMMON_AREA": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "e7130ac6-b0a3-4f86-9856-da6a4a852357",
    "name": "Elevator 1",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::e7130ac6-b0a3-4f86-9856-da6a4a852357",
    "tags": {
      "space:COMMON_AREA": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "76b3cfc1-91b5-483b-b7c3-0daf78a4c7d1",
    "name": "Elevator 2",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::76b3cfc1-91b5-483b-b7c3-0daf78a4c7d1",
    "tags": {
      "space:COMMON_AREA": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "c3e9f3be-99d3-426e-8678-623da8e28e95",
    "name": "Package Room",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::c3e9f3be-99d3-426e-8678-623da8e28e95",
    "tags": {
      "space:STORAGE_GROUP": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "1af9dff9-1d1e-4b9e-bcda-ffac894e69c4",
    "name": "Delivery Service Door",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::c3e9f3be-99d3-426e-8678-623da8e28e95::1af9dff9-1d1e-4b9e-bcda-ffac894e69c4",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "C44B0BA4-F048-44EF-85FF-97CDFC7106EF"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "2bdcdc74-f531-4c78-a4f8-8726c35b05e7",
    "name": "Lockbox 310",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::c3e9f3be-99d3-426e-8678-623da8e28e95::2bdcdc74-f531-4c78-a4f8-8726c35b05e7",
    "tags": {
      "space:STORAGE_SLOT": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "d783b427-565a-477b-8545-db4853a21667",
    "name": "Lockbox 101",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::c3e9f3be-99d3-426e-8678-623da8e28e95::d783b427-565a-477b-8545-db4853a21667",
    "tags": {
      "space:STORAGE_SLOT": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "dc800aad-8264-41a6-bef0-e0ededcd213d",
    "name": "Amenities",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::dc800aad-8264-41a6-bef0-e0ededcd213d",
    "tags": {
      "space:COMMON_GROUP": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "66daf37d-120a-434b-a138-b3882695e774",
    "name": "Amenities Entrance",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::dc800aad-8264-41a6-bef0-e0ededcd213d::66daf37d-120a-434b-a138-b3882695e774",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "FB7F93D5-514D-4B05-89FC-96F981788526"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "22151f31-58ba-415e-8d58-88eef1cb568d",
    "name": "Meeting Rooms",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::dc800aad-8264-41a6-bef0-e0ededcd213d::22151f31-58ba-415e-8d58-88eef1cb568d",
    "tags": {
      "space:COMMON_AREA": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "4404ece7-1b70-42d6-89af-31a1211b7ce2",
    "name": "Room 6",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::dc800aad-8264-41a6-bef0-e0ededcd213d::22151f31-58ba-415e-8d58-88eef1cb568d::4404ece7-1b70-42d6-89af-31a1211b7ce2",
    "tags": {
      "space:ROOM": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "473cdefb-5728-4c65-8e5e-970a26562504",
    "name": "Room 1",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::dc800aad-8264-41a6-bef0-e0ededcd213d::22151f31-58ba-415e-8d58-88eef1cb568d::473cdefb-5728-4c65-8e5e-970a26562504",
    "tags": {
      "space:ROOM": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "44581365-7c22-4025-9650-d08b1e8ddc20",
    "name": "Meeting Rooms Door",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::dc800aad-8264-41a6-bef0-e0ededcd213d::22151f31-58ba-415e-8d58-88eef1cb568d::44581365-7c22-4025-9650-d08b1e8ddc20",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "FABE83D5-2A4F-48DA-8B1A-33779F9C79D8"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "1e7a7823-0412-4215-8a35-427d63058d7f",
    "name": "Spa",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::dc800aad-8264-41a6-bef0-e0ededcd213d::1e7a7823-0412-4215-8a35-427d63058d7f",
    "tags": {
      "space:COMMON_AREA": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "d8f76a3b-8269-48ee-8c7f-be959b66391b",
    "name": "Spa Door",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::dc800aad-8264-41a6-bef0-e0ededcd213d::1e7a7823-0412-4215-8a35-427d63058d7f::d8f76a3b-8269-48ee-8c7f-be959b66391b",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "172D2A44-971D-4653-AE2F-4B2B2E7BF456"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "133c3edc-ed4b-4a34-9d90-633150b89250",
    "name": "Gym",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::dc800aad-8264-41a6-bef0-e0ededcd213d::133c3edc-ed4b-4a34-9d90-633150b89250",
    "tags": {
      "space:COMMON_AREA": "",
      "item:SPACE": ""
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  },
  {
    "id": "02f19ffd-c9ed-44d5-8f41-3637d49e797d",
    "name": "Gym Door",
    "path": "::2018b94b-9df5-4456-9c5d-9e984993afee::972e4151-0f73-4cd5-913e-70dd5fc8ad45::ea41ad14-3e2b-495b-b76a-a194217961cc::62f5f7f3-0c03-4e5f-8299-25c6e3a4fff9::b3f10a8b-3cce-49ca-b470-92d0c6e4c656::dc800aad-8264-41a6-bef0-e0ededcd213d::133c3edc-ed4b-4a34-9d90-633150b89250::02f19ffd-c9ed-44d5-8f41-3637d49e797d",
    "tags": {
      "space:ENTRANCE": "",
      "item:SPACE": "",
      "cortex:DOOR": "CFBE6B75-4B9A-4FCC-939D-538B51FBCB58"
    },
    "createdAt": "2025-12-22T17:26:20Z",
    "createdBy": {
      "authorType": "USER",
      "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
    }
  }
]
```

<br />

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

To help you get started, we've provided an example CSV file. This file contains sample data that will be used in the subsequent guide pages.

```Text import-into-OpenDOOR.csv
`SPACE TYPE,BP SPACE NAME,BP SPACE PARENT NAME,LATCH UUID / ID
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

Request definition:

* Method: POST
* Host: https://api.prod.door.com
* Path: `blueprint-internal/v1/items/import-csv`
* Headers:
  * Authorization TBD
* File: 

```curl
curl -X 'POST' \
  'https://api.prod.door.com/blueprint-internal/v1/items/import-csv' \
  -H 'accept: */*' \
  -H 'x-door-auth: Bearer {token}' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@import-into-OpenDOOR.csv;type=text/csv'
```

### Step 3: Validate Response

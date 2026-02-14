---
title: Bulk Import Property Data
excerpt: Send a CSV file to your DOOR Sales Representative
deprecated: false
hidden: false
metadata:
  robots: index
next:
  pages:
    - slug: assign-locks-to-directories
      title: 2. Directory Locks Setup
      type: basic
---
<Callout icon="⚠️" theme="warning">
  **Important Note:** If you are using the method shown on this page and your locks have already been installed, you may **skip** the next step: [2. Directory Locks Setup](doc:assign-locks-to-directories). Your DOOR Sales Representative will have already assigned your Locks to the provided Directory items.
</Callout>

### Step 1: Organize your Directory Structure in a CSV file

The CSV file should have the following header: `SPACE TYPE,BP SPACE NAME,BP SPACE PARENT NAME`.

<Accordion title="CSV Structure Guidelines" icon="list">
  1. `SPACE TYPE`:
     1. Represents the type of Space in the Client Directory tree. It should match the type in the DOOR Client Account.
     2. **Possible values:** `ACCOUNT`, `PORTFOLIO`, `PROPERTY`, `BUILDING`, `FLOOR`, `UNIT`, `ROOM`, `PARKING_GROUP`, `PARKING_SLOT`, `STORAGE_GROUP`, `STORAGE_SLOT`, `COMMON_GROUP`, `COMMON_AREA`, `PRIVATE_GROUP`, `PRIVATE_AREA` and `ENTRANCE`
  2. `BP SPACE NAME`: The name of the desired Directory Item.
  3. `BP SPACE PARENT NAME`: The name of the Parent Directory Item, which must *exactly* match a previous row.
</Accordion>

#### Create your CSV file and populate it with import data

<Callout icon="📝" theme="default">
  **Tip:** Use your preferred spreadsheet software to create the data, then export it as a CSV file. For example, with Google Sheets, select **File → Download → Comma Separated Values (.csv)**. Microsoft Excel, Numbers and LibreOffice Calc all offer similar export capabilities; feel free to use whichever tool your organization commonly uses for spreadsheets.
</Callout>

#### Example CSV File

The following example CSV file should help you get started. It is based on the [Example Directory Structure](doc:example-directory-structure). The subsequent guide pages will continue to refer to this directory structure as an example, but you should define and submit your own directory structure instead.

```less import-into-OpenDOOR.csv
SPACE TYPE,BP SPACE NAME,BP SPACE PARENT NAME
ACCOUNT,OpenDOOR Client Account,
PORTFOLIO,ODC Portfolio 1,OpenDOOR Client Account
PROPERTY,ODCP1 Property 1,ODC Portfolio 1
BUILDING,Parking Lot,ODCP1 Property 1
ENTRANCE,Parking Lot Entrance,Parking Lot
PARKING_GROUP,Staff Parking,Parking Lot
PARKING_SLOT,Staff Slot 1,Staff Parking
PARKING_SLOT,Staff Slot 10,Staff Parking
PARKING_GROUP,Residents Parking,Parking Lot
PARKING_SLOT,Residents Slot 1,Staff Parking
PARKING_SLOT,Residents Slot 10,Staff Parking
BUILDING,Residential Building,ODCP1 Property 1
ENTRANCE,Residential Building Entrance,Residential Building
COMMON_GROUP,Common Areas,Residential Building
COMMON_AREA,Lobby,Common Areas
STORAGE_GROUP,Package Room,Common Areas
SERVICE,Delivery Service Door,Package Room
STORAGE_SLOT,Lockbox 101,Package Room
STORAGE_SLOT,Lockbox 310,Package Room
COMMON_AREA,Elevator 1,Common Areas
COMMON_AREA,Elevator 2,Common Areas
COMMON_GROUP,Amenities,Common Areas
ENTRANCE,Amenities Entrance,Amenities
COMMON_AREA,Spa,Amenities
ENTRANCE,Spa Door,Spa
COMMON_AREA,Gym,Amenities
ENTRANCE,Gym Door,Gym
COMMON_AREA,Meeting Rooms,Amenities
ENTRANCE,Meeting Rooms Door,Meeting Rooms
ROOM,Room 1,Meeting Rooms
ROOM,Room 6,Meeting Rooms
FLOOR,Floor 1,Residential Building
UNIT,Floor 1 - Unit 101,Floor 1
ENTRANCE,Floor 1 - Unit 101 Door,Floor 1 - Unit 101
UNIT,Floor 1 - Unit 110,Floor 1
ENTRANCE,Floor 1 - Unit 110 Door,Floor 1 - Unit 110
FLOOR,Floor 2,Residential Building
UNIT,Floor 2 - Unit 201,Floor 2
ENTRANCE,Floor 2 - Unit 201 Door,Floor 2 - Unit 201
UNIT,Floor 2 - Unit 210,Floor 2
ENTRANCE,Floor 2 - Unit 210 Door,Floor 2 - Unit 210
FLOOR,Floor 3,Residential Building
UNIT,Floor 3 - Unit 301,Floor 3
ENTRANCE,Floor 3 - Unit 301 Door,Floor 3 - Unit 301
UNIT,Floor 3 - Unit 310,Floor 3
ENTRANCE,Floor 3 - Unit 310 Door,Floor 3 - Unit 310
PROPERTY,ODCP1 Property 2,ODC Portfolio 1
PORTFOLIO,ODC Portfolio 2,OpenDOOR Client Account
```

### Step 2: Send the file to your DOOR Sales Representative

They will check your file, provide feedback on its contents, and create the directory items.

<br />

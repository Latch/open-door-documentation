---
title: Bulk Import Property Data
deprecated: false
hidden: false
metadata:
  robots: index
---
### Step 1: Organize DOOR Client Account data in a CSV file

#### Column meaning and specifications:

1. `SPACE TYPE`:
   1. Type of Space represented by the row (future Directory Item) in the Client Directory tree. It should be the same type as in the DOOR Client Account.
   2. **Possible values:** `ROOT`, `ACCOUNT`, `PORTFOLIO`, `PROPERTY`, `BUILDING`, `FLOOR`, `UNIT`, `ROOM`, `PARKING_GROUP`, `PARKING_SLOT`, `STORAGE_GROUP`, `STORAGE_SLOT`, `COMMON_GROUP`, `COMMON_AREA`, `PRIVATE_GROUP`, `PRIVATE_AREA` and `ENTRANCE`
2. `BP SPACE NAME`: Directory Item name. It should be the same as the DOOR Client Account entity name.
3. `BP SPACE PARENT NAME`: Name of the Parent Directory Item. It should be from a previous row and should be a perfect String match.
4. `LATCH UUID / ID`: Latch UUID of the entity, be it Portfolio, Property, Unit, Door/Lock, and so on. It can be obtained from DoorOS or AdminTool.

<br />

<Accordion title="Column Specifications" icon="fa-table">
  **SPACE TYPE** - Type of Space represented by the row (future Directory Item)

  * **Values:** `ROOT`, `ACCOUNT`, `PORTFOLIO`, `PROPERTY`, `BUILDING`, `FLOOR`, `UNIT`, `ROOM`, `PARKING_GROUP`, `PARKING_SLOT`, `STORAGE_GROUP`, `STORAGE_SLOT`, `COMMON_GROUP`, `COMMON_AREA`, `PRIVATE_GROUP`, `PRIVATE_AREA`, `ENTRANCE`

  **BP SPACE NAME** - Directory Item name (matches DOOR Client Account entity name)

  **BP SPACE PARENT NAME** - Parent Directory Item name (must match previous row exactly)

  **LATCH UUID / ID** - Entity UUID from DoorOS or AdminTool
</Accordion>

<br />

#### TIP: You can use Google Sheets to create the import table, populate it and then export it as CSV following options File → Download → Comma Separated Values (.csv)

Create your import data

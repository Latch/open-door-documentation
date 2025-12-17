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

<Cards columns={2}>
  <Card title="SPACE TYPE" icon="fa-building">
    Type of Space represented by the row (future Directory Item) in the Client Directory tree. Should match the DOOR Client Account type.

    **Values:** `ROOT`, `ACCOUNT`, `PORTFOLIO`, `PROPERTY`, `BUILDING`, `FLOOR`, `UNIT`, `ROOM`, `PARKING_GROUP`, `PARKING_SLOT`, `STORAGE_GROUP`, `STORAGE_SLOT`, `COMMON_GROUP`, `COMMON_AREA`, `PRIVATE_GROUP`, `PRIVATE_AREA`, `ENTRANCE`
  </Card>

  <Card title="BP SPACE NAME" icon="fa-tag">
    Directory Item name. Should match the DOOR Client Account entity name.
  </Card>

  <Card title="BP SPACE PARENT NAME" icon="fa-sitemap">
    Name of the Parent Directory Item. Must be from a previous row and be a perfect String match.
  </Card>

  <Card title="LATCH UUID / ID" icon="fa-key">
    Latch UUID of the entity (Portfolio, Property, Unit, Door/Lock, etc.). Available from DoorOS or AdminTool.
  </Card>
</Cards>

#### TIP: You can use Google Sheets to create the import table, populate it and then export it as CSV following options File → Download → Comma Separated Values (.csv)

Create your import data 

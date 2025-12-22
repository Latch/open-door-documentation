---
title: Bulk Import Property Data
deprecated: false
hidden: false
metadata:
  robots: index
---
### Step 1: Organize DOOR Client Account data in a CSV file

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

<br />

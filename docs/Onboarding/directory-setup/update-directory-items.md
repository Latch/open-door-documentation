---
title: Update Directory Items
deprecated: false
hidden: false
metadata:
  robots: index
---
sadasd

| **Method** | **Host**                                               | **Path**                     | Details                                               |
| :--------- | :----------------------------------------------------- | :--------------------------- | :---------------------------------------------------- |
| PATCH      | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/items/{uuid}` | Update Directory Item data, identified by its `uuid`. |

**URL parameters:**

* **This is applicable only for listing endpoints `/directory/v1/subtree` and `/directory/v1/subtree/{scope}`**. See usage example in [`GET /directory/v1/subtree/{scope}` endpoint to retrieve information about a known Directory Item](https://opendoor-uwel.readme.io/docs/get-directory-items#2-get-directoryv1subtreescope-endpoint-to-retrieve-information-about-a-known-directory-item-1).
* `pageSize`: Specify the number of items to be returned in a single page of results when listing Directory Items. It helps control the amount of data retrieved in one request, allowing for efficient data handling and navigation through large datasets.
* `pageToken`: Specify the starting point (ID/UUID) for the next page of data in a paginated list. When combined with pageSize, it allows for efficient navigation through large datasets by fetching subsequent pages of results.

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: TBD

### Example Usages

We'll be using as example `uuid = 972e4151-0f73-4cd5-913e-70dd5fc8ad45` (`ODC Portfolio 1` Directory Item) from [Bulk Import Property Data → Step 3. Validate Response](doc:https://opendoor-uwel.readme.io/docs/migrate-from-legacy-property#step-3-validate-response).

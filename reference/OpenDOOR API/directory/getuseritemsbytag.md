---
title: Get visible directory items by tag
excerpt: >-
  Gets directory items visible to the current user, filtered by a specific tag.
  Searches ancestors first, then subtree if no ancestor match is found.
  Pagination is best-effort: the first page includes all ancestor matches before
  subtree traversal, so the number of returned items may exceed pageSize.
api:
  file: blueprint-openapi.json
  operationId: getUserItemsByTag
hidden: false
---
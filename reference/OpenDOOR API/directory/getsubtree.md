---
title: Gets all the nodes starting from the root item recursively.
excerpt: >-
  This endpoint can be used to retrieve a paginated parent-first subtree of a
  directory item. 
          The subtree is returned in a paginated format, with each page containing a specified number of nodes. 
          The nodes are returned in a parent-first order, meaning that the parent nodes are returned before their child nodes. 
          The subtree can be filtered by tags and the depth of the subtree can be specified. 
          Additionally a set of tags can be specified to filter the subtree by.
api:
  file: blueprint-openapi.json
  operationId: getSubtree
hidden: false
---
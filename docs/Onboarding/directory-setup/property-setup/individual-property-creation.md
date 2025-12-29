---
title: Individual Property Creation
excerpt: POST Directory Item(s).
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
<br />

<Callout icon="⚠️" theme="warning">
  **Important Note:** If you've provided Lock ID/UUIDs and they appear in successful responses body (end of this page), you don't have to complete [2. Directory Locks Setup](doc:assign-locks-to-directories) for them anymore, the Lock is assigned to the created Directory.
</Callout>

<Callout icon="📝" theme="default">
  **How to use below endpoints:**

  1. `/directory/v1/items` to create the initial Directory structure, can even be complete at the moment.
  2. `/directory/v1/items/{scope}` to create additional Directory Items and link them to an existing Item, identified by `scope`.
</Callout>

**Request Definitions:**

| **Method** | **Host**                                               | **Path**                      | Details                                                           |
| :--------- | :----------------------------------------------------- | :---------------------------- | :---------------------------------------------------------------- |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/items`         | Create a Directory Item and its subtree.                          |
| POST       | [https://api.prod.door.com](https://api.prod.door.com) | `/directory/v1/items/{scope}` | Create a Directory Item under the given `scope` (Directory Item). |

**Headers:**

* **`accept`**: `*/*`
* **`Authorization`**: TBD
* **`Content-Type`**: `application/json`

**Request Body:** uses below structure . `children` JSON property can accommodate an entire nested Directory structure, so the Directory can be built in one request.

```json Request Body Structure
{
  "name": "string",
  "tags": {
    "additionalProp1": "string",
    "additionalProp2": "string",
    "additionalProp3": "string"
  },
  "children": [
    "string"
  ]
}
```

### Create Entire Directory Structure in One Request

#### Step 1: Prepare JSON Request Body

We'll be using Directory structure from [Property Setup](doc:property-setup) as an example. It contains sample data that will be used in the subsequent guide pages. We're leaving out some Lock Assignments/Associations to Directories and some Directory items, that will be used in later Steps.

```json Request Body
{
    "name": "OpenDOOR Client Account",
    "tags": {
        "space:ACCOUNT": "",
        "item:SPACE": ""
    },
    "children": [
        {
            "name": "ODC Portfolio 1",
            "tags": {
                "space:PORTFOLIO": "",
                "item:SPACE": "",
                "cortex:ACCOUNT": "936037B4-9250-4778-BC81-57660C3A011B"
            },
            "children": [
                {
                    "name": "ODCP1 Property 1",
                    "tags": {
                        "space:PROPERTY": "",
                        "item:SPACE": "",
                        "cortex:BUILDING": "1765CB13-36D6-461A-9ACB-59D1A2CE9BF6"
                    },
                    "children": [
                        {
                            "name": "Parking Lot",
                            "tags": {
                                "space:BUILDING": "",
                                "item:SPACE": ""
                            },
                            "children": [
                                {
                                    "name": "Parking Lot Entrance",
                                    "tags": {
                                        "space:ENTRANCE": "",
                                        "item:SPACE": ""
                                    }
                                },
                                {
                                    "name": "Staff Parking",
                                    "tags": {
                                        "space:PARKING_GROUP": "",
                                        "item:SPACE": ""
                                    },
                                    "children": [
                                        {
                                            "name": "Staff Slot 1",
                                            "tags": {
                                                "space:PARKING_SLOT": "",
                                                "item:SPACE": ""
                                            }
                                        },
                                        {
                                            "name": "Staff Slot 10",
                                            "tags": {
                                                "space:PARKING_SLOT": "",
                                                "item:SPACE": ""
                                            }
                                        }
                                    ]
                                },
                                {
                                    "name": "Residents Parking",
                                    "tags": {
                                        "space:PARKING_GROUP": "",
                                        "item:SPACE": ""
                                    },
                                    "children": [
                                        {
                                            "name": "Residents Slot 1",
                                            "tags": {
                                                "space:PARKING_SLOT": "",
                                                "item:SPACE": ""
                                            }
                                        },
                                        {
                                            "name": "Residents Slot 10",
                                            "tags": {
                                                "space:PARKING_SLOT": "",
                                                "item:SPACE": ""
                                            }
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "Residential Building",
                            "tags": {
                                "space:BUILDING": "",
                                "item:SPACE": ""
                            },
                            "children": [
                                {
                                    "name": "Residential Building Entrance",
                                    "tags": {
                                        "space:ENTRANCE": "",
                                        "item:SPACE": "",
                                        "cortex:DOOR": "D7EE4D4D-3991-4D76-AD8A-7C1FA9B52459"
                                    }
                                },
                                {
                                    "name": "Common Areas",
                                    "tags": {
                                        "space:COMMON_GROUP": "",
                                        "item:SPACE": ""
                                    },
                                    "children": [
                                        {
                                            "name": "Lobby",
                                            "tags": {
                                                "space:COMMON_AREA": "",
                                                "item:SPACE": ""
                                            }
                                        },
                                        {
                                            "name": "Package Room",
                                            "tags": {
                                                "space:STORAGE_GROUP": "",
                                                "item:SPACE": ""
                                            },
                                            "children": [
                                                {
                                                    "name": "Delivery Service Door",
                                                    "tags": {
                                                        "space:ENTRANCE": "",
                                                        "item:SPACE": "",
                                                        "cortex:DOOR": "C44B0BA4-F048-44EF-85FF-97CDFC7106EF"
                                                    }
                                                },
                                                {
                                                    "name": "Lockbox 101",
                                                    "tags": {
                                                        "space:STORAGE_SLOT": "",
                                                        "item:SPACE": ""
                                                    }
                                                },
                                                {
                                                    "name": "Lockbox 310",
                                                    "tags": {
                                                        "space:STORAGE_SLOT": "",
                                                        "item:SPACE": ""
                                                    }
                                                }
                                            ]
                                        },
                                        {
                                            "name": "Elevator 1",
                                            "tags": {
                                                "space:COMMON_AREA": "",
                                                "item:SPACE": ""
                                            }
                                        },
                                        {
                                            "name": "Elevator 2",
                                            "tags": {
                                                "space:COMMON_AREA": "",
                                                "item:SPACE": ""
                                            }
                                        },
                                        {
                                            "name": "Amenities",
                                            "tags": {
                                                "space:COMMON_GROUP": "",
                                                "item:SPACE": ""
                                            },
                                            "children": [
                                                {
                                                    "name": "Amenities Entrance",
                                                    "tags": {
                                                        "space:ENTRANCE": "",
                                                        "item:SPACE": "",
                                                        "cortex:DOOR": "FB7F93D5-514D-4B05-89FC-96F981788526"
                                                    }
                                                },
                                                {
                                                    "name": "Spa",
                                                    "tags": {
                                                        "space:COMMON_AREA": "",
                                                        "item:SPACE": ""
                                                    },
                                                    "children": [
                                                        {
                                                            "name": "Spa Door",
                                                            "tags": {
                                                                "space:ENTRANCE": "",
                                                                "item:SPACE": "",
                                                                "cortex:DOOR": "172D2A44-971D-4653-AE2F-4B2B2E7BF456"
                                                            }
                                                        }
                                                    ]
                                                },
                                                {
                                                    "name": "Gym",
                                                    "tags": {
                                                      "space:COMMON_AREA": "",
                                                      "item:SPACE": ""
                                                    },
                                                    "children": [
                                                        {
                                                            "name": "Gym Door",
                                                            "tags": {
                                                                "space:ENTRANCE": "",
                                                                "item:SPACE": "",
                                                                "cortex:DOOR": "CFBE6B75-4B9A-4FCC-939D-538B51FBCB58"
                                                            }
                                                        }
                                                    ]
                                                },
                                                {
                                                    "name": "Meeting Rooms",
                                                    "tags": {
                                                        "space:COMMON_AREA": "",
                                                        "item:SPACE": ""
                                                    },
                                                    "children": [
                                                        {
                                                            "name": "Meeting Rooms Door",
                                                            "tags": {
                                                                "space:ENTRANCE": "",
                                                                "item:SPACE": "",
                                                                "cortex:DOOR": "FABE83D5-2A4F-48DA-8B1A-33779F9C79D8"
                                                            }
                                                        },
                                                        {
                                                            "name": "Room 1",
                                                            "tags": {
                                                                "space:ROOM": "",
                                                                "item:SPACE": ""
                                                            }
                                                        },
                                                        {
                                                            "name": "Room 6",
                                                            "tags": {
                                                                "space:ROOM": "",
                                                                "item:SPACE": ""
                                                            }
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "name": "Floor 1",
                                    "tags": {
                                        "space:FLOOR": "",
                                        "item:SPACE": ""
                                    },
                                    "children": [
                                        {
                                            "name": "Floor 1 - Unit 101",
                                            "tags": {
                                                "space:UNIT": "",
                                                "item:SPACE": "",
                                                "cortex:UNIT": "831436"
                                            },
                                            "children": [
                                                {
                                                    "name": "Floor 1 - Unit 101 Door",
                                                    "tags": {
                                                        "space:ENTRANCE": "",
                                                        "item:SPACE": "",
                                                        "cortex:DOOR": "AA58FE86-B93F-416B-B653-91ABE67C49B4"
                                                    }
                                                }
                                            ]
                                        },
                                        {
                                            "name": "Floor 1 - Unit 110",
                                            "tags": {
                                                "space:UNIT": "",
                                                "item:SPACE": "",
                                                "cortex:UNIT": "831438"
                                            },
                                            "children": [
                                                {
                                                    "name": "Floor 1 - Unit 110 Door",
                                                    "tags": {
                                                        "space:ENTRANCE": "",
                                                        "item:SPACE": "",
                                                        "cortex:DOOR": "20BF8AE3-0CAC-487C-928F-82A4F344D0FC"
                                                    }
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "name": "Floor 2",
                                    "tags": {
                                        "space:FLOOR": "",
                                        "item:SPACE": ""
                                    },
                                    "children": [
                                        {
                                            "name": "Floor 2 - Unit 201",
                                            "tags": {
                                                "space:UNIT": "",
                                                "item:SPACE": "",
                                                "cortex:UNIT": "831440"
                                            },
                                            "children": [
                                                {
                                                    "name": "Floor 2 - Unit 201 Door",
                                                    "tags": {
                                                        "space:ENTRANCE": "",
                                                        "item:SPACE": "",
                                                        "cortex:DOOR": "7E8CC077-B07E-4A44-AAA1-1DB05F6D48D2"
                                                    }
                                                }
                                            ]
                                        },
                                        {
                                            "name": "Floor 2 - Unit 210",
                                            "tags": {
                                                "space:UNIT": "",
                                                "item:SPACE": "",
                                                "cortex:UNIT": "831442"
                                            },
                                            "children": [
                                                {
                                                    "name": "Floor 2 - Unit 210 Door",
                                                    "tags": {
                                                        "space:ENTRANCE": "",
                                                        "item:SPACE": "",
                                                        "cortex:DOOR": "1DFAC8E4-1192-48C9-B6CD-243C21C47265"
                                                    }
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "name": "Floor 3",
                                    "tags": {
                                        "space:FLOOR": "",
                                        "item:SPACE": ""
                                    },
                                    "children": [
                                        {
                                            "name": "Floor 3 - Unit 301",
                                            "tags": {
                                                "space:UNIT": "",
                                                "item:SPACE": "",
                                                "cortex:UNIT": "831444"
                                            },
                                            "children": [
                                                {
                                                    "name": "Floor 3 - Unit 301 Door",
                                                    "tags": {
                                                        "space:ENTRANCE": "",
                                                        "item:SPACE": "",
                                                        "cortex:DOOR": "1E3ECFA4-18E2-4B17-9699-D262C2AC6A2B"
                                                    }
                                                }
                                            ]
                                        },
                                        {
                                            "name": "Floor 3 - Unit 310",
                                            "tags": {
                                                "space:UNIT": "",
                                                "item:SPACE": "",
                                                "cortex:UNIT": "831446"
                                            },
                                            "children": [
                                                {
                                                    "name": "Floor 3 - Unit 310 Door",
                                                    "tags": {
                                                        "space:ENTRANCE": "",
                                                        "item:SPACE": "",
                                                        "cortex:DOOR": "2FA9AA99-7C67-4EA7-889E-ED96F039C23D"
                                                    }
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "name": "ODC Portfolio 2",
            "tags": {
              "space:PORTFOLIO": "",
              "item:SPACE": "",
              "cortex:ACCOUNT": "0517C840-086B-4423-BE9E-2F021CB328B3"
            }
        }  
    ]
}
```

#### Step 2: Send Request!

Using JSON from [Step 1: Prepare JSON Request Body](https://opendoor-uwel.readme.io/docs/individual-property-creation#step-1-prepare-json-request-body):

```curl
curl -X 'POST' \
  'https://api.prod.door.com/directory/v1/items' \
  -H 'accept: */*' \
  -H 'Authorization: Bearer {token}' \
  -H 'Content-Type: application/json' \
  -d '{
		...
  }'
```

#### Step 3: Validate Response

Response should successful, HTTP 200 and body containing the root Directory Item.

```json Response
{
  "id": "e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
  "name": "OpenDOOR Client Account",
  "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
  "tags": {
    "space:ACCOUNT": "",
    "item:SPACE": ""
  },
  "createdAt": "2025-12-29T16:38:44Z",
  "createdBy": {
    "authorType": "USER",
    "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
  }
}
```

#### Step 4: Retrieve the entire Directory Subtree

Sending a [GET Directory Subtree](https://opendoor-uwel.readme.io/docs/get-directory-items#2-get-directoryv1subtreescope-endpoint-to-retrieve-information-about-directory-items-from-a-known-subtree) request with `pageSize = 50` and `scope = e43f4017-da92-4c4a-87ff-5c5f418c3cf6` should get you the entire Directory starting from Root Item from above Response.

```json Directory Subtree JSON
{
  "items": [
    {
      "id": "e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
      "name": "OpenDOOR Client Account",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6",
      "tags": {
        "space:ACCOUNT": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "4a9fc553-e920-499b-92b1-fd08e7507b91",
      "name": "ODC Portfolio 1",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91",
      "tags": {
        "space:PORTFOLIO": "",
        "item:SPACE": "",
        "cortex:ACCOUNT": "936037B4-9250-4778-BC81-57660C3A011B"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "8ae57cb5-206e-4f2b-9f71-879024309ea1",
      "name": "ODCP1 Property 1",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1",
      "tags": {
        "space:PROPERTY": "",
        "item:SPACE": "",
        "cortex:BUILDING": "1765CB13-36D6-461A-9ACB-59D1A2CE9BF6"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "02ab66db-d4cb-4148-905f-e6545259db41",
      "name": "Residential Building",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41",
      "tags": {
        "space:BUILDING": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "1dcdccde-fe58-4887-b6c7-5929de1d4b29",
      "name": "Common Areas",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29",
      "tags": {
        "space:COMMON_GROUP": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "064fd175-31a0-4611-8269-2ef43f725a2f",
      "name": "Elevator 2",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::064fd175-31a0-4611-8269-2ef43f725a2f",
      "tags": {
        "space:COMMON_AREA": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "39a412c1-ea20-40fd-b938-1609d7a0921e",
      "name": "Amenities",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::39a412c1-ea20-40fd-b938-1609d7a0921e",
      "tags": {
        "space:COMMON_GROUP": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "049313c6-d483-491d-8429-19129dfb181f",
      "name": "Amenities Entrance",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::39a412c1-ea20-40fd-b938-1609d7a0921e::049313c6-d483-491d-8429-19129dfb181f",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "FB7F93D5-514D-4B05-89FC-96F981788526"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "4c6d7e54-f77d-4564-ac7b-f2644c6e7637",
      "name": "Spa",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::39a412c1-ea20-40fd-b938-1609d7a0921e::4c6d7e54-f77d-4564-ac7b-f2644c6e7637",
      "tags": {
        "space:COMMON_AREA": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "24c44308-ecb3-4db1-9cf1-deb758f4dc9a",
      "name": "Spa Door",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::39a412c1-ea20-40fd-b938-1609d7a0921e::4c6d7e54-f77d-4564-ac7b-f2644c6e7637::24c44308-ecb3-4db1-9cf1-deb758f4dc9a",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "172D2A44-971D-4653-AE2F-4B2B2E7BF456"
      },
      "createdAt": "2025-12-29T16:38:45Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "5ab1929d-a085-4d85-8c34-6b6fda0239cf",
      "name": "Gym",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::39a412c1-ea20-40fd-b938-1609d7a0921e::5ab1929d-a085-4d85-8c34-6b6fda0239cf",
      "tags": {
        "space:COMMON_AREA": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:45Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "5af43e29-cd9a-4a74-a815-c8d1ff0b6384",
      "name": "Gym Door",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::39a412c1-ea20-40fd-b938-1609d7a0921e::5ab1929d-a085-4d85-8c34-6b6fda0239cf::5af43e29-cd9a-4a74-a815-c8d1ff0b6384",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "CFBE6B75-4B9A-4FCC-939D-538B51FBCB58"
      },
      "createdAt": "2025-12-29T16:38:45Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "681777ad-79af-43c8-970e-6ad44fd6976f",
      "name": "Meeting Rooms",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::39a412c1-ea20-40fd-b938-1609d7a0921e::681777ad-79af-43c8-970e-6ad44fd6976f",
      "tags": {
        "space:COMMON_AREA": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "07e8c489-ca09-47f9-ac05-52a0d161fad3",
      "name": "Room 6",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::39a412c1-ea20-40fd-b938-1609d7a0921e::681777ad-79af-43c8-970e-6ad44fd6976f::07e8c489-ca09-47f9-ac05-52a0d161fad3",
      "tags": {
        "space:ROOM": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:45Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "39d282ed-06dc-4947-8ee3-b882ba56cdb3",
      "name": "Meeting Rooms Door",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::39a412c1-ea20-40fd-b938-1609d7a0921e::681777ad-79af-43c8-970e-6ad44fd6976f::39d282ed-06dc-4947-8ee3-b882ba56cdb3",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "FABE83D5-2A4F-48DA-8B1A-33779F9C79D8"
      },
      "createdAt": "2025-12-29T16:38:45Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "c9c323a0-c0ee-4b16-811a-65f4e191cd57",
      "name": "Room 1",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::39a412c1-ea20-40fd-b938-1609d7a0921e::681777ad-79af-43c8-970e-6ad44fd6976f::c9c323a0-c0ee-4b16-811a-65f4e191cd57",
      "tags": {
        "space:ROOM": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:45Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "4b15f3d0-83c5-41dc-a0dc-fed33afba6c4",
      "name": "Package Room",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::4b15f3d0-83c5-41dc-a0dc-fed33afba6c4",
      "tags": {
        "space:STORAGE_GROUP": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "06245e70-ed58-4bcf-ad70-77286313b70f",
      "name": "Lockbox 101",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::4b15f3d0-83c5-41dc-a0dc-fed33afba6c4::06245e70-ed58-4bcf-ad70-77286313b70f",
      "tags": {
        "space:STORAGE_SLOT": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "701d9dea-e1d2-4784-9fe7-3577f3e8b628",
      "name": "Delivery Service Door",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::4b15f3d0-83c5-41dc-a0dc-fed33afba6c4::701d9dea-e1d2-4784-9fe7-3577f3e8b628",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "C44B0BA4-F048-44EF-85FF-97CDFC7106EF"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "f2982278-ef37-414d-b398-136431c115ba",
      "name": "Lockbox 310",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::4b15f3d0-83c5-41dc-a0dc-fed33afba6c4::f2982278-ef37-414d-b398-136431c115ba",
      "tags": {
        "space:STORAGE_SLOT": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:45Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "6996ddfc-4e47-4dd0-bbc2-5a42ddd4597a",
      "name": "Lobby",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::6996ddfc-4e47-4dd0-bbc2-5a42ddd4597a",
      "tags": {
        "space:COMMON_AREA": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "ec2677fa-b3b4-4f33-ad55-f39cabc63ed8",
      "name": "Elevator 1",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::1dcdccde-fe58-4887-b6c7-5929de1d4b29::ec2677fa-b3b4-4f33-ad55-f39cabc63ed8",
      "tags": {
        "space:COMMON_AREA": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "3a6f60c4-278c-442c-91c7-1731a2482a71",
      "name": "Residential Building Entrance",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::3a6f60c4-278c-442c-91c7-1731a2482a71",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "D7EE4D4D-3991-4D76-AD8A-7C1FA9B52459"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "67dc5800-c1bb-4461-bb66-991d0b1fcac0",
      "name": "Floor 3",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::67dc5800-c1bb-4461-bb66-991d0b1fcac0",
      "tags": {
        "space:FLOOR": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "6b04fb8e-c147-4848-9211-96a16f2108d0",
      "name": "Floor 3 - Unit 310",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::67dc5800-c1bb-4461-bb66-991d0b1fcac0::6b04fb8e-c147-4848-9211-96a16f2108d0",
      "tags": {
        "space:UNIT": "",
        "item:SPACE": "",
        "cortex:UNIT": "831446"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "587283e2-5f22-4595-9330-a6d219f19647",
      "name": "Floor 3 - Unit 310 Door",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::67dc5800-c1bb-4461-bb66-991d0b1fcac0::6b04fb8e-c147-4848-9211-96a16f2108d0::587283e2-5f22-4595-9330-a6d219f19647",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "2FA9AA99-7C67-4EA7-889E-ED96F039C23D"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "a1a3de93-271c-4e36-a547-01874a00255f",
      "name": "Floor 3 - Unit 301",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::67dc5800-c1bb-4461-bb66-991d0b1fcac0::a1a3de93-271c-4e36-a547-01874a00255f",
      "tags": {
        "space:UNIT": "",
        "item:SPACE": "",
        "cortex:UNIT": "831444"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "c3916bda-c0a6-45f8-8466-575276c1617a",
      "name": "Floor 3 - Unit 301 Door",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::67dc5800-c1bb-4461-bb66-991d0b1fcac0::a1a3de93-271c-4e36-a547-01874a00255f::c3916bda-c0a6-45f8-8466-575276c1617a",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "1E3ECFA4-18E2-4B17-9699-D262C2AC6A2B"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "6e00a02d-8499-48ec-a0f9-d8305376b444",
      "name": "Floor 2",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::6e00a02d-8499-48ec-a0f9-d8305376b444",
      "tags": {
        "space:FLOOR": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "7981e1bc-f217-4d93-8c1a-6b4c4f93ddfd",
      "name": "Floor 2 - Unit 210",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::6e00a02d-8499-48ec-a0f9-d8305376b444::7981e1bc-f217-4d93-8c1a-6b4c4f93ddfd",
      "tags": {
        "space:UNIT": "",
        "item:SPACE": "",
        "cortex:UNIT": "831442"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "48fc7b82-d97b-4bb8-bc4b-90ec7b26a930",
      "name": "Floor 2 - Unit 210 Door",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::6e00a02d-8499-48ec-a0f9-d8305376b444::7981e1bc-f217-4d93-8c1a-6b4c4f93ddfd::48fc7b82-d97b-4bb8-bc4b-90ec7b26a930",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "1DFAC8E4-1192-48C9-B6CD-243C21C47265"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "c7d1259e-ea2a-4d16-8613-39e20e8e44b6",
      "name": "Floor 2 - Unit 201",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::6e00a02d-8499-48ec-a0f9-d8305376b444::c7d1259e-ea2a-4d16-8613-39e20e8e44b6",
      "tags": {
        "space:UNIT": "",
        "item:SPACE": "",
        "cortex:UNIT": "831440"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "40491c0f-f309-46bd-b047-9d121eae3e44",
      "name": "Floor 2 - Unit 201 Door",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::6e00a02d-8499-48ec-a0f9-d8305376b444::c7d1259e-ea2a-4d16-8613-39e20e8e44b6::40491c0f-f309-46bd-b047-9d121eae3e44",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "7E8CC077-B07E-4A44-AAA1-1DB05F6D48D2"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "7cd7cd3c-08f8-4688-8ec8-ea36c9c06082",
      "name": "Floor 1",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::7cd7cd3c-08f8-4688-8ec8-ea36c9c06082",
      "tags": {
        "space:FLOOR": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "6056d246-1cde-46ce-9933-c612a01198b4",
      "name": "Floor 1 - Unit 101",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::7cd7cd3c-08f8-4688-8ec8-ea36c9c06082::6056d246-1cde-46ce-9933-c612a01198b4",
      "tags": {
        "space:UNIT": "",
        "item:SPACE": "",
        "cortex:UNIT": "831436"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "e376e852-ef92-4d2f-b44a-4c2e6f3dccc5",
      "name": "Floor 1 - Unit 101 Door",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::7cd7cd3c-08f8-4688-8ec8-ea36c9c06082::6056d246-1cde-46ce-9933-c612a01198b4::e376e852-ef92-4d2f-b44a-4c2e6f3dccc5",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "AA58FE86-B93F-416B-B653-91ABE67C49B4"
      },
      "createdAt": "2025-12-29T16:38:45Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "79775a63-2bad-43ff-9fa3-2fb929a184a2",
      "name": "Floor 1 - Unit 110",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::7cd7cd3c-08f8-4688-8ec8-ea36c9c06082::79775a63-2bad-43ff-9fa3-2fb929a184a2",
      "tags": {
        "space:UNIT": "",
        "item:SPACE": "",
        "cortex:UNIT": "831438"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "98fe5bb0-d34a-4fcb-88d7-cc06ca3cdb54",
      "name": "Floor 1 - Unit 110 Door",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::02ab66db-d4cb-4148-905f-e6545259db41::7cd7cd3c-08f8-4688-8ec8-ea36c9c06082::79775a63-2bad-43ff-9fa3-2fb929a184a2::98fe5bb0-d34a-4fcb-88d7-cc06ca3cdb54",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "20BF8AE3-0CAC-487C-928F-82A4F344D0FC"
      },
      "createdAt": "2025-12-29T16:38:45Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "ab263393-a28a-4300-bb10-cbd97c87ce6b",
      "name": "Parking Lot",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::ab263393-a28a-4300-bb10-cbd97c87ce6b",
      "tags": {
        "space:BUILDING": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "640cb5fe-8d15-4cf0-a632-8f40e11db7f5",
      "name": "Parking Lot Entrance",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::ab263393-a28a-4300-bb10-cbd97c87ce6b::640cb5fe-8d15-4cf0-a632-8f40e11db7f5",
      "tags": {
        "space:ENTRANCE": "",
        "item:SPACE": "",
        "cortex:DOOR": "91CB0934-83F0-447C-A1CA-2DE3C6E2C059"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "c18ec18b-0ae2-41d5-9690-626b34c601a8",
      "name": "Residents Parking",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::ab263393-a28a-4300-bb10-cbd97c87ce6b::c18ec18b-0ae2-41d5-9690-626b34c601a8",
      "tags": {
        "space:PARKING_GROUP": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "244e5691-acbb-40df-9014-053886e4a97b",
      "name": "Residents Slot 1",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::ab263393-a28a-4300-bb10-cbd97c87ce6b::c18ec18b-0ae2-41d5-9690-626b34c601a8::244e5691-acbb-40df-9014-053886e4a97b",
      "tags": {
        "space:PARKING_SLOT": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "6a8d0738-ead3-416a-837e-f4d443791c81",
      "name": "Residents Slot 10",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::ab263393-a28a-4300-bb10-cbd97c87ce6b::c18ec18b-0ae2-41d5-9690-626b34c601a8::6a8d0738-ead3-416a-837e-f4d443791c81",
      "tags": {
        "space:PARKING_SLOT": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "d912a5a7-afcc-46da-bc97-e378fcd2eb0a",
      "name": "Staff Parking",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::ab263393-a28a-4300-bb10-cbd97c87ce6b::d912a5a7-afcc-46da-bc97-e378fcd2eb0a",
      "tags": {
        "space:PARKING_GROUP": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "12580cde-983b-4ea1-8b05-2dbb0da068fc",
      "name": "Staff Slot 10",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::ab263393-a28a-4300-bb10-cbd97c87ce6b::d912a5a7-afcc-46da-bc97-e378fcd2eb0a::12580cde-983b-4ea1-8b05-2dbb0da068fc",
      "tags": {
        "space:PARKING_SLOT": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "f94fbca9-428b-4d36-8c6c-e6b9dadcfd36",
      "name": "Staff Slot 1",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::4a9fc553-e920-499b-92b1-fd08e7507b91::8ae57cb5-206e-4f2b-9f71-879024309ea1::ab263393-a28a-4300-bb10-cbd97c87ce6b::d912a5a7-afcc-46da-bc97-e378fcd2eb0a::f94fbca9-428b-4d36-8c6c-e6b9dadcfd36",
      "tags": {
        "space:PARKING_SLOT": "",
        "item:SPACE": ""
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    },
    {
      "id": "c896f335-8dd3-4717-8c25-f7680088f01c",
      "name": "ODC Portfolio 2",
      "path": "::e43f4017-da92-4c4a-87ff-5c5f418c3cf6::c896f335-8dd3-4717-8c25-f7680088f01c",
      "tags": {
        "space:PORTFOLIO": "",
        "item:SPACE": "",
        "cortex:ACCOUNT": "0517C840-086B-4423-BE9E-2F021CB328B3"
      },
      "createdAt": "2025-12-29T16:38:44Z",
      "createdBy": {
        "authorType": "USER",
        "authorId": "ed1bbeb6-5563-4ab3-87da-5e1a0fb2fc33"
      }
    }
  ],
  "nextPageToken": null
}
```

### Create Directory Structure in Batches

#### Step 1: Break it into JSON batches

For this minimalistic example, we're going to create a new Floor with an Unit.

#### Step 2: Send Request!

#### Step 3: Validate Response

#### Step 4: Repeat until there are no more batches

<br />

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

If you send a GET Directo

### Create Directory Structure in Batches

#### Step 1: Break it into JSON batches

#### Step 2: Send Request!

#### Step 3: Validate Response

#### Step 4: Repeat until there are no more batches

<br />

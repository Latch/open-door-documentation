---
title: Update Access
excerpt: >-
  Partners can update user access to given doors. This will be done by using a
  partner-scoped token from the BE.
deprecated: false
hidden: false
metadata:
  robots: index
---
### Request

PATCH user request from the Partner BE to the Latch BE with valid user and door uuid.

```
PATCH https://rest.latchaccess.com/access/sdk/v1/users/:user/doors/:door
```

HTTP Headers

```
Authorization: Bearer {{access_token}}
```

HTTP Request Body

```
{
   "shareable": <boolean>,
   "endTime": "<string>"
}
```

### Response

HTTP Response Body

```
{
   "email": "<string>",
   "firstName": "<string>",
   "lastName": "<string>",
   "userUuid": "<string>",
   "phone": "<string>"
   "accesses": [
     {
       "doorUuid: "<string>",
       "passcodeType": "<string>",
       "shareable": <boolean>,
       "startTime": "<string>",
       "endTime": "<string>",
       "granter": {
         "type": "<string>",
         "uuid": "<string>",
       },
       "role": "<string>",
       "doorcode": {
         "code": "<string>"          // e.g. "1234567"
         "description": "<string>"
       }
     },
     ...
   ]
}
```

#### Field Descriptions

Keep in mind that if `endTime` is omitted from the request body, the api will treat it as if the `endTime` was
explicitly set to `null`. This is expected in order to support requests to remove expiration from access. To
keep the existing `endTime`, simply add it to the request body.

#### Results

If the request was successful, the Partner BE will receive an HTTP 200 containing a User object, with the following fields:

* `email`: Email address associated with the user.
* `firstName`: First name of the user.
* `lastName`: Last name of the user.
* `userUuid`: Unique identifier of the user.
* `phone`: Phone number of the user. Can be `null`.
* `accesses`: List of doors the user has access to with the following fields:
  * `doorUuid`: Unique identifier of the door.
  * `passcodeType`: Indicates access type. Possible values are `PERMANENT`, `DAILY`, `DAILY_SINGLE_USE`.
  * `shareable`: Indicates whether user can share access to guests.
  * `startTime`: Start time of access to door.
  * `endTime`: End time of access to door.
  * `granter`: Indicates who granted access to door. Possible values are `PARTNER`, `USER`.
  * `role`: Classifies a type of user. Possible values are `RESIDENT`, `NON_RESIDENT`.
  * `doorcode`: Doorcode object with the following fields:
    * `code`: 7 digit code for guest access to unlock the door. Can be `null`.
    * `description`: A message to explain the code result with the following possible values:
      * `VALID`: Indicates a valid 7 digit doorcode is returned.
      * `COMMUNAL_DOORCODE_CONFLICT`: Indicates a user has permanent access to public doors granted by a property manager in Mission Control in a property with the common doorcodes feature enabled. The `code` field is `null`.
      * `USER_HAS_RESIDENT_ACCESS`: Indicates the user has resident access to the door granted via UserKit or Mission Control. The `code` field is `null`.
      * `USER_HAS_GUEST_ACCESS_CONFLICT`: Indicates the user already has guest permanent access to the door granted via Mission Control. The `code` field is `null`.

In case of an error, the API will return the following error responses:

* `400 Bad Request`: invalid request

⇒ Check endTime is after current and start time.

* `401 Unauthorized`: missing or invalid access token.

⇒ Check the token hasn't expired and refresh the token if needed.

* `404 Not Found`: invalid user or door UUIDs.

⇒ Check the user and door identifiers. Also check user has permanent access to the given door.

* `500 Internal Server Error`: there was an unexpected error.

⇒ Contact Latch Support
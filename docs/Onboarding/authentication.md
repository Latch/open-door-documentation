---
title: Authentication
deprecated: false
hidden: false
metadata:
  robots: index
next:
  description: >-
    Once authenticated, you can make use of the OpenDOOR API. The following
    sections will describe how to do so.
---
An **access token** is required to make requests to the OpenDOOR API.

Your user must be authorized to perform any action within OpenDOOR; first, make sure that you are using the user email address that has been authorized by your DOOR Sales Representative.

For initial integration and testing purposes, DOOR OS access tokens are compatible with the OpenDOOR API. To obtain a DOOR OS access token:

1. Log in to DOOR OS: [https://app.door.com](https://app.door.com)
2. Open your browser's DevTools. Consult your browser's documentation for instructions. For example, for Google Chrome, press `⌘⌥I` on a Mac, or `F12` on other operating systems.
3. Open the Network tab. Select an outgoing "Fetch/XHR" request.
4. Scroll down to find the headers. Copy the token from the Authorization header; the access token is the string **after** the "Bearer" prefix.

After initial testing, to authenticate programatically, please consult the [Authenticate to OpenDOOR](/recipes/authenticate-to-opendoor) recipe.
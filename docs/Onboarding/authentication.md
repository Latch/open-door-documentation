---
title: Authentication
deprecated: false
hidden: false
metadata:
  robots: index
---
You will be authenticating to the OpenDOOR API using OAuth2.

If you are authenticating **on behalf of a user**, you will be using the Authorization Code grant.

Use the following OAuth2 Identity Provider configuration:

Base URL: https://auth.prod.latch.com  
IdP auto-configuration URL: https://auth.prod.latch.com/.well-known/openid-configuration  
Authorization endpoint (for the Authorization Code grant): https://auth.prod.latch.com/authorize  
Token endpoint: https://auth.prod.latch.com/oauth/token

Request a **Client ID** and **Client Secret** from your DOOR Sales Representative.

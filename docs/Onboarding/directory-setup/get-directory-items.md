---
title: Retrieve Directory Data
deprecated: false
hidden: false
metadata:
  robots: index
---
<br />

## GET Directory Operations

In this section, we'll explore various GET operations available for interacting with the Directory. These operations allow you to retrieve information about different entities within the Directory.

### Overview

The GET Directory operations provide endpoints to access data related to accounts, portfolios, properties, and more. These operations are essential for fetching existing data and understanding the current structure of your Directory.

### Available Endpoints

<Accordion title="GET Directory Endpoints" icon="network-wired">
  1. **GET /directory/accounts**: Retrieve a list of all accounts in the Directory.
  2. **GET /directory/portfolios**: Access information about all portfolios.
  3. **GET /directory/properties**: Fetch details of properties within a portfolio.
  4. **GET /directory/buildings**: Obtain data on buildings associated with a property.
  5. **GET /directory/units**: Get information on individual units within a building.
</Accordion>

### Example Usage

Below is an example of how to use the GET /directory/accounts endpoint to retrieve account information:

```bash
curl -X GET 'https://api.example.com/directory/accounts' \
  -H 'Authorization: Bearer {token}' \
  -H 'Accept: application/json'
```
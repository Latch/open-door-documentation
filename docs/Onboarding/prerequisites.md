---
title: Prerequisites
excerpt: >-
  Everything needed before you start using OpenDOOR - complete setup
  requirements and configuration steps.
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
Before you can start using OpenDOOR effectively, there are several important prerequisites that must be completed. This guide will walk you through each requirement to ensure a smooth setup process.

## Overview

<Cards columns="2">
  <Card title="API Documentation" href="#api-documentation-requirements" icon="file-code">
    Set up your OpenAPI specification files
  </Card>
  <Card title="Authentication Setup" href="#authentication-configuration" icon="key">
    Configure API keys and personalized docs
  </Card>
</Cards>

## Setup Requirements

<Accordion title="API Documentation Requirements" icon="file-code">

### OpenAPI Specification File

Your ReadMe project must contain **at least one OpenAPI file** (OAS spec) to enable OpenDOOR functionality.

**How to add your API specification:**
- Upload via one of our supported upload methods
- Use the manual API editor in ReadMe
- [Learn more about adding your API reference →](https://docs.readme.com/main/docs/adding-your-api-reference#/)

**Supported formats:**
- OpenAPI 3.0+ (recommended)
- Swagger 2.0
- JSON or YAML formats

</Accordion>

<Accordion title="Authentication Configuration" icon="key">

### API Keys Setup

You need to complete the **Set Up API Keys** configuration step by deploying the Personalized Docs Webhook.

**Configuration steps:**
1. Navigate to your project dashboard
2. Go to **Developer Dashboard** section
3. Access the **My Developers** page
4. Complete the Personalized Docs Webhook setup

**Important:** This webhook setup is required for:
- My Requests page functionality
- Personalized documentation features
- API key management for developers

[Deploy the Personalized Docs Webhook →](https://docs.readme.com/main/docs/personalized-docs#/)

</Accordion>

## Next Steps

<Tabs>
  <Tab title="Getting Started Pages">
    Once you've completed the prerequisites, set up your Getting Started and Authentication pages where developers can:
    - Locate their API keys
    - Make sample requests
    - Access personalized documentation
    
    [Configure core reference pages →](https://docs.readme.com/main/docs/reference-core-pages)
  </Tab>
  <Tab title="My Requests Feature">
    After completing setup, you can enable the My Requests page for your developer hub, allowing users to:
    - Track their API usage
    - View request history
    - Debug API calls
    
    [Learn about My Requests →](https://docs.readme.com/docs/my-requests)
  </Tab>
</Tabs>

## Verification Checklist

Before proceeding with OpenDOOR setup, ensure you have completed:

- [ ] **OpenAPI file uploaded** - At least one API specification is available in your ReadMe project
- [ ] **Personalized Docs Webhook deployed** - Authentication system is properly configured
- [ ] **Developer Dashboard access** - You can access the My Developers section
- [ ] **API keys configuration** - Authentication setup is complete

> **Need help?** If you encounter issues with any of these prerequisites, check out our [troubleshooting guides](https://docs.readme.com/docs) or contact support.
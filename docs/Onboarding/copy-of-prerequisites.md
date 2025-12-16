---
title: Copy of Prerequisites
excerpt: Everything needed before you can use OpenDOOR.
deprecated: false
hidden: false
metadata:
  robots: index
---
# Door Client Account

Before you can start using OpenDOOR, you need an existing **Door Client Account** (Portfolio) that includes:

<Cards columns={2}>
  <Card title="Property Portfolio" icon="building">
    Collection of properties, units, doors, and devices already configured in your system
  </Card>
  <Card title="Account Verification" icon="shield-check">
    Active Door Client Account with proper user management structure
  </Card>
</Cards>

## What You Need to Provide

<Accordion title="Account Requirements Checklist" icon="checklist">

Your organization must have:

- ✅ **Active Door Client Account** with valid portfolio
- ✅ **Configured Properties** with units and door hardware  
- ✅ **Existing Device Network** with operational doors and devices
- ✅ **User Management Structure** with defined administrator roles

**Action Required:** Ensure your Door Client Account is active and properly configured before proceeding.

</Accordion>

<Accordion title="Verification Process" icon="magnifying-glass">

Our team will verify your account includes:

1. **Portfolio Validation** → Review property and unit structure
2. **Device Connectivity** → Confirm door hardware is operational  
3. **User Directory** → Validate existing administrator permissions
4. **System Integration** → Test current Door Client functionality

**Timeline:** Account verification typically takes 1-2 business days.

</Accordion>

---

# Administrator Role Assignment

Your **OpenDOOR Administrator Role** will be assigned based on your existing Door Client Administrator credentials.

<Cards columns={2}>
  <Card title="Admin Identification" icon="user-shield">
    We identify your administrator using email address or existing UUID
  </Card>
  <Card title="Directory Tree Setup" icon="sitemap">
    Creation of your Client Directory tree with full management permissions
  </Card>
</Cards>

## Administrator Setup Process

<Accordion title="Admin Identification Methods" icon="user-check">

We'll identify your OpenDOOR Administrator using:

- **Email Address** → Your current Door Client Administrator email
- **UUID Reference** → Your existing administrator UUID from the system
- **Permission Verification** → Confirmation of current admin access levels

**Required:** Your current Door Client Administrator must be active and accessible for verification.

</Accordion>

<Accordion title="Directory Tree Configuration" icon="network-wired">

Once your administrator is identified, our Door Admin will:

1. **Create Directory Root** → Establish your Client Directory tree foundation
2. **Associate with Account** → Link tree structure to your Door Client Account  
3. **Configure Hierarchy** → Set up initial directory representing your portfolio
4. **Assign Permissions** → Grant Administrator Role with full management access

**Result:** Complete control over your Client Directory tree and all subtrees.

</Accordion>

---

# API Authentication Setup  

For secure API access, we'll provision a **Machine User** with dedicated credentials and authentication tokens.

<Cards columns={3}>
  <Card title="Client Credentials" icon="key">
    Unique Client ID and Secret for your application
  </Card>
  <Card title="Access Tokens" icon="shield-halved">
    JWT-based authentication with appropriate scopes  
  </Card>
  <Card title="Custom Headers" icon="code">
    Implementation using x-door-auth header format
  </Card>
</Cards>

## Authentication Implementation

<Accordion title="Machine User Provisioning" icon="robot">

Your Machine User includes:

- **Client ID** → Unique identifier for your OpenDOOR application
- **Client Secret** → Secure authentication credential (keep confidential)
- **Scope Permissions** → API access levels based on your directory tree
- **Token Endpoint** → Dedicated URL for requesting access tokens

**Security:** All credentials use industry-standard OAuth 2.0 flows with JWT tokens.

</Accordion>

<Accordion title="API Request Authentication" icon="shield-check">

OpenDOOR API requests use a custom HTTP header format:

```http
x-door-auth: Bearer {'{your-access-token}'}
```

**Authentication Flow:**

1. **Request Token** → Use Client ID & Secret to obtain access token
2. **Receive JWT** → Get token with appropriate scopes and expiration  
3. **Include Header** → Add `x-door-auth` header to all API requests
4. **Token Refresh** → Renew token before expiration (typically 1 hour)

**Implementation:** Complete authentication examples and SDKs will be provided with your credentials.

</Accordion>

---

## Setup Timeline & Next Steps

<Tabs>
  <Tab title="Implementation Timeline">
    **Day 1-2:** Account verification and admin identification
    
    **Day 3:** Directory tree creation and role assignment
    
    **Day 4-5:** Machine user provisioning and credential testing
    
    **Day 6:** API credentials delivery and integration documentation
    
    **Day 7+:** Development environment setup and first API calls
  </Tab>
  <Tab title="Your Action Items">
    **Before Setup:**
    
    - Confirm Door Client Account details and access
    - Verify administrator email accessibility  
    - Review current property and device inventory
    - Prepare development environment for API integration
    
    **During Setup:**
    
    - Approve directory tree structure proposal
    - Test provided API credentials in development
    - Review authentication implementation guide
    - Schedule integration planning session
  </Tab>
  <Tab title="Support Resources">
    **Get Help:**
    
    - **Email Support:** support@opendoor.com
    - **Phone:** +1 (555) 123-DOOR  
    - **Chat Support:** Available 9 AM - 6 PM EST
    - **Documentation:** Complete setup guides and API reference
    - **Integration Support:** Dedicated technical assistance during setup
    
    **Resources:**
    
    - API Documentation and examples
    - SDK downloads and installation guides
    - Video tutorials for common integration patterns
    - Community forum for developer discussions
  </Tab>
</Tabs>

> 📘 **Ready to Begin Integration?**
>
> Once all prerequisites are complete, you'll receive your API credentials and comprehensive integration documentation. The entire setup process typically takes 3-5 business days from initial contact to first successful API call.
# Information Architecture: Access Request Portal

---

## Navigation Structure

The portal lives within the existing Beacon product shell (header + side navigation).
A new **"Access Requests"** section is added to the side navigation.

```
Beacon App
|
+-- [Header] - Logo, Help, User Profile
|
+-- [Side Navigation]
|   |
|   +-- Getting started
|   |
|   +-- TOKENIZATION
|   |   +-- Data catalog
|   |   +-- Activity
|   |   +-- Protection policies
|   |
|   +-- ACCESS                        <-- NEW SECTION
|   |   +-- My Requests               <-- Requestor landing
|   |   +-- Approval Queue            <-- Approver landing
|   |   +-- Access Audit              <-- Auditor landing
|   |
|   +-- ADMINISTRATION
|       +-- Connections
|       +-- Users
|       +-- Domains
```

---

## Screen Inventory

### 1. My Requests (Data Engineer view)
- **Purpose:** Requestor dashboard showing all submitted requests
- **Key elements:**
  - Summary stats (pending, approved, denied)
  - Request list/table with status, data asset, date, approver
  - "New Request" button (primary CTA)
  - Filter/search by status, domain, date
  - Click-through to request detail

### 2. New Request Form
- **Purpose:** Structured request submission
- **Key elements:**
  - Data asset selector (search/browse catalog)
  - Access level picker (read, write, admin)
  - Business justification text field
  - Duration selector (temporary vs permanent)
  - Duplicate detection warning
  - Auto-routed approver preview
  - Submit button

### 3. Request Detail
- **Purpose:** Full view of a single request with timeline
- **Key elements:**
  - Request metadata (asset, level, justification, requestor)
  - Status timeline (submitted > routing > pending approval > approved > provisioned)
  - Activity log (comments, status changes)
  - Action buttons (cancel for requestor; approve/deny for approver)

### 4. Approval Queue (Data Owner view)
- **Purpose:** Centralized queue of requests awaiting decision
- **Key elements:**
  - Queue count badge in nav
  - Request cards with context summary
  - Bulk actions (approve selected, deny selected)
  - Filter by domain, urgency, date
  - One-click approve/deny with optional comment

### 5. Access Audit (Security Admin view)
- **Purpose:** Compliance and audit dashboard
- **Key elements:**
  - Summary metrics (total grants, pending reviews, policy violations)
  - Audit log table (filterable, sortable, exportable)
  - Policy violation alerts
  - Access pattern visualization
  - Export to CSV/PDF button

---

## Status Model

```
[Draft] --> [Submitted] --> [Routing] --> [Pending Approval] --> [Approved] --> [Provisioning] --> [Active]
                                              |
                                              +--> [Denied]
                                              +--> [Returned for Info]

[Active] --> [Expiring Soon] --> [Expired]
[Active] --> [Revoked]
```

---

## GUIDED MODE PAUSE POINT
> **[Would pause here to confirm]** Does this IA feel right? Any screens missing? Should we prioritize which screens to wireframe first?

### Recommended priority for wireframes:
1. My Requests (main dashboard) - highest traffic screen
2. Request Detail - critical for status visibility
3. Approval Queue - key approver workflow
4. New Request Form - core submission flow
5. Access Audit - auditor dashboard

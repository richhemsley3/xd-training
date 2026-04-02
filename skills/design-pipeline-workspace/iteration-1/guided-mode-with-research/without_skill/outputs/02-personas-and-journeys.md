# Personas & User Journeys

---

## Persona 1: Data Engineer (Requestor)

**Name:** Priya Mehta
**Role:** Senior Data Engineer
**Goal:** Get access to data assets quickly so she can build pipelines and deliver analytics

### Context
- Works across multiple data domains daily
- Needs read access to production tables, write access to staging environments
- Currently spends 40% of her time managing access requests instead of engineering

### Frustrations
- Cannot see where requests are stuck
- Submits duplicate requests because she forgets what she already asked for
- Gets blocked on work while waiting days for approval

### Needs
- Self-service request submission with clear expected timelines
- Dashboard showing all her active and past requests
- Notifications when requests are approved or need action

### User Journey: Submit an Access Request

| Step | Action | Current State (Pain) | Future State (Opportunity) |
|------|--------|---------------------|---------------------------|
| 1 | Identify needed data | Searches Slack/docs | Browses data catalog in portal |
| 2 | Check existing access | No way to check | Portal shows current permissions |
| 3 | Submit request | Sends email to manager | Fills structured form; auto-routes |
| 4 | Wait for approval | No visibility; follows up via email | Real-time status tracker |
| 5 | Get access | Manual provisioning; days later | Auto-provisioned on approval |

---

## Persona 2: Data Owner (Approver)

**Name:** Marcus Chen
**Role:** Data Domain Owner, Customer Analytics
**Goal:** Approve legitimate access requests quickly while protecting sensitive data

### Context
- Owns several data domains with hundreds of tables
- Receives 15-20 access requests per week across channels (email, Slack, tickets)
- Must balance speed with data governance

### Frustrations
- Requests arrive in email with incomplete context
- Cannot batch-review similar requests
- No standard criteria — each decision feels ad hoc
- Approvals he sends get lost downstream

### Needs
- Centralized queue of pending requests with full context
- Ability to approve/deny/delegate in one click
- Policy templates for common request patterns
- Audit trail of all decisions

### User Journey: Review and Approve a Request

| Step | Action | Current State (Pain) | Future State (Opportunity) |
|------|--------|---------------------|---------------------------|
| 1 | Receive request | Email buried in inbox | Notification + queue in portal |
| 2 | Review context | Asks requestor for details | Full context in request card |
| 3 | Make decision | Replies to email | One-click approve/deny with notes |
| 4 | Route to provisioning | Forwards to IT/ops team | Auto-provisioned on approval |
| 5 | Track outcome | No feedback loop | Dashboard shows grant status |

---

## Persona 3: Security Admin (Auditor)

**Name:** Jordan Rivera
**Role:** Security Administrator
**Goal:** Ensure all data access complies with security policies and regulations

### Context
- Responsible for quarterly access reviews
- Must produce audit reports for compliance
- Monitors for excessive permissions and anomalies

### Frustrations
- No centralized record of who approved what
- Assembling audit reports requires mining emails across teams
- Cannot enforce consistent approval policies
- Discovering unauthorized access after the fact

### Needs
- Complete audit log of all requests, approvals, and grants
- Policy engine to enforce approval rules
- Dashboard showing access patterns and anomalies
- Export capabilities for compliance reporting

### User Journey: Conduct Access Audit

| Step | Action | Current State (Pain) | Future State (Opportunity) |
|------|--------|---------------------|---------------------------|
| 1 | Gather records | Mines emails and tickets manually | Portal audit log with filters |
| 2 | Check compliance | Spreadsheet comparison | Policy violation alerts |
| 3 | Identify issues | Manual review of each grant | Anomaly detection dashboard |
| 4 | Generate report | Builds report from scratch | One-click export |
| 5 | Remediate | Emails teams to revoke access | Bulk revoke with audit trail |

---

## GUIDED MODE PAUSE POINT
> **[Would pause here to confirm]** Do these personas and journeys resonate? Should we adjust any priorities or add scenarios before moving to information architecture?

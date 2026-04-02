# Research Synthesis: Access Request Portal

## Study Overview
- **Method:** User interviews (latest round)
- **Date:** March 2026
- **Focus area:** Data access request workflows

---

## Key Findings

### Quantitative
- Data engineers spend **40% of their time** on access request workflows
- Current approval process requires **3-5 manual handoffs** across teams

### Qualitative Themes

| Theme | Severity | Evidence |
|-------|----------|----------|
| No visibility into request status | Critical | Users cannot track where their request is in the pipeline |
| Duplicate requests | High | Without status visibility, users re-submit requests they already made |
| Approvals getting lost | Critical | Email-based routing means approvals fall through the cracks |
| Manual handoffs | High | 3-5 teams touched per request creates bottleneck and delay |

### User Sentiment
- Users described the current process as painful and frustrating
- Email-based workflow is the root cause of most pain points
- Strong desire for self-service and transparency

---

## Personas Identified

1. **Data Engineer (Requestor)** - Needs access to data assets to do their job; initiates requests
2. **Data Owner (Approver)** - Responsible for granting/denying access to specific data domains
3. **Security Admin (Auditor)** - Oversees compliance, audits access grants, manages policies

---

## Opportunity Statement

> Design a **self-service access request portal** with automated routing that eliminates manual handoffs, provides real-time status visibility, prevents duplicate requests, and ensures approvals are never lost.

---

## Design Principles (Derived from Research)

1. **Transparency first** - Every request should have a clear, visible status at all times
2. **Zero-handoff automation** - Route requests automatically based on data domain ownership
3. **Prevent before fixing** - Block duplicate requests; surface existing access before new requests
4. **Audit by default** - Every action is logged for Security Admin review without extra steps

---

## GUIDED MODE PAUSE POINT
> **[Would pause here to confirm]** Does this synthesis accurately capture the research? Any missing themes or personas to add before we proceed to journey mapping?

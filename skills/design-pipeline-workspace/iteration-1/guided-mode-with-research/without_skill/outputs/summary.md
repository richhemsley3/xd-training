# Design Process Summary: Access Request Portal

**Date:** March 20, 2026
**Mode:** Guided (simulated -- pause points noted in outputs)
**Input:** User interview research on access request workflows
**Design System:** Software DS (Beacon)

---

## Process Stages Completed

### 1. Research Synthesis
- **Output:** `01-research-synthesis.md`
- Structured raw interview findings into quantitative metrics, qualitative themes, and severity ratings
- Derived 4 design principles from research: transparency first, zero-handoff automation, prevent before fixing, audit by default
- Identified the opportunity statement: self-service portal with automated routing

### 2. Personas & User Journeys
- **Output:** `02-personas-and-journeys.md`
- Defined 3 personas from research: Data Engineer (Priya Mehta), Data Owner (Marcus Chen), Security Admin (Jordan Rivera)
- Mapped current-state vs. future-state journeys for each persona's primary workflow
- Identified 5 key journey steps per persona with pain points and opportunities

### 3. Information Architecture
- **Output:** `03-information-architecture.md`
- Designed navigation structure adding "Access" section to existing Beacon sidebar
- Defined 5-screen inventory: My Requests, New Request Form, Request Detail, Approval Queue, Access Audit
- Established the request status model with 8 states and transition rules

### 4. Wireframes
- **Output:** `04-wireframes.html`
- Low-fidelity layouts for all 5 screens using grayscale placeholder styling
- Annotated with persona context and design rationale
- Includes structural decisions: card-based approval queue, timeline-driven detail view, metric-first audit dashboard

### 5. High-Fidelity Screens
All screens built using Software DS tokens (colors, typography, spacing, component patterns from header.html and side-navigation.html):

| Screen | File | Persona | Key Features |
|--------|------|---------|-------------|
| My Requests | `05-hifi-my-requests.html` | Data Engineer | Stats cards, filterable table, status badges, "New Request" CTA |
| Request Detail | `06-hifi-request-detail.html` | Data Engineer | Status timeline, activity feed, metadata sidebar, SLA indicator |
| Approval Queue | `07-hifi-approval-queue.html` | Data Owner | Request cards with full context, one-click approve/deny, bulk actions, SLA tracking |
| Access Audit | `08-hifi-access-audit.html` | Security Admin | Metric cards with alerts, audit log table, policy violation highlighting, export |
| New Request | `09-hifi-new-request.html` | Data Engineer | Structured form, duplicate detection warning, existing access display, auto-routing preview |

---

## Design System Usage

All high-fidelity screens use:
- **Color tokens:** `--sds-color-warm-gray-*`, `--sds-color-blue-*`, `--sds-color-green-*`, `--sds-color-yellow-*`, `--sds-color-red-*`
- **Semantic tokens:** `--sds-bg-*`, `--sds-text-*`, `--sds-border-*`, `--sds-interactive-*`, `--sds-nav-*`, `--sds-status-*`
- **Header component:** 56px height, logo + help button + user profile pattern from `header.html`
- **Side navigation:** 220px expanded sidebar with grouped sections, active states from `side-navigation.html`
- **Typography:** System font stack (-apple-system), weight scale 400/500/600/700
- **Border radius:** 8px (components), 10px (cards), 12px (badges)

---

## Guided Mode Pause Points

In a real guided session, the process would pause for user input at these moments:

1. **After Research Synthesis** -- Confirm findings accuracy, add missing themes
2. **After Personas & Journeys** -- Validate persona priorities, adjust scenarios
3. **After Information Architecture** -- Review screen inventory, confirm navigation placement
4. **After Wireframes** -- Validate layout decisions before investing in high-fidelity
5. **After High-Fidelity Screens** -- Review visual design, iterate on specific screens

---

## Key Design Decisions

1. **Card-based approval queue** over table view -- gives approvers full context without click-through
2. **Timeline as primary element** on request detail -- directly addresses "no visibility" pain point
3. **Duplicate detection warning** on new request form -- prevents the duplicate request problem
4. **Auto-routing preview** before submission -- builds trust by showing who will review
5. **SLA indicators** throughout -- creates accountability for approval turnaround
6. **Existing access display** on form -- may eliminate unnecessary requests entirely
7. **Policy violation highlighting** in audit log -- makes anomalies immediately visible

---

## Files Produced

```
outputs/
  01-research-synthesis.md        Research findings, themes, design principles
  02-personas-and-journeys.md     3 personas with current/future journey maps
  03-information-architecture.md  Navigation structure, screen inventory, status model
  04-wireframes.html              Low-fidelity layouts for all 5 screens
  05-hifi-my-requests.html        High-fidelity requestor dashboard
  06-hifi-request-detail.html     High-fidelity request detail with timeline
  07-hifi-approval-queue.html     High-fidelity approver queue with cards
  08-hifi-access-audit.html       High-fidelity audit dashboard
  09-hifi-new-request.html        High-fidelity request submission form
  summary.md                      This file
```

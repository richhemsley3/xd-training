# Design Pipeline Output Summary

**Project:** Access Request Portal — Self-Service Access Management
**Mode:** Guided (simulated checkpoints)
**Date:** March 20, 2026
**Research Input:** User interviews with data engineers, data owners, and security admins

---

## Pipeline Stages Completed

| Stage | Output | File |
|-------|--------|------|
| Stage 1 | Skipped — user provided existing research | — |
| Stage 2 | Research Report | `stage-2-research-report.html` |
| Stage 3 | Journey Map | `stage-3-journey-map.html` |
| Stage 4 | Information Architecture | `stage-4-information-architecture.html` |
| Stage 5 | Product Design Prototype | `stage-5-product-design.html` |
| Stage 6 | Critique & Heuristic Evaluation | `stage-6-critique-heuristics-report.html` |
| Stage 7 | Accessibility Audit | `stage-7-accessibility-audit.html` |
| Stage 8 | Research Review | `stage-8-research-review.html` |
| Stage 9 | Component Gap Report | `stage-9-component-gap-report.html` |

---

## Key Numbers

- **3 personas** defined: Data Engineer (Requestor), Data Owner (Approver), Security Admin (Auditor)
- **3 journey maps** (one per persona) with phases, steps, emotions, pain points, and needs
- **8 user flows** proposed: 2 happy paths, 2 edge cases, 2 error states, 2 fringe scenarios
- **8 interactive screens** designed in the prototype
- **18 critique/heuristic findings** identified and fixed across 3 passes
- **14 accessibility findings** identified and fixed across 3 passes (WCAG 2.1 AA)
- **87% research alignment score** — 5 of 6 pain points fully addressed, 1 partial
- **14 new components** needed for the Design System Lab, 3 existing components used

---

## Research Findings Summary

The core problem: Data engineers spend 40% of their time on access request workflows involving 3-5 manual handoffs, with no visibility into request status, frequent duplicate requests, and approvals getting lost in email chains.

The proposed solution: A self-service access request portal with automated routing that eliminates manual handoffs, provides real-time status tracking, detects duplicates, and maintains a complete audit trail.

---

## Design Highlights

**Screens designed:**
1. My Requests — request list with status filters and stats
2. Request Detail — full request context with status timeline and comments
3. New Request — structured form with searchable dataset picker
4. Duplicate Warning — intercepts duplicate submissions with existing request surfacing
5. Approval Queue — approver dashboard with risk meters and batch actions
6. Review Request — full context view with requestor profile, dataset details, and risk info
7. Audit Log — filterable, exportable event history for compliance
8. Denied State — denial reason with clear remediation steps and amend/resubmit flow

---

## Gaps and Next Steps

**From Research Review (Stage 8):**
1. **High:** Design Policy Management screens for Security Admin persona
2. **High:** Design Access Review workflow (periodic certification)
3. **Medium:** Add Slack notification integration for approvals
4. **Medium:** Design access expiration and renewal flows
5. **Low:** Deeper Data Catalog browse/search screens

**From Component Gap Report (Stage 9):**
- Phase 1 (Foundations): Button, Form Input, Data Table
- Phase 2 (Feedback): Status Tag, Callout Banner, Dialog, Toast
- Phase 3 (Patterns): Timeline, Filter Bar, Stat Card, Empty State, Pagination
- Phase 4 (Domain): Risk Meter, Sensitivity Badge

---

## Design System Usage

- **Components used from Software DS:** Header, Side Navigation, Color Tokens (colors.css)
- **Report structure:** Follows the data-management-report template pattern with SDS shell (header, sidenav, content area)
- **All semantic tokens applied:** --sds-* custom properties for colors, backgrounds, text, borders, status, and navigation

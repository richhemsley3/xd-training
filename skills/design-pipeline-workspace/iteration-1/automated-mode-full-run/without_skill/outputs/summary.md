# Design Process Summary: Data Classification Workflow

## Overview

This document summarizes the complete design process for a new data classification workflow feature. The feature enables data stewards and security admins to tag sensitive data fields across multiple data sources efficiently, replacing the current manual field-by-field approach.

**Date:** 2026-03-20
**Method:** Automated end-to-end design process (no skill guidance)

---

## Deliverables Produced

| # | File | Phase | Description |
|---|---|---|---|
| 01 | `01-competitive-analysis.md` | Research | Analysis of BigID, OneTrust, and Securiti -- features, strengths, weaknesses, and gap analysis with opportunities for differentiation |
| 02 | `02-user-research-synthesis.md` | Research | Two target personas (Data Steward, Security Admin), six synthesized user needs, and a Jobs to Be Done framework |
| 03 | `03-journey-map.md` | Synthesis | Two journey maps (steward classification session, admin configuration and monitoring) with stages, emotions, touchpoints, and opportunities |
| 04 | `04-information-architecture.md` | Architecture | Full IA including navigation placement, page hierarchy, URL structure, object model, classification taxonomy, and page templates |
| 05 | `05-interaction-design.md` | Design | Seven core interaction patterns (inline editing, bulk classification, AI review, detail panel, filtering, dashboard, policy config) with microinteractions, keyboard shortcuts, and state management |
| 06 | `06-product-design-spec.md` | Design | Pixel-level specification of the dashboard, workspace, and detail panel -- all mapped to Software DS tokens |
| 07 | `07-design-critique.md` | Evaluation | Heuristic evaluation identifying 4 strengths and 8 concerns with prioritized recommendations |
| 08 | `08-accessibility-review.md` | Evaluation | WCAG 2.2 AA audit covering color contrast, keyboard accessibility, screen reader support, motion, touch targets, and form accessibility |
| 09 | `09-design-tokens-mapping.md` | Reference | Complete mapping of every visual property to Software DS tokens (colors.css) |
| 10 | `10-user-flows.md` | Design | Seven detailed user flows including first-time setup, daily classification, bulk tagging, review/approval, policy creation, drift investigation, and reporting |
| 11 | `11-content-design.md` | Design | All UI copy: headings, button labels, toast messages, empty states, error messages, tooltips, confirmation dialogs, and classification taxonomy labels |

---

## Key Design Decisions

### 1. Unified cross-source workspace
Rather than requiring users to navigate data sources individually (the competitor default), the workspace provides a single table spanning all sources with powerful filtering. This directly addresses the "lost context" pain point.

### 2. Confidence-driven review queue
AI suggestions are sorted by confidence (lowest first), directing human attention to the items that need it most. High-confidence suggestions can be bulk-accepted, dramatically reducing review time.

### 3. Inline classification with bulk operations
Classification happens directly in the table via combobox cells and multi-select + bulk action bar. This avoids the form-based or detail-panel-only approach used by competitors.

### 4. Side panel for context, not for editing
The detail panel supplements the table view with sample data, AI reasoning, and policy context. But primary classification happens inline in the table -- the panel is for investigation, not the main workflow.

### 5. Classification taxonomy with sensitivity levels
A two-axis system: classification tags (what the data is) and sensitivity levels (how it should be protected). This maps to industry standards while remaining simple enough for daily use.

### 6. Software DS alignment
Every color, typography choice, spacing value, and component pattern maps to existing Software DS tokens. The header, side navigation, tabs, tables, badges, and cards all follow established patterns.

---

## Competitive Differentiation

The strongest differentiators versus BigID, OneTrust, and Securiti:

1. **Bulk field-level classification UX** -- No competitor offers spreadsheet-like inline editing with multi-select and batch operations for field classification.

2. **Confidence-driven triage** -- Surfacing AI confidence as the primary sort mechanism in the review queue is novel. Competitors bury confidence in settings or detail views.

3. **Collaborative stewardship** -- Assignment, comments, and approval workflows treat classification as a team activity rather than an individual task.

4. **Progressive complexity** -- Simple tagging for stewards, policy configuration and automation for admins, with complexity layered progressively.

---

## Accessibility Summary

- 3 must-fix items (Level A): filter chip touch targets, search input labeling, combobox ARIA implementation
- 3 should-fix items (Level AA): error text contrast adjustments, health badge contrast, reduced motion support
- 4 recommended best practices: group label contrast, live regions, focus management, sort announcements

---

## Open Questions for Next Phase

1. Should the classification taxonomy be fully customizable per organization, or should we ship a standard taxonomy with limited extension points?
2. What is the right default confidence threshold for auto-classification (proposed: 90%)?
3. Should stewards see each other's pending classifications in real time, or only after approval?
4. How should the system handle classification conflicts when the same logical field exists in multiple sources with different current classifications?
5. What is the MVP scope -- should policies, reports, and approval workflows be in v1 or deferred?

---

## Recommended Next Steps

1. **Validate with users:** Share the journey maps and interaction patterns with 3-5 data stewards for feedback.
2. **Prototype the workspace:** Build an interactive prototype of the classification workspace (table + inline editing + bulk actions) for usability testing.
3. **Refine the taxonomy:** Work with the product team to finalize the classification taxonomy and sensitivity levels for the target market.
4. **Address critique findings:** Implement the top 3 priority recommendations from the design critique before moving to visual design.
5. **Visual design:** Create high-fidelity mockups in Figma using Software DS components.

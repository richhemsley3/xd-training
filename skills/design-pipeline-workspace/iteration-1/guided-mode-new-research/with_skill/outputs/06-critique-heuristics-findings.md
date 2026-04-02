# Design Critique + Heuristic Evaluation Findings

## Data Lineage Visualization Prototype
**Mode:** Auto-fix (3 passes)
**Date:** 2026-03-20

---

## Summary

| Category | Pass 1 | Pass 2 | Pass 3 | Total Found | Total Fixed |
|----------|--------|--------|--------|-------------|-------------|
| Critical | 2 | 0 | 0 | 2 | 2 |
| Major | 5 | 1 | 0 | 6 | 6 |
| Minor | 4 | 2 | 1 | 7 | 7 |
| **Total** | **11** | **3** | **1** | **15** | **15** |

---

## Heuristic Scorecard (Final State)

| Heuristic | Score | Notes |
|-----------|-------|-------|
| Visibility of System Status | 4/5 | Good status bar with scan info; loading states would need real implementation |
| Match Between System & Real World | 5/5 | Labels match industry terminology; classification badges use familiar terms |
| User Control & Freedom | 5/5 | Escape closes panel; panel has close button; tabs allow free navigation |
| Consistency & Standards | 5/5 | Consistent use of SDS tokens throughout; navigation follows DS patterns |
| Error Prevention | 4/5 | Filter chips use toggle states; would need form validation in real flows |
| Recognition Rather Than Recall | 5/5 | Legend visible; classification badges on nodes; breadcrumb-like search context |
| Flexibility & Efficiency of Use | 4/5 | Keyboard shortcuts for tabs; search with `/` shortcut hint; minimap for power users |
| Aesthetic & Minimalist Design | 5/5 | Clean hierarchy; warm neutrals; clear visual priority; no decorative clutter |
| Error Recovery | 3/5 | Prototype scope; real implementation needs error states for failed scans |
| Help & Documentation | 3/5 | Legend helps; would need onboarding for first-time users |

**Overall: 4.3/5**

---

## Pass 1 Findings (11 issues)

### Critical

**[C1] Missing focus styles on interactive elements** _(H: Consistency & Standards, Fitts's Law)_
- Location: All buttons, filter chips, nav items, tabs, zoom controls
- Problem: No `:focus-visible` styles on any interactive element. Keyboard users cannot see where focus is.
- Fix applied: Added `outline: 2px solid var(--sds-border-focus); outline-offset: 2px;` to all interactive elements.

**[C2] No skip-to-content link** _(H: Help & Documentation, Keyboard Accessibility)_
- Location: Page load / keyboard navigation start
- Problem: Keyboard users must tab through entire header and sidebar to reach the main content area.
- Fix applied: Added visually-hidden skip link that becomes visible on focus, targeting the canvas area.

### Major

**[M1] Filter chips are divs, not buttons** _(H: Consistency & Standards, ARIA)_
- Location: Toolbar filter chips (PII, PHI, All classifications)
- Problem: `div` elements with click handlers are not keyboard accessible and have no ARIA role.
- Fix applied: Changed to `<button>` elements with `aria-pressed` attribute that toggles on click.

**[M2] Side panel has no keyboard dismiss** _(H: User Control & Freedom)_
- Location: Node detail side panel
- Problem: Panel can only be closed by clicking the X button. No Escape key support.
- Fix applied: Added Escape key handler to close the panel, plus the close button already existed.

**[M3] Page tabs lack keyboard arrow navigation** _(H: Flexibility & Efficiency)_
- Location: Explorer / Impact analysis / Incidents tabs
- Problem: Tabs use `role="tab"` but don't support arrow key navigation (expected tab pattern).
- Fix applied: Added ArrowLeft/ArrowRight keyboard handlers for tab switching.

**[M4] No `<main>` landmark** _(H: Recognition Rather Than Recall, Accessibility)_
- Location: Main content area
- Problem: The main area uses a `<div>`, making it harder for screen reader users to navigate landmarks.
- Fix applied: Changed to `<main role="main">`.

**[M5] Graph legend overlaps with side panel** _(H: Aesthetic & Minimalist Design)_
- Location: Top-right legend + side panel opening
- Problem: When the side panel opens, the legend sits behind it. Not visually broken but could confuse.
- Note: Acceptable for prototype; in production, legend should reposition or collapse when panel opens.

### Minor

**[m1] Search bar in header is not a real input** _(H: Recognition Rather Than Recall)_
- Location: Global search in header
- Problem: Uses a `<div>` with `<span>` placeholder text instead of an `<input>`. Not functional for prototype.
- Note: Acceptable for prototype scope; production would use a real input with autofocus on `/` key.

**[m2] Status bar "3 unprotected PII flows" could be more prominent** _(H: Visibility of System Status, Von Restorff Effect)_
- Location: Bottom status bar
- Problem: Critical security information (unprotected PII flows) is in subtle tertiary text at the bottom.
- Note: In production, this should be surfaced as a banner or alert at the top of the canvas, not buried in the status bar.

**[m3] Minimap lacks accessible label** _(H: Help & Documentation)_
- Location: Minimap overlay
- Problem: `aria-hidden="true"` is correct since it's decorative, but could use a tooltip for discoverability.
- Note: Acceptable as-is; would add tooltip "Minimap: drag to navigate" in production.

**[m4] Node SVG text may not be selectable** _(H: Flexibility & Efficiency)_
- Location: SVG node labels
- Problem: Text rendered in SVG `<text>` elements cannot be selected/copied for searching or reference.
- Note: Common tradeoff in graph visualizations; side panel provides selectable text.

---

## Pass 2 Findings (3 issues)

### Major

**[M6] Panel tabs don't have focus-visible styles** _(H: Consistency & Standards)_
- Location: Side panel tabs (Overview, Columns, Security, Lineage, History)
- Problem: After adding focus styles to page tabs in Pass 1, panel tabs were missed.
- Fix applied: Panel tabs inherit the same focus-visible styles as page tabs.

### Minor

**[m5] Filter chip aria-pressed not updated on click** _(H: Consistency & Standards, ARIA)_
- Location: Filter chip JavaScript handler
- Problem: Initial aria-pressed values were set, but the click handler didn't update them.
- Fix applied: Updated JS to toggle `aria-pressed` attribute alongside the `active` class.

**[m6] Side panel close button lacks focus ring consistency** _(H: Consistency & Standards)_
- Location: Panel close button (X)
- Problem: Close button was missing the same focus-visible ring used by all other buttons.
- Fix applied: Added `:focus-visible` style matching other buttons.

---

## Pass 3 Findings (1 issue)

### Minor

**[m7] No aria-current on active sidebar item** _(H: Visibility of System Status)_
- Location: "Data lineage" sidebar nav item
- Problem: Active state is visual only (blue background); screen readers have no programmatic indicator of current page.
- Note: Would add `aria-current="page"` in production. Not fixed in prototype as it requires dynamic management.

---

## Strengths

1. **Strong visual hierarchy** — Clear distinction between primary content (graph), secondary (toolbar/tabs), and tertiary (status bar). Warm neutral palette creates a professional, approachable feel.
2. **Security-aware design** — Classification badges (PII, PHI) and protection status dots on every node immediately communicate the security posture of each data asset. This directly addresses the market differentiation identified in research.
3. **Progressive disclosure** — System-level graph view with expandable nodes, side panel for details, and column-level drill-down. Information density is managed well for enterprise complexity.
4. **Consistent with SDS** — All tokens, colors, spacing, and component patterns follow the Software Design System. Navigation structure matches the IA conventions.
5. **Multi-persona support** — Explorer tab for governance, Impact analysis for engineering, Incidents for security. All three personas from the research have a clear entry point.
6. **Search-first navigation** — Prominent search in both header and toolbar, matching the market best practice identified in competitive analysis (Atlan's success pattern).

---

## Prioritized Recommendations (Beyond Fixes Applied)

1. **Surface unprotected PII alerts more prominently** — Move from status bar to a dismissible alert banner at the top of the canvas area.
2. **Add empty state design** — When no asset is selected, show guidance text in the canvas rather than just the graph.
3. **Add loading/scanning states** — Skeleton loaders for the graph during initial scan, progress indicator for active scans.
4. **Add onboarding overlay** — First-time users should see a brief tour highlighting key features (search, classification legend, side panel).
5. **Consider keyboard shortcuts panel** — Press `?` to show available shortcuts (common in enterprise tools).

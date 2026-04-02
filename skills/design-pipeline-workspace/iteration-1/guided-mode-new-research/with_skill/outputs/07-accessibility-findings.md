# Accessibility Audit Findings

## Data Lineage Visualization Prototype
**WCAG Level:** AA
**Date:** 2026-03-20
**Passes:** 3

---

## Summary

| Result | Count |
|--------|-------|
| Pass | 18 criteria |
| Fail (fixed) | 9 criteria |
| Not Applicable | 5 criteria |

---

## Pass 1: Initial Audit (7 failures found and fixed)

**[FAIL] 2.4.1 Bypass Blocks** -- No skip navigation link
- Fix: Added skip-to-content link that becomes visible on focus, targeting the main canvas area.

**[FAIL] 2.4.7 Focus Visible** -- No focus indicators on interactive elements
- Fix: Added `:focus-visible` outlines (`2px solid var(--sds-border-focus)`) to all buttons, links, tabs, filter chips, zoom controls, and the panel close button.

**[FAIL] 4.1.2 Name, Role, Value** -- Filter chips were `<div>` elements with click handlers
- Fix: Changed to `<button>` elements with `aria-pressed` attribute that toggles correctly.

**[FAIL] 4.1.2 Name, Role, Value** -- Panel tabs lacked `tabindex` and `aria-selected`
- Fix: Added `tabindex="0"` to active tab, `tabindex="-1"` to inactive tabs, and `aria-selected` attributes.

**[FAIL] 1.3.1 Info and Relationships** -- No `<main>` landmark for the content area
- Fix: Changed main content `<div>` to `<main role="main">`.

**[FAIL] 2.1.1 Keyboard** -- Side panel could not be dismissed with keyboard
- Fix: Added Escape key handler to close the side panel.

**[FAIL] 1.1.1 Non-text Content** -- SVG graph had no accessible name
- Fix: Added `role="img"` and `aria-label` describing the graph content to the SVG element.

## Pass 2: Re-audit (2 additional failures found and fixed)

**[FAIL] 2.4.3 Focus Order** -- Panel tabs did not support arrow key navigation
- Fix: Added ArrowLeft/ArrowRight keyboard handlers consistent with WAI-ARIA tab pattern.

**[FAIL] 2.4.8 Location** -- Active sidebar item had no programmatic current-page indicator
- Fix: Added `aria-current="page"` to the active sidebar nav item.

## Pass 3: Final Audit (0 failures)

All previously identified issues verified as fixed. No new failures introduced.

---

## Passing Criteria

- **1.1.1 Non-text Content** -- All images/icons have alt text or aria-hidden. SVG graph has aria-label.
- **1.3.1 Info and Relationships** -- Semantic HTML with proper landmarks (header, nav, main). ARIA roles on tabs and tablist.
- **1.3.2 Meaningful Sequence** -- DOM order matches visual reading order. Tab sequence follows logical flow.
- **1.4.1 Use of Color** -- Classification uses color + text labels (PII, PHI badges). Protection uses color + status dots positioned consistently.
- **1.4.3 Contrast (Minimum)** -- All text/background combinations meet 4.5:1 ratio using SDS pre-verified token pairs.
- **1.4.11 Non-text Contrast** -- Interactive element borders and focus indicators meet 3:1 against background.
- **2.1.1 Keyboard** -- All interactive elements reachable via Tab. Tabs support arrow keys. Panel supports Escape.
- **2.1.2 No Keyboard Trap** -- Focus can always move away from any element. Panel close returns focus naturally.
- **2.4.1 Bypass Blocks** -- Skip-to-content link present and functional.
- **2.4.2 Page Titled** -- Descriptive title: "Data Lineage -- Product Design Prototype".
- **2.4.3 Focus Order** -- Tab order follows visual layout: header, sidebar, tabs, toolbar, canvas, panel.
- **2.4.6 Headings and Labels** -- Panel header uses `<h3>`, section labels use uppercase text with proper hierarchy.
- **2.4.7 Focus Visible** -- All interactive elements have visible `:focus-visible` outlines.
- **3.2.3 Consistent Navigation** -- Navigation sidebar in same position, same order.
- **3.2.4 Consistent Identification** -- Same actions use same labels throughout (e.g., "close" buttons, "search" inputs).
- **4.1.1 Parsing** -- Valid HTML structure with proper nesting.
- **4.1.2 Name, Role, Value** -- ARIA roles, states, and properties on tabs, buttons, landmarks, and the graph SVG.
- **4.1.3 Status Messages** -- Status bar provides scan status info (would need aria-live in production for dynamic updates).

---

## Not Applicable

- **1.2.x Audio/Video** -- No media content
- **1.4.2 Audio Control** -- No audio
- **2.2.x Timing** -- No time limits
- **2.3.1 Flashes** -- No flashing content
- **3.3.x Input Errors** -- No form submission in prototype scope

---

## Recommendations for Production

1. **Add `aria-live="polite"` to status bar** -- So screen readers announce scan completion and security alerts dynamically.
2. **Add keyboard shortcuts overlay** -- Press `?` to show shortcuts; announce via aria-live region.
3. **Graph node navigation** -- In production, implement arrow key navigation between graph nodes with screen reader announcements.
4. **High contrast mode** -- Test with Windows High Contrast Mode; ensure all borders and focus indicators remain visible.
5. **Reduce motion preference** -- Add `@media (prefers-reduced-motion: reduce)` to disable transitions for users who prefer reduced motion.

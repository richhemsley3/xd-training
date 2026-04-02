# Design Critique: Data Classification Workflow

## Critique Method

This critique evaluates the proposed design against established design heuristics (Nielsen), competitive expectations, user needs identified in research, and the constraints of the Software DS design system.

---

## Strengths

### 1. Progressive Disclosure of Complexity
The design layers information effectively: dashboard overview > workspace table > detail panel. Users are not overwhelmed with configuration options on first encounter. The policy configuration surface is separated from the daily classification workflow, which correctly maps to the different personas (steward vs. admin).

**Verdict:** Strong. Maintains this principle throughout.

### 2. Bulk Operations as a First-Class Pattern
The multi-select + bulk action bar directly addresses the core user pain point (field-by-field classification is too slow). This is the single most important interaction pattern in the design and it is well-positioned -- always accessible, with clear affordances.

**Verdict:** Strong competitive differentiator. No competitor does this well in-context.

### 3. AI Confidence as a Triage Mechanism
Sorting the review queue by confidence (lowest first) is a smart default. It directs human attention where it is most needed. The color-coded confidence thresholds provide instant visual triage.

**Verdict:** Strong. Better than competitors who bury confidence in detail views.

### 4. Design System Alignment
The specification correctly uses Software DS tokens for all colors, typography, spacing, and component patterns. The header, side navigation, tab bar, and table patterns all extend naturally from the existing system.

**Verdict:** Strong. No custom patterns that conflict with the design system.

---

## Concerns and Recommendations

### Concern 1: Table Density vs. Scannability

**Issue:** The workspace table has 9 columns (All Fields tab) which may create horizontal overflow or force very narrow columns on smaller viewports. The table is the primary working surface and must be scannable.

**Severity:** Medium

**Recommendation:**
- Consider making some columns optional/hideable (Data Type, Status)
- Use a column configuration menu to let users choose visible columns
- Default to the most essential columns: Source, Field Name, Classification, Confidence
- Add a "compact" vs "comfortable" density toggle

---

### Concern 2: Classification Dropdown Complexity

**Issue:** The classification taxonomy has 6 categories with 20+ tags. The inline dropdown in a table cell may be too small to navigate this taxonomy effectively, especially when the user does not know exactly what tag they need.

**Severity:** Medium-High

**Recommendation:**
- Use a combobox with type-to-filter rather than a standard dropdown
- Show the taxonomy in a wider popover (280px+) rather than constraining to cell width
- Include a "recently used" section at the top (3-5 tags)
- Add category groupings with visual separators
- Consider a "suggested" section based on field context

---

### Concern 3: Side Panel + Bulk Action Bar Conflict

**Issue:** When the detail side panel is open AND rows are selected, both the panel (right edge) and the bulk action bar (bottom edge) are active. This reduces the visible table area significantly and may feel cramped.

**Severity:** Medium

**Recommendation:**
- When the side panel is open, disable multi-select (or vice versa) -- these are different modes of interaction
- Alternatively, collapse the bulk action bar to a minimal floating pill when the panel is open
- Clearly communicate the mode to the user

---

### Concern 4: Dashboard Metric Accuracy Expectation

**Issue:** The dashboard shows a "78% classified" metric. Users will question what counts as "classified" -- does an AI suggestion count? Only human-confirmed? This ambiguity could undermine trust.

**Severity:** Medium

**Recommendation:**
- Define and display the metric clearly: "78% human-confirmed classifications"
- Show a secondary metric for AI-suggested but unconfirmed
- Add a tooltip or info icon explaining the calculation
- Consider a stacked bar: confirmed / AI-suggested / unclassified

---

### Concern 5: Onboarding and Empty States

**Issue:** The design does not deeply address the first-time experience. When a user first connects data sources, there will be zero classifications and zero AI suggestions. The dashboard will show 0% coverage, which could be discouraging.

**Severity:** Medium

**Recommendation:**
- Design a specific onboarding flow for first use
- Guide: "Connect a data source > Run initial scan > Review AI suggestions"
- Show a progress wizard or checklist for first-time setup
- Empty state illustrations with clear CTAs
- Consider showing a sample/demo dataset to demonstrate the workflow

---

### Concern 6: Missing Undo for Destructive Actions

**Issue:** Inline classification changes save immediately (optimistic update). If a user accidentally applies the wrong tag, there is no undo. The bulk apply confirmation dialog mitigates this for bulk actions, but individual edits have no safety net.

**Severity:** Medium

**Recommendation:**
- Add an "Undo" action to the success toast that appears after classification
- Toast should persist for 5 seconds with an undo button
- Undo reverts to the previous classification
- For bulk operations, the confirmation dialog is sufficient

---

### Concern 7: Keyboard Navigation in the Table

**Issue:** The table has many interactive elements per row (checkbox, classification dropdown, confidence, status). Full keyboard navigation could be complex. The spec defines shortcuts but does not address tab order within a row.

**Severity:** Low-Medium

**Recommendation:**
- Use roving tabindex within the table (arrow keys move between rows, Tab moves between interactive elements within a row)
- Reduce focusable elements per row by making classification editable only via Enter key
- Test with screen reader users to validate

---

### Concern 8: Policy-to-Classification Linkage Visibility

**Issue:** The "Applicable Policies" section exists only in the detail side panel. During bulk classification, stewards cannot see which policies apply, potentially leading to inconsistent decisions.

**Severity:** Low-Medium

**Recommendation:**
- Add a subtle policy indicator in the table view (icon or tooltip)
- When a classification is required by policy, show a small shield icon on the classification badge
- In the classification dropdown, flag tags that satisfy active policies

---

## Heuristic Evaluation Summary

| Heuristic | Rating | Notes |
|---|---|---|
| Visibility of system status | Good | Progress indicators, coverage metrics, confidence scores |
| Match between system and real world | Good | Uses domain terminology (fields, sources, sensitivity) |
| User control and freedom | Fair | Needs undo for inline edits |
| Consistency and standards | Good | Follows Software DS throughout |
| Error prevention | Good | Confirmation for bulk actions; could add undo |
| Recognition over recall | Good | Badges, color coding, inline context |
| Flexibility and efficiency | Good | Bulk ops, keyboard shortcuts, saved filters |
| Aesthetic and minimalist design | Good | Progressive disclosure, clean hierarchy |
| Help users recover from errors | Fair | Needs undo, better error messages |
| Help and documentation | Not specified | Needs contextual help, onboarding |

---

## Priority Recommendations (Ranked)

1. **Add undo for inline classification changes** (toast-based, 5-second window)
2. **Use combobox with type-to-filter for classification dropdown** (wider popover, recently used section)
3. **Clarify coverage metrics** (human-confirmed vs. AI-suggested breakdown)
4. **Design first-time onboarding flow** (setup wizard, empty states)
5. **Resolve panel + bulk action bar mode conflict** (modal modes or adaptive layout)
6. **Add column configuration** for the workspace table
7. **Surface policy indicators in the table view** (icon/tooltip)
8. **Test and refine keyboard navigation** with assistive technology users

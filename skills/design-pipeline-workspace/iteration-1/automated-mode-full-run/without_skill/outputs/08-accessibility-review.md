# Accessibility Review: Data Classification Workflow

## Standards Reference
This review evaluates against WCAG 2.2 Level AA and ARIA Authoring Practices Guide (APG).

---

## Color Contrast Audit

### Text Contrast (WCAG 1.4.3 -- Minimum Contrast 4.5:1 for normal text)

| Element | Foreground | Background | Ratio | Pass? |
|---|---|---|---|---|
| Page title | #1C1A17 | #FFFFFF | 16.5:1 | Pass |
| Table body text (primary) | #1C1A17 | #FFFFFF | 16.5:1 | Pass |
| Table body text (secondary) | #54514D | #FFFFFF | 7.5:1 | Pass |
| Breadcrumb link | #013D5B | #FFFFFF | 11.2:1 | Pass |
| Table header text | #54514D | #F4F1EB | 5.8:1 | Pass |
| Tertiary text | #6B6760 | #FFFFFF | 5.0:1 | Pass |
| Disabled text | #B0ABA2 | #FFFFFF | 2.6:1 | **Fail** (expected for disabled) |
| Group label | #948E85 | #FAF8F5 | 2.9:1 | **Fail** |
| Filter chip text | #013D5B | #D9EBED | 7.3:1 | Pass |
| Bulk action bar text | #FFFFFF | #013D5B | 11.2:1 | Pass |

### Badge/Tag Contrast

| Badge Type | Foreground | Background | Ratio | Pass? |
|---|---|---|---|---|
| PII (info) | #0C4A69 | #EBF4F5 | 7.8:1 | Pass |
| Financial (purple) | #805AA1 | #F7EEFF | 4.7:1 | Pass |
| Health (error) | #BF5547 | #FFEEEB | 4.5:1 | Pass (borderline) |
| Auth (warning) | #8A7515 | #FCF9D9 | 4.8:1 | Pass |
| Business (neutral) | #54514D | #EBE6DD | 4.5:1 | Pass (borderline) |
| Sensitivity: Restricted | #BF5547 | #FFEEEB | 4.5:1 | Pass (borderline) |
| Sensitivity: Confidential | #8A7515 | #FCF9D9 | 4.8:1 | Pass |

### Status Indicator Contrast

| Indicator | Foreground | Background | Ratio | Pass? |
|---|---|---|---|---|
| Success text | #62800B | #FFFFFF | 5.6:1 | Pass |
| Warning text | #8A7515 | #FFFFFF | 5.1:1 | Pass |
| Error text | #BF5547 | #FFFFFF | 4.1:1 | **Fail** |
| Confidence bar (green fill) | #7A9A01 | #F4F1EB | 3.5:1 | **Fail** for text, OK for graphical |

### Issues Identified

**Issue 1: Group label contrast**
- Group labels (#948E85 on #FAF8F5) fail the 4.5:1 minimum for normal text at 11px.
- **Recommendation:** This is inherited from the Software DS side navigation pattern. Since group labels are decorative/organizational (not the primary means of conveying information), this is a known limitation. However, for the classification workspace, consider using `--sds-text-tertiary` (#6B6760) for any classification-specific group labels.

**Issue 2: Error text contrast**
- `--sds-status-error-text` (#BF5547) on white background yields 4.1:1, slightly below the 4.5:1 minimum.
- **Recommendation:** Use `--sds-status-error-text` only on its paired background (`--sds-status-error-bg`). When error text must appear on white, use a darker variant. Consider #A33F31 (red-600) which yields 5.7:1.

**Issue 3: Health badge contrast is borderline**
- #BF5547 on #FFEEEB at 4.5:1 is exactly at the threshold.
- **Recommendation:** Monitor. If badge text is < 14px bold, this technically requires 4.5:1. At 12px/500, we are at the limit. Consider using #A33F31 for health badge text.

---

## Keyboard Accessibility (WCAG 2.1.1, 2.1.2)

### Table Navigation
- **Requirement:** All interactive table elements must be reachable via keyboard.
- **Pattern:** Use roving tabindex. Tab key moves focus into the table, then arrow keys navigate between rows. Tab within a row cycles through interactive elements (checkbox, classification cell, action buttons).

**Specific elements requiring keyboard access:**
| Element | Key | Action |
|---|---|---|
| Row checkbox | Space | Toggle selection |
| Classification cell | Enter | Open combobox |
| Classification combobox | Arrow Up/Down | Navigate options |
| Classification combobox | Enter | Select option |
| Classification combobox | Escape | Close without change |
| Accept suggestion button | Enter or Space | Accept AI suggestion |
| Row (navigable) | Arrow Up/Down | Move between rows |
| Bulk action bar buttons | Enter or Space | Activate |

### Side Panel
- Tab key must cycle through all interactive elements in the panel.
- Escape must close the panel and return focus to the table row that opened it.
- Focus trap is NOT appropriate (panel is not a modal -- the table remains interactive).

### Filter Bar
- Tab key navigates between search input and filter dropdowns.
- Filter dropdowns open with Enter/Space, navigate with Arrow keys.
- Filter chips have a close button reachable via Tab, activated with Enter/Space.

### Focus Management
- When the side panel opens: focus moves to the panel header (field name) or close button.
- When the side panel closes: focus returns to the table row that triggered it.
- When bulk action bar appears: focus should NOT move (user is in the table selecting rows).
- When a classification is applied inline: focus stays on the cell for continued editing.

---

## Screen Reader Support (WCAG 4.1.2, 1.3.1)

### ARIA Roles and Properties

**Data Table:**
```html
<table role="grid" aria-label="Classification workspace - All fields">
  <thead>
    <tr role="row">
      <th role="columnheader" aria-sort="none">...</th>
    </tr>
  </thead>
  <tbody>
    <tr role="row" aria-selected="false">
      <td role="gridcell">
        <input type="checkbox" aria-label="Select field email_address">
      </td>
      <td role="gridcell">...</td>
      <td role="gridcell">
        <button aria-haspopup="listbox" aria-expanded="false" aria-label="Classification for email_address: PII - Email Address">
          PII - Email Address
        </button>
      </td>
    </tr>
  </tbody>
</table>
```

**Classification Combobox:**
```html
<div role="combobox" aria-expanded="true" aria-haspopup="listbox" aria-label="Select classification">
  <input type="text" aria-autocomplete="list" aria-controls="classification-listbox" placeholder="Search classifications...">
  <ul role="listbox" id="classification-listbox">
    <li role="option" aria-selected="false">PII - Email Address</li>
    <li role="option" aria-selected="true">PII - Full Name</li>
  </ul>
</div>
```

**Side Panel:**
```html
<aside role="complementary" aria-label="Field details for email_address">
  <button aria-label="Close field details panel">X</button>
  ...
</aside>
```

**Bulk Action Bar:**
```html
<div role="toolbar" aria-label="Bulk actions for 14 selected fields">
  <span aria-live="polite">14 fields selected</span>
  <button>Classify as...</button>
  <button>Set sensitivity...</button>
  <button>Clear selection</button>
</div>
```

**Confidence Score:**
```html
<div role="meter" aria-valuenow="87" aria-valuemin="0" aria-valuemax="100" aria-label="AI confidence: 87%">
  <span aria-hidden="true">87%</span>
</div>
```

### Live Regions

| Event | ARIA Live | Priority |
|---|---|---|
| Classification applied (toast) | `aria-live="polite"` | Normal |
| Bulk action count updated | `aria-live="polite"` | Normal |
| Error saving classification | `aria-live="assertive"` | High |
| Filter results count changed | `aria-live="polite"` | Normal |
| Side panel content updated | `aria-live="polite"` | Normal |

---

## Motion and Animation (WCAG 2.3.3)

### Reduced Motion Support
All animations must respect `prefers-reduced-motion: reduce`.

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Specific animations to disable/reduce:**
- Side panel slide transition: Replace with instant show/hide
- Bulk action bar slide: Replace with instant show/hide
- Row highlight pulse: Replace with static background change
- Badge scale animation: Remove
- Toast slide: Replace with instant show/hide
- Confidence counter animation: Show final value immediately

---

## Touch Target Sizes (WCAG 2.5.8 -- 24x24px minimum)

| Element | Current Size | Pass? |
|---|---|---|
| Row checkbox | ~18x18px visible, but clickable area should be full cell (40px) | Pass if cell is target |
| Filter chip close button | ~12x12px icon | **Fail** |
| Classification badge (clickable) | ~24px height by variable width | Borderline |
| Accept suggestion button | ~32x32px | Pass |
| Side panel close button | 32x32px | Pass |

**Recommendation:**
- Filter chip close button: Increase clickable area to 24x24px minimum (larger invisible hit area around the 12px icon)
- Classification badge: Ensure minimum 24px hit area by adding padding to the clickable region

---

## Form Accessibility (WCAG 3.3.1, 3.3.2)

### Classification Dropdown
- Must have a visible label or `aria-label`
- Error states (failed to save) must be announced and visible
- The selected value must be announced to screen readers

### Filter Inputs
- Search input: visible placeholder is not sufficient as a label. Add `aria-label="Search fields, tables, and sources"`
- Filter dropdowns: must have visible labels or `aria-label` attributes

### Policy Configuration Form (Admin)
- All form fields must have associated `<label>` elements
- Required fields must be marked with `aria-required="true"`
- Validation errors must be associated with fields via `aria-describedby`
- Error summary should appear at the top of the form and be announced

---

## Content Accessibility

### Data Tables
- Tables must use proper `<th>` elements with `scope="col"` or `scope="row"`
- Sortable columns should indicate sort direction via `aria-sort`
- Empty cells should contain "None" or similar text (not be blank)

### Charts/Visualizations (Dashboard)
- Coverage heatmap must have a text alternative (summary table)
- Color must not be the only means of conveying coverage status -- include text percentages
- The progress bars on the dashboard should have `role="meter"` with value attributes

### Status Indicators
- Colored dots alone must not convey review status. The text label ("Approved", "Needs Review") is required alongside the dot.
- This is correctly specified in the design -- the dot is decorative; the text carries the meaning.

---

## Summary of Required Fixes

### Must Fix (Level A violations)
1. **Filter chip close button touch target:** Increase to 24x24px minimum
2. **Search input labeling:** Add `aria-label` (placeholder is insufficient)
3. **Classification combobox ARIA:** Implement full combobox pattern per APG

### Should Fix (Level AA violations)
4. **Error text contrast on white:** Use #A33F31 instead of #BF5547 when on white backgrounds
5. **Health badge text contrast:** Strengthen to #A33F31
6. **Reduced motion support:** Implement `prefers-reduced-motion` media query for all animations

### Recommended (Best Practices)
7. **Group label contrast:** Use #6B6760 for classification-specific group labels
8. **Live regions:** Implement `aria-live` for dynamic content updates
9. **Focus management:** Ensure proper focus return when panels close
10. **Column header sorting announcements:** Add `aria-sort` to sortable columns

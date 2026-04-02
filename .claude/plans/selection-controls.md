# Selection Controls Component Page

## Overview
Create a new **Selection Controls** component page at `/Users/richhemsley/Desktop/design-system-labs/components/selection-controls.html` covering advanced checkbox, radio, and toggle patterns beyond the basic form inputs already documented. Focused on enterprise data security product use cases.

## Patterns to Include

### 1. Checkbox Group with Select All
- Vertical stack of checkboxes with a "Select all" parent checkbox
- Parent shows indeterminate state when some children are checked
- Use case: Bulk selecting data classifications, permission sets

### 2. Radio Card Group
- Bordered cards with radio selection (only one selectable)
- Each card has a title, description, and optional icon
- Selected card gets highlighted border + subtle background
- Use case: Choosing a policy type, selecting a scan mode

### 3. Checkbox Card Group
- Same card pattern but with multi-select (checkboxes)
- Use case: Selecting data sources to monitor, choosing notification channels

### 4. Toggle List
- Vertical list of label + description rows with toggles on the right
- Optional section grouping with dividers
- Use case: Settings pages (enable/disable features, notifications)

### 5. Filter Chips
- Horizontal row of pill-shaped toggleable chips
- Single-select and multi-select variants
- Active chip gets filled background
- Use case: Filtering dashboard views, log severity levels

### 6. Inline Checkbox Table
- Table rows with leading checkboxes, bulk select header, and action bar
- Shows selected count and bulk action buttons when items are selected
- Use case: Data table row selection for bulk operations

## Page Structure (following gold standard from tags.html)

```
Imports: colors.css, spacing.css, typography.css, Material Symbols
Page chrome CSS (gold standard)
Component CSS (all selection control patterns)

<h1>Selection Controls</h1>
<p class="page-subtitle">Advanced selection patterns for checkboxes, radios, and toggles...</p>

<h2>Checkbox Group</h2>
<p>Intro text</p>
<div class="demo-block">Select all + children demos</div>

<h2>Radio Cards</h2>
<p>Intro text</p>
<div class="demo-block">Card group demos</div>

<h2>Checkbox Cards</h2>
<p>Intro text</p>
<div class="demo-block">Multi-select card demos</div>

<h2>Toggle List</h2>
<p>Intro text</p>
<div class="demo-block">Settings-style toggle list</div>

<h2>Filter Chips</h2>
<p>Intro text</p>
<div class="demo-block">Single-select and multi-select chip rows</div>

<h2>Inline Checkbox Table</h2>
<p>Intro text</p>
<div class="demo-block">Table with row checkboxes and bulk actions</div>

<h2>Specifications</h2>
<table class="spec-table">Token/property reference for all patterns</table>

<script src="../shared/nav.js"></script>
```

## CSS Class Naming
All classes use `.sds-` prefix following system convention:
- `.sds-checkbox-group`, `.sds-checkbox-group-parent`
- `.sds-radio-card`, `.sds-radio-card-group`
- `.sds-checkbox-card`, `.sds-checkbox-card-group`
- `.sds-toggle-list`, `.sds-toggle-list-item`
- `.sds-chip`, `.sds-chip-group`
- `.sds-selection-table`, `.sds-selection-bar`

## Integration Steps

1. **Create** `selection-controls.html` with all patterns, CSS, and interactive JS demos
2. **Update nav.js** — Add `Selection Controls` entry in alphabetical order within Components group (between `Side Navigation` and `Tables`)
3. **Update index.html** — Add card with SVG preview in alphabetical order within the Components section (between `Side Navigation` and `Tables`)

## Design Tokens Used
- Existing checkbox/radio/toggle tokens from form-inputs (reused, not redefined)
- `--sds-interactive-primary` for selected states
- `--sds-border-focus` + box-shadow ring for focus
- `--sds-bg-subtle` for card hover/selected backgrounds
- `--sds-border-default` / `--sds-border-strong` for card borders

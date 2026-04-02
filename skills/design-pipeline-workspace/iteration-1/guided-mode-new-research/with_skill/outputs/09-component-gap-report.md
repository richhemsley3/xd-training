# Component Gap Report

## Data Lineage Visualization — Missing Design System Components

**Date:** 2026-03-20
**Design System:** Software DS (Design System Lab)
**Components available:** Header (`header.html`), Side Navigation (`side-navigation.html`), Color tokens (`tokens/colors.css`)

---

## Components Used from Software DS

| Component | Source | Usage in Prototype |
|-----------|--------|-------------------|
| Header | `header.html` | Top-level app header with logo, search, actions |
| Side Navigation | `side-navigation.html` | Primary navigation with groups, icons, active state |
| Color Tokens | `tokens/colors.css` | All colors via semantic tokens (--sds-*) |

---

## Missing Components (Not in Software DS)

### 1. Page Tabs
- **Where used:** Explorer / Impact analysis / Incidents tabs within Data Lineage
- **Description:** Horizontal tab bar for secondary navigation within a page context. Underline-style active indicator with SDS blue-750.
- **Closest existing component:** None -- side navigation has active state patterns but no horizontal tab component.
- **Specification:** Height 40px, label in 13px medium weight, 2px bottom border for active state, no background fill.

### 2. Filter Chip / Toggle Chip
- **Where used:** Toolbar classification filters (PII, PHI, All classifications)
- **Description:** Small toggle-able pill buttons for filtering. Support `aria-pressed` state. Active state uses blue-050 background + blue-750 border.
- **Closest existing component:** None.
- **Specification:** Height 28px, border-radius 6px, icon + text, toggleable active state.

### 3. Icon Button
- **Where used:** Toolbar actions (list view, fit to screen), zoom controls, notifications
- **Description:** Square button containing only a Material Symbol icon. 32x32 with border and hover background.
- **Closest existing component:** Header help button (circular) is similar but uses round shape and different sizing.
- **Specification:** 32x32px, border-radius 8px, border 1px solid warm-gray-150, hover: bg-subtle.

### 4. Primary Button
- **Where used:** (Would be used in empty states, confirmation dialogs)
- **Description:** Filled button with blue-750 background, white text, icon support.
- **Closest existing component:** None.
- **Specification:** Padding 6px 14px, border-radius 8px, font 13px medium, bg interactive-primary.

### 5. Secondary Button
- **Where used:** Export button in toolbar
- **Description:** Outlined button with warm-gray-700 border, white background, icon support.
- **Closest existing component:** None.
- **Specification:** Padding 6px 14px, border-radius 8px, font 13px medium, border 1px solid warm-gray-700.

### 6. Search Input
- **Where used:** Toolbar asset search, global header search
- **Description:** Input field with search icon prefix, bg-surface background, rounded corners.
- **Closest existing component:** None.
- **Specification:** Height 32px, border-radius 8px, bg warm-gray-025, border warm-gray-150, search icon 18px.

### 7. Side Panel (Detail Panel)
- **Where used:** Node detail view on graph click
- **Description:** Sliding panel from right side with header, tabs, and scrollable body. Supports keyboard dismiss (Escape).
- **Closest existing component:** None.
- **Specification:** Width 380px, absolute positioned, slide-in transition 0.2s, shadow -4px 0 16px.

### 8. Status Tag / Badge
- **Where used:** Classification badges (PII, PHI), protection status (Protected, Partial, Unprotected), column info (PK)
- **Description:** Small colored tag with text label. Uses status color tokens (error for PII, purple for PHI, success for protected, warning for partial).
- **Closest existing component:** Stat cards in the research report use similar color patterns.
- **Specification:** Padding 2px 8px, border-radius 4px, font 11px semibold, background/text from status tokens.

### 9. Graph Legend
- **Where used:** Overlay on lineage graph canvas
- **Description:** Floating card with color-dot legend items for classification and protection status.
- **Closest existing component:** None.
- **Specification:** Card with 8px border-radius, shadow, 12px caption text, 8px color dots.

### 10. Minimap
- **Where used:** Bottom-right of graph canvas
- **Description:** Thumbnail overview of the full graph with viewport indicator for navigation.
- **Closest existing component:** None.
- **Specification:** 180x120px, card styling, SVG miniature, draggable viewport rectangle.

### 11. Zoom Controls
- **Where used:** Bottom-left of graph canvas
- **Description:** Vertical stack of icon buttons for zoom in/out/fit. Card-style container.
- **Closest existing component:** Derived from Icon Button (gap #3).
- **Specification:** 36px square buttons stacked vertically, card wrapper with border-radius 8px.

### 12. Status Bar
- **Where used:** Bottom of main content area
- **Description:** Thin bar showing system status: connection status, asset count, warnings, zoom level.
- **Closest existing component:** None.
- **Specification:** Height ~28px, caption text, warm-gray-550, border-top subtle, flex layout.

### 13. Column List Item
- **Where used:** Side panel columns tab
- **Description:** Row showing column name, data type (mono font), and classification badge.
- **Closest existing component:** Table rows in the research report are somewhat similar.
- **Specification:** Flex row, space-between, 13px label text, caption mono for type, border-bottom subtle.

### 14. Detail Row (Label + Value)
- **Where used:** Side panel overview tab
- **Description:** Stacked label (overline) + value (label) pattern for metadata display.
- **Closest existing component:** Stat card uses a similar label/value pattern but with centered alignment.
- **Specification:** Label: 11px semibold uppercase warm-gray-400. Value: 13px regular warm-gray-900.

### 15. Graph Node
- **Where used:** Lineage graph nodes
- **Description:** SVG-rendered card representing a data asset with title, subtitle, classification badge, type icon, and protection dot.
- **Closest existing component:** None -- this is a domain-specific visualization component.
- **Specification:** SVG rect 160-180px wide, 60-65px tall, white fill, warm-gray-150 stroke, 8px border-radius.

---

## Priority Recommendations for Design System Team

### High Priority (used across multiple features)
1. **Primary Button** -- Needed everywhere; currently ad-hoc in every prototype
2. **Secondary Button** -- Needed everywhere alongside primary
3. **Search Input** -- Needed in header and many feature pages
4. **Status Tag / Badge** -- Used for classification, status, and metadata display across the product
5. **Page Tabs** -- Used for secondary navigation in multiple features

### Medium Priority (used in specific features)
6. **Filter Chip** -- Used in lineage and likely in catalog, reports
7. **Icon Button** -- Used in toolbars across features
8. **Side Panel** -- Reusable detail panel pattern for catalog, policies, and lineage
9. **Detail Row** -- Common metadata display pattern

### Lower Priority (domain-specific)
10. **Graph Node** -- Specific to lineage visualization
11. **Graph Legend** -- Specific to graph views
12. **Minimap** -- Specific to graph views
13. **Zoom Controls** -- Specific to graph views
14. **Status Bar** -- May be useful product-wide but lower immediate need
15. **Column List Item** -- Specific to schema/lineage detail views

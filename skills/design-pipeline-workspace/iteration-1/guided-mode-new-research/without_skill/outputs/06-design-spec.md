# Design Specification: Data Lineage Visualization
## Component & Interaction Reference

**Date:** 2026-03-20

---

## Design Principles

1. **Search-first, not graph-first** -- Users start by finding a specific asset, not browsing the entire graph
2. **Security-aware by default** -- Protection status overlay is ON by default; this is our differentiator
3. **Progressive disclosure** -- Start at table-level; let users drill into column-level on demand
4. **Familiar metaphors** -- Stoplight colors for status; map-like pan/zoom for navigation
5. **Dual-mode accessibility** -- Works for both technical users (engineers) and business users (stewards, compliance)

---

## Color System for Lineage

### Node Type Colors (left border indicator)
| Type | Color | Token |
|------|-------|-------|
| Source | `#6AA5B8` | `--sds-color-blue-350` |
| Transformation | `#C39DE3` | `--sds-color-purple-300` |
| Destination | `#7A9A01` | `--sds-color-green-400` |
| Alert/Issue | `#CF6253` | `--sds-color-red-450` |

### Protection Status (stoplight pattern)
| Status | Badge BG | Badge Text | Dot Color |
|--------|----------|------------|-----------|
| Protected | `--sds-color-green-025` | `--sds-color-green-650` | `--sds-color-green-400` |
| Partial | `--sds-color-yellow-025` | `--sds-color-yellow-500` | `--sds-color-yellow-200` |
| Unprotected | `--sds-color-red-050` | `--sds-color-red-650` | `--sds-color-red-450` |

### Classification Tags
| Classification | Background | Text |
|---------------|-----------|------|
| PII | `--sds-color-red-100` | `--sds-color-red-650` |
| Financial | `--sds-color-blue-100` | `--sds-color-blue-700` |
| Internal | `--sds-color-warm-gray-100` | `--sds-color-warm-gray-650` |
| PHI | `#F7EEFF` | `--sds-color-purple-550` |

---

## Component Specifications

### Lineage Node
- **Border:** 1.5px solid `--sds-border-default`
- **Border radius:** 10px
- **Background:** `--sds-bg-page` (white)
- **Padding:** 12px 16px
- **Min width:** 160px
- **Left type indicator:** 3px wide, rounded, colored by node type
- **Hover:** border darkens to `--sds-color-warm-gray-250`, subtle shadow
- **Selected:** border `--sds-interactive-primary`, 3px focus ring at 10% opacity, elevated shadow

### Node Icon
- **Size:** 28x28px
- **Border radius:** 6px
- **Background:** Tinted to match node type (e.g., blue-050 for sources)
- **Icon size:** 16x16px SVG, stroke-based, 1.5px stroke

### Edge Lines
- **Default:** 1.5px solid `--sds-color-warm-gray-200`
- **Highlighted (connected to selected):** 2px solid `--sds-interactive-primary`
- **Arrowhead:** 8x6px triangle markers
- **Curve:** Cubic bezier for smooth routing

### Search Bar
- **Border:** 1.5px solid `--sds-border-default`
- **Border radius:** 10px
- **Padding:** 10px 16px
- **Font size:** 14px
- **Focus:** border `--sds-interactive-primary`, 3px ring at 10% opacity
- **Keyboard shortcut badge:** `/` key shown at right

### Toolbar Buttons
- **Padding:** 5px 12px
- **Border radius:** 6px
- **Font size:** 12px, weight 500
- **Default:** border `--sds-border-default`, white bg
- **Active:** bg `--sds-color-blue-050`, text `--sds-interactive-primary`, border `--sds-color-blue-200`

### Detail Panel
- **Width:** 320px
- **Border left:** 1px solid `--sds-border-default`
- **Section dividers:** 1px solid `--sds-border-subtle`
- **Section title:** 11px, weight 600, uppercase, `--sds-color-warm-gray-400`

### Minimap
- **Size:** 140x90px
- **Position:** Bottom-right of canvas, 16px inset
- **Border radius:** 8px
- **Background:** white at 92% opacity with 8px blur
- **Viewport indicator:** 1.5px border `--sds-interactive-primary`

### Zoom Controls
- **Button size:** 36x36px
- **Position:** Bottom-left of canvas, 16px inset
- **Border radius:** 8px top, 8px bottom (grouped)
- **Icons:** `+` and `-` at 18px

---

## Interaction States

### Node Selection
1. Click node: select, show detail panel, highlight connected edges
2. Click canvas: deselect, hide detail panel
3. Double-click node: expand/collapse connections
4. Right-click node: context menu (View in catalog, Copy link, Export subtree)

### Graph Navigation
1. Pan: click-drag on canvas background
2. Zoom: scroll wheel, pinch, or zoom buttons
3. Fit to view: double-click empty canvas
4. Center on node: click from search results

### Search
1. Focus search: click or press `/`
2. Type: autocomplete appears after 2 characters
3. Results: show icon, name, subtitle, classification tags
4. Select: Enter or click to center graph on that asset
5. Recent: shown on focus before typing

### Overlay Toggles
1. Protection: ON by default, shows status badges on all nodes
2. Quality: ON by default, shows health indicator
3. Classifications: OFF by default, shows PII/PHI/FIN tags
4. Access: OFF by default, shows access policy information

---

## Responsive Behavior

| Breakpoint | Sidebar | Detail Panel | Canvas |
|-----------|---------|-------------|--------|
| >= 1440px | 220px expanded | 320px | Fills remaining space |
| 1024-1439px | 56px collapsed | 280px | Fills remaining space |
| < 1024px | Hidden (hamburger) | Full-width overlay | Full width |

---

## Accessibility Requirements

- All interactive elements must be keyboard-navigable
- Nodes are focusable with Tab key; Enter to select
- Arrow keys navigate between connected nodes
- Status colors must not be the sole indicator (text labels required)
- Minimum contrast ratio: 4.5:1 for text, 3:1 for UI components
- Screen reader: nodes announce name, type, protection status
- Reduced motion: disable edge animations and transitions

---

> **GUIDED MODE PAUSE POINT:** In a guided process, this spec would be reviewed by engineering for feasibility before handoff. Key questions: (1) Can we render 1000+ nodes performantly? (2) What graph layout algorithm should we use? (3) How do we handle cross-system lineage stitching? (4) What is the API contract for lineage data?

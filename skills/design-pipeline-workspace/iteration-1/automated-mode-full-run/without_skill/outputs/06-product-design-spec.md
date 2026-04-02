# Product Design Specification: Data Classification Workflow

## Design System Reference

This specification uses the **Software DS** design system. All colors, typography, and component patterns reference tokens defined in `tokens/colors.css` and component patterns from `header.html` and `side-navigation.html`.

---

## 1. Classification Dashboard

### Layout
- **Shell:** Standard app shell (56px header + 220px side navigation + content area)
- **Content padding:** 24px
- **Breadcrumb:** "Data Security > Data Classification"
- **Page title:** "Data Classification" -- 24px, font-weight 600, `--sds-text-primary`

### Summary Cards Row

Three summary cards in a horizontal row with 16px gap.

**Card: Classification Coverage**
```
+-----------------------------------+
| Classification Coverage           |
|                                   |
| 78%        +12% from last month   |
| ████████░░                        |
| 4,230 of 5,423 fields            |
+-----------------------------------+
```

- Card background: `--sds-bg-card` (white)
- Border: 1px solid `--sds-border-default` (#E0DCD3)
- Border-radius: 8px
- Padding: 20px
- Title: 13px, font-weight 500, `--sds-text-secondary`
- Large number: 32px, font-weight 700, `--sds-text-primary`
- Trend indicator: 13px, `--sds-status-success-text` (green) for positive, `--sds-status-error-text` (red) for negative
- Progress bar: 4px height, border-radius 2px, track `--sds-bg-subtle`, fill `--sds-interactive-primary`
- Subtitle: 13px, `--sds-text-tertiary`

**Card: Review Queue**
```
+-----------------------------------+
| Review Queue                      |
|                                   |
| 142                               |
| fields need human review          |
| [Start reviewing ->]              |
+-----------------------------------+
```

- Same card styling as above
- Large number: 32px, font-weight 700, `--sds-status-warning-text` if > 0, `--sds-status-success-text` if 0
- CTA link: 13px, font-weight 500, `--sds-text-link` (#013D5B), underline on hover

**Card: Unclassified**
```
+-----------------------------------+
| Unclassified Fields               |
|                                   |
| 1,193                             |
| across 8 data sources             |
| [View unclassified ->]            |
+-----------------------------------+
```

- Same card styling
- Large number: 32px, font-weight 700, `--sds-status-error-text` if > 0

### Coverage by Data Source Table

Full-width table below the summary cards. 24px top margin.

**Table header:**
- Background: `--sds-bg-subtle` (#F4F1EB)
- Font: 12px, font-weight 600, `--sds-text-secondary`, uppercase, letter-spacing 0.4px
- Padding: 10px 16px
- Border-bottom: 2px solid `--sds-border-default`

**Columns:**
| Column | Width | Alignment |
|---|---|---|
| Data Source | flex | left |
| Total Fields | 120px | right |
| Classified | 120px | right |
| Unclassified | 120px | right |
| Needs Review | 120px | right |
| Coverage | 100px | right |

**Table rows:**
- Font: 13px, `--sds-text-primary` for first column, `--sds-text-secondary` for others
- Padding: 12px 16px
- Border-bottom: 1px solid `--sds-border-subtle` (#EBE6DD)
- Hover background: `--sds-bg-subtle`
- Cursor: pointer (row is clickable)

**Coverage percentage display:**
- Inline progress bar (48px wide, 4px height) + percentage text
- Color thresholds:
  - 90-100%: `--sds-status-success-strong` (#7A9A01)
  - 70-89%: `--sds-status-warning-strong` (#EBCE2D)
  - Below 70%: `--sds-status-error-strong` (#CF6253)

**Data source icon:**
- 20x20px icon preceding the source name
- 8px gap between icon and name
- Icons for common sources: Snowflake, BigQuery, PostgreSQL, S3, etc.

---

## 2. Classification Workspace

### Tab Bar
Positioned below the page title. Follows the tab pattern from the Software DS side-navigation.html component.

- Tab font: 13px, `--sds-text-tertiary` (inactive), `--sds-nav-item-active-text` (#013D5B) (active)
- Active tab: font-weight 500, 2px bottom border `--sds-interactive-primary`
- Tab padding: 10px 16px
- Badge (count): Inline, 11px, background `--sds-interactive-primary-subtle` (#D9EBED), color `--sds-interactive-primary`, padding 1px 6px, border-radius 10px

**Tabs:**
- All fields (5,423)
- Review queue (142)
- Unclassified (1,193)
- Recently modified

### Filter Bar
Below tabs, 16px margin-top.

**Search input:**
- Width: 280px
- Height: 36px
- Border: 1px solid `--sds-border-strong` (#D0CBC3)
- Border-radius: 8px
- Placeholder: "Search fields, tables, sources..."
- Font: 13px
- Focus border: `--sds-border-focus` (#013D5B)
- Search icon (magnifying glass) at left, 16px, `--sds-text-tertiary`

**Filter dropdowns:**
- Height: 36px
- Border: 1px solid `--sds-border-default`
- Border-radius: 8px
- Font: 13px, `--sds-text-secondary`
- Chevron icon at right
- Labels: "Source", "Classification", "Sensitivity", "Status"

**Active filter chips:**
- Appear in a row below the filter bar, 8px gap
- Background: `--sds-interactive-primary-subtle` (#D9EBED)
- Color: `--sds-interactive-primary` (#013D5B)
- Font: 12px, font-weight 500
- Padding: 4px 8px 4px 10px
- Border-radius: 16px
- Close icon (X): 12px, right side, hover turns to `--sds-status-error-text`

### Data Table

**Columns (All Fields tab):**
| Column | Width | Content |
|---|---|---|
| Checkbox | 40px | Selection checkbox |
| Source | 160px | Source icon + name |
| Schema / Table | 200px | Hierarchical path |
| Field Name | flex | Field/column name |
| Data Type | 100px | String, Number, Date, etc. |
| Classification | 180px | Classification badge (editable) |
| Sensitivity | 120px | Sensitivity level badge |
| Confidence | 90px | AI confidence (if suggestion exists) |
| Status | 100px | Review status |

**Additional columns (Review Queue tab):**
| Column | Width | Content |
|---|---|---|
| AI Suggestion | 180px | Suggested classification badge |
| Actions | 100px | Accept / Change buttons |

**Classification badge (in table cell):**
- Inline badge: background varies by category, rounded corners
- PII tags: background `--sds-status-info-bg` (#EBF4F5), text `--sds-status-info-text` (#0C4A69)
- Financial tags: background `--sds-status-purple-bg` (#F7EEFF), text `--sds-status-purple-text` (#805AA1)
- Health tags: background `--sds-status-error-bg` (#FFEEEB), text `--sds-status-error-text` (#BF5547)
- Auth tags: background `--sds-status-warning-bg` (#FCF9D9), text `--sds-status-warning-text` (#8A7515)
- Business tags: background `--sds-status-neutral-bg` (#EBE6DD), text `--sds-status-neutral-text` (#54514D)
- Technical tags: background `--sds-bg-subtle`, text `--sds-text-tertiary`
- Badge padding: 2px 8px
- Badge border-radius: 4px
- Badge font: 12px, font-weight 500

**Sensitivity level badge:**
- Restricted: background `--sds-status-error-bg`, text `--sds-status-error-text`
- Confidential: background `--sds-status-warning-bg`, text `--sds-status-warning-text`
- Internal: background `--sds-status-info-bg`, text `--sds-status-info-text`
- Public: background `--sds-status-success-bg`, text `--sds-status-success-text`

**Review status indicators:**
- Unreviewed: gray dot + "Unreviewed" in `--sds-text-tertiary`
- Approved: green dot + "Approved" in `--sds-status-success-text`
- Needs Review: yellow dot + "Needs Review" in `--sds-status-warning-text`
- Rejected: red dot + "Rejected" in `--sds-status-error-text`
- Dot: 6px circle, filled, 6px right margin

### Bulk Action Bar

Appears at the bottom of the content area when rows are selected.

- Position: sticky bottom
- Background: `--sds-interactive-primary` (#013D5B)
- Color: `--sds-text-on-primary` (white)
- Height: 56px
- Border-radius: 12px 12px 0 0
- Padding: 0 24px
- Box-shadow: 0 -4px 12px rgba(0,0,0,0.1)

**Contents (left to right):**
- Checkbox (to deselect all): 16px, white
- Selected count: "14 fields selected" -- 14px, font-weight 500
- Divider: 1px vertical, rgba(255,255,255,0.2), 20px height
- "Classify as..." button: ghost white, 13px, font-weight 500, 8px 16px padding, border 1px solid rgba(255,255,255,0.3), border-radius 6px
- "Set sensitivity..." button: same styling
- Spacer (flex)
- "Clear selection" text button: 13px, rgba(255,255,255,0.7), underline on hover

---

## 3. Field Detail Side Panel

### Panel Container
- Width: 400px
- Background: `--sds-bg-card` (white)
- Border-left: 1px solid `--sds-border-default`
- Box-shadow: -4px 0 12px rgba(0,0,0,0.06)
- Overflow-y: auto
- Z-index: above table content

### Panel Header
- Padding: 20px 24px 16px
- Border-bottom: 1px solid `--sds-border-subtle`
- Field name: 18px, font-weight 600, `--sds-text-primary`
- Source path: 12px, `--sds-text-tertiary`, "Snowflake > analytics_db > users > email_address"
- Close button: top-right, 32x32px, `--sds-text-tertiary`, hover `--sds-text-primary`

### Section: Sample Data
- Section title: 11px, font-weight 600, uppercase, letter-spacing 0.4px, `--sds-text-tertiary`, padding-bottom 8px
- Values displayed in a monospace font: 13px, `SF Mono` / `Menlo`
- Background: `--sds-bg-subtle` (#F4F1EB)
- Padding: 12px 16px
- Border-radius: 8px
- Each value on its own line, with alternating subtle backgrounds
- Masked values show: "j***@example.com" format

### Section: AI Analysis
- Suggested tag badge (same badge styling as table)
- Confidence bar: 100px wide, 6px height, filled portion colored by threshold
- Confidence percentage: 13px, font-weight 600, colored by threshold
- Reasoning text: 13px, `--sds-text-secondary`, e.g., "Matched pattern: email format (95% of values match RFC 5322)"

### Section: Classification
- Dropdown for classification tag: full-width, 40px height
- Dropdown for sensitivity level: full-width, 40px height
- Both use `--sds-border-strong` border, `--sds-border-focus` on focus
- "Applied by" metadata: 12px, `--sds-text-tertiary`

### Section: Applicable Policies
- List of linked policies
- Each policy: card with 1px border `--sds-border-subtle`, 8px border-radius, 12px padding
- Policy name: 13px, font-weight 500, `--sds-text-link`
- Policy description: 12px, `--sds-text-tertiary`

### Section: Related Fields
- Compact table showing related fields across sources
- Columns: Source, Table, Field, Classification
- Max 5 rows shown, "View all [N] related" link

### Section: History
- Timeline layout with vertical line on the left
- Each event: avatar circle (20px) + "Dana H. changed classification to PII - Email" + timestamp
- Avatar: matches header component pattern from Software DS
- Text: 13px, `--sds-text-secondary`
- Timestamp: 12px, `--sds-text-tertiary`

### Section: Comments
- Thread layout
- Comment input at bottom: textarea, 80px min-height, `--sds-border-default` border
- Submit button: `--sds-interactive-primary` background, white text, 8px 16px padding, 6px border-radius
- Existing comments: avatar + name + timestamp + message body

---

## 4. Typography Summary

| Element | Size | Weight | Token/Color |
|---|---|---|---|
| Page title | 24px | 600 | `--sds-text-primary` |
| Section title | 18px | 600 | `--sds-text-primary` |
| Card title | 13px | 500 | `--sds-text-secondary` |
| Card large number | 32px | 700 | Varies by status |
| Table header | 12px | 600 | `--sds-text-secondary`, uppercase |
| Table body | 13px | 400 | `--sds-text-primary` (primary col), `--sds-text-secondary` (others) |
| Badge text | 12px | 500 | Varies by category |
| Filter label | 13px | 400 | `--sds-text-secondary` |
| Breadcrumb | 13px | 400 | `--sds-text-link` |
| Caption/metadata | 12px | 400 | `--sds-text-tertiary` |
| Group label | 11px | 600 | `--sds-text-tertiary`, uppercase, 0.4px letter-spacing |

---

## 5. Iconography

All icons follow the Software DS pattern: 18x18px, stroke-based, 1.5px stroke width, `stroke-linecap: round`, `stroke-linejoin: round`.

**Custom icons needed for this feature:**
- Classification tag (label/tag icon)
- Sensitivity shield (shield with levels)
- AI suggestion (sparkle/wand icon)
- Confidence meter (gauge icon)
- Review checkmark (checkmark in circle)
- Data source icons (database, cloud storage, etc.)
- Filter funnel
- Bulk select (stacked checkboxes)

Default icon color: `--sds-text-tertiary` (#6B6760)
Active icon color: `--sds-interactive-primary` (#013D5B)
Hover icon color: `--sds-text-primary` (#1C1A17)

---

## 6. Responsive Considerations

This is a desktop-first enterprise application. Minimum supported viewport: 1280px wide.

| Viewport | Side Nav | Detail Panel | Behavior |
|---|---|---|---|
| >= 1440px | 220px expanded | 400px | Full layout |
| 1280-1439px | 220px expanded | 360px | Slightly narrower panel |
| 1024-1279px | 56px collapsed | 400px overlay | Panel overlays table |
| < 1024px | Hidden (hamburger) | Full-width overlay | Mobile not primary target |

# Interaction Design: Data Classification Workflow

## Core Interaction Patterns

---

## Pattern 1: Inline Classification Editing

**Trigger:** User clicks on the classification cell in the data table.

**Behavior:**
1. The cell transforms into a dropdown/combobox with the classification taxonomy.
2. The dropdown shows recently used tags at the top, then the full taxonomy grouped by category.
3. User can type to filter the list.
4. Selecting a tag applies it immediately (optimistic update).
5. A brief success toast appears: "Classification applied."
6. The cell returns to display mode with the new tag shown as a colored badge.

**Keyboard support:**
- Tab to the classification cell
- Enter or Space to open the dropdown
- Type to filter
- Arrow keys to navigate
- Enter to select
- Escape to cancel

**Edge cases:**
- If the field already has a classification, the current value is pre-selected in the dropdown.
- If a policy requires a specific classification, a hint appears in the dropdown.
- If the user removes a classification, a confirmation appears.

---

## Pattern 2: Bulk Classification

**Trigger:** User selects multiple rows using checkboxes.

**Behavior:**
1. When the first checkbox is selected, a bulk action bar slides up from the bottom of the table area.
2. The bar shows: selected count, "Classify as..." button, "Set sensitivity..." button, "Clear" button.
3. Clicking "Classify as..." opens the classification dropdown (same as inline).
4. Selecting a tag applies it to ALL selected fields.
5. A confirmation dialog appears: "Apply [PII - Email Address] to 14 fields?"
6. On confirm, all selected fields are updated with a batch animation (rows briefly highlight green).
7. The bulk action bar dismisses. Checkboxes are cleared.

**Keyboard support:**
- Shift+Click for range selection
- Cmd/Ctrl+Click for individual toggle
- Cmd/Ctrl+A to select all visible rows
- The bulk action bar is keyboard-accessible

**Selection helpers:**
- "Select all on this page" checkbox in the table header
- "Select all [N] matching fields" link when filters are active
- "Select all with same AI suggestion" quick action

---

## Pattern 3: AI Suggestion Review

**Trigger:** User navigates to the "Review queue" tab.

**Behavior:**
1. The table shows fields with AI suggestions, sorted by confidence (lowest first by default).
2. Each row displays: field name, source, AI-suggested classification (badge), confidence score (percentage + color indicator).
3. Confidence colors:
   - 90-100%: `--sds-status-success-text` (green) -- High confidence
   - 70-89%: `--sds-status-warning-text` (yellow) -- Medium confidence
   - Below 70%: `--sds-status-error-text` (red) -- Low confidence
4. Each row has inline actions: "Accept" (checkmark) and "Change" (edit icon).
5. "Accept" applies the AI suggestion immediately.
6. "Change" opens the classification dropdown with the AI suggestion pre-selected.

**Bulk review actions:**
- "Accept all high-confidence" button in the toolbar (accepts all 90%+ suggestions)
- "Accept all on this page" for batch processing
- Filter by confidence range

---

## Pattern 4: Field Detail Side Panel

**Trigger:** User clicks a row in the table (not on the classification cell or checkbox).

**Behavior:**
1. The data table compresses to accommodate a 400px side panel sliding in from the right.
2. The panel contains:
   - **Header:** Field name, source icon + name, close button (X)
   - **Section: Sample Data** -- 5-10 sample values from the field (masked if highly sensitive)
   - **Section: AI Analysis** -- Suggested classification, confidence score, reasoning (which patterns matched)
   - **Section: Classification** -- Current tag (dropdown to change), sensitivity level (dropdown), effective date
   - **Section: Applicable Policies** -- Linked policies with brief descriptions
   - **Section: Related Fields** -- Other fields with similar names or patterns across sources
   - **Section: History** -- Timeline of classification changes (who, when, what)
   - **Section: Comments** -- Threaded comments for discussion
3. Changes made in the panel are saved automatically (with debounce).
4. Navigating to another row in the table updates the panel content without closing it.
5. Close: X button, Escape key, or clicking outside the panel.

**Transitions:**
- Panel slides in: 250ms ease-out
- Panel content transitions: 150ms crossfade when switching between fields
- Panel slides out: 200ms ease-in

---

## Pattern 5: Filter and Search

**Trigger:** User interacts with the filter bar above the data table.

**Components:**
1. **Search box:** Full-text search across field names, table names, source names.
2. **Filter chips:**
   - Source (multi-select dropdown)
   - Classification (multi-select dropdown of tags)
   - Sensitivity level (multi-select)
   - Review status (Unreviewed, Approved, Needs Review, Rejected)
   - Confidence range (slider or preset buttons)
   - Data type (string, number, date, boolean)
3. Active filters appear as removable chips below the filter bar.
4. "Clear all filters" link when any filters are active.
5. Filter changes update the table immediately (no submit button).

**Saved filters:**
- Users can save filter combinations as named views.
- Saved views appear in a dropdown next to the filter bar.

---

## Pattern 6: Classification Dashboard Interactions

**Coverage cards:**
- Clicking a coverage card navigates to the workspace filtered to that context.
- Example: Clicking "23 unclassified fields" opens `/workspace?tab=unclassified`.

**Coverage heatmap/table:**
- Rows represent data sources.
- Columns: Total fields, Classified, Unclassified, Needs Review, Coverage %.
- Clicking a row navigates to the workspace filtered to that source.
- Color-coding: coverage percentage maps to green (high) through red (low).

**Activity feed:**
- Shows recent classification events: "[Dana] classified 14 fields in [Snowflake Production]"
- Clicking an event navigates to the relevant context.

---

## Pattern 7: Policy Configuration (Security Admin)

**Policy creation flow:**
1. "Create policy" button opens a full-page form.
2. **Step 1: Define** -- Name, description, regulation link (optional).
3. **Step 2: Match** -- Define matching criteria:
   - Field name patterns (regex or keyword list)
   - Data patterns (regex against sample values)
   - Data source filters
   - Data type filters
4. **Step 3: Classify** -- Set the classification tag and sensitivity level to apply.
5. **Step 4: Automate** -- Toggle auto-classification, set confidence threshold, choose action (auto-apply or suggest for review).
6. **Step 5: Review** -- Preview matching fields with a live count. Test against current data.
7. Save and activate.

**Policy testing:**
- "Test policy" button shows a preview of which fields would match.
- Results appear in a table identical to the workspace table.
- The admin can refine patterns before activating.

---

## Microinteractions

| Interaction | Animation | Duration | Easing |
|---|---|---|---|
| Classification badge appears | Fade in + scale from 0.9 to 1.0 | 200ms | ease-out |
| Bulk action bar slides up | Translate Y from 100% to 0 | 250ms | ease-out |
| Row highlight on classification | Background color pulse (green-025) | 1000ms | ease-in-out |
| Confidence score change | Number counter animation | 300ms | ease-out |
| Side panel open | Translate X from 100% to 0 | 250ms | cubic-bezier(0.4, 0, 0.2, 1) |
| Side panel close | Translate X from 0 to 100% | 200ms | cubic-bezier(0.4, 0, 0.2, 1) |
| Toast notification | Slide up + fade in, auto-dismiss after 3s | 300ms in, 200ms out | ease-out |
| Checkbox select | Scale bounce 1.0 > 1.1 > 1.0 | 150ms | spring |
| Filter chip added | Fade in + slide right | 200ms | ease-out |
| Filter chip removed | Fade out + slide left | 150ms | ease-in |

---

## Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| `/` or `Cmd+K` | Focus search |
| `Cmd+A` | Select all visible rows |
| `Escape` | Close panel / cancel action / clear selection |
| `Enter` | Open classification dropdown on focused row |
| `Tab` | Move to next interactive element |
| `Shift+Tab` | Move to previous interactive element |
| `Arrow Up/Down` | Navigate table rows |
| `Space` | Toggle row checkbox |
| `Cmd+Enter` | Accept AI suggestion for focused row |
| `Cmd+Shift+Enter` | Accept all visible AI suggestions |

---

## State Management

### Loading States
- Initial page load: Skeleton table (rows of gray bars matching column widths)
- Filter change: Table content fades to 50% opacity, updates, fades back to 100%
- Side panel content: Skeleton blocks for each section

### Empty States
- No fields found (filters applied): "No fields match your filters. Try adjusting your search criteria." + "Clear filters" button.
- No unclassified fields: Success illustration + "All fields are classified. Great work!" + "View all fields" link.
- No AI suggestions: "No AI suggestions available yet. Run a classification scan to generate suggestions." + "Start scan" button.

### Error States
- Classification failed to save: Inline error on the field row + retry button. Toast: "Failed to save classification. Please try again."
- Search failed: "Search encountered an error. Please try again." in the search results area.
- Side panel failed to load: Error message in the panel with retry button.

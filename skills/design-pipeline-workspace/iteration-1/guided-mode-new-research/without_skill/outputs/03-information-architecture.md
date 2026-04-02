# Information Architecture & User Flows
## Data Lineage Visualization Feature

**Date:** 2026-03-20

---

## Navigation Placement

Data Lineage sits within the existing product navigation under a new section. Based on the existing side navigation structure (Getting Started, Tokenization group, Administration group), lineage belongs in the **Tokenization** group alongside Data Catalog, Activity, and Protection Policies -- since lineage is a visualization layer over the same data assets.

### Updated Side Navigation Structure

```
Getting started

TOKENIZATION
  Data catalog
  Data lineage        <-- NEW
  Activity
  Protection policies

ADMINISTRATION
  Connections
  Users
  Domains
```

---

## Page Hierarchy

### Data Lineage Landing Page
The main entry point. Search-first design with a visual lineage explorer.

```
Data Lineage
  |
  |-- Search bar (primary action -- "Search assets, tables, pipelines...")
  |-- Quick filters (System | Database | Table | Column | Pipeline)
  |-- Recent lineage explorations (saved searches / bookmarks)
  |
  |-- Lineage Explorer (main canvas)
  |     |-- Graph view (default)
  |     |-- List view (alternative)
  |     |-- Minimap (bottom-right corner)
  |     |
  |     |-- Node types:
  |     |     Source systems (databases, APIs, files)
  |     |     Transformation nodes (ETL, dbt models, Airflow tasks)
  |     |     Destination systems (warehouses, BI tools, exports)
  |     |
  |     |-- Edge types:
  |     |     Direct flow (solid line)
  |     |     Derived/computed (dashed line)
  |     |
  |     |-- Overlay toggles:
  |           [x] Protection status
  |           [x] Data quality health
  |           [ ] Classification labels
  |           [ ] Access policies
  |
  |-- Detail Panel (right sidebar, contextual)
        |-- Asset overview (name, type, owner, description)
        |-- Protection status
        |-- Data quality score
        |-- Classifications (PII, PHI, Financial, etc.)
        |-- Upstream dependencies (count + list)
        |-- Downstream consumers (count + list)
        |-- Recent changes / activity
        |-- Actions: View in Catalog | Edit Policy | Export
```

### Asset Lineage Detail View
Accessed by clicking an asset in the explorer or from the Data Catalog.

```
Asset Detail > Lineage Tab
  |
  |-- Granularity toggle: System | Table | Column
  |-- Direction toggle: Upstream | Full | Downstream
  |-- Depth slider: 1-5 hops (default: 2)
  |
  |-- Focused lineage graph (centered on selected asset)
  |-- Impact analysis panel
  |     |-- "X upstream sources"
  |     |-- "Y downstream consumers"
  |     |-- "Z affected dashboards"
  |
  |-- Column-level lineage (expandable)
        |-- Column mapping table
        |-- Transformation details
```

---

## Core User Flows

### Flow 1: Search and Explore Lineage (Primary)

```
1. User navigates to Data Lineage page
2. Types search query (e.g., "customer_orders")
3. Autocomplete suggests matching assets with type icons
4. User selects an asset
5. Lineage graph renders, centered on selected asset
   - 2-hop upstream and downstream shown by default
   - Protection status overlay is ON by default
6. User clicks a node to see detail panel
7. User can:
   a. Expand a node (show its connections)
   b. Collapse a branch (reduce complexity)
   c. Switch granularity (system > table > column)
   d. Toggle overlays (quality, classifications)
   e. Export view as image or report
```

### Flow 2: Debug Data Quality Issue (Data Engineer)

```
1. Engineer receives alert about data quality issue in "monthly_revenue" table
2. Clicks "View Lineage" from alert or navigates to Data Lineage
3. Searches for "monthly_revenue"
4. Lineage renders with quality overlay showing RED status on upstream node
5. Engineer traces upstream to find the problematic source
6. Clicks problematic node to see:
   - Recent schema changes
   - Data quality score trend
   - Column-level details
7. Identifies root cause (e.g., schema change in source system)
8. Clicks "View Impact" to see all downstream consumers affected
```

### Flow 3: Audit Preparation (Data Steward / Compliance)

```
1. Steward navigates to Data Lineage
2. Uses filter: Classification = "PII" + Protection Status = "Unprotected"
3. Graph shows all PII data flows lacking protection policies
4. Steward reviews each unprotected flow
5. For each:
   a. Views detail panel showing classification and owner
   b. Clicks "Assign Protection Policy" to link to policy editor
6. Exports filtered view as compliance report (PDF/CSV)
```

### Flow 4: Impact Analysis Before Change (Data Engineer)

```
1. Engineer needs to modify schema of "raw_user_events" table
2. Searches for the table in Data Lineage
3. Toggles to "Downstream only" view
4. Expands to 3-hop depth
5. Sees all downstream tables, models, and dashboards affected
6. Impact summary panel shows:
   - 12 downstream tables
   - 3 dbt models
   - 5 dashboards
   - 2 external data shares
7. Engineer exports impact report to share in PR/Slack
```

---

## Key Interaction Patterns

### Search
- Global search bar at top of lineage page
- Autocomplete with asset type icons (database, table, column, pipeline)
- Recent searches and bookmarked assets
- Supports natural language queries (future: AI-powered)

### Navigation (Graph)
- Pan: Click and drag on canvas
- Zoom: Scroll wheel or pinch gesture
- Fit to view: Double-click on empty canvas or button
- Center on asset: Click asset in search results or list view

### Selection & Detail
- Single click: Select node, show detail panel
- Double click: Expand/collapse node's connections
- Right click: Context menu (View in catalog, Copy link, Export subtree)

### Overlays
- Toggle buttons in toolbar above the graph
- Protection status: Green (protected), Yellow (partial), Red (unprotected), Gray (unclassified)
- Data quality: Green (healthy), Yellow (degraded), Red (critical), Gray (not monitored)
- Classification badges: Small labels on nodes (PII, PHI, Financial, etc.)

---

## Information Density Levels

| Level | Shows | Use Case |
|-------|-------|----------|
| **System** | Source systems, warehouses, BI tools as large nodes | Executive/compliance overview |
| **Table** | Individual tables/datasets with flow arrows | Default working view for most users |
| **Column** | Column-level mappings and transformations | Deep debugging and impact analysis |

---

> **GUIDED MODE PAUSE POINT:** In a guided process, we would review this IA with stakeholders and validate the navigation placement, page hierarchy, and user flows before proceeding to wireframes. Key questions: (1) Does lineage belong in the Tokenization group or should it be a top-level section? (2) Should the default view be graph or list? (3) Is search-first the right entry pattern for all personas?

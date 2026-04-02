# Information Architecture: Data Classification Workflow

## Navigation Placement

The Data Classification feature lives within the existing application shell (header + side navigation) as defined in the Software DS. It is a top-level section in the side navigation under a "Data Security" group.

```
Side Navigation (220px expanded)
------------------------------------
Getting started

[GROUP: Data Security]
  Data catalog
  * Data classification  <-- NEW
  Protection policies
  Activity

[GROUP: Administration]
  Connections
  Users
  Domains
```

---

## Page Hierarchy

### Level 0: Data Classification (Landing / Dashboard)
The entry point provides an overview of classification status across all data sources.

```
/data-classification
```

**Content:**
- Classification coverage summary (overall percentage, trend)
- Coverage by data source (heatmap or table)
- Review queue count (items needing human review)
- Recent activity feed
- Quick actions: "Start classifying", "View review queue"

---

### Level 1: Classification Workspace
The primary working surface where stewards classify fields.

```
/data-classification/workspace
```

**Tabs:**
- **All fields** -- Unified view across all sources
- **Review queue** -- AI-suggested classifications needing review
- **Unclassified** -- Fields with no classification
- **Recently modified** -- Fields changed in the last 7/30 days

**Content:**
- Filterable, sortable data table of fields
- Inline classification editing
- Bulk selection and batch actions
- Field detail side panel

---

### Level 2: Field Detail (Side Panel)
Appears as a slide-over panel from the right, keeping the table visible.

```
/data-classification/workspace?field={fieldId}  (panel state, not a separate page)
```

**Content:**
- Field metadata (name, type, source, table/collection)
- Sample data values (masked if highly sensitive)
- Current classification + history
- AI suggestion with confidence score and reasoning
- Applicable policies
- Comments and activity log
- Related fields (same name pattern across sources)

---

### Level 1: Policies
Configuration surface for classification policies and automation rules.

```
/data-classification/policies
```

**Content:**
- Policy list (name, type, status, field count matched)
- Policy detail editor
- Pattern builder (regex, keyword lists)
- Confidence threshold configuration
- Auto-classification toggle

---

### Level 1: Reports
Audit and compliance reporting.

```
/data-classification/reports
```

**Content:**
- Pre-built report templates
- Coverage report
- Activity report (who classified what, when)
- Compliance report (by regulation)
- Export options (CSV, PDF)

---

## Object Model

```
Data Source (e.g., Snowflake Production)
  |
  +-- Schema / Database
       |
       +-- Table / Collection
            |
            +-- Field / Column
                 |
                 +-- Classification Tag  (e.g., "PII - Email Address")
                 +-- Sensitivity Level   (e.g., "High", "Medium", "Low", "Public")
                 +-- AI Suggestion       (tag + confidence score)
                 +-- Classification History (who, when, what changed)
                 +-- Policy Link         (which policy requires this classification)
                 +-- Review Status       (unreviewed, approved, rejected, needs-review)
```

---

## Classification Taxonomy

### Sensitivity Levels (top-level)
1. **Restricted** -- Highest sensitivity. Regulatory or contractual obligations.
2. **Confidential** -- Internal-only. Business-sensitive.
3. **Internal** -- General internal use. Low risk if exposed.
4. **Public** -- No sensitivity. Safe for external use.

### Classification Tags (nested under sensitivity)
Organized by category:

**Personally Identifiable Information (PII)**
- Full name
- Email address
- Phone number
- Mailing address
- Date of birth
- Government ID (SSN, passport, national ID)
- Driver's license number

**Financial Data**
- Bank account number
- Credit card number
- Tax ID
- Income / salary
- Transaction data

**Health Data (PHI)**
- Medical record number
- Diagnosis / condition
- Treatment information
- Insurance ID
- Prescription data

**Authentication & Access**
- Password / hash
- API key / token
- Access credential
- Session identifier

**Business Confidential**
- Trade secret
- Internal strategy
- Employee performance
- Compensation data
- Customer list

**Technical Metadata**
- System identifier
- Timestamp
- Configuration value
- Log data

---

## Page Templates

### Dashboard Template
```
+-------------------------------------------------------+
| Header (56px)                                         |
+--------+----------------------------------------------+
| Side   | Breadcrumb: Data Security > Classification   |
| Nav    | Page Title: Data Classification              |
| (220px)|                                              |
|        | [Summary Cards Row]                          |
|        | [Coverage] [Review Queue] [Unclassified]     |
|        |                                              |
|        | [Coverage by Source - Table/Heatmap]          |
|        |                                              |
|        | [Recent Activity Feed]                       |
+--------+----------------------------------------------+
```

### Workspace Template
```
+-------------------------------------------------------+
| Header (56px)                                         |
+--------+----------------------------------------------+
| Side   | Breadcrumb: Data Classification > Workspace  |
| Nav    | Page Title: Classification Workspace         |
| (220px)|                                              |
|        | [Tabs: All | Review Queue | Unclassified]    |
|        | [Filter Bar + Search + Bulk Actions]          |
|        | [Data Table - Fields]                        |
|        | | Source | Table | Field | Type | Class. |   |
|        | |--------|-------|-------|------|---------|   |
|        | | ...    | ...   | ...   | ...  | [tag]  |   |
|        |                                              |
|        | [Pagination / Infinite scroll]               |
+--------+----------------------------------------------+
```

### Workspace with Detail Panel
```
+-------------------------------------------------------+
| Header (56px)                                         |
+--------+---------------------------+------------------+
| Side   | [Data Table - compressed] | Field Detail     |
| Nav    | | Source | Field | Class. || Panel (400px)   |
| (220px)| |--------|-------|--------|| Field name      |
|        | | ...    | ...   | [tag]  || Sample data     |
|        | | ...    | ...   | [tag]  || AI suggestion   |
|        | | >>>    | ...   | [tag]  || Confidence: 87% |
|        |                           || Classification  |
|        |                           || [dropdown]      |
|        |                           || Policy context  |
|        |                           || Comments        |
+--------+---------------------------+------------------+
```

---

## Navigation Patterns

| Action | Pattern |
|---|---|
| Enter classification | Side nav click > Dashboard |
| Start classifying | Dashboard CTA > Workspace |
| Open field detail | Row click > Side panel slides in |
| Close field detail | Panel close button or Escape key |
| Switch between tabs | Tab click (no page reload) |
| Filter fields | Filter bar interactions |
| Bulk classify | Checkbox select > Action bar appears |
| Navigate to policies | Tab or breadcrumb |

---

## URL Structure

```
/data-classification                          Dashboard
/data-classification/workspace                Workspace (all fields)
/data-classification/workspace?tab=review     Review queue tab
/data-classification/workspace?tab=unclassified  Unclassified tab
/data-classification/workspace?source={id}    Filtered to source
/data-classification/workspace?field={id}     With detail panel open
/data-classification/policies                 Policy list
/data-classification/policies/{id}            Policy detail
/data-classification/reports                  Reports
/data-classification/reports/{type}           Specific report
```

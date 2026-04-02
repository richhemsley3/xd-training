# Content Design: Data Classification Workflow

## Voice and Tone

Follow the existing product voice: professional, clear, direct. Avoid jargon where possible but use domain terms that data stewards and security admins expect (classification, sensitivity, PII, etc.). Use active voice and present tense.

---

## Page Titles and Headings

| Page | Title | Breadcrumb |
|---|---|---|
| Dashboard | Data Classification | Data Security > Data Classification |
| Workspace | Classification Workspace | Data Classification > Workspace |
| Policies | Classification Policies | Data Classification > Policies |
| Policy Detail | [Policy Name] | Classification Policies > [Policy Name] |
| Reports | Classification Reports | Data Classification > Reports |

---

## Summary Card Copy

### Classification Coverage
- **Title:** Classification Coverage
- **Trend (positive):** +12% from last month
- **Trend (negative):** -3% from last month
- **Trend (neutral):** No change from last month
- **Subtitle:** 4,230 of 5,423 fields

### Review Queue
- **Title:** Review Queue
- **Subtitle (items pending):** fields need human review
- **Subtitle (empty):** All suggestions reviewed
- **CTA:** Start reviewing

### Unclassified Fields
- **Title:** Unclassified Fields
- **Subtitle:** across 8 data sources
- **CTA:** View unclassified

---

## Tab Labels

| Tab | Label | Badge |
|---|---|---|
| All fields | All fields | (total count) |
| Review queue | Review queue | (pending count) |
| Unclassified | Unclassified | (count) |
| Recently modified | Recently modified | -- |

---

## Table Column Headers

| Column | Header Text |
|---|---|
| Checkbox | (no text, checkbox only) |
| Data source | Source |
| Schema/Table | Location |
| Field name | Field |
| Data type | Type |
| Classification | Classification |
| Sensitivity | Sensitivity |
| AI confidence | Confidence |
| Review status | Status |
| AI suggestion | Suggestion |
| Actions | (no header text) |

---

## Classification Taxonomy Labels

### Sensitivity Levels
| Level | Label | Description (tooltip) |
|---|---|---|
| Restricted | Restricted | Highest sensitivity. Subject to regulatory or contractual obligations. |
| Confidential | Confidential | Internal only. Business-sensitive information. |
| Internal | Internal | General internal use. Low risk if exposed. |
| Public | Public | No sensitivity restrictions. Safe for external use. |

### Classification Tags (grouped)
Displayed in the classification combobox:

**Recently Used** (dynamic, based on user history)

**PII**
- Full name
- Email address
- Phone number
- Mailing address
- Date of birth
- Government ID
- Driver's license number

**Financial**
- Bank account number
- Credit card number
- Tax ID
- Income / salary
- Transaction data

**Health (PHI)**
- Medical record number
- Diagnosis / condition
- Treatment information
- Insurance ID
- Prescription data

**Authentication**
- Password / hash
- API key / token
- Access credential
- Session identifier

**Business**
- Trade secret
- Internal strategy
- Employee performance
- Compensation data
- Customer list

**Technical**
- System identifier
- Timestamp
- Configuration value
- Log data

---

## Button Labels

| Context | Label | Notes |
|---|---|---|
| Accept AI suggestion | Accept | Checkmark icon + text |
| Change classification | Change | Edit icon + text |
| Bulk classify | Classify as... | Opens combobox |
| Bulk sensitivity | Set sensitivity... | Opens dropdown |
| Clear selection | Clear selection | Text only |
| Accept all high-confidence | Accept all high-confidence | Toolbar button |
| Create policy | Create policy | Primary button |
| Save policy | Save and activate | Primary button |
| Test policy | Test policy | Secondary button |
| Generate report | Generate report | Primary button |
| Export report | Export | Secondary button with format options |

---

## Toast Messages

| Event | Message | Duration |
|---|---|---|
| Single classification applied | Classification updated to [tag name]. [Undo] | 5s |
| Bulk classification applied | [N] fields classified as [tag name]. [Undo] | 5s |
| AI suggestion accepted | Suggestion accepted for [field name]. | 3s |
| Bulk suggestions accepted | [N] suggestions accepted. | 3s |
| Classification removed | Classification removed from [field name]. | 5s |
| Save error | Failed to save classification. Please try again. | Persistent until dismissed |
| Partial bulk failure | [N] of [M] fields classified. [K] failed. [Retry] | Persistent |
| Policy activated | Policy "[name]" activated. [N] fields classified. | 5s |
| Report generated | Report ready. [Download] | 5s |

---

## Empty States

### No data sources connected
- **Heading:** Connect a data source to get started
- **Body:** Data classification requires at least one connected data source. Connect a database, data warehouse, or cloud storage service to begin discovering and classifying your data fields.
- **CTA:** Connect data source

### No unclassified fields
- **Heading:** All fields are classified
- **Body:** Every field across your connected data sources has been classified. Check back when new fields are detected or data sources are added.
- **CTA:** View all fields

### No review queue items
- **Heading:** Review queue is empty
- **Body:** All AI-suggested classifications have been reviewed. New suggestions will appear when data sources are scanned.
- **CTA:** View all fields

### No search results
- **Heading:** No matching fields
- **Body:** No fields match your current search and filter criteria. Try adjusting your search terms or removing some filters.
- **CTA:** Clear filters

### No policies configured
- **Heading:** No classification policies yet
- **Body:** Classification policies automate tagging based on field names, data patterns, and business rules. Create your first policy to reduce manual classification effort.
- **CTA:** Create policy

---

## Error Messages

| Error | Title | Body |
|---|---|---|
| Classification save failed | Unable to save classification | The classification change could not be saved. Check your connection and try again. |
| Scan failed | Data source scan failed | We could not complete the scan of [source name]. This may be due to a connection issue. Check your connection settings and retry. |
| Policy test failed | Policy test error | The policy could not be tested against your data. Please verify your match patterns and try again. |
| Report generation failed | Report generation failed | The report could not be generated. Please try again later or contact support if the issue persists. |
| Unauthorized | Access denied | You do not have permission to perform this action. Contact your administrator to request access. |

---

## Help Text and Tooltips

| Element | Tooltip/Help |
|---|---|
| Confidence percentage | AI confidence that this classification is correct, based on field name, data patterns, and policy rules. |
| Sensitivity level | Controls how the field is protected. Restricted fields receive the strongest security controls. |
| Review status | Tracks whether this classification has been reviewed by a human. |
| Auto-classify toggle | When enabled, fields matching this policy will be classified automatically without human review. |
| Confidence threshold | Minimum AI confidence required for auto-classification. Fields below this threshold are sent to the review queue. |

---

## Confirmation Dialogs

### Bulk Classification
- **Title:** Classify [N] fields?
- **Body:** You are about to apply "[tag name]" ([sensitivity]) to [N] fields. This action can be undone.
- **Primary button:** Apply classification
- **Secondary button:** Cancel

### Remove Classification
- **Title:** Remove classification?
- **Body:** Removing the classification from [field name] will mark it as unclassified. The field will appear in the unclassified queue.
- **Primary button:** Remove
- **Secondary button:** Cancel

### Accept All High-Confidence
- **Title:** Accept [N] AI suggestions?
- **Body:** You are about to accept [N] AI-suggested classifications with 90% or higher confidence. You can review and change individual classifications later.
- **Primary button:** Accept all
- **Secondary button:** Cancel

### Deactivate Policy
- **Title:** Deactivate policy?
- **Body:** Deactivating "[policy name]" will stop automatic classification for matching fields. Existing classifications will not be removed.
- **Primary button:** Deactivate
- **Secondary button:** Cancel

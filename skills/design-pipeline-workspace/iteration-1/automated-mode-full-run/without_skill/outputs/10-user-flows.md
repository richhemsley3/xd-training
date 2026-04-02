# User Flows: Data Classification Workflow

## Flow 1: First-Time Classification Setup (Security Admin)

```
[Start]
  |
  v
[Open Data Classification from side nav]
  |
  v
[See empty dashboard with onboarding prompt]
  "Connect your first data source to begin classifying data"
  |
  v
[Click "Connect data source" CTA]
  |
  v
[Redirect to Connections page (Administration)]
  |
  v
[Select data source type (e.g., Snowflake)]
  |
  v
[Enter connection credentials and test]
  |
  v
[Connection successful -- return to Data Classification]
  |
  v
[System begins initial scan]
  "Scanning 3 schemas, 47 tables, ~2,400 fields..."
  |
  v
[Scan complete -- dashboard shows initial results]
  - 0% classified (all fields are new)
  - AI suggestions generated for ~60% of fields
  - Review queue shows 1,440 suggestions
  |
  v
[Click "Review AI suggestions" CTA]
  |
  v
[Enter Classification Workspace > Review Queue tab]
  |
  v
[End -- handoff to classification flow]
```

---

## Flow 2: Daily Classification Session (Data Steward)

```
[Start]
  |
  v
[Open Data Classification from side nav]
  |
  v
[View dashboard]
  - Coverage: 78%
  - Review queue: 142 items
  - Unclassified: 1,193 items
  |
  v
[Click "Start reviewing" on Review Queue card]
  |
  v
[Workspace opens on Review Queue tab]
  [Sorted by confidence: lowest first]
  |
  +------> [Filter to assigned data source]
  |
  v
[Scan list of AI suggestions]
  |
  +---+--- Low confidence items (< 70%)
  |   |
  |   v
  |   [Click row to open detail panel]
  |   |
  |   v
  |   [Review sample data + AI reasoning]
  |   |
  |   +---> [AI is correct] --> [Click "Accept"] --> [Classification applied]
  |   |
  |   +---> [AI is wrong] --> [Click "Change"] --> [Select correct tag] --> [Applied]
  |   |
  |   +---> [Uncertain] --> [Add comment for team discussion] --> [Move to next]
  |   |
  |   v
  |   [Repeat for each low-confidence item]
  |
  +---+--- High confidence items (>= 90%)
      |
      v
      [Click "Accept all high-confidence" in toolbar]
      |
      v
      [Confirmation: "Accept 87 AI suggestions with 90%+ confidence?"]
      |
      v
      [Confirm] --> [All 87 items classified] --> [Toast: "87 classifications applied"]
      |
      v
      [Review remaining medium-confidence items individually]
      |
      v
      [Session complete -- coverage increased from 78% to 84%]
      |
      v
      [End]
```

---

## Flow 3: Bulk Classification of Similar Fields (Data Steward)

```
[Start]
  |
  v
[Workspace > Unclassified tab]
  |
  v
[Search for "email" in search bar]
  |
  v
[Results show 23 fields with "email" in the name across 6 sources]
  |
  v
[Select all 23 fields using "Select all matching" link]
  |
  v
[Bulk action bar appears: "23 fields selected"]
  |
  v
[Click "Classify as..."]
  |
  v
[Classification combobox opens]
  |
  v
[Type "email" to filter]
  |
  v
[Select "PII - Email Address"]
  |
  v
[Confirmation: "Apply PII - Email Address to 23 fields?"]
  |
  v
[Confirm]
  |
  v
[All 23 rows flash green briefly]
  [Toast: "23 fields classified as PII - Email Address" + Undo]
  |
  v
[Repeat for "phone", "ssn", "address" patterns]
  |
  v
[End]
```

---

## Flow 4: Review and Approve Classifications (Security Admin)

```
[Start]
  |
  v
[Open Data Classification dashboard]
  |
  v
[See "24 classifications pending approval" alert]
  |
  v
[Click to open approval queue]
  |
  v
[View list of recent classifications by stewards]
  [Shows: Steward name, Field, Previous classification, New classification, Date]
  |
  +---> [Select multiple straightforward changes]
  |     |
  |     v
  |     [Bulk approve] --> [Approved. Steward notified.]
  |
  +---> [Click into a questionable change]
        |
        v
        [View detail panel with diff: "Changed from 'Internal' to 'PII - Full Name'"]
        [See sample data, steward's comment, applicable policies]
        |
        +---> [Approve] --> [Classification confirmed]
        |
        +---> [Reject with comment] --> [Steward notified to re-review]
        |
        +---> [Override] --> [Admin applies different classification]
        |
        v
        [Continue through remaining items]
        |
        v
        [End]
```

---

## Flow 5: Create Classification Policy (Security Admin)

```
[Start]
  |
  v
[Data Classification > Policies tab]
  |
  v
[Click "Create policy"]
  |
  v
[Step 1: Define]
  - Name: "SSN Detection - US"
  - Description: "Classify fields containing US Social Security Numbers"
  - Regulation: CCPA, SOX (multi-select)
  |
  v
[Step 2: Match]
  - Field name pattern: /ssn|social.*sec|tax.*id/i
  - Data pattern: /^\d{3}-?\d{2}-?\d{4}$/
  - Data sources: All (or specific)
  |
  v
[Step 3: Classify]
  - Classification: "PII - Government ID"
  - Sensitivity: "Restricted"
  |
  v
[Step 4: Automate]
  - Auto-classify: ON
  - Confidence threshold: 85%
  - Action: Auto-apply (vs. suggest for review)
  |
  v
[Step 5: Review]
  - "This policy matches 47 fields across 5 data sources"
  - [Preview matching fields in table]
  - [Adjust patterns if needed]
  |
  v
[Save and activate]
  |
  v
[Policy active. 47 fields auto-classified.]
  [Toast: "Policy 'SSN Detection - US' activated. 47 fields classified."]
  |
  v
[End]
```

---

## Flow 6: Investigate Classification Drift (Security Admin)

```
[Start]
  |
  v
[Dashboard shows drift alert]
  "12 fields in Snowflake Production have changed since last scan"
  |
  v
[Click drift alert]
  |
  v
[Workspace filtered to recently modified fields in that source]
  |
  v
[Review changes]
  - 4 new fields detected (unclassified)
  - 3 fields with changed data types
  - 5 fields with new data patterns that conflict with current classification
  |
  v
[For new fields: classify using AI suggestions or manual review]
  |
  v
[For changed fields: review if current classification still applies]
  |
  +---> [Classification still valid] --> [Dismiss alert]
  |
  +---> [Classification needs update] --> [Reclassify]
  |
  v
[All drift items resolved]
  |
  v
[End]
```

---

## Flow 7: Generate Compliance Report (Security Admin)

```
[Start]
  |
  v
[Data Classification > Reports tab]
  |
  v
[Select report template: "GDPR Data Classification Report"]
  |
  v
[Configure scope]
  - Data sources: All / specific
  - Date range: Last 30 days
  - Include: Coverage metrics, Classification breakdown, Steward activity
  |
  v
[Click "Generate report"]
  |
  v
[Report generated with sections:]
  - Executive summary (coverage %, trend)
  - Classification by sensitivity level (table + chart)
  - Coverage by data source (table)
  - Unclassified field inventory
  - Steward activity log
  - Policy compliance status
  |
  v
[Export as PDF or CSV]
  |
  v
[End]
```

---

## Decision Tree: Which Tab Should the User Start On?

```
Is this the user's first visit?
  |
  +-- YES --> Dashboard (onboarding flow)
  |
  +-- NO
       |
       Are there items in the review queue?
         |
         +-- YES --> Review Queue tab
         |
         +-- NO
              |
              Are there unclassified fields?
                |
                +-- YES --> Unclassified tab
                |
                +-- NO --> All Fields tab (maintenance mode)
```

---

## Error Recovery Flows

### Classification Save Fails
```
[User applies classification]
  |
  v
[Optimistic update shows new tag]
  |
  v
[Server returns error]
  |
  v
[Revert to previous classification]
[Show inline error on the row: "Failed to save. Retry?"]
[Toast: "Classification failed to save. Please try again."]
  |
  v
[User clicks Retry] --> [Attempt save again]
  |
  v
[Success] --> [Toast: "Classification saved."]
```

### Bulk Operation Partial Failure
```
[User bulk-applies classification to 23 fields]
  |
  v
[20 succeed, 3 fail]
  |
  v
[Toast: "20 of 23 fields classified. 3 failed."]
[Failed rows highlighted with error state]
[Bulk action bar shows: "Retry 3 failed"]
  |
  v
[User clicks Retry] --> [Attempt 3 again]
```

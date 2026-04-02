# Journey Map: Data Classification Workflow

## Journey 1: Data Steward -- Classifying Fields Across Data Sources

### Stage 1: Orient
**Action:** Dana opens the Data Classification section from the side navigation. She sees the classification dashboard showing coverage across all connected data sources.

**Thinking:** "What needs my attention today? Where should I focus?"

**Touchpoints:** Side navigation > Data Classification > Dashboard

**Emotions:** Neutral to slightly anxious (large backlog)

**Opportunities:**
- Show a prioritized "needs review" count prominently
- Surface data sources with the lowest classification coverage
- Show recent changes or new fields detected since last session

---

### Stage 2: Triage
**Action:** Dana clicks into the review queue, which shows fields sorted by AI confidence (lowest first). She filters to a specific data source she is responsible for. She scans the list to understand the scope.

**Thinking:** "How many fields need my attention? Are the AI suggestions reasonable?"

**Touchpoints:** Review Queue > Filters > Field list

**Emotions:** Relieved (system did most of the work) or frustrated (many low-confidence items)

**Opportunities:**
- Show confidence score visually (color-coded bar or badge)
- Enable grouping by suggested classification to spot patterns
- Show field sample values inline to aid decision-making

---

### Stage 3: Classify (Bulk)
**Action:** Dana selects multiple fields that share the same sensitivity type (e.g., all email columns). She applies "PII - Contact Information" to all selected fields at once. She repeats for other obvious groupings.

**Thinking:** "These are clearly all email addresses. I can tag them all at once."

**Touchpoints:** Field list > Multi-select > Bulk tag action

**Emotions:** Satisfied (efficient), confident (clear-cut cases)

**Opportunities:**
- Provide keyboard shortcuts for common operations
- Show "similar fields" suggestions when one field is classified
- Auto-suggest groupings based on field name patterns

---

### Stage 4: Classify (Individual Review)
**Action:** Dana encounters fields where the AI suggestion is uncertain or wrong. She opens the field detail panel to see sample data, the AI's reasoning, and the applicable policy. She makes a classification decision.

**Thinking:** "This field name is ambiguous. Let me look at the actual data to decide."

**Touchpoints:** Field detail panel > Sample data > Policy reference > Classification selector

**Emotions:** Focused, occasionally uncertain

**Opportunities:**
- Show sample data values prominently (with masking for truly sensitive data)
- Display the AI's reasoning (which patterns triggered the suggestion)
- Surface the relevant organizational policy inline
- Allow adding a note explaining the classification rationale

---

### Stage 5: Validate
**Action:** Dana checks her session progress -- fields classified, remaining, coverage percentage. She reviews any flagged conflicts (fields classified differently across sources).

**Thinking:** "Am I done? Did I miss anything?"

**Touchpoints:** Progress bar > Coverage metrics > Conflict alerts

**Emotions:** Accomplished or slightly anxious (remaining items)

**Opportunities:**
- Show session summary with before/after coverage
- Highlight any classification conflicts across sources
- Provide a "mark session complete" action that logs progress

---

### Stage 6: Hand Off
**Action:** Dana submits her classifications for review (if approval workflow is enabled) or they are applied immediately. She logs out or switches to another task.

**Thinking:** "My work is saved. The security team can see what I've done."

**Touchpoints:** Submit/Save > Activity log > Dashboard update

**Emotions:** Accomplished, ready to move on

**Opportunities:**
- Send a summary notification to the security admin
- Update the dashboard in real time
- Show a confirmation with session statistics

---

## Journey 2: Security Admin -- Configuring and Monitoring Classification

### Stage 1: Assess Coverage
**Action:** Marcus opens the Data Classification dashboard. He reviews the coverage heatmap across all data sources. He identifies sources with low coverage or recent drift.

**Touchpoints:** Dashboard > Coverage heatmap > Drift alerts

**Opportunities:**
- Aggregate coverage by source, department, or regulation
- Show trend lines (coverage over time)
- Alert on newly detected unclassified fields

---

### Stage 2: Configure Policies
**Action:** Marcus creates or updates a classification policy (e.g., "All fields matching SSN patterns must be classified as PII - Government ID"). He sets the confidence threshold for auto-classification.

**Touchpoints:** Policy editor > Pattern builder > Threshold slider > Test against sample data

**Opportunities:**
- Provide a policy template library
- Show live preview of how many fields the policy would match
- Enable regex and pattern testing against real data

---

### Stage 3: Assign Work
**Action:** Marcus assigns unclassified data sources to specific stewards based on their domain expertise. He sets review deadlines.

**Touchpoints:** Assignment panel > Steward selector > Deadline picker

**Opportunities:**
- Show steward workload and capacity
- Suggest assignments based on past classification history
- Enable bulk assignment by data source or department

---

### Stage 4: Review and Approve
**Action:** Marcus reviews classifications submitted by stewards. He approves, rejects with comments, or overrides specific decisions.

**Touchpoints:** Approval queue > Classification diff view > Comment/approve actions

**Opportunities:**
- Show what changed (diff view) rather than all classifications
- Enable batch approval for high-confidence items
- Track approval history for audit trail

---

### Stage 5: Report
**Action:** Marcus generates an audit report showing classification coverage, policy compliance, and steward activity.

**Touchpoints:** Reports section > Report builder > Export

**Opportunities:**
- Pre-built report templates for common regulations
- Scheduled report delivery
- Interactive dashboard with drill-down capability

---

## Emotional Journey Summary

```
                Orient    Triage    Classify(Bulk)  Classify(Detail)  Validate    Hand Off
Data Steward:   Anxious   Relieved  Satisfied       Focused           Accomplished Done
Security Admin: Concerned Informed  Confident       Analytical        Satisfied    Accountable
```

## Critical Moments of Truth

1. **First impression of the review queue:** If the AI suggestions are good, the steward trusts the system. If they are poor, the steward reverts to manual classification.

2. **Bulk classification speed:** If multi-select and batch tagging is fast and reliable, the steward's efficiency improves dramatically.

3. **Coverage dashboard accuracy:** If the security admin trusts the coverage numbers, they can make informed decisions about where to allocate resources.

4. **Policy-to-classification linkage:** If stewards can see why a classification is required (policy context), they make better decisions and feel more confident.

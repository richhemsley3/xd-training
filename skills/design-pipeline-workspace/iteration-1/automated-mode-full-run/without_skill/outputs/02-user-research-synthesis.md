# User Research Synthesis: Data Classification Workflow

## Target Personas

### Persona 1: Dana -- Data Steward

**Role:** Data Steward, mid-level, 3-7 years experience
**Organization:** Enterprise (1,000-10,000 employees), data-intensive industry (financial services, healthcare, retail)

**Goals:**
- Ensure all sensitive data fields are properly classified across the organization's data estate
- Maintain classification accuracy as data sources change
- Reduce time spent on manual field-by-field review
- Demonstrate classification coverage to compliance teams

**Frustrations:**
- Spends 60-70% of time on repetitive manual tagging
- Inconsistency between her classifications and those made by colleagues
- No visibility into what has changed since the last review cycle
- AI suggestions exist but are buried -- she often reclassifies things the system already identified
- Switching between data sources loses her context and flow

**Technical comfort:** Moderate. Comfortable with data catalogs and spreadsheets. Does not write code or regex.

**Workflow context:** Works in 2-4 hour classification sessions. Typically handles 50-200 fields per session. Reviews one data source at a time today but would prefer cross-source views.

---

### Persona 2: Marcus -- Security Admin

**Role:** Security Administrator / Data Security Lead, senior, 8-15 years experience
**Organization:** Enterprise, regulated industry

**Goals:**
- Enforce classification policies consistently across all data sources
- Identify unclassified or misclassified sensitive data quickly
- Produce audit-ready reports showing classification coverage and policy compliance
- Configure automated classification rules that reduce manual effort for stewards

**Frustrations:**
- Cannot see a unified view of classification coverage across all sources
- Policy enforcement is disconnected from the classification workflow
- Stewards make inconsistent decisions because policies are documented separately
- No way to prioritize which unclassified fields are highest risk
- Report generation requires exporting data and building spreadsheets manually

**Technical comfort:** High. Comfortable with regex, policy configuration, API integrations.

**Workflow context:** Sets up classification policies and automation rules. Reviews classification dashboards weekly. Audits steward work monthly. Manages 10-50 data sources.

---

## Synthesized User Needs

### Need 1: Efficient Bulk Classification
Users need to classify many fields quickly without opening individual detail views for each one. The current field-by-field model is the primary bottleneck.

**Evidence:** Manual classification is cited as the #1 pain point across industry research. Data stewards report spending the majority of their time on repetitive tagging tasks.

**Design implication:** Provide inline editing, multi-select, and batch-apply operations for classification tags.

---

### Need 2: AI-Assisted Triage
Users need the system to pre-classify fields using AI/ML so they can focus on reviewing and correcting rather than classifying from scratch.

**Evidence:** All three competitors invest heavily in ML classification. Industry research shows rule-based approaches fail at scale. Users want to shift from "classify everything" to "review what the system found."

**Design implication:** Show AI-suggested classifications with confidence scores. Provide a review queue sorted by confidence (lowest first). Allow bulk-accept of high-confidence suggestions.

---

### Need 3: Cross-Source Visibility
Users need to see and manage classifications across multiple data sources without losing context.

**Evidence:** Competitors require source-by-source navigation. Data stewards report losing context when switching between sources. Security admins need unified coverage dashboards.

**Design implication:** Provide a unified classification table that spans data sources. Enable filtering and grouping by source, sensitivity level, and classification status.

---

### Need 4: Policy-Linked Classification
Users need classification decisions to be connected to organizational policies so that the "why" behind each classification is clear.

**Evidence:** Security admins report that policies are documented separately from classification workflows. Stewards make inconsistent decisions because policy context is not available in the classification UI.

**Design implication:** Surface applicable policies inline during classification. Show policy requirements alongside field details. Link classifications to specific regulatory or organizational policies.

---

### Need 5: Progress and Coverage Tracking
Users need real-time visibility into classification progress -- how much is done, what remains, and where accuracy is low.

**Evidence:** All competitors provide only basic metrics. Data stewards report finishing sessions without knowing if they covered everything. Security admins build manual reports to track coverage.

**Design implication:** Provide a classification dashboard with coverage metrics, completion tracking, and drift alerts. Show progress inline during classification sessions.

---

### Need 6: Collaborative Review
Users need to assign, review, comment on, and approve classification decisions as a team activity.

**Evidence:** No competitor offers strong collaboration features for classification. Organizations report inconsistency when multiple stewards classify independently.

**Design implication:** Support classification assignment to specific stewards, review/approval workflows, and inline comments on classification decisions.

---

## Jobs to Be Done

| Job | Primary User | Frequency |
|---|---|---|
| Classify untagged fields across my data sources efficiently | Data Steward | 2-5x per week |
| Review and correct AI-suggested classifications | Data Steward | Daily |
| Apply a classification tag to multiple similar fields at once | Data Steward | Multiple times per session |
| See which data sources have incomplete classification coverage | Security Admin | Weekly |
| Configure classification policies and automation rules | Security Admin | Monthly |
| Generate audit reports showing classification status | Security Admin | Monthly / on-demand |
| Resolve disagreements or ambiguities in classification decisions | Both | As needed |
| Track classification drift when data sources change | Security Admin | Weekly |

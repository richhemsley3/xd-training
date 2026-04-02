# User Personas & Jobs-to-be-Done
## Data Lineage Visualization Feature

**Date:** 2026-03-20

---

## Primary Personas

### 1. Data Steward -- "Sarah"

**Role:** Data Governance Lead
**Organization:** Enterprise financial services (5,000+ employees)
**Technical skill:** Moderate -- understands data concepts but does not write SQL
**Tools today:** Collibra, Excel-based data dictionaries, email chains

**Goals:**
- Ensure compliance with GDPR, DORA, and internal data governance policies
- Understand where sensitive data lives and how it flows between systems
- Respond to audit requests quickly with documented data provenance

**Frustrations:**
- Current lineage tools are too technical; she relies on engineers to interpret graphs
- Audit preparation takes weeks because lineage documentation is manual and outdated
- Cannot easily see which data flows involve PII or are subject to protection policies

**Jobs-to-be-Done:**
| Job | Context | Outcome |
|-----|---------|---------|
| Trace data origin for audit | Regulator asks "where does this customer data come from?" | Produce a clear, shareable lineage report within minutes |
| Assess protection coverage | Quarterly governance review | See which data flows lack protection policies |
| Validate compliance posture | New regulation takes effect | Map all affected data flows to regulatory requirements |

---

### 2. Data Engineer -- "Marcus"

**Role:** Senior Data Engineer
**Organization:** SaaS company with complex multi-cloud data platform
**Technical skill:** Expert -- writes dbt, manages Airflow DAGs, builds Snowflake pipelines
**Tools today:** dbt docs, Airflow UI, custom scripts, Monte Carlo

**Goals:**
- Debug pipeline failures by tracing data from source to destination
- Assess the impact of schema changes before deploying
- Understand which downstream consumers are affected by changes

**Frustrations:**
- Lineage information is fragmented across multiple tools
- Column-level lineage is often missing or inaccurate
- Graph visualizations choke on large pipelines (500+ nodes)
- No connection between lineage and data security/access policies

**Jobs-to-be-Done:**
| Job | Context | Outcome |
|-----|---------|---------|
| Debug data quality issue | Alert fires for bad data in a dashboard | Trace upstream to find where data was corrupted |
| Assess schema change impact | Before deploying a new dbt model | See all downstream tables, dashboards, and consumers affected |
| Understand data flow | Onboarding to a new project | Explore lineage to learn how data moves through the system |

---

### 3. Compliance Officer -- "Diana"

**Role:** Chief Data Privacy Officer / Compliance Director
**Organization:** Healthcare or financial enterprise subject to heavy regulation
**Technical skill:** Low -- needs plain-language, visual summaries
**Tools today:** Manual spreadsheets, legal review tools, periodic reports from data team

**Goals:**
- Demonstrate to regulators that data handling meets legal requirements
- Ensure PII and sensitive data are properly classified and protected throughout their lifecycle
- Get real-time visibility into data protection status without depending on the data team

**Frustrations:**
- Has no self-service access to lineage information
- Depends entirely on data engineers for compliance reports
- Cannot connect protection policies to actual data flows
- Audit preparation is a fire drill every time

**Jobs-to-be-Done:**
| Job | Context | Outcome |
|-----|---------|---------|
| Generate compliance report | Regulatory audit | One-click report showing data flows with protection status |
| Monitor sensitive data flows | Ongoing compliance | Dashboard showing all PII flows and their protection level |
| Respond to data subject request | GDPR right-to-erasure request | Trace all locations where a person's data exists |

---

### 4. Analytics Director -- "Raj"

**Role:** Director of Analytics / Head of BI
**Organization:** Retail or e-commerce enterprise
**Technical skill:** Moderate -- understands SQL, uses BI tools daily
**Tools today:** Looker/Tableau, Snowflake, Slack

**Goals:**
- Trust the data in executive dashboards
- Understand the provenance of KPI metrics
- Quickly determine if a data issue affects critical reports

**Frustrations:**
- When numbers look wrong, it takes days to find the root cause
- Does not know which upstream pipelines feed into key dashboards
- Cannot see if data quality issues are affecting metrics in real time

**Jobs-to-be-Done:**
| Job | Context | Outcome |
|-----|---------|---------|
| Verify metric trustworthiness | Executive questions a KPI | Trace the metric back to its source and transformations |
| Assess incident impact | Data quality alert fires | Determine which dashboards and reports are affected |
| Plan data migration | Moving BI tool or warehouse | Understand all dependencies on current data assets |

---

## Persona Priority Matrix

| Persona | Frequency of Use | Business Impact | Design Priority |
|---------|-----------------|----------------|----------------|
| Data Steward (Sarah) | Daily/Weekly | High -- drives governance adoption | **P0** -- Primary design target |
| Data Engineer (Marcus) | Daily | High -- power user, drives technical credibility | **P0** -- Must satisfy core workflows |
| Compliance Officer (Diana) | Monthly/Quarterly | Very High -- regulatory risk | **P1** -- Key differentiator for our product |
| Analytics Director (Raj) | Weekly | Medium -- improves trust in data | **P2** -- Important but secondary |

---

## Key Design Implications

1. **Dual-mode interface required:** Technical view (column-level, transformations) for engineers AND business view (system-level, plain language) for stewards and compliance
2. **Search-first, not graph-first:** All personas need to FIND specific assets, not browse entire graphs
3. **Security/protection overlay is unique:** Every persona benefits from seeing protection status alongside lineage -- this is our differentiator
4. **Export and sharing:** Compliance officers need to generate reports; engineers need to share context in Slack/Jira
5. **Progressive disclosure:** Start with high-level system flows; let users drill into table-level and column-level detail on demand

---

> **GUIDED MODE PAUSE POINT:** In a guided process, we would validate these personas with actual user interviews before proceeding to information architecture. Key questions to validate: (1) Do data stewards actually use lineage tools today? (2) What is the typical audit workflow? (3) How do engineers currently debug data quality issues?

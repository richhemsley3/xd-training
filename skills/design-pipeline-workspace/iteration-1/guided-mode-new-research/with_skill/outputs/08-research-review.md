# Research Review: Designs vs. Original Research

## Evaluation of Data Lineage Visualization Prototype Against Market Research Findings

**Date:** 2026-03-20

---

## Overall Assessment

The prototype strongly addresses the primary market opportunity identified in the research: **security-aware data lineage** as a differentiated position. The design successfully integrates security classification and protection status directly into the lineage graph -- a capability no competitor offers today. The three-persona approach (governance, engineering, security) is well-served by the tab structure (Explorer, Impact analysis, Incidents).

**Score: 8.5/10** -- Strong alignment with research; a few gaps remain.

---

## Research Findings vs. Design Coverage

### Key Pain Points Addressed

| Pain Point (from Research) | Addressed in Design? | How |
|---------------------------|---------------------|-----|
| No visibility into sensitive data flows | YES | Core lineage graph with classification badges (PII, PHI) on every node |
| Security and governance in separate tools | YES | Security tab in node detail panel; protection status dots on graph nodes |
| Audit preparation takes weeks | PARTIAL | Compliance tab in IA; export button in toolbar; would need full report generation |
| Cannot assess data exposure without manual investigation | YES | Protection status indicators (green/yellow/red dots) visible at a glance |
| Schema changes break downstream reports | YES | Impact analysis tab with upstream/downstream analysis flow |
| Manual investigation during breaches takes days | PARTIAL | Incidents tab defined in IA; blast radius view in flow spec; not fully prototyped |
| No unified view of lineage + data sensitivity | YES | Primary differentiator -- every node shows both lineage position AND security status |
| Hard to navigate large graphs | YES | Minimap, search-first toolbar, zoom controls, filter chips |

### Persona Goals Covered

| Persona | Primary Goal | Addressed? | Evidence |
|---------|-------------|------------|---------|
| Diana (Governance) | Trace sensitive data flows, prove compliance | YES | Explorer tab, classification badges, security panel tab, export |
| Marcus (Engineering) | Impact analysis before schema changes | YES | Impact analysis tab, column-level detail in side panel |
| Serena (CISO) | Breach investigation, data exposure risk | PARTIAL | Incidents tab in IA, but not fully designed in prototype |

### Market Opportunities Addressed

| Opportunity (from Research) | Addressed? | Notes |
|---------------------------|------------|-------|
| Security-aware lineage (primary differentiator) | YES | Core design concept -- no competitor does this |
| Consumer-grade UX | YES | Clean SDS-based design; search-first; progressive disclosure |
| Column-level lineage | YES | Column list in side panel with classification per column |
| Fast time-to-value | PARTIAL | Embedded in existing product shell; would need connector setup flow |
| Multi-persona design | YES | Three tabs serve three personas; shared graph with role-appropriate entry points |
| Scale handling | YES | Minimap, search, filter chips, progressive loading in IA spec |

---

## Gaps and Recommendations

### Gap 1: Incident Investigation Not Fully Prototyped
The research identified breach investigation as a critical CISO use case. The IA defines the flow (blast radius, affected assets, timeline), but the prototype only shows the Explorer tab.

**Recommendation:** Design a dedicated "Incidents" tab prototype showing the blast radius view with affected-asset highlighting and one-click investigation from a SIEM deep-link.

### Gap 2: Compliance Reporting Not Visualized
Diana's primary need is proving compliance to auditors. The export button exists, but the report generation experience is not designed.

**Recommendation:** Design the compliance report output -- a printable/PDF view showing data lineage + protection status for a selected scope, suitable for audit evidence.

### Gap 3: Empty State / First-Run Experience
The research emphasizes fast time-to-value. The IA defines an empty state flow, but the prototype starts with data already populated.

**Recommendation:** Design the empty state with guided setup: "Connect your first data source" with a progress indicator showing scan status and asset discovery.

### Gap 4: Real-Time Scan Status
The journey map identifies the "Initial lineage scan" step as a high-emotion moment (hopeful, then either encouraged or frustrated). The prototype shows a static "Last scan: 2 hours ago" in the status bar.

**Recommendation:** Design the active scan experience: progress bar, asset count incrementing, nodes appearing as they're discovered -- to make the "aha moment" of first lineage visible and exciting.

### Gap 5: Executive Dashboard
Serena needs to present data security posture to leadership. The research recommends executive dashboards with risk scoring.

**Recommendation:** Design a dashboard widget or standalone executive view showing aggregate lineage health: % of sensitive data with full protection, unprotected flow count, and coverage trends over time.

---

## What the Design Does Well (Research Alignment)

1. **Differentiator is front and center** -- Classification badges and protection dots are the most visually prominent elements on graph nodes, reinforcing the security-aware positioning.

2. **Search-first matches market best practice** -- The prominent search in toolbar mirrors Atlan's successful pattern identified in competitive analysis.

3. **Progressive disclosure handles scale** -- System-level graph > table detail > column detail matches the multi-level drill-down pattern identified in UX pattern analysis.

4. **SDS consistency builds trust** -- Using the established design system ensures the lineage feature feels native to the product, reducing adoption friction for existing customers.

5. **Side panel pattern is industry-standard** -- Click-to-detail with a side panel matches the dominant interaction pattern across Atlan, Collibra, and Google Dataplex.

---

## Recommended Next Iterations

1. **Iteration 2:** Incident investigation (blast radius) prototype
2. **Iteration 3:** Compliance report generation + export flow
3. **Iteration 4:** Empty state + first-run / onboarding experience
4. **Iteration 5:** Executive dashboard with aggregate risk scoring
5. **Iteration 6:** User research validation with 6-8 participants across persona segments

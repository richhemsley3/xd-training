# Design Tokens Mapping: Data Classification Workflow

## Purpose
This document maps every visual property in the data classification feature to Software DS tokens, ensuring consistency and maintainability.

---

## Background Tokens

| Usage | Token | Resolved Value |
|---|---|---|
| Page background | `--sds-bg-page` | #FFFFFF |
| Sidebar background | `--sds-nav-sidebar-bg` | #FAF8F5 |
| Card background | `--sds-bg-card` | #FFFFFF |
| Table header background | `--sds-bg-subtle` | #F4F1EB |
| Sample data block background | `--sds-bg-subtle` | #F4F1EB |
| Bulk action bar background | `--sds-interactive-primary` | #013D5B |
| Row hover background | `--sds-bg-subtle` | #F4F1EB |
| Active nav item background | `--sds-nav-item-active-bg` | #D9EBED |

---

## Text Tokens

| Usage | Token | Resolved Value |
|---|---|---|
| Page titles, primary text | `--sds-text-primary` | #1C1A17 |
| Body copy, descriptions | `--sds-text-secondary` | #54514D |
| Captions, metadata, placeholders | `--sds-text-tertiary` | #6B6760 |
| Disabled text | `--sds-text-disabled` | #B0ABA2 |
| Text on dark backgrounds (bulk bar) | `--sds-text-on-primary` | #FFFFFF |
| Links, breadcrumbs | `--sds-text-link` | #013D5B |

---

## Border Tokens

| Usage | Token | Resolved Value |
|---|---|---|
| Card borders, dividers | `--sds-border-default` | #E0DCD3 |
| Table row separators | `--sds-border-subtle` | #EBE6DD |
| Input borders, strong dividers | `--sds-border-strong` | #D0CBC3 |
| Focus rings | `--sds-border-focus` | #013D5B |

---

## Interactive Tokens

| Usage | Token | Resolved Value |
|---|---|---|
| Primary buttons, active states | `--sds-interactive-primary` | #013D5B |
| Primary hover | `--sds-interactive-primary-hover` | #05314D |
| Primary active/pressed | `--sds-interactive-primary-active` | #032740 |
| Subtle primary backgrounds (badges, chips) | `--sds-interactive-primary-subtle` | #D9EBED |
| Secondary button background | `--sds-interactive-secondary` | #FFFFFF |
| Secondary button border | `--sds-interactive-secondary-border` | #302D28 |

---

## Status Tokens (Classification Badges)

### PII / Info Category
| Property | Token | Value |
|---|---|---|
| Background | `--sds-status-info-bg` | #EBF4F5 |
| Text | `--sds-status-info-text` | #0C4A69 |

### Financial / Purple Category
| Property | Token | Value |
|---|---|---|
| Background | `--sds-status-purple-bg` | #F7EEFF |
| Text | `--sds-status-purple-text` | #805AA1 |

### Health / Error Category
| Property | Token | Value |
|---|---|---|
| Background | `--sds-status-error-bg` | #FFEEEB |
| Text | `--sds-status-error-text` | #BF5547 |

### Auth / Warning Category
| Property | Token | Value |
|---|---|---|
| Background | `--sds-status-warning-bg` | #FCF9D9 |
| Text | `--sds-status-warning-text` | #8A7515 |

### Business / Neutral Category
| Property | Token | Value |
|---|---|---|
| Background | `--sds-status-neutral-bg` | #EBE6DD |
| Text | `--sds-status-neutral-text` | #54514D |

### Technical / Subtle Category
| Property | Token | Value |
|---|---|---|
| Background | `--sds-bg-subtle` | #F4F1EB |
| Text | `--sds-text-tertiary` | #6B6760 |

---

## Sensitivity Level Tokens

| Level | Background Token | Text Token |
|---|---|---|
| Restricted | `--sds-status-error-bg` | `--sds-status-error-text` |
| Confidential | `--sds-status-warning-bg` | `--sds-status-warning-text` |
| Internal | `--sds-status-info-bg` | `--sds-status-info-text` |
| Public | `--sds-status-success-bg` | `--sds-status-success-text` |

---

## Confidence Score Tokens

| Range | Fill Color Token | Text Token |
|---|---|---|
| 90-100% (High) | `--sds-status-success-strong` | `--sds-status-success-text` |
| 70-89% (Medium) | `--sds-status-warning-strong` | `--sds-status-warning-text` |
| Below 70% (Low) | `--sds-status-error-strong` | `--sds-status-error-text` |
| Track (unfilled) | `--sds-bg-subtle` | -- |

---

## Navigation Tokens

| Usage | Token | Value |
|---|---|---|
| Side nav "Data classification" active bg | `--sds-nav-item-active-bg` | #D9EBED |
| Side nav "Data classification" active text | `--sds-nav-item-active-text` | #013D5B |
| Side nav default item text | `--sds-nav-item-text` | #54514D |
| Side nav section header | `--sds-nav-section-header` | #6B6760 |
| Tab active text | `--sds-nav-item-active-text` | #013D5B |
| Tab active border | `--sds-interactive-primary` | #013D5B |
| Tab inactive text | `--sds-text-tertiary` | #6B6760 |

---

## Data Visualization Tokens (Dashboard Charts)

| Series | Token | Value |
|---|---|---|
| Primary (coverage) | `--sds-interactive-primary` | #013D5B |
| Secondary (classified) | `--sds-status-success-strong` | #7A9A01 |
| Tertiary (needs review) | `--sds-status-warning-strong` | #EBCE2D |
| Quaternary (unclassified) | `--sds-status-error-strong` | #CF6253 |

---

## Spacing and Layout Constants

These are not tokenized in Software DS but are used consistently:

| Property | Value | Context |
|---|---|---|
| Page content padding | 24px | Content area inside app shell |
| Card padding | 20px | Summary cards |
| Card border-radius | 8px | All cards |
| Table cell padding | 12px 16px | Standard rows |
| Table header padding | 10px 16px | Header cells |
| Badge padding | 2px 8px | Classification/sensitivity badges |
| Badge border-radius | 4px | All badges |
| Filter chip padding | 4px 8px 4px 10px | Active filter chips |
| Filter chip border-radius | 16px | Pill shape |
| Side panel width | 400px | Detail panel |
| Sidebar width (expanded) | 220px | Per Software DS |
| Sidebar width (collapsed) | 56px | Per Software DS |
| Header height | 56px | Per Software DS |
| Input height | 36px | Filter inputs |
| Gap between cards | 16px | Summary card row |
| Gap between filter chips | 8px | Active filter row |

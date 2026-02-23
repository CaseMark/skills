---
name: warranty-timeline
description: Generates a chronological timeline of warranty requests, claims, and customer complaints for a potentially defective product. Analyzes patterns, establishes manufacturer notice dates, and supports causation arguments in commercial litigation. Use when building warranty claim timelines, product defect chronologies, complaint pattern analysis, discovery summaries, expert report exhibits, or trial timeline exhibits.
tags:
  - analysis
  - litigation
  - summary
---

# Warranty Request Timeline

Produces a defensible chronological timeline of warranty requests and complaints for use in product defect litigation, regulatory proceedings, or internal investigations.

## Prerequisites

1. **Product identification** — model number, SKU, or product name to scope the search
2. **Source documents** — warranty databases, customer complaints, service records, RMA logs, internal emails, quality reports
3. **Date range** — target period for the timeline
4. **Protective order / privacy constraints** — any redaction or anonymization requirements for customer PII

## Process

### Phase 1: Data Collection

Search all uploaded documents using broad terms:

| Primary Terms | Secondary Terms |
|---|---|
| warranty claim, warranty request | return authorization, RMA |
| product defect, malfunction | service request, repair request |
| customer complaint, product failure | engineering investigation, quality hold |
| [product name/model/SKU] | batch number, lot number |

For each record, extract:

| Field | Notes |
|---|---|
| Date/time of request | Exact date; temporal proximity matters for notice |
| Customer ID | Name, account, location (redact per protective order) |
| Product info | Model, serial, mfg date, batch/lot, purchase date |
| Defect description | Preserve customer's own language verbatim where possible |
| Company response | Repair / replace / refund / deny + rationale |
| Resolution date | Calculate days-to-resolution |
| Handling personnel | Name and role (potential fact witnesses) |
| Source attribution | Document title, repository location, custodian, creation date |

### Phase 2: Chronological Organization & Pattern Analysis

Organize entries chronologically (earliest → most recent). For high-volume products, group by week/month while preserving drill-down capability.

**Identify and flag:**

- [ ] **Earliest complaint** — establishes initial notice date (critical for SOL, punitive damages exposure, regulatory reporting)
- [ ] **Temporal clusters / spikes** — may indicate bad production batches or design-phase defects
- [ ] **Geographic concentrations** — distribution, storage, or environmental factors
- [ ] **Defect evolution** — progressive failure modes or emerging secondary defects
- [ ] **Internal acknowledgments** — engineering emails, quality holds, supplier communications, design change discussions
- [ ] **Response pattern changes** — shifts in denial rates, response times, escalation frequency, or legalistic language changes
- [ ] **Inconsistencies** — gaps between internal knowledge and public statements (relevant to fraud/misrepresentation)

**Calculate statistics:**

- Total warranty requests + unresolved count
- Requests per 1,000 units sold (if sales data available)
- Repair vs. replace vs. deny rates
- Average/median time to resolution
- Median time from purchase to first complaint (short = latent defect argument)

### Phase 3: Deliverable Structure

#### A. Master Spreadsheet

| Column | Format |
|---|---|
| Request Date | YYYY-MM-DD |
| Customer Name/ID | Redacted per applicable orders |
| Customer Location | City, State minimum |
| Product Model | — |
| Serial Number | — |
| Mfg/Batch Date | If available |
| Defect Category | Electrical / Mechanical / Cosmetic / Safety / Performance |
| Severity | Minor / Moderate / Severe / Safety-Critical |
| Defect Description | Concise, from source language |
| Company Response | Repair / Replace / Refund / Deny / Pending |
| Resolution Date | YYYY-MM-DD |
| Days to Resolution | Calculated |
| Handling Personnel | Name + role |
| Source Reference | Document ID with link |

#### B. Executive Summary

Present at-a-glance metrics:
- Total requests, date range, unresolved count
- Top defect categories with counts/percentages
- Most affected regions
- Notable spikes with dates
- Key statistical measures

#### C. Narrative Overview (2–5 paragraphs)

Synthesize the chronological progression highlighting:
- When defects first appeared
- When patterns became statistically significant
- When internal investigations began or should have begun
- When regulatory reporting obligations triggered
- When corrective action was taken or not taken

Present facts neutrally — no legal conclusions. Frame for adaptation into mediation statements, SJ briefing, or trial presentations.

#### D. Supporting Materials

- Source document log with full attribution
- Methodology statement (search terms, repositories, date ranges, limitations)
- Visualizations if data supports (complaint volume over time, geographic heat maps)

## Guidelines

- **Preserve verbatim language** — customer descriptions carry evidentiary weight as contemporaneous non-expert statements
- **Note all gaps explicitly** — missing periods due to retention policies, system migrations, or business unit changes must be disclosed, not papered over
- **Do not interpret ambiguous complaints** — present as-written; let counsel characterize
- **Maintain factual objectivity** — this is a factual compilation, not attorney argument; separate factual data from analytical observations to preserve work product protection
- **Dual format output** — provide spreadsheets in manipulable format (Excel) and fixed format (PDF) for discovery production
- **Privacy compliance** — redact customer PII per protective orders and applicable consumer protection statutes
- **Authentication readiness** — source attribution must be specific enough for independent verification by opposing counsel or the court
- **Flag regulatory triggers** — note when complaint volume or severity may trigger reporting obligations under CPSA or state consumer protection statutes [VERIFY]

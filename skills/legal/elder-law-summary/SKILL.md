---
name: elder-law-summary
description: Generates structured elder law summaries covering estate planning, elder abuse, healthcare rights, Medicaid eligibility, and guardianship. Analyzes uploaded documents to identify risks, protection gaps, and prioritized actions. Outputs are structured for both legal professionals and families. Use when summarizing elderly client matters, elder care legal overviews, long-term care planning reviews, or guardianship assessments.
tags:
  - analysis
  - summarization
  - summary
  - transactional
---

# Elder Law Summary

Produces a structured legal overview for elderly client matters, covering all relevant domains with jurisdiction-specific detail and a prioritized action plan.

## Prerequisites

1. **Client profile** — age, state of residence, capacity status, living situation
2. **Existing legal documents** — wills, trusts, POAs, advance directives, guardianship orders
3. **Financial information** — asset inventory, income sources, benefit status (Medicare/Medicaid/SSI)
4. **Medical context** — relevant conditions, care needs, current care arrangements
5. **Concerns or triggers** — suspected abuse, upcoming Medicaid application, capacity decline, family disputes

## Output Structure

### 1. Executive Overview

| Element | Content |
|---|---|
| Client snapshot | Name, age, state, capacity status, living situation |
| Critical issues | Top 3-5 pressing legal concerns |
| Immediate actions | Time-sensitive items (deadlines, reporting obligations, urgent filings) |
| Risk level | Low / Moderate / High with brief justification |

### 2. Domain Analysis

Address each applicable domain using this format:

#### Estate Planning
- **Current status** — inventory existing documents; note execution defects, staleness, or missing instruments
- **Gaps** — untitled assets, missing beneficiary designations, outdated fiduciaries
- **Recommendations** — specific documents to draft/update, titling changes

#### Elder Abuse Assessment
- **Indicators** — flag suspicious transactions, undue influence signs, neglect markers from uploaded documents
- **Reporting obligations** — state-specific mandatory reporting rules, applicable agencies
- **Remedies** — protective orders, civil claims, criminal referrals, APS reporting

#### Healthcare Rights & Advance Directives
- **Directive status** — validity, accessibility, consistency with current wishes
- **Medicare/Medicaid status** — current enrollment, eligibility issues
- **Care rights** — nursing home residents' rights, HIPAA considerations

#### Medicaid Planning & Long-Term Care
- **Eligibility analysis** — income/asset limits for client's state
- **Look-back period** — 60 months (30 months in California pre-2024 [VERIFY]); flag any disqualifying transfers
- **Asset protection strategies** — spousal protections, exempt assets, permissible planning tools
- **Compliance check** — verify current arrangements meet regulatory requirements

#### Guardianship / Conservatorship
- **Necessity assessment** — is guardianship needed or are less restrictive alternatives sufficient (POA, representative payee, supported decision-making)?
- **State procedure** — jurisdiction-specific filing requirements, costs, timelines
- **Existing orders** — review scope, reporting compliance, modification needs

#### Benefits & Income
- Social Security, SSI, pension status
- Veteran's benefits if applicable
- Tax implications of current arrangements

### 3. Document Review Findings

When documents are uploaded:

| Document | Key Facts Extracted | Red Flags | Status |
|---|---|---|---|
| {document name} | {dates, parties, terms} | {concerns} | Valid / Defective / Stale |

### 4. Prioritized Action Plan

| Priority | Action | Owner | Deadline/Urgency |
|---|---|---|---|
| Immediate | {e.g., file APS report} | Attorney | Within 24-48 hrs |
| Short-term | {e.g., update POA} | Attorney + family | 2-4 weeks |
| Long-term | {e.g., Medicaid pre-planning} | Attorney + financial advisor | 3-6 months |

## Guidelines

- **Jurisdiction matters**: Elder law varies dramatically by state — always specify which state's rules apply, especially for Medicaid thresholds, guardianship procedures, and abuse reporting
- **Audience-aware language**: Explain legal concepts in plain terms; the summary serves both attorneys and family caregivers
- **Cite sources from uploads**: Reference specific uploaded documents by name when identifying facts or concerns
- **Flag capacity issues carefully**: Note observations without making clinical determinations — recommend formal capacity evaluation where appropriate
- **Mark uncertain citations**: Use `[VERIFY]` for any statutory cite or threshold amount not confirmed against current law
- **Dignity and autonomy**: Frame recommendations to preserve client self-determination; favor least restrictive alternatives
- **State agency references**: Include relevant state aging/protective services contacts where actionable (e.g., APS hotline, state Medicaid office, long-term care ombudsman)

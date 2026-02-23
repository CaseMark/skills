---
name: background-check-summary
description: Summarizes background check data into structured executive reports with risk categorization. Covers criminal records, court filings, employment and education verification, sanctions screening, and adverse media. Use when processing raw background investigation data for pre-employment screening, executive due diligence, or investment-grade investigations.
tags:
  - analysis
  - corporate
  - litigation
  - summarization
  - summary
  - transactional
---

# Background Check Summarization

Transforms raw background check data into a decision-ready summary with risk categorization and compliance flags.

## Output Structure

### 1. Executive Summary

- **Subject**: Full name, DOB, SSN (last 4), search scope
- **Overall Status**: GREEN (clear) / YELLOW (requires review) / RED (adverse findings)
- **Category Table**: Pass/Flag/Pending for each check type
- **Key Findings**: 2-3 most significant items
- **Compliance Flags**: Jurisdiction-specific requirements

### 2. Detailed Findings by Category

Present each with findings or explicit "No records found":

| Category | Key Data Points |
|----------|----------------|
| Criminal Records (Fed/State/County) | Charges, disposition, date, jurisdiction, sentence |
| Sex Offender Registry | Status, jurisdiction |
| Civil Litigation | Case type, role, disposition, damages |
| Employment Verification | Title (claimed vs. verified), dates, departure reason |
| Education Verification | Degree (claimed vs. verified), institution, dates |
| Professional Licenses | Status, disciplinary actions |
| Sanctions/Watchlist | OFAC, BIS, state debarment |
| Adverse Media | Source, date, relevance assessment |

### 3. Methodology & Limitations

Sources searched and any limitations (e.g., jurisdictions not covered, records sealed).

## Risk Categorization

| Status | Criteria | Action |
|--------|----------|--------|
| GREEN | No adverse records, all verifications confirmed | Proceed |
| YELLOW | Minor discrepancies, old/minor offenses, items needing context | Human review required |
| RED | Significant adverse findings, verification failures, recent serious offenses | Enhanced review / adverse action |

### Escalation Factors
- **Criminal**: Felony, violence/fraud/theft-related, recency (<7 years), relevance to position, pending charges
- **Employment**: Title inflation, date gaps >3 months, overlapping employment, employer not found
- **Education**: Degree or institution mismatch, unaccredited institution

## Compliance Requirements

- **FCRA**: All summaries must note that adverse action requires pre-adverse action notice, copy of report, and Summary of Rights
- **Ban-the-Box / Fair Chance**: Flag jurisdictions restricting criminal history inquiries at specific hiring stages
- **EEOC Guidance**: Criminal history must be evaluated for nature of offense, time elapsed, and job-relatedness
- **State-specific lookback limits**: Note applicable 7-year or other limitations on reportable records

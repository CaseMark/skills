---
name: managing-sec-reporting
description: Structures SEC filing preparation with 10-K, 10-Q, 8-K content requirements and XBRL tagging. Use when preparing SEC filings, reviewing filing content, or managing XBRL tagging.
tags:
  - management
  - accounting
metadata:
  author: casemark
  practice_areas:
    - Financial Reporting
    - Audit
    - Accounting
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Sec Reporting

Structures SEC filing preparation with 10-K, 10-Q, 8-K content requirements and XBRL tagging.

## When To Use

- Preparing annual (10-K), quarterly (10-Q), or current (8-K) reports for EDGAR submission
- Reviewing filing content for Regulation S-K and S-X compliance before sign-off
- Coordinating XBRL/Inline XBRL tagging with financial data and disclosure narratives
- Managing the filing calendar, contributor assignments, and cross-functional review cycles
- Responding to SEC comment letters requiring amendments or supplemental filings

## Inputs To Gather

- **Prior filings**: Most recent 10-K and last two 10-Qs as baseline templates and comparatives
- **Trial balance and financial statements**: Audited (10-K) or reviewed (10-Q) figures from the GL
- **Management discussion drafts**: MD&A narratives from FP&A, treasury, and business unit leads
- **Legal and risk disclosures**: Litigation contingencies, risk factors, and subsequent events from legal counsel
- **XBRL taxonomy**: Current US-GAAP taxonomy version; list of company-specific extension elements from prior filings
- **Filing calendar**: SEC deadline date, printer/filing agent cutoff, board and audit committee approval dates
- **Comment letter history**: Any open or recent SEC staff comments and the company's prior responses

## Workflow

1. **Set filing scope and timeline**
   - Confirm filing type (10-K, 10-Q, or 8-K) and the applicable reporting period
   - Map SEC deadline, audit committee review date, and EDGAR filing window
   - Assign section owners: financial statements, MD&A, risk factors, exhibits, XBRL tagging

2. **Assemble and validate financial content**
   - Import trial balance data into the filing template; reconcile to audited/reviewed financials
   - Verify footnote disclosures against ASC requirements (revenue, leases, debt, fair value, etc.) [VERIFY against current ASC guidance for any new standards effective this period]
   - Cross-check numerical consistency: face financials must tie to footnotes, MD&A figures, and selected financial data

3. **Draft and review narrative sections**
   - Update MD&A for the current period: results of operations, liquidity, capital resources, critical accounting estimates
   - Refresh risk factors — add new risks, remove stale ones, confirm boilerplate language still applies
   - Review Item 1 (Business), Item 1A (Risk Factors), and Item 7/7A (MD&A and Quantitative Disclosures) for 10-K; Items 1-4 for 10-Q
   - For 8-K: identify triggering event, confirm correct Item number(s), and draft disclosure within the four-business-day window [VERIFY triggering event Item mapping under Form 8-K instructions]

4. **Execute XBRL/Inline XBRL tagging**
   - Map all financial statement line items to US-GAAP taxonomy elements; flag any that require custom extensions
   - Tag all four face financials (balance sheet, income statement, comprehensive income, cash flows) plus equity roll-forward
   - Apply detail tagging to footnotes as required under the SEC's Inline XBRL mandate [VERIFY current phase-in requirements for detail tagging based on filer status]
   - Run XBRL validation: check for calculation inconsistencies, negative values on unsigned elements, and missing required contexts

5. **Internal review and sign-off**
   - Route draft to audit committee and external auditors for review; incorporate comments
   - Obtain CEO/CFO certifications under SOX Sections 302 and 906
   - Confirm all exhibits (material contracts, sub-certifications, consents) are attached and current
   - Perform final Regulation S-K/S-X compliance check across all Items

6. **File and post-filing tasks**
   - Submit via EDGAR; confirm accepted status and correct filing date
   - Publish earnings press release and investor deck if coordinating with the 10-Q/10-K filing
   - Archive final tagged filing and working papers; update the XBRL extension taxonomy log for next period
   - If an 8-K: confirm no additional Items were triggered by the same event

## Output

- **Filing-ready document** with all Regulation S-K Items populated, financial statements tied, and exhibits indexed
- **XBRL instance document** validated against the US-GAAP taxonomy with a summary of custom extensions used
- **Filing checklist** showing section owner, review status, sign-off date, and open items for each component
- **Comment letter tracker** (if applicable) mapping each SEC staff comment to the responsive disclosure change

## Quality Checks

- All financial figures in MD&A and selected financial data tie exactly to the face financials and footnotes
- XBRL validation report shows zero errors and zero inconsistent calculations
- CEO/CFO certifications are executed and dated; SOX 302 and 906 language matches current requirements [VERIFY certification language against latest SEC rules]
- Filing date is on or before the applicable deadline (60 days for large accelerated filers on 10-K, 40 days on 10-Q; 75/40 for accelerated filers; 90/45 for non-accelerated filers) [VERIFY filer status category and corresponding deadline]
- All exhibits listed in the exhibit index are attached and have correct Item references
- 8-K filings are submitted within four business days of the triggering event
- No tracked-changes, comments, or draft watermarks remain in the final submission

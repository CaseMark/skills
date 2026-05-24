---
name: tax-preparation-workflow
language: en
description: >-
  Automates tax preparation workflows from document collection through return
  generation. Handles income verification, deduction identification, form
  completion, and compliance checking for individual and business returns.
  Use when preparing tax returns, organizing tax documents, or ensuring
  compliance across multiple filing periods.
tags:
  - compliance
  - regulatory
  - drafting
---

# Tax Preparation Workflow

Automated workflow for end-to-end tax preparation: from document ingestion
through return generation and compliance verification.

## Prerequisites

- Tax documents (W-2s, 1099s, K-1s, receipts, prior-year returns)
- Filing status and dependency information
- Business entity documentation (if applicable)
- Tax year and jurisdiction(s)

## Workflow

1. **Document collection and categorization** — ingest and classify all tax documents:
   - Income documents (W-2, 1099 series, K-1, 1098, statements)
   - Deduction evidence (receipts, invoices, mileage logs, charitable contributions)
   - Credits documentation (education, energy, childcare, adoption)
   - Prior-year returns (for carryforward items: NOL, credits, losses)
2. **Income reconstruction** — build complete income picture:
   - Aggregate all income sources by type (wage, self-employment, investment, passive)
   - Identify unreported income from information returns
   - Reconcile with bank statements and financial records
   - Flag discrepancies between reported and claimed income
3. **Deduction and credit identification** — map available deductions and credits:
   - Standard vs. itemized deduction analysis
   - Above-the-line deductions (IRA, student loan, HSA)
   - Schedule C deductions (self-employment)
   - Credit optimization (EITC, CTC, AOTC, Saver's Credit)
   - State-specific deductions and credits
4. **Form preparation and assembly** — generate all required forms:
   - Core forms (1040, schedules, attachments)
   - Entity forms (1120, 1120-S, 1065, 941)
   - Information returns (1099, 1096, W-2c)
   - State and local returns
5. **Compliance verification** — validate the prepared return:
   - Mathematical accuracy check
   - Tax law compliance (recent changes, updates, expiration of provisions)
   - Consistency check across all forms and schedules
   - Prior-year carryforward reconciliation
6. **Review and filing** — produce final deliverables:
   - Draft return with supporting worksheets
   - Tax liability/schedule with cash flow impact
   - Filing instructions and deadline calendar
   - Recommended advisory items (estimated payments, planning opportunities)

## Pitfalls

- Information returns (1099s) filed by payers must match the taxpayer's return — mismatch triggers IRS correspondence
- Standard deduction amounts change annually — verify the correct year's threshold
- Tax law provisions have expiration dates — a deduction available this year may not exist next year
- State filing requirements can be triggered by remote activities — don't assume one state covers all
- Estimated tax penalties apply when payments fall below 90% of current-year or 100% of prior-year tax — calculate exposure proactively
- Carryforward items (NOL, capital losses, tax credits) from prior years are the most common source of filing errors — always reconcile

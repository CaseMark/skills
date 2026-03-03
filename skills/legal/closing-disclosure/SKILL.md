---
name: closing-disclosure
description: Drafts and reviews TRID-compliant U.S. residential Closing Disclosures, assembling all five pages, comparing to Loan Estimates, checking tolerance buckets, and flagging re-disclosure triggers. Use when working with closing disclosures, CDs, TRID, Regulation Z, LE comparison, tolerance cures, cash-to-close, settlement statements, or closing compliance review.
---

# Closing Disclosure

Produce a complete five-page Closing Disclosure per CFPB Form H-25 and a compliance review memo.

## Quick Start

1. Confirm role: lender, settlement agent, borrower counsel, or seller counsel.
2. Gather: loan terms, Loan Estimate(s) with dates, itemized closing costs, escrow/prepaids, payoffs/prorations, closing timeline.
3. If attorney role: produce issue list and client summary — not a lender-signed CD.

## Core Workflow

### 1. Data Intake by CD Page

| Page | Section | Required Inputs |
|------|---------|-----------------|
| 1 | Closing/transaction/loan info | Issue date, closing/disbursement dates, borrower(s), seller(s), property, sale price, lender, loan term, purpose, product, loan ID |
| 1 | Loan terms | Loan amount, rate, P&I, prepay penalty, balloon |
| 1 | Projected payments | P&I, MI, escrow, totals by period |
| 1 | Costs at closing | Total closing costs, lender credits, cash to close |
| 2 | Loan costs (A–C) | Origination, lender-required services, shopped services |
| 2 | Other costs (E–H) | Gov fees, prepaids, escrows, commissions, owner title |
| 2 | Totals (D, I, J) | Subtotals and lender credits |
| 3 | Cash to close | LE vs CD comparison with change reasons |
| 3 | Summaries (K–N) | Borrower/seller transaction summaries, credits, payoffs |
| 4 | Loan disclosures | Assumption, demand, late fee, neg-am, partial payments |
| 4 | Escrow account | Escrowed vs non-escrowed costs, waiver fee |
| 4 | ARM tables | AP/AIR tables (if applicable) |
| 5 | Loan calculations | Total of payments, finance charge, amount financed, APR, TIP |
| 5 | Other disclosures | Appraisal, contract details, liability, refinance, tax |
| 5 | Contact info | Lender/broker/RE agent/settlement agent identifiers |

Flag any missing field as `MISSING`.

### 2. LE Comparison and Tolerance Analysis

| Bucket | Rule | Typical Items |
|--------|------|---------------|
| Zero tolerance | No increase over LE | Lender/broker fees, transfer taxes, non-shoppable services |
| 10% cumulative | Aggregate increase ≤ 10% | Recording fees, shoppable services on lender list |
| No limit | May change if good faith | Prepaids, escrow, non-list providers, owner title |

For each bucket, compare LE vs CD amounts and compute variance. If a zero-tolerance or 10% violation exists without a valid revised LE, state the cure amount and responsible party.

### 3. Re-Disclosure Triggers

A new 3-business-day waiting period is required if any of:

- APR increases > 0.125% (fixed) or > 0.25% (ARM)
- Loan product changes (fixed/ARM, term, IO, neg-am)
- Prepayment penalty added

### 4. Delivery and Timing

```
CD issue date:
Delivery method:    hand / mail / electronic
Deemed receipt date:
Earliest consummation date:
```

Business-day counting excludes Sundays and federal holidays. [VERIFY jurisdiction-specific rules]

## Pitfalls and Checks

- Use CFPB Form H-25 structure; do not rewrite statutory disclosure text unless a state addendum requires it.
- Settlement agent role: confirm lender-supplied loan terms before finalizing pages 1 and 5.
- Lender role: validate settlement fees and prorations from settlement agent before issuing final CD.
- Always reconcile cash-to-close with the transaction summary and payoffs.
- For state transfer taxes, recording fees, and proration rules, require jurisdiction-specific confirmation. [VERIFY]
- Cite: 12 CFR 1026.38, 12 CFR 1026.19(e)(3), 12 CFR 1026.19(f), TILA, RESPA.

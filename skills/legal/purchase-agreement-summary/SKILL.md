---
name: purchase-agreement-summary
language: en
description: Produces structured operational summaries from fully executed residential purchase agreements for title closers and processors. Extracts parties, property identifiers, price/EMD, financing, contingencies, title/survey, HOA, closing costs, prorations, possession, and critical deadlines into scannable tables with source pointers. Flags missing data, document conflicts, unusual clauses, and tight deadlines. Use when summarizing a purchase agreement, opening a title file, preparing escrow instructions, or reviewing contract terms for closing.
---

# Purchase Agreement Summary

Extracts deal-critical terms from a fully executed residential purchase agreement package into a structured operational summary for title closers and processors.

## Prerequisites

Before starting, confirm you have:

- Fully executed purchase agreement (all pages, exhibits, riders, signatures)
- All addenda, amendments, and counteroffers
- Effective date (date of last signature/acceptance)
- State identification

If any referenced document is missing, flag immediately and do not proceed. If effective date is unavailable, ask the user and flag deadline calculations as unconfirmed.

## Workflow

### 1. Normalize Documents

- State scope boundary: operational extraction only, not legal advice
- Label each instrument with a reference tag (e.g., "Amendment #2")
- Preserve page numbers; use "PDF page X of Y" if absent
- Flag when amendments modify previously extracted terms
- Verify signatures/initials on all required pages; flag "execution incomplete" for blanks

### 2. Extract Parties

Extract buyer(s)/seller(s) exactly as written (middle initials, suffixes, entity designations, "and/or assigns"), trust details (full name + trustees), contact info, and broker/agent info.

**Flag:** Spouse missing in community property state, corporate signer without officer title, name discrepancies between documents, marital/vesting language ("Confirm deed vesting instructions").

### 3. Extract Property Identifiers

Required: street address (incl. unit/city/state/zip), parcel ID/APN/PIN, legal description or exhibit reference. Flag each if missing — address-only identification is a title-search risk.

Also capture: county, additional parcels/outlots/common elements, personal property included/excluded (may require Bill of Sale).

### 4. Extract Financial Terms

**Price & EMD:** Current controlling purchase price, price history if amended (each price + source), each EMD deposit (amount, holder, deadline, method), escalation clause terms.

**Financing:** Type (Cash/Conventional/FHA/VA), loan amount or max LTV, down payment, application deadline, commitment/approval deadline.

**Credits & Concessions:** Seller concessions/closing cost credits, repair credits (separate from general — lenders treat differently), rate buy-down credits, TX option fee (paid to seller, not escrow — do not conflate with EMD). Flag: "Seller credit present — confirm lender acceptability."

### 5. Map Critical Deadlines

Build a chronological table:

| Item | Deadline (as written) | Computed Date | Status | Source |
|------|----------------------|---------------|--------|--------|

**Status values** (only when effective date and day-count convention are clear): Passed / Due within 48 hrs / Due within 7 days / Future / Unknown.

**Key deadlines:** Effective date, EMD deposits, inspection period, repair request/resolution, appraisal contingency, financing application/commitment, title commitment delivery/objection/cure, survey, HOA document delivery/review, closing date, possession date.

**Flag:** Closing on Sunday/holiday, "Time is of the Essence" language, amendments resetting deadlines, undefined day-count convention, ambiguous effective date.

### 6. Title, Survey, HOA & Assessments

**Title & Survey:** Who selects title co., owner's policy (required? who pays?), survey type/cost/deadline, title standards, permitted exceptions, commitment/objection/cure timelines, termination rights on title objections.

**HOA/Condo:** Association name/contact, required disclosures, transfer fee allocation, buyer review/termination period. Flag if docs or fees unclear.

**Special Assessments:** Allocation of pending/existing. If silent: "Not stated — confirm local custom."

**Home Warranty:** Note cost/provider for settlement statement.

### 7. Closing Costs, Possession & Special Provisions

**Cost Allocations** — extract who pays: owner's/lender's policy, escrow/closing fee, recording fees, transfer taxes, survey, pest inspection, home warranty.

**Prorations:** Tax proration method (calendar vs. fiscal, current vs. last available) — extract verbatim. Note HOA dues, rents, utilities.

**Possession:** Date, time, rent-back terms, per diem, holdback/deposit, utility transfer. Flag post-closing possession as heightened risk requiring occupancy agreement.

**Special Provisions — flag for review:** Handwritten terms, tenant in property, solar lease, sale contingency, arbitration/mediation clauses, builder addenda, any non-standard clause ("Attorney or underwriter review recommended").

## Output Structure

Produce sections in this order:

1. **Header** — Property address, state, documents received, effective date, summary date, disclaimer
2. **Deal Snapshot** — Two-column table: Buyers, Sellers, Property, Price, Total EMD, Closing Date, Possession, Loan Type/Amount, Title Co., HOA, Special Assessments, Key Flags count
3. **Parties & Contacts**
4. **Property Details**
5. **Price, Earnest Money & Credits**
6. **Financing & Appraisal**
7. **Contingencies**
8. **Title, Survey & Closing Documentation**
9. **HOA & Condominium**
10. **Closing Date, Possession & Occupancy**
11. **Closing Costs, Taxes & Prorations**
12. **Addenda & Amendments Inventory** — Name, date, signing status, what it modifies, source pages
13. **Critical Dates & Deadlines** — Timeline table from Step 5
14. **Flags & Follow-Up** — By severity: Critical (blocking), High (likely delay), Medium (needs clarification), Low (informational)
15. **Source Map** — Category to document label + page/section

## State-Specific Notes

When state is identified, note form-specific issues:

| State | Watch For |
|-------|-----------|
| **California** (C.A.R.) | Liquidated damages/arbitration initials; Natural Hazard Disclosure |
| **Texas** (TREC) | Option Fee paid to seller, not escrow; distinguish from EMD |
| **Florida** (FAR/BAR) | "As-Is" vs. standard inspection clause; EMD refundability trigger |
| **New York / NE** | Attorney review period — contract may not bind until cleared |
| **Minnesota** | Statutory cancellation rights; well/septic disclosure rescission |

Identify specific form version (e.g., "TREC 20-17," "C.A.R. RPA-CA") when possible.

## Guardrails

- **Never fabricate** — use "Not stated" + follow-up flag for missing values
- **Never resolve conflicts** — display side-by-side with source pointers; flag for human resolution
- **Never offer legal conclusions** — use "Contract states..." or "Agreement provides..."
- **Mask sensitive data** — redact SSNs/account numbers; flag "Sensitive data present"
- **Never fabricate legal citations** — use web search for verifiable sources or flag for attorney verification
- **TRID timing** — within 5 days of closing on financed transaction: flag "TRID timing risk"
- **Every term needs a source pointer** (document label + section/page)
- **"Closing Day" test** — if a closer would be surprised by anything missing, the summary is incomplete

**Required disclaimer (verbatim, end of every output):**

> Operational summary for title and escrow processing only. Not legal advice. Verify all terms against the fully executed purchase agreement, counteroffers, amendments, and addenda. Flagged items require human review before reliance.

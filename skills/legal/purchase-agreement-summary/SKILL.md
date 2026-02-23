---
name: purchase-agreement-summary
description: Analyzes fully executed residential purchase agreements (including addenda, amendments, and counteroffers) and produces structured operational summaries for title company closers and processors. Extracts parties, property identifiers, price/EMD, financing, contingencies, title/survey provisions, HOA details, closing cost allocations, prorations, possession terms, and critical deadlines into scannable tables with source pointers. Flags missing information, document conflicts, unusual clauses, and tight/passed deadlines. Use when summarizing a residential purchase agreement, opening a title file, preparing escrow instructions, or reviewing contract terms for closing.
tags:
  - analysis
  - summarization
  - summary
  - transactional
---

# Residential Purchase Agreement Summary for Title & Escrow

Extracts deal-critical terms from a fully executed residential purchase agreement package into a structured operational summary for title closers and processors.

## Prerequisites

1. **Fully executed purchase agreement** — all pages, exhibits, riders, signature blocks with all buyer/seller signatures
2. **All addenda and amendments** — financing, inspection, appraisal, well/septic, lead-based paint, FHA/VA, seller concession, escalation, attorney riders
3. **All counteroffers** incorporated by reference
4. **Effective date** — date of last signature/acceptance; if unavailable, ask the user and flag deadline calculations as unconfirmed
5. **State identification** — for jurisdiction-specific headings and form identification

If any referenced document is missing (legal description exhibit, signed amendments, execution signatures), flag immediately — do not proceed with incomplete data.

## Process

### Step 1: Document Normalization

- State scope boundary at top of every output: operational extraction only, not legal advice
- Label every distinct instrument (e.g., "Purchase Agreement," "Amendment #2," "Counteroffer #1") with a short reference tag
- Preserve page numbers; if absent, use "PDF page X of Y"
- Treat amendments as potentially controlling — flag when later documents modify previously extracted terms
- Verify signatures/initials on all required pages; flag "execution incomplete" for blanks

### Step 2: Extract Parties

| Extract | Notes |
|---------|-------|
| Buyer(s) / Seller(s) exactly as written | Include middle initials, suffixes, entity designations, "and/or assigns" |
| Trust details | Full trust name + trustee names (processor needs trust documents) |
| Addresses, emails, phone numbers | Do not invent missing data |
| Broker/agent info | Separate from parties clearly |

**Flag triggers:**
- Spouse missing from signature block in potential community property state
- Corporate entity signing without officer title
- Name discrepancies between documents (critical flag)
- Marital/vesting language present → "Confirm deed vesting instructions"

### Step 3: Extract Property Identifiers

| Field | Required |
|-------|----------|
| Street address (incl. unit), city, state, zip | Yes |
| County | If stated |
| Parcel ID / APN / PIN | Yes — flag if missing |
| Legal description or exhibit reference | Yes — flag if missing |
| Additional parcels, outlots, common elements, parking, dock rights | Flag each for title follow-up |
| Personal property included/excluded | Note; may require Bill of Sale |

Address-only identification = title-search risk flag.

### Step 4: Extract Financial Architecture

**Purchase Price & EMD:**

| Item | Extract |
|------|---------|
| Purchase price | Current controlling amount |
| Price history | If amended, show each price + source |
| Each EMD deposit | Amount, holder, deadline, method (check/wire) |
| Escalation clause terms | Note whether price was adjusted |

**Financing:**

| Item | Extract |
|------|---------|
| Type | Cash / Conventional / FHA / VA |
| Loan amount or max LTV | As stated |
| Down payment | As stated |
| Application deadline | Date |
| Commitment/approval deadline | Date |

**Credits & Concessions:**

| Item | Extract |
|------|---------|
| Seller concessions / closing cost credits | Amount + source |
| Repair credits | Separate from general credits (lenders treat differently) |
| Rate buy-down credits | Amount + source |
| Option fee (TX) | Amount, paid directly to seller — do not conflate with EMD |

Flag: "Seller credit present — confirm lender acceptability and disclosure requirements."

### Step 5: Map Critical Timeline

Build chronological deadline table with these columns:

| Item | Trigger | Deadline (as written) | Computed Date | Status | Notes | Source |
|------|---------|----------------------|---------------|--------|-------|--------|

**Status values** (compute only when effective date and day-count convention are clear):
- **Passed** / **Due within 48 hrs** / **Due within 7 days** / **Future** / **Unknown**

**Key deadlines to capture:** Effective date, EMD deposit(s), inspection period, repair request/resolution, appraisal contingency, financing application, financing commitment, title commitment delivery, buyer title objection, seller cure, survey, HOA document delivery/review, closing date, possession date/time.

**Flag triggers:**
- Closing date on Sunday or federal holiday
- "Time is of the Essence" language present
- Amendments that reset deadlines
- Day-count convention undefined ("business days" without definition)
- Effective date ambiguous → "Cannot compute — effective date not confirmed"

### Step 6: Title, Survey, HOA & Assessments

**Title & Survey:**
- Who selects title company/escrow holder
- Owner's policy required? Who pays?
- ALTA survey or existing survey — who pays, deadline
- Title standards referenced (marketable, insurable, ALTA owner's)
- Permitted exceptions (easements, covenants, mineral rights)
- Commitment delivery, objection, and cure timelines
- Right to terminate based on title objections — notice mechanics

**HOA / Condo:**
- Association applies? Name/contact?
- Resale disclosures, bylaws, budgets required?
- Who pays transfer fees?
- Buyer review/termination period
- Flag: "HOA indicated but documents or fee allocation unclear"

**Special Assessments:**
- Allocation of pending/existing assessments
- If silent: "Special assessments allocation not stated — confirm local custom"

**Home Warranty:** Note cost/provider (settlement statement line item).

### Step 7: Closing Costs, Possession & Special Provisions

**Cost Allocations** — extract who pays each:

| Item | Buyer | Seller | Split | Source |
|------|-------|--------|-------|--------|
| Owner's policy | | | | |
| Lender's policy | | | | |
| Escrow/closing fee | | | | |
| Recording fees | | | | |
| Transfer taxes | | | | |
| Survey | | | | |
| Pest inspection | | | | |
| Home warranty | | | | |

**Prorations:** Tax proration method (calendar vs. fiscal year, current vs. last available) — extract verbatim if present. Note HOA dues, rents, utilities.

**Possession:** Date, time, rent-back terms, per diem rent, holdback/security deposit, utility transfer. Flag post-closing possession as heightened operational risk requiring occupancy agreement.

**Special Provisions — flag for review:**
- Handwritten terms, "Additional Terms" / "Special Stipulations"
- Tenant in property, solar panel lease, sale contingency
- Arbitration, mediation, attorney fees, specific performance clauses
- Builder addenda shifting risk
- Any non-standard clause → "Non-standard clause — attorney or underwriter review recommended"

## Output Structure

Produce all sections in this order:

1. **Header** — File/order name, property address, state, documents received, effective date, summary date, disclaimer
2. **Deal Snapshot** — Two-column summary table (Buyers, Sellers, Property, Price, Total EMD, Closing Date, Possession, Loan Type/Amount, Title Co., HOA status, Special Assessments, Key Flags count)
3. **Parties & Contacts** — Separate tables for parties and agents/brokers
4. **Property Details**
5. **Price, Earnest Money & Credits**
6. **Financing & Appraisal**
7. **Contingencies**
8. **Title, Survey & Closing Documentation**
9. **HOA & Condominium**
10. **Closing Date, Possession & Occupancy**
11. **Closing Costs, Taxes & Prorations**
12. **Addenda, Amendments & Disclosures Inventory** — Name, date, signing status, what it modifies, source page range
13. **Critical Dates & Deadlines** — Timeline table per Step 5
14. **Flags & Follow-Up Items** — Organized by severity: Critical (blocking), High (likely delay), Medium (needs clarification), Low (informational)
15. **Source Map** — Category → document label + page/section

## State-Specific Notes

When state is identified, add a brief subsection noting form-specific issues:

| State | Watch For |
|-------|-----------|
| **California** (C.A.R.) | Liquidated damages / arbitration initials; Natural Hazard Disclosure |
| **Texas** (TREC) | Option Fee (¶5) paid directly to seller, not escrow; distinguish from EMD |
| **Florida** (FAR/BAR) | "As-Is" vs. standard contract inspection/terminate clause; EMD refundability trigger |
| **New York / NE states** | Attorney review period — contract may not be binding until cleared |
| **Minnesota** | Statutory cancellation rights; well/septic disclosure rescission rights |

Identify the specific state form version (e.g., "TREC 20-17," "C.A.R. RPA-CA") when possible.

## Guidelines

- **Never fabricate missing values** — use "Not stated" and add a follow-up flag
- **Never resolve conflicts** — display side-by-side with source pointers; flag for human resolution
- **Never offer legal conclusions** — use "Contract states…" or "Agreement provides…"; if asked for enforceability analysis, state attorney review is required
- **Mask sensitive data** — redact SSNs, account numbers if detected; flag "Sensitive data present — do not distribute"
- **Never fabricate legal citations** — if jurisdiction-specific info is needed, perform web search with verifiable URLs or state attorney verification required
- **TRID timing** — if summary is produced within 5 days of closing, flag "High Priority — TRID timing risk" for financed transactions
- **Apply the "Closing Day" test** — if a closer at the table today would be surprised by anything not in the summary, the summary is incomplete
- **Every extracted term must have a source pointer** (document label + section/page)

**Required disclaimer (verbatim, end of every output):**
> Operational summary for title and escrow processing only. Not legal advice. Verify all terms against the fully executed purchase agreement, counteroffers, amendments, and addenda. Flagged items require human review before reliance.

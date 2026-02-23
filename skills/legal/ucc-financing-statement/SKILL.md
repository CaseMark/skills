---
name: ucc-financing-statement
description: Drafts UCC-1 Financing Statements and UCC-3 Amendments to perfect security interests in personal property collateral under Article 9 of the Uniform Commercial Code. Handles debtor identification, collateral descriptions, jurisdictional filing requirements, continuations, terminations, and assignments. Use when drafting UCC-1 filings, UCC-3 amendments, continuation statements, or secured transaction perfection documents in loan and financing transactions.
tags:
  - agreement
  - drafting
  - transactional
---

# UCC Financing Statement and Amendments

Drafts filing-ready UCC-1 Financing Statements or UCC-3 Amendments that comply with Article 9 and state-specific filing office requirements.

## Prerequisites

1. **Security agreement** — executed agreement identifying debtor, secured party, and collateral
2. **Entity verification documents** — certificate of formation/incorporation, organizational ID, or individual debtor's driver's license name
3. **Transaction documents** — loan agreement, promissory note, any related guaranty or subordination agreements
4. **Collateral details** — serial numbers, account numbers, registration numbers for specific assets if applicable
5. **Filing jurisdiction confirmed** — state of organization (registered entities) or principal residence (individuals) per § 9-307

## Process

### Step 1: Extract Party Information

| Field | Individual Debtor | Organization Debtor |
|-------|-------------------|---------------------|
| Name | Exact name per driver's license / govt ID | Exact registered name per state records |
| Address | Mailing address | Mailing address |
| Jurisdiction | Principal residence state | State of organization |
| Org ID | N/A | Organizational ID number |
| Tax ID | If required by jurisdiction | If required by jurisdiction |

- Cross-check debtor name against organizational documents — minor variations can render filing "seriously misleading" under § 9-506
- For secured party, capture full legal name, mailing address, and any filing agent designation

### Step 2: Determine Filing Type and Jurisdiction

**Filing office**: Generally Secretary of State for the debtor's jurisdiction of organization/residence.

**Exceptions requiring special filing**:
- **Fixture filings** → county real estate records where fixtures located
- **As-extracted collateral** (minerals/timber) → county real estate records
- **Transmitting utilities** → may have special state procedures

**Check**: State-specific form requirements (standard vs. state-modified UCC-1/UCC-3), electronic filing availability, current filing fees.

### Step 3: Draft Collateral Description

Use UCC-defined Article 9 categories where possible:

| Category | Examples |
|----------|----------|
| Accounts | Rights to payment for goods/services |
| Chattel paper | Records evidencing monetary obligation + security interest |
| Deposit accounts | Demand, time, savings, passbook accounts |
| Equipment | Goods used in business (not inventory/farm products/consumer goods) |
| General intangibles | Payment intangibles, software, IP rights |
| Instruments | Promissory notes, drafts |
| Inventory | Goods held for sale/lease, raw materials, WIP |
| Investment property | Securities, securities accounts, commodity contracts |
| Letter-of-credit rights | Rights to draw under letter of credit |
| Commercial tort claims | Must be specifically described — no category-only filing |

**Description rules**:
- Must "reasonably identify" collateral per § 9-108
- Methods: specific listing, category, UCC type, quantity, formula, or other objective method
- "All assets" / "all personal property" supergeneric descriptions are permitted **only in financing statements** (not security agreements) — confirm jurisdiction allows
- For specific equipment/vehicles: include make, model, year, serial/VIN
- For IP: include registration numbers, application numbers
- Add proceeds clause if intended: "together with all proceeds and products thereof"

### Step 4: UCC-1 Assembly

```
UCC FINANCING STATEMENT (UCC-1)

1. DEBTOR
   Name: [exact legal name]
   Address: [mailing address]
   Jurisdiction of Organization: [state]    Org ID: [number]

2. SECURED PARTY
   Name: [exact legal name]
   Address: [mailing address]

3. COLLATERAL DESCRIPTION
   [Collateral description per Step 3]

4. ADDITIONAL INFORMATION (if applicable)
   [ ] Proceeds  [ ] Products  [ ] After-acquired property
   [ ] Fixture filing (include real estate description + record owner)
   [ ] Transmitting utility
   [ ] Public-finance transaction
   [ ] Manufactured-home transaction
```

### Step 5: UCC-3 Amendment Assembly

Reference the original filing: file number, filing date, filing office.

| Amendment Type | Timing / Requirements |
|----------------|----------------------|
| **Continuation** | File within 6-month window before 5-year lapse date |
| **Termination** | Secured party must file within 20 days of demand if obligation satisfied (§ 9-513) |
| **Assignment** | Full assignee name, address; authority documentation |
| **Amendment** | Specify exactly what is added, deleted, or changed |

- For collateral amendments: state precisely what collateral is added or released
- For party name changes: include both old and new information
- Debtor must authorize amendments that add collateral or add a debtor

### Step 6: Quality Control Checklist

- [ ] Debtor name matches organizational records / government ID exactly
- [ ] Organizational ID included for registered organizations
- [ ] Collateral description covers all intended property per security agreement
- [ ] Collateral description consistent with (but need not mirror) security agreement
- [ ] Correct filing office for debtor's jurisdiction
- [ ] For UCC-3: original file number and filing date verified
- [ ] For continuations: filing within 6-month pre-lapse window confirmed
- [ ] Authorization exists (security agreement grants filing authority, or separate authorization obtained)
- [ ] State-specific form requirements satisfied
- [ ] Filing fee amount confirmed
- [ ] No common rejection triggers: wrong name, missing org ID, wrong office, incomplete fields

## Output

Produce two deliverables:

1. **Filing-ready UCC-1 or UCC-3** formatted per the jurisdiction's accepted form, all mandatory fields completed
2. **Filing guidance memo** covering: filing office and method, fees, statutory citations for key compliance points, any state non-uniform provisions identified, and lapse/continuation calendar dates

## Guidelines

- Never assume debtor name — always verify against organizational records or government-issued ID
- Flag any jurisdiction with known non-uniform Article 9 amendments (e.g., states requiring tax ID, additional certifications)
- Commercial tort claims cannot be described by category alone — require specific description
- Consumer-goods transactions have additional requirements under § 9-625(c)-(d)
- When in doubt about supergeneric descriptions, use specific categories as a safer approach
- Mark any state-specific citation or rule you cannot fully verify with `[VERIFY]`
- Include a tickler date for the 5-year lapse and the 6-month continuation window in the guidance memo

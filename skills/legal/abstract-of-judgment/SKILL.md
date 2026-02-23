---
name: abstract-of-judgment
description: Drafts an Abstract of Judgment for recording with the county recorder to create a judgment lien on a debtor's real property. Extracts party information, judgment details, and monetary components from case documents and applies state-specific formatting and certification requirements. Use post-judgment in commercial litigation to enforce monetary awards, perfect judgment liens, or prepare lien filings.
tags:
  - drafting
  - litigation
  - summary
---

# Abstract of Judgment

Drafts a recordable Abstract of Judgment that creates a valid judgment lien on the debtor's real property.

## Prerequisites

1. **Judgment order** — final judgment with entry date, relief granted, and any amendments
2. **Case filing documents** — complaint, caption, case number
3. **Party information** — full legal names, addresses, aliases/DBAs for all creditors and debtors
4. **Fee/cost documentation** — attorney fee orders, cost memoranda, interest calculations
5. **Jurisdiction** — state and county where abstract will be recorded

## Output Structure

### 1. Court & Case Information

| Field | Source |
|-------|--------|
| Court name (full, with department/division) | Case caption |
| County | Filing records |
| Case number | Case caption |
| Date judgment entered | Judgment order |
| Type of judgment | Default / summary judgment / jury verdict / bench trial |

### 2. Party Identification

For each **judgment creditor** and **judgment debtor**:

- [ ] Full legal name exactly as it appears in the judgment
- [ ] Individual vs. entity designation (include corporate suffixes)
- [ ] Aliases, DBAs, former names
- [ ] Last known address (debtor address critical for enforcement)
- [ ] Middle initials, suffixes — verify spelling against judgment

### 3. Monetary Breakdown

| Component | Amount (numerical) | Amount (written) |
|-----------|--------------------|-------------------|
| Principal | $ | |
| Costs of suit | $ | |
| Attorney fees | $ | |
| Other awards | $ | |
| **Subtotal** | $ | |
| Post-judgment interest | $ | |
| **Total due as of [date]** | $ | |

Interest calculation requirements:
- Statutory rate (verify current rate — varies by state)
- Simple vs. compound
- Accrual start date
- Cite controlling statute (e.g., Cal. Civ. Proc. § 685.010 [VERIFY])

### 4. Judgment Modifications

If applicable, list each amendment/modification with:
- Date of order
- Nature of modification
- Effect on monetary amount

### 5. Certification Block

- Clerk certification language per jurisdiction's required form
- Signature line for clerk
- Court seal placement
- Date of certification
- Notarization block (if jurisdiction requires)

## Jurisdiction-Specific Compliance

- [ ] Check for **mandatory court forms** (e.g., California Judicial Council Form EJ-001 [VERIFY])
- [ ] Verify **statutory authority** for judgment liens in the state
- [ ] Confirm **recording requirements** for the target county
- [ ] Check whether **legal property descriptions** are required in the abstract
- [ ] Verify **lien duration and renewal** deadlines under state law
- [ ] Confirm whether abstract covers real property only or also personal property

## Guidelines

- Every fact in the abstract must be verified against source documents — errors can void the lien
- Present all dollar amounts in both numerical and written form
- If the judgment was entered against multiple debtors, specify joint/several liability status
- Do not conflate the abstract (lien creation) with writs of execution (enforcement)
- Flag any discrepancies between party names in the complaint vs. the judgment
- Mark any unverified statutory citations with `[VERIFY]`
- Note that recording requirements vary by county even within the same state

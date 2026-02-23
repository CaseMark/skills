---
name: revolving-credit-agreement
description: Drafts a market-standard U.S. revolving credit agreement establishing a revolving line of credit between lender and borrower. Covers facility structure, commitment amounts, borrowing mechanics, SOFR/base rate interest, letter of credit sublimits, borrowing base calculations, collateral and security packages, guarantees, representations and warranties, affirmative/negative/financial covenants, conditions precedent, events of default, and remedies. Use when drafting or negotiating revolving credit facilities, asset-based lending agreements, or syndicated loan documents.
tags:
  - agreement
  - drafting
  - transactional
---

# Revolving Credit Agreement

Drafts a complete, market-standard revolving credit agreement for U.S. commercial lending transactions, suitable for bilateral or syndicated facilities.

## Prerequisites

1. **Parties** — full legal names, states of organization; for syndicated deals, each lender's commitment amount and administrative agent identity
2. **Facility economics** — total commitment amount, maturity date, applicable margins (SOFR spread, base rate spread), unused fee rate
3. **Collateral package** — asset types, borrowing base methodology (if asset-based), advance rates against eligible A/R and inventory
4. **Guarantors** — full legal names, guaranty scope (unconditional/absolute vs. limited amount)
5. **Financial covenant targets** — FCCR threshold, leverage ratio cap, testing frequency
6. **Permitted basket sizes** — indebtedness, investments, restricted payments, asset sale thresholds

## Output Structure

### 1. Document Header & Parties
- Execution date; full legal names and states of organization for all parties
- Syndicated facilities: administrative agent designation, lender commitment schedule
- Recitals: transaction context, refinancing purpose if applicable
- Defined terms: "Agreement," "Borrower," "Lender," "Obligations"

### 2. Credit Facility Structure

| Element | Drafting Notes |
|---|---|
| Revolving Commitment | Amount in figures and words |
| Availability Period | Closing Date → Maturity Date; earlier termination triggers |
| LC Sublimit | Max aggregate face amount outstanding; reduces revolving availability dollar-for-dollar |
| Borrowing Base | Advance rates vs. eligible A/R and inventory; BB certificate delivery schedule |
| Commitment Reductions | Voluntary (borrower election) and mandatory (specified events/amortization schedule) |

### 3. Borrowing Mechanics

| Loan Type | Notice Deadline | Lead Time |
|---|---|---|
| Base Rate | 11:00 a.m. | Same business day |
| SOFR (1M / 3M / 6M) | 11:00 a.m. | 2–3 business days prior |

**Borrowing Notice required contents:** requested amount, funding date, rate option, interest period (SOFR only)

- Disbursement: wire to borrower's designated account
- Conversions / continuations: specify procedures at interest period end
- Each borrowing request constitutes a deemed representation that all conditions precedent remain satisfied

### 4. Interest, Fees & Payments

**Interest Rate Options:**

| Rate Type | Formula |
|---|---|
| SOFR Rate | Term SOFR (CME) + Credit Spread Adjustment + Applicable Margin |
| Base Rate | Highest of: (i) Fed Funds Rate + 0.50%, (ii) Prime Rate, (iii) Term SOFR + 1.00% — then + Applicable Margin |
| Default Rate | Applicable Rate + 2.00% per annum |

**Fees:**

| Fee | Typical Rate | Basis | Payment Timing |
|---|---|---|---|
| Unused Commitment Fee | 0.125%–0.50% p.a. | Daily avg. unused commitment | Quarterly in arrears |
| LC Fronting Fee | Negotiated | Outstanding LC face amount | Monthly |
| LC Participation Fee | Applicable Margin | Outstanding LC face amount | Monthly |

**Payment mechanics:** Immediately available funds; no setoff, counterclaim, or deduction permitted.

### 5. Repayment & Prepayment

- **Scheduled amortization:** None; principal due in full on Maturity Date
- **Voluntary prepayment:** Any time without premium or penalty; advance notice per rate type
- **Mandatory prepayment:** Immediately upon outstandings exceeding commitment or borrowing base (from commitment reductions, BB declines, or other causes)
- **Re-borrowing:** Permitted up to revolving commitment; prepayments do not permanently reduce availability

### 6. Collateral & Security

- First-priority security interest in all present and after-acquired assets: A/R, inventory, equipment, general intangibles, investment property, and proceeds
- Reference Security Agreement / Pledge Agreement; UCC financing statements in all applicable jurisdictions
- Real property: Mortgage or Deed of Trust (identify mortgaged properties)
- Permitted priority liens: PMSI, statutory tax liens, other negotiated permitted liens
- Borrower obligations: maintain collateral; deliver periodic collateral reports; permit field exams and appraisals
- Borrowing base certificates: delivery frequency (weekly vs. monthly keyed to availability thresholds)

### 7. Guarantees & Credit Support

- Identify guarantors by full legal name; reference separate Guaranty Agreement
- Guaranty type: unconditional and absolute; specify all-obligations vs. limited amount/scope
- Address upstream / cross-stream / downstream structure; analyze fraudulent transfer exposure and corporate benefit
- Guarantor collateral: reference applicable security documents
- Release triggers: subsidiary sale, financial metric achievement, or other negotiated conditions

### 8. Representations & Warranties

Made as of Closing Date; deemed repeated on each borrowing date and each certificate or financial statement delivery:

- [ ] Due organization, valid existence, qualification in all necessary jurisdictions
- [ ] Corporate power and authority; execution duly authorized by all necessary action
- [ ] No violation of organizational documents, applicable law, or material contracts; all required consents obtained
- [ ] Financial statements accurate, complete, GAAP-compliant; no MAE since date thereof
- [ ] No undisclosed liabilities
- [ ] Good and marketable title to properties; no liens except Permitted Liens
- [ ] No IP infringement on third-party rights
- [ ] No pending or threatened litigation with reasonably expected MAE
- [ ] Compliance with law: environmental, ERISA, tax, anti-corruption (FCPA / OFAC / AML)

### 9. Affirmative Covenants

| Covenant | Requirement |
|---|---|
| Annual Financials | Audited, within 90–120 days of FY-end + CFO compliance certificate |
| Quarterly Financials | Unaudited, within 45 days of quarter-end + compliance certificate |
| Tax Payments | Pay before delinquency; contest in good faith with adequate reserves maintained |
| Insurance | Property, casualty, liability, BI coverage; lender named as loss payee and additional insured |
| Legal Compliance | Maintain all licenses, permits, corporate existence, and material franchises |
| Property Maintenance | Maintain properties in good condition and repair |
| Default / MAE Notice | Prompt written notice of defaults and material adverse changes |
| Books & Records | GAAP-compliant; permit lender inspections and field audits |

### 10. Negative Covenants

| Restriction | Typical Permitted Basket |
|---|---|
| Additional Indebtedness | PMSI up to $[__]; intercompany debt; refinancings of existing debt |
| Liens | Permitted Liens only (PMSI, statutory tax, existing specified liens) |
| Investments / Acquisitions | Subsidiary investments; liquid short-term instruments; general basket up to $[__] |
| Restricted Payments | Permitted only if no Default exists and specified financial tests satisfied |
| Fundamental Changes | No mergers, consolidations, or substantially-all asset sales without lender consent |
| Asset Dispositions | Ordinary course only; consent required above $[__] threshold |
| Affiliate Transactions | Arm's-length; board approval + fairness opinion above $[__] |

### 11. Financial Covenants (if applicable)

| Covenant | Typical Threshold | Testing Period |
|---|---|---|
| Min. Fixed Charge Coverage Ratio | ≥ 1.10:1.00 – 1.25:1.00 | Quarterly TTM |
| Max. Total Leverage Ratio | ≤ 2.50:1.00 – 4.00:1.00 | Quarterly TTM |
| Min. Asset Coverage / Borrowing Base | Per BB certificate | Weekly or monthly |

**EBITDA definition:** Specify inclusions/exclusions — extraordinary items, non-cash charges, pro forma adjustments for permitted acquisitions. Compliance certificates due concurrently with financial statement delivery.

### 12. Conditions Precedent

**Initial Funding:**
- [ ] Executed loan documents (credit agreement, security agreement, guaranty, promissory note)
- [ ] Organizational documents: charter, bylaws/operating agreement, good standing certificates
- [ ] Authorizing board resolutions and incumbency certificates
- [ ] Legal opinion from borrower's counsel (authority, enforceability, no conflicts)
- [ ] Evidence of required insurance with lender as loss payee / additional insured
- [ ] UCC / lien searches; UCC-1 financing statements filed in all required jurisdictions
- [ ] Payoff letters for refinanced indebtedness; lien termination statements
- [ ] Closing certificate (no Default; reps true and correct in all material respects; no MAE)

**Each Subsequent Borrowing:**
- [ ] Borrowing notice properly and timely delivered
- [ ] Representations and warranties true and correct in all material respects
- [ ] No Default or Event of Default exists or would result
- [ ] Total outstandings after funding ≤ Revolving Commitment and Borrowing Base availability

### 13. Events of Default & Remedies

| Event of Default | Grace Period |
|---|---|
| Payment of Principal | None |
| Payment of Interest or Fees | 3–5 business days |
| Affirmative Covenant Breach | 30 days after notice |
| Financial Covenant Breach | None |
| Negative Covenant Breach | None |
| Material Representation Misstatement | None |
| Cross-Default (material indebtedness) | Per other agreement; threshold $500K–$5M depending on borrower size |
| Voluntary or Involuntary Bankruptcy / Insolvency | None (automatic acceleration for voluntary filing) |
| Unsatisfied Judgment | Unstayed for [30] days above $[__] threshold |
| Change of Control | As defined |

**Remedies:** Accelerate all obligations; terminate commitment; impose default rate; exercise all rights under loan documents and applicable law, including UCC Article 9 enforcement and collateral foreclosure.

### 14. Miscellaneous

| Provision | Standard Treatment |
|---|---|
| Governing Law | State of lender's location or borrower's principal operations |
| Jurisdiction / Venue | Exclusive jurisdiction; **JURY TRIAL WAIVER IN ALL CAPS** |
| Notices | Hand delivery, overnight courier, or email with confirmation; specify addresses |
| Amendments / Waivers | Written; signed by all required parties; no implied continuing waiver |
| Assignments | Borrower: no assignment without consent. Lender: free assignment to eligible financial institutions |
| Costs & Expenses | Borrower reimburses lender's reasonable attorneys' fees (preparation, negotiation, enforcement) |
| Indemnification | Borrower indemnifies lender; carve-out for gross negligence and willful misconduct |
| Counterparts / E-Signatures | Execution in counterparts permitted; electronic signatures valid and binding |

### 15. Signature Blocks

- Full legal entity name; signature line; printed name and title of authorized officer
- Corporate secretary attestation confirming authority of signing officers
- Reference agreement title and execution date on each signature page

## Guidelines

- **Usury compliance:** Verify rate caps under applicable state law before finalizing margins [VERIFY state-specific usury limits]
- **UCC Article 9:** Confirm financing statements filed and control agreements executed prior to or concurrently with closing; run pre-closing lien searches
- **SOFR:** Use Term SOFR (CME Group) + ARRC-recommended credit spread adjustment; confirm tenor (1M / 3M / 6M) matches borrower's operational needs [VERIFY current ARRC guidance]
- **Fraudulent transfer:** Analyze guaranty and upstream/cross-stream security interests for corporate benefit and borrower/guarantor solvency at time of grant
- **Syndicated facilities:** Add pro rata sharing, voting thresholds (majority lenders for operational consents; all-lender consent for fundamental changes), and agency/indemnification provisions for administrative agent
- **Bank regulatory:** If lender is a regulated depository institution, confirm compliance with applicable lending limits and regulatory capital requirements
- **Truth in Lending / Reg Z:** Generally inapplicable to commercial credit facilities; confirm borrower is not a natural person consumer
- All financial thresholds, basket amounts, and ratio levels are placeholders — calibrate to borrower's industry, size, leverage profile, and lender's credit policy

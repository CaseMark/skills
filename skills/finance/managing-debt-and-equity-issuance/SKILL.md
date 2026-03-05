---
name: managing-debt-and-equity-issuance
description: Structures accounting for debt and equity issuances with classification, measurement, and issuance cost treatment. Use when accounting for debt issuance, recording equity offerings, or classifying hybrid instruments.
tags:
  - management
  - accounting
  - treatment
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
# Managing Debt And Equity Issuance

Structures accounting for debt and equity issuances including initial recognition, classification of instruments as debt or equity, measurement at issuance, treatment of issuance costs, and ongoing reporting under ASC 470/480/505 and IFRS 9/IAS 32.

## When To Use

- Recording a new debt issuance (term loan, bond, note, credit facility draw)
- Accounting for an equity offering (common stock, preferred stock, warrants)
- Classifying a hybrid or compound instrument (convertible notes, mandatorily redeemable preferred)
- Allocating proceeds when debt and equity are bundled (units, debt with detachable warrants)
- Determining treatment of issuance costs, discounts, or premiums
- Evaluating whether an instrument is liability-classified or equity-classified under ASC 480 / IAS 32

## Inputs To Gather

- **Term sheet or indenture** — principal amount, stated rate, maturity, conversion features, call/put provisions
- **Proceeds received** — gross cash, in-kind consideration, or net proceeds after underwriting fees
- **Issuance costs breakdown** — underwriting discounts, legal fees, registration costs, printing, rating agency fees
- **Instrument features** — mandatory redemption, contingent settlement, conversion ratios, anti-dilution adjustments, participating rights
- **Entity's functional currency and reporting framework** (US GAAP vs. IFRS) [VERIFY]
- **Fair value data** — market yields for similar debt, Black-Scholes or lattice inputs for embedded options or warrants
- **Board resolutions and authorizations** — authorized share counts, par value

## Workflow

1. **Classify the instrument**
   - Apply ASC 480 to determine if the instrument has mandatory redemption or is settleable in a variable number of shares (liability) [VERIFY applicable guidance version]
   - For convertible instruments, evaluate under ASC 470-20 whether a beneficial conversion feature (BCF) exists or, post-ASU 2020-06, whether the simplified single-model applies [VERIFY adoption status of ASU 2020-06]
   - Under IFRS, apply IAS 32 fixed-for-fixed test to split compound instruments into liability and equity components
   - For warrants and options, assess ASC 815-40 equity-classification conditions (indexed to own stock, settlement requirements)

2. **Measure at initial recognition**
   - **Plain debt**: Record at fair value of proceeds received; calculate effective interest rate if issued at a discount or premium
   - **Plain equity**: Credit common/preferred stock at par, credit APIC for excess over par
   - **Bundled instruments (debt + warrants)**: Allocate proceeds using relative fair value method (US GAAP) or residual method — liability component first at fair value, residual to equity (IFRS)
   - **Convertible debt (post-ASU 2020-06, US GAAP)**: Record as single liability unit at proceeds less issuance costs; no separate equity component unless there is a substantive conversion premium settled in cash

3. **Account for issuance costs**
   - **Debt issuance costs**: Present as a direct deduction from the carrying amount of the debt liability (ASC 835-30); amortize over the debt term using the effective interest method
   - **Line of credit / revolving facility**: Issuance costs may be recorded as a deferred asset and amortized ratably [VERIFY — ASC 835-30-45-1A exception]
   - **Equity issuance costs**: Charge against APIC (net of any tax benefit); do not run through the income statement
   - **Hybrid instruments**: Allocate issuance costs proportionally between debt and equity components

4. **Record journal entries**
   - Debt issuance: Dr. Cash, Dr. Debt Issuance Costs (contra-liability) / Cr. Notes Payable (face), Cr. Premium or Dr. Discount as needed
   - Equity issuance: Dr. Cash / Cr. Common Stock (par), Cr. APIC (excess), Dr. APIC (issuance costs)
   - Compound instrument (IFRS): Dr. Cash / Cr. Financial Liability (at FV), Cr. Equity — Conversion Option (residual)

5. **Set up ongoing measurement**
   - Amortize discount/premium and issuance costs using effective interest method each reporting period
   - Monitor for modifications or extinguishments that trigger gain/loss recognition (ASC 470-50 10% cash flow test for debt modifications)
   - Track conversion features for potential diluted EPS impact (if-converted method under ASC 260)

## Output

Produce a management report containing:

- **Instrument classification summary** — liability vs. equity vs. compound, with citation to the governing ASC/IFRS paragraph
- **Initial recognition entry** — full journal entry with amounts, accounts, and effective interest rate
- **Issuance cost schedule** — total costs, allocation between debt and equity (if applicable), amortization method, and projected amortization table
- **Ongoing measurement guidance** — amortization schedule for discount/premium, key dates (interest payments, maturity, first call date), and triggers for reassessment
- **Disclosure checklist** — required footnote disclosures for debt (ASC 470) and equity (ASC 505) or IAS 32/IFRS 7 equivalents

## Quality Checks

- Classification analysis references the specific ASC or IAS paragraph supporting the conclusion
- Effective interest rate calculation ties to cash flow schedule and reconciles to carrying amount at maturity
- Issuance costs net against the correct balance sheet line (contra-liability for debt, APIC offset for equity) — not expensed
- Bundled instrument allocation sums to total proceeds received with no residual unallocated
- Entries balance (total debits = total credits) and use the entity's actual chart of accounts where provided
- All jurisdiction-dependent or standard-dependent conclusions are marked [VERIFY] where the entity's specific adoption status or reporting framework could change the outcome
- Diluted EPS impact is flagged for any instrument with potential share settlement

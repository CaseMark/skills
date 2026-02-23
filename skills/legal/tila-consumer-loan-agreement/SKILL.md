---
name: tila-consumer-loan-agreement
description: Drafts U.S. consumer loan agreements with integrated Truth in Lending (TILA/Reg Z) disclosures for use in negotiation and closing. Use for drafting enforceable credit agreements that must include disclosure-box construction, APR and finance-charge calculations, payment schedule formatting, prepayment/default/enforcement clauses, co-signer notice, and state-law overlays. Trigger when user requests include "consumer loan agreement", "TILA", "Regulation Z", "Truth in Lending", "APR disclosure", "finance charge", and "loan contract drafting".
tags:
  - agreement
  - drafting
  - regulatory
  - transactional
---

# TILA-Compliant Consumer Loan Agreement

Drafts a U.S. consumer loan contract and disclosure package that is ready for borrower execution and downstream enforcement review.

## Prerequisites

1. **Transaction snapshot**: all borrower/lender legal names, addresses, contact channels, jurisdiction/state of compliance.
2. **Loan economics**: principal/face amount, fees, add-ons, APR basis, rate type, term, payment frequency, payment count, due dates.
3. **Regulatory facts**: whether borrower is consumer and whether loan is closed-end/open-end; state-law limits, required notices, licensing/state form requirements.
4. **Collateral status**: unsecured vs secured, collateral description (VIN/VIN + location or legal description/address), insurance requirements.
5. **Credit posture**: co-borrowers, co-signers/guarantors, servicemember status.
6. **Remedy controls**: acceleration trigger policy, late fee cap preferences, cure rights, repossession method, attorney fee entitlement rules.

## Output Structure / Process

1) **Extract and normalize inputs**
   - Use a single source of truth for numeric values and party names.
   - Reject contradictions before drafting (e.g., finance charge inconsistent with APR or payment totals).

| Required Field | Format | Validation Rule |
|---|---|---|
| Lender legal name | Exact legal entity name | Must match regulatory filings |
| Borrower legal name(s) | Full legal names | Match ID docs style |
| Loan amount | Currency | Two-decimal precision |
| Rate type | APR %, fixed/variable | APR must reconcile to finance charge |
| Term | Months or schedule dates | Payments × due date cadence aligns |
| Fees included as finance charge | Currency | Include only conditional charges |
| Payment schedule | table or formula | Sum must match Total of Payments |
| State | US state/jurisdiction | Use state overlays after federal text |

2) **Build the TILA disclosure block first**
   - Place disclosure block before core contract terms.
   - Use bold, boxed, conspicuous presentation.
   - Keep borrower-facing language plain and exact.

```text
**FEDERAL TRUTH IN LENDING DISCLOSURES**
| Required disclosure (exact label) | Value |
| Amount Financed | |
| Finance Charge | |
| APR | |
| Total of Payments | |
| Total Payments if irregular | |
| Payment Schedule (Your payment schedule will be) | |
| State-specific required notice | |
| Co-signer required notice (if applicable) | |
```

3) **Compute disclosure math before drafting narrative terms**
   - Amount Financed = principal actually made available to borrower (or to borrower’s behalf), net of excluded items.
   - Finance Charge = cost of credit under Reg Z definition.
   - Total of Payments = Amount Financed + Finance Charge (plus verified fees per term).
   - APR = computed under Regulation Z methodology [VERIFY].
   - Payment schedule must reconcile exactly to Total of Payments within tolerance.
   - If precomputed method used, prepayment finance charge refunds apply per governing method for the product type [VERIFY].

4) **Draft contract body in deterministic sequence**
   - Intro/parties/recitals.
   - Core promise: credit extended, repayment obligation, disclosure incorporation.
   - Payment terms with clear schedule and frequency.
   - Prepayment clause: no-penalty default plus exception branch if penalty exists.
   - Late charges: amount/method/cap, no compounding default.
   - Default events with cure period and notice method.
   - Security clause (if secured) or unsecured limitation statement.

5) **Apply conditional modules**
   
| Module | Include when |
|---|---|
| Secured collateral package | collateral used |
| Unsecured limitation statement | no collateral granted |
| Co-signer/guarantor provisions | third-party guarantee present |
| Force-placed insurance | borrower failure to maintain required coverage |
| Servicemembers Civil Relief Act notice | servicemember status confirmed/possible |
| Co-signer federal notice | co-signer not receiving loan proceeds |

6) **Generate execution package**
   - Full borrower acknowledgment before signature lines.
   - One signature block each for every borrower/co-signer/guarantor.
   - Lender officer block (name/title) + date.
   - Execution language confirming borrower received complete agreement and disclosures.

```text
**Execution acknowledgment**
By signing below, I/we acknowledge... [insert exact acknowledgment language]
Borrower Signature / Printed Name / Date
Co-Borrower Signature / Printed Name / Date
Co-Signer Signature / Printed Name / Date (if any)
Lender Signature / Printed Name / Title / Date
```

7) **Run final consistency pass**
   - Reconcile every dollar and percentage across disclosure and operative clauses.
   - Verify state overlays for:
     - interest/late fee caps
     - prepayment penalty bans/restrictions
     - repossession and cure notice requirements
     - anti-waiver and unconscionability restrictions
     - deficiency judgment limitations
   - Verify all required notices are present and in prominence.

## Guidelines

1. Use plain headings and short defined terms, then define once.
2. Keep borrower-facing disclosure language identical to statutory labels to avoid ambiguity.
3. Do not let operational clauses override disclosures; define priority order.
4. Never include hidden fees, non-itemized service charges, or unilateral rights without disclosure.
5. Do not omit state-law cure/repo notices where required.
6. Never apply late fees as penalties; tie to administrative-cost rationale and lawful caps.
7. Flag unverifiable jurisdictional assumptions and request confirmatory inputs before finalizing.
8. Add `[VERIFY]` to any tolerance/wording you cannot source with certainty in the current workflow.

# Underwriting Rules: Spreading, Cash Flow, Structure and Collateral

Credit-analysis rules for the draft credit memo. Institution policy governs every threshold (minimum DSCR, maximum LTV, advance rates, amortization limits); this file says how to compute and test against it. Regulatory overlays (appraisal regulation, CRE concentrations, Regulation O, Regulation B, Section 1071, leveraged lending) are in `references/regulatory-overlays.md`.

## Contents

1. Spreading and normalization
2. Cash available for debt service and DSCR
3. Global cash flow
4. Adjustments that are not allowed
5. Structure: amount, amortization, tenor and useful life
6. Covenant levels and headroom
7. Collateral, advance rates and LTV
8. Risk rating
9. Policy tests and exceptions

## 1. Spreading and normalization

- Spread each period from the highest-ranked source: audited, then reviewed, then compiled statements, then tax returns, then company-prepared statements. Tie every spread total to the source statement (revenue, net income, total assets, total liabilities, equity) and record the difference, which should be zero.
- State the fiscal year end, the statement quality (audited, reviewed, compiled, tax return, internal) and the period length of each column. An interim period is never annualized without saying so and without a seasonality note.
- Normalization adjustments (non-recurring items, owner compensation above or below market, related-party rent at non-market terms) each get one row, a source and a reason. An adjustment is allowed only when a document shows the item and shows why it will not recur or why the market figure differs.
- Reconcile book income to the tax return (Schedule M-1 or M-3) when both exist. A large unexplained difference is a source conflict.
- Keep three EBITDA rows when they exist: reported, lender-adjusted (the institution's own normalization) and borrower or broker-adjusted. Policy tests use the lender-adjusted figure.

## 2. Cash available for debt service and DSCR

DSCR is cash available for debt service (CADS) divided by debt service. Use the institution's written definition. When the policy is silent, compute and show:

| Line | Treatment |
|---|---|
| EBITDA (lender-adjusted) | Start here, never stop here |
| Less unfinanced capital expenditures | Maintenance capex paid from cash; capex funded by a specific new loan is excluded only if that loan's debt service is in the denominator |
| Less cash income taxes paid by the entity | From the tax return or cash flow statement |
| Less distributions and dividends | Including tax distributions of pass-through entities, unless the policy treats them only in global cash flow |
| = CADS | |
| Debt service | Scheduled principal and interest on all existing debt plus the proposed loan, annualized; capital lease payments; for interest-only periods show both the interest-only and the amortizing case |

Rules:
- An EBITDA-only DSCR may appear only as a labelled secondary figure. Never test policy on it unless the written policy says EBITDA is the numerator.
- Debt service for the proposed loan is computed from amount, rate, amortization and payment frequency by formula; show the monthly and annual figures. For floating rates, use the rate at underwriting and a stressed rate stated in the policy or the request.
- Include all debt, including shareholder loans that are being paid and debt of a co-borrower.
- Sensitivity: show DSCR at revenue down 10 percent and rate up 200 basis points (or the policy's stresses), and the break-even revenue decline.

## 3. Global cash flow

Global cash flow combines the borrower, each guarantor and each entity in which a guarantor has a material interest that the policy requires to be included (affiliates, real estate holding companies that lease to the borrower).

- Start from each entity's CADS before distributions. Do not add the distributions a guarantor receives from an entity whose cash flow is already counted: that double counts.
- Include each affiliate's net operating cash flow and each affiliate's debt service, even when the affiliate is not a party to the loan.
- Include the guarantor's personal income not already counted, less personal income taxes actually paid, less living expenses (the guarantor's stated figure, else the policy's standard figure, else an unknown fact), less personal debt service: residential mortgage, personal loans, and payments on other personal guarantees that are being called.
- Contingent liabilities (other personal guarantees, pending litigation) are listed even when not in debt service.
- Global DSCR is global cash available divided by global debt service. Policy minimums for business and global DSCR are usually different; test each against its own minimum.
- Who is in the population is a scope decision: list every entity and person included and every one excluded, with the reason.

## 4. Adjustments that are not allowed

These are declined under Ground Rule 7 and the matching hard stop, whoever asks for them:
- Adding back an expense described as one-time when the spread or the statements show it in two or more of the last three years.
- Removing unfinanced maintenance capex on the assumption that it will be financed, when no financing exists.
- Replacing historical CADS with projections to meet a historical-coverage test, unless the policy itself allows projections for that loan type, and then only with the projection's source and a historical comparison.
- Choosing the DSCR numerator, the denominator, or the population (which guarantors and affiliates count) because it produces a passing number.
- Reclassifying recurring operating costs as financing or owner costs without a document.

What the draft does instead: shows the actual figures, the policy gap in dollars of CADS and in turns, and legitimate options (lower amount, more equity, additional collateral, an additional guarantor whose own figures support it, a shorter or longer amortization within useful life, or a documented policy exception for the credit officer to accept or reject).

## 5. Structure: amount, amortization, tenor and useful life

- Amortization never exceeds the remaining economic life of the collateral financed (equipment appraisal, engineering report, vehicle age) or the policy's maximum, whichever is shorter. A balloon at maturity needs a stated refinance source and a refinance-risk test at a stressed rate.
- Maximum loan amount at a policy DSCR is computed: maximum new annual debt service = CADS / minimum DSCR - existing debt service; maximum amount = present value of that payment over the allowed amortization at the loan rate.
- Revolving lines: borrowing base with eligibility rules, advance rates from policy, an annual clean-up or a term-out if the policy requires one.
- Construction and interest-only periods: test coverage at stabilization and during interest-only periods separately.

## 6. Covenant levels and headroom

- Set each financial covenant from the base-case projection with the institution's headroom target, after testing it against the most recent actual figure.
- Headroom for a minimum ratio = (projected ratio - covenant level) / projected ratio. For a maximum ratio = (covenant level - projected ratio) / covenant level. Show the result for actual and for each projection year.
- A covenant that the borrower fails on actual figures at closing is a day-one default and is reported as such, never as headroom.
- Write the covenant definition (numerator, denominator, test period, first test date) in the memo so post-close monitoring uses the same definition. Post-close calculation and compliance certificates go to managing-debt-covenant-compliance.

## 7. Collateral, advance rates and LTV

- Advance rates come from the institution's policy. Common market ranges (receivables, inventory, equipment on orderly liquidation value) are not rules; if the policy is silent, record a policy election and do not invent a rate.
- Real estate LTV uses "value" as the supervisory LTV appendix defines it: the market value in an appraisal or evaluation that meets the agencies' appraisal regulation, and, for a purchase, the lesser of acquisition cost and that value. Compute LTV on both figures when they differ and test on the lesser.
- Value of record must come from an appraisal or evaluation the institution engaged or accepted under its regulation and reviewed before the credit decision (`references/regulatory-overlays.md`, Section 1). Any other value is shown only as "Indicative - not value of record".
- Perfection: UCC search and filing, mortgage recording, title insurance, flood determination, environmental report for real estate, assignment of leases and rents. Each is a condition precedent with an owner.

## 8. Risk rating

- Propose a rating only on the institution's written scale, citing the definition each driver meets. If the scale is not supplied, label it "Not rated - scale not supplied".
- Use separate borrower (probability of default) and facility (loss given default) ratings where the institution has a dual-rating system. A proposed rating is a draft; the credit officer assigns it.

## 9. Policy tests and exceptions

Each policy test (DSCR, global DSCR, LTV, advance rate, leverage, liquidity, amortization, guarantor support) gets one row: policy citation, required level, actual, result. Result labels and their tests are in `references/output-template.md` Section 4. An exception is never buried in narrative; it is listed with its size, mitigants and who must approve it under the policy.

---
name: building-lbo-models
language: en
description: >
  Builds and reviews leveraged buyout (LBO) models for financial sponsor acquisitions:
  sources and uses with transaction fees, financing fees, OID and cash to balance sheet;
  an EBITDA bridge reconciling reported, management-adjusted or QoE EBITDA to credit
  agreement Consolidated EBITDA; operating projections and free cash flow; a debt
  schedule by tranche with mandatory amortization, excess cash flow sweep, minimum cash,
  revolver draws and average-balance interest circularity; cash taxes with the IRC 163(j)
  business interest limit, NOL and Section 382 limits; exit scenarios; sponsor returns as
  dated IRR (XIRR) and MOIC; sensitivity tables; credit statistics and covenant headroom;
  and tie-out checks (sources equal uses, debt rolls forward, balance sheet balances,
  cash ties). Use for LBO model, leveraged buyout, paper LBO, sponsor returns, equity
  check, debt capacity, cash sweep, IRR, MOIC, private equity acquisition model, or
  reviewing a sponsor or lender model. Outputs are drafts for qualified finance review.
tags:
  - modeling
  - investment-banking
metadata:
  author: casemark
  practice_areas:
    - Investment Banking
    - Mergers and Acquisitions
    - Corporate Finance
  document_types:
    - Model
  skill_modes:
    - Modeling
---

# Building LBO Models

Builds, or reviews, a leveraged buyout model for a financial sponsor's acquisition of a target: sources and uses, an EBITDA bridge, operating projections, a tranche-by-tranche debt schedule, a cash tax schedule, exit and sponsor returns, sensitivities, credit statistics, and a reconciliation table that proves the model ties. The deliverable follows `references/output-template.md` and ends with ranked issues, hand-offs and open items. Everything it produces is a draft for review by a qualified finance professional; it is not investment, tax, accounting or legal advice and not a lender commitment.

## Why This Skill Exists

An LBO model looks like arithmetic and fails on definitions. The equity check is a plug, so every fee left out of uses inflates the IRR. Debt is sized on the lender's EBITDA, not the seller's. The sweep, the minimum cash balance and the interest line feed each other in a loop that breaks quietly when someone pastes values. Returns are quoted on the wrong dates and exit at the entry multiple because no one chose otherwise. Tax rules for interest deductibility changed for 2022 through 2024 and changed back for years beginning after 2024. This skill forces each of those choices into the open, ties every input to a document, and proves the model balances before anyone reads the IRR.

## Where Mistakes Hide

Read each input with this suspicion before building from it.

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Management-adjusted EBITDA (CIM, management deck, QoE report) | Entry valuation and the starting point for debt sizing | Addbacks the credit agreement does not permit or caps (run-rate synergies over the cap, cost savings outside the realization window); leverage quoted on management EBITDA while the lender sizes on Consolidated EBITDA; LTM date differs from the purchase price basis |
| Credit agreement, commitment letter and fee letter | Tranches, pricing, floors, amortization, ECF sweep, covenants, OID and upfront fees | Sweep percentage and leverage step-downs misread; voluntary prepayments not credited against the sweep; sweep timing after annual financials ignored; amortization taken on the beginning balance instead of original principal; OID or flex terms left out |
| Sources and uses and the funds flow memo | Sponsor equity check | OID, financing fees, buyer advisory fees, seller expenses the buyer pays, refinancing breakage and cash to the balance sheet omitted, so the equity plug is too small; debt shown at face in sources with no OID use, or OID counted twice (net proceeds in sources and OID again in uses), so the plug is too large |
| Debt schedule and interest calculation | Interest expense, deleveraging, ending debt | Average-balance circularity broken by pasted values or iteration turned off; the sweep uses all cash above zero instead of cash above minimum cash; revolver never draws when cash falls short; floors applied to the all-in rate |
| Tax schedule | Cash taxes and levered free cash flow | Interest assumed fully deductible; the 2022-2024 EBIT-based ATI rule applied to 2025 or later years; book interest (with amortized issuance costs) used as 163(j) business interest; target NOLs used without the 80 percent and Section 382 limits; deal costs deducted in full |
| Closing date and projection calendar | Year-1 cash flow, interest and the first sweep | A mid-year close modeled with a full first fiscal year of EBITDA, free cash flow and interest, overstating year-1 deleveraging; the stub period's sweep and amortization dates not matched to the credit agreement |
| Equity documents (rollover, option pool, promote, co-invest) | Split of exit equity between sponsor and others | Management rollover, the option pool or a promote left out, so 100 percent of exit equity is counted as sponsor proceeds and IRR and MOIC are overstated; rollover counted as a source but not as a share of exit proceeds |
| Sponsor cash flow schedule and returns | IRR and MOIC | IRR computed on annual periods when close and exit are mid-year; add-on equity, dividend recaps or management dilution missing; gross and net returns mixed |
| Exit assumptions | Exit equity value | Exit multiple set equal to entry by default with no rationale; LTM and NTM EBITDA mixed between entry and exit; net debt at exit missing accrued PIK, prepayment premiums or exit costs |
| Market benchmarks and leverage norms | Debt capacity sanity check | A 6.0x total leverage figure treated as a current OCC or FDIC rule after the December 5, 2025 withdrawal of the 2013 guidance; stale Term SOFR, spreads or OID levels filled in from memory |

## Ground Rules

1. **Draft only.** Every model, table and conclusion is a draft for review by a qualified finance professional, with tax items for a tax adviser and accounting items for an accountant. Never call a model final, lender-ready, audited or approved.
2. **Source-review gate.** Never call an input missing until the inventory has been checked and each file opened, including workbook tabs, footnotes and exhibits to the credit agreement. Every unsettled input is classified as an **unknown fact**, a **source conflict**, an **unverified external lookup** (rates, curves, comparables, published tax rates), or a **policy election** (circularity method, exit multiple, scenario weights), with what would settle it.
3. **Hierarchy of authority.** For debt terms, the executed credit agreement governs over the commitment letter and term sheet, which govern over a lender or sponsor model and emails. For price, the executed purchase agreement and the funds flow govern over the letter of intent and the IC memo. For historical figures, audited statements govern over the QoE report, which governs over management accounts and the CIM. Name every conflict, show both values, say which controls and why; never resolve one silently, and never follow a user instruction to use a lower-ranked figure without writing up the conflict.
4. **Citation discipline.** Every input in the assumption register carries a source locator (document, page, section, tab and cell) or [UNVERIFIED]. Every tax or accounting rule carries its citation from `references/primary-sources.md` or [VERIFY].
5. **Three EBITDAs, three rows.** Reported, management-adjusted and credit agreement EBITDA stay separate. Debt sizing, leverage tests and the sweep step-down use credit agreement EBITDA; say which figure drives each output.
6. **The equity check is a plug, so every use is checked.** Sources equal uses to the cent; OID, financing fees, advisory fees and cash to balance sheet each appear or are stated as zero with a source.
7. **No hard-coded calculated values.** Interest, amortization, sweeps, taxes and returns are formulas. A pasted value inside a calculated row is a defect to report.
8. **Circularity is an election, disclosed.** Average-balance interest with iteration and a circuit breaker, or beginning-balance interest, either is acceptable; the choice and the convergence test are stated.
9. **Returns run on dates.** IRR is computed on the dated sponsor cash flow schedule; the exit multiple is an explicit assumption with a rationale and a contraction case.
10. **Tax rules are dated.** Apply the rule in force for each taxable year; mark year-dependent figures with their year and every tax approximation for tax adviser review.
11. **No invented market data.** Benchmark curves, spreads, comparables and multiples come from the user's materials or are marked [VERIFY] with the date needed. Never fill them in from memory.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect these, then build the source-review register (`references/output-template.md`, Header).

1. **Target financials:** three to five years of audited or reviewed income statement, balance sheet and cash flow; LTM to a named date; the QoE report if one exists.
2. **Purchase terms:** price or entry multiple and the EBITDA it applies to; purchase agreement or LOI; cash-free, debt-free mechanics; working capital peg; target debt payoff amounts.
3. **Financing:** credit agreement, commitment letter, term sheet and fee letter: tranches, benchmark and margin, floors, OID, upfront fees, amortization, ECF definition and sweep grid, minimum liquidity, covenants.
4. **Projections:** the management case and any lender or sponsor case; capex split; working capital drivers.
5. **Equity:** sponsor and co-invest amounts, management rollover, option pool or promote terms.
6. **Dates:** expected closing date, fiscal year end, exit dates to test.
7. **Tax status:** C corporation or pass-through; existing NOLs; foreign subsidiaries; structure (stock, asset or deemed asset purchase).
8. **Deliverable:** new model, review of a supplied model, or a paper LBO (quick approximation).

**Default fallbacks (each stated in the assumption register as a policy election or unknown fact):** fees as a percent of the relevant amount with [UNVERIFIED]; minimum cash at the level in the commitment papers, otherwise a stated figure; beginning-balance interest if the user does not want circularity; exit multiple equal to entry only as one case among several, never alone; mid-year or year-end convention stated; base-case tax at 21 percent federal with state taxes [VERIFY].

**Hard stops (do not produce returns; report what is needed):**
- No historical or LTM EBITDA from any source, so no entry value or leverage can be computed.
- The request is to present the model as final, audited, lender-approved or ready to send to investors as fact.
- The request is to back-solve historical figures, addbacks or the credit agreement definition to reach a target IRR or leverage.
- The debt terms the user supplies contradict an executed credit agreement in the file, and the user directs the agreement be ignored without a written conflict note.

## Step 1: Inventory and Assumption Register

Build the source-review register and assumption register in the layouts in `references/output-template.md`. Open every file; read the credit agreement's definitions article (Consolidated EBITDA, Excess Cash Flow, Indebtedness, Consolidated Total Net Leverage) and its prepayment section in full. Classify every gap. For a review of a supplied model, also trace each input cell to a source and list hard-coded values in calculated rows.

## Step 2: EBITDA Bridge and Entry Valuation

Read `references/model-mechanics.md` Sections 1 and 2. Build the bridge from reported EBITDA to management-adjusted and to credit agreement EBITDA, one addback per row, applying every cap and its base. Compute entry enterprise value on the stated EBITDA and bridge to equity purchase price with the purchase agreement's mechanics. State leverage at close on credit agreement EBITDA and the dollar and turns difference from management EBITDA.

## Step 3: Sources and Uses

Read `references/model-mechanics.md` Section 3 and `references/tax-and-accounting-rules.md` Sections 7 and 8. List every use, including OID (or net proceeds), financing fees, advisory fees, seller expenses paid by the buyer, refinancing payoff with breakage, and cash to the balance sheet. Solve the sponsor equity plug. Run checks R1 and R2. Record the GAAP and tax treatment of each fee for the opening balance sheet and tax schedule.

## Step 4: Operating Model and Free Cash Flow

Read `references/model-mechanics.md` Section 4. Set the projection calendar from the closing date, with a stub period for a mid-year close. Project revenue, EBITDA, capex and working capital by driver. Build the three statements where the deliverable is a full model; a paper LBO may skip the balance sheet but must say so and mark R4 "Not built". Separate non-cash interest from cash interest.

## Step 5: Debt Schedule, Sweep and Circularity

Read `references/model-mechanics.md` Sections 5 to 7. Build each tranche's roll-forward with amortization on the agreement's basis, the benchmark plus margin with floors, commitment fees, and PIK. Compute excess cash flow by the agreement's definition, apply the sweep percentage and step-downs, credit voluntary prepayments, and protect minimum cash; draw the revolver when cash falls short. State the circularity election and test convergence. Run checks R3, R5 to R8.

## Step 6: Tax Schedule

Read `references/tax-and-accounting-rules.md` Sections 1 to 6 and 9. Compute cash taxes by taxable year: the 163(j) limit using the ATI rule for that year, business interest from stated interest plus OID accrual (not book interest), the debt issuance cost deduction outside the limit but inside ATI, the carryforward roll (R13), NOL usage with the 80 percent and Section 382 limits, and tax depreciation. Mark each line as an approximation for tax adviser review and hand the structure questions to the M&A tax skill.

## Step 7: Exit and Returns

Read `references/model-mechanics.md` Section 8. For each exit date, compute exit EV on a stated multiple with its rationale, deduct net debt at exit from the debt schedule (R10) and exit costs, then allocate exit equity to rollover, co-investors and the option pool or promote per the equity documents before counting sponsor proceeds. Build the dated sponsor cash flow schedule, including add-on contributions and interim distributions, and compute IRR on dates (XIRR) and MOIC (R11). Report the holding period in years and state that returns are gross unless net was modeled.

## Step 8: Sensitivities, Scenarios and Credit Statistics

Read `references/model-mechanics.md` Section 9. Produce the two-way tables, the scenario table (base, management, lender, downside) and annual credit statistics against the credit agreement's covenant levels, not market norms. Confirm one data-table cell against a manual rerun.

## Step 9: Reconcile, Rank Issues and Hand Off

Complete the reconciliation table in `references/output-template.md` Section 10; every Fail or Not built row becomes an issue. Rank issues by the template's severity rule, each with sources in conflict, the controlling source, the effect on equity check, IRR or leverage, and a recommendation. Write complete hand-offs (Section 12) and the open items and [VERIFY] list (Section 13).

## Checkpoint B: Post-Draft Alignment

Before the Quality Audit, re-read the request and confirm:
- The deliverable type matches the request (new model, review, or paper LBO) and the scope limits are stated.
- The returns answer the question asked (bid level, hurdle test, or range) and the hurdle the user named is compared with the dated IRR and MOIC.
- Every conflict the user's instructions created with a higher-ranked document is written up, not followed silently.
- Nothing is presented as a recommendation to invest or lend; the closing line from the template is present.

## Quality Audit

Confirm each statement is true of the draft; fix the draft if one is not.

1. Sources equal uses to the cent, and OID, financing fees, advisory fees and cash to balance sheet each appear or are stated as zero with a source.
2. Reported, management-adjusted and credit agreement EBITDA appear as separate rows, every cap in the definition is applied with its base, and debt sizing and leverage use credit agreement EBITDA.
3. Each tranche rolls forward period to period (R3) and mandatory amortization uses the agreement's basis.
4. The sweep uses the agreement's ECF definition, percentage and step-downs, credits voluntary prepayments, and never takes cash below minimum cash; the revolver draws when needed.
5. The circularity election is stated and converged, or beginning-balance interest is disclosed; no pasted values sit in calculated rows.
6. The balance sheet balances and cash ties across all three statements every period (R4, R5), or the model is labeled a paper LBO with R4 marked Not built.
7. The 163(j) computation uses the ATI rule for each taxable year and tax interest rather than book interest, deducts debt issuance costs outside the limit, and its carryforward rolls (R13).
8. NOL usage respects the 80 percent limit and any Section 382 limit, or is marked [VERIFY] for the tax adviser.
9. IRR is computed on dated cash flows that include every contribution and distribution, sponsor proceeds exclude rollover, co-invest and option pool shares, year 1 reflects any stub period, and MOIC equals distributions over contributions.
10. The exit multiple has a rationale and at least one contraction case; entry equals exit only as a labeled case.
11. Every input has a source locator or [UNVERIFIED]; every rule has a citation or [VERIFY]; no market rate or multiple was supplied from memory.
12. Every conflict names both sources, the controlling one and the effect; every open item has an owner and next action.
13. The draft-for-review closing line is present and no statement calls the model final or lender-ready.

## Guidelines

- Work in the units of the source documents and state them once; never mix thousands and millions.
- Prefer the structure of a model the user supplies; flag defects rather than rebuilding unasked.
- Keep the model's color or labeling convention for inputs versus formulas when building a spreadsheet, and put every input on the assumption sheet.
- Present downside cases with the same care as the base case; liquidity and covenant headroom in the downside are part of the answer.
- Quote ranges for anything that depends on a policy election rather than one point estimate.
- Do not opine on whether the sponsor should bid or the lender should lend; present returns, risks and sensitivities for the decision-maker.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Sources do not equal uses by a round amount | OID or a fee omitted, or debt at face with no OID use | Walk the uses checklist in `references/model-mechanics.md` Section 3 |
| Debt balance goes negative or the sweep exceeds cash | Sweep not capped at outstanding balance or ignores minimum cash | Cap each payment at the balance; sweep only cash above minimum |
| Iteration returns errors or does not converge | An error value circulating in the loop | Turn on the circuit breaker, clear the error, recalculate, then turn it off |
| Balance sheet off by the amount of fees | Fees expensed in the income statement but capitalized in the opening balance sheet, or the reverse | Apply `references/tax-and-accounting-rules.md` Section 8 consistently |
| Credit agreement is a scan or only a term sheet is available | Definitions unreadable or not yet final | Attempt extraction; if unreadable, record it, use the term sheet with [UNVERIFIED], and list the dependent outputs |
| Supplied model and credit agreement disagree on a term | Model built on a superseded draft | Use the executed agreement; write up the conflict and the effect on returns |
| QoE and CIM EBITDA differ | Different periods or addbacks | Bridge both to reported EBITDA and to credit agreement EBITDA; name the period of each |
| Tax rate or threshold looks stale | Year-dependent figure | Check `references/primary-sources.md`; mark [VERIFY] with the year needed |

## Related Skills

- analyzing-m-and-a-tax-implications: structure (stock, asset, 338 elections), basis step-up, 163(j), Section 382, AHYDO and deal-cost deductibility conclusions.
- analyzing-earnings-quality: addbacks or accruals that the QoE report or statements do not support.
- managing-debt-covenant-compliance: ongoing covenant calculations and compliance certificates after close.
- analyzing-covenant-compliance: covenant headroom, cure rights and default triggers in a stressed case.
- structuring-debt-financing: designing the capital structure and negotiating terms before commitment papers exist.
- analyzing-leveraged-loans: loan market terms, repricing and amendment analysis for the tranches.
- managing-interest-rate-hedging: swaps, caps or collars on floating-rate tranches.
- building-equity-valuation-models: DCF and comparables used to support the exit multiple.
- building-merger-models: strategic acquirer accretion and dilution instead of sponsor returns.
- modeling-portfolio-company-returns: value creation attribution and fund-level returns after the deal.
- writing-investment-committee-memos: turning the model's outputs into an IC recommendation.

## Reference Files

- `references/model-mechanics.md`: EBITDA bridge, purchase price, sources and uses, projections, debt schedule, sweep and minimum cash, circularity, exit and returns, sensitivities and credit statistics.
- `references/tax-and-accounting-rules.md`: corporate rate, IRC 163(j), definition of interest, OID and AHYDO, NOLs and Section 382, bonus depreciation, deal-cost tax and GAAP treatment.
- `references/output-template.md`: deliverable sections, assumption register, reconciliation checks R1 to R13, issue severity, hand-off table.
- `references/primary-sources.md`: each authority checked with citation and date, and the [VERIFY] list.

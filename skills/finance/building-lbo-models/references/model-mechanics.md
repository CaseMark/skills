# LBO Model Mechanics

Construction rules for each schedule of the model. Read the section named in the SKILL.md step before building that schedule. Contract terms (EBITDA definition, sweep percentages, amortization, floors, fees) always come from the executed credit agreement or commitment papers; the numbers below are illustrations or common market patterns, never defaults to apply silently.

## Contents

1. EBITDA bridge: three definitions kept apart
2. Entry valuation and purchase price
3. Sources and uses
4. Operating model and free cash flow
5. Debt schedule
6. Excess cash flow sweep and minimum cash
7. Interest circularity
8. Exit and sponsor returns
9. Sensitivities, scenarios and credit statistics

## 1. EBITDA bridge: three definitions kept apart

Every LBO carries at least three EBITDA figures. Keep each in its own labeled row and never let one stand in for another.

| Definition | Source | Used for |
|---|---|---|
| Reported EBITDA | Audited or reviewed financial statements: operating income plus D&A, each line tied to a statement page | Starting point; tax model; audit trail |
| Management-adjusted (or QoE-adjusted) EBITDA | CIM, management presentation, quality-of-earnings report | Purchase price negotiation; sponsor's valuation view |
| Credit agreement EBITDA ("Consolidated EBITDA") | The definitions article of the executed credit agreement or the commitment papers' term sheet | Debt sizing at the lender's multiple, leverage-based pricing grids, sweep step-downs, financial covenants |

Bridge rules:
- Walk from reported to each adjusted figure one addback at a time, with the amount, the source locator and whether the credit agreement permits it.
- Apply every cap in the definition. Run-rate cost savings and synergies are commonly capped as a percentage of EBITDA, limited to actions taken or expected within a stated period, and sometimes require an officer's certificate. Read whether the cap base is EBITDA before or after the capped addbacks; the answer changes the number.
- An addback in the QoE report that the credit agreement does not list is excluded from credit agreement EBITDA until counsel or the lender confirms otherwise. Record it as a source conflict.
- State the period: LTM to a named date, fiscal year, or pro forma for an acquisition. Leverage at close and exit valuation must use the same period convention the source uses (LTM versus NTM).

## 2. Entry valuation and purchase price

- Entry enterprise value is the entry multiple times the named EBITDA definition. Say which definition; a multiple applied to management-adjusted EBITDA is not comparable to one applied to reported EBITDA.
- Bridge enterprise value to equity purchase price with the executed purchase agreement's mechanics: cash-free, debt-free; indebtedness and debt-like items as the agreement defines them; seller transaction expenses; the working capital adjustment against the peg; escrows and earn-outs. A letter of intent is a lower-ranked source than the executed agreement.
- Refinanced target debt appears in uses at the payoff amount in the payoff letter, including breakage, prepayment premium and accrued interest.

## 3. Sources and uses

Sources must equal uses to the cent. The sponsor equity line is the plug, so every omitted use understates the equity check and overstates IRR.

| Uses (check each) | Sources (check each) |
|---|---|
| Equity purchase price paid to sellers | Revolver drawn at close (often zero) |
| Refinanced target debt (payoff letter amount) | Each term loan tranche at face (principal) |
| Seller transaction expenses the buyer pays | Senior or subordinated notes at face |
| Buyer M&A advisory, legal, accounting, diligence fees | Seller note or earn-out financing |
| Financing fees (arrangement, underwriting, upfront) | Management rollover equity |
| Original issue discount, when debt is shown at face in sources | Sponsor equity (plug) |
| Cash funded to the balance sheet (minimum operating cash) | Co-investor equity |

OID presentation: either show debt at face in sources and OID as a use, or show net proceeds in sources. Never show face in sources and omit the OID; that is a funding gap equal to the discount. Never show net proceeds in sources and OID again in uses; that double counts the discount and overstates the equity check by the same amount. Fee letters often allow the arrangers to increase OID or margin ("flex"); model the flexed terms as a downside case.

Accounting treatment differs from cash treatment and drives the opening balance sheet (`tax-and-accounting-rules.md` covers the citations): acquisition-related advisory costs are expensed by the acquirer, debt issuance costs and OID reduce the carrying amount of the term debt and amortize to interest expense, revolver costs may be carried as an asset, and equity issuance costs reduce equity. The tax treatment of each fee is separate again.

## 4. Operating model and free cash flow

- Set the projection calendar from the closing date. For a mid-year close, model a stub period from closing to the first fiscal year end with only the stub's share of EBITDA, free cash flow, interest and amortization (or state the full-year simplification and its effect); align the first sweep and amortization dates with the credit agreement.
- Project revenue by driver where the data supports it (volume and price, segments); EBITDA by margin or cost build.
- Working capital from days metrics (DSO, DIO, DPO) on historical averages, not a flat percent of revenue, unless the data does not support days.
- Separate maintenance capex from growth capex.
- Unlevered free cash flow: EBITDA less cash taxes (unlevered), less capex, less increase in net working capital. Levered free cash flow for debt service: EBITDA less cash interest, less cash taxes (levered, after the interest limitation), less capex, less change in working capital, less other cash items in the credit agreement's ECF definition.
- Non-cash interest (amortization of OID and debt issuance costs, PIK accrual) is added back in the cash flow statement; PIK increases the tranche balance.

## 5. Debt schedule

Per tranche, per period:

```
Beginning balance
+ Draws (revolver only) and PIK accrual
- Mandatory amortization (scheduled; often a percent of original principal per year for term loan B)
- Excess cash flow sweep (Section 6)
- Optional prepayments
= Ending balance
```

- Mandatory amortization is set by the credit agreement schedule; it is a percent of original principal, not of the beginning balance, unless the agreement says otherwise. Cap it at the outstanding balance.
- Prepayment waterfall order (which tranche receives the sweep, pro rata or by maturity) comes from the agreement.
- Floating rate: the benchmark (for example Term SOFR for the stated tenor) plus margin, subject to any floor. A floor applies to the benchmark, not the all-in rate, unless the agreement says otherwise. Use the forward curve the user supplies or mark the rate assumption [VERIFY]; never fill in a market rate from memory.
- Revolver: draws whenever cash before revolver falls below minimum cash; repays first when cash is available; commitment fee on the undrawn amount.
- Fixed-rate notes typically have no amortization and call protection; model any make-whole or call premium on early repayment.
- Leverage-based margin step-downs depend on the credit agreement EBITDA, not management EBITDA.

## 6. Excess cash flow sweep and minimum cash

- Compute excess cash flow exactly as the credit agreement defines it (typically net income or EBITDA based, less cash interest, mandatory and certain voluntary prepayments, capex and working capital increases, plus or minus listed items).
- Apply the sweep percentage and any leverage-based step-downs (for example a lower percentage once net leverage falls below a stated level); read the percentages from the agreement.
- Deduct voluntary prepayments that the agreement credits against the sweep, so cash is not counted twice.
- Timing: agreements usually require payment after annual financial statements are delivered, so the sweep for fiscal year N often reduces debt in year N+1. Modeling it at year-end N is a simplification; say so.
- Minimum cash: the sweep and optional prepayments use only cash above the minimum operating cash balance. A sweep formula that uses all cash above zero, or a minimum cash balance that the sweep ignores, is the common break. Cash after sweep must equal or exceed minimum cash in every period; if it does not, the revolver draws.

## 7. Interest circularity

Interest on average balances depends on ending balances; ending balances depend on the sweep; the sweep depends on cash after interest. This is a true circular reference.

Acceptable treatments (state which one the model uses):
1. **Iterative calculation** in the spreadsheet, with a circuit-breaker switch that sets interest to beginning-balance interest when on, so a single error does not propagate. Excel's default iteration settings stop after 100 iterations or when values change by less than 0.001; tighten Maximum Change for large models and confirm convergence by comparing two successive runs.
2. **Beginning-balance interest** (no circularity). Simpler, slightly overstates interest when debt is falling. Disclose the election.
3. **Closed-form or copy-paste macro** solution. Acceptable only if the values are recomputed on every change; a pasted value that no longer ties to the balances is a broken model.

Check: interest in each period equals rate times the balance basis stated, recomputed outside the model for at least one period per tranche.

## 8. Exit and sponsor returns

- Exit enterprise value: exit multiple times the stated EBITDA (say LTM or NTM). The exit multiple is an explicit assumption with a rationale (current trading and transaction comparables, growth and margin at exit, entry multiple and the market at entry). Setting exit equal to entry is a choice that must be justified, never a default; show multiple contraction cases.
- Exit equity value: exit EV less net debt at exit (all tranches at principal, accrued PIK, prepayment premiums, less cash above any trapped amount), less exit transaction costs.
- Sponsor share: allocate exit equity per the equity documents. Deduct management rollover and co-investor shares pro rata to their ownership, the option pool or promote at its vesting and strike terms, and any preferred return ahead of common. Rollover equity that appears as a source at close must also take its share of exit proceeds.
- Sponsor cash flow schedule: every dated equity contribution (close, add-on acquisitions, equity cures) as negative; every dated distribution (dividend recaps, partial exits, final exit) as positive.
- IRR on actual dates: use a dated-cash-flow function (XIRR in Excel), which discounts each flow by (date minus first date)/365. Annual-period IRR assumes equal one-year spacing and misstates returns when close or exit is mid-year or when interim flows exist. State the close date and exit date used.
- MOIC: total distributions divided by total contributions. Report gross (deal-level) returns and say they are before fund fees and carried interest unless net returns were specifically modeled.
- Check: a stated MOIC and IRR must be consistent with the holding period (for example 2.0x over five years is about 14.9 percent annually).

## 9. Sensitivities, scenarios and credit statistics

- Two-way tables at minimum: entry multiple versus exit multiple (IRR and MOIC); exit year versus exit multiple; leverage versus EBITDA growth. Data tables recompute the whole model, so they inherit any circularity; confirm a table cell against a manual rerun.
- Scenarios: base, management, lender (bank) case and downside. The downside should stress revenue, margin and rates together and test minimum liquidity and covenant headroom. Illustrative stresses, to be replaced by the user's or the lender's case where one exists: revenue 10 to 20 percent below base, EBITDA margin 100 to 300 basis points lower, benchmark rate higher, exit one year later.
- Solve the breakeven entry multiple (or maximum bid) at which the sponsor's stated hurdle IRR and MOIC are just met, holding financing constant, and say how financing would change at that price.
- Where a dividend recap or partial exit is modeled, show returns with and without it.
- Credit statistics each year: total and senior leverage on credit agreement EBITDA (gross and net as defined), interest coverage, fixed charge coverage, free cash flow to debt, cumulative debt paydown. Compare with the agreement's covenant levels, not with general market norms.

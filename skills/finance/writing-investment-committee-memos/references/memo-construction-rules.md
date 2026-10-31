# Memo Construction Rules

Rules for turning model outputs, diligence reports and deal documents into the analytical sections of an IC memo. Formulas are stated so every memo figure can be recomputed. Legal and regulatory points are in `references/regulatory-and-disclosure.md`.

## Contents

1. Returns: IRR, MOIC and the dated cash flow schedule
2. Cases: management, sponsor, downside, exit at entry
3. Value-creation bridge and exit multiple support
4. Thesis pillars and falsifiable KPIs
5. Comparables selection protocol
6. Financing alignment with commitment papers
7. Risk matrix scales
8. Diligence status and findings
9. Strategy-specific adjustments: growth, credit, real estate

## 1. Returns: IRR, MOIC and the dated cash flow schedule

- **Source.** Every returns figure comes from the model's sponsor (or fund) cash flow schedule for a named version and date. The memo restates; it does not recompute a different number unless the reconciliation shows the model is wrong, and then it reports both.
- **IRR on dates.** IRR is the rate that sets the net present value of dated cash flows to zero, discounting each flow by (1 + r) raised to (days from the first flow / 365): the XIRR convention, confirmed by building-lbo-models. An IRR computed on fiscal-year columns treats a March close and a September exit as whole years apart and misstates the return; replace it with the dated figure and show the difference.
- **Every flow counts.** Include add-on equity, follow-on investments, dividend recaps, interim distributions and fees paid by the fund in the deal (if the case is net). Sponsor proceeds exclude management rollover, the option pool or management incentive plan (at the vesting and hurdle terms that apply in each case) and co-investor shares.
- **Tax leakage.** State whether returns are before or after taxes between the company and the fund's investors: blocker-level tax, withholding on distributions and transfer taxes. If leakage differs by investor type, say so rather than quoting one figure. The memo reports the structure memo's conclusions; acquisition structure and deal withholding go to analyzing-m-and-a-tax-implications and cross-border withholding to analyzing-international-tax-planning.
- **MOIC** = total distributions (realized plus remaining value at exit) / total contributions. A MOIC that divides by the initial check alone, when later contributions exist, is overstated.
- **Holding period** in years = (exit date - first contribution date) / 365; state it next to every IRR.
- **Gross or net.** Deal-level returns are gross of fund management fees, fund expenses and carried interest unless the model computes net. Say which on every returns line. Do not label a gross figure "net" or leave it unlabeled. This internal default does not carry over to any version for investors: there the Marketing Rule requires net with gross (see `references/regulatory-and-disclosure.md` Section 6).
- **Subscription line.** If the fund bridges the equity with a capital call facility, the deal IRR from the fund's perspective differs from the IRR on the LP capital-call dates. State which dates are used.
- **Tolerance.** Memo IRR within 0.1 percentage point and MOIC within 0.01x of the model; any larger gap is check M1 or M2 failing.

## 2. Cases: management, sponsor, downside, exit at entry

| Case | What it is | Rule |
|---|---|---|
| Management case | Projections from the company or seller (CIM, management model) | Shown for reference and labeled as such; never called the base case |
| Sponsor case (base) | The deal team's own view after diligence haircuts | The case the recommendation rests on; each change from the management case listed with its diligence source |
| Downside case | A plausible adverse case tied to the top risks in the matrix | Shows MOIC, IRR, minimum liquidity and covenant headroom; says what breaks first (covenant, liquidity, principal loss) |
| Exit at entry | Sponsor case EBITDA at the entry multiple | Always shown when the sponsor case exits above entry |
| Upside | Optional | Never the only case above the sponsor case's returns hurdle |

If the model has only a management case, the memo shows it labeled "Management case", records "Sponsor case: Not modeled" and "Downside case: Not modeled" as Critical issues with the model owner, and does not invent either case by hand. Alternative exit multiples may be computed from the model's own exit EBITDA and net debt (exit equity = exit EBITDA x multiple - net debt at exit - exit costs), labeled "computed from model outputs".

**Hurdles.** When a case falls below the IC hurdle, the memo says so. It may show the breakeven input (for example, the exit multiple at which the IRR reaches the hurdle) as a labeled sensitivity. It never moves the case's own input to clear the hurdle.

## 3. Value-creation bridge and exit multiple support

Equity gain = exit equity + interim distributions - total contributions. Split it:

- EBITDA growth = (exit EBITDA - entry EBITDA) x entry multiple
- Multiple change = (exit multiple - entry multiple) x exit EBITDA
- Net debt reduction = net debt at close - net debt at exit (adjust for add-on equity and recaps so the total ties)
- Interim distributions and other items, each named

The four components must sum to the equity gain (check M6). Report multiple change as a share of the gain. Multiple expansion is a market outcome, not a lever the deal team controls; it is shown separately and not counted as a thesis pillar.

An exit multiple above the entry multiple needs a documented reason tied to the business at exit (mix shift to a higher-multiple segment, scale crossing a buyer-universe threshold, de-risking such as reduced customer concentration) with evidence such as comparables for that profile. "Comparables trade higher today" supports the entry price, not an exit five years out. Without support, the sponsor case exits at or below entry, and a contraction case (at least one turn below entry, or the low end of the cycle range from the comparables) is shown.

## 4. Thesis pillars and falsifiable KPIs

Each pillar states: the KPI (a number the company reports or the deal team can measure), the baseline with date and source, the sponsor-case target with date, the disconfirming result (the level at which the pillar has failed) and the trigger date to test it, the dollar value it contributes to the bridge, and the owner. "Pricing power", "best-in-class management" or "platform for M&A" without these is a theme, not a thesis. Hand KPI tracking after close to managing-value-creation-plans.

## 5. Comparables selection protocol

1. Write the selection criteria (sector, size band, growth, margin, geography, date window for transactions, control or minority) before looking at multiples.
2. List the full candidate set that meets the criteria, with source and date.
3. Exclude only for a stated reason unrelated to the multiple (data unavailable, distressed sale, different business mix). Excluding the lowest multiples without a reason is a Critical issue.
4. Report median, mean, range and interquartile range for the full set and the selected set, on one basis (LTM or NTM), and place the entry multiple in each.
5. Precedent transactions carry their date; a multiple from a different rate or credit environment is labeled with its year.
6. No comparable or multiple is supplied from memory; take it from the user's materials or mark it [VERIFY].

## 6. Financing alignment with commitment papers

- The executed commitment letter, term sheet and fee letter govern over a banker's indication, a model assumption or the memo text.
- Match each tranche: amount, OID, margin and floor, upfront and ticking fees, amortization, maturity, call protection, covenants, sweep, flex (pricing and structure), conditions and expiry. A memo that assumes leverage or pricing better than the papers is check M5 failing.
- State commitment status: committed (signed), highly confident, indicative, or none. Returns resting on uncommitted financing say so in the executive summary.
- Run the returns at full flex if the papers permit flex, and state the change in IRR.
- Leverage at close is stated on the credit agreement's EBITDA definition, not management-adjusted EBITDA. Bank leverage norms are not a regulatory cap: the OCC and FDIC withdrew the 2013 leveraged lending guidance on December 5, 2025 (confirmed by building-lbo-models).

## 7. Risk matrix scales

- **Probability**: High (more likely than not within the hold, or already occurring), Medium (plausible, has occurred at peers), Low (remote but material if it occurs). State the basis.
- **Impact**: in dollars or in IRR and MOIC points, tied to the downside case or a named sensitivity. "Significant" is not an impact.
- **Mitigant**: a mechanism with an owner: contractual (indemnity with cap, basket and survival; escrow; price adjustment), insurance (policy and exclusions; R&W policies commonly exclude matters known to the buyer, so read the binder's exclusions rather than assuming cover [VERIFY]), structural (covenant, preferred terms), operational (plan, owner, date).
- **Residual**: what remains after the mitigant, in the same units as the impact.
- Every risk raised in diligence reports or by IC members in prior meetings appears, or is listed in the issues log with the reason it was judged immaterial and who judged it.

## 8. Diligence status and findings

Use the status labels from `references/output-template.md` Section 8 verbatim. Report each finding as the report states it, with the report's own quantification (range, not midpoint alone). A finding may be judged immaterial only with a stated reason and the name of the person who judged it, and it still appears in the diligence table. Earnings adjustments, addbacks and QoE disputes route to analyzing-earnings-quality; the memo reports the conclusion and its source.

## 9. Strategy-specific adjustments: growth, credit, real estate

- **Growth equity (minority, little or no leverage).** Returns depend on ownership after dilution, liquidation preference and participation, anti-dilution, and exit route. Show returns at the preference (downside) and as-converted (upside), and the protective provisions. Hand capitalization-table modeling to modeling-cap-table-scenarios.
- **Private credit.** The memo's returns are yield to maturity and to expected call, with OID and fees; MOIC and IRR from the lender's dated flows. Downside is default and recovery: loan-to-value at entry on a stated enterprise value, recovery by waterfall position, covenant package and headroom. Cases still distinguish the borrower's case from the lender's case. A bank credit approval package is a different deliverable (managing-credit-approval-packages).
- **Real estate.** The exit multiple analog is the exit cap rate: an exit cap rate below the going-in cap rate needs the same support as multiple expansion. Show NOI from the rent roll, debt service coverage, debt yield, and loan-to-value at entry and exit; tie lease-up and rent growth to the pro forma (building-real-estate-pro-formas).

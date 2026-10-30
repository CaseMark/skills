# Valuation Mechanics

Construction and review rules for each part of an equity valuation model. Read the section named in the SKILL.md step before building or reviewing that part. Formulas are standard practice; market inputs (risk-free rate, equity risk premium, betas, multiples, spreads) always come from the user's materials or a dated source and are never filled in from memory.

## Contents

1. Cash flow type and the matching discount rate
2. Unlevered free cash flow build and stock-based compensation
3. WACC: unlevering and relevering beta, weights, cost of debt
4. Discounting calendar: valuation date, stub period, mid-year convention
5. Terminal value: Gordon growth, exit multiple and the cross-check
6. Enterprise value to equity value bridge
7. Fully diluted shares: treasury stock method and convertibles
8. Trading comparables
9. Precedent transactions and control premiums
10. Weighting, the football field and sensitivities

## 1. Cash flow type and the matching discount rate

| Cash flow discounted | Discount rate | Result | Then |
|---|---|---|---|
| Unlevered free cash flow (to all capital providers, before interest) | WACC | Enterprise value | Deduct debt and other non-common claims, add non-operating assets |
| Free cash flow to equity (after interest, net borrowing) | Cost of equity at the leverage the forecast assumes | Equity value | No net debt deduction; add only non-operating assets not in FCFE |

- Unlevered cash flow discounted at the cost of equity understates value (the rate carries financial risk the cash flow does not bear); levered cash flow discounted at WACC overstates it. IVS 103 Appendix A20.05 and A20.30 require the discount rate to be consistent with the type of cash flow.
- Taxes in unlevered cash flow are on EBIT (operating taxes), not on pre-tax income after interest; the interest tax shield lives in the after-tax cost of debt.
- Nominal cash flows take a nominal rate; real cash flows a real rate. Currency of the cash flow and of the risk-free rate must match.

## 2. Unlevered free cash flow build and stock-based compensation

UFCF = EBIT x (1 - operating tax rate) + D&A - capital expenditures - increase in net working capital (+/- other operating non-cash items stated one per row).

- Start from reported EBIT tied to the statements; show each normalization (non-recurring items, owner compensation for a private company) as its own row with its source.
- Under US GAAP, operating lease cost is a single straight-line lease cost in operating expense (ASC 842-20-25-6), so EBITDA and UFCF are after operating lease cost; finance lease cost is ROU amortization plus interest (ASC 842-20-25-5), so it sits below EBITDA. Under IFRS 16 the lessee presents interest on the lease liability separately from depreciation (IFRS 16.49), so IFRS EBITDA is before lease cost. Section 6 sets the matching bridge treatment.
- Stock-based compensation (SBC). Choose one treatment and state it as a policy election:
  - Default: treat SBC as an operating expense (no add-back) and count only securities outstanding at the valuation date in the share count (Section 7).
  - Alternative: add SBC back as non-cash and model the future share issuance it implies (projected grants diluting the share count or a cash-equivalent deduction).
  - Never both add SBC back and ignore future grants: that values the employee compensation as free. Report the value difference between the two treatments when the add-back is found.

## 3. WACC: unlevering and relevering beta, weights, cost of debt

- Cost of equity (CAPM) = risk-free rate + levered beta x equity risk premium (+ any size or company-specific premium, each stated with its source and marked as a judgment).
- Peer betas reflect each peer's own leverage. Unlever each peer beta, take the median or mean of unlevered betas, then relever at the subject's capital structure. Hamada form with debt beta zero (state it as the election):
  - Unlevered beta = levered beta / (1 + (1 - t) x D/E)
  - Relevered beta = unlevered beta x (1 + (1 - t) x D/E of the subject)
- The D/E used to relever is the same capital structure used for the WACC weights. For fair value or fair market value that is a market participant or industry structure; for investment value it may be the owner's planned structure. Say which.
- Weights at market value (or the target structure), not book. D/V and E/V sum to 100 percent.
- Pre-tax cost of debt is the current yield the subject would pay (rating, spread or observed yield), not the historical coupon. After-tax cost of debt = pre-tax cost x (1 - marginal tax rate). The US federal corporate rate is 21 percent under IRC 11(b) (confirmed in the sibling skill building-lbo-models); add state and foreign taxes from the user's facts.
- Risk-free rate and equity risk premium are dated market inputs: take them from the user's materials with the date and source, or mark [VERIFY] with the date needed.

## 4. Discounting calendar: valuation date, stub period, mid-year convention

- The valuation date sets time zero. Net debt and share count are measured at the same date (Section 6).
- End-of-period convention: year i discounted at t = i.
- Mid-year convention (cash flows arrive evenly): full year i discounted at t = i - 0.5.
- Stub period of length s (fraction of a year from the valuation date to the first fiscal year end): include only the cash flow for the stub (not the full fiscal year), discount it at s/2 (mid-period) or s (end-period); later full years at s + (i - 1) + 0.5 (mid-period) or s + i (end-period), where i counts full years after the stub.
- Terminal value timing is an election to state: an exit-multiple terminal value is a point-in-time price at the end of the final year (discount at s + N with N full years after the stub); a Gordon growth value built on mid-year flows is commonly discounted with the same half-year shift as the final year's flow. Use one convention throughout and show it.
- Common errors: using 0.5, 1.5, 2.5 when a stub exists; counting the whole first fiscal year's cash flow when part of it was earned before the valuation date (and is already in the balance sheet cash).

## 5. Terminal value: Gordon growth, exit multiple and the cross-check

- Gordon growth: TV(N) = UFCF(N+1) / (WACC - g) = UFCF(N) x (1 + g) / (WACC - g). Requires WACC > g.
- Exit multiple: TV(N) = multiple x metric in year N (state LTM or NTM at the exit date and keep it consistent with the multiple's source).
- Cross-check both ways and show the results:
  - Implied exit multiple of the Gordon value = TV(N) / EBITDA(N).
  - Implied perpetual growth of the exit multiple value: g = (TV x WACC - UFCF(N)) / (TV + UFCF(N)).
- Growth rate: a perpetual nominal growth rate above the expected long-run nominal growth of the economies where the cash flows arise implies the company eventually outgrows the economy. Use the user's long-run nominal growth assumption, with its source and date, as the ceiling for the base case; any higher rate needs a written rationale and a sensitivity.
- Normalize the terminal year: margin at a sustainable level, capital expenditure consistent with growth (capex at or above D&A when g > 0), working capital investment at the growth rate, no one-time items, tax at the long-run rate.
- Terminal value share of enterprise value = PV(TV) / EV. Above about 75 to 80 percent is a review trigger, not a rule: explain it (early-stage cash flows, short forecast) and test it with a longer explicit forecast or the cross-check.

## 6. Enterprise value to equity value bridge

Measure every item at the valuation date. A claim is deducted once; an asset is added only if its cash flows are not already in UFCF.

| Item | Treatment | Watch for |
|---|---|---|
| Debt (loans, bonds, notes, revolver drawn) | Deduct, at fair value where it differs materially from carrying amount; state which | Accrued interest; make-whole or change-of-control premiums in a sale context |
| Finance lease liabilities | Deduct (cost sits below EBITDA under ASC 842-20-25-5) | Omitted because filed under "other liabilities" |
| Operating lease liabilities (US GAAP) | Do not deduct when UFCF and multiples are after operating lease cost (ASC 842-20-25-6); deduct only on a gross basis with EBITDAR or IFRS-basis EBITDA | Deducting them and also leaving lease cost in UFCF counts the leases twice; peers reporting under IFRS 16 need restating to one basis |
| Preferred stock | Deduct at liquidation preference plus accrued unpaid dividends, or fair value; convertible preferred tested like a convertible (Section 7) | Treated as equity in the share count and also deducted |
| Noncontrolling interests | Deduct at estimated value where available; book value is a labeled fallback | Omitted although 100 percent of the subsidiary's cash flows are in UFCF |
| Unfunded pension and OPEB obligations | Deduct the deficit; after tax at the marginal rate as the default election where contributions are deductible, pre-tax as the stated alternative | Deficit deducted and deficit-funding contributions also left in UFCF |
| Cash and equivalents | Add cash that is available to the common holders | Cash trapped by exchange controls, regulatory capital, or a subsidiary with minority holders; cash needed as minimum operating cash; cash earned in a stub already counted in UFCF |
| Equity-method investments and other non-operating assets | Add at estimated value when their income is excluded from EBITDA and UFCF | Added although the income is in EBITDA |
| Other debt-like items | Deduct where they are financing in substance (deferred consideration, earn-outs, litigation settlements, asset retirement obligations, declared unpaid dividends); state each | Selective inclusion |
| Tax assets (NOLs) | Add the present value of usable tax savings only if UFCF taxes ignore them | Counted in UFCF taxes and added again |

Equity value = EV - claims above + non-operating assets. Per-share value = equity value / fully diluted shares (Section 7).

## 7. Fully diluted shares: treasury stock method and convertibles

- Start from basic shares outstanding at the latest cover-page or register date; reconcile to the valuation date.
- Options and warrants: treasury stock method. Incremental shares = in-the-money units x (1 - strike / price). ASC 260-10-45-23 applies it to diluted EPS using the average market price for the period; for valuation the price is a stated election: the implied value per share (iterate to convergence, since the price depends on the share count) for an intrinsic value, or the offer price for a transaction analysis. Out-of-the-money options add no shares.
- RSUs and PSUs: count outstanding awards as shares (no exercise proceeds) unless the user elects the ASC 260-10-45-29 assumed-proceeds approach; performance awards at the expected achievement level, stated.
- Convertibles: test both ways. If converting is worth more to the holder (conversion shares x per-share value above the claim's face or redemption amount), add the conversion shares and remove the instrument from debt; otherwise keep it as debt. Settlement terms (physical, cash, net share) change the count; read the indenture or note. ASC 260 diluted EPS applies the if-converted method; valuation follows the economic test above, stated.
- Iteration: compute per-share value, recompute TSM shares and the conversion test at that value, and repeat until the change is immaterial; report the converged value and the count by class.

## 8. Trading comparables

- Selection: same business model, end markets, scale, growth and margin profile; document inclusion and exclusion criteria and why each peer is in or out. A peer growing much faster or with structurally higher margins needs an adjustment or exclusion, stated.
- Numerator and denominator match: EV multiples (EV/Revenue, EV/EBITDA, EV/EBIT) use EV computed with the same bridge items as the subject (Section 6); equity multiples (P/E) use diluted equity value and earnings after interest.
- Period match: LTM multiples apply to the subject's LTM metric, NTM multiples to the subject's NTM metric. Calendarize peers with different fiscal year ends to the subject's period.
- Clean the metrics: remove non-recurring items consistently for peers and subject; same lease basis (US GAAP versus IFRS 16) for all.
- Trading multiples reflect minority, marketable trades in the peers' shares.

## 9. Precedent transactions and control premiums

- Transaction multiples reflect prices for controlling interests, often including buyer-specific synergies, and the market conditions at announcement; record date, consideration form, stake acquired and the metric period (LTM at announcement).
- Applying precedent multiples to a minority interest imports a control premium the holder cannot realize. Either use trading comparables for a minority interest or apply a discount for lack of control with support. IVS 103 Appendix A10.17(b) describes discounts for lack of control when guideline transaction prices reflecting control are used for a minority interest; under ASC 820 a premium or discount must be consistent with the unit of account (ASC 820-10-35-36B).
- Stale transactions (different rate environment or cycle) carry less weight; say why each is included.

## 10. Weighting, the football field and sensitivities

- Show each method's range side by side (DCF, trading comparables, precedent transactions, any market-implied analysis) with the inputs driving the range.
- Weighting is a judgment: state the weights and why. A method that does not fit the subject interest (precedents for a minority stake) gets no weight unless adjusted.
- Two-way sensitivities: WACC versus terminal growth; WACC versus exit multiple; the comps multiple range against the metric. The centre cell equals the base case.
- A market-implied (reverse DCF) analysis that solves for the growth or margin embedded in a market price is legitimate when it is labeled as such; tuning inputs to reach a predetermined value and presenting them as independent estimates is not (Checkpoint A hard stop).

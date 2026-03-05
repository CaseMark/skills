---
name: structuring-interest-rate-swaps
description: Designs IRS structures with fixed/float mechanics, day count conventions, and mark-to-market valuation analysis. Use when structuring rate swaps, analyzing swap economics, or evaluating hedging alternatives.
tags:
  - derivatives-and-structured-products
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Structured Products
    - Hedging
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Interest Rate Swaps

Designs IRS structures with fixed/float mechanics, day count conventions, and mark-to-market valuation analysis.

## When To Use

- Structuring a plain-vanilla or non-standard interest rate swap for a new financing or refinancing
- Evaluating fixed-vs-floating economics for a borrower or asset manager considering a hedge overlay
- Analyzing mark-to-market exposure and potential termination costs on an existing swap book
- Comparing swap structures (par swap, off-market swap, forward-starting swap, amortizing swap) against hedging objectives
- Reviewing ISDA confirmation terms, payment mechanics, and day count conventions before execution

## Inputs To Gather

- **Notional profile**: Fixed notional, amortizing schedule, or accreting schedule with amounts and dates
- **Tenor and dates**: Effective date, maturity date, and any forward-start period
- **Floating leg details**: Reference rate (SOFR, EURIBOR, TONA, etc.), reset frequency, compounding method (in arrears, in advance, payment delay), and spread adjustment [VERIFY applicable fallback language for legacy LIBOR transitions]
- **Fixed leg details**: Target fixed rate or par-swap rate, payment frequency
- **Day count conventions**: Specify for each leg (e.g., ACT/360, 30/360, ACT/ACT) [VERIFY market convention by currency]
- **Business day convention**: Modified Following, Following, or Preceding; relevant holiday calendars
- **Current market data**: Swap curve (OIS or term rate curve), discount curve, and any basis spread curves
- **Valuation date**: As-of date for mark-to-market and DV01 calculations
- **Counterparty context**: Credit support annex (CSA) terms — collateral currency, threshold, minimum transfer amount — to determine proper discount curve (OIS vs. CSA curve)
- **Regulatory context**: Clearing mandate applicability, initial margin (IM) requirements under UMR, and reporting obligations [VERIFY jurisdiction-specific clearing thresholds]

## Workflow

1. **Define the hedge objective** — Determine whether the goal is cash-flow hedging (locking in budget certainty), fair-value hedging (offsetting balance-sheet exposure), or speculative positioning. Confirm hedge accounting intent (ASC 815 / IFRS 9) if applicable.

2. **Select swap structure** — Choose from:
   - **Par swap**: Zero upfront value; fixed rate = par swap rate from the curve
   - **Off-market swap**: Upfront payment exchanged for an above/below-market fixed rate
   - **Forward-starting swap**: Effective date in the future to match anticipated debt issuance
   - **Amortizing/accreting swap**: Notional schedule mirrors underlying debt amortization
   - **Basis swap**: Float-for-float when converting between reference rates

3. **Build the cash flow schedule** — For each leg:
   - Generate accrual periods using the specified roll convention and business day rules
   - Apply the correct day count fraction per period
   - For the floating leg, determine fixing dates, observation periods (for SOFR compounding in arrears), and lockout/lookback adjustments
   - Calculate projected floating payments from the forward curve

4. **Price the swap** — Discount all projected net cash flows using the appropriate discount curve:
   - If cleared or CSA with cash collateral in swap currency → OIS discount curve
   - If uncollateralized → credit-adjusted discount curve or funding curve
   - Compute the **par fixed rate** (rate that sets NPV = 0) or the **NPV** for an off-market rate
   - Report the **DV01** (dollar value of a 1 bp parallel shift) for each leg and net

5. **Assess risk metrics** — Calculate:
   - **DV01 / PV01**: Sensitivity to 1 bp parallel rate move
   - **Key rate durations (KRDs)**: Sensitivity at individual tenor buckets along the curve
   - **Convexity**: Second-order rate sensitivity for large moves
   - **Potential future exposure (PFE)**: Simulated MTM distribution for counterparty credit risk
   - **Termination value scenarios**: MTM under +/−50, 100, 200 bp rate shifts

6. **Review documentation terms** — Confirm alignment of economic terms with ISDA confirmation language:
   - Fixed rate, floating rate option, designated maturity, spread, compounding method
   - Payment dates, calculation agent, fallback provisions
   - Early termination triggers and close-out netting provisions

7. **Compile analysis and recommendations** — Summarize the chosen structure, pricing, risk profile, and any trade-offs versus alternative hedging instruments (caps, collars, swaptions).

## Output

Deliver a structured report containing:

- **Executive summary**: Hedge objective, recommended structure, and par swap rate or NPV
- **Term sheet / indicative terms**: Notional, tenor, fixed rate, floating rate reference and spread, day counts, payment frequencies, business day conventions
- **Cash flow schedule**: Period-by-period projected payments for both legs with net settlement amounts
- **Valuation summary**: NPV, DV01/PV01 (net and per-leg), key rate sensitivities
- **Scenario analysis table**: MTM under parallel and non-parallel rate shifts (at minimum ±50, ±100, ±200 bp)
- **Comparison matrix** (if applicable): Side-by-side of swap vs. cap vs. collar vs. swaption on cost, risk profile, and accounting treatment
- **Assumptions and limitations**: Curve construction methodology, interpolation method, credit adjustments, and any data gaps flagged with [VERIFY]

## Quality Checks

- Confirm par swap rate is consistent with current broker/dealer indicative screens or Bloomberg SWPM output
- Verify that floating leg projected cash flows reproduce the forward rates implied by the discount curve
- Check that DV01 of the fixed leg and floating leg are approximately equal at the par rate (net DV01 ≈ 0 for a par swap)
- Validate day count fractions by independently computing at least two accrual periods
- Ensure the discount curve selection matches CSA collateral terms — using the wrong curve is a common and material valuation error
- Confirm notional schedule aligns with underlying debt amortization (no over-hedging or under-hedging)
- Flag any periods where the floating rate observation period or fixing methodology does not match market convention with [VERIFY]
- Cross-check that business day adjustments on payment dates match the holiday calendar for the relevant currency center

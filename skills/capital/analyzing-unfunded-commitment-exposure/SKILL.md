---
name: analyzing-unfunded-commitment-exposure
description: Evaluates unfunded commitment obligations with call probability, pacing models, and portfolio-level exposure management. Use when analyzing unfunded exposure, managing commitment pacing, or stress testing capital calls.
tags:
  - analysis
  - secondaries-and-gp-led
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Secondaries
    - GP-Led Transactions
    - LP Portfolio Management
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Unfunded Commitment Exposure

## When To Use

- Evaluating an LP's total unfunded obligation across active fund commitments before making new allocations
- Stress-testing capital call scenarios for secondary portfolio acquisitions or GP-led continuation vehicles
- Assessing pacing risk when an LP's liquid reserves may be insufficient to meet projected drawdowns
- Preparing exposure reports for investment committees ahead of re-up or new commitment decisions
- Modeling unfunded exposure impact during denominator-effect periods (portfolio NAV declines increasing PE allocation weight)

## Inputs To Gather

- **Commitment schedule**: Fund name, vintage year, total commitment, called capital to date, unfunded balance, and fund term/extension status
- **GP call history**: Historical call cadence per fund (quarterly call amounts as % of commitment) and any known upcoming large calls (e.g., deal closings)
- **Fund lifecycle stage**: Investment period vs. harvest period designation for each fund; expected remaining investment period duration
- **Distribution data**: Recent distribution rates and whether distributions are being recalled or recycled
- **LP liquidity profile**: Available cash, credit facility capacity, expected near-term distributions, and any over-commitment policy limits
- **Market context**: Current fundraising environment, deal flow pace, and whether GPs are accelerating or slowing deployment
- **Secondary-specific inputs** (if applicable): Unfunded assumptions embedded in secondary pricing, seller's remaining pacing obligations, and any escrow or deferred payment structures

## Workflow

1. **Build the commitment inventory** — Aggregate all active fund commitments into a single ledger. Categorize each by vintage, strategy (buyout, growth, venture, real assets, credit), fund lifecycle stage, and GP. Calculate unfunded balance as total commitment minus cumulative called capital. Flag any funds with extension provisions or zombie-fund risk.

2. **Assign call probability profiles** — For each fund, estimate the likelihood and timing of remaining capital calls:
   - *Investment-period funds*: Assume 80–100% of unfunded will be called; model call pacing based on GP's historical deployment speed and stated pipeline
   - *Post-investment-period funds*: Assume 5–20% residual calls (follow-ons, fees, recycling); assign lower call probability
   - *Continuation/GP-led vehicles*: Assess whether new unfunded tranches exist and model per the vehicle's stated drawdown schedule
   - [VERIFY] Confirm whether each fund's partnership agreement permits capital recycling, which inflates effective callable capital beyond original commitment

3. **Model pacing scenarios** — Project quarterly or annual capital calls across the portfolio using at least three scenarios:
   - *Base case*: Calls follow historical GP pacing patterns; distributions partially offset outflows
   - *Accelerated deployment*: GPs call capital 30–50% faster (e.g., competitive deal environment); distributions slow
   - *Stress case*: Simultaneous acceleration across multiple funds, distribution freeze, credit facility unavailable
   - For each scenario, compute net cash flow (calls minus distributions) and cumulative unfunded drawdown over 1-, 2-, and 3-year horizons

4. **Calculate exposure metrics** — Derive key ratios:
   - **Unfunded-to-NAV ratio**: Total unfunded ÷ current portfolio NAV (typical LP range: 0.3x–0.6x; above 0.7x signals elevated risk)
   - **Unfunded-to-liquid-assets ratio**: Total unfunded ÷ (cash + undrawn credit facility + projected near-term distributions)
   - **Over-commitment ratio**: Total commitments (funded + unfunded) ÷ target allocation, measuring reliance on distributions to fund future calls
   - **Weighted-average call probability**: Portfolio-level expected callable amount using fund-by-fund probability weights
   - [VERIFY] Confirm the LP's internal policy limits for each ratio and flag any breaches

5. **Identify concentration risks** — Assess unfunded exposure by:
   - Single GP (>15% of total unfunded to one manager is a common concentration threshold)
   - Vintage year clustering (multiple funds from the same vintage calling simultaneously)
   - Strategy overlap (e.g., heavy unfunded in venture during a slow-exit environment)
   - Currency exposure on non-USD commitments with unfunded balances

6. **Synthesize findings and recommend actions** — Summarize exposure posture and propose mitigants:
   - Adjust new commitment pacing if stress-case liquidity gap exceeds tolerance
   - Consider secondary sales of fund interests with high unfunded and low call probability (zombie positions)
   - Evaluate credit facility sizing relative to stress-case peak call quarter
   - Flag any GP-led transactions where rolling into a continuation vehicle resets unfunded exposure

## Output

- **Unfunded Exposure Summary Table**: Fund-by-fund breakdown showing commitment, called, unfunded, % remaining, lifecycle stage, call probability tier, and expected call horizon
- **Portfolio-Level Metrics Dashboard**: Unfunded-to-NAV, unfunded-to-liquidity, over-commitment ratio, and weighted-average callable amount
- **Pacing Scenario Analysis**: Quarterly projected net cash flows under base, accelerated, and stress cases with cumulative drawdown curves
- **Concentration Heat Map**: Unfunded exposure by GP, vintage, strategy, and currency
- **Risk Flags and Recommendations**: Bullet-point list of breaches, concentration warnings, and proposed actions (pacing adjustment, secondary sale candidates, credit facility review)

## Quality Checks

- Confirm every active fund commitment is included; cross-check against capital account statements and the LP's commitment ledger
- Validate that called-capital figures reconcile with GP capital call notices (not just internal estimates)
- Ensure call probability assumptions are documented with rationale — do not assign blanket percentages without fund-specific justification
- Verify that distribution assumptions in pacing models are conservative (use net distributions, not gross, and exclude any one-time outlier events)
- Check that over-commitment ratio calculations use the correct denominator (target allocation vs. total portfolio value) per the LP's policy definition
- Confirm currency conversion rates are current for non-USD unfunded obligations
- Mark any data gaps or stale GP reports with [VERIFY] and note the as-of date for all NAV and call figures

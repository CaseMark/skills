---
name: modeling-share-repurchase-optimization
language: en
description: Analyzes buyback program design with timing optimization, price sensitivity, and EPS accretion impact modeling. Use when optimizing buybacks, modeling repurchase economics, or comparing return-of-capital alternatives.
tags:
  - modeling
  - capital-allocation-and-corporate-strategy
metadata:
  author: casemark
  practice_areas:
    - Corporate Strategy
    - Capital Allocation
    - Shareholder Value
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Share Repurchase Optimization

Analyzes buyback program design with timing optimization, price sensitivity, and EPS accretion impact modeling.

## When To Use

- Evaluating whether to authorize a new buyback program or expand an existing one
- Comparing share repurchases against dividends, debt paydown, or M&A as capital return alternatives
- Modeling EPS accretion from a proposed repurchase at varying price levels and execution timelines
- Assessing optimal execution strategy (open-market, ASR, tender offer, Rule 10b5-1 plan)
- Stress-testing buyback economics under different share price, interest rate, and free cash flow scenarios
- Preparing board materials or investor communications on capital allocation strategy

## Inputs To Gather

- **Share data**: Current share price, shares outstanding (basic and diluted), historical price/volume data, float composition
- **Financial projections**: Net income forecast (next 4–8 quarters), free cash flow projections, existing debt obligations and maturities
- **Program parameters**: Authorized repurchase amount, planned execution timeline, funding source (cash on hand vs. incremental debt)
- **Cost of capital**: Current WACC, marginal cost of debt (if debt-funded), after-tax interest rate on foregone cash
- **Market context**: Current P/E and forward P/E, analyst consensus EPS, historical buyback execution prices for the company and peers
- **Regulatory/structural constraints**: Blackout windows, Rule 10b-18 daily volume limits (25% of ADTV), insider trading policy restrictions [VERIFY: confirm company-specific blackout calendar and any SEC safe harbor reliance]

## Workflow

1. **Establish baseline EPS trajectory** — Project quarterly EPS for 4–8 quarters with no repurchase activity. Include existing dilution from stock-based compensation and convertible instruments.

2. **Define repurchase scenarios** — Build at least three execution scenarios:
   - **Accelerated (ASR)**: Full authorization executed via investment bank within 1–3 months; model upfront share retirement with true-up
   - **Ratable open-market**: Even quarterly purchases over 4–8 quarters subject to volume limits
   - **Opportunistic/price-triggered**: Purchases concentrated when price falls below intrinsic value threshold (e.g., below forward P/E of X)

3. **Model shares retired per period** — For each scenario, calculate shares purchased = dollars deployed / assumed average purchase price. Apply volume constraints (Rule 10b-18: 25% of trailing 20-day ADTV). Reduce diluted share count each period by cumulative repurchased shares minus ongoing SBC dilution.

4. **Calculate EPS accretion** — Compare pro forma EPS (net income / reduced share count) against the baseline. If debt-funded, reduce net income by after-tax interest expense on incremental borrowings. Express accretion as both cents-per-share and percentage uplift.

5. **Build price sensitivity matrix** — Vary the average repurchase price (e.g., -20% / -10% / current / +10% / +20%) and show resulting shares retired, EPS accretion, and implied buyback yield (EPS accretion / price premium paid).

6. **Compare return-of-capital alternatives** — Model the same dollar amount deployed as:
   - Special or incremental regular dividend (after-tax yield to shareholders)
   - Debt reduction (interest savings, leverage ratio impact)
   - Retain for M&A or organic investment (required IRR hurdle to match buyback accretion)

7. **Run sensitivity and breakeven analysis** — Identify the breakeven repurchase price at which buyback accretion equals zero (the price where cost of retired equity equals earnings yield). Stress-test against FCF shortfall (what happens if cash generation misses plan by 20%?) and rising rates (if debt-funded, at what rate does accretion turn negative?).

8. **Assess leverage and rating impact** — Calculate pro forma net debt / EBITDA after repurchase. Flag if leverage exceeds rating agency thresholds for current credit rating [VERIFY: confirm relevant agency trigger levels for the issuer's rating category].

## Output

- **Executive summary table**: Authorization size, execution method, timeline, total shares retired, pro forma EPS accretion ($ and %), pro forma leverage
- **EPS accretion waterfall**: Step from baseline EPS to pro forma EPS showing share reduction benefit, SBC dilution offset, and (if applicable) incremental interest cost
- **Price sensitivity matrix**: Rows = average purchase price scenarios; columns = shares retired, EPS accretion, buyback yield, breakeven analysis
- **Capital allocation comparison**: Side-by-side of repurchase vs. dividend vs. debt paydown vs. reinvestment on key metrics (EPS impact, shareholder yield, leverage, IRR hurdle)
- **Scenario dashboard**: Summary across accelerated / ratable / opportunistic scenarios with key tradeoffs highlighted
- **Risk flags**: Leverage constraint warnings, FCF coverage shortfalls, blackout window execution gaps, volume limit constraints on timeline

## Quality Checks

- Confirm diluted share count reconciles to latest 10-Q/10-K and includes all in-the-money options, RSUs, and convertible instruments [VERIFY]
- Verify that modeled daily repurchase volumes do not exceed Rule 10b-18 safe harbor limits (25% of ADTV)
- Check that EPS accretion math accounts for both share reduction and any offsetting cost (foregone interest income or incremental interest expense)
- Validate that breakeven repurchase price is consistent with the company's current earnings yield (E/P ratio)
- Ensure pro forma leverage ratios use the same EBITDA definition as the company's credit facility covenants [VERIFY: confirm covenant EBITDA definition and any restricted payment baskets]
- Cross-check total dollar outflow against projected cumulative free cash flow to confirm cash sufficiency without covenant breach
- Flag if repurchase authorization exceeds 10% of market cap (may trigger heightened disclosure or governance scrutiny)

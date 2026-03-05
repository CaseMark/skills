---
name: analyzing-convertible-instrument-terms
description: Evaluates SAFE, convertible note, and KISS structures with conversion mechanics, caps, discounts, and MFN provisions. Use when analyzing convertible instruments, comparing SAFE vs note terms, or modeling conversion scenarios.
tags:
  - analysis
  - venture-capital
metadata:
  author: casemark
  practice_areas:
    - Venture Capital
    - Seed/Series Investing
    - Startup Ecosystems
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Convertible Instrument Terms

## When To Use

- Reviewing a SAFE, convertible note, or KISS before a founder signs or an investor commits
- Comparing multiple convertible instruments across a cap table to assess aggregate dilution
- Modeling conversion outcomes at various pre-money valuations for an upcoming priced round
- Evaluating whether MFN provisions or pro-rata rights create conflicts across investor cohorts
- Advising on whether a valuation cap, discount rate, or hybrid structure best fits the deal context

## Inputs To Gather

- **Instrument documents**: Full text of each SAFE, convertible note, or KISS (identify version — e.g., YC post-money SAFE 2018 vs. 2023 template)
- **Instrument type and variant**: Pre-money SAFE, post-money SAFE, convertible note (secured/unsecured), KISS (debt/equity variant)
- **Economic terms**: Valuation cap, discount rate (or both), interest rate and accrual method (notes only), maturity date (notes only)
- **Key provisions**: MFN clause scope, pro-rata rights, amendment/waiver thresholds, dissolution/liquidation waterfall priority
- **Cap table context**: Current outstanding shares, option pool size, any prior convertible instruments outstanding
- **Anticipated round terms** (if available): Expected pre-money valuation, round size, lead investor terms

## Workflow

1. **Classify each instrument**
   - Identify instrument type (post-money SAFE, pre-money SAFE, convertible note, KISS debt, KISS equity)
   - Note the template version and any custom modifications from standard forms
   - Flag if the instrument is a non-standard or bespoke structure

2. **Extract and tabulate economic terms**
   - For each instrument, record: investment amount, valuation cap, discount rate, interest rate, maturity date, and MFN status
   - For convertible notes: confirm whether interest is simple or compound, accrual frequency, and whether interest converts or is repaid [VERIFY: confirm accrual terms in instrument]
   - Identify whether the cap is pre-money or post-money — this fundamentally changes dilution math

3. **Analyze conversion mechanics**
   - **Cap conversion**: Shares = Investment ÷ (Cap ÷ fully-diluted capitalization at conversion)
   - **Discount conversion**: Shares = Investment ÷ (Price per share × (1 − discount rate))
   - **Hybrid (cap + discount)**: Investor receives the more favorable of cap-based or discount-based conversion
   - For post-money SAFEs: the investor's ownership percentage is fixed (Investment ÷ Cap), and dilution falls on founders and prior investors — not SAFE holders
   - For notes with accrued interest: calculate total converting principal + interest at expected conversion date

4. **Model conversion scenarios**
   - Run conversion at 2–3 representative pre-money valuations (e.g., $5M, $10M, $20M or as contextually appropriate)
   - Show resulting ownership percentages for each investor and for founders post-conversion
   - Identify the valuation at which the cap vs. discount "crossover" occurs (discount becomes more favorable than cap)
   - For stacked instruments: model aggregate dilution from all converting instruments simultaneously

5. **Evaluate protective and structural provisions**
   - MFN: Does it apply only to future SAFEs, or also to future convertible notes? Does it auto-trigger or require election? What is the notification mechanism?
   - Pro-rata rights: side letter or built into the instrument? Based on pre- or post-conversion ownership?
   - Amendment provisions: majority-in-interest threshold — by dollar amount or by holder count?
   - Dissolution/wind-down: payment priority relative to other instruments and equity holders [VERIFY: confirm liquidation waterfall ordering if multiple instrument types]

6. **Identify risks and flag issues**
   - Stacking risk: total SAFE/note overhang as a percentage of anticipated post-money valuation
   - MFN conflicts: later instruments with better terms triggering MFN for earlier holders, compounding dilution
   - Maturity risk (notes): what happens at maturity — auto-convert, founder repayment obligation, or default?
   - Shadow preferred: SAFEs converting into a separate series with different rights than the lead investor's preferred stock

## Output

Structure the analysis report as follows:

- **Instrument Summary Table**: One row per instrument — type, date, amount, cap, discount, interest rate, maturity, MFN status
- **Conversion Modeling**: Scenario table showing shares issued and ownership percentages at 2–3 valuations
- **Cap vs. Discount Crossover**: The pre-money valuation at which each instrument's discount becomes more favorable than its cap
- **Aggregate Dilution Impact**: Total founder dilution from all converting instruments at the most likely round valuation
- **Provision Comparison**: Side-by-side comparison of MFN scope, pro-rata rights, amendment thresholds, and dissolution treatment
- **Risk Flags**: Bullet list of material risks (stacking, MFN cascades, maturity exposure, structural conflicts)
- **Recommendations**: Specific, actionable guidance — e.g., "Negotiate removal of MFN from Investor B's SAFE before closing Investor C" or "Cap total convertible overhang at 25% of anticipated post-money"

## Quality Checks

- Confirm whether each instrument uses pre-money or post-money cap mechanics — misclassifying this produces materially wrong dilution figures
- Verify that conversion math uses the correct fully-diluted share count (including or excluding the option pool, depending on instrument terms) [VERIFY: check instrument definition of "Company Capitalization" or equivalent]
- Cross-check that MFN analysis accounts for all outstanding instruments, not just the one under review
- Ensure interest accrual calculations on notes match the stated accrual method and compounding frequency
- Validate that scenario modeling uses consistent assumptions across all instruments (same pre-money, same option pool treatment)
- Flag any instrument that deviates from standard YC SAFE / 500 Startups KISS templates and note the specific deviations

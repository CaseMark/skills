---
name: modeling-dilution-impact-analysis
language: en
description: Calculates dilutive impact of equity issuance on existing shareholders with EPS, ownership, and NAV per share analysis. Use when modeling dilution, communicating shareholder impact, or comparing capital raise alternatives.
tags:
  - modeling
  - equity-capital-markets
metadata:
  author: casemark
  practice_areas:
    - ECM
    - IPO Advisory
    - Equity Origination
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Dilution Impact Analysis

## When To Use

- Issuer is evaluating a primary equity offering (IPO, follow-on, ATM, PIPE, rights offering) and needs to quantify shareholder impact before launch
- Board or management requests a comparison of capital raise alternatives (e.g., 10% vs. 15% primary offering, common vs. convertible) on a per-share basis
- Investor relations needs pro-forma EPS and ownership tables for investor presentations or prospectus disclosure
- Evaluating anti-dilution protection triggers in existing preferred stock or convertible instruments

## Inputs To Gather

- **Pre-offering share data**: Basic shares outstanding, diluted share count (treasury stock method), fully diluted share count including all convertible securities, options, warrants, and RSUs with strike prices and vesting schedules
- **Offering terms**: Number of new shares issued, offering price (or price range), greenshoe/over-allotment option size, any discount to market price
- **Financial projections**: Consensus or management EPS estimates for current and next fiscal year, net income forecast, book value / NAV per share [VERIFY: source — consensus vs. management guidance]
- **Use of proceeds**: Debt paydown (interest savings), acquisition (accretion/dilution from target), general corporate purposes, or share buyback offset
- **Existing capital structure**: Outstanding convertible notes (conversion price, conversion ratio), preferred stock (participation rights, conversion mechanics), anti-dilution ratchet provisions [VERIFY: exact anti-dilution formula — broad-based weighted average vs. full ratchet]
- **Market data**: Current stock price, 30-day VWAP, 52-week range (for pricing context)

## Workflow

1. **Build the pre-offering share count schedule**
   - Start with basic shares outstanding from the most recent filing (10-Q/10-K or equivalent)
   - Layer in dilutive securities using treasury stock method at the assumed offering price: options, warrants, RSUs, convertible debt, convertible preferred
   - Separately track fully diluted share count (all instruments regardless of in/out of the money)

2. **Model the offering mechanics**
   - Calculate new shares from primary issuance at offering price
   - Add greenshoe shares (typically 15% of base deal) as a separate toggle
   - Compute gross and net proceeds (deduct underwriting discount — typically 3–7% depending on deal type [VERIFY: fee schedule for specific deal])
   - If convertible offering: model conversion premium, conversion price, and incremental shares at conversion

3. **Calculate pro-forma dilution metrics**
   - **Ownership dilution**: (New shares issued) / (Pre-offering diluted shares + New shares issued) — express as percentage reduction in existing holder ownership
   - **EPS dilution**: Compare pre-offering EPS to pro-forma EPS = (Net income ± proceeds impact) / (Post-offering diluted shares)
   - **NAV/Book value dilution**: Compare pre-offering NAV per share to post-offering NAV per share after adding net proceeds to equity
   - If proceeds retire debt: add back after-tax interest savings to net income in EPS calculation
   - If proceeds fund an acquisition: layer in target earnings contribution and additional shares

4. **Build the comparison matrix**
   - Run scenarios across at least 3 offering sizes and 3 price points (e.g., ±5%, ±10% from spot)
   - For each scenario, display: shares issued, gross proceeds, ownership dilution %, EPS dilution %, NAV dilution/accretion %, and breakeven period (quarters until EPS recovers to pre-deal level assuming proceeds deployment)
   - Highlight the scenario closest to issuer's target raise amount

5. **Assess convertible and anti-dilution impacts**
   - Check whether offering price triggers anti-dilution adjustments on existing preferred or convertible instruments
   - If broad-based weighted average: recalculate adjusted conversion price using the standard formula and show incremental dilution from conversion price reset
   - If full ratchet: show worst-case conversion price adjustment and flag magnitude of additional dilution
   - Model contingent dilution from convertible notes at various stock price levels ($X, $Y, $Z) showing incremental share issuance at each threshold

6. **Sensitivity analysis**
   - Vary offering price (±10–20% from base case) and show impact on all key metrics
   - Vary use-of-proceeds assumptions (100% debt paydown vs. 100% general corporate vs. blend)
   - If applicable, toggle greenshoe exercise on/off
   - Present results in a matrix format suitable for board or management review

## Output

- **Summary table**: Pre-offering vs. post-offering comparison showing basic shares, diluted shares, ownership %, EPS, and NAV per share — for base case and key scenarios
- **Scenario matrix**: Grid of offering size × offering price with ownership dilution %, EPS dilution %, and NAV impact for each cell
- **Anti-dilution waterfall** (if applicable): Step-through showing how existing conversion prices adjust and incremental shares created
- **Sensitivity tables**: EPS dilution and ownership dilution across price and size ranges
- **Key assumptions list**: Clearly labeled with sources (consensus, management, filing date) and [VERIFY] flags on any estimated inputs
- All outputs should be formatted for direct insertion into investor presentations, S-1/prospectus supplements, or board materials

## Quality Checks

- Confirm diluted share count ties to the most recent SEC filing or equivalent disclosure — reconcile any difference
- Verify that treasury stock method is applied correctly: only in-the-money instruments at the offering price add incremental shares
- Cross-check that pro-forma EPS × post-offering diluted shares ≈ adjusted net income (arithmetic consistency)
- Confirm ownership dilution percentage is calculated on the correct base (pre-offering diluted, not basic)
- Validate that use-of-proceeds adjustments to net income use the correct tax rate [VERIFY: marginal vs. effective tax rate]
- Ensure anti-dilution calculations use the exact formula from the governing instrument, not a generic approximation
- Flag any scenario where dilution exceeds 20% ownership — this may trigger exchange listing rules or shareholder approval requirements [VERIFY: applicable exchange rules — NYSE §312.03, Nasdaq §5635]

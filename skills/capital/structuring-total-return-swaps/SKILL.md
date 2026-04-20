---
name: structuring-total-return-swaps
language: en
description: Designs TRS structures with reference asset selection, financing rate mechanics, and collateral arrangements. Use when structuring TRS, analyzing synthetic exposure, or evaluating unfunded exposure alternatives.
tags:
  - derivatives-and-structured-products
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
# Structuring Total Return Swaps

Designs TRS structures with reference asset selection, financing rate mechanics, and collateral arrangements for synthetic exposure to credit, equity, or real asset portfolios.

## When To Use

- Structuring a new TRS to gain unfunded synthetic exposure to a reference asset or portfolio
- Evaluating TRS versus cash purchase, repo financing, or credit-linked note alternatives
- Analyzing financing rate economics (TRS spread over reference rate) for a proposed trade
- Designing collateral and margin frameworks for a TRS facility
- Reviewing or restructuring an existing TRS to adjust tenor, reset mechanics, or termination triggers
- Assessing counterparty credit exposure embedded in a TRS position

## Inputs To Gather

- **Reference asset details**: Single-name bond/loan, equity, basket, or index; CUSIP/ISIN; notional amount; current market price and accrued interest
- **Economic terms**: Desired tenor, reset frequency (quarterly/semi-annual), payment dates, day-count convention (ACT/360, 30/360)
- **Financing rate**: Benchmark rate (SOFR, EURIBOR, SONIA) plus proposed TRS spread in basis points; fixed vs. floating leg structure
- **Total return leg**: Whether total return includes price appreciation only or price + coupon/dividend; treatment of defaults, restructurings, or corporate actions on the reference asset
- **Collateral framework**: Initial margin percentage, variation margin triggers, eligible collateral types, haircut schedule, rehypothecation rights
- **Termination provisions**: Scheduled maturity, optional early termination rights, market disruption events, credit events on reference obligor, and settlement method (physical vs. cash)
- **Counterparty information**: Credit rating, netting agreement status (ISDA Master in place), CSA terms, regulatory classification (dealer, buy-side, special purpose vehicle)
- **Regulatory context**: Applicable margin rules (uncleared swap margin requirements), capital treatment under Basel III/IV, reporting obligations (EMIR, Dodd-Frank Title VII) [VERIFY jurisdiction-specific thresholds]

## Workflow

1. **Define the economic objective** — Confirm whether the TRS is for leveraged long exposure, short exposure via receiving financing leg, balance-sheet optimization, or regulatory capital relief. Identify the reference asset and target notional.

2. **Select reference asset and price source** — Specify the reference obligation(s), pricing source (dealer marks, third-party vendor, index level), and valuation frequency. For loan TRS, confirm whether price is par-adjusted or market-based and whether funded/unfunded commitments are included.

3. **Structure the financing leg** — Set the benchmark rate, TRS spread, reset dates, and compounding convention. Calculate the all-in financing cost and compare against alternative funding sources (repo rate, warehouse facility cost, margin loan rate). Ensure the spread reflects counterparty credit, reference asset liquidity, and tenor risk.

4. **Define total return mechanics** — Specify what constitutes "total return": price change plus coupon/interest/dividend income, minus any applicable withholding. Address treatment of:
   - Coupon or dividend record dates vs. payment dates
   - Reference asset defaults or credit events (triggers cash settlement or physical delivery)
   - Corporate actions (mergers, tenders, consent solicitations) on the reference obligor
   - Negative total return periods and netting across reset dates

5. **Design collateral and margin framework** — Set initial margin (typically 5-20% for investment-grade; 15-40% for high-yield or illiquid references). Define variation margin call frequency (daily or weekly), minimum transfer amounts, eligible collateral (cash, Treasuries, agency MBS), and haircuts. Address substitution rights and dispute resolution for valuations.

6. **Draft termination and settlement provisions** — Define scheduled maturity, early termination triggers (credit event, NAV decline threshold, change of control, illegality), and settlement method. For physical settlement, specify deliverable obligation characteristics. For cash settlement, specify valuation agent, polling dealers, and fallback pricing.

7. **Assess counterparty and regulatory requirements** — Confirm ISDA Master Agreement and CSA are in place. Evaluate whether the TRS falls within uncleared margin rules [VERIFY applicable phase-in thresholds by counterparty classification]. Assess capital charges: risk-weighted asset impact for banks, leverage ratio treatment, and any SA-CCR exposure calculation requirements. Confirm trade reporting obligations.

8. **Model economics and stress scenarios** — Calculate expected carry (total return on reference asset minus financing cost). Stress-test for: reference asset price decline of 10-30%, benchmark rate increase of 200-400 bps, reference obligor credit event, and counterparty default with close-out netting. Quantify maximum margin call under stress.

## Output

Produce a **TRS Structuring Report** containing:

- **Executive summary**: Objective, reference asset, notional, tenor, and financing rate
- **Term sheet**: Complete economic terms in standard ISDA TRS confirmation format — reference obligation, notional, trade/effective/maturity dates, total return amounts, financing amounts, payment dates, business day convention, calculation agent
- **Economics analysis**: Expected carry calculation, breakeven reference asset return, comparison to alternative funding structures with all-in cost
- **Collateral schedule**: Initial margin, variation margin mechanics, eligible collateral with haircuts, minimum transfer amount, rounding
- **Risk summary**: Key sensitivities (spread duration, rate duration, default probability impact), maximum loss under stress, counterparty exposure profile over tenor
- **Regulatory checklist**: Applicable margin rules, capital treatment, reporting obligations, with [VERIFY] flags for jurisdiction-dependent items

## Quality Checks

- Financing rate convention (ACT/360 vs. 30/360) is consistent between term sheet and economics model
- Total return definition captures all income components and correctly handles ex-date vs. payment-date timing
- Collateral haircuts align with CSA terms and are appropriate for reference asset volatility
- Termination triggers are consistent with ISDA Credit Derivatives Definitions where credit events are referenced [VERIFY: 2014 vs. 2003 Definitions applicability]
- Settlement method (physical vs. cash) is feasible given reference asset liquidity
- Capital and margin calculations use correct counterparty classification and netting set [VERIFY regulatory classification under local rules]
- All notional amounts, dates, and payment frequencies are internally consistent across term sheet, economics, and collateral sections

---
name: building-merger-models
description: Constructs merger consequence analysis with accretion/dilution, pro forma financials, and synergy assumptions. Use when modeling mergers, calculating accretion/dilution, or analyzing deal structures.
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
# Building Merger Models

## When To Use

- Evaluating whether a proposed acquisition is accretive or dilutive to the acquirer's EPS
- Building pro forma combined financial statements for a merger transaction
- Stress-testing deal structures across varying consideration mixes (cash, stock, mixed)
- Quantifying synergy assumptions (revenue and cost) and their impact on deal economics
- Comparing multiple deal scenarios (e.g., different offer prices, financing structures, or synergy ramp schedules)

## Inputs To Gather

- **Acquirer financials**: Latest annual and interim income statement, balance sheet, share count (basic and diluted), current stock price, existing debt schedule
- **Target financials**: Same as acquirer; also any available management projections or consensus estimates
- **Deal terms**: Offer price per share (or total equity value), consideration mix (% cash / % stock), expected close date, breakup fee, collar provisions if any
- **Financing assumptions**: New debt tranches (amount, rate, tenor), cash on hand used, any equity issuance beyond stock consideration
- **Synergy estimates**: Cost synergies (headcount, facilities, procurement) with phase-in timeline; revenue synergies if modeled, with probability weighting
- **Transaction costs**: Advisory fees, financing fees, integration costs, severance/restructuring charges
- **Tax rates**: Acquirer and target marginal rates, any step-up or NOL considerations [VERIFY jurisdiction-specific tax treatment]

## Workflow

1. **Set up standalone models**
   - Build or import acquirer and target income statements on a consistent fiscal-year basis
   - Calendarize target financials if fiscal year-ends differ
   - Confirm diluted share counts and current EPS for the acquirer as the baseline

2. **Model the transaction structure**
   - Calculate total consideration: offer price x target diluted shares
   - Allocate between cash and stock; compute new shares issued to target shareholders
   - Determine goodwill and intangible asset write-ups using purchase price allocation (fair value of net assets vs. purchase price)
   - Build the sources & uses table: equity issued, new debt raised, cash from balance sheet, fees

3. **Construct pro forma adjustments**
   - Add new interest expense on acquisition debt (net of tax)
   - Remove target's existing interest expense if debt is retired at close
   - Add D&A from intangible asset write-ups (customer relationships, technology, trade names) with appropriate amortization schedules
   - Layer in synergies on the phase-in schedule (e.g., 25% Year 1, 75% Year 2, 100% Year 3)
   - Back out one-time transaction and integration costs in the relevant periods
   - Adjust share count for new shares issued; apply treasury stock method for any options/convertibles

4. **Calculate accretion / dilution**
   - Pro forma combined EPS = (Acquirer net income + Target net income + synergies - incremental interest - incremental D&A) / pro forma diluted shares
   - Compare to standalone acquirer EPS; express as % accretive or dilutive
   - Show Year 1, Year 2, and Year 3 to capture synergy ramp

5. **Run sensitivity analysis**
   - Offer price vs. accretion/dilution (price sensitivity table)
   - Consideration mix (all-cash, all-stock, 50/50) impact on EPS and leverage
   - Synergy achievement rate (50%, 75%, 100%) vs. accretion breakeven
   - Interest rate sensitivity on floating-rate acquisition debt
   - Create a football-field-style summary showing accretion/dilution across scenarios

6. **Build credit and returns checks**
   - Pro forma leverage (Net Debt / EBITDA) vs. acquirer's target or rating threshold
   - Interest coverage ratio (EBITDA / Interest) post-deal
   - IRR to acquirer at various exit multiples (if PE-backed or strategic with exit horizon)

## Output

- **Sources & Uses table**: Clear breakdown of deal financing
- **Pro forma income statement**: Combined P&L with line-item adjustments labeled
- **Accretion/dilution summary**: Year 1-3 EPS impact in dollars and percentage terms
- **Sensitivity tables**: At minimum, offer price vs. accretion and synergy achievement vs. accretion
- **Key assumptions page**: All inputs, synergy estimates, and financing terms in one reference sheet
- **Credit metrics**: Pro forma leverage and coverage ratios

## Quality Checks

- Accretion/dilution output ties to the difference between pro forma EPS and standalone acquirer EPS — cross-check arithmetic
- Sources & uses balance exactly (total sources = total uses)
- Goodwill = purchase price - fair value of net tangible and identifiable intangible assets [VERIFY purchase price allocation assumptions]
- New shares issued = stock consideration / acquirer share price — confirm this flows through to diluted share count
- Interest expense ties to debt schedule (principal x rate); verify pre-tax vs. after-tax treatment
- Synergies phase in over the correct timeline and are excluded from Year 0 / close-date calculations
- Tax rate applied to pre-tax synergies and interest adjustments is consistent with the stated marginal rate [VERIFY if deal creates NOL or changes tax jurisdiction]
- Pro forma leverage ratios are computed on the same EBITDA definition (with or without synergies) disclosed to the user
- No circular references between interest income on cash and net income if cash sweeps are modeled

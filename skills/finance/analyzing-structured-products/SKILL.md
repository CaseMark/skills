---
name: analyzing-structured-products
description: Evaluates ABS, MBS, CLO, and CDO structures with cash flow waterfall and subordination analysis. Use when analyzing structured products, modeling cash flow waterfalls, or evaluating tranche risk.
tags:
  - analysis
  - fixed-income
  - risk
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Structured Products

## When To Use

- Evaluating a new ABS, MBS, CLO, or CDO offering for investment suitability
- Assessing tranche risk and credit enhancement adequacy on an existing position
- Modeling cash flow waterfalls under base, stress, and default scenarios
- Comparing subordination levels, excess spread, and overcollateralization across deals
- Reviewing deal documents (indenture, offering circular, trustee reports) for structural features
- Monitoring portfolio holdings for collateral deterioration or trigger breaches

## Inputs To Gather

- **Deal documents**: Offering circular/prospectus supplement, indenture, servicing agreement
- **Collateral data**: Loan-level tape or pool stratification (WAC, WAM, WALA, FICO distribution, geographic concentration, LTV distribution for MBS; industry/rating distribution for CLO/CDO)
- **Tranche structure**: Par amounts, coupon types (fixed/floating), spread, legal final maturity, expected maturity, payment priority
- **Credit enhancement details**: Subordination percentages, overcollateralization (OC) targets and triggers, excess spread, reserve accounts, insurance wraps if applicable
- **Performance data**: Monthly trustee/remittance reports — delinquency buckets (30/60/90+), CDR, CPR, loss severity, cumulative losses vs. trigger levels
- **Rating agency presale reports or surveillance commentary** (Moody's, S&P, Fitch, KBRA, DBRS)
- **Pricing/spread context**: Comparable deal spreads, secondary trading levels, index benchmarks (e.g., CMBX, ABX, Markit CLO indices)

## Workflow

1. **Classify the structure**
   - Identify product type: RMBS (agency/non-agency), CMBS, auto ABS, credit card ABS, student loan ABS, CLO, CDO (cash/synthetic), or bespoke
   - Note static vs. revolving/managed pool; amortizing vs. bullet tranches
   - Identify waterfall type: sequential pay, pro rata, modified pro rata with trigger-based switches

2. **Map the cash flow waterfall**
   - Trace payment priority from senior through mezzanine to equity/residual
   - Identify interest waterfall vs. principal waterfall (many deals separate these)
   - Document trigger events: OC tests, IC (interest coverage) tests, delinquency triggers, cumulative loss triggers
   - Note what happens on trigger breach (e.g., diversion of excess spread, turbo amortization of seniors, trapping of equity distributions)

3. **Assess credit enhancement**
   - Calculate current subordination for each tranche: (total par below tranche) / (total deal par)
   - Compare initial vs. current subordination — has it grown (sequential pay building credit enhancement) or eroded (losses eating into junior tranches)?
   - Quantify OC cushion: (collateral par − tranche par) / tranche par for each OC test
   - Evaluate excess spread: gross WAC − senior coupon − servicing fee − expected losses
   - For CLOs: check reinvestment period remaining, WARF, WAL, diversity score, CCC bucket limits [VERIFY: specific threshold levels vary by deal and manager]

4. **Run scenario analysis**
   - **Base case**: Forward curves, current prepayment/default/severity assumptions
   - **Stress case**: Elevate CDR by 2–3x, increase loss severity 10–20 pp, slow prepayments (extend duration) or spike prepayments (reduce excess spread capture)
   - **Tail risk**: Model what default rate/severity combination breaks each tranche — solve for breakeven loss multiple
   - For CMBS: model individual large-loan default scenarios and balloon extension risk
   - For CLOs: model par erosion from downgrades/defaults reducing the OC cushion

5. **Evaluate collateral quality**
   - Review pool stratification for concentration risk (single obligor, industry, geography)
   - Assess vintage performance: compare deal's cumulative loss curve to similar-vintage benchmark curves
   - For MBS: analyze LTV distribution, documentation type, occupancy status, loan purpose
   - For CLOs: review collateral manager track record, portfolio turnover, CCC-rated bucket size, weighted average rating factor (WARF) trajectory
   - Flag any deteriorating collateral metrics vs. prior reporting periods

6. **Determine relative value**
   - Compare tranche spread to similarly rated tranches from comparable deals
   - Assess spread per unit of credit enhancement (compensation for risk)
   - Factor in liquidity premium — off-the-run or esoteric deals trade wider
   - Consider rating trajectory: is the tranche on watch or trending toward upgrade/downgrade?

## Output

- **Structure summary**: Deal name, collateral type, closing date, pool balance, number of tranches, reinvestment period (if applicable)
- **Waterfall diagram**: Simplified schematic showing payment priority, trigger levels, and current OC/IC cushions
- **Tranche-level analysis table**: For each tranche — rating, coupon, current par, subordination %, OC cushion, WAL, spread, breakeven loss multiple
- **Scenario results**: Cash flow projections under base/stress/tail showing principal losses, WAL extension, and yield impact per tranche
- **Collateral health scorecard**: Key pool metrics with trend arrows (improving/stable/deteriorating) vs. prior periods
- **Risk flags**: Trigger proximity, concentration risks, servicer concerns, rating watch items
- **Recommendation**: Buy/hold/sell with spread target and key monitoring triggers

## Quality Checks

- Verify that waterfall mapping matches the indenture — payment priority errors cascade through all downstream analysis
- Confirm subordination math: tranche sizes must sum to total deal par; percentages should cross-check against trustee reports
- Validate scenario assumptions against historical analogs (e.g., 2007–2009 loss curves for stress cases) [VERIFY: appropriate stress benchmarks depend on asset class and vintage]
- Ensure collateral data vintage matches the most recent trustee report date — stale data understates risk
- Cross-check ratings against all agencies covering the deal; note any split ratings
- Flag any structural features that could impair analysis accuracy: clean-up calls, optional redemption provisions, servicer advancing mechanics [VERIFY: advancing conventions differ by asset class and servicer]
- Confirm that breakeven calculations account for timing of losses, not just cumulative magnitude

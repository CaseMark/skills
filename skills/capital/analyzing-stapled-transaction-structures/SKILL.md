---
name: analyzing-stapled-transaction-structures
description: Evaluates stapled secondary structures combining primary commitment with secondary purchase in coordinated transactions. Use when analyzing stapled deals, structuring combined primary/secondary, or evaluating staple economics.
tags:
  - analysis
  - secondaries-and-gp-led
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
# Analyzing Stapled Transaction Structures

## When To Use

- Evaluating a secondary purchase where the GP or seller requires the buyer to make a concurrent primary commitment to a new or successor fund
- Comparing blended economics of the stapled package (secondary discount vs. primary commitment at par) against standalone secondary pricing
- Advising an LP on whether accepting a staple improves or degrades overall portfolio return expectations
- Structuring a GP-led process where stapled commitments are offered to incentivize secondary liquidity

## Inputs To Gather

- **Secondary portfolio details**: Fund name, vintage, strategy, NAV, unfunded commitments, underlying asset composition, and most recent quarterly report
- **Primary staple terms**: Target fund name, fund size, commitment amount required, management fee and carry structure, investment period length, and any fee offsets or discounts offered as staple incentives
- **Staple ratio**: Required primary commitment as a percentage of secondary purchase price (e.g., 1:1, 0.5:1)
- **Secondary pricing**: Proposed purchase price as a percentage of NAV, any deferred payment or earnout components
- **GP track record**: Prior fund performance (net IRR, TVPI, DPI) for both the legacy fund and GP's overall platform
- **Cash flow projections**: Expected distribution timeline from the secondary portfolio and projected capital call schedule for the primary commitment
- **Comparable transactions**: Recent stapled deal pricing in the same strategy or vintage cohort [VERIFY market data source and recency]

## Workflow

1. **Map the staple structure**
   - Identify whether the staple is hard (mandatory primary commitment) or soft (optional but incentivized via pricing)
   - Document the staple ratio and determine if the ratio is fixed or negotiable
   - Confirm whether the primary commitment is to the same GP's next fund, a co-investment vehicle, or a separate strategy

2. **Analyze secondary component standalone**
   - Underwrite the secondary portfolio: remaining NAV, unfunded exposure, expected distributions, and hold period
   - Calculate standalone secondary IRR and MOIC at the proposed pricing
   - Assess J-curve exposure — determine how much unfunded liability transfers with the purchase

3. **Analyze primary component standalone**
   - Model the primary fund's projected returns based on GP track record and strategy benchmarks
   - Calculate expected net IRR and MOIC for the primary commitment at par (1.00x entry)
   - Estimate capital call pacing and time-to-first-distribution

4. **Calculate blended economics**
   - Combine secondary and primary cash flow streams into a single blended return profile
   - Compute blended IRR, MOIC, and DPI at multiple exit timing scenarios
   - Compare blended returns to: (a) the secondary purchased without staple at market pricing, and (b) the primary fund commitment made independently
   - Determine the **effective discount**: the implicit pricing benefit (or penalty) the staple creates when viewed as a single investment

5. **Assess staple-specific risks**
   - **Adverse selection**: Is the GP using the staple to move a difficult secondary portfolio by bundling it with an attractive primary?
   - **Capital concentration**: Does the stapled package overweight the buyer's exposure to a single GP, strategy, or vintage?
   - **Liquidity mismatch**: Does the primary commitment's call schedule conflict with expected secondary distributions?
   - **GP alignment**: Does the GP benefit disproportionately (e.g., locking in management fees on a new fund via forced commitments)?
   - **Negotiation leverage**: Can the buyer negotiate a lower staple ratio, fee concessions, or co-investment rights?

6. **Benchmark against market**
   - Compare the staple ratio to recent market norms for the strategy [VERIFY current market staple ratios — these shift with fundraising conditions]
   - Evaluate whether secondary pricing includes a meaningful concession to compensate for the staple obligation
   - Assess whether competing bids in the process are also stapled or if standalone bids are accepted

## Output

- **Staple Structure Summary**: Hard vs. soft staple, ratio, primary vehicle details, and any negotiated concessions
- **Return Analysis Table**: Standalone secondary IRR/MOIC, standalone primary IRR/MOIC, blended IRR/MOIC, and effective discount calculation
- **Cash Flow Waterfall**: Combined projection showing capital calls (primary) against distributions (secondary) with net cash position by quarter
- **Risk Assessment**: Adverse selection indicators, concentration impact, liquidity mismatch analysis, and GP alignment evaluation
- **Recommendation**: Proceed / negotiate modifications / decline, with specific suggested negotiation points (e.g., reduce staple ratio from 1:1 to 0.5:1, request management fee waiver on primary during investment period)

## Quality Checks

- Verify that blended return math correctly weights the secondary and primary components by committed capital, not NAV
- Confirm staple ratio is applied consistently (some GPs quote ratio against NAV, others against purchase price) [VERIFY basis for ratio calculation]
- Ensure cash flow projections for the primary use realistic call pacing — do not assume immediate full deployment
- Cross-check GP track record figures against an independent source (Preqin, Burgiss, Cambridge Associates) [VERIFY data provider access]
- Flag any scenario where blended returns are lower than a standalone secondary purchase at the same price — this indicates the staple is value-destructive
- Confirm that the analysis accounts for management fees and carry on both the secondary (if applicable) and primary components

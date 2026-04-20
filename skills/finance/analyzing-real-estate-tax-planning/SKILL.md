---
name: analyzing-real-estate-tax-planning
language: en
description: Evaluates real estate tax strategies including 1031 exchanges, opportunity zones, and cost segregation. Use when planning real estate tax, structuring 1031 exchanges, or analyzing cost segregation studies.
tags:
  - analysis
  - tax
metadata:
  author: casemark
  practice_areas:
    - Tax Planning
    - Tax Compliance
    - International Tax
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Real Estate Tax Planning

## When To Use

- Evaluating whether a property disposition qualifies for a Section 1031 like-kind exchange
- Assessing Qualified Opportunity Zone (QOZ) investments for capital gains deferral and exclusion
- Reviewing a cost segregation study to accelerate depreciation deductions
- Comparing hold-vs-sell-vs-exchange scenarios across multiple properties
- Analyzing cross-border real estate structures with international tax implications (treaty benefits, FIRPTA withholding, branch profits tax)
- Structuring acquisition or disposition to optimize basis allocation, depreciation schedules, and entity-level tax treatment

## Inputs To Gather

- **Property details**: Type (commercial, residential, mixed-use), location, acquisition date, purchase price, current fair market value, outstanding debt
- **Ownership structure**: Entity type (LLC, LP, S-corp, REIT, DST), number of owners, allocation provisions
- **Transaction specifics**: Proposed sale price, timeline, identified replacement properties (for 1031), capital gains amount and character (short-term vs. long-term)
- **Cost segregation data**: Engineering study report, asset classifications (5-year, 7-year, 15-year, 27.5/39-year), bonus depreciation elections already taken
- **Tax position**: Owner's marginal tax rate, net investment income tax (NIIT) exposure, passive activity loss carryforwards, prior Section 1231 gains/losses
- **QOZ specifics** (if applicable): Census tract designation, date of original capital gain, investment vehicle structure, substantial improvement plans
- **International elements** (if applicable): Foreign investor residency, treaty country, FIRPTA withholding status, branch vs. subsidiary structure

## Workflow

1. **Define scope** — Confirm which strategies are under evaluation (1031, QOZ, cost segregation, entity restructuring, or combination). Identify the taxable event and relevant tax years.

2. **Validate 1031 exchange eligibility** (if applicable)
   - Confirm both relinquished and replacement properties are held for investment or productive use in a trade or business [VERIFY: state conformity with federal 1031 rules]
   - Check 45-day identification and 180-day closing deadlines
   - Evaluate boot received (cash, debt relief, non-like-kind property) and resulting gain recognition
   - Assess related-party restrictions under IRC §1031(f)
   - For reverse exchanges, confirm compliance with Rev. Proc. 2000-37 parking arrangements

3. **Evaluate QOZ investment** (if applicable)
   - Verify the investment is in a designated Qualified Opportunity Zone [VERIFY: current census tract designation status]
   - Confirm capital gain was invested within 180 days of recognition event
   - Assess whether the Qualified Opportunity Fund (QOF) meets the 90% asset test
   - Evaluate substantial improvement requirements for existing buildings (doubling basis within 30 months)
   - Model deferral benefit (original gain deferred until 2026 or earlier disposition) and exclusion of post-investment appreciation after 10-year hold [VERIFY: current legislative status of QOZ incentives post-2026]

4. **Analyze cost segregation** (if applicable)
   - Review engineering study methodology (detailed engineering approach vs. residual estimation)
   - Validate asset reclassifications from 27.5/39-year to 5, 7, or 15-year recovery periods
   - Calculate present value of accelerated depreciation benefit at owner's marginal rate
   - Assess bonus depreciation applicability under IRC §168(k) [VERIFY: current bonus depreciation phase-down percentage for placed-in-service year]
   - Flag depreciation recapture exposure (§1245 ordinary income vs. §1250 unrecaptured gain at 25%) upon future disposition

5. **Model tax outcomes** — Build side-by-side comparison of scenarios:
   - Outright sale (federal + state capital gains, NIIT, depreciation recapture)
   - 1031 exchange (deferred gain, adjusted basis in replacement property)
   - QOZ investment (deferral value, exclusion value at 10-year mark)
   - Cost segregation impact on annual cash flow and effective tax rate
   - Combined strategies (e.g., cost segregation on replacement property post-1031)

6. **Address international considerations** (if applicable)
   - FIRPTA withholding obligations (15% of gross proceeds for foreign sellers) [VERIFY: current withholding rate and exemptions]
   - Treaty-based rate reductions or exemptions
   - Branch profits tax for foreign corporations
   - State-level withholding for nonresident sellers

7. **Synthesize findings** — Summarize the optimal strategy, quantify tax savings, and flag implementation risks, deadlines, and compliance requirements.

## Output

- **Executive summary**: Recommended strategy with estimated tax savings and key trade-offs
- **Scenario comparison table**: Side-by-side tax impact for each strategy analyzed (sale, exchange, QOZ, cost segregation)
- **Timeline and deadlines**: Critical dates (45-day ID period, 180-day closing, QOZ investment window, placed-in-service dates)
- **Risk factors**: Disqualification triggers, audit exposure areas, legislative uncertainty
- **Implementation checklist**: Qualified intermediary engagement, QOF formation steps, cost segregation study commissioning, entity restructuring actions
- **[VERIFY] items**: Consolidated list of jurisdiction-specific or time-sensitive points requiring confirmation

## Quality Checks

- All IRC section references are cited correctly and correspond to current law
- Tax rate assumptions match the owner's actual marginal bracket, not default rates
- 1031 timeline calculations account for weekends/holidays per Treasury Regulation rules
- Cost segregation benefit is calculated on a present-value basis, not nominal
- QOZ analysis reflects current legislative status (not outdated pre-extension assumptions)
- State tax conformity is flagged for every federal provision relied upon [VERIFY: state-by-state conformity for 1031, QOZ, bonus depreciation]
- Depreciation recapture is modeled in every disposition scenario, not just outright sale
- Net investment income tax (3.8%) is included where applicable
- All [VERIFY] markers are present for jurisdiction-dependent or time-sensitive items

---
name: structuring-real-asset-fund-vehicles
language: en
description: Designs fund structures for real asset strategies with long-dated commitments, NAV-based mechanics, and co-investment programs. Use when structuring resource funds, designing natural resource vehicles, or analyzing real asset fund terms.
tags:
  - real-assets-and-natural-resources
  - investment
metadata:
  author: casemark
  practice_areas:
    - Natural Resources
    - Energy Capital
    - Commodity Investment
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Real Asset Fund Vehicles

Designs fund structures for real asset strategies spanning natural resources, energy infrastructure, timberland, farmland, and commodity-linked investments. Addresses the unique structuring challenges of illiquid, long-dated asset classes including NAV-based economics, depletion-driven return profiles, and co-investment programs.

## When To Use

- Structuring a new closed-end or open-end fund targeting physical assets (mining, energy, agriculture, timber, water)
- Designing capital call mechanics and distribution waterfalls for resource funds with irregular cash flows
- Evaluating co-investment vehicle structures alongside a main fund
- Analyzing existing real asset fund terms for LP or GP advisory
- Comparing vehicle types (LP/GP, LLC, JV, trust) for a specific real asset strategy
- Structuring NAV-based credit facilities or subscription lines for real asset portfolios

## Inputs To Gather

- **Strategy type**: Commodity production, infrastructure, land/timber, royalties, or diversified real assets
- **Target asset characteristics**: Asset life, depletion schedule, capital intensity, cash flow profile (front-loaded vs. back-loaded)
- **Investor base**: Institutional LPs, sovereign wealth funds, family offices, retail-qualified investors
- **Target fund size and vintage**: Impacts minimum commitment thresholds, GP commit percentage, fee breakpoints
- **Jurisdiction and tax considerations**: Onshore vs. offshore feeder structures, UBTI/ECI sensitivity, withholding obligations [VERIFY]
- **Co-investment expectations**: Whether LPs expect deal-by-deal co-invest rights, allocation methodology, fee treatment on co-invest capital
- **Leverage policy**: Fund-level borrowing limits, subscription facility terms, asset-level project finance assumptions
- **Return targets**: Gross/net IRR, cash yield, total value to paid-in (TVPI), and DPI benchmarks

## Workflow

1. **Profile the asset class and return driver**
   - Identify whether returns are driven by commodity price, production volume, land appreciation, royalty streams, or infrastructure yield
   - Map expected cash flow timing — resource extraction funds often have a 3-5 year J-curve before production revenue; royalty funds may generate income from year one
   - Determine asset holding period and whether assets are depletable (minerals, oil/gas) vs. appreciating (farmland, timberland)

2. **Select the vehicle structure**
   - Closed-end LP/GP for finite-life resource extraction (typically 10-12 years plus extensions) [VERIFY fund term norms by sub-sector]
   - Evergreen or semi-liquid structures for income-producing real assets (timberland, farmland, infrastructure royalties)
   - Delaware LLC or Cayman exempted LP depending on investor tax profile — UBTI-sensitive investors (pensions, endowments) may require blocker entities [VERIFY]
   - Parallel fund / feeder structures for mixed domestic and offshore LPs

3. **Design capital deployment mechanics**
   - Capital call schedule aligned to acquisition pipeline — resource funds often front-load calls during acquisition phase
   - Recycling provisions: define whether disposition proceeds within investment period can be re-called (common for funds with lumpy deal flow)
   - Subscription credit facility sizing — typically 15-25% of uncalled commitments; consider NAV-based facilities for funds with appraised assets

4. **Structure economics and waterfall**
   - Management fee: commonly 1.5-2.0% on committed capital during investment period, stepping down to invested capital or NAV thereafter
   - Carried interest: standard 20% over 8% preferred return; resource funds may use deal-by-deal carry with a whole-fund clawback
   - GP catch-up: typically 80/20 after preferred return hurdle
   - Distribution frequency: quarterly for income-generating assets; event-driven for disposition-heavy strategies
   - NAV-based fee adjustments: for evergreen vehicles, fees may reference appraised NAV with independent valuation cadence (annual or semi-annual)

5. **Design co-investment program**
   - Define allocation policy: pro-rata to commitments, rotational, or discretionary
   - Fee and carry treatment: co-invest capital typically at reduced or zero management fee, with carry at 0-10%
   - SPV structure per deal vs. aggregator co-invest vehicle
   - Information rights and governance for co-investors (board observation, veto on dispositions)

6. **Address valuation and reporting**
   - Appraisal methodology: independent third-party valuations for NAV-dependent structures (USPAP for real property, reserve-based for oil/gas) [VERIFY applicable valuation standards by asset type]
   - Reporting cadence: quarterly NAV statements, annual audited financials, reserve/resource updates
   - Key metrics to report: IRR, TVPI, DPI, RVPI, production volumes, depletion rates, commodity price sensitivity

7. **Tax and regulatory structuring**
   - UBTI mitigation for tax-exempt investors via blocker corporations or leverage carve-outs [VERIFY current IRS guidance]
   - FIRPTA considerations for non-US investors holding US real property interests [VERIFY]
   - Depletion allowances and intangible drilling cost deductions for oil/gas funds — pass-through treatment benefits taxable LPs
   - State-level severance taxes and royalty obligations [VERIFY by jurisdiction]
   - ERISA plan asset considerations if benefit plan investors exceed 25% threshold

## Output

Deliver a structured fund design report containing:

- **Executive summary**: Strategy overview, vehicle type recommendation, target fund size
- **Structure diagram**: Visual representation of fund, feeder, blocker, co-invest, and GP entities
- **Term sheet**: Key economic terms (fees, carry, hurdle, fund life, extensions, recycling)
- **Waterfall illustration**: Modeled distribution waterfall with sample return scenarios (base, upside, downside)
- **Co-investment framework**: Allocation policy, fee terms, SPV mechanics
- **Tax structuring summary**: Entity selection rationale, UBTI/FIRPTA analysis, depletion treatment
- **Valuation protocol**: Appraisal methodology, frequency, NAV calculation mechanics
- **Risk factors**: Commodity price exposure, regulatory risk, illiquidity, concentration limits

## Quality Checks

- Waterfall math reconciles — total distributions to LP and GP sum to 100% of distributable proceeds
- Preferred return and catch-up mechanics are internally consistent with stated hurdle rate
- Fee step-downs trigger correctly at specified milestones (end of investment period, deployment thresholds)
- Co-invest economics do not create misalignment between main fund LPs and co-investors
- Tax structure addresses UBTI, FIRPTA, and withholding for each investor category identified
- NAV calculation methodology is consistent with the chosen fee basis (committed, invested, or appraised NAV)
- All jurisdiction-dependent terms, tax rates, and regulatory thresholds are marked [VERIFY]
- Fund term and extension provisions are realistic for the asset class holding period

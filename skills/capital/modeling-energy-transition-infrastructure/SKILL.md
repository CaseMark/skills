---
name: modeling-energy-transition-infrastructure
description: Assesses energy transition investments with battery storage, grid modernization, EV charging, and hydrogen infrastructure analysis. Use when modeling energy transition assets, evaluating storage economics, or analyzing grid infrastructure.
tags:
  - modeling
  - infrastructure-and-project-finance
  - investment
metadata:
  author: casemark
  practice_areas:
    - Project Finance
    - Infrastructure Investment
    - PPP
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Energy Transition Infrastructure

Assesses energy transition investments with battery storage, grid modernization, EV charging, and hydrogen infrastructure analysis.

## When To Use

- Modeling project-financed battery energy storage systems (BESS) for merchant or contracted revenue structures
- Evaluating grid modernization capital programs (T&D upgrades, smart grid, DERMS platforms)
- Sizing and financing EV charging networks across depot, fleet, and public-access configurations
- Analyzing green/blue hydrogen production, storage, and offtake economics
- Structuring blended capital stacks with ITC/PTC, state incentives, and concessional finance layers
- Comparing energy transition assets on a risk-adjusted return basis for infrastructure fund deployment

## Inputs To Gather

- **Asset specification**: technology type, nameplate capacity (MW/MWh), degradation curves, round-trip efficiency (storage), utilization assumptions
- **Revenue structure**: PPA/tolling terms, capacity market clearing prices, energy arbitrage spreads, ancillary service revenue, demand charge savings, REC/carbon credit pricing [VERIFY market-specific pricing]
- **Capital costs**: EPC contract pricing or benchmark $/kW and $/kWh, interconnection costs, land/easement costs, development fees
- **Operating costs**: O&M contracts (fixed and variable $/kW-yr), augmentation capex schedule (BESS), insurance, property tax, land lease escalators
- **Financing terms**: senior debt tenor and pricing, debt service coverage ratios (DSCR), cash sweep mechanics, equity return hurdles (levered IRR, cash-on-cash), construction facility terms
- **Incentives and policy**: ITC/PTC eligibility and phase-down schedule [VERIFY current IRC provisions], state-level incentives, prevailing wage/apprenticeship bonus credit requirements, domestic content adder eligibility
- **Offtake/counterparty**: creditworthiness of offtaker, contract tenor, curtailment risk allocation, merchant tail exposure

## Workflow

1. **Classify the asset and revenue model**
   - Identify technology (BESS, T&D, EVCI, hydrogen electrolyzer, etc.) and primary revenue pathway (contracted vs. merchant vs. hybrid)
   - For BESS: determine use case stack (energy arbitrage, frequency regulation, capacity, resource adequacy, T&D deferral) and whether revenues are co-optimized or siloed
   - For hydrogen: classify by color (green/blue/pink), map electrolyzer technology (PEM vs. alkaline vs. SOEC), and define offtake structure (tolling, merchant, hub pricing)

2. **Build the operating model**
   - Construct hourly or sub-hourly dispatch profile for storage assets; use 8760 analysis where arbitrage is a material revenue source
   - Model degradation: capacity fade curves for lithium-ion (typically 2–3% annual with augmentation strategy), efficiency degradation for electrolyzers
   - For EV charging: model utilization ramp (typically 3–7 year curve to stabilization), energy throughput per charger, demand charge exposure, and network effects across sites
   - For grid modernization: model regulated rate-base treatment, allowed ROE, and capital deployment schedule across multi-year programs

3. **Structure the capital stack**
   - Layer ITC/PTC benefits — determine whether tax equity, transferability (post-IRA), or direct pay is optimal [VERIFY entity tax status and election availability]
   - Size senior debt to target DSCR (typically 1.30–1.50x for contracted BESS; higher for merchant exposure); model sculpted amortization where appropriate
   - For PPP structures: model availability-based payments, handback provisions, and lifecycle reserve funding
   - Calculate levered equity returns (IRR, MOIC, cash yield) with and without incentive scenarios

4. **Run revenue and risk scenarios**
   - Energy price scenarios: base, high, low, and stress cases using forward curves and fundamental supply/demand analysis
   - Technology risk: sensitivity on degradation rate, replacement capex timing, and efficiency assumptions
   - Policy risk: model returns with and without ITC/PTC, with and without state incentives; quantify breakeven incentive level
   - Counterparty risk: evaluate impact of offtaker default or contract termination on debt coverage and equity returns
   - For hydrogen: sensitivity on electrolyzer capex learning curve, electricity input cost, and offtake price indexation

5. **Produce output tables and investment memo inputs**
   - Summary returns table: unlevered IRR, levered IRR, MOIC, cash-on-cash by year, payback period
   - Debt metrics: DSCR profile, average DSCR, minimum DSCR, debt yield
   - Waterfall: sources and uses, construction draw schedule, annual cash flow waterfall (revenue → opex → debt service → cash sweep → equity distributions)
   - Sensitivity matrix: 2-way tables on key variables (e.g., capacity price vs. degradation rate; electricity cost vs. hydrogen offtake price)

## Output

- **Pro forma financial model** with annual (and sub-annual where needed) projections over asset life (typically 20–30 years for storage/grid; 15–20 for EV/hydrogen)
- **Returns summary** with base, upside, and downside scenarios clearly separated
- **Capital structure recommendation** with optimal debt sizing, tax equity or transfer pricing, and incentive monetization strategy
- **Risk register** mapping each key assumption to its sensitivity impact on levered IRR and DSCR
- **Investment committee memo inputs**: executive summary, asset description, market context, financial summary, risk factors, and recommendation

## Quality Checks

- Confirm DSCR never breaches lockup or default levels in base case; document minimum DSCR year and driver
- Verify balance sheet balances in every period (total assets = total liabilities + equity)
- Check that degradation and augmentation assumptions align with manufacturer warranties and independent engineer reports [VERIFY]
- Validate ITC/PTC calculations against current IRS guidance and bonus credit qualification requirements [VERIFY]
- Ensure merchant revenue assumptions are supportable by recent market data (ISO clearing prices, REC auction results, hydrogen hub pricing indices)
- Cross-check $/kW and $/kWh capital cost assumptions against recent comparable transactions and NREL/Lazard benchmarks
- Confirm discount rate and WACC assumptions reflect current market pricing for comparable risk-profile assets
- Flag any input where source data is older than 12 months or drawn from a different jurisdiction with [VERIFY]

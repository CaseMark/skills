---
name: building-roic-analysis-frameworks
description: Constructs ROIC decomposition with invested capital measurement, operating return analysis, and value creation vs destruction assessment. Use when analyzing ROIC, building capital return frameworks, or assessing value creation.
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
    - Model
  skill_modes:
    - Modeling
---
# Building Roic Analysis Frameworks

Constructs ROIC decomposition with invested capital measurement, operating return analysis, and value creation vs destruction assessment.

## When To Use

- Evaluating whether a company earns returns above or below its cost of capital
- Decomposing ROIC into operating margin and capital turnover drivers
- Comparing capital efficiency across business units, peers, or time periods
- Assessing whether M&A, capex programs, or reinvestment are creating or destroying value
- Building a DuPont-style ROIC bridge for board or investor presentations

## Inputs To Gather

- **Income statement**: Revenue, EBIT or NOPAT, tax rate (effective vs. statutory) [VERIFY statutory rate by jurisdiction]
- **Balance sheet**: Total assets, current liabilities (excluding debt), goodwill and intangibles (for invested capital variants)
- **Capital structure**: Short-term and long-term debt, operating lease obligations (post-ASC 842 / IFRS 16 treatment) [VERIFY lease capitalization method]
- **WACC inputs**: Cost of equity (risk-free rate, beta, equity risk premium), cost of debt (pre-tax yield, marginal tax rate), target capital weights
- **Peer data**: Comparable company ROIC, invested capital composition, and margin/turnover benchmarks
- **Time horizon**: Number of historical periods (minimum 3–5 years for trend analysis) and any forecast periods

## Workflow

1. **Calculate NOPAT**
   - Start with EBIT; apply a cash operating tax rate (not GAAP effective rate)
   - Exclude non-recurring items: restructuring charges, litigation settlements, asset impairments
   - Decide on treatment of stock-based compensation (include for economic ROIC; exclude for cash ROIC variant)
   - Adjust for operating lease interest if using pre-capitalization financials [VERIFY whether filings already capitalize leases]

2. **Measure Invested Capital**
   - **Operating approach**: Net working capital + net PP&E + capitalized leases + other operating assets − non-debt current liabilities
   - **Financing approach**: Total debt + equity − excess cash − non-operating assets
   - Reconcile both approaches; material discrepancies indicate classification errors
   - Choose average vs. beginning-of-period invested capital (beginning-period avoids circularity in forecasting; average better reflects capital deployed during the period)
   - Decide on goodwill inclusion: with goodwill = acquisition ROIC (tests deal value); without goodwill = organic operating ROIC

3. **Compute ROIC and Decompose**
   - ROIC = NOPAT ÷ Invested Capital
   - Decompose via DuPont: ROIC = NOPAT Margin × Capital Turnover
   - NOPAT Margin = NOPAT ÷ Revenue
   - Capital Turnover = Revenue ÷ Invested Capital
   - Further decompose margin into gross margin, SG&A efficiency, R&D intensity
   - Further decompose turnover into fixed asset turnover, working capital turns (DSO, DIO, DPO)

4. **Assess Value Creation vs. Destruction**
   - Calculate ROIC − WACC spread; positive spread = value creation
   - Compute Economic Profit (EP) = Invested Capital × (ROIC − WACC)
   - Track EP trend over time: improving spread on growing capital base = compounding value creation
   - Flag segments or periods where ROIC < WACC persistently (value destruction zones)
   - For multi-segment companies, allocate invested capital by segment and compute segment-level ROIC [VERIFY segment asset allocation methodology in 10-K notes]

5. **Build Comparative and Trend Analysis**
   - Benchmark ROIC, margin, and turnover against 4–6 direct peers
   - Construct ROIC bridge: walk from prior period to current showing contribution of margin change vs. turnover change
   - Run sensitivity analysis on key drivers: what margin improvement is needed to achieve ROIC = WACC + 300 bps?
   - For M&A assessment: model pro-forma invested capital including deal goodwill and synergies; test whether post-deal ROIC exceeds WACC within 3 years

## Output

- **ROIC summary table**: NOPAT, invested capital, ROIC, WACC, and EP for each period analyzed
- **DuPont decomposition chart**: margin and turnover components with period-over-period changes
- **Value creation waterfall**: EP by segment or business unit, showing contribution to total firm EP
- **Peer benchmarking matrix**: ROIC, ROIC−WACC spread, margin, and turnover for each comparable
- **Sensitivity table**: ROIC under varying margin, turnover, and WACC assumptions
- **Key findings narrative**: 2–3 paragraphs summarizing whether the company creates value, where ROIC is trending, and which lever (margin vs. turnover) offers greatest improvement potential

## Quality Checks

- NOPAT reconciles to reported EBIT after tax adjustments within 2% tolerance
- Invested capital calculated via operating and financing approaches matches within 5% (or discrepancies are explained)
- ROIC for mature, stable businesses falls within plausible range (typically 5–25%); outliers flagged and investigated
- WACC inputs sourced from current market data; beta and ERP are not stale [VERIFY date of market data]
- Goodwill-inclusive and goodwill-exclusive ROIC both presented when acquisitions are material
- All non-recurring adjustments individually listed with source references
- Sensitivity ranges are symmetric and cover at least ±200 bps on WACC and ±200 bps on NOPAT margin

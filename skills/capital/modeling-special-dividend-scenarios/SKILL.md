---
name: modeling-special-dividend-scenarios
description: Analyzes special dividend catalysts with balance sheet capacity, tax efficiency, and shareholder return comparison analysis. Use when modeling special dividends, evaluating capital return catalysts, or assessing dividend capacity.
tags:
  - modeling
  - activist-and-event-driven-investing
  - tax
metadata:
  author: casemark
  practice_areas:
    - Activist Investing
    - Event-Driven Strategy
    - Special Situations
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Special Dividend Scenarios

## When To Use

- An activist campaign is evaluating whether a target company has excess cash or under-leveraged balance sheet capacity to fund a special dividend
- Assessing a special dividend as an alternative or complement to share buybacks, debt paydown, or M&A
- Modeling the shareholder return impact of a one-time cash distribution triggered by an asset sale, litigation recovery, or business unit divestiture
- Evaluating tax efficiency of a special dividend versus other capital return mechanisms for the shareholder base
- Stress-testing balance sheet capacity to determine maximum supportable dividend without breaching covenants or impairing operations

## Inputs To Gather

- **Balance sheet data**: Cash and equivalents, short-term investments, restricted cash, total debt, net debt, and working capital (most recent quarter and trailing four quarters)
- **Debt covenants**: Leverage ratio caps (Net Debt / EBITDA), minimum liquidity thresholds, restricted payment baskets, and any incurrence-based vs. maintenance-based distinctions [VERIFY against credit agreement]
- **Cash flow profile**: LTM and projected FCF, capex requirements (maintenance vs. growth), mandatory debt amortization, and seasonal working capital swings
- **Share count**: Basic and diluted shares outstanding, treasury shares, and any pending conversions or option exercises that affect per-share math
- **Tax parameters**: Qualified vs. non-qualified dividend treatment, corporate-level tax on repatriated foreign cash (if applicable), shareholder-level tax rates for institutional vs. retail holders [VERIFY jurisdiction-specific rates]
- **Catalyst details**: Source of excess capital (asset sale proceeds, litigation settlement, spin-off, accumulated cash), timing, and any contractual restrictions on use of proceeds
- **Comparables**: Precedent special dividends in the sector — size as % of market cap, stock price reaction, and payout ratios

## Workflow

1. **Determine excess capital capacity**
   - Calculate unrestricted cash, net of minimum operating cash buffer (typically 3–6 months of operating expenses or management-stated floor)
   - Assess incremental debt capacity: headroom under covenant limits at current EBITDA, and pro forma leverage post-dividend
   - Identify any trapped cash (foreign subsidiaries, regulated entity capital requirements, restricted payment baskets) and estimate repatriation cost

2. **Size the special dividend**
   - Model three scenarios: conservative (cash-only, no incremental debt), base (partial leverage), and aggressive (full covenant headroom utilization)
   - Express each as total dollar amount, per-share amount, and yield on current stock price
   - Verify that each scenario leaves adequate liquidity for operations, near-term maturities, and a reasonable cushion (typically 1.0–1.5x minimum covenant thresholds)

3. **Compare capital return alternatives**
   - Build a side-by-side matrix: special dividend vs. accelerated buyback vs. tender offer vs. debt paydown
   - Key metrics for comparison: after-tax value per share to holders, EPS accretion/dilution, impact on leverage ratios, and signaling effect
   - For buybacks, model at various price assumptions (current, +10%, +20%) to capture execution risk

4. **Assess tax efficiency**
   - Model after-tax proceeds to shareholders under qualified dividend rates vs. return-of-capital treatment (if tax basis supports it) [VERIFY current tax rates and holding period requirements]
   - Compare to buyback tax treatment (capital gains rate, timing of realization, and impact of the 1% excise tax on corporate repurchases post-IRA) [VERIFY current excise tax applicability]
   - Note differential impact on tax-exempt holders (pensions, endowments) vs. taxable holders

5. **Run sensitivity and scenario analysis**
   - Sensitize on: EBITDA (±10–20%), cash balance assumptions, interest rates on incremental debt, share price (affects yield and buyback comparison), and tax rate changes
   - Model a downside case: what happens if EBITDA declines 20% post-dividend — does the company breach covenants or face a liquidity shortfall?
   - Calculate breakeven: at what share price does a buyback deliver superior per-share value vs. the special dividend?

6. **Build the catalyst timeline**
   - Map board approval requirements, record date / ex-date mechanics, and any required lender consent or covenant waiver timeline
   - For activist-driven scenarios, align the dividend proposal with proxy season calendar, 13D filing dates, or settlement negotiation windows

## Output

- **Executive summary**: Recommended dividend amount per share across scenarios with key supporting rationale
- **Capacity analysis table**: Unrestricted cash, debt headroom, total available capital, minimum liquidity floor, and maximum distributable amount
- **Scenario matrix**: Conservative / base / aggressive columns showing total payout, per-share amount, dividend yield, pro forma leverage, and pro forma liquidity
- **Capital return comparison**: Side-by-side table of special dividend vs. buyback vs. tender offer with after-tax shareholder value, EPS impact, and leverage impact
- **Tax efficiency analysis**: After-tax value per share by holder type (taxable individual, tax-exempt, corporate)
- **Sensitivity tables**: Tornado charts or data tables on EBITDA, cash, interest rate, and share price assumptions
- **Risk flags**: Covenant proximity warnings, liquidity stress results, and any [VERIFY] items requiring confirmation

## Quality Checks

- Per-share amounts reconcile to total payout divided by correct diluted share count
- Pro forma leverage ratios are calculated on the same EBITDA basis used in the covenant definitions (not adjusted EBITDA unless the covenant permits it) [VERIFY covenant EBITDA definition]
- Minimum cash / liquidity buffers account for seasonal troughs, not just spot balances
- Tax rate assumptions match current law and are flagged for any pending legislative changes
- Buyback comparison uses realistic execution assumptions (not 100% of volume; typically 10–25% of ADTV)
- All covenant calculations tie to the actual credit agreement terms, not approximations — mark [VERIFY] if working from summary descriptions rather than the executed agreement
- Downside scenario confirms no covenant breach or, if a breach occurs, the analysis explicitly flags the required waiver or amendment

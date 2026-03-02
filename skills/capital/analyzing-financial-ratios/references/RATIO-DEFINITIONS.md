# Ratio Definitions & Interpretation Guide

Complete reference for all financial ratios used in the `analyzing-financial-ratios` skill. Each ratio includes the exact formula, input definitions, and interpretation guidance.

---

## 1. Liquidity Ratios

Measure a company's ability to meet short-term obligations.

### Current Ratio

```
Current Ratio = Total Current Assets / Total Current Liabilities
```

- **Inputs**: Current assets (cash, receivables, inventory, prepaid); current liabilities (AP, accrued expenses, short-term debt, current portion of LTD)
- **Interpretation**: > 1.0 means short-term assets cover short-term liabilities. Industry-dependent — retailers often operate below 1.0 due to fast inventory turns; utilities are typically 0.8–1.2.
- **Watch**: > 3.0 may signal excess idle assets. < 1.0 requires cash flow analysis to confirm liquidity adequacy.

### Quick Ratio (Acid Test)

```
Quick Ratio = (Cash + Short-Term Investments + Accounts Receivable) / Total Current Liabilities
```

- **Inputs**: Excludes inventory and prepaid expenses from current assets
- **Interpretation**: More conservative than current ratio. Critical for companies with slow-moving or perishable inventory (manufacturing, retail).
- **Watch**: Significant gap between current and quick ratios signals inventory-heavy balance sheet.

### Cash Ratio

```
Cash Ratio = (Cash + Cash Equivalents + Short-Term Investments) / Total Current Liabilities
```

- **Inputs**: Only the most liquid assets
- **Interpretation**: Most conservative liquidity measure. Relevant for distressed companies, startups, or during credit crises. Most healthy companies have cash ratios well below 1.0.

---

## 2. Profitability Ratios

Measure how effectively a company converts revenue into profit at various levels.

### Gross Margin

```
Gross Margin = (Revenue − COGS) / Revenue × 100
```

- **Inputs**: Revenue (net of returns/discounts); COGS (direct materials, labor, manufacturing overhead)
- **Interpretation**: Reflects pricing power and production efficiency. Software: 70–85%. Retail: 25–45%. Manufacturing: 30–50%.
- **Watch**: Declining gross margin = input cost inflation, competitive pricing pressure, or unfavorable product mix shift.

### Operating Margin (EBIT Margin)

```
Operating Margin = EBIT / Revenue × 100
```

- **GAAP EBIT**: Revenue − COGS − SGA − R&D − D&A (operating income per income statement)
- **Adjusted EBIT**: GAAP EBIT + SBC + restructuring + other one-time items
- **Interpretation**: Measures core operational profitability before capital structure effects. Always present both GAAP and adjusted.
- **Watch**: Expanding adjusted margins with flat GAAP margins = growing SBC or recurring "one-time" charges.

### Net Profit Margin

```
Net Margin = Net Income / Revenue × 100
```

- **Inputs**: Net income attributable to common shareholders (after tax, interest, minority interest)
- **Interpretation**: Bottom-line profitability. Heavily influenced by tax rate and capital structure — less useful for cross-border or cross-capital-structure comparisons.

### EBITDA Margin

```
EBITDA Margin = EBITDA / Revenue × 100
EBITDA = EBIT + Depreciation + Amortization
```

- **Adjusted EBITDA**: Add back SBC, restructuring, acquisition costs per management reconciliation
- **Interpretation**: Proxy for cash operating profitability. Widely used but criticized — ignores capex needs, working capital, and tax. Always pair with FCF analysis.

### Return on Equity (ROE)

```
ROE = Net Income / Average Shareholders' Equity × 100
Average Equity = (Beginning Equity + Ending Equity) / 2
```

- **Interpretation**: Return generated on shareholder investment. Must be decomposed via DuPont to understand drivers. High ROE from leverage is fundamentally different from high ROE from margins.
- **Watch**: Negative equity makes ROE meaningless — switch to ROA or ROIC.

### Return on Assets (ROA)

```
ROA = Net Income / Average Total Assets × 100
```

- **Inputs**: Use average total assets to smooth seasonal or acquisition-driven balance sheet changes
- **Interpretation**: How efficiently assets generate profit regardless of financing. Asset-light businesses (software, services) naturally have higher ROA than asset-heavy (utilities, manufacturing).
- **Variant**: Some analysts use EBIT × (1 − Tax Rate) / Avg Assets to remove capital structure effect.

### Return on Invested Capital (ROIC)

```
ROIC = NOPAT / Average Invested Capital × 100
NOPAT = EBIT × (1 − Effective Tax Rate)
Invested Capital = Total Equity + Total Debt − Cash − Short-Term Investments
```

- **Alternative IC definition**: Net Working Capital + Net PP&E + Net Intangibles + Other LT Operating Assets
- **Interpretation**: The most comprehensive return metric. Measures return on all capital deployed (debt + equity) net of excess cash. **ROIC > WACC = value creation. ROIC < WACC = value destruction.**
- **Watch**: Goodwill treatment matters significantly. Compute both including and excluding goodwill for acquisition-heavy companies.

---

## 3. Leverage Ratios

Measure the degree and sustainability of debt financing.

### Debt-to-Equity Ratio

```
Debt / Equity = Total Debt / Total Shareholders' Equity
Total Debt = Short-Term Debt + Current Portion of LTD + Long-Term Debt
```

- **Adjusted version**: Add capitalized operating leases and unfunded pension obligations to debt
- **Interpretation**: Measures financial risk from creditor vs. shareholder funding. Industry-dependent — banks: 8–12x; utilities: 1–2x; tech: 0–0.5x.
- **Watch**: Negative equity (accumulated losses exceed contributed capital) renders this ratio meaningless.

### Total Debt / EBITDA

```
Debt / EBITDA = Total Debt / EBITDA
```

- **Adjusted version**: Include operating lease liabilities in debt; use adjusted EBITDA
- **Interpretation**: The most widely used leverage metric in credit analysis. Investment grade typically < 3.0x. High yield: 3.0–6.0x. Leveraged loans: 4.0–7.0x.
- **Watch**: EBITDA is a point-in-time measure — assess leverage at different points in the business cycle.

### Net Debt / EBITDA

```
Net Debt / EBITDA = (Total Debt − Cash − Short-Term Investments) / EBITDA
```

- **Interpretation**: Adjusts for available cash. Negative net debt = net cash position (common in tech). Preferred by many analysts as it reflects true payoff burden.
- **Watch**: Cash may be trapped offshore, restricted, or needed for operations — not all cash is equally available for debt reduction.

### Interest Coverage Ratio

```
Interest Coverage = EBIT / Interest Expense
```

- **Alternative**: EBITDA / Interest Expense (less conservative)
- **Interpretation**: Times earnings cover interest obligations. < 1.0 = not earning enough to cover interest. < 2.0 = credit stress. > 5.0 = comfortable. Rating agencies weight this heavily.
- **Watch**: Cash interest may differ from reported interest expense due to PIK, amortization of debt issuance costs.

### Fixed Charge Coverage Ratio

```
Fixed Charge Coverage = (EBIT + Lease Payments) / (Interest Expense + Lease Payments + Mandatory Principal Repayments)
```

- **Interpretation**: Broader than interest coverage — includes all fixed obligations. Critical for companies with significant lease exposure (airlines, retail).
- **Watch**: Mandatory debt repayments from amortizing term loans can dramatically reduce this ratio.

### Debt Service Coverage Ratio (DSCR)

```
DSCR = Cash Flow from Operations / Total Debt Service
Total Debt Service = Interest Payments + Scheduled Principal Repayments
```

- **Interpretation**: Cash-based coverage metric preferred in project finance and real estate. < 1.0x = insufficient cash flow to service debt. Lenders typically require 1.2–1.5x minimum.

---

## 4. Efficiency Ratios

Measure how effectively a company manages its operating assets and liabilities.

### Asset Turnover

```
Asset Turnover = Revenue / Average Total Assets
```

- **Interpretation**: Revenue generated per dollar of assets. Higher = more efficient. Key driver in DuPont decomposition. Asset-light models (software): 0.5–1.0x. Retail: 1.5–3.0x. Heavy industry: 0.3–0.6x.
- **Watch**: Declining asset turnover after acquisitions (goodwill inflating asset base) is normal but must be tracked.

### Inventory Turnover

```
Inventory Turnover = COGS / Average Inventory
Days Inventory Outstanding (DIO) = 365 / Inventory Turnover
```

- **Inputs**: Use COGS (not revenue) in numerator for accuracy; average inventory over the period
- **Interpretation**: How quickly inventory is sold. Higher = faster turns. Grocery: 12–20x. Apparel: 4–8x. Industrial: 4–6x.
- **Watch**: Declining turnover with rising inventory = potential obsolescence, demand weakness, or channel stuffing.

### Days Sales Outstanding (DSO)

```
DSO = (Average Accounts Receivable / Revenue) × 365
```

- **Alternative**: Period-end AR / (Revenue / 365)
- **Interpretation**: Average days to collect receivables. Lower = faster collection. B2B companies: 30–60 days typical. B2C: < 15 days.
- **Watch**: DSO increasing faster than revenue growth = deteriorating collection quality, customer distress, or aggressive revenue recognition. Compare to payment terms in customer contracts.

### Days Payable Outstanding (DPO)

```
DPO = (Average Accounts Payable / COGS) × 365
```

- **Interpretation**: Average days to pay suppliers. Higher = retaining cash longer. Powerful buyers (Walmart, Amazon): 60–90+ days. Most companies: 30–45 days.
- **Watch**: Rapidly increasing DPO may signal liquidity problems rather than negotiating power — check against liquidity ratios.

### Cash Conversion Cycle (CCC)

```
CCC = DSO + DIO − DPO
```

- **Interpretation**: Days between paying for inputs and collecting from customers. Lower or negative = more efficient. Negative CCC (Amazon model) = company is funded by suppliers/customers.
- **Watch**: Lengthening CCC = deteriorating working capital efficiency. Decompose into components to identify the driver.

---

## 5. DuPont Decomposition

### Three-Component DuPont

```
ROE = Net Profit Margin × Asset Turnover × Equity Multiplier

Where:
  Net Profit Margin = Net Income / Revenue
  Asset Turnover    = Revenue / Average Total Assets
  Equity Multiplier = Average Total Assets / Average Shareholders' Equity
```

### Five-Component DuPont (Extended)

```
ROE = Tax Burden × Interest Burden × EBIT Margin × Asset Turnover × Equity Multiplier

Where:
  Tax Burden     = Net Income / Pre-Tax Income
  Interest Burden = Pre-Tax Income / EBIT
  EBIT Margin    = EBIT / Revenue
  Asset Turnover = Revenue / Average Total Assets
  Equity Multiplier = Average Total Assets / Average Shareholders' Equity
```

- **Use 5-component when**: comparing companies across tax jurisdictions or with materially different capital structures, to isolate operational efficiency from financing and tax effects.

---

## 6. Non-GAAP Adjustment Reference

When computing adjusted metrics, apply these standard adjustments and label clearly:

| Item | Add Back to EBITDA? | Add Back to EBIT? | Notes |
|---|---|---|---|
| Stock-based compensation | Yes (market practice) | Yes (if adjusted) | Always show both GAAP and adjusted; note dilution impact separately |
| Restructuring charges | Yes | Yes | Only if genuinely non-recurring; flag if recurring pattern |
| Acquisition/integration costs | Yes | Yes | Limited to identifiable transaction and integration expenses |
| Asset impairments | Yes | Yes | Goodwill, intangible, and long-lived asset write-downs |
| Litigation settlements | Yes | Yes | Material settlements outside ordinary course |
| Gain/loss on asset sales | Yes | Yes | Non-operating dispositions |
| Amortization of acquired intangibles | No (already in D&A) | Yes (common in tech) | Distinguish from internally developed intangible amortization |
| Operating lease adjustment | See below | See below | Capitalize leases; add to debt; adjust D&A and interest |

**Rule**: If a company reports a "one-time" item in 3+ consecutive years, it is not one-time. Flag and discuss whether to adjust.

---

## Interpretation Quick Reference

| Metric | Generally Strong | Generally Weak | Context Dependency |
|---|---|---|---|
| Current Ratio | > 1.5 | < 1.0 | Retail/subscription models can operate lower |
| Quick Ratio | > 1.0 | < 0.5 | Less relevant for service businesses |
| Gross Margin | Expanding, above peers | Contracting, below peers | Highly industry-specific |
| Operating Margin | > peer median, stable/expanding | Below peer median, contracting | SBC treatment critical in tech |
| ROIC | > WACC | < WACC | The definitive value creation test |
| Debt / EBITDA | < 3.0x (IG); < 5.0x (HY) | > 5.0x for non-utility | Must assess through the cycle |
| Interest Coverage | > 5.0x | < 2.0x | Fixed-rate vs. floating-rate matters |
| DSO | Stable or declining | Growing faster than revenue | Compare to contractual payment terms |
| CCC | Low or negative | Lengthening trend | Industry norms vary dramatically |

**Critical principle**: No ratio threshold is universally "good" or "bad." Always interpret within industry context, business model, and economic cycle position.

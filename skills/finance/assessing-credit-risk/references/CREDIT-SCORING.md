# Credit Scoring Methodology

## Internal Risk Rating Scale

A typical 10-point internal rating scale mapped to external agency equivalents:

| Internal | Description | S&P Equiv | Moody's Equiv | Default Probability (1yr) |
|----------|-----------|-----------|--------------|--------------------------|
| 1 | Minimal risk | AAA/AA+ | Aaa/Aa1 | 0.01-0.02% |
| 2 | Low risk | AA/AA- | Aa2/Aa3 | 0.03-0.04% |
| 3 | Satisfactory | A+/A | A1/A2 | 0.05-0.10% |
| 4 | Adequate | A-/BBB+ | A3/Baa1 | 0.12-0.20% |
| 5 | Acceptable | BBB/BBB- | Baa2/Baa3 | 0.25-0.50% |
| 6 | Watch | BB+/BB | Ba1/Ba2 | 0.75-1.50% |
| 7 | Substandard | BB-/B+ | Ba3/B1 | 2.0-4.0% |
| 8 | Doubtful | B/B- | B2/B3 | 5.0-10.0% |
| 9 | Loss likely | CCC+ and below | Caa1 and below | 15-30% |
| 10 | Loss | D | D | Default |

## Financial Scoring Matrix

### Revenue/Size Score (10% weight)

| Annual Revenue | Score |
|---------------|-------|
| > $500M | 1 |
| $100M - $500M | 2 |
| $50M - $100M | 3 |
| $10M - $50M | 4 |
| < $10M | 5 |

### Leverage Score (25% weight)

| Debt/EBITDA | Score |
|------------|-------|
| < 1.0x | 1 |
| 1.0-2.0x | 2 |
| 2.0-3.0x | 3 |
| 3.0-4.0x | 4 |
| > 4.0x | 5 |

### Coverage Score (25% weight)

| DSCR | Score |
|------|-------|
| > 2.5x | 1 |
| 2.0-2.5x | 2 |
| 1.5-2.0x | 3 |
| 1.25-1.5x | 4 |
| < 1.25x | 5 |

### Profitability Score (15% weight)

| EBITDA Margin | Score |
|-------------|-------|
| > 25% | 1 |
| 15-25% | 2 |
| 10-15% | 3 |
| 5-10% | 4 |
| < 5% | 5 |

### Qualitative Factors (25% weight)

| Factor | Assessment Criteria |
|--------|-------------------|
| Management quality | Track record, depth, succession, governance |
| Industry position | Market share, competitive advantages, barriers to entry |
| Industry outlook | Growth, cyclicality, regulatory risk |
| Customer concentration | Top customer %, diversification |
| Collateral quality | Type, LTV, liquidity of collateral |

## DSCR Calculation

```
DSCR = Net Operating Income / Total Debt Service

Where:
  Net Operating Income = EBITDA - Taxes - Maintenance CapEx - Unfunded CapEx
  Total Debt Service = Principal Payments + Interest Payments + Lease Payments
```

Minimum DSCR by loan type:
| Loan Type | Minimum DSCR |
|-----------|-------------|
| Senior secured | 1.20x |
| Real estate (stabilized) | 1.25x |
| Real estate (construction) | 1.10x (projected) |
| Leveraged/acquisition | 1.10x |
| Investment grade unsecured | 1.50x |

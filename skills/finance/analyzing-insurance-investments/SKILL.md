---
name: analyzing-insurance-investments
description: Evaluates insurance company investment portfolios with ALM considerations and regulatory constraints. Use when analyzing insurer investments, managing ALM, or evaluating portfolio compliance.
tags:
  - analysis
  - insurance
  - compliance
  - regulatory
metadata:
  author: casemark
  practice_areas:
    - Insurance
    - Actuarial Science
    - Reinsurance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Insurance Investments

Evaluates insurance company investment portfolios with asset-liability management (ALM) considerations, statutory accounting constraints, and regulatory capital implications.

## When To Use

- Reviewing an insurer's invested asset portfolio for concentration risk, credit quality, or duration mismatch
- Assessing ALM alignment between policy liabilities (reserves) and supporting investment assets
- Evaluating compliance with state investment statutes or NAIC model investment law limits
- Analyzing portfolio impact on risk-based capital (RBC) ratios or BCAR/AM Best scores
- Comparing portfolio allocation against peer insurers or rating agency benchmarks
- Reviewing reinsurer collateral trusts or funds-withheld asset pools

## Inputs To Gather

- **Schedule D / Schedule DA filings** — statutory investment schedules from the insurer's annual or quarterly statement
- **Investment policy statement (IPS)** — board-approved guidelines on asset classes, credit quality floors, duration bands, and concentration limits
- **Liability profile** — reserve breakdown by line of business, loss payout patterns, and duration of liabilities
- **RBC filing or capital model output** — C-1 (asset risk) and C-3 (interest rate risk) factor charges [VERIFY: confirm whether entity is life, P&C, or health — RBC formulas differ]
- **Rating agency criteria** — AM Best BCAR, S&P capital model, or Moody's requirements applicable to the entity
- **Domiciliary state investment statute** — quantitative limits on asset classes, single-issuer caps, and admitted/non-admitted asset rules [VERIFY: varies by state of domicile]
- **Current yield curve and market data** — for mark-to-market analysis of unrealized gains/losses

## Workflow

1. **Map the portfolio** — Categorize holdings by NAIC asset class designation (1–6 for bonds, common/preferred stock, mortgage loans, real estate, alternatives). Calculate percentage allocation to each class.
2. **Assess credit quality distribution** — Tabulate bond holdings by NAIC designation and equivalent rating (NAIC 1 = A or better, NAIC 2 = BBB, etc.). Flag any NAIC 3–6 concentrations exceeding IPS limits.
3. **Perform duration/cash-flow analysis** — Compare effective duration of invested assets against estimated duration of liabilities. Identify duration gap and convexity mismatch. For life insurers, check key-rate duration buckets. [VERIFY: for P&C, loss reserve payout patterns may substitute for traditional duration analysis]
4. **Test statutory concentration limits** — Check single-issuer exposure, sector concentration, and asset-class caps against domiciliary state statute and NAIC model law benchmarks (e.g., typically 3–5% of admitted assets per issuer for bonds). [VERIFY: state-specific limits]
5. **Calculate RBC impact** — Apply C-1 risk factors to each asset holding. Identify the largest capital charges and assess whether portfolio reallocation could improve the RBC ratio. For life companies, run C-3 Phase I/II interest rate scenarios if applicable.
6. **Evaluate ALM alignment** — Overlay liability cash flows against asset cash flows under base and stress scenarios (e.g., +/- 100–300 bps parallel shift, steepener/flattener). Quantify surplus volatility.
7. **Benchmark against peers** — Compare allocation percentages, credit quality mix, and yield to similar-sized carriers in the same line of business using NAIC aggregate data or SNL/S&P Capital IQ.
8. **Identify findings and recommendations** — Summarize concentration risks, ALM mismatches, statutory compliance gaps, and capital efficiency opportunities.

## Output

Structure the analysis report with these sections:

- **Executive Summary** — Key findings, portfolio size, overall credit quality, and ALM posture in 3–5 bullet points
- **Portfolio Composition** — Table showing asset class breakdown (bonds, equities, mortgage loans, real estate, alternatives, cash) with dollar amounts and percentages
- **Credit Quality Profile** — Distribution by NAIC designation with comparison to IPS minimums and peer averages
- **Duration & ALM Analysis** — Asset vs. liability duration, gap analysis, and surplus sensitivity to rate scenarios
- **Statutory Compliance Review** — Pass/fail table for each applicable investment statute limit (single issuer, asset class caps, foreign investment, below-investment-grade aggregate)
- **RBC / Capital Impact** — C-1 charges by asset bucket, total asset risk charge, and modeled impact of proposed reallocations
- **Recommendations** — Prioritized list of portfolio actions (e.g., reduce NAIC 3+ exposure, extend/shorten duration, diversify sector concentration)

## Quality Checks

- Confirm all holdings sum to the total invested assets figure on the balance sheet — reconcile any discrepancies before proceeding
- Verify NAIC designations match SVO-assigned ratings (not issuer ratings) for privately placed bonds [VERIFY: check if any holdings received NAIC filing-exempt treatment]
- Ensure duration calculations use option-adjusted duration for callable bonds and mortgage-backed securities, not Macaulay duration
- Cross-check statutory limits against the correct state code — do not assume NAIC model law applies without confirming adoption [VERIFY: domiciliary state statute version]
- Flag any affiliated-party investments and confirm they comply with holding company act restrictions
- Mark all jurisdiction-dependent thresholds and regulatory references with [VERIFY] for manual confirmation
- Confirm that any reinsurer trust assets analyzed are valued on a statutory (not GAAP) basis unless otherwise specified

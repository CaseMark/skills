---
name: analyzing-loss-reserves
language: en
description: Evaluates loss reserve adequacy with development triangle analysis and actuarial methods. Use when analyzing reserves, interpreting loss triangles, or assessing reserve adequacy.
tags:
  - analysis
  - insurance
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
# Analyzing Loss Reserves

Evaluates loss reserve adequacy using development triangle analysis, actuarial projection methods, and benchmark comparisons to determine whether carried reserves are reasonable, deficient, or redundant.

## When To Use

- Reviewing an insurer's or reinsurer's Statement of Actuarial Opinion and supporting exhibits
- Assessing reserve adequacy during due diligence for M&A, commutation, or loss portfolio transfer
- Interpreting loss development triangles provided in Schedule P, statutory filings, or internal actuarial reports
- Comparing carried reserves against independent point estimates or range estimates
- Evaluating reserve changes period-over-period (favorable/adverse development) and their drivers
- Supporting reinsurance treaty pricing or reserve credit analysis

## Inputs To Gather

- **Loss development triangles**: Paid and incurred triangles by accident year (or underwriting year/report year), ideally at 12-month intervals; note whether triangles are cumulative or incremental
- **Earned premium and exposure data**: By corresponding year and line of business
- **Carried reserve balances**: Case reserves, IBNR, and total by accident year and LOB
- **Actuarial report or opinion**: Including selected methods, assumptions, selected loss development factors (LDFs), and tail factors
- **Line of business and claim type**: Workers' comp, general liability, professional liability, auto, property, etc. — development patterns vary dramatically
- **Benchmark data**: Industry LDFs from sources such as AM Best, ISO/Verisk, or NAIC Schedule P industry aggregates [VERIFY: confirm which benchmark source is available and appropriate for the line]
- **Prior analyses**: Previous reserve studies or external auditor findings for trend comparison

## Workflow

1. **Validate triangle integrity**
   - Confirm triangles are on a consistent basis (paid vs. incurred, cumulative vs. incremental)
   - Check that the latest diagonal ties to the balance sheet carried amounts
   - Identify any triangle adjustments (large-loss caps, commutation removals, currency conversions) and note their impact

2. **Calculate age-to-age development factors**
   - Compute link ratios for each development period across all accident years
   - Examine simple average, volume-weighted average, and medial (excluding high/low) selections
   - Identify accident years with unusually high or low factors — flag potential large-loss distortion, reserve strengthening, or claim settlement pattern changes

3. **Apply standard actuarial projection methods**
   - **Chain Ladder (Development)**: Apply selected LDFs to the latest cumulative values; most reliable for mature, stable lines
   - **Bornhuetter-Ferguson (BF)**: Blend development projection with an a priori expected loss ratio; preferred for immature accident years or volatile lines
   - **Cape Cod (Stanard-Buhlmann)**: Use exposure-weighted expected losses; useful when loss ratios are expected to be stable across years
   - **Frequency-Severity**: Where claim count and average severity data are available, project separately; valuable for lines with known count trends
   - Select tail factors for development beyond the triangle's observed maturity [VERIFY: tail factor assumptions are highly judgment-dependent — confirm basis and reasonableness]

4. **Develop ultimate loss estimates and ranges**
   - Produce point estimates from each method by accident year
   - Weight or select among methods based on data credibility, line characteristics, and maturity
   - Construct a reasonable range (e.g., low/central/high) reflecting parameter uncertainty
   - Compare to the company's carried reserves — quantify redundancy or deficiency by accident year and in total

5. **Analyze reserve development trends**
   - Track prior-year development (favorable or adverse) over multiple calendar periods
   - Identify whether development is concentrated in specific accident years or lines
   - Assess whether development patterns indicate systematic under- or over-reserving
   - Consider external drivers: legal environment changes, inflation, claim handling practice shifts

6. **Benchmark and stress test**
   - Compare company LDFs and ultimate loss ratios to industry benchmarks for the same line and maturity
   - Test sensitivity to alternative tail factors, LDF selections, and expected loss ratio assumptions
   - Quantify the reserve impact of plausible adverse scenarios (e.g., social inflation, latent exposure emergence)

## Output

Structure the analysis report as follows:

- **Executive Summary**: Overall reserve adequacy conclusion (adequate / likely deficient / likely redundant), magnitude of estimated surplus or shortfall, key risk factors
- **Data and Scope**: Lines of business, accident years, triangle basis, and any data limitations
- **Development Factor Analysis**: Table of age-to-age factors with selected factors and basis for selection; highlight anomalies
- **Ultimate Loss Projections**: Table by accident year showing results from each method, selected ultimates, and comparison to carried reserves
- **Reserve Adequacy Assessment**: Quantified redundancy/deficiency by year and total; confidence range; discussion of key judgment areas
- **Development History**: Summary of favorable/adverse development trends and their implications
- **Sensitivity Analysis**: Impact of alternative assumptions on the adequacy conclusion
- **Limitations and Caveats**: Data gaps, areas of high uncertainty, reliance on third-party information

## Quality Checks

- Confirm all triangle arithmetic is internally consistent (incremental values sum to cumulative; latest diagonal matches reported data)
- Verify that selected LDFs fall within a reasonable range relative to historical averages and industry benchmarks — outlier selections require explicit justification
- Ensure BF and Cape Cod a priori loss ratios are sourced and documented, not assumed without basis
- Check that tail factors are reasonable for the line's claim closure characteristics [VERIFY: long-tail lines like workers' comp or environmental liability may need tails extending 20+ years]
- Confirm the analysis addresses both paid and incurred bases — significant divergence between paid and incurred projections should be explained
- Validate that large losses or one-time events are identified and their treatment (capped, excluded, separately developed) is clearly stated
- Ensure the adequacy conclusion accounts for discount effects if reserves are on a present-value basis [VERIFY: confirm whether reserves are discounted and the applicable discount rate/standard]
- Flag any areas where actuarial judgment materially drives the result and a qualified actuary should review

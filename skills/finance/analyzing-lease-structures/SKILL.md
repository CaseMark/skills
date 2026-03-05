---
name: analyzing-lease-structures
description: Evaluates commercial lease terms with net effective rent, concession analysis, and tenant credit assessment. Use when analyzing leases, calculating effective rents, or comparing lease structures.
tags:
  - analysis
  - real-estate-finance
  - credit
metadata:
  author: casemark
  practice_areas:
    - Real Estate Finance
    - REIT Analysis
    - Property Investment
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Lease Structures

Evaluates commercial lease terms by computing net effective rent, quantifying concession packages, and assessing tenant credit quality to support underwriting, acquisition, and portfolio management decisions.

## When To Use

- Underwriting a property acquisition and need to stress-test in-place lease economics
- Comparing competing tenant proposals on an apples-to-apples net effective rent basis
- Evaluating a REIT portfolio's weighted-average lease profile and rollover risk
- Assessing whether landlord concessions (TI, free rent, moving allowances) are market-appropriate
- Reviewing tenant creditworthiness before committing to long-term lease exposure

## Inputs To Gather

- **Lease abstracts or full lease documents** — base rent schedule, escalation clauses, expense structure (NNN, modified gross, full-service gross)
- **Concession details** — tenant improvement (TI) allowance, free rent periods, moving allowances, lease buyout payments
- **Tenant financials** — credit rating (Moody's/S&P if investment-grade), most recent annual revenue, net income, and balance sheet highlights; for private tenants, request financial statements or guarantor information
- **Market comps** — comparable lease transactions in the submarket (asking rent, achieved rent, concession packages, lease term)
- **Property-level data** — operating expenses per SF, cap rate assumptions, discount rate for NPV calculations
- **Lease term parameters** — commencement date, expiration, renewal options (fixed-rate vs. fair-market-value), termination rights, co-tenancy clauses

## Workflow

1. **Classify the lease structure**
   - Identify expense type: NNN, modified gross, or full-service gross
   - Map escalation mechanism: fixed annual bumps, CPI-linked, percentage rent, or fair-market resets
   - Note any unusual provisions: co-tenancy kick-outs, go-dark clauses, exclusive-use restrictions, ROFO/ROFR on adjacent space

2. **Calculate net effective rent (NER)**
   - Compute total undiscounted rent over the lease term including all escalations
   - Subtract landlord concessions: TI allowance, free rent (valued at face rent for those months), moving allowances
   - Divide by total lease months for a per-month NER, then annualize per SF
   - For a present-value approach, discount cash flows at the landlord's cost of capital or market discount rate [VERIFY discount rate assumption with client/underwriting team]

3. **Analyze the concession package**
   - Express TI as $/SF and compare to submarket averages
   - Convert free rent to an equivalent rent reduction per SF per year over the term
   - Calculate the landlord's total concession cost as a percentage of gross lease value
   - Flag concessions that exceed market norms by more than 15–20% for further diligence

4. **Assess tenant credit quality**
   - Investment-grade tenants (BBB-/Baa3 or above): note rating, outlook, and sector
   - Sub-investment-grade or unrated tenants: review guarantor strength, security deposit or letter of credit terms, and lease guaranty structure
   - Assign an internal credit tier (strong / acceptable / watch / substandard) based on financial metrics: debt-to-EBITDA, interest coverage ratio, and liquidity position [VERIFY internal credit-tier definitions per firm policy]
   - For percentage-rent leases, evaluate tenant sales performance and trend trajectory

5. **Benchmark against market**
   - Compare NER to submarket comps on a per-SF basis, adjusting for floor level, vintage, and amenity package
   - Assess whether escalation structure keeps pace with projected market rent growth
   - Identify mark-to-market exposure: leases significantly above or below market at expiration

6. **Compile risk factors**
   - Rollover concentration: flag years where >15% of portfolio NRA or revenue rolls
   - Tenant concentration: single-tenant exposure exceeding 10% of portfolio revenue
   - Lease duration: weighted-average lease term (WALT) relative to debt maturity
   - Early termination or contraction option exposure

## Output

Produce a structured analysis report containing:

- **Lease summary table** — tenant name, suite, SF, lease type, term, base rent/SF, escalation structure, NER/SF
- **Net effective rent calculation** — step-by-step buildup showing gross rent, concession deductions, and resulting NER (both undiscounted and PV-adjusted)
- **Concession benchmarking** — TI $/SF, free rent months, and total concession cost vs. market comps
- **Tenant credit snapshot** — rating/tier, key financial ratios, guaranty structure, and any watch-list flags
- **Risk summary** — rollover schedule, mark-to-market exposure, tenant concentration, and any non-standard lease provisions requiring attention
- **Recommendation** — clear statement on whether lease terms are at-market, above-market, or below-market, with suggested negotiation points or underwriting adjustments

## Quality Checks

- Verify that NER calculation accounts for all concession types, not just free rent
- Confirm escalation math ties to lease language (compounding vs. simple annual increases)
- Ensure expense stop or base-year assumptions are correctly reflected in NNN-equivalent comparisons
- Cross-check tenant credit data against the most recent available filings [VERIFY filing date]
- Validate that market comps are from the same submarket and asset class (office vs. industrial vs. retail)
- Confirm discount rate used for PV calculations aligns with property type and risk profile
- Flag any lease provisions that could affect NOI stability (kick-out clauses, co-tenancy triggers) even if not yet exercisable

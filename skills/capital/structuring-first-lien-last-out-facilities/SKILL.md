---
name: structuring-first-lien-last-out-facilities
language: en
description: Designs FILO structures with tranche-level pricing, distribution waterfalls, and intercreditor provisions within unitranche financing. Use when structuring FILO tranches, analyzing split economics, or designing blended pricing.
tags:
  - credit-and-institutional-lending
  - credit
metadata:
  author: casemark
  practice_areas:
    - Credit Markets
    - Leveraged Lending
    - Direct Lending
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring First Lien Last Out Facilities

Designs FILO structures with tranche-level pricing, distribution waterfalls, and intercreditor provisions within unitranche financing.

## When To Use

- Structuring a unitranche facility that splits into first-out (FO) and last-out (LO) tranches with differentiated economics
- Analyzing blended yield versus tranche-level pricing to determine FILO feasibility against a traditional first lien / second lien stack
- Designing or reviewing the Agreement Among Lenders (AAL) governing FO/LO intercreditor rights
- Evaluating FILO economics for a direct lender syndicating the FO piece to a bank or other lower-cost capital provider
- Modeling distribution waterfalls, default interest allocation, and recovery scenarios across tranches

## Inputs To Gather

- **Deal parameters**: Total facility size, FO/LO split (dollar amounts and percentages), maturity, amortization schedule
- **Pricing terms**: FO coupon (spread + floor), LO coupon (spread + floor), OID on each tranche, any PIK toggle or PIK component on the LO
- **Blended yield target**: Weighted-average cost the borrower sees as a single unitranche rate
- **Credit metrics**: Borrower EBITDA, total leverage, FO leverage, LO leverage, fixed charge coverage ratio
- **Intercreditor provisions**: Voting thresholds for amendments/waivers, standstill periods, purchase option triggers, buyout pricing mechanics
- **Waterfall mechanics**: Order of payments (interest, principal, fees), default interest allocation, excess cash flow sweep split
- **Recovery assumptions**: Collateral value estimates, expected recovery rates by tranche under stress scenarios
- **Market context**: Comparable FILO transactions, current spread benchmarks for FO (bank market) and LO (direct lending market)

## Workflow

1. **Define the tranche architecture**
   - Set FO and LO commitment amounts as a percentage of total facility size
   - Determine whether the LO tranche carries a PIK component, cash-pay coupon, or blended structure
   - Confirm maturity alignment — typically co-terminus, but flag any maturity mismatch risk

2. **Build blended pricing analysis**
   - Calculate the blended all-in yield the borrower pays across FO and LO tranches
   - Compare blended cost against alternatives: traditional first lien/second lien, standalone unitranche, or syndicated TLB
   - Model OID amortization and upfront fee impact on effective yield for each tranche holder

3. **Structure the distribution waterfall**
   - Define payment priority: FO interest → LO interest → FO scheduled amortization → LO scheduled amortization → excess cash flow sweep allocation
   - Specify default interest treatment — whether it flows pro rata or is allocated entirely to FO
   - Address make-whole and prepayment premium allocation between tranches
   - Model the waterfall under base case, downside, and default scenarios

4. **Draft intercreditor provisions (AAL terms)**
   - **Voting rights**: Identify which amendments require unanimous consent versus FO-only or LO-only consent [VERIFY — AAL terms are deal-specific and heavily negotiated]
   - **Standstill period**: Specify duration during which LO lenders cannot exercise remedies after an event of default (typically 90–180 days)
   - **Purchase option**: Define the LO lender's right to purchase FO claims at par (or par plus accrued) upon a default trigger
   - **Buyout mechanics**: Set pricing for the buyout option — par, par plus accrued, or a premium
   - **Release and DIP provisions**: Address how FO and LO rights interact in a bankruptcy filing, including DIP financing consent and collateral release

5. **Run recovery and stress analysis**
   - Model collateral recovery at multiple enterprise value haircuts (e.g., 20%, 40%, 60% decline)
   - Calculate recovery rates for FO and LO tranches separately under each scenario
   - Determine the enterprise value breakpoint at which LO recovery drops below a target threshold
   - Assess whether FO sizing provides adequate cushion under stress

6. **Benchmark against market**
   - Compare FO spread to bank-market first lien spreads for similar credit profiles
   - Compare LO spread to direct lending second lien or stretched senior pricing
   - Validate that the blended yield falls within market norms for the borrower's leverage and sector

## Output

- **FILO Structure Summary**: Tranche sizes, pricing (coupon, OID, PIK if applicable), blended all-in yield, and key dates
- **Waterfall Exhibit**: Step-by-step payment cascade under performing, stressed, and default scenarios with dollar allocations to each tranche
- **Intercreditor Term Sheet**: AAL provisions covering voting, standstill, purchase option, buyout pricing, and bankruptcy-related rights
- **Recovery Analysis Table**: FO and LO recovery percentages at multiple enterprise value haircut levels
- **Blended Pricing Comparison**: Side-by-side analysis of FILO blended cost versus alternative capital structures
- **Key Risk Flags**: Identified issues such as thin LO cushion, aggressive standstill periods, or blended yield above market

## Quality Checks

- Blended yield calculation reconciles exactly to the weighted average of FO and LO all-in costs
- Waterfall allocations sum to total available cash in each scenario — no leakage or rounding gaps
- Intercreditor provisions are internally consistent (e.g., standstill period length aligns with purchase option trigger timeline)
- Recovery analysis uses collateral values consistent with the deal's appraisal or enterprise valuation basis
- FO leverage and LO leverage correctly map to the borrower's capital structure and priority of claims
- All jurisdiction-dependent provisions (UCC perfection, intercreditor enforceability) are marked [VERIFY]
- PIK accrual mechanics, if applicable, are modeled through maturity with compounding correctly applied

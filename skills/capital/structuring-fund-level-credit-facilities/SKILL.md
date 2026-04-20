---
name: structuring-fund-level-credit-facilities
language: en
description: Designs subscription credit facilities with LP commitment-based lending, borrowing base mechanics, and advance rate analysis. Use when structuring fund lines, analyzing subscription facilities, or evaluating fund-level leverage.
tags:
  - fund-formation-and-structuring
  - credit
metadata:
  author: casemark
  practice_areas:
    - Fund Formation
    - Fund Structuring
    - Partnership Law
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Fund Level Credit Facilities

## When To Use

- Structuring a new subscription credit facility (capital call line) for a PE, VC, real estate, or infrastructure fund
- Analyzing an existing facility's borrowing base composition and advance rate adequacy
- Evaluating LP commitment quality and concentration risk for lending purposes
- Comparing term sheet proposals from prospective lenders
- Assessing fund-level leverage limits against LPA covenants and side letter restrictions
- Reviewing facility compliance during the investment or harvest period

## Inputs To Gather

- **LPA and side letters**: Capital commitment amounts, excuse/exclusion rights, default remedies, leverage limitations, borrowing restrictions [VERIFY specific side letter carve-outs for each LP]
- **LP roster with commitment details**: Legal name, commitment amount, funded/unfunded split, investor type (pension, sovereign wealth, HNWI, fund-of-funds, endowment), domicile, credit rating or financial profile
- **Proposed or existing facility terms**: Commitment amount, tenor, interest rate (spread + benchmark), advance rates by LP tier, borrowing base formula, conditions precedent, financial covenants
- **Fund economics**: Target fund size, investment period length, expected capital call cadence, distribution waterfall provisions affecting repayment
- **Lender requirements**: Eligible LP criteria, concentration limits, minimum commitment thresholds, exclusion triggers (e.g., LP default, excuse rights exercised, ERISA thresholds)

## Workflow

1. **Map the LP base into borrowing base tiers**
   - Classify each LP by credit quality tier (e.g., Tier 1: rated investment-grade institutions; Tier 2: unrated institutional; Tier 3: HNWI/family office; Tier 4: fund-of-funds or feeder vehicles)
   - Apply advance rates per tier (typical ranges: Tier 1 at 90-95%, Tier 2 at 75-85%, Tier 3 at 50-65%, Tier 4 at 0-50%) [VERIFY lender-specific advance rate schedules]
   - Exclude LPs with excuse/exclusion rights that could reduce callable capital, defaulted LPs, and any LP below minimum commitment thresholds

2. **Calculate the borrowing base**
   - For each eligible LP: uncalled commitment x advance rate = included amount
   - Sum included amounts across all eligible LPs
   - Apply concentration limits (single LP cap typically 15-25% of borrowing base; single investor-type cap varies) [VERIFY concentration thresholds per term sheet]
   - Apply aggregate facility cap (borrowing base vs. facility commitment, whichever is lower)

3. **Analyze facility sizing and leverage**
   - Compare facility size to total unfunded commitments (typical subscription lines: 15-30% of total commitments)
   - Confirm compliance with LPA leverage restrictions (percentage-of-commitments cap, duration limits on outstanding borrowings, purpose restrictions)
   - Check side letter restrictions that may impose tighter leverage covenants on specific LPs [VERIFY each side letter's borrowing limitation language]

4. **Evaluate key structural terms**
   - **Tenor and extension options**: Match facility tenor to remaining investment period; flag mismatch risk if facility extends into harvest period
   - **Interest rate and fees**: Benchmark rate (SOFR + spread), unused commitment fee, upfront/arrangement fees; compare to market benchmarks
   - **Clean-down provisions**: Frequency and duration of mandatory repayment periods (common: 1-2 annual clean-downs of 3-10 days)
   - **Collateral package**: Assignment of right to make capital calls, pledge of capital commitment receivables, control account agreements
   - **Events of default**: LP-related triggers (key-person departure, no-fault termination, GP removal), fund-level triggers (NAV decline, investment period expiration)

5. **Assess LP-related risks**
   - Concentration risk: Over-reliance on a small number of large LPs
   - Sovereign/regulatory risk: Foreign LPs subject to capital controls or sanctions [VERIFY OFAC/sanctions screening for each LP jurisdiction]
   - Excuse/exclusion exposure: Aggregate callable capital at risk if excuse rights are broadly exercised
   - Default cascade risk: Impact on borrowing base if one or more large LPs default on capital calls

6. **Document facility structure and recommendations**
   - Produce borrowing base certificate with LP-by-LP detail
   - Summarize advance rate analysis with sensitivity scenarios (e.g., loss of top 3 LPs, downgrade of Tier 1 LP)
   - Flag any LPA or side letter provisions that create structural risk for the facility
   - Recommend facility sizing, lender selection criteria, and negotiation points

## Output

Deliver a structured report containing:

- **Borrowing base schedule**: LP-by-LP breakdown showing commitment, tier classification, advance rate, included amount, and any exclusion reasons
- **Facility sizing summary**: Recommended facility amount, leverage ratio to total commitments, headroom analysis
- **Term comparison matrix** (if multiple lender proposals): Side-by-side comparison of pricing, advance rates, covenants, and structural features
- **Risk assessment**: Concentration analysis, LP credit quality distribution, sensitivity to LP attrition or default
- **LPA/side letter compliance checklist**: Confirmation that proposed facility terms satisfy all partnership agreement restrictions
- **Negotiation recommendations**: Key points to push on with lenders (advance rate improvements, concentration limit flexibility, clean-down waivers, covenant thresholds)

## Quality Checks

- Verify that every LP in the roster is accounted for — either included in the borrowing base or explicitly excluded with a stated reason
- Confirm advance rates applied match the lender's term sheet or credit policy (not assumed market averages)
- Cross-check LPA leverage limits against the proposed facility size and confirm compliance
- Validate that concentration limits are correctly applied (both single-LP and investor-type caps)
- Ensure side letter borrowing restrictions are individually reviewed, not treated as uniform [VERIFY]
- Flag any LP whose commitment is subject to regulatory approval, capital controls, or pending legal dispute
- Confirm the collateral package includes assignment of capital call rights and account control agreements as required by the lender

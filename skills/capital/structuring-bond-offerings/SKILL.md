---
name: structuring-bond-offerings
language: en
description: Designs bond offering structures with tenor, coupon, call provisions, covenant packages, and pricing methodology. Use when structuring bond deals, selecting debt parameters, or comparing issuance alternatives.
tags:
  - debt-capital-markets
metadata:
  author: casemark
  practice_areas:
    - DCM
    - Leveraged Finance
    - Debt Origination
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Bond Offerings

Designs bond offering structures covering tenor selection, coupon type, call/put provisions, covenant packages, and pricing methodology for investment-grade and high-yield issuances.

## When To Use

- Structuring a new bond issuance and selecting debt parameters (tenor, coupon, redemption features)
- Comparing alternative offering structures (e.g., fixed vs. floating, secured vs. unsecured, senior vs. subordinated)
- Evaluating covenant packages for high-yield or leveraged finance transactions
- Advising on call protection schedules, make-whole premiums, or equity clawback provisions
- Preparing pricing methodology recommendations ahead of bookbuilding or private placement

## Inputs To Gather

- **Issuer profile**: credit rating (Moody's/S&P/Fitch), sector, public vs. private, existing capital structure and leverage ratios
- **Transaction objectives**: refinancing, acquisition financing, general corporate purposes, dividend recap
- **Target size and currency**: principal amount, single vs. multi-tranche, USD/EUR/other
- **Market context**: current benchmark yields (UST/Bund), recent comparable issuances (comps), credit spread environment
- **Investor base considerations**: 144A/Reg S, institutional vs. retail, geographic distribution
- **Issuer constraints**: maximum coupon tolerance, total leverage caps, restricted payments basket needs, required call flexibility
- **Rating agency feedback**: any preliminary guidance on notching, recovery ratings, or structure-specific conditions

## Workflow

1. **Profile the credit and capital structure**
   - Summarize current debt stack (revolver, term loans, existing bonds), maturity profile, and coverage ratios (interest coverage, fixed charge)
   - Identify the tranche's position in the capital structure (senior secured, senior unsecured, subordinated, holdco vs. opco)
   - Note rating (actual or expected) and any rating triggers in existing docs [VERIFY against current rating agency reports]

2. **Select tenor and coupon structure**
   - Recommend maturity based on issuer's refinancing profile, asset life, and investor demand curves (e.g., 5NC2, 7-year bullet, 10NC5)
   - Choose fixed vs. floating rate (or fixed-to-floating toggle) based on issuer preference and hedging strategy
   - For floating-rate notes: specify reference rate (SOFR, EURIBOR) plus spread, floor provisions, and reset frequency [VERIFY applicable benchmark conventions by currency]

3. **Design call provisions and redemption features**
   - **Make-whole call**: set make-whole premium (typically T+ spread, e.g., T+50 bps) for investment-grade or par-plus-premium for high-yield
   - **Fixed-price call schedule**: define non-call period (NC2, NC3, NC4) and step-down schedule (e.g., 104.25 → 102.125 → 100)
   - **Equity clawback**: specify percentage callable (typically 35-40% of original principal) at par plus coupon within first 3 years from equity proceeds
   - **Change-of-control put**: 101% put right upon change of control plus ratings downgrade (double trigger) [VERIFY market standard for sector]
   - **Special mandatory redemption**: if proceeds are for an acquisition that may not close

4. **Draft covenant package**
   - For **investment-grade**: typically covenant-lite — negative pledge, limitation on sale-leasebacks, merger restriction, with broad carve-outs
   - For **high-yield**: full incurrence-based covenant package:
     - Limitation on indebtedness (with permitted debt baskets and ratio test, e.g., 2.0x fixed charge coverage)
     - Restricted payments (with builder basket, general basket amounts, and specific carve-outs)
     - Limitation on asset sales (with reinvestment rights period, typically 365-450 days)
     - Limitation on affiliate transactions (with board approval thresholds and fairness opinion requirements)
     - Reporting requirements and SEC compliance covenants
   - Define "Permitted Liens," "Permitted Investments," and "Restricted Subsidiary" definitions based on issuer operations [VERIFY consistency with existing credit agreement definitions]

5. **Develop pricing methodology**
   - Pull comparable recent issuances (same rating tier, sector, tenor) and spread benchmarks
   - Recommend initial price talk range (e.g., T+175-200 bps or 6.25-6.50% coupon)
   - Outline bookbuilding strategy: price talk → order book accumulation → pricing tightening → final allocation
   - Assess OID (original issue discount) if applicable; flag tax implications of OID exceeding de minimis threshold [VERIFY IRS de minimis OID rules]
   - Consider new issue concession (typically 10-25 bps over secondary trading levels for comparable credits)

6. **Compare structural alternatives**
   - Present side-by-side comparison of 2-3 structural options (e.g., single tranche senior unsecured vs. secured/unsecured split vs. term loan B + bond combination)
   - Evaluate each on: all-in cost, covenant flexibility, call optionality, execution certainty, and rating impact
   - Recommend preferred structure with rationale tied to issuer objectives

## Output

Deliver a **Bond Structuring Memorandum** containing:

- **Executive summary**: recommended structure with key terms (size, tenor, coupon guidance, call schedule)
- **Capital structure pro forma**: pre- and post-issuance debt stack with leverage and coverage metrics
- **Term sheet**: principal amount, maturity, coupon, call provisions, change-of-control, covenants summary, security/guarantees, use of proceeds
- **Comparable issuance table**: 5-10 recent comps with issuer, rating, tenor, coupon, spread at issue, and current trading levels
- **Pricing analysis**: recommended price talk, new issue concession analysis, sensitivity to spread movement (±25 bps on coupon cost)
- **Alternative structures comparison**: tabular side-by-side with cost, flexibility, and execution dimensions
- **Risk factors and open items**: items requiring issuer decision, rating agency confirmation, or legal review

## Quality Checks

- Confirm all spread and yield references cite a specific date and source (Bloomberg, market color, syndicate desk)
- Verify call schedule math: non-call period, step-down amounts, and equity clawback percentages are internally consistent
- Ensure covenant baskets are cross-referenced to existing credit facility definitions to avoid conflicts or unintended tightening
- Check that pro forma leverage and coverage ratios reflect the new issuance proceeds and use of funds
- Validate that 144A/Reg S, transfer restrictions, and minimum denomination are appropriate for the target investor base [VERIFY SEC registration requirements]
- Flag any assumptions about benchmark rates, credit spreads, or market conditions with dates and sources

---
name: structuring-employee-stock-offerings
description: Designs ESPP and directed share programs with eligibility, pricing mechanics, and regulatory compliance requirements. Use when structuring employee offerings, designing share purchase plans, or managing directed share allocations.
tags:
  - equity-capital-markets
  - compliance
  - regulatory
metadata:
  author: casemark
  practice_areas:
    - ECM
    - IPO Advisory
    - Equity Origination
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Employee Stock Offerings

Designs ESPP and directed share programs with eligibility, pricing mechanics, and regulatory compliance requirements.

## When To Use

- Structuring a Section 423 or non-423 Employee Stock Purchase Plan (ESPP) for a pre-IPO or public company
- Designing a directed share program (DSP/friends-and-family allocation) in connection with an IPO
- Evaluating eligibility criteria, contribution limits, and offering-period mechanics for employee share plans
- Assessing discount pricing, lookback provisions, and reset features against tax and securities rules
- Reviewing regulatory compliance for employee offerings across multiple jurisdictions

## Inputs To Gather

- **Company profile**: Public vs. pre-IPO status, exchange listing, employee headcount, and jurisdictions of employment
- **Plan type**: Section 423 qualified ESPP, non-423 ESPP, DSP, or hybrid structure
- **Offering parameters**: Proposed discount rate, lookback period length, offering period duration, purchase intervals, contribution caps
- **Eligible participant pool**: Full-time vs. part-time thresholds, service-length requirements, excluded employee categories (e.g., 5% owners), international employees
- **Share reserve**: Number of shares authorized, percentage of outstanding, evergreen replenishment provisions
- **Tax and accounting guidance**: Target treatment under IRC Section 423, ASC 718 compensation expense estimates, payroll tax implications
- **Underwriter requirements** (for DSPs): Allocation size, lockup terms, FINRA Rule 5130/5131 restricted-person screens

## Workflow

1. **Determine plan type and objectives**
   - Identify whether the goal is broad-based employee retention (ESPP) or targeted IPO participation (DSP)
   - For ESPPs, decide between Section 423 qualified (favorable tax treatment, stricter rules) and non-423 (flexibility for international employees) [VERIFY: Section 423 eligibility requirements per current IRC provisions]
   - For DSPs, confirm underwriter willingness and typical allocation as a percentage of offering size (commonly 2-5%)

2. **Design eligibility and enrollment mechanics**
   - Set minimum service requirement (Section 423 plans cannot exclude employees with <2 years of service but can exclude those with <2 years) [VERIFY: current IRS guidance on permissible exclusions]
   - Define enrollment windows, payroll deduction authorization process, and withdrawal rights
   - For international sub-plans, map local labor, tax, and securities filing requirements per jurisdiction
   - Screen DSP participants against FINRA Rule 5130 (restricted persons) and Rule 5131 (spinning) [VERIFY: current FINRA rule text and no-action letters]

3. **Structure pricing and purchase mechanics**
   - Set discount rate (up to 15% for Section 423 plans; non-423 plans may vary)
   - Determine lookback feature: purchase price = discount applied to lower of FMV at offering-period start or purchase date
   - Evaluate reset/rollover provisions — automatic re-enrollment into a new offering period if stock price declines
   - Calculate $25,000 annual purchase limit under Section 423 (based on FMV at grant date) [VERIFY: IRS annual limit and FMV calculation methodology]
   - For DSPs, confirm IPO price allocation, confirm no discount below public offering price, and establish lockup period (typically 25-180 days)

4. **Assess share reserve and dilution**
   - Model share usage under various participation-rate assumptions (typical ESPP participation: 20-40% of eligible employees)
   - Calculate dilutive impact and confirm alignment with ISS/Glass Lewis burn-rate guidelines
   - Draft evergreen replenishment terms if applicable (e.g., annual increase of 1% of outstanding shares, subject to board cap)

5. **Map regulatory and compliance requirements**
   - Securities Act: Confirm Registration Statement on Form S-8 (ESPP) or inclusion in IPO prospectus (DSP) [VERIFY: current SEC form requirements]
   - Exchange rules: Confirm shareholder approval requirements for new plans or share reserve increases
   - Tax withholding: Identify qualifying vs. disqualifying dispositions and employer reporting obligations (Forms W-2, 3922)
   - International: Flag countries requiring local prospectus filings, data privacy consents, or exchange-control approvals (common issues: France, India, China, Germany)

6. **Compile accounting and disclosure analysis**
   - Estimate ASC 718 fair-value expense using Black-Scholes or Monte Carlo for plans with reset features
   - Draft proxy statement disclosure language for shareholder approval
   - Outline board resolution and plan document terms

## Output

- **Plan structure summary**: One-page overview of plan type, eligibility, pricing mechanics, offering periods, and contribution limits
- **Regulatory compliance matrix**: Jurisdiction-by-jurisdiction table of securities filings, tax treatment, and labor-law requirements
- **Dilution and share-reserve analysis**: Projected share usage, burn rate, and dilutive impact under base/upside/downside participation scenarios
- **DSP allocation memo** (if applicable): Participant eligibility screens, allocation methodology, lockup terms, and FINRA compliance confirmation
- **Risk and open-items register**: Items requiring legal counsel confirmation, board approval, or further tax analysis marked with [VERIFY]

## Quality Checks

- Section 423 plans: Confirm the $25,000 annual limit is correctly applied using grant-date FMV, not purchase-date FMV
- Discount and lookback combination does not inadvertently exceed the 15% statutory discount for qualified plans
- DSP participants have been screened against FINRA restricted-person definitions — no portfolio managers, broker-dealer employees, or their immediate family members unless an exception applies
- International sub-plans are not assumed to mirror U.S. tax treatment — each jurisdiction's qualifying conditions are independently verified
- Evergreen provisions include a hard share cap and sunset date to avoid ISS governance policy flags
- ASC 718 expense estimates reflect actual plan features (lookback, reset) rather than a simplified Black-Scholes on the discount alone
- All jurisdiction-specific statutes, regulations, and exchange rules are tagged [VERIFY] where the analysis depends on current law

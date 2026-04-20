---
name: analyzing-compensation-tax
language: en
description: Evaluates executive compensation tax with Section 409A, 280G golden parachute, and equity comp treatment. Use when analyzing compensation tax, evaluating 409A compliance, or structuring equity compensation.
tags:
  - analysis
  - tax
  - compliance
  - treatment
metadata:
  author: casemark
  practice_areas:
    - Tax Planning
    - Tax Compliance
    - International Tax
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Compensation Tax

Evaluates executive compensation tax implications for executive and equity compensation arrangements, focusing on Section 409A deferred compensation rules, Section 280G golden parachute excise taxes, and tax treatment of equity-based awards.

## When To Use

- Reviewing or structuring deferred compensation plans for Section 409A compliance
- Analyzing change-in-control scenarios for Section 280G parachute payment exposure
- Evaluating tax treatment of stock options (ISOs vs. NQSOs), RSUs, restricted stock, SARs, or phantom equity
- Assessing compensation structures in M&A transactions, IPOs, or executive hiring/separation
- Reviewing employment agreements, severance plans, or equity award agreements for tax risk
- Advising on international compensation tax where cross-border equity grants or expatriate packages are involved

## Inputs To Gather

- **Compensation arrangement documents**: Employment agreements, equity plan documents, award agreements, severance plans, change-in-control agreements
- **Participant data**: Base compensation history (5-year lookback for 280G base amount), vesting schedules, exercise dates and prices, separation/termination dates
- **Transaction details** (if applicable): Deal structure, closing timeline, accelerated vesting provisions, single vs. double trigger mechanisms
- **Entity information**: Corporate structure (C-corp, S-corp, partnership, LLC), public vs. private status, tax year
- **Prior Section 409A valuations**: 409A valuation reports (for private company stock), exercise price documentation
- **International elements**: Jurisdictions involved, tax treaty applicability, local equity compensation rules [VERIFY local jurisdiction rules]

## Workflow

1. **Classify each compensation element**
   - Identify all deferred compensation arrangements subject to Section 409A (salary deferrals, SERPs, phantom equity, in-the-money options)
   - Distinguish exempt arrangements: short-term deferrals, separation pay exceptions, stock options granted at FMV with no additional deferral features
   - Categorize equity awards by type and applicable tax regime (IRC Section 83, 421/422 for ISOs, 409A if applicable)

2. **Analyze Section 409A compliance**
   - Verify that payment triggers qualify as permissible distribution events (separation from service, fixed date, change in control, disability, death, unforeseeable emergency)
   - Confirm six-month delay for specified employees of public companies upon separation from service
   - Check that plan terms prohibit acceleration of payments except for permitted exceptions [VERIFY against current Treasury Regulations Section 1.409A-3(j)(4)]
   - Review amendment and modification history for potential material modifications restarting the deferral analysis
   - Evaluate document correction opportunities under IRS Notice 2008-113 or subsequent correction programs [VERIFY current correction guidance]

3. **Model Section 280G exposure** (change-in-control scenarios)
   - Calculate each disqualified individual's base amount (average W-2/1099 compensation for five preceding tax years)
   - Identify all parachute payments: accelerated vesting, severance, non-compete payments, benefits continuation, and other contingent-on-change compensation
   - Apply the 3x base amount threshold — if aggregate parachute payments equal or exceed 3x the base amount, the excess over 1x is subject to 20% excise tax under Section 4999
   - Evaluate reasonable compensation exceptions for non-compete agreements and post-transaction services
   - For private companies, assess availability of shareholder approval safe harbor under Section 280G(b)(5) [VERIFY adequate disclosure requirements]
   - Model net-better-off vs. gross-up vs. hard-cap cutback approaches and quantify after-tax outcomes for each

4. **Evaluate equity compensation tax treatment**
   - **ISOs**: Confirm $100K annual vesting limit, holding period requirements (1 year from exercise, 2 years from grant), AMT preference item on exercise spread
   - **NQSOs**: Ordinary income at exercise on spread; confirm grant-date FMV to avoid 409A issues for private companies
   - **Restricted stock / Section 83(b) elections**: Evaluate timing benefits and risks of early election; note 30-day filing deadline
   - **RSUs**: Taxed as ordinary income at vesting/settlement; review settlement timing for 409A implications if settlement is deferred beyond vesting
   - **Profits interests / carried interest**: Confirm safe harbor under Rev. Proc. 93-27 (and Rev. Proc. 2001-43); assess Section 1061 three-year holding period for applicable partnership interests [VERIFY current legislative status]

5. **Address international considerations**
   - Identify taxable events in each jurisdiction for mobile employees or cross-border grants
   - Analyze treaty-based relief for double taxation on equity compensation income
   - Flag local filing and reporting obligations (e.g., UK share scheme reporting, Canadian stock option deduction changes) [VERIFY jurisdiction-specific rules]
   - Evaluate transfer pricing implications of intercompany cost-sharing for equity plans

## Output

The analysis report should include:

- **Executive summary**: Key findings, aggregate tax exposure, and recommended actions
- **Compensation element table**: Each arrangement classified by type, IRC section, and compliance status (compliant / at risk / non-compliant)
- **Section 409A compliance matrix**: Plan-by-plan assessment of document terms against 409A requirements, with specific deficiency citations
- **Section 280G exposure model**: Per-individual parachute payment calculations, excise tax estimates, and comparison of mitigation approaches (cutback vs. gross-up vs. shareholder vote)
- **Equity award tax summary**: Per-award type tax treatment at grant, vest, exercise, and sale with applicable rates and holding period requirements
- **Risk items and recommendations**: Prioritized list of issues, correction opportunities, and structuring alternatives
- **International tax overlay** (if applicable): Jurisdiction-by-jurisdiction treatment and filing obligations

## Quality Checks

- Verify that 280G base amount calculations use the correct five-year lookback period and include all required compensation elements (W-2 Box 1, not just base salary)
- Confirm Section 409A analysis distinguishes between grandfathered (pre-2005) and post-effective date arrangements
- Check that ISO analysis accounts for AMT implications, not just regular tax treatment
- Ensure equity valuations reference contemporaneous 409A valuations or other defensible FMV determinations
- Validate that recommended correction methods match current IRS correction programs and deadlines [VERIFY]
- Cross-check all statutory thresholds, tax rates, and penalty rates against current law — flag any amounts that may have been adjusted for inflation or legislative change [VERIFY]
- Confirm international analysis reflects current treaty provisions and local law, not outdated guidance [VERIFY]

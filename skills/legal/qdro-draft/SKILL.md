---
name: qdro-draft
description: Drafts Qualified Domestic Relations Orders (QDROs) compliant with ERISA §206(d)(3) and IRC §414(p) to divide retirement benefits in divorce. Handles defined benefit pensions, 401(k)s, and defined contribution plans with plan-specific division formulas, coverture fractions, and alternate payee protections. Use when drafting QDROs, dividing retirement assets post-judgment, or preparing domestic relations orders for plan administrator review.
tags:
  - drafting
  - litigation
  - pleading
---

# Qualified Domestic Relations Order (QDRO)

Drafts a court-ready QDRO that divides retirement benefits between a plan participant and alternate payee pursuant to a divorce decree, compliant with ERISA and the specific plan's requirements.

## Prerequisites

1. **Divorce decree or marital settlement agreement** — with case number, filing date, and any provisions referencing retirement benefits
2. **Retirement plan documents** — plan name (exact IRS-registered name), plan number, plan type (DB/DC/401(k)), plan administrator contact, and any model QDRO language the administrator requires
3. **Party information** — full legal names, DOBs, SSNs, current addresses for both participant and alternate payee
4. **Key dates** — marriage date, separation date, agreed valuation date
5. **Division terms** — percentage or dollar amount, division method (shared payment vs. separate interest for DB plans), treatment of earnings/losses between valuation and segregation

## Output Structure

### Court Caption & Recitals

- Match caption format to local court rules of the divorce jurisdiction
- Reference divorce decree by exact date and case number
- State the order is intended to qualify under ERISA §206(d)(3) and IRC §414(p)
- Include mandatory ERISA findings:

| Required Finding | Purpose |
|---|---|
| Does not require increased benefits | ERISA §206(d)(3)(D)(i) |
| Does not require benefit type/form not provided by plan | ERISA §206(d)(3)(D)(ii) |
| Does not require benefits already assigned to another alternate payee | ERISA §206(d)(3)(D)(iii) |

### Definitions Section

Define at minimum:

| Term | Notes |
|---|---|
| Participant | Plan member whose benefits are divided |
| Alternate Payee | Former spouse receiving benefits |
| Plan | Full legal name + plan number |
| Plan Administrator | Entity + address |
| Valuation Date | Date for calculating division |
| Marital Coverture Fraction | If applicable (months married during participation ÷ total months of participation) |
| Accrued Benefit / Account Balance | Per plan type |
| Benefit Commencement Date | DB plans only |

### Division Methodology

**Defined Contribution (401(k), 403(b), etc.):**
- State exact percentage or dollar amount
- Specify valuation date
- Address gains/losses from valuation date through segregation date
- State whether alternate payee directs investments post-segregation

**Defined Benefit (Pension):**
- Specify method: **shared payment** (% of each payment to participant) or **separate interest** (independently calculated benefit, alternate payee can commence separately)
- Include coverture fraction formula if dividing marital portion only
- Address: early retirement subsidies, COLAs, ancillary benefits — specify who retains each
- Specify form of benefit (lump sum eligibility vs. annuity only — must not exceed plan options)

### Alternate Payee Rights & Protections

```
☐ Right to designate own beneficiaries
☐ Right to receive plan information from administrator
☐ Pre-retirement survivor benefit rights (specify % if applicable)
☐ Protection from participant loans/hardship withdrawals against segregated share
☐ Immediate vesting upon qualification regardless of participant's vesting schedule
☐ Protection from plan amendments reducing awarded benefits
```

### Plan Administrator Directives

1. Segregate alternate payee's share as of valuation date
2. Establish separate account (DC plans) or calculate separate benefit (DB plans)
3. Grant alternate payee beneficiary rights including distribution options and investment direction
4. Process distributions per plan terms — note QDRO distributions are rollover-eligible and exempt from 10% early withdrawal penalty under IRC §72(t)(2)(C)
5. Provide written notice to both parties upon qualification
6. Notify both parties of segregated balance/benefit amount

### Compliance Certifications & Effective Date

- Certify compliance with ERISA §206(d)(3), IRC §414(p), and applicable state domestic relations law
- Repeat the three mandatory ERISA findings from recitals
- Effective date: typically date of court signature or date plan administrator deems qualified, whichever is later
- Termination conditions: note ERISA generally does **not** permit termination of QDRO rights based on remarriage for retirement plans, regardless of state law

### Signature Block

- Judge signature line with printed name, title, date
- Court certification that order meets ERISA/IRC requirements
- Check local rules for seal or clerk certification requirements

## Guidelines

- **Always match plan administrator's model language** when available — deviations are the #1 cause of QDRO rejection
- **Never require benefits the plan doesn't offer** (e.g., lump sum from a plan that only pays annuities)
- **Verify plan type before drafting** — DB and DC plans require fundamentally different QDRO structures
- **Federal plans use different instruments**: military (USFSPA court order), FERS/CSRS (court order acceptable for processing, not ERISA QDROs), TSP (retirement benefits court order per 5 CFR §1653)
- **Tax treatment**: alternate payee reports distributions as own income (IRC §402(e)(1)(A)); participant is not taxed on amounts paid to alternate payee under QDRO
- **Key regulatory references**: ERISA §206(d)(3)(B) (definition), IRC §414(p) (tax code parallel), 29 CFR §2530.206 (DOL regulations) [VERIFY]
- **Do not include SSNs in the body** if the jurisdiction requires them filed under seal or on a separate confidential information sheet
- **Flag missing information** explicitly rather than assuming or omitting — incomplete QDROs are routinely rejected by plan administrators

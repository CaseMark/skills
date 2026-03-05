---
name: structuring-infrastructure-debt-facilities
description: Designs infrastructure lending with mini-perm structures, cash sweep mechanics, and maintenance/distribution covenants. Use when structuring project debt, designing covenant packages, or analyzing infrastructure lending terms.
tags:
  - infrastructure-and-project-finance
metadata:
  author: casemark
  practice_areas:
    - Project Finance
    - Infrastructure Investment
    - PPP
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Infrastructure Debt Facilities

Designs infrastructure lending with mini-perm structures, cash sweep mechanics, and maintenance/distribution covenants for greenfield, brownfield, and PPP infrastructure projects.

## When To Use

- Structuring senior secured project debt for infrastructure assets (transport, energy, water, social infrastructure)
- Designing mini-perm or fully-amortizing tenor profiles matched to concession/asset life
- Building covenant packages with maintenance tests, distribution lock-ups, and cash sweep triggers
- Analyzing existing infrastructure credit agreements for refinancing, restructuring, or amendment
- Evaluating debt sizing and sculpting against base-case and downside cash flow projections
- Advising on PPP availability-payment or toll-revenue financing structures

## Inputs To Gather

- **Project description**: asset type, greenfield vs. brownfield, concession term or useful life, offtake/revenue model (contracted, merchant, availability-based)
- **Financial model outputs**: base-case and downside CFADS projections, construction draw schedule, target DSCR/LLCR/PLCR metrics
- **Sponsor requirements**: target leverage, equity IRR hurdles, distribution frequency preferences, refinancing intent
- **Lender market context**: bank vs. institutional debt, number of tranches, pricing benchmarks, hedging requirements
- **Regulatory/concession constraints**: permitted debt levels, step-in rights, change-of-control restrictions, government consent requirements [VERIFY jurisdiction-specific concession terms]
- **Security package scope**: asset pledges, assignment of project contracts, share pledges, direct agreements with counterparties

## Workflow

1. **Classify the project profile**
   - Determine revenue type: contracted (PPA, offtake, availability payment) vs. merchant vs. hybrid
   - Identify construction risk allocation (EPC fixed-price, alliance, cost-plus)
   - Confirm concession/license term and tail period available for debt repayment

2. **Size and sculpt the debt**
   - Apply target DSCR to base-case CFADS to derive maximum annual debt service
   - Sculpt repayment profile to match projected cash flow shape (front-loaded, level, or back-loaded)
   - Stress-test under downside scenarios; confirm LLCR and PLCR meet lender minimums (typically LLCR ≥ 1.15–1.25x for contracted assets, ≥ 1.30–1.40x for merchant) [VERIFY against current market benchmarks]
   - Determine mini-perm tenor (typically 5–7 years with soft/hard refinancing triggers) vs. fully-amortizing tenor

3. **Design the mini-perm structure (if applicable)**
   - Set initial maturity with cash sweep step-ups beginning at the soft mini-perm date
   - Define cash sweep percentages: e.g., 50% of excess cash flow from soft date, stepping to 75–100% at hard mini-perm date
   - Specify margin ratchet or step-up mechanics post-soft mini-perm to incentivize refinancing
   - Address refinancing risk allocation — sponsor equity cure rights, market disruption provisions

4. **Build the covenant package**
   - **Maintenance covenants**: set ongoing DSCR floors (e.g., historical and projected DSCR ≥ 1.10–1.20x); specify measurement periods (trailing 12 months, forward-looking 12 months)
   - **Distribution test**: require minimum DSCR (e.g., ≥ 1.20x historical and projected) plus no outstanding defaults; include lock-up DSCR threshold below which distributions are blocked entirely
   - **Reserve accounts**: define required balances for debt service reserve (typically 6 months' debt service), maintenance reserve, and insurance proceeds account
   - **Additional indebtedness test**: cap incremental borrowing by leverage ratio or DSCR impact; require rating agency confirmation for rated transactions
   - **Cash waterfall**: specify priority of payments — O&M costs → senior debt service → reserve funding → cash sweep (if triggered) → subordinated debt → equity distributions

5. **Structure the security package**
   - First-priority security over project assets, real property interests, and material project accounts
   - Assignment of key project agreements (offtake/PPA, EPC, O&M, insurance)
   - Direct/step-in agreements with major project counterparties and concession grantor
   - Share pledge over SPV equity; negative pledge and restriction on disposals
   - Identify any regulatory limitations on security enforcement [VERIFY local law perfection requirements]

6. **Address PPP-specific provisions (if applicable)**
   - Government consent and notification mechanics for debt and security
   - Lender step-in and cure rights under the concession/project agreement
   - Compensation on termination regime — how termination payments interact with debt repayment priority
   - Change-of-control and transfer restrictions aligned with concession terms

## Output

Produce a structured infrastructure debt facility report containing:

- **Executive summary**: asset overview, recommended debt quantum, tenor, and key terms
- **Debt sizing table**: annual CFADS, debt service, DSCR, LLCR, and PLCR under base and downside cases
- **Term sheet outline**: facility amount, tenor, amortization profile, mini-perm mechanics (if used), pricing, and key conditions precedent
- **Covenant schedule**: maintenance DSCR levels, distribution test thresholds, reserve requirements, cash sweep triggers with step-up percentages
- **Cash waterfall diagram**: sequential priority of payments from project revenue through equity distributions
- **Security package summary**: list of collateral, assignments, direct agreements, and perfection steps
- **Risk flags**: identified structural risks (refinancing risk, construction delay, revenue shortfall) with proposed mitigants

## Quality Checks

- Confirm DSCR sculpting produces no period below the minimum maintenance covenant level under base case
- Verify LLCR and PLCR calculations use consistent discount rates and cash flow periods
- Check that cash sweep mechanics and distribution lock-up thresholds are internally consistent (lock-up DSCR < distribution DSCR < default DSCR)
- Ensure mini-perm soft/hard dates, margin step-ups, and sweep percentages align and create genuine refinancing incentive
- Validate that the security package covers all material project contracts and accounts; flag any unsecured exposures
- Confirm reserve account sizing matches debt service profile and lender market standards [VERIFY against comparable recent transactions]
- Cross-check covenant definitions (e.g., CFADS, permitted leakage, capital expenditure carve-outs) for consistency between financial model and legal documentation

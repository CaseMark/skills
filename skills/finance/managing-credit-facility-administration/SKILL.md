---
name: managing-credit-facility-administration
description: Tracks revolving credit facility compliance with borrowing base, covenant calculations, and amendment documentation. Use when managing credit facilities, calculating borrowing availability, or tracking covenants.
tags:
  - management
  - corporate-finance
  - compliance
  - credit
metadata:
  author: casemark
  practice_areas:
    - Corporate Finance
    - Treasury
    - Financial Planning
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Credit Facility Administration

## When To Use

- Calculating borrowing base availability under a revolving credit facility
- Tracking financial covenant compliance (leverage ratio, interest coverage, fixed charge coverage, etc.)
- Preparing for quarterly or monthly compliance certificate submissions
- Managing amendment, waiver, or consent requests with the lender group
- Monitoring borrowing base eligibility criteria (eligible receivables, inventory, concentration limits)
- Coordinating draw-down requests, paydowns, or facility rollovers

## Inputs To Gather

- **Credit agreement** — executed version plus all amendments, waivers, and side letters
- **Borrowing base certificate** — most recent submission and any interim updates
- **Financial statements** — period-end balance sheet, income statement, and cash flow statement used for covenant calculations
- **Accounts receivable aging** — detail by counterparty with dilution, dispute, and past-due flags
- **Inventory report** — by category (raw materials, WIP, finished goods) with appraisal values if required
- **Covenant compliance certificate** — prior period's certificate for trend comparison
- **Lender correspondence** — any recent notices, consent requests, or default/reservation-of-rights letters
- **Amortization/fee schedule** — commitment fees, unused line fees, letter of credit fees, and maturity dates

## Workflow

1. **Map facility terms** — Extract key provisions from the credit agreement: facility size, maturity, applicable margins and pricing grid, mandatory prepayment triggers, borrowing base formula, and each financial covenant with its defined-term calculations. Note any springing covenants or seasonal adjustments.

2. **Calculate borrowing base availability**
   - Populate eligible receivables: exclude past-due (>90 days typical), cross-aged accounts, concentrations exceeding single-obligor caps, foreign receivables beyond sublimit, and government/affiliated-party exclusions. [VERIFY: specific eligibility criteria and aging thresholds per credit agreement]
   - Populate eligible inventory: apply advance rates by category (e.g., 65% finished goods, 50% raw materials), exclude slow-moving/obsolete, cap WIP if restricted. [VERIFY: advance rates and appraisal requirements]
   - Apply reserves: dilution reserve, rent reserve, priority-payable reserve, environmental reserves.
   - Compute net availability = borrowing base minus outstanding loans and letters of credit.

3. **Run covenant calculations**
   - Identify each financial covenant and its measurement period (trailing four quarters, single quarter, rolling twelve months).
   - Build calculations using credit-agreement-defined terms — not GAAP defaults — for Adjusted EBITDA, Total Funded Debt, Net Debt, Fixed Charges, etc. Watch for pro forma adjustments, permitted add-backs (restructuring, non-recurring), and capped add-back limits.
   - Compare computed ratios to covenant thresholds. Flag headroom or shortfall for each covenant.
   - For springing covenants, confirm whether the trigger condition (e.g., availability falling below a specified percentage of commitments) has been activated. [VERIFY: springing trigger thresholds]

4. **Prepare compliance deliverables**
   - Draft the compliance certificate in the form attached as an exhibit to the credit agreement.
   - Attach supporting schedules: borrowing base detail, covenant calculations, material debt schedule, and permitted investments/liens/dispositions tracker if required.
   - Confirm delivery deadline — typically 45-60 days post-quarter-end, 90-120 days post-fiscal-year-end. [VERIFY: specific delivery windows per agreement]

5. **Manage amendments and waivers**
   - If a covenant breach is anticipated, prepare a projected covenant forecast showing expected cure timeline.
   - Draft amendment/waiver request narrative explaining the operational context and proposed relief.
   - Identify required lender approvals: majority lenders vs. supermajority vs. unanimous consent based on the type of modification. [VERIFY: voting thresholds for specific amendment type]
   - Track amendment fees, legal costs, and any tightened terms (pricing step-ups, added reporting, additional reserves).

6. **Monitor ongoing obligations**
   - Track recurring reporting requirements: monthly/quarterly borrowing base certificates, annual audited financials, budget delivery, insurance certificate renewals.
   - Monitor negative covenant baskets: permitted indebtedness, liens, investments, restricted payments, asset dispositions. Maintain a running tally against basket capacities.
   - Flag upcoming maturity dates, interest period expirations, and SOFR/benchmark transition requirements.

## Output

Produce a **Credit Facility Administration Report** containing:

- **Facility summary** — commitment amount, drawn balance, available capacity, maturity date, current applicable margin
- **Borrowing base schedule** — line-by-line eligibility, advance rates, reserves, and net availability
- **Covenant compliance matrix** — each covenant, threshold, actual result, cushion/shortfall, and pass/fail status
- **Negative covenant basket tracker** — capacity used vs. remaining for key baskets (debt, liens, investments, restricted payments)
- **Upcoming deadlines** — next compliance certificate due date, interest payment dates, fee payment dates, reporting milestones
- **Issues and action items** — anticipated covenant pressure, approaching concentration limits, amendment status, or required lender communications

## Quality Checks

- Confirm all defined terms trace back to the credit agreement (not generic GAAP definitions) — especially Adjusted EBITDA add-backs and exclusions
- Verify arithmetic in borrowing base: individual line items should sum to reported totals; advance rates applied correctly
- Cross-check covenant inputs against the financial statements used in the compliance certificate
- Ensure pro forma adjustments (acquisitions, dispositions) are applied consistently with credit agreement provisions
- Validate that concentration limits, sublimits, and reserve calculations reflect the most recent amendment
- Confirm no events of default or potential events of default are overlooked (payment defaults, cross-defaults, MAC clauses, reporting failures)
- Mark any jurisdiction-specific or agreement-specific assumptions with [VERIFY]

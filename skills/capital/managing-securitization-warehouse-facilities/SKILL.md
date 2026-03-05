---
name: managing-securitization-warehouse-facilities
description: Structures warehouse lending for securitization programs with advance rates, eligibility criteria, and ramp-up analysis. Use when managing warehouse lines, structuring ramp facilities, or analyzing warehouse economics.
tags:
  - management
  - structured-finance
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Securitization Warehouse Facilities

## When To Use

- Structuring or renewing a warehouse credit facility to fund asset origination ahead of term securitization
- Evaluating advance rates, borrowing base mechanics, and concentration limits for a new or existing warehouse line
- Modeling ramp-up timelines and warehouse economics (carry cost vs. term takeout spread)
- Monitoring eligibility criteria compliance and mark-to-market triggers during the accumulation period
- Coordinating across originator, warehouse lender, trustee/custodian, and rating agencies during facility lifecycle

## Inputs To Gather

- **Facility term sheet or credit agreement** — committed amount, maturity, extension options, pricing grid (spread over SOFR/benchmark + fees)
- **Collateral parameters** — asset class (consumer ABS, RMBS, CLO, auto, etc.), eligible asset definitions, concentration limits, seasoning requirements, geographic or obligor caps
- **Advance rate schedule** — initial advance rates by collateral type, haircuts for non-performing or aged assets, mark-to-market methodology
- **Borrowing base certificate (most recent)** — current outstanding, eligible collateral balance, excess availability, compliance with sub-limits
- **Ramp-up plan** — target origination volume, expected time to fill the warehouse, pipeline data from originator
- **Term takeout assumptions** — expected securitization frequency, minimum deal size, target timing from warehouse close to term issuance
- **Fee structure** — commitment fees (drawn/undrawn), upfront fees, utilization fees, early termination penalties
- **Trigger/covenant package** — portfolio performance triggers (delinquency, default, loss), borrowing base deficiency cure periods, market value decline triggers [VERIFY specific trigger levels against credit agreement]

## Workflow

1. **Map the facility structure**
   - Identify the warehouse lender(s), SPV borrower, servicer, backup servicer, custodian, and any credit enhancer
   - Confirm whether the facility is a repurchase (repo) structure or a traditional revolving credit facility — this drives accounting treatment and margin call mechanics
   - Document the waterfall: interest and principal payment priorities, reserve account requirements, and excess spread disposition

2. **Analyze advance rates and borrowing base**
   - Build a matrix of advance rates by collateral sub-type (e.g., prime auto 85%, subprime auto 75%, non-performing 0%)
   - Calculate effective blended advance rate against the current or projected portfolio composition
   - Stress-test the borrowing base under adverse scenarios: rating migration, prepayment spikes, increased delinquencies reducing the eligible pool
   - Flag any assets that are approaching ineligibility (seasoning limits, performance triggers) and quantify the borrowing base impact of their exclusion

3. **Model warehouse economics**
   - Calculate all-in carry cost: benchmark rate + warehouse spread + commitment fees + hedging cost (if floating-rate collateral is warehoused against a fixed-rate takeout)
   - Compare carry cost against projected term securitization execution (weighted-average coupon on issued notes) to determine negative carry during ramp
   - Estimate total warehouse cost per securitization cycle: (average outstanding × all-in rate × ramp period in days / 360) + fixed fees
   - Assess break-even utilization — the minimum portfolio balance at which fee income or spread covers undrawn commitment fees

4. **Monitor eligibility and compliance**
   - Track concentration limits in real time: single obligor, geographic, industry, FICO/credit band, loan-to-value, or weighted-average life constraints
   - Confirm each new asset added to the warehouse satisfies eligibility representations before funding
   - Monitor portfolio performance triggers monthly: delinquency ratios (30/60/90+ days), cumulative default rate, cumulative net loss rate against threshold levels [VERIFY trigger definitions — some facilities use static pool metrics vs. dynamic pool]
   - Prepare borrowing base certificates per the required delivery schedule (typically monthly or with each funding request)

5. **Coordinate ramp-up and term takeout**
   - Maintain a ramp-up tracker: target fill date, current funded balance as a percentage of target deal size, pipeline-to-close conversion rates
   - Identify the optimal takeout window — balance between minimizing warehouse carry and achieving sufficient deal size for efficient term execution
   - Coordinate with rating agencies on preliminary feedback as the portfolio nears critical mass
   - Prepare the collateral tape and stratification tables needed for the term securitization offering documents

6. **Report facility status**
   - Produce a warehouse dashboard summarizing: outstanding balance, available capacity, days in warehouse (weighted average), portfolio composition snapshot, trigger headroom (distance to breach for each performance metric)
   - Highlight upcoming maturities, extension decision deadlines, and any required lender approvals
   - Escalate borrowing base deficiencies, trigger breaches, or collateral disputes immediately with recommended cure actions

## Output

- **Warehouse Facility Summary** — one-page overview of structure, counterparties, key terms, and current utilization
- **Borrowing Base Analysis** — detailed eligible collateral breakdown, advance rate application, excess availability calculation, and stress scenarios
- **Warehouse Economics Model** — carry cost analysis, break-even utilization, and comparison to term takeout economics across multiple ramp timelines
- **Compliance Monitoring Report** — concentration limit utilization, performance trigger headroom, eligibility exception log
- **Ramp-Up Tracker** — origination pipeline status, projected fill date, and recommended term takeout timing

## Quality Checks

- Advance rates applied match the executed credit agreement schedule — not indicative term sheet rates [VERIFY against final signed facility documents]
- Borrowing base arithmetic ties to the custodian's collateral report and servicer's tape
- All-in carry cost includes every fee component (commitment, utilization, admin, trustee) — not just the margin spread
- Concentration limits are tested against the full portfolio, not just the most recent additions
- Performance trigger calculations use the correct denominator and lookback period as defined in the facility agreement [VERIFY — some use trailing 3-month annualized, others use cumulative since closing]
- Mark-to-market valuations, if applicable, use the methodology specified in the agreement (dealer quotes, model-based, index-referenced)
- Ramp-up projections are reconciled against actual origination run-rates, not aspirational targets

---
name: analyzing-public-to-private-transactions
language: en
description: Evaluates take-private feasibility with premium analysis, financing capacity, governance considerations, and regulatory requirements. Use when analyzing take-private opportunities, modeling go-private premiums, or assessing delisting mechanics.
tags:
  - analysis
  - private-equity
  - regulatory
metadata:
  author: casemark
  practice_areas:
    - Private Equity
    - Leveraged Buyouts
    - Growth Equity
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Public To Private Transactions

## When To Use

- Evaluating whether a publicly traded company is a viable take-private candidate
- Modeling go-private premiums and assessing implied returns at various offer prices
- Analyzing financing capacity (debt quantum, equity check size) for a leveraged take-private
- Reviewing governance mechanics — board composition, shareholder approval thresholds, anti-takeover provisions
- Assessing regulatory filing requirements and timeline risk for transaction closing

## Inputs To Gather

- **Target company financials**: Last 3 years of audited financials plus LTM; current trading data (share price, volume, market cap, enterprise value)
- **Capital structure**: Outstanding shares (basic and fully diluted), convertible instruments, existing debt with change-of-control provisions
- **Governance documents**: Charter, bylaws, shareholder rights plan (poison pill), staggered board provisions, supermajority requirements
- **Shareholder register**: Top 20 holders, activist positions, insider ownership percentage, short interest
- **Comparable transactions**: Recent public-to-private deals in same sector with premium and multiple data
- **Financing market context**: Current leveraged loan and high-yield spreads, lender appetite for sector, available stapled financing terms
- **Regulatory profile**: Industry-specific approvals needed (HSR, CFIUS, sector regulators), jurisdictional requirements [VERIFY]

## Workflow

1. **Establish baseline valuation**
   - Calculate unaffected share price (use 30-day VWAP prior to any leak or rumor date)
   - Build DCF, comparable company, and precedent transaction valuations
   - Identify valuation disconnect — is the company trading below intrinsic value, and why (market dislocation, orphaned coverage, misunderstood story)?

2. **Model go-private premium range**
   - Analyze premiums paid in comparable take-privates (1-day, 30-day, 60-day premia)
   - Bracket offer price range: minimum to clear appraisal risk vs. maximum to meet return hurdle
   - Sensitivity table: offer price vs. sponsor IRR at varying leverage levels and exit multiples

3. **Assess financing capacity**
   - Determine maximum debt quantum using sector-appropriate leverage benchmarks (Senior / Total leverage, interest coverage, fixed charge coverage)
   - Size the equity check and test against fund concentration limits and co-invest appetite
   - Identify rollover equity participants (management, founders, strategic holders)
   - Stress-test the capital structure against downside operating scenarios

4. **Evaluate governance and deal mechanics**
   - Map approval path: one-step merger vs. two-step tender offer; simple majority vs. supermajority vote [VERIFY — depends on state of incorporation]
   - Identify anti-takeover defenses: poison pill, staggered board, no-shop / go-shop provisions likely in merger agreement
   - Assess special committee process requirements (particularly if management is part of the buyer group)
   - Flag MFW (Kahn v. M&F Worldwide) compliance for controller-led take-privates [VERIFY — Delaware law specific]

5. **Map regulatory and timeline risk**
   - HSR filing: determine if thresholds are met, estimate review timeline, identify potential second-request risk areas [VERIFY — current HSR thresholds]
   - CFIUS: assess whether foreign ownership or sensitive-sector issues trigger mandatory or voluntary filing
   - Sector-specific approvals: insurance, banking, telecom, defense — identify long-lead approvals early
   - SEC requirements: Schedule TO (tender offer) or proxy statement / Schedule 13E-3 (going-private transaction)
   - Build critical-path timeline from signing to closing

6. **Synthesize feasibility assessment**
   - Summarize go / no-go factors across valuation, financing, governance, and regulatory dimensions
   - Identify key risks and mitigants for each
   - Recommend next steps: pursue, pass, or pursue-with-conditions

## Output

Structure the deliverable as follows:

- **Executive summary**: One-page verdict with key metrics (offer price range, implied premium, equity check, target IRR, timeline estimate)
- **Valuation analysis**: Unaffected price, DCF range, comps range, precedent premium analysis
- **Premium and returns sensitivity**: Matrix of offer price vs. IRR at 3-5 leverage and exit scenarios
- **Financing assessment**: Debt capacity analysis, sources-and-uses table, credit metric summary
- **Governance and process**: Approval mechanics, anti-takeover provisions, special committee considerations
- **Regulatory and timeline**: Filing requirements, estimated review periods, critical-path Gantt
- **Risk matrix**: Top 10 risks ranked by likelihood and impact with proposed mitigants

## Quality Checks

- Confirm unaffected share price date is genuinely pre-leak — check for unusual trading volume or price movement in prior weeks
- Verify fully diluted share count includes all in-the-money options, RSUs, convertibles at the proposed offer price
- Ensure leverage multiples use consistent EBITDA definition (check for add-backs, run-rate adjustments)
- Cross-check premium statistics against a reliable precedent transaction database, not stale or cherry-picked comps
- Validate that governance analysis reflects the target's actual state of incorporation, not assumed Delaware defaults [VERIFY]
- Confirm HSR thresholds and CFIUS rules against current-year values — these adjust annually [VERIFY]
- Flag any change-of-control triggers in the target's material contracts (credit agreements, customer contracts, IP licenses) that could affect deal value

---
name: building-venture-return-models
language: en
description: Constructs venture return models with entry valuation, follow-on reserve, multiple scenario exits, and portfolio-level fund math. Use when modeling VC returns, calculating fund economics, or projecting portfolio outcomes.
tags:
  - modeling
  - venture-capital
  - portfolio
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Venture Capital
    - Seed/Series Investing
    - Startup Ecosystems
  document_types:
    - Model
  skill_modes:
    - Modeling
---
# Building Venture Return Models

## When To Use

- Modeling expected returns for a new fund or vintage year
- Evaluating a prospective deal's impact on portfolio-level fund math
- Sizing follow-on reserves and determining pro-rata allocation strategies
- Preparing fund economics exhibits for LP reporting or fundraising decks
- Stress-testing portfolio outcomes under varying exit timing, valuation, and dilution assumptions

## Inputs To Gather

- **Fund parameters**: Fund size, management fee rate and structure (on committed vs. invested), carry percentage, preferred return / hurdle rate, GP commit percentage
- **Portfolio construction**: Target number of investments, initial check size range, stage focus (pre-seed / seed / Series A+)
- **Entry deal terms**: Pre-money valuation, round size, ownership target, instrument type (priced equity, SAFE, convertible note), discount/cap terms if applicable
- **Follow-on strategy**: Reserve ratio (e.g., 1:1, 2:1 follow-on to initial), pro-rata rights, expected follow-on rounds and dilution per round
- **Exit assumptions**: Target exit multiples (base / upside / downside), expected hold period by scenario, exit modality (M&A vs. IPO vs. secondary)
- **Loss/write-off rate**: Historical or assumed percentage of portfolio companies returning 0-1x
- **Recycling policy**: Whether and how much the fund recycles management fees or early proceeds

## Workflow

1. **Set fund-level parameters**
   - Define fund size, fee structure (typical: 2% on committed capital during investment period, stepping down thereafter), carry split, and hurdle rate
   - Calculate investable capital after fees (e.g., $100M fund → ~$80-85M deployable over fund life) [VERIFY fee assumptions against actual LPA terms]
   - Determine GP commit amount and any co-invest sidecar capacity

2. **Build portfolio construction model**
   - Allocate investable capital across initial checks and follow-on reserves
   - Map target ownership at entry for each stage bucket (e.g., 10-15% at seed, 7-10% at Series A)
   - Model expected dilution per subsequent financing round (typical: 15-25% per round) [VERIFY against current market dilution data]
   - Calculate fully-diluted ownership at exit after projected dilution rounds, accounting for pro-rata follow-on participation

3. **Model individual deal economics**
   - For each representative investment, compute entry ownership, follow-on investment amounts, and resulting cost basis
   - Apply scenario-based exit valuations:
     - **Downside**: 0-1x return (write-off / acqui-hire)
     - **Base case**: 3-5x gross MOIC
     - **Upside**: 10-30x+ gross MOIC (fund returners)
   - Account for liquidation preferences, participation rights, and any ratchets that affect payout waterfall
   - Convert gross deal MOIC to net proceeds after accounting for dilution and preference stack

4. **Aggregate to portfolio-level fund math**
   - Apply a return distribution across the portfolio (e.g., power-law: 50% return 0-1x, 20% return 1-3x, 20% return 3-10x, 10% return 10x+)
   - Sum gross portfolio proceeds and compute gross fund TVPI and IRR
   - Run the GP/LP waterfall: return of contributed capital → preferred return → catch-up → carried interest split
   - Calculate net TVPI, net IRR, and DPI at projected exit timelines
   - Determine fund-returner threshold — what exit valuation a single company needs to return 1x the fund

5. **Sensitivity and scenario analysis**
   - Vary key drivers independently: loss rate (±10%), median exit multiple (±2x), hold period (±2 years), dilution per round (±5%)
   - Build a scenario matrix (bear / base / bull) with coherent macro assumptions per scenario
   - Identify which 2-3 variables have the highest sensitivity on net IRR and net TVPI
   - Test J-curve profile by modeling cash flow timing (drawdowns, distributions, net cash position by year)

6. **Document and present**
   - Summarize all key assumptions in a dedicated assumptions table
   - Present core outputs: net TVPI, net IRR, DPI trajectory, and fund-returner analysis
   - Include sensitivity tables and tornado charts for the highest-impact variables
   - Flag all [VERIFY] items for review against actual LPA terms, market benchmarks, or GP-provided data

## Output

- **Assumptions table**: Fund size, fees, carry, portfolio construction, dilution schedule, exit timing, loss rate
- **Deal-level schedule**: Per-company entry, follow-on, ownership, and scenario exit proceeds
- **Portfolio summary**: Gross TVPI, gross IRR, return distribution histogram
- **Waterfall output**: Net TVPI, net IRR, DPI, GP carry, LP net proceeds
- **Sensitivity matrix**: Net IRR / TVPI under varied loss rates, exit multiples, hold periods, and dilution
- **J-curve / cash flow schedule**: Year-by-year drawdowns, distributions, and net cash flow to LPs

## Quality Checks

- Investable capital + total fees + GP commit = fund size (balance check)
- Sum of initial checks + follow-on reserves = investable capital allocation
- Ownership-at-exit correctly reflects cumulative dilution from all subsequent rounds minus pro-rata participation
- Waterfall math reconciles: LP distributions + GP carry + unreturned capital = total gross proceeds
- Net IRR is computed on actual cash flow timing, not simplified annual averages
- Power-law return distribution is realistic — a single company should not drive >50% of gross returns unless explicitly modeled as a concentrated-bet strategy
- All jurisdiction-dependent tax treatment (e.g., QSBS exclusion, long-term capital gains rates) marked with [VERIFY]
- Management fee offset or rebate provisions reflected accurately per LPA terms [VERIFY]

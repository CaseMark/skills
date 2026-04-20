---
name: managing-tax-loss-harvesting
language: en
description: Identifies and executes tax-loss harvesting opportunities with wash sale compliance and tracking. Use when harvesting tax losses, managing wash sale rules, or optimizing after-tax returns.
tags:
  - management
  - asset-management
  - compliance
  - tax
metadata:
  author: casemark
  practice_areas:
    - Portfolio Management
    - Asset Management
    - Wealth Management
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Tax Loss Harvesting

## When To Use

- Reviewing portfolios for unrealized losses that can offset realized gains or ordinary income
- Approaching year-end and need to quantify harvesting opportunities across accounts
- A client has triggered significant realized gains and needs loss offsets before the tax year closes
- Rebalancing a portfolio and want to prioritize selling loss positions over gain positions
- Evaluating whether to harvest a loss now versus holding for long-term capital loss treatment

## Inputs To Gather

- **Portfolio holdings**: Current positions with cost basis (lot-level), acquisition dates, and current market values
- **Realized gains YTD**: Short-term and long-term capital gains already recognized in the current tax year
- **Income context**: Ordinary income estimate (losses can offset up to $3,000/$1,500 MFS of ordinary income annually) [VERIFY: current annual limit]
- **Loss carryforward balance**: Any capital loss carryforwards from prior tax years
- **Account structure**: Taxable vs. tax-advantaged accounts — harvesting only applies to taxable accounts
- **Wash sale exposure**: Positions held in IRAs, 401(k)s, or spouse accounts that could trigger wash sale disqualification
- **Replacement security candidates**: Substitute securities or ETFs to maintain market exposure without triggering wash sales
- **Client tax bracket**: Marginal federal and state rates to quantify the tax benefit of harvesting [VERIFY: applicable state tax treatment of capital gains]

## Workflow

1. **Screen for unrealized losses** — Pull all taxable account positions with unrealized losses. Separate into short-term (held ≤ 1 year) and long-term (held > 1 year). Prioritize short-term losses first since they offset higher-taxed short-term gains dollar-for-dollar.

2. **Quantify the tax benefit** — For each candidate position, calculate:
   - Loss amount (proceeds minus cost basis at the lot level)
   - Tax savings = loss × applicable marginal tax rate
   - Transaction costs (commissions, bid-ask spread on replacement)
   - Net benefit = tax savings − transaction costs
   - Discard candidates where net benefit is negligible or negative

3. **Check wash sale constraints** — For each candidate sale, verify:
   - The same or "substantially identical" security was not purchased 30 days before the sale date
   - No repurchase of the same or substantially identical security will occur within 30 days after the sale
   - No purchase of the same security exists in IRAs, Roth IRAs, or spouse accounts within the 61-day window [VERIFY: IRS guidance on cross-account wash sale treatment]
   - Dividend reinvestment plans (DRIPs) on the same security are paused or redirected

4. **Select replacement securities** — Identify substitutes that maintain asset allocation exposure without being "substantially identical":
   - Different index (e.g., swap S&P 500 ETF for a total market ETF)
   - Different fund family tracking a different benchmark
   - Individual stocks in the same sector as a proxy (higher tracking error)
   - Document why each replacement is not substantially identical

5. **Execute harvesting trades** — Sell loss positions using specific lot identification to maximize the loss. Simultaneously purchase replacement securities to avoid market exposure gaps. Record trade dates to start the 30-day post-sale wash sale window.

6. **Set wash sale calendar controls** — Create 31-day hold alerts for each replacement position. Block automated rebalancing or DRIP from repurchasing the original security within the window. After day 31, the original security can be repurchased if desired.

7. **Track basis adjustments** — If a wash sale is inadvertently triggered, the disallowed loss is added to the cost basis of the replacement shares. Document the adjusted basis and new holding period for affected lots.

## Output

- **Harvesting summary table**: Position | Cost Basis | Market Value | Unrealized Loss | Loss Type (ST/LT) | Estimated Tax Savings | Replacement Security | Trade Date | Wash Sale Window End
- **Net tax impact**: Total losses harvested, gains offset, remaining carryforward, and estimated tax savings at the client's marginal rate
- **Wash sale compliance log**: Each sold position mapped to its 61-day exclusion window, cross-account holdings check, and DRIP status
- **Replacement security rationale**: Brief note per swap explaining why the replacement avoids substantially identical classification
- **Post-harvest allocation comparison**: Pre- and post-harvest asset allocation to confirm portfolio drift is within acceptable tolerance

## Quality Checks

- Verify lot-level cost basis data — aggregate basis numbers mask partial-lot opportunities and can miscalculate gains/losses
- Confirm short-term vs. long-term classification by checking actual acquisition dates, not estimates
- Cross-reference all taxable and tax-advantaged accounts for wash sale exposure — omitting an IRA or 401(k) holding is the most common compliance failure
- Validate that replacement securities are not substantially identical (different index, different issuer, materially different composition)
- Ensure harvested losses are not artificially inflated by pending corporate actions (stock splits, mergers, return of capital adjustments)
- Flag any position where the unrealized loss is less than 2% of position value — transaction costs may eliminate the benefit
- Confirm the $3,000 ordinary income offset limit and carryforward mechanics apply correctly to the client's filing status [VERIFY: filing status impact on loss limits]

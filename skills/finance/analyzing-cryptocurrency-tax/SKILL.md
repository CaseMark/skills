---
name: analyzing-cryptocurrency-tax
description: Structures cryptocurrency tax analysis with cost basis tracking, gain classification, and reporting requirements. Use when analyzing crypto tax, tracking digital asset basis, or classifying crypto transactions.
tags:
  - analysis
  - tax
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
# Analyzing Cryptocurrency Tax

Structures cryptocurrency tax analysis with cost basis tracking, gain classification, and reporting requirements.

## When To Use

- Analyzing taxable events from cryptocurrency trading, staking, lending, or mining activity
- Determining cost basis methodology and gain/loss classification for digital asset dispositions
- Preparing or reviewing IRS Form 8949, Schedule D, or Schedule 1 entries related to crypto
- Evaluating international reporting obligations (FBAR, Form 8938) for crypto held on foreign exchanges
- Advising on tax-loss harvesting strategies or wash sale considerations for digital assets
- Reviewing DeFi protocol interactions (swaps, liquidity provision, yield farming) for taxable event classification

## Inputs To Gather

- **Transaction history**: Exchange CSV exports, on-chain wallet records, DeFi protocol interactions (include timestamps, amounts, token pairs, fees)
- **Acquisition records**: Purchase dates, prices paid in fiat, source of funds, any airdrop/fork/mining receipts
- **Disposition records**: Sale dates, proceeds in fiat, exchange or platform used
- **Cost basis method election**: FIFO, LIFO, specific identification, or highest-in-first-out [VERIFY: specific identification requires adequate records per IRS guidance]
- **Holding period data**: Date acquired vs. date disposed for short-term/long-term classification (threshold: 1 year)
- **Staking/mining/airdrop details**: Fair market value at time of receipt, nature of activity (hobby vs. trade/business)
- **DeFi activity**: Liquidity pool entries/exits, wrapped token conversions, governance token rewards
- **Foreign exchange accounts**: Whether assets were held on non-US exchanges or in non-US wallets for FBAR/FATCA analysis [VERIFY: current FinCEN guidance on virtual currency FBAR reporting requirements]
- **Prior-year carryforward losses**: Any capital loss carryovers from previous tax years

## Workflow

1. **Classify each transaction type**
   - Dispositions: sales, exchanges, crypto-to-crypto swaps (each is a taxable event)
   - Income events: mining rewards, staking income, airdrops, hard fork tokens, interest from lending
   - Non-taxable movements: wallet-to-wallet transfers (same owner), certain like-kind exchanges pre-2018 [VERIFY: like-kind exchange applicability ended for crypto after TCJA 2017]
   - DeFi-specific: determine whether liquidity provision constitutes a taxable exchange or not [VERIFY: no definitive IRS guidance on LP token tax treatment as of current date]

2. **Calculate cost basis for each lot**
   - Apply elected cost basis method consistently across the tax year
   - For crypto-to-crypto trades, determine FMV in USD at the exact time of transaction
   - Include transaction fees (gas fees, exchange fees) in the cost basis
   - For forked/airdropped tokens, cost basis is typically the FMV at time of receipt (which is also the income recognized)
   - Track basis through wrapped token conversions and bridge transactions

3. **Determine gain/loss character**
   - Short-term capital gain: held ≤ 1 year (taxed at ordinary income rates)
   - Long-term capital gain: held > 1 year (preferential rates: 0%, 15%, or 20% + possible 3.8% NIIT)
   - Ordinary income: mining, staking rewards, compensation paid in crypto
   - Self-employment income: mining/staking as a trade or business (subject to SE tax) [VERIFY: facts-and-circumstances test for trade/business determination]

4. **Assess wash sale exposure**
   - Identify dispositions at a loss followed by repurchase of substantially identical assets within 30 days before/after
   - [VERIFY: IRC § 1091 wash sale rules technically apply only to "stock or securities" — IRS has not formally extended to crypto, but proposed legislation may change this; check current status]
   - Document position taken and risk level if claiming losses near repurchases

5. **Evaluate international reporting obligations**
   - FBAR (FinCEN 114): required if aggregate foreign financial accounts exceed $10,000 at any point during the year [VERIFY: whether specific foreign crypto exchanges are classified as "foreign financial accounts"]
   - FATCA (Form 8938): applies if specified foreign financial assets exceed applicable thresholds
   - Form 1099-DA: [VERIFY: check effective date and broker reporting requirements under Infrastructure Investment and Jobs Act provisions]

6. **Compile tax reporting outputs**
   - Map each taxable disposition to Form 8949 (Part I for short-term, Part II for long-term)
   - Aggregate to Schedule D for net capital gain/loss
   - Report ordinary income items on Schedule 1 or Schedule C as appropriate
   - Apply $3,000 annual capital loss limitation against ordinary income; carry forward excess

## Output

- **Transaction classification table**: Each transaction categorized by type (disposition, income event, non-taxable transfer) with supporting rationale
- **Cost basis schedule**: Per-lot basis tracking showing acquisition date, cost, adjustments, and method applied
- **Gain/loss summary**: Aggregated short-term and long-term capital gains/losses with character breakdown
- **Income items summary**: Mining, staking, airdrop, and other ordinary income with FMV at receipt
- **Form 8949 / Schedule D draft entries**: Transaction-level detail ready for tax return preparation
- **International reporting checklist**: FBAR/FATCA applicability determination with supporting analysis
- **Risk flags and open items**: Wash sale exposure, positions lacking definitive IRS guidance, missing transaction data

## Quality Checks

- Verify that every disposition has a corresponding cost basis lot — flag orphan transactions with no acquisition record
- Confirm cost basis method is applied consistently (no cherry-picking between FIFO and specific ID within the same year without proper election)
- Cross-check that total proceeds match exchange 1099-B/1099-DA amounts where available
- Validate that holding periods are calculated correctly (acquisition date + 1 day begins the count)
- Ensure FMV sources are documented and defensible (e.g., CoinMarketCap, CoinGecko, exchange spot price at timestamp)
- Check for double-counting: transfers between own wallets should not appear as dispositions
- Confirm all income events are captured — search for staking rewards, airdrops, and referral bonuses that clients commonly overlook
- Flag any transaction exceeding $10,000 for potential Form 8300 or structuring considerations [VERIFY: Form 8300 digital asset reporting effective date]
- Mark all jurisdiction-dependent conclusions with [VERIFY] for state-level crypto tax treatment variations

---
name: managing-crypto-asset-analysis
description: Structures cryptocurrency and digital asset analysis with protocol evaluation and market assessment. Use when analyzing crypto assets, evaluating blockchain protocols, or assessing digital asset markets.
tags:
  - management
  - financial-technology
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Fintech
    - Payments
    - Digital Banking
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Crypto Asset Analysis

## When To Use

- Coordinating due diligence on a cryptocurrency or digital asset for investment, lending, or custody decisions
- Structuring a protocol-level evaluation for a Layer 1, Layer 2, or DeFi project
- Preparing a management-level report on crypto market exposure, portfolio composition, or risk posture
- Assessing a token's fundamentals before listing, integration, or partnership decisions
- Reviewing digital asset holdings for regulatory reporting or audit preparation

## Inputs To Gather

- **Asset identification**: Token name, ticker, contract address(es), chain(s) deployed on, token standard (ERC-20, SPL, BEP-20, etc.)
- **On-chain data**: Total supply, circulating supply, holder distribution, transaction volume, active addresses, smart contract audit status
- **Protocol documentation**: Whitepaper, technical docs, governance framework, roadmap, changelog history
- **Market data**: Price history, trading volume across exchanges (CEX and DEX), liquidity depth, market cap ranking
- **Team and governance**: Core team backgrounds, DAO structure, multisig configuration, treasury holdings, vesting schedules
- **Regulatory context**: Token classification posture (utility vs. security vs. commodity), jurisdiction of issuer, any enforcement actions or no-action letters [VERIFY]
- **Competitive landscape**: Comparable protocols, market share metrics, TVL (Total Value Locked) benchmarks where applicable

## Workflow

1. **Define scope and asset classification**
   - Confirm whether the asset is a Layer 1 native token, Layer 2/rollup token, DeFi governance token, stablecoin, wrapped asset, NFT collection, or other category
   - Establish the analysis purpose: investment thesis, risk assessment, custody eligibility, regulatory compliance, or portfolio rebalancing
   - Identify the audience (investment committee, compliance team, board, external auditors)

2. **Conduct protocol-level evaluation**
   - Review consensus mechanism, validator/node economics, and network security model
   - Assess smart contract risk: audit history, bug bounty program, incident history, upgradeability patterns (proxy contracts, timelocks)
   - Evaluate decentralization metrics: Nakamoto coefficient, validator concentration, governance participation rates
   - Examine tokenomics: inflation/deflation schedule, staking yields, fee burn mechanisms, treasury runway

3. **Perform market and liquidity analysis**
   - Map trading venues and assess liquidity depth (order book depth at 1% and 2% slippage)
   - Identify concentration risk: percentage of supply held by top 10/50/100 wallets
   - Review historical volatility, correlation to BTC/ETH, and drawdown patterns
   - Flag wash trading indicators or abnormal volume spikes [VERIFY exchange-reported vs. adjusted volume]

4. **Assess regulatory and compliance posture**
   - Determine token classification under applicable frameworks (Howey test, MiCA, MAS guidelines) [VERIFY jurisdiction-specific rules]
   - Check sanctions screening status (OFAC, EU sanctions lists) for contract addresses and known team wallets
   - Review AML/KYC posture of primary trading venues
   - Note any pending or concluded regulatory actions against the issuer or protocol

5. **Synthesize risk matrix and recommendations**
   - Score across dimensions: technology risk, market risk, liquidity risk, regulatory risk, counterparty risk, smart contract risk
   - Assign an overall risk tier (e.g., Low / Medium / High / Do Not Proceed)
   - Provide actionable recommendations: position sizing guidance, hedging considerations, monitoring triggers, rebalancing thresholds

6. **Compile management report and coordinate review**
   - Draft executive summary with key findings and risk tier
   - Circulate to relevant stakeholders (portfolio managers, compliance, legal)
   - Track open items, pending verifications, and escalation flags
   - Set review cadence (monthly, quarterly) based on asset volatility and materiality

## Output

The deliverable is a **Crypto Asset Analysis Report** structured as:

- **Executive Summary**: Asset name, classification, risk tier, key recommendation (1 paragraph)
- **Protocol Overview**: Chain, consensus, tokenomics summary, audit status
- **Market Assessment**: Liquidity profile, price performance, holder concentration
- **Risk Matrix**: Scored table across technology, market, liquidity, regulatory, and smart contract dimensions
- **Regulatory Status**: Classification posture, sanctions screening results, compliance flags [VERIFY]
- **Recommendations**: Position guidance, monitoring triggers, next review date
- **Open Items**: Unresolved verifications, pending data, escalation items marked with [VERIFY]

## Quality Checks

- All on-chain data references include block explorer links or data provider sources (e.g., Etherscan, Dune, DeFiLlama)
- Token supply figures reconcile between CoinGecko/CoinMarketCap and on-chain contract queries — flag discrepancies
- Smart contract audit citations include auditor name, date, and scope — note if audit predates significant contract upgrades
- Regulatory classification analysis cites the specific framework applied and notes jurisdictional limitations [VERIFY]
- Liquidity figures distinguish between reported and adjusted volume; note methodology
- Risk scores use a consistent rubric defined at the top of the matrix — no ad hoc ratings
- Report clearly separates factual findings from analyst opinions and forward-looking statements
- All [VERIFY] tags are resolved or explicitly carried forward as open items before final distribution

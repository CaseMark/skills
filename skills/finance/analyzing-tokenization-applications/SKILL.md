---
name: analyzing-tokenization-applications
description: Evaluates real-world asset tokenization with legal structure, market infrastructure, and liquidity analysis. Use when analyzing tokenization, evaluating security tokens, or assessing asset digitization.
tags:
  - analysis
  - financial-technology
metadata:
  author: casemark
  practice_areas:
    - Fintech
    - Payments
    - Digital Banking
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Tokenization Applications

Evaluates real-world asset tokenization (RWA tokenization) projects across legal structure, token design, market infrastructure, regulatory posture, and liquidity mechanisms. Produces a structured analysis report suitable for investment committees, compliance teams, or strategic planning.

## When To Use

- Evaluating a proposed tokenization of real estate, private credit, fund interests, commodities, or other illiquid assets
- Conducting due diligence on a security token offering (STO) or tokenized asset platform
- Comparing tokenization structures (e.g., direct issuance vs. SPV-wrapped vs. fund tokenization)
- Assessing whether an existing asset class is a viable candidate for on-chain representation
- Reviewing a tokenization platform's infrastructure, custody model, and transfer mechanics

## Inputs To Gather

- **Asset description**: Asset class, valuation methodology, underlying cash flows, and ownership chain
- **Token structure**: Token standard (ERC-20, ERC-1400, ERC-3643, etc.), chain selection, smart contract features (whitelisting, forced transfers, dividend distribution)
- **Legal wrapper**: SPV formation docs, offering memorandum, subscription agreements, transfer restrictions
- **Regulatory posture**: Jurisdiction(s), exemption relied upon (e.g., Reg D 506(b)/(c), Reg S, Reg A+, MiFID II prospectus exemption) [VERIFY jurisdiction-specific exemptions]
- **Market infrastructure**: Primary issuance platform, secondary trading venue (ATS, MTF, or bilateral), transfer agent, KYC/AML provider, custodian
- **Investor base**: Target investor profile (accredited, qualified purchaser, retail), geographic restrictions, minimum investment size

## Workflow

1. **Map the asset-to-token chain** — Trace from the underlying asset through the legal entity structure to the on-chain token. Identify each layer: asset holder → SPV/issuer → token contract → investor wallet. Flag any gaps in the ownership chain or unclear beneficial ownership mapping.

2. **Evaluate token design decisions**
   - Confirm token standard supports required compliance features (transfer restrictions, forced transfers for court orders, cap table snapshots for distributions)
   - Assess whether on-chain logic matches off-chain legal rights (e.g., does a token transfer actually convey legal ownership, or only an economic interest?)
   - Review smart contract audit status and upgrade mechanisms

3. **Analyze regulatory classification**
   - Determine whether the token constitutes a security under applicable law (apply Howey test for US; assess under MiFID II financial instruments definition for EU) [VERIFY applicable test per jurisdiction]
   - Identify the offering exemption and confirm investor eligibility requirements are enforced on-chain or at the platform level
   - Check broker-dealer, transfer agent, and ATS registration requirements [VERIFY state blue-sky requirements if US-based]

4. **Assess market infrastructure and liquidity**
   - Evaluate primary distribution mechanics (direct subscription, auction, book-building)
   - Analyze secondary market options: Is there an ATS/MTF listing? What are historical trading volumes and bid-ask spreads if available?
   - Review lockup periods, transfer restriction windows, and any contractual ROFR provisions that constrain liquidity
   - Estimate realistic liquidity premium/discount relative to traditional securitization of the same asset class

5. **Review custody and operational risk**
   - Identify custodial model (self-custody, qualified custodian, omnibus vs. segregated)
   - Assess key-management architecture, multisig requirements, and disaster recovery
   - Evaluate oracle dependencies for any on-chain valuations or cash flow triggers
   - Review reconciliation process between on-chain records and off-chain registrar/transfer agent

6. **Benchmark against alternatives** — Compare tokenized structure against traditional alternatives (e.g., LP interest in a fund, REIT shares, securitized notes) on cost basis, time-to-settlement, investor access, reporting transparency, and ongoing administrative burden.

## Output

Structure the analysis report with these sections:

- **Executive Summary**: One-paragraph verdict on viability, key strengths, and primary risks
- **Asset & Structure Overview**: Asset description, legal wrapper, token mechanics diagram
- **Regulatory Analysis**: Classification, exemption, jurisdictional constraints, ongoing compliance obligations
- **Infrastructure Assessment**: Platform, custody, KYC/AML, transfer agent, secondary venue evaluation
- **Liquidity Analysis**: Expected liquidity profile, lockup terms, secondary market depth, liquidity discount estimate
- **Risk Matrix**: Tabular summary of risks (smart contract, regulatory, counterparty, market, operational) rated by likelihood and severity
- **Comparative Benchmark**: Side-by-side against non-tokenized alternatives on 4-6 key dimensions
- **Recommendations**: Go/no-go assessment with conditions, or specific structural modifications to improve viability

## Quality Checks

- Every claim about regulatory classification cites the specific statute or rule — mark [VERIFY] if jurisdiction-specific and not independently confirmed
- Token standard features are validated against actual smart contract capabilities, not just marketing materials
- Liquidity projections are flagged as estimates and distinguish between contractual liquidity mechanisms and organic secondary trading
- Ownership chain is traced end-to-end; any break between on-chain token and off-chain legal title is explicitly called out
- Custody arrangement is assessed against qualified custodian requirements where applicable (e.g., SEC Investment Advisers Act custody rule) [VERIFY]
- Analysis does not conflate technological decentralization with legal/regulatory decentralization — SPV-issued tokens on a public chain are still centrally administered securities

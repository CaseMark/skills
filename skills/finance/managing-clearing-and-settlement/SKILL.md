---
name: managing-clearing-and-settlement
description: Structures central clearing analysis with CCP margin methodology and default waterfall assessment. Use when managing clearing relationships, analyzing CCP margins, or evaluating default waterfalls.
tags:
  - management
  - quantitative-finance
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Quantitative Analysis
    - Structured Products
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Clearing and Settlement

Structures end-to-end clearing and settlement analysis across asset classes, covering CCP margin methodology, default waterfall adequacy, settlement cycle compliance, and netting efficiency for centrally cleared and bilaterally settled instruments.

## Why This Skill Exists

Central clearing and settlement sit at the core of financial system plumbing. A single CCP failure — or even a prolonged margin call dispute — can cascade across interconnected participants, freezing liquidity and triggering systemic contagion. The 2008 Lehman default demonstrated that bilateral OTC settlement without central netting magnifies counterparty risk; post-crisis reforms under Dodd-Frank Title VII (mandatory clearing for standardized swaps via DCOs), Title VIII (designation of systemically important FMUs), EMIR (EU mandatory clearing obligations and CCP supervision under ESMA), and the CPMI-IOSCO Principles for Financial Market Infrastructures (PFMIs, 2012) collectively mandate robust clearing architecture with prefunded default resources, margin adequacy, and recovery/resolution planning.

Practitioners must navigate real operational complexity: DTCC/NSCC processes ~$2.5 trillion in U.S. equities and fixed-income daily; LCH SwapClear clears the majority of global interest rate swaps; CME Clearing handles futures and options margin calls intraday; ICE Clear Credit manages CDS clearing; Eurex Clearing operates the prisma margin methodology for cross-asset portfolios. SEC Rule 15c6-2 (effective May 2024) requires broker-dealers to establish written agreements for settlement allocation, complementing the T+1 cycle under Rule 15c6-1(a). An agent operating in this domain must understand margin types (initial margin, variation margin, default fund contributions), netting mechanics (multilateral netting, payment-vs-payment, delivery-vs-payment), and default waterfall sequencing — or risk producing analysis that is operationally useless or regulatorily non-compliant.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before drafting any clearing/settlement analysis, gather the following from the user:

1. **Asset class(es) in scope?** (e.g., listed derivatives, OTC IRS, CDS, equities, repo, FX — default: OTC interest rate swaps)
2. **CCP(s) involved?** (e.g., LCH SwapClear, CME Clearing, ICE Clear Credit, DTCC/NSCC, Eurex — default: LCH SwapClear)
3. **Jurisdiction and regulatory regime?** (U.S. CFTC/SEC, EU EMIR/ESMA, UK EMIR, cross-border — default: U.S. CFTC)
4. **Analysis purpose?** (margin adequacy review, default waterfall stress test, settlement cycle compliance, netting optimization, onboarding a new CCP, clearing mandate assessment — default: margin adequacy review)
5. **Participant type?** (clearing member, buy-side client clearing through FCM/GCM, CCP risk team, regulator — default: clearing member)
6. **Portfolio size and composition?** (notional, trade count, tenor distribution, currency mix — request specifics)
7. **Time horizon for analysis?** (point-in-time snapshot, historical back-test period, forward-looking stress window — default: point-in-time with 2-year lookback)
8. **Known constraints or concerns?** (liquidity buffers, concentration limits, wrong-way risk, recent margin call disputes, pending regulatory changes)

### Documents to Request

- Current CCP margin parameter disclosures (e.g., LCH margin methodology PDFs, CME SPAN/PRIME documentation)
- Recent margin call statements and intraday call history (minimum 90 days)
- Default fund contribution notices and latest CCP quantitative disclosure (CPMI-IOSCO public disclosure framework)
- Portfolio position reports with trade-level detail (product, notional, maturity, currency, counterparty)
- Clearing agreements (FCM/client clearing addenda, CCP rulebook extracts relevant to default procedures)
- Settlement instructions and fails history (minimum 30 days)
- Any recent CCP stress test results or fire drill reports

---

## Step 1: Map the Clearing and Settlement Architecture

Document the full clearing chain from execution to final settlement.

| Layer | Component | Detail to Capture |
|-------|-----------|-------------------|
| Execution | Trading venue / bilateral | SEF, exchange, voice, platform identifiers |
| Affirmation/Matching | Middleware | MarkitWire, Traiana, DTCC CTM — match rates and STP % |
| Clearing submission | CCP gateway | Real-time vs. batch, acceptance/rejection rates |
| Novation | CCP interposes | Original bilateral trade replaced by two CCP-facing legs |
| Margining | CCP margin engine | IM model (SIMM, SPAN, prisma, VaR-based), VM frequency |
| Netting | Multilateral netting | Netting set definition, compression participation |
| Settlement | CSD / payment system | DvP model (1/2/3), settlement currency, CLS for FX legs |
| Reconciliation | Post-settlement | Breaks, fails management, buy-in procedures |

**Deliverable:** Architecture diagram (text-based flow) and component inventory table with responsible parties, SLAs, and escalation contacts.

---

## Step 2: Analyze CCP Margin Methodology

For each CCP in scope, decompose the margin framework:

### 2a. Initial Margin (IM)

| CCP | IM Model | Confidence Level | Lookback Period | MPOR | Anti-Procyclicality Tool |
|-----|----------|------------------|-----------------|------|--------------------------|
| LCH SwapClear | Filtered Historical VaR | 99.7% | 10+ years incl. stress | 5 days (members) / 7 days (clients) | 25% stress period floor + buffer |
| CME Clearing | SPAN → PRIME (transition) | 99%+ (product-dependent) | Varies | 1–5 days by product | Price scan range floors |
| ICE Clear Credit | Spread margin + jump-to-default | 99%+ | Stress-calibrated | 5 days for CDS | Minimum margin floors |
| Eurex | Prisma (portfolio-based) | 99.0%–99.7% (tiered) | Historical + stress | 2 days (equities) / 5 days (OTC) | Floor methodology per EMIR RTS |

For each, assess:
- **Model coverage gaps:** Does the IM model capture basis risk, curve risk, cross-currency risk, concentration risk, and jump-to-default (for credit)? [VERIFY against CCP model validation reports]
- **Procyclicality controls:** Confirm compliance with EMIR RTS 153 Art. 28 or CFTC Reg. 39.13 — margin should not drop more than 25% from the stress-period calibrated level
- **Margin period of risk (MPOR):** Verify MPOR assumptions align with product liquidity — illiquid/concentrated positions may require extended MPOR

### 2b. Variation Margin (VM)

- **Frequency:** At least daily; most CCPs call intraday (LCH runs multiple VM cycles)
- **Valuation methodology:** Mark-to-market vs. mark-to-model — identify products where model-based VM applies
- **Currency of payment:** Identify FX risk from non-USD collateral; haircut schedules for non-cash collateral
- **Grace periods and intraday deadlines:** Map exact cut-off times (e.g., LCH 09:00 London for VM call, 10:00 for payment) [VERIFY current CCP deadlines]

### 2c. Collateral Eligibility and Haircuts

| Collateral Type | Typical Haircut Range | Concentration Limit | Key Risks |
|-----------------|----------------------|---------------------|-----------|
| Cash (settlement currency) | 0% | None typically | Opportunity cost |
| G7 sovereign bonds (< 1yr) | 0.5–2% | Usually uncapped | Duration, FX if cross-currency |
| G7 sovereign bonds (> 10yr) | 3–8% | May apply | Interest rate / DV01 |
| Corporate bonds (IG) | 5–15% | 10–30% of requirement | Credit spread, liquidity |
| Equities (major index) | 10–25% | 10–25% of requirement | Gap risk, correlation |
| Gold | 10–15% | Varies | Price volatility |

**Deliverable:** Margin methodology comparison table, IM back-test results (breaches vs. confidence level), VM cash flow timeline, collateral optimization recommendations.

---

## Step 3: Evaluate Default Waterfall Adequacy

Map the CCP's default waterfall and stress-test each layer:

### Standard CCP Default Waterfall Sequence

| Priority | Resource Layer | Typical Sizing |
|----------|---------------|----------------|
| 1 | Defaulter's initial margin | Covers 99%+ of close-out losses under normal conditions |
| 2 | Defaulter's default fund contribution | Typically 5–15% of total default fund |
| 3 | CCP's first tranche of own capital (Skin-in-the-Game, SITG) | EMIR: 25% of minimum capital requirement; varies by CCP |
| 4 | Non-defaulting members' default fund contributions (mutualized) | Sized to cover "Cover 2" — simultaneous default of two largest members |
| 5 | CCP's second tranche of own capital | Varies; some CCPs commit additional equity |
| 6 | Assessment powers / rights of assessment | Capped (e.g., 1x or 2x default fund contribution per member) |
| 7 | Recovery tools | VM haircutting, partial tear-up, forced allocation |
| 8 | Resolution (regulatory intervention) | Title II OLA (U.S.), BRRD/CCP Recovery & Resolution Regulation (EU) |

For each layer, analyze:
- **Cover 2 adequacy:** Does the default fund cover simultaneous default of the two largest clearing members under extreme-but-plausible stress? [VERIFY against CCP's CPMI-IOSCO quantitative disclosures, Principle 4/7]
- **SITG sufficiency:** Is the CCP's skin-in-the-game meaningful relative to mutualized losses, or is moral hazard created?
- **Assessment caps and frequency:** What is each member's maximum exposure beyond initial margin + default fund contribution?
- **Recovery tool calibration:** Are VM haircutting triggers well-defined? Are partial tear-up and forced allocation rules transparent and legally enforceable?

**Deliverable:** Default waterfall diagram with dollar-sized layers, Cover 2 stress test summary, and assessment exposure calculation per member.

---

## Step 4: Settlement Cycle Compliance and Fails Analysis

### 4a. Settlement Cycle Mapping

| Market / Product | Standard Cycle | Regulatory Basis | Key Deadline |
|------------------|---------------|------------------|--------------|
| U.S. equities | T+1 | SEC Rule 15c6-1(a) (eff. May 2024) | DTC night cycle / day-of settlement |
| U.S. corporate/muni bonds | T+1 | SEC Rule 15c6-1(a) | NSCC CNS netting |
| U.S. Treasuries | T+1 | Industry convention (SEC push) | Fedwire DVP |
| EU equities | T+2 | CSDR Art. 5 | TARGET2-Securities |
| OTC derivatives (cleared) | Daily VM; IM on T+1 | CCP rulebook | CCP-specific deadlines |
| FX spot | T+2 (T+1 for CAD/USD) | Market convention | CLS settlement windows |

### 4b. Fails Analysis

- **Fails rate:** Calculate rolling 30/60/90-day fails rate by product, counterparty, custodian
- **Root cause taxonomy:** Inventory shortfall, timing mismatch, SSI error, collateral lock-up, operational break
- **CSDR mandatory buy-in exposure** (EU): Identify positions at risk of cash penalty regime (currently penalty-only; mandatory buy-in deferred)
- **Fails charges:** Quantify cost under Treasury fails charge (3% – Fed funds target rate floor at 0) and DTC fails tracking

**Deliverable:** Settlement cycle compliance matrix, 90-day fails trend analysis, root cause Pareto chart, remediation action plan.

---

## Step 5: Netting Efficiency and Compression

Quantify netting benefits and identify optimization opportunities:

| Metric | Calculation | Target |
|--------|-------------|--------|
| Multilateral netting ratio | 1 – (net settled value / gross trade value) | > 95% for equities (NSCC), > 80% for cleared swaps |
| Compression ratio | Notional eliminated / gross notional pre-compression | 30–70% for IRS portfolios (triReduce, Quantile) |
| Trade count reduction | Trades eliminated via compression / total trades | > 50% for mature portfolios |
| IM savings from netting | Portfolio IM vs. sum of individual trade IM | Report absolute $ and % reduction |

Actions:
- Assess eligibility for portfolio compression cycles (LCH SwapClear runs regular compression with TriOptima/Quantile)
- Evaluate cross-product netting benefits where CCP offers portfolio margining (e.g., Eurex prisma cross-margining between OTC and listed)
- Identify fragmented clearing across CCPs that prevents netting — model consolidation benefits vs. concentration risk

**Deliverable:** Netting efficiency report with before/after metrics, compression participation recommendations, CCP consolidation cost-benefit analysis.

---

## Step 6: Produce the Deliverable

Compile the final clearing and settlement analysis report with the following structure:

1. **Executive Summary** — Key findings, margin adequacy status, settlement compliance, and top 3–5 risk items
2. **Clearing Architecture Map** — From Step 1
3. **Margin Methodology Analysis** — IM/VM/collateral assessment from Step 2
4. **Default Waterfall Assessment** — Sizing, Cover 2 results, SITG analysis from Step 3
5. **Settlement Compliance Report** — Cycle mapping, fails analysis from Step 4
6. **Netting and Compression Optimization** — Efficiency metrics and recommendations from Step 5
7. **Risk Register** — Itemized risks with likelihood, impact, owner, and mitigation
8. **Regulatory Compliance Checklist** — Mapped to PFMI Principles, EMIR RTS, CFTC Part 39, SEC Rules
9. **Appendices** — Data sources, methodology notes, glossary, CCP contact details

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

Before finalizing, confirm with the user:

1. **Margin adequacy conclusions** — Do the IM back-test breach counts and VM liquidity assessments align with internal risk appetite? Any overrides needed?
2. **Default waterfall exposure** — Is the mutualized loss exposure (default fund + assessments) within the firm's tolerance? Flag if assessment caps are unclear.
3. **Settlement cycle gaps** — Are any markets or products at risk of non-compliance with T+1 requirements? Confirm remediation ownership.
4. **Netting/compression recommendations** — Are proposed CCP consolidation or compression cycle participations feasible given legal and operational constraints?
5. **Regulatory mapping completeness** — Have all applicable jurisdictions been covered? Any pending rule changes (e.g., SEC Treasury clearing mandate, EMIR 3.0 active account requirement) that should be flagged?

---

## Quality Audit

| # | Criterion | Pass/Fail |
|---|-----------|-----------|
| 1 | All CCPs in scope are identified with correct margin model names and parameters | |
| 2 | Initial margin confidence levels and MPOR are stated and sourced from CCP disclosures | |
| 3 | Default waterfall is sequenced correctly with dollar-sized estimates per layer | |
| 4 | Cover 2 adequacy is assessed against CPMI-IOSCO Principle 4 (credit risk) and Principle 7 (liquidity) | |
| 5 | Settlement cycles are mapped to correct regulatory basis (Rule 15c6-1, CSDR Art. 5, etc.) | |
| 6 | Fails analysis includes at least 30-day history with root cause categorization | |
| 7 | Netting ratios are calculated with clear gross-to-net methodology | |
| 8 | Collateral haircut schedules reference actual CCP-published tables [VERIFY] | |
| 9 | Anti-procyclicality controls are assessed per EMIR RTS 153 or CFTC Reg. 39.13 | |
| 10 | VM call timing and grace periods cite specific CCP operational deadlines [VERIFY] | |
| 11 | Assessment cap exposure is quantified per clearing member | |
| 12 | Recovery and resolution tools (VM haircutting, tear-up) are identified and legally referenced | |
| 13 | All [VERIFY] tags are resolved or explicitly flagged as pending confirmation | |
| 14 | Report does not contain generic filler — every statement is grounded in specific mechanics or data | |

---

## Guidelines

1. **Use CCP-specific terminology precisely** — SPAN is CME's legacy model; PRIME is CME's replacement; prisma is Eurex; filtered historical simulation is LCH. Do not interchange or genericize.
2. **Distinguish member vs. client clearing** — Margin treatment, portability, and default waterfall position differ materially between direct members and clients clearing through FCMs/GCMs. Always specify which perspective applies.
3. **Cite regulatory articles, not just statute names** — Reference "EMIR Art. 41" for margin requirements, "CFTC Reg. 39.13(g)(2)" for IM standards, "PFMI Principle 6" for margin — not just "EMIR" or "Dodd-Frank."
4. **Treat CCP quantitative disclosures as primary sources** — CPMI-IOSCO public quantitative disclosure data (published quarterly/semi-annually) is the authoritative baseline for Cover 2 analysis, default fund sizing, and credit/liquidity stress results. Mark any deviation with [VERIFY].
5. **Never assume uniform margin across CCPs** — The same portfolio cleared at LCH vs. CME vs. Eurex will produce different IM amounts due to model differences, lookback periods, and anti-procyclicality buffers. Always compare.
6. **Flag wrong-way risk explicitly** — Where collateral posted is correlated with the defaulter's exposure (e.g., a bank posting its own sovereign bonds while being a major clearing member in that sovereign's jurisdiction), this must be called out.
7. **Account for intraday liquidity demands** — Margin calls are not only end-of-day. Intraday VM and extraordinary IM calls (during volatility spikes) create acute liquidity stress. Model peak intraday exposure, not just end-of-day.
8. **Track regulatory pipeline** — Flag upcoming changes: SEC mandatory Treasury clearing (expected 2025–2026 phased), EMIR 3.0 active account requirements for EU participants clearing at UK CCPs, and any pending CCP recovery/resolution regulation updates.

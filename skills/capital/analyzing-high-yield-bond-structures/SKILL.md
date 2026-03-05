---
name: analyzing-high-yield-bond-structures
description: Evaluates high-yield issuance with call schedules, change of control puts, and restricted payment baskets. Use when analyzing HY bonds, comparing HY vs leveraged loan terms, or assessing issuer flexibility.
tags:
  - analysis
  - debt-capital-markets
metadata:
  author: casemark
  practice_areas:
    - DCM
    - Leveraged Finance
    - Debt Origination
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing High Yield Bond Structures

## When To Use

- Evaluating a new HY bond offering (144A/Reg S or registered) for investment or origination
- Comparing covenant packages across competing HY issuances in the same sector
- Assessing issuer flexibility under restricted payment, debt incurrence, and lien baskets
- Benchmarking HY bond terms against leveraged loan alternatives in a capital structure
- Reviewing call schedule economics and make-whole premiums for refinancing analysis
- Analyzing change-of-control provisions for M&A or LBO exposure

## Inputs To Gather

- **Offering memorandum or indenture** — full text including covenant definitions, call schedule exhibit, and description of notes
- **Deal pricing details** — coupon, issue price, OID (if any), maturity date, expected ratings (Moody's/S&P/Fitch)
- **Issuer financials** — LTM EBITDA, total debt, secured debt, cash position, and projected credit metrics
- **Comparable transactions** — recent HY issuances in the same rating tier and sector for covenant benchmarking
- **Capital structure diagram** — full debt stack showing priority, security, and guarantor coverage
- **Call schedule** — non-call period, par call dates, make-whole spread, equity clawback percentage and sunset

## Workflow

1. **Map the capital structure** — Identify where the HY notes sit relative to secured credit facilities, other unsecured debt, and any structural subordination through non-guarantor subsidiaries. Calculate the percentage of assets at guarantor vs. non-guarantor entities.

2. **Analyze call provisions and redemption economics**
   - Document the non-call period (typically NC/2 or NC/3 for standard HY)
   - Build the step-down call price schedule (e.g., 104.25 → 102.125 → 100)
   - Note equity clawback terms: percentage cap (typically 35–40%), time window, and funding source requirements
   - Identify make-whole premium formula and reference treasury rate plus spread
   - Flag any special redemption provisions (tax redemption, gaming/regulatory redemption)

3. **Evaluate change-of-control provisions**
   - Confirm the CoC put price (typically 101% of par)
   - Analyze the CoC definition: what triggers it (acquisition of >50% voting stock, merger, asset sale of all/substantially all) [VERIFY against specific indenture language]
   - Check for a "portability" or "CoC triggering event" structure requiring both a CoC *and* a ratings downgrade
   - Assess interaction with any CoC provisions in the secured credit facility

4. **Assess incurrence-based covenant package**
   - **Debt incurrence** — Identify the fixed-charge coverage ratio test (typically 2.0x) and carve-out baskets (general basket, credit facility basket, capital lease basket, acquired debt basket). Quantify each basket in dollar terms relative to issuer EBITDA.
   - **Restricted payments** — Map the builder basket formula (typically 50% of consolidated net income accruing from a start date), permitted investment baskets, and any "Available Amount" concept. Note the general RP basket size.
   - **Liens** — Document permitted lien baskets and any distinction between liens securing pari passu vs. junior obligations
   - **Asset sale covenant** — Identify the reinvestment period (typically 365–450 days), excess proceeds trigger amount, and offer price (typically 100% of par)
   - **Affiliate transaction thresholds** — Note board approval and fairness opinion trigger amounts

5. **Benchmark against comparable issuances**
   - Compare covenant flexibility across 3–5 recent deals in the same rating category
   - Highlight where the subject deal is tighter or looser than market on key baskets
   - Note any emerging "covenant innovations" or aggressive terms (e.g., EBITDA add-backs exceeding 25%, uncapped contribution debt baskets, J.Crew-style trapdoor provisions)

6. **Compare HY vs. leveraged loan alternative** (if applicable)
   - Contrast maintenance vs. incurrence covenant structures
   - Evaluate all-in cost of capital including OID, call premiums, and prepayment flexibility
   - Assess secured vs. unsecured trade-offs for recovery positioning
   - Note differences in amendment/waiver mechanics (simple majority for loans vs. supplemental indenture process)

## Output

Produce a structured analysis report containing:

- **Executive summary** — 3–5 sentence overview of the issuance, key structural features, and overall assessment of covenant flexibility (issuer-friendly, market, or investor-friendly)
- **Capital structure table** — Debt instrument, amount, rate, maturity, security, and priority
- **Call schedule matrix** — Date, call price, and effective yield-to-call at current trading levels
- **Covenant summary table** — Each major covenant, the applicable test/threshold, key basket amounts, and comparison to market benchmarks
- **Red flags and notable terms** — Provisions that deviate materially from market standard or create potential value leakage
- **HY vs. loan comparison matrix** (if applicable)

## Quality Checks

- Verify that all dollar-denominated baskets are cross-referenced against the issuer's LTM EBITDA to show relative size (e.g., "$50M general basket = ~0.5x LTM EBITDA")
- Confirm call schedule math: verify step-down intervals align with the stated non-call period and maturity
- Ensure CoC trigger language is quoted or closely paraphrased from the actual indenture — do not paraphrase loosely [VERIFY]
- Check that incurrence ratio calculations use the indenture's specific definition of "Fixed Charges" and "Consolidated Cash Flow" rather than generic EBITDA [VERIFY]
- Validate that EBITDA add-back provisions are captured, as these materially affect ratio-based covenant headroom
- Flag any provisions where governing law or jurisdiction affects enforceability (e.g., New York law vs. English law for cross-border issuances) [VERIFY]
- Cross-check restricted subsidiary vs. unrestricted subsidiary definitions — value leakage through unrestricted subsidiary designation is a key structural risk

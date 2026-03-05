---
name: structuring-term-loan-b-facilities
description: Designs institutional term loan structures with amortization schedules, repricing protection, and soft call provisions. Use when structuring TLBs, analyzing institutional loan terms, or comparing bank vs institutional debt.
tags:
  - debt-capital-markets
metadata:
  author: casemark
  practice_areas:
    - DCM
    - Leveraged Finance
    - Debt Origination
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Term Loan B Facilities

Designs institutional term loan structures with amortization schedules, repricing protection, and soft call provisions for leveraged finance transactions.

## When To Use

- Structuring a new TLB tranche for an LBO, recapitalization, or acquisition financing
- Comparing institutional term loan terms against bank loan (TLA) alternatives
- Analyzing repricing or refinancing economics on an existing TLB
- Evaluating amortization, excess cash flow sweep, and prepayment mechanics
- Advising on soft call protection windows and step-downs for a credit agreement

## Inputs To Gather

- **Transaction context**: LBO, M&A, dividend recap, refinancing, or add-on
- **Borrower profile**: issuer name, sector, credit rating (corporate family / instrument), sponsor (if any)
- **Facility size and tenor**: target principal amount, maturity (typically 7 years), any existing first-lien debt
- **Pricing indications**: SOFR spread, SOFR floor, OID range from arranger/bookrunner
- **Amortization requirement**: standard 1% p.a. or alternative schedule
- **Call protection terms**: soft call premium (typically 101 for 6 months), any hard no-call period
- **Excess cash flow sweep**: percentage tiers, leverage-based step-downs, starter basket/threshold
- **Credit agreement provisions**: MFN sunset, incremental capacity, ratio debt baskets, AHYDO considerations
- **Comparable transactions**: recent TLB pricings in the same sector/rating tier for benchmarking

## Workflow

1. **Define the capital structure context**
   - Map total debt stack: revolver, TLA, TLB, second lien, bonds
   - Calculate pro forma leverage (Total Debt / EBITDA, First Lien / EBITDA, Secured / EBITDA)
   - Confirm credit ratings or expected ratings; flag if split-rated [VERIFY]

2. **Set pricing and floor parameters**
   - Identify SOFR floor (market standard 0.00%–0.75%; confirm current convention) [VERIFY]
   - Determine spread based on rating tier and comparable deal analysis
   - Calculate OID and effective yield; convert to bond-equivalent yield for comparison
   - Assess all-in cost vs. high-yield bond alternative (crossover analysis)

3. **Build amortization and repayment schedule**
   - Standard: 1% annual amortization (0.25% quarterly) with bullet at maturity
   - Model mandatory prepayments from excess cash flow sweep with leverage step-downs (e.g., 50% > 4.0x, 25% > 3.5x, 0% > 3.0x) — confirm actual thresholds with credit agreement [VERIFY]
   - Model asset sale and debt incurrence sweep mechanics
   - Calculate weighted average life (WAL) under base case and downside scenarios

4. **Structure repricing and call protection**
   - Soft call: typically 101 premium for voluntary repricing within first 6 months post-closing [VERIFY period and premium against current market]
   - Distinguish between repricing transactions (spread reduction via amendment) and refinancing (new facility)
   - Evaluate MFN (most-favored-nation) protection on existing tranches — sunset period (typically 6–12 months), spread differential trigger (typically 50 bps)
   - Model the breakeven analysis: at what spread reduction does refinancing economics overcome soft call cost?

5. **Analyze covenant and flexibility provisions**
   - Springing financial covenant on revolver (typically first lien net leverage, tested only when revolver > 35% drawn) [VERIFY threshold]
   - Incremental facility capacity: ratio-based (typically inside closing date leverage) plus fixed-dollar basket
   - Permitted debt baskets, restricted payment capacity, and J. Crew / Chewy-style trapdoor provisions
   - AHYDO (applicable high-yield discount obligation) compliance if OID exceeds de minimis threshold [VERIFY: OID > 0.25% per year to maturity triggers AHYDO]

6. **Benchmark against comparables**
   - Pull 5–10 recent TLB transactions in same rating/sector cohort
   - Compare: spread, floor, OID, soft call period, WAL, leverage at close, ECF sweep terms
   - Identify where proposed terms sit relative to market (tight/wide/in-line)

## Output

Produce a **TLB Structuring Report** containing:

- **Executive summary**: facility size, tenor, pricing (spread + floor + OID = effective yield), key structural features
- **Capital structure table**: pro forma debt stack with leverage multiples at each tier
- **Amortization schedule**: quarterly principal payments, ECF sweep projections, WAL calculation
- **Repricing protection analysis**: soft call mechanics, breakeven repricing spread, MFN applicability
- **Comparable transaction table**: benchmarking grid with 5–10 recent deals
- **Key risk flags**: ratings migration sensitivity, SOFR floor value at different rate environments, covenant headroom
- **Open items**: any inputs still pending or terms requiring negotiation, marked [VERIFY]

## Quality Checks

- Confirm amortization sums to 1% p.a. (or stated alternative) and final bullet equals remaining principal
- Verify effective yield calculation accounts for OID amortization over expected life (not stated maturity)
- Check that ECF sweep step-down leverage thresholds align with credit agreement definitions of "Consolidated EBITDA" and "Net Debt"
- Ensure MFN analysis uses correct inside maturity date and spread differential trigger
- Validate AHYDO compliance math if OID is material (compare yield vs. AFR + 500 bps) [VERIFY: current AFR]
- Cross-check comparable deal data against Leveraged Commentary & Data (LCD), Pitchbook, or arranger term sheets
- Flag any covenant terms that deviate materially from LSTA market standards

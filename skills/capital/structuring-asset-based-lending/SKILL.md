---
name: structuring-asset-based-lending
language: en
description: Designs ABL facilities with borrowing base calculations, collateral eligibility criteria, and field exam requirements. Use when structuring ABL facilities, calculating borrowing availability, or analyzing collateral pools.
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
# Structuring Asset Based Lending

Designs ABL facilities with borrowing base calculations, collateral eligibility criteria, and field exam requirements.

## When To Use

- Structuring a new ABL revolving credit facility or term loan secured by working capital assets
- Calculating borrowing base availability against accounts receivable, inventory, or other eligible collateral
- Evaluating collateral pool quality and setting eligibility criteria for a prospective borrower
- Analyzing advance rates, reserves, and availability blocks for an existing or proposed facility
- Preparing for or reviewing field examination findings and their impact on borrowing capacity
- Comparing ABL structures across competing lender proposals or refinancing scenarios

## Inputs To Gather

- **Financial statements**: Trailing 12-month P&L, balance sheet, and cash flow statement; most recent monthly/quarterly interim financials
- **Accounts receivable aging**: Detailed AR aging schedule (current, 30, 60, 90, 90+ days) with concentration by obligor, cross-aging percentages, and dilution history (credits, returns, allowances)
- **Inventory reports**: Perpetual inventory or recent physical count broken out by raw materials, WIP, and finished goods; obsolescence reserves; NOLV (net orderly liquidation value) appraisal if available
- **Existing credit agreements**: Current facility terms, liens, intercreditor arrangements, and any subordination agreements
- **Collateral-specific data**: Equipment appraisals, real estate valuations, IP schedules, or other hard-asset detail if part of the borrowing base
- **Industry context**: Sector-specific risk factors (e.g., perishability, fashion risk, commodity price exposure) that affect advance rates
- **Field exam reports**: Most recent field exam or collateral audit findings, including any identified discrepancies

## Workflow

1. **Profile the borrower and collateral pool**
   - Classify collateral types: eligible AR, eligible inventory (by sub-category), equipment, real estate, other
   - Identify revenue concentration risks — flag any single obligor exceeding 10–15% of total AR
   - Assess inventory composition and turnover; distinguish between readily liquidatable finished goods and slow-moving or specialized WIP

2. **Set eligibility criteria**
   - Define AR eligibility: exclude past-due beyond 60–90 days [VERIFY against lender policy], cross-aged accounts (typically >50% past due triggers full exclusion), foreign receivables without credit insurance, affiliate/intercompany receivables, contra accounts, and government receivables subject to assignment restrictions
   - Define inventory eligibility: exclude consignment goods, bill-and-hold, in-transit beyond a threshold, obsolete or slow-moving stock (>12 months aged), and categories with no NOLV appraisal
   - Document any borrower-specific carve-outs or negotiated exceptions

3. **Calculate the borrowing base**
   - Apply advance rates to each eligible collateral class:
     - Eligible AR: typically 80–85% [VERIFY — varies by industry and credit quality]
     - Eligible inventory (finished goods at NOLV): typically 50–70% of appraised NOLV
     - Eligible inventory (raw materials): typically 40–60% of cost
     - Equipment/RE (if included): per appraisal, usually at forced liquidation value
   - Subtract reserves: dilution reserve (formula-based on trailing dilution %), rent reserve (3 months of landlord exposure if no SNDA), availability block or minimum excess availability requirement, and any springing reserves tied to financial covenants
   - Compute gross availability, net availability, and excess availability after outstanding loans and letters of credit

4. **Structure facility terms**
   - Size the commitment relative to peak and trough borrowing base projections (seasonal modeling)
   - Set financial covenants: springing fixed charge coverage ratio (typically 1.0x–1.1x, triggered when excess availability falls below a defined threshold, often the greater of a fixed dollar amount or 10–12.5% of the line cap) [VERIFY threshold conventions with lender]
   - Define reporting requirements: monthly borrowing base certificates, quarterly financials, annual audited financials, and periodic collateral reporting
   - Establish field exam frequency: typically 1–2x per year under normal conditions; accelerated to quarterly if a triggering event occurs (e.g., excess availability falls below threshold)

5. **Stress-test and scenario analysis**
   - Model borrowing base under downside scenarios: AR collection slowdown (+15–30 days DSO), inventory write-downs (10–20% NOLV decline), customer concentration loss, dilution spike
   - Assess whether the facility remains adequately available under stress — minimum excess availability should cover at least 60–90 days of operating cash burn
   - Identify structural mitigants: blocked-account arrangements (springing vs. hard), cash dominion triggers, and LC sub-facility sizing

## Output

- **Borrowing Base Model**: Spreadsheet-ready calculation showing eligible collateral by category, advance rates applied, reserves deducted, and resulting availability
- **Eligibility Criteria Summary**: Clear table of inclusion/exclusion rules for each collateral class with rationale
- **Facility Term Sheet Markup**: Key commercial terms including commitment size, advance rates, reserves, covenants, reporting, and field exam requirements
- **Scenario Analysis**: Sensitivity tables showing availability under base, downside, and severe stress cases
- **Risk Flags**: Highlighted concentration risks, unusual dilution patterns, inventory quality concerns, or structural gaps requiring lender negotiation

## Quality Checks

- Confirm advance rates and eligibility criteria are consistent with current market conventions for the borrower's industry [VERIFY against recent comparable ABL transactions]
- Validate that the borrowing base arithmetic ties — gross eligible collateral minus ineligibles, times advance rate, minus reserves equals net availability
- Ensure dilution reserve formula is internally consistent with trailing dilution data provided
- Cross-check that springing covenant thresholds and cash dominion triggers are aligned (they should reference the same or coordinated availability thresholds)
- Verify that field exam frequency and reporting cadence match the risk profile — higher-risk or seasonal borrowers warrant more frequent monitoring
- Confirm all [VERIFY] items are flagged for lender counsel or credit committee review before final structuring

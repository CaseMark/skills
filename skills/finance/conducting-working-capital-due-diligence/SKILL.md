---
name: conducting-working-capital-due-diligence
description: Analyzes target company working capital for M&A with normalization, peg calculation, and adjustment mechanics. Use when analyzing WC for transactions, calculating WC pegs, or structuring WC adjustment mechanisms.
tags:
  - process
  - corporate-finance
metadata:
  author: casemark
  practice_areas:
    - Corporate Finance
    - Treasury
    - Financial Planning
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Working Capital Due Diligence

## When To Use

- Buyer or seller side in an M&A transaction needs to establish a working capital peg for the purchase agreement
- Evaluating whether a target's reported working capital reflects normalized, sustainable operating levels
- Structuring the post-closing true-up mechanism (adjustment collar, escrow, dispute resolution)
- Assessing seasonal or cyclical distortions in current assets/liabilities before signing

## Inputs To Gather

- **Trial balance and general ledger detail** for the trailing 12–24 months (monthly granularity)
- **Balance sheet** at each month-end for the reference period, with sub-account breakouts for receivables, inventory, payables, accrued liabilities, and prepaid expenses
- **Revenue and COGS schedules** to correlate WC swings with business activity
- **Accounts receivable aging reports** and bad debt reserve history
- **Inventory valuation methodology** (FIFO, LIFO, weighted average) and obsolescence/slow-moving reserve schedules
- **Accounts payable aging** and any stretched-payment or early-pay discount programs
- **Accrued liabilities detail** — bonus accruals, warranty reserves, customer deposits, deferred revenue
- **Intercompany balances** and management fee allocations
- **Draft or executed purchase agreement** — specifically the WC definitions, excluded items, and adjustment mechanics sections
- **Quality of earnings (QoE) report**, if available, for cross-reference on normalizing adjustments

## Workflow

### 1. Define the Working Capital Framework

- Identify which balance sheet line items are included/excluded per the purchase agreement definition (e.g., cash and debt are almost always excluded; tax assets/liabilities may be carved out)
- Confirm whether the definition uses net working capital (current assets minus current liabilities) or a customized subset
- Map each GL account to an included or excluded category; flag ambiguous accounts for negotiation [VERIFY against draft SPA language]

### 2. Build the Monthly Bridge

- Populate a 12–24 month monthly working capital schedule using the defined components
- Calculate month-end NWC for each period; compute the trailing 12-month average, median, and identify outlier months
- Chart NWC alongside revenue to visualize seasonality and operating leverage effects

### 3. Normalize Working Capital

Apply adjustments for items that distort run-rate WC levels:

- **Non-recurring items** — one-time inventory write-downs, litigation accruals, restructuring reserves
- **Timing distortions** — quarter-end channel stuffing, delayed vendor payments, accelerated collections before close
- **Policy changes** — shifts in revenue recognition, changes to reserve methodology mid-period
- **Related-party / intercompany items** — management fees, shared-services allocations that will not continue post-close
- **Transaction-related accruals** — deal bonuses, advisor fees, change-of-control payments

Document each adjustment with a clear rationale and dollar impact. Mark any adjustment relying on management representations with [VERIFY].

### 4. Calculate the Working Capital Peg

- Compute the normalized average (typically trailing 12 months) after all adjustments
- Sensitivity-test the peg by excluding high/low months or using a shorter reference period
- Compare the peg to the estimated closing date balance sheet to quantify the expected true-up direction and magnitude
- If the target has strong seasonality, consider whether a fixed peg or a seasonally adjusted peg is more appropriate [VERIFY with deal team preference]

### 5. Structure the Adjustment Mechanism

- **Collar / de minimis threshold** — recommend a collar (e.g., +/- $X around the peg) within which no adjustment is made; size the collar relative to NWC volatility
- **Escrow / holdback** — estimate the appropriate escrow amount based on the magnitude of potential shortfall
- **Dispute resolution** — confirm the SPA specifies an independent accounting firm, timeline for objection notices (typically 30–60 days post-closing), and which accounting standards govern the closing balance sheet
- **Permitted leakage** — in locked-box deals, identify permitted leakage categories and verify they do not erode the WC position

### 6. Identify Risk Areas and Open Items

- Flag accounts with high subjectivity (e.g., warranty reserves, percentage-of-completion accruals, inventory obsolescence)
- Note any data gaps — missing months, unreconciled intercompany balances, lack of sub-ledger detail
- Highlight management estimates that could swing the peg by more than 5%

## Output

- **Working Capital Summary Table** — monthly NWC for the reference period, with each normalizing adjustment shown as a separate line, arriving at the normalized peg
- **Peg Recommendation** — stated dollar amount with sensitivity range and rationale for the reference period chosen
- **Adjustment Narrative** — description of each normalization adjustment, dollar impact, and supporting evidence
- **Risk and Open Items Log** — list of unresolved data issues, subjective estimates, and items requiring further negotiation
- **Mechanism Recommendations** — proposed collar size, escrow amount, and key SPA provisions to negotiate

## Quality Checks

- Normalized NWC peg reconciles back to the unadjusted monthly schedule (adjustments net correctly)
- No double-counting between WC adjustments and net debt / transaction expense adjustments in the purchase price bridge
- Peg reference period is consistent with the period used in the QoE report (if one exists)
- Each normalization adjustment has a documented source (GL entry, management memo, or third-party confirmation)
- Seasonal patterns are acknowledged — if the closing date falls in a peak/trough month, the estimated closing NWC reflects that reality
- SPA WC definition and the analysis framework use identical account inclusion/exclusion [VERIFY SPA exhibit against model mapping]

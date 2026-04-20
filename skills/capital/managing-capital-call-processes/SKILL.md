---
name: managing-capital-call-processes
language: en
description: Structures capital call execution with notice preparation, pro-rata allocation, default remedy provisions, and wire coordination. Use when processing capital calls, calculating LP contributions, or managing call logistics.
tags:
  - management
  - investor-relations-and-lp-reporting
metadata:
  author: casemark
  practice_areas:
    - Investor Relations
    - LP Reporting
    - Fund Administration
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Capital Call Processes

Structures capital call execution with notice preparation, pro-rata allocation, default remedy provisions, and wire coordination.

## When To Use

- Processing a drawdown against LP unfunded commitments for investments, expenses, or management fees
- Calculating each LP's pro-rata share across multiple commitment tranches or series
- Preparing formal capital call notices compliant with LPA notice periods and delivery requirements
- Coordinating wire instructions, funding deadlines, and reconciliation across the investor base
- Evaluating or enforcing default remedy provisions when an LP fails to fund

## Inputs To Gather

- **LPA / Side Letter Terms**: Notice period (typically 10–15 business days [VERIFY per fund]), call frequency limits, excuse/exclusion rights, default penalty provisions, GP clawback interaction
- **Commitment Schedule**: Each LP's total commitment, funded-to-date, remaining unfunded commitment, and any commitment reductions from excuse rights or secondary transfers
- **Call Purpose & Amount**: Aggregate amount needed, breakdown by use (investment acquisition, follow-on, fees, expenses, organizational costs), and whether the call is a true drawdown vs. a recycling/recall
- **Wire & Banking Details**: Fund's bank account, LP-specific wire instructions on file, currency requirements, intermediary bank details for non-USD LPs
- **Prior Call History**: Sequence number, amounts previously called, any outstanding defaults or partial payments, recycled/returned capital amounts

## Workflow

1. **Determine Call Amount & Purpose**
   - Confirm the aggregate capital needed with the investment team or CFO
   - Classify the call: investment drawdown, management fee, fund expense, or organizational cost
   - Check whether recycled capital or fund-level credit facility proceeds reduce the call amount

2. **Calculate Pro-Rata Allocations**
   - Pull each LP's unfunded commitment from the fund accounting system
   - Compute each LP's share: `LP Call Amount = Aggregate Call × (LP Unfunded / Total Unfunded)`
   - Adjust for excuse/exclusion rights — if any LP is excused from a specific investment, reallocate their share pro-rata among participating LPs
   - Adjust for side-letter fee discounts on management fee calls (reduced rate × commitment basis)
   - Validate that individual LP call amounts sum exactly to the aggregate call (reconcile rounding)

3. **Prepare Capital Call Notice**
   - Draft notice including: call number, call date, due date, aggregate amount, LP-specific amount, purpose description, wire instructions, and contact for questions
   - Reference the specific LPA section authorizing the call [VERIFY section number per fund]
   - Confirm the notice period meets LPA requirements (count business days, exclude holidays per governing law jurisdiction) [VERIFY]
   - Attach or reference the call calculation schedule showing each LP's allocation

4. **Distribute Notices & Coordinate Wires**
   - Send notices via the delivery method specified in the LPA (email, portal upload, registered mail) [VERIFY per LP]
   - Log delivery timestamps — these start the funding clock
   - Confirm wire instructions are current for each LP; flag any LP with stale or missing banking details for immediate outreach
   - Set internal tracking milestones: T-5 business days (reminder), T-2 (escalation for non-confirmation), T-0 (due date)

5. **Receive, Reconcile & Confirm Funds**
   - Monitor the fund's bank account for incoming wires daily as the due date approaches
   - Match each wire to the correct LP — verify amount, reference codes, and originating bank
   - Issue funding confirmations to each LP upon receipt
   - Reconcile total received against total called; investigate discrepancies (partial payments, overpayments, FX differences)

6. **Handle Defaults & Shortfalls**
   - If an LP fails to fund by the due date, issue a formal default notice per LPA terms [VERIFY cure period — commonly 5–10 business days]
   - Calculate default interest (typically LIBOR/SOFR + 200–500 bps on the unpaid amount) [VERIFY rate per LPA]
   - Evaluate available remedies: forced sale of LP interest at discount, forfeiture of a percentage of funded capital, loss of voting/advisory committee rights, GP right to call remaining unfunded commitment in full
   - If shortfall impacts the investment closing, determine whether GP bridge financing or over-call to non-defaulting LPs is needed
   - Document all default actions and maintain a remedies log for LPAC review

## Output

- **Capital Call Notice** (per LP): Formal notice with call number, due date, LP-specific amount, purpose, and wire instructions
- **Allocation Schedule**: Spreadsheet or table showing each LP's commitment, unfunded balance, pro-rata percentage, excuse adjustments, and called amount
- **Reconciliation Report**: Post-funding summary matching wires received to amounts called, with variance explanations
- **Default Tracking Log** (if applicable): LP name, amount in default, cure deadline, interest accruing, remedy status

## Quality Checks

- All LP call amounts sum to the aggregate call with no rounding discrepancy exceeding $1
- Notice period calculation is correct under the applicable LPA (business days, holiday calendar) [VERIFY]
- Excuse/exclusion adjustments are applied only where side letters or LPA provisions explicitly permit
- Wire instructions match the most recently confirmed banking details for each LP
- Default interest rate and cure period match the specific LPA — do not assume a standard; each fund varies [VERIFY]
- Confirm that the call does not exceed any single LP's remaining unfunded commitment
- Verify that aggregate calls to date plus this call do not exceed total fund commitments

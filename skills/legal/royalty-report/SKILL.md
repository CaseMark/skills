---
name: royalty-report
description: Drafts auditable Royalty Report Forms for IP licensing agreements, extracting party names, royalty rates, deduction categories, and reporting specs from the governing license. Calculates tiered royalties, minimum guarantees, advance recoupments, and produces a certification-ready compliance document. Use when preparing licensee royalty reports, royalty payment calculations, license compliance filings, or periodic royalty submissions.
tags:
  - agreement
  - drafting
  - transactional
---

# Royalty Report Form

Drafts an execution-ready royalty report that satisfies licensee reporting obligations under an IP license agreement, functioning as both an accounting instrument and a legally binding compliance document.

## Prerequisites

1. **Governing license agreement** — including amendments; extract exact legal entity names from signature blocks, royalty rates, calculation methodology, allowable deductions, reporting frequency, and submission requirements
2. **Sales data** — product-level transactions for the reporting period (or confirm template-only output)
3. **Prior reports** (if applicable) — for advance recoupment balances, cumulative tier thresholds

If multiple license agreements exist in uploaded documents, ask which governs before proceeding.

## Key Extraction from License Agreement

Extract and note before drafting:

| Field | Source |
|---|---|
| Licensor legal name | Signature block (exact match required) |
| Licensee legal name | Signature block (exact match required) |
| Agreement date + amendments | Preamble / amendment headers |
| Reporting period / frequency | Reporting provisions |
| Royalty rate(s) | Royalty calculation section |
| Tiered rate thresholds | Royalty calculation section |
| Minimum royalty guarantee | Payment terms |
| Allowable deductions | Definitions / calculation provisions |
| Advance recoupment terms | Payment terms |
| Required accounting standard | Reporting provisions (GAAP or other) |
| Submission format / method | Reporting provisions |
| Confidentiality marking | Confidentiality section |
| Concurrent payment required? | Payment terms |
| Audit period | Audit rights section |

## Output Structure

### 1. Document Header

```
                        ROYALTY REPORT

[Licensee Legal Name — exact match to agreement]

For the [Quarter/Period] Ending [Date] / From [Start Date] through [End Date]

Pursuant to License Agreement dated [Date] between [Licensor Legal Name]
and [Licensee Legal Name] [, as amended by Amendment No. [X] dated [Date]]

Report No.: [If required by agreement]
Reference No.: [If applicable]
```

### 2. Sales Data Table

| Product SKU | Product Description | Qty Sold | Unit Price | Gross Sales |
|---|---|---:|---:|---:|
| [SKU] | [Must match licensed product definitions] | [X] | $[X.XX] | $[X.XX] |

- Organize by product line, territory, or license type if different rates apply
- Include subtotals per category before grand total
- Currency per agreement; right-align all numerical columns
- If no sales data provided, generate template with sample entries and note: **"[INSERT ACTUAL SALES DATA FROM ACCOUNTING RECORDS]"**

### 3. Royalty Calculation

Present as sequential line items:

```
Total Gross Sales                                    $[________]

Less Allowable Deductions:
  Returns & allowances                              ($[________])
  Freight & shipping (third-party)                  ($[________])
  Sales taxes & governmental charges                ($[________])
  Trade discounts                                   ($[________])
  [Other per agreement]                             ($[________])
Total Deductions                                    ($[________])

Net Sales Subject to Royalty                         $[________]

Royalty Calculation:
  [Rate]% on first $[threshold]                      $[________]
  [Rate]% on excess over $[threshold]                $[________]
Calculated Royalty                                   $[________]

Minimum Royalty Guarantee (if applicable)             $[________]
Royalty Due (greater of calculated or minimum)        $[________]

Less: Advance Recoupment                            ($[________])
Plus: Marketing Fund Contribution ([X]%)              $[________]
Plus: [Other fees per agreement]                      $[________]

TOTAL AMOUNT DUE                                     $[________]
```

- Show each deduction category separately (never aggregate)
- For tiered rates, show each tier calculation independently
- If advances recouped, show royalty earned and recoupment as separate line items

### 4. Certification & Signature Block

Draft certification incorporating:

- [ ] Signer is duly authorized officer with authority to bind licensee
- [ ] Report prepared in strict accordance with the license agreement
- [ ] All information true, complete, and accurate after reasonable inquiry
- [ ] Data derived from books and records maintained per [GAAP / agreement-specified standard]
- [ ] Payment represents full amount owed; nothing withheld except as permitted

> If the agreement prescribes specific certification language, incorporate it **verbatim**.

```
CERTIFICATION

The undersigned, a duly authorized officer of [Licensee], hereby certifies
that this Royalty Report has been prepared in accordance with the License
Agreement dated [Date], that all information is true, complete, and accurate
to the best of the undersigned's knowledge and belief after reasonable inquiry,
and that the sales data and calculations are derived from books and records
maintained in the ordinary course of business in accordance with [GAAP/specified standard].

Signature: ___________________________
Name:      ___________________________
Title:     ___________________________
Date:      ___________________________
Email:     ___________________________
Phone:     ___________________________
```

### 5. Payment Instructions (if concurrent payment required)

Include: amount due, payment method, payee name (exact per agreement), wire transfer details or mailing address, payment due date.

## Formatting Requirements

- Standard letter-size, 1-inch margins
- Professional font (Times New Roman, Arial, or Calibri), 11-12pt body
- Page numbers: "Page X of Y" in footer
- Confidentiality footer per agreement (e.g., "Confidential and Proprietary")
- PDF output if agreement requires it

## Guidelines

- **Entity name precision** — any variance from signature block names may invalidate submission
- **Deductions** — include only those explicitly authorized by the agreement; when uncertain, use `[VERIFY DEDUCTION ELIGIBILITY UNDER SECTION [X]]`
- **Audit exposure** — every figure must reconcile to source documents (invoices, credit memos, ledger entries); reports are typically auditable for 2-3 years
- **Missing information** — use bracketed placeholders referencing the specific agreement section: `[INSERT ROYALTY RATE FROM SECTION 4.2]`
- **Supporting documents** — check whether agreement requires attachments (detailed invoices, territory breakdowns, accountant certifications above thresholds)
- **Tiered calculations** — if cumulative annual thresholds apply, account for sales reported in prior periods of the same contract year
- **Material misrepresentation** — report creates contractual representations that may trigger breach, fraud claims, or termination rights; emphasize accuracy over speed

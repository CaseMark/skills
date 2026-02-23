---
name: final-tax-return-corporate
description: Drafts and analyzes final U.S. tax return filings for dissolving corporate entities, including C-corps (Form 1120), S-corps, and partnerships (Form 1065). Enforces IRS compliance for short-year partial-period reporting, proration of deductions and credits, liquidating distribution gain recognition, Schedule K-1 issuance, and dissolution-period deadline rules. Use when preparing a final return for a dissolving corporation, winding-up entity, or corporate liquidation closing.
tags:
  - analysis
  - corporate
  - drafting
  - regulatory
---

# Corporate Final Tax Return Filing

Prepares IRS-compliant final tax returns for dissolving corporate entities covering the partial tax year from January 1 through the date of dissolution.

## Prerequisites

1. **Dissolution documents** — articles of dissolution, board/shareholder resolutions authorizing liquidation, state dissolution filing confirmation
2. **Final financial statements** — balance sheet, P&L, and trial balance through dissolution date
3. **Income records** — all Forms W-2, 1099, K-1, brokerage statements, and business ledgers for the period
4. **Asset disposition records** — sale proceeds, adjusted basis, and date of each asset disposition
5. **Liquidating distribution records** — amounts distributed, recipients, and characterization
6. **Prior-year returns** — to confirm accounting method, depreciation schedules, and carryforwards
7. **EIN and registered address** confirmed against IRS records

## Output Structure

### 1. Final Return Designation

| Form | Action Required |
|---|---|
| Form 1120 (C-corp) | Check "Final return" box; write **FINAL RETURN** across top of page 1 |
| Form 1120-S (S-corp) | Check "Final return" box; complete Schedule K and all K-1s |
| Form 1065 (Partnership) | Check "Final return" box; complete Schedule K and all K-1s |

- Taxpayer name must match EIN registration exactly
- Include name, title, and contact of liquidating trustee or authorized officer in signature block

---

### 2. Filing Deadlines (Short-Year Returns)

| Entity Type | Deadline |
|---|---|
| C-corporation (Form 1120) | 15th day of the **4th month** after dissolution date (for tax years beginning after 12/31/2017) |
| S-corporation (Form 1120-S) | 15th day of the **3rd month** after the short tax year ends |
| Partnership (Form 1065) | 15th day of the **3rd month** after the short tax year ends |

- Extensions: File Form 7004 before original due date (6-month extension available)
- Short-year return period: January 1 → dissolution date; do **not** annualize income unless required by the applicable method

---

### 3. Income Reporting Checklist

- [ ] All Forms 1099, W-2, and K-1 received and reconciled to ledger
- [ ] Gross receipts and sales through dissolution date only
- [ ] Gains/losses from asset dispositions — each transaction on Form 4797 (ordinary) or Schedule D (capital)
- [ ] Liquidating distributions: calculate gain or loss per IRC § 331/336 [VERIFY specific subsection applicability]
- [ ] Step-up (or step-down) in basis on distributed assets per IRC § 334 [VERIFY]
- [ ] No post-dissolution income included in this return

---

### 4. Deductions & Credits

**Do not prorate:**
- Standard deductions where applicable

**Do prorate or limit:**
- Depreciation: computed only through dissolution date; use actual days in service
- Business expenses: deductible only if incurred before dissolution
- Dissolution-related expenses (legal fees, accounting fees, asset liquidation costs): deduct as ordinary business expenses if incurred in the course of winding up

**Dissolution-specific items:**
- NOL carryforwards: apply any available NOL to final-year income; unused NOLs expire on dissolution
- Credits: compute only for the covered partial-year period; confirm no carryforward is available to a successor

---

### 5. Required Schedules & Attachments

| Schedule/Form | Required When |
|---|---|
| Schedule D | Any capital asset disposition |
| Form 4797 | Sale of business property / depreciable assets |
| Schedule K-1 (per partner/shareholder) | All S-corps and partnerships |
| Form 1099-DIV / 1099-B | Liquidating distributions to shareholders |
| Supporting statement | Explanation of any unusual item or uncertain position |
| Form 8275 | Disclosure of positions lacking substantial authority |

**Schedule K-1 requirements (S-corps/partnerships):**
- Issue to each partner/shareholder showing final-year distributive share of income, deductions, credits, and liquidating distribution amounts
- Must reconcile to entity-level totals
- Furnish to recipients by the return due date so they can report on personal returns

---

### 6. Payments, Refunds & Estimated Tax Credits

- [ ] All estimated tax payments credited with date and amount
- [ ] Withholding from Forms 1099/W-2 reconciled
- [ ] Refund directed to estate/liquidating account; confirm routing/account number
- [ ] If tax owed: calculate any penalty under IRC § 6655 for underpayment of estimated tax [VERIFY applicability to short-year]

---

### 7. Quality Control

- [ ] All math recomputed line-by-line; amounts flow correctly from schedules to main form
- [ ] No income or expense from after dissolution date included
- [ ] "Final return" box checked on all applicable forms
- [ ] K-1s issued and reconciled to Schedule K totals
- [ ] Supporting statements attached for any item likely to draw IRS scrutiny
- [ ] Signature block completed with liquidating trustee/officer name, title, and date

## Guidelines

- **Short-year proration**: Apply proration only where the Code or regulations explicitly require it; do not prorate items (e.g., standard deduction) that the IRS does not prorate
- **Liquidating distributions**: Gain or loss to the distributing corporation on property distributed in liquidation is generally recognized under IRC § 336; gain or loss to shareholders under IRC § 331 [VERIFY exceptions for subsidiary liquidations under § 332]
- **State returns**: A final federal return does not satisfy state filing obligations — identify all states where the entity had nexus and file separate state final returns; some states require a tax clearance certificate before dissolution is effective
- **Records retention**: Retain complete copy of filed return, all supporting documents, and proof of filing for minimum 3 years from filing date; retain longer if the return involves NOL carrybacks, asset basis issues, or open estate administration
- **Uncertain positions**: Flag any issue involving valuation, multi-state apportionment, or novel tax treatment with `[NEEDS TAX COUNSEL REVIEW]` and attach Form 8275 where disclosure is warranted
- **Jurisdiction**: US federal rules govern this skill; state and local tax treatment may differ materially

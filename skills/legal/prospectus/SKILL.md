---
name: prospectus
description: Drafts SEC-compliant prospectuses for U.S. corporate securities offerings (IPOs, follow-ons, private placements). Structures all required disclosure sections—cover page, risk factors, use of proceeds, business description, MD&A, management bios, financial statements, and offering terms—against uploaded company documents, financial data, and EDGAR comparables. Use when preparing a Form S-1, S-11, offering circular, or any primary disclosure document for a public or private securities issuance.
tags:
  - analysis
  - corporate
  - drafting
  - regulatory
  - research
---

# Securities Prospectus

Drafts a complete, SEC-compliant prospectus integrating uploaded company materials with current EDGAR standards and applicable disclosure rules.

## Prerequisites

1. **Corporate formation docs** — certificate of incorporation, bylaws, capitalization table
2. **Financial statements** — audited annuals + unaudited interim (GAAP); any projections or non-GAAP metrics
3. **Offering terms** — term sheet, underwriting agreement, or draft pricing supplement
4. **Management profiles** — bios, compensation schedules, director independence determinations
5. **Legal/regulatory file** — pending litigation, regulatory orders, IP assignments, material contracts
6. **Business plan or investor deck** — for operations narrative and growth strategy

## Output Structure

### 1. Cover Page
| Element | Requirement |
|---|---|
| Issuer name | Full legal name as registered |
| Securities offered | Type, quantity, par value |
| Offering price | Fixed price or range; "subject to change" if preliminary |
| Proceeds to issuer | Net of underwriting discounts |
| SEC legends | Rule 424 / preliminary prospectus disclaimers |
| Risk warning | "See 'Risk Factors' beginning on page X" |

### 2. Prospectus Summary
- Company overview (3–5 sentences), core value proposition
- Offering snapshot: security type, aggregate amount, use of proceeds (high-level)
- No stand-alone statements — every claim cross-referenced to a detailed section

### 3. Risk Factors
Organize in this sequence:
1. **Offering-specific risks** (dilution, no established market, lock-up expiration)
2. **Business & operational risks** (company-specific; no generic boilerplate)
3. **Industry & regulatory risks** (sector-specific; cite applicable statutes/rules)
4. **Macro & market risks** (interest rate, liquidity, economic conditions)

Each risk: named header → specific harm → magnitude where quantifiable. Avoid generic language that SEC comment letters flag.

### 4. Use of Proceeds
```
Total gross proceeds:          $___
Underwriting discounts/fees:   ($___)
Estimated offering expenses:   ($___)
Net proceeds to issuer:        $___

Allocation:
  [Category]                   $___  (___%)  [Timeframe]
  [Category]                   $___  (___%)  [Timeframe]
  General corporate purposes   Remainder
```
Disclose assumptions; note if management retains reallocation discretion.

### 5. Business Description
- History, formation date, jurisdiction, key milestones
- Products/services, revenue model, pricing structure
- Target markets, customer concentration, distribution channels
- Competitive landscape; basis of competition
- Intellectual property (patents, trademarks, licenses)
- Regulatory environment and material compliance obligations
- Supply chain dependencies and key supplier/customer relationships

### 6. Management & Governance
- **Officers & Directors table**: Name | Title | Age | Since
- Individual bios: relevant experience, prior positions, education
- Compensation summary: base, bonus, equity grants, deferred compensation
- Board composition: independence determinations, committee memberships
- Related-party transactions: Item 404 of Reg S-K threshold ($120K) [VERIFY current threshold]
- Beneficial ownership table: 5%+ holders + all directors/officers as a group

### 7. Financial Information
- Present audited financial statements per Reg S-X (balance sheet, income statement, cash flows, equity)
- Interim unaudited financials if within reporting window
- Non-GAAP measures: label clearly, reconcile to nearest GAAP equivalent, explain why used
- MD&A: results of operations, liquidity, capital resources, known trends, critical accounting estimates
- Forward-looking statements: include safe harbor language under PSLRA [VERIFY applicability to offering type]

### 8. Legal Proceedings
- All material litigation, arbitration, regulatory investigations
- Per proceeding: parties, claims, forum, status, management's exposure estimate
- Threshold: proceedings where loss is reasonably possible and material (ASC 450 standard)

### 9. Offering Terms
| Term | Detail |
|---|---|
| Security type | Common stock / preferred / notes / warrants |
| Shares offered | Primary + secondary (if any) |
| Price / mechanism | Fixed, bookbuild, Dutch auction |
| Underwriting structure | Firm commitment / best efforts; over-allotment option |
| Lock-up period | Duration; covered persons |
| Registration rights | Demand, piggyback, S-3 shelf |
| Dilution | Net tangible book value per share before/after offering |
| Transfer restrictions | Rule 144 / Securities Act legend |

### 10. Signatures & Certifications
- CEO and CFO SOX §302 and §906 certifications (if Exchange Act registrant) [VERIFY applicability]
- Board signature block: majority of directors required for S-1
- Principal accounting officer sign-off

### 11. Table of Contents & Exhibits
- Full TOC with page references
- Exhibit index per Item 601 of Reg S-K (material contracts, legal opinion, consent of independent auditor)

## Guidelines

- **Materiality standard**: TSC Industries v. Northway — substantial likelihood a reasonable investor would consider the information important [VERIFY cite]
- **Plain English Rule** (Rule 421(d)): active voice, short sentences, no defined-term overload in cover/summary/risk factors
- **No selective disclosure**: information in the prospectus must be consistent with any contemporaneous roadshow materials
- **Preliminary vs. final**: mark all unpriced terms clearly; final prospectus must be filed within Rule 424 timeframes
- **Emerging Growth Company (EGC)**: if applicable, note JOBS Act accommodations (reduced financial periods, executive comp disclosure) [VERIFY current EGC thresholds]
- **Jurisdiction**: US federal securities law governs; note any state blue-sky compliance obligations
- **Flag gaps**: if uploaded materials are insufficient to complete a section, insert `[INFORMATION NEEDED: ___]` rather than speculating

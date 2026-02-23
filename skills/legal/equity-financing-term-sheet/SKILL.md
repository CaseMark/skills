---
name: equity-financing-term-sheet
description: >-
  Produces a U.S. equity-financing term sheet for venture/private equity
  rounds that converts available deal facts into a negotiation-ready,
  investor-grade draft. Use when counsel or founders need a structured
  framework for pricing, capitalization math, liquidation and anti-dilution
  mechanics, investor protections, governance, transfer and registration
  rights, and closing/legal-effect clauses. Trigger keywords: term sheet,
  equity financing, venture capital, series preferred stock, pre-money
  valuation, liquidation preference, conversion ratio, pro rata, ROFR,
  co-sale, registration rights, exclusivity.
tags:
  - agreement
  - corporate
  - drafting
---

# Equity Financing Term Sheet

Draft a complete US venture equity term sheet with minimal placeholders and explicit consistency controls for follow-on definitive agreements.

## Prerequisites

1. Legal identity of company and jurisdiction of incorporation.
2. Existing charter, bylaws, investor approvals, and any prior financing agreements.
3. Round metadata: series name, proposed investor list, lead investor, amount raised, and valuation inputs.
4. Pre-financing capitalization data (common, preferred, options, warrants, converts, reserved shares).
5. Governance baseline: current board size, nominee rights, voting structure.
6. Financing documents and diligence materials to reduce placeholder usage.
7. Clear allocation of deal roles and mandatory parties.
8. Jurisdiction and law-selection preferences for governing law and dispute resolution.
9. Confidentiality and securities-regulatory constraints from counsel.
10. Pre-set commercial boundaries for negotiation (e.g., cap on liquid preference, anti-dilution type, board control).

## Output Structure / Process

1. Intake validation
- Build a data-completion map and mark missing fields with explicit placeholders.

| Required Input | Purpose | Output Action |
|---|---|---|
| Company/Jurisdiction | Header, governing law alignment | Populate exact legal names and entity state |
| Economic Inputs | Valuation, share price, pre/post ownership | Compute formulas, flag any placeholders |
| Cap Table | Dilution impact and conversion basis | Generate pre/post capitalization summary |
| Rights Matrix | Board/information/protection terms | Insert into protection and governance sections |
| Closing Preconditions | Legal and transaction sequencing | Build definitive-docs and “conditions precedent” list |
| Regulatory/Securities Constraints | Registration and confidentiality language | Add jurisdiction-aware caveats and flags |

2. Draft with hard section order
- Intro and nature of document.
- Definitions and key terms.
- Economics and capitalization mechanics.
- Preferred stock rights (dividends, liquidation, conversion, anti-dilution).
- Governance and voting protections.
- Investor rights and access.
- Registration, transfer, liquidity rights.
- Closing mechanics and legal effect.
- Signature block.

3. Validation pass
- Verify defined-term consistency.
- Verify all numeric variables resolve or explicitly placeholder-marked.
- Verify binding clause list is isolated.

## Core Clauses Checklist

| Category | Mandatory | Minimum Content |
|---|---|---|
| Deal Identity | Yes | Date, parties, round, amount, currency, pre-money basis |
| Economics | Yes | valuation inputs, conversion ratio, price per share formula |
| Economic Preferences | Yes | dividends, liquidation preference, conversion trigger, anti-dilution |
| Governance | Yes | board allocation, observer terms, protective provisions |
| Investor Rights | Yes | information, inspection, registration demand/piggyback |
| Liquidity Controls | Yes | ROFR, co-sale, pro-rata, exceptions |
| Closing | Yes | diligence standards, required agreements, conditions, timeline |
| Enforceability | Yes | binding clause carve-out, non-binding statement, survival and law |

## Required Templates

```text
NON-BINDING TERM SHEET (unless section marked binding)
Company:
Date:
Lead Investor:
Proposed Round:
Proposed Capital Raise:
Proposed Valuation:
```

```text
Definitions (insert first):
“Binding Provisions”, “Major Investor”, “Fully Diluted Capitalization”, “Registrable Securities”, “Qualified IPO”
```

```text
Preferred Stock Economics:
- Security Type:
- Original Issue Price:
- Pre-Money Fully Diluted Basis:
- Post-Money Fully Diluted Basis:
- Liquidation Preference:
- Dividend Terms:
- Conversion:
- Anti-Dilution Method:
```

## Calculation Standards

```text
Price Per Share = Pre-Money Valuation / Pre-Money Fully Diluted Shares
Ownership % (post-close) = (Founder/Common + New Investor Conversion Equivalents) / Total Post-Financing FD Shares
```

```text
Preferred Liquidation Preference:
- Non-participating: greater of preference or conversion value
- Participating: preference plus pro-rata on residuals (include cap if any)
```

```text
Anti-dilution (weighted average):
Adjusted Conversion Price = Old Conversion Price × (A + B) / (A + C)
Where A = basic FD shares on full basis (or narrow basis if negotiated)
B = consideration / old conversion price
C = new shares issued at lower price
```

## Document Assembly Rules

- Place binding clauses in a dedicated section: confidentiality, exclusivity, expense reimbursement, law and forum.
- Mark all unresolved fields as `{{PLACEHOLDER: field name}}`.
- Use exact thresholds in percentages and timeframes (e.g., 30-day, 45-day periods, percentage thresholds).
- Ensure each protection is referenced in both definition and operative clause.
- Include closing conditions and required definitive documents by name.
- Add a “Termination and survival” paragraph aligned to transaction stage.
- Add post-term-sheet risk log for all redline-heavy points: legal opinions, reps/warranties depth, closing timing, and financing mechanics.
- Attach exhibit placeholders for cap table and schedule of rights where required.

## Guidelines

### Do
1. Use available source documents first; keep placeholders only for unresolved business terms.
2. Distinguish with explicit headings what is binding vs non-binding.
3. Normalize terminology across table, clause text, and signature block.
4. Cross-reference every economic right to its effect on governance and transfer provisions.
5. Flag any securities-law dependency and add a legal-confirmation note before final output [VERIFY].
6. Include US-regulatory placeholders for IPO/readiness and resale restrictions with current-filing caveats [VERIFY].

### Don't
1. Do not mix broad-based and narrow-based anti-dilution results without branch language.
2. Do not present incomplete economics without explicit missing-field markers.
3. Do not lock valuation or ownership math in prose only; provide formulas.
4. Do not promise registration timing or filing outcomes without legal confirmation [VERIFY].

### Jurisdiction and Compliance Notes
1. Default document assumptions should be US-centric; do not imply non-US corporate law applies.
2. Verify governing law, federal securities implications, and any Rule 144 / resale language before release [VERIFY].
3. Ensure confidentiality survival terms are compatible with carve-outs required by law and transaction advisors.

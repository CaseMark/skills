---
name: charity-filing-thresholds
description: Researches state-specific charitable solicitation filing requirements keyed to gross revenue, producing a structured state-by-state compliance matrix of audit thresholds, financial-statement tiers, filing fees, and due dates with full citation documentation. Use when building charity compliance matrices, researching nonprofit filing thresholds, charitable solicitation registration renewals, or comparing state audit requirements for 501(c)(3) organizations.
tags:
  - analysis
  - checklist
  - corporate
  - memo
  - regulatory
  - research
---

# State Charity Filing Threshold Research

Produces a citation-backed, state-by-state compliance matrix of charitable solicitation filing requirements (audit/review/compilation thresholds, fees, deadlines) keyed to gross revenue.

## Prerequisites

1. **Jurisdictions in scope** — specific states, or default to all 41 registration states + DC
2. **Organization's gross revenue / total contributions** (per Form 990) — default: $1,000,000
3. **Fiscal year end date** — default: December 31
4. **Entity category** — public charity, private foundation, religious, educational (default: 501(c)(3) public charity)
5. **Desired output format** — memo, spreadsheet, CSV, JSON (default: full compliance package)

## Scope

- **In scope:** Charitable solicitation registration/renewal filings for 501(c)(3) organizations
- **Out of scope:** Corporate annual reports, IRS filings, professional fundraiser/solicitor/commercial co-venturer regimes (unless requested)

## Process

### Phase 1: Source Identification

For each state, locate and record:

| Field | Entry |
|---|---|
| Regulator / Agency | e.g., Attorney General Charities Bureau |
| Statute citation | Code + section |
| Regulation citation | Admin code title + section |
| Filing form(s) | Name/number + link |
| Instruction booklet | Link |
| Fee schedule page | Link |
| Due date authority | Statute/reg or instructions |
| Last verified (date) | YYYY-MM-DD |

**Search queries per state:**
- `[State] charitable solicitation renewal audit requirement gross revenue`
- `[State] financial statement review compilation threshold charitable organization`
- `[State] charitable organization annual report filing fee schedule`
- `[State] due date fiscal year end charitable solicitation extension`

**Primary-source-first rule:** Prefer statute/regulation text over FAQ summaries. Flag guidance-only sources.

### Phase 2: Data Extraction

Extract four rule categories per state using this template:

| Category | Field | Value | Citation | Quoted Language | Last Verified |
|---|---|---|---|---|---|
| **Audit** | Threshold (≥ or >) | | | | |
| **Audit** | Revenue basis term (verbatim) | | | | |
| **Audit** | Exemptions / alternatives | | | | |
| **Review** | Threshold | | | | |
| **Review** | Revenue basis term | | | | |
| **Compilation** | Threshold | | | | |
| **Compilation** | Acceptable below threshold? | Yes/No/Unclear | | | |
| **Fees** | Tier table | | | Full schedule | |
| **Fees** | Revenue basis term | | | | |
| **Due Date** | Rule | | | e.g., "4.5 months after FYE" | |
| **Due Date** | Extension available | Yes/No | | Length + mechanism | |

#### Critical: Revenue Definition Variance

States define the revenue trigger differently. Capture verbatim and map to Form 990:

| State Term | Typical 990 Line | Notes |
|---|---|---|
| "gross annual revenue" (CA) | Part VIII, Line 12 | Excludes certain gov. grants |
| "total revenue" (NY, GA, PA) | Part VIII, Line 12 | Broad measure |
| "contributions" (IL, FL) | Part VIII, Line 1h | Narrower — contributions only |
| "gross support and revenue" (MA) | Part VIII, Line 12 | Combined measure |

**Do not assume** "gross revenue" equals "contributions" — capture each state's term verbatim.

#### Extraction Rules

- If instructions conflict with statute/regulation, **prioritize statute** and note the conflict
- If a state uses IRS Form 990 line references, capture explicitly
- If multiple programs exist (trust reporting vs. solicitation), label which program the threshold applies to

### Phase 3: Normalization

Transform state-specific language into standardized fields:

| Normalized Field | Description |
|---|---|
| `state` | Two-letter abbreviation |
| `audit_threshold_amount` | USD with comparator (≥ or >) |
| `audit_threshold_basis_raw` | State's verbatim term |
| `audit_threshold_990_line` | Form 990 line reference |
| `review_threshold_amount` | USD range |
| `compilation_acceptable_below` | Yes/No/Unclear |
| `fee_schedule` | Tier list (amount : fee) |
| `due_date_rule_raw` | Verbatim rule |
| `due_months_after_fye` | Numeric (e.g., 4.5, 6) |
| `extension_available` | Yes/No |
| `extension_length` | Days or months |
| `extension_mechanism` | e.g., "Copy of IRS Form 8868" |
| `citations` | Statute/reg/instruction references |
| `last_verified_date` | YYYY-MM-DD |

Maintain a **decision log** for ambiguities:

| Issue | State | Sources | Decision | Follow-Up |
|---|---|---|---|---|
| Term not defined in statute | XX | Statute §…, Instructions | Treat as total revenue; flag | Confirm with agency |
| Instructions vs. statute conflict | YY | Statute §…, Form | Use statute; note conflict | Attorney review |

### Phase 4: Deliverables Assembly

#### Master Matrix

| State | Audit At | Revenue Basis | Review At | Compilation Below | Fee (summary) | Due Date | Extension | Primary Sources | Verified |
|---|---|---|---|---|---|---|---|---|---|
| CA | ≥ $2M | Gross annual revenue | N/A | $2M | $25–$300 tiered | 4.5 mo | Yes (8868) | Gov. Code §12586; RRF-1 [VERIFY] | YYYY-MM-DD |
| NY | ≥ $1M | Total revenue | $250K–$1M | $250K | $25–$750 tiered | 4.5 mo | Yes (180 days) | EPTL §8-1.4; CHAR500 [VERIFY] | YYYY-MM-DD |
| IL | ≥ $300K | Contributions | $25K–$300K | $25K | $15 flat | 6 mo | Yes (60 days) | 225 ILCS 460; AG-990-IL [VERIFY] | YYYY-MM-DD |
| FL | ≥ $1M | Contributions | $500K–$1M | $500K | $10–$400 tiered | 4.5 mo | No (strict) | Fla. Stat. §496; CH-1 [VERIFY] | YYYY-MM-DD |
| PA | ≥ $750K | Total revenue | $250K–$750K | $250K | $250 | 4.5 mo | Yes (8868) | BCO-10 [VERIFY] | YYYY-MM-DD |
| MA | ≥ $500K | Gross support & revenue | $200K–$500K | $200K | $300 | 4.5 mo | Yes (8868) | Form PC [VERIFY] | YYYY-MM-DD |
| GA | ≥ $1M | Total revenue | $500K–$1M | $500K | — | — | — | C-100 [VERIFY] | YYYY-MM-DD |

#### Attorney Review Memo (1–3 pages)

Address:
- **Definitional variances** — states where "gross revenue" means materially different things
- **Guidance-only items** — thresholds found only in instructions/FAQs, not statute
- **Conflicts** — between statutes and instructions
- **Lowest thresholds** — states triggering audit/review first (MA at $500K, IL at $300K contributions)
- **Strictest deadlines** — states with no extensions (FL) or short windows
- **Update cadence** — recommend quarterly re-verification given administrative changes

## Guidelines

- **Verify all citations** — thresholds from the illustrative matrix are reference points; confirm against current statute/regulation before reliance
- **Fees change without legislation** — always check state charity bureau websites for current fee schedules
- **Primary source controls** — if FAQ/instructions conflict with statute, statute governs; note the conflict
- **Revenue ≠ contributions** — never assume equivalence across states; the definitional difference can shift which tier applies
- **Flag staleness** — any source not verified within 90 days should be marked for re-verification
- **Organization bylaws may impose lower thresholds** — board audit policies can require audits below state-mandated levels
- This skill is a research aid, not legal advice. A qualified attorney or CPA specializing in nonprofit compliance should review before filing.

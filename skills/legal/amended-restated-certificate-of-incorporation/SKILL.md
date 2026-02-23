---
name: amended-restated-certificate-of-incorporation
description: >-
  Drafts a filing-ready Delaware Amended and Restated Certificate of
  Incorporation for venture-financing rounds, converting term-sheet economics
  and negotiated governance terms into a defensible charter document. Use when
  updating or reauthorizing capital structure, preferred stock terms, or
  investor protections before/after closing. Trigger keywords: Delaware,
  242/245, cap table, Series A preferred, anti-dilution, liquidation
  preference, conversion, mandatory conversion, board seats, protective
  provisions, charter filing.
tags:
  - agreement
  - corporate
  - drafting
---

# Amended and Restated Certificate of Incorporation (Delaware)

Creates a drafting workflow for a Delaware Amended and Restated Certificate of Incorporation that is ready for filing and aligned to term-sheet, stock purchase, and governance documentation.

## Prerequisites

1. Exact legal name, Delaware formation date, and current charter text.
2. Board resolution and stockholder approval route (DGCL 242 vs. 245 pathway).
3. Term sheet + definitive documents (SPA, investors’ rights, voting agreement, registration/ROFR/Co-sale where applicable).
4. Cap table with current issuances, option pool, convertible instruments, warrants, and contemplated financing amounts.
5. Final economics by series: OIP, liquidation multiple, conversion mechanics, anti-dilution method, voting/protective rights.
6. Delaware registered office/agent name and physical address with county.
7. Planned series authority and board composition rights, including any carve-outs by series.
8. Authorized signer and corporate authorization evidence for execution.

## Output Structure / Process

Use this sequence and stop if any required data is missing.

| Step | Input Validation | Required Output |
|---|---|---|
| 1 | Deal parsing | Confirm transaction math and legal term consistency before drafting |
| 2 | Entity compliance | Confirm jurisdiction, registered details, and adoption path |
| 3 | Capital math | Produce authorized share tables with rounding/cushion checks |
| 4 | Preferred architecture | Draft Series provisions, voting, protections, conversion, anti-dilution |
| 5 | Governance layer | Add Section 102(b)(7), optional indemnification, forum/consent mechanics |
| 6 | Filing hardening | Build witness/signature execution block and final filing check |

### Required Input Matrix

| Item | Required? | Source | Validation check |
|---|---|---|---|
| Legal name | Required | Delaware certificate / formation docs | Matches all transaction docs exactly |
| Registered office + agent | Required | Corporate records | Physical address; county present |
| Series designations | Required | Term sheet | Unique identifiers and share counts |
| OIP / Conversion price | Required | Cap table + pricing | Convertible math tested |
| Liquidation waterfall | Required | Term sheet/SPA | Participating vs non-participating logic explicit |
| Anti-dilution | Required | Term sheet | Full formula with carve-outs specified |
| Protective provisions | Required | Term sheet + voting agreement | Series-specific treatment resolved |
| Officer execution | Required | Corporate records | Authorized signer identified |

### Drafting Framework (Section-by-Section)

1. **Preface/Recitals**
   - Heading: “Amended and Restated Certificate of Incorporation of [Exact Legal Name]”
   - Opening statement: Delaware corporation + DGCL 242/245 basis.
   - Include supersession clause and full textual restatement statement.

2. **Article I–III (core identity)**
   - **Name**: exact legal name + Delaware naming compliance.
   - **Registered office/agent**: Delaware physical office, county, consent posture.
   - **Purpose**: broad Delaware-purpose clause unless narrowed by deal terms.

3. **Article IV (Capitalization)**
   - Include:
     - Common authorized shares/par value
     - Preferred authorized shares/par value
     - Per-series designation and share count
     - Any undesignated preferred (“blank check”) authorization if negotiated
   - Math checks:
     - common authorized >= outstanding + reserved option pool + convertibles + reasonable cushion
     - preferred authorized includes pre/post financing and anti-dilution reserve buffer

4. **Article V (Preferred Stock rights)**
   - Dividends: cumulative/non-cumulative, rate, declaration conditions, payout priority.
   - Liquidation preference and distribution waterfall: 1x default unless negotiated higher multiple.
   - Participation/election logic for non-participating structures.
   - Conversion: optional + mandatory mechanics, surrender/issuance, fractional handling, conversion-effective timing.
   - Anti-dilution: weighted-average formula unless narrow instruction (full ratchet) exists.
   - Protective provisions: include standard veto rights thresholds, define affected actions and exceptions.
   - Voting: as-converted voting framework + class/series voting where required.

5. **Article VI (Directors)**
   - Include 102(b)(7) exculpation language and future DGCL-compliance fallback.
   - Add indemnification/advice-of-counsel-typical sections only if negotiated/consistent with rights docs.
   - Optional: forum-selection for internal corporate claims; board action/bylaw/meeting call mechanics.

6. **Execution**
   - “IN WITNESS WHEREOF” block + officer signature/date lines.
   - Ensure signatory authority is supported in corp action record.

### Templates

```text
AMENDED AND RESTATED CERTIFICATE OF INCORPORATION OF [LEGAL NAME]
Filed under Section 242 and, if applicable, Section 245 of the DGCL.
...
```

```text
Series [X] Preferred Stock - [Term]
- Designated Shares: [__]
- OIP: [$__]  Conversion Price: [$__]
- Liquidation: [__]x non-participating
- Conversion: Optional [yes/no], Mandatory: [trigger list]
- Anti-dilution: [broad-based weighted avg / other]
- Voting: [as-converted rights text]
- Protective actions: [list with vote threshold]
```

## Guidelines

- Use exact defined terms once, then reference consistently across sections.
- Align all charter economics with SPA, investor rights, and voting agreement; resolve conflicts explicitly before drafting.
- Keep statutory references in filing text anchored to current DGCL language and confirm latest amendments before finalizing `[VERIFY]`.
- Do not include investor-specific terms that are outside preferred stock mechanics (e.g., repurchase discounts, drag thresholds) unless documents require charter language.
- Require clear missing-data checkpoints for:
  - adoption path (242 vs 245),
  - minimum and maximum authorized share totals,
  - series-specific protective voting split,
  - anti-dilution carve-outs.
- For Delaware-only charter filing, include county and physical registered office address only; avoid non-Delaware filing forms.
- Reconcile waterfall outputs under at least three exit-value scenarios and two dilution scenarios before output.
- Preserve flexibility where possible, but do not overbroaden to the point of investor intent drift.
- Output only the complete certificate text if requested; otherwise provide a redline-ready draft and assumptions log separately.

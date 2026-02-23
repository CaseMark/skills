---
name: labeling-compliance-review
description: Conducts FDA labeling compliance reviews for drugs, foods, dietary supplements, and medical devices. Analyzes principal display panels and information panels against FDCA, 21 CFR, and FDA guidance to identify misbranding risks, claims violations, and mandatory disclosure gaps. Use when reviewing product labels, auditing FDA compliance, assessing labeling risk, or preparing for FDA submission.
tags:
  - analysis
  - drafting
  - regulatory
---

# FDA Labeling Compliance Review

Produces a structured compliance assessment of FDA-regulated product labeling, identifying misbranding risks and regulatory gaps with actionable corrective recommendations.

## Prerequisites

1. **Product label files** — high-resolution images or PDFs of all label panels (PDP, information panel, back/side panels)
2. **Product classification** — drug (OTC/Rx), food, dietary supplement, medical device, or cosmetic
3. **Intended use statement** — as marketed and as labeled
4. **Claims substantiation file** (if applicable) — scientific support for any health, structure/function, or nutrient content claims
5. **Prior FDA correspondence** (if any) — warning letters, 510(k) clearance, or labeling supplements

## Output Structure

### 1. Product Identification

| Field | Detail |
|---|---|
| Product name (as labeled) | Include trademarked elements |
| Product classification | Drug / Food / Dietary Supplement / Device / Cosmetic |
| Intended use | Specific conditions, target population, route/method |
| Applicable framework | Identify controlling CFR parts (e.g., 21 CFR 101 for food, 21 CFR 201 for drugs) |

### 2. Principal Display Panel (PDP) Review

Evaluate against product-specific PDP requirements:

| Element | Requirement | Compliant? | Citation | Notes |
|---|---|---|---|---|
| Statement of identity | Common/usual name or standard of identity | | 21 CFR 101.3 (food) / 21 CFR 201.10 (drug) | |
| Net quantity of contents | Lower 30% of PDP, minimum type size per area | | 21 CFR 101.105 / 21 CFR 201.51 | |
| Established drug name | Prominent, ≥½ size of proprietary name | | 21 CFR 201.10(g) | |
| Prohibited terms/imagery | No unapproved therapeutic claims, no misleading vignettes | | FDCA §403(a) / §502(a) | |
| Type size & prominence | Meets minimum ratios; not obscured by design elements | | 21 CFR 101.15 / 21 CFR 201.15 | |

### 3. Information Panel Review

**For Foods — Nutrition Facts:**

- [ ] Correct format per 21 CFR 101.9
- [ ] Serving size per RACC (21 CFR 101.12)
- [ ] All mandatory nutrients declared in prescribed order
- [ ] Daily value percentages current
- [ ] Type size ≥ 6 pt (≥ 8 pt for "Nutrition Facts" heading)
- [ ] Ingredient list in descending order of predominance (21 CFR 101.4)
- [ ] Allergen declaration per FALCPA (21 CFR 101.4(d)) — "Contains:" statement or parenthetical

**For OTC Drugs — Drug Facts:**

- [ ] Standardized format per 21 CFR 201.66
- [ ] Headings in prescribed order: Active ingredient → Purpose → Uses → Warnings → Directions → Other information → Inactive ingredients
- [ ] Minimum 6 pt type size
- [ ] Warnings include all required subheadings (Ask a doctor, Do not use, etc.)
- [ ] Adequate directions for use (21 CFR 201.5)

**For Dietary Supplements — Supplement Facts:**

- [ ] Format per 21 CFR 101.36
- [ ] All dietary ingredients listed with amounts and %DV
- [ ] "Other ingredients" listed below panel
- [ ] Required § 403(s) disclaimer present

**For Medical Devices:**

- [ ] Adequate directions for use (21 CFR 801.5)
- [ ] Intended use and indications
- [ ] Contraindications, warnings, precautions
- [ ] UDI compliance if applicable (21 CFR 801.20)

### 4. Claims Compliance

For each claim on the label, complete:

| Claim Text | Claim Type | Permissible? | Required Disclaimer | Substantiation | Citation |
|---|---|---|---|---|---|
| | Health / Qualified Health / Structure-Function / Nutrient Content / Therapeutic | Y/N | Text of required disclaimer | Adequate / Insufficient / Missing | |

**Key rules:**

- Structure/function claims (supplements): must include "This statement has not been evaluated by the FDA..." disclaimer and must not imply disease treatment (21 CFR 101.93)
- Health claims: must be authorized by regulation (21 CFR 101.70-83) or qualify as qualified health claim with appropriate language
- Nutrient content claims: must meet defined criteria (21 CFR 101.13, 101.54-101.69)
- Claims that imply disease diagnosis, treatment, cure, or prevention → product may be an unapproved new drug (FDCA § 201(g))

### 5. Warnings & Mandatory Statements

| Required Statement | Present? | Correct Format? | Citation |
|---|---|---|---|
| Allergen declaration (FALCPA) | | | 21 CFR 101.4(d) |
| Pregnancy/nursing warning | | | 21 CFR 201.63 / 101.17(h) |
| Children's dosing/warning | | | Product-specific |
| Tamper-evident statement | | | 21 CFR 211.132 (drugs) |
| Storage conditions | | | 21 CFR 201.66(c)(8) |
| Manufacturer/distributor name & address | | | 21 CFR 101.5 / 201.1 |
| Prop 65 (if CA distribution) | | | CA Health & Safety Code § 25249.6 [VERIFY] |

### 6. Compliance Conclusion

**Overall status:** Compliant / Non-Compliant / Conditionally Compliant

**Findings table:**

| # | Finding | Severity | Regulatory Basis | Recommended Correction | Priority |
|---|---|---|---|---|---|
| | | Critical / Major / Minor | CFR cite | Specific fix | Immediate / 30-day / Next revision |

**Severity definitions:**

- **Critical** — renders product misbranded; exposes to enforcement (warning letter, seizure, injunction)
- **Major** — significant regulatory gap; likely flagged in FDA inspection
- **Minor** — technical deficiency; low enforcement risk but should be corrected

**Risk assessment:** Summarize enforcement exposure — likelihood of warning letter, import detention (if applicable), or referral to DOJ.

**Reviewer documentation:** Record reviewer name, date, label version/lot examined.

## Guidelines

- Always cite specific 21 CFR sections — do not give generic "FDA requires" statements
- Flag any area where product classification is ambiguous (e.g., supplement vs. drug boundary) and note the regulatory consequences of each classification
- If the product is marketed for a disease condition but classified as a supplement or food, flag the unapproved new drug risk explicitly
- Mark any citations you cannot verify with `[VERIFY]`
- Do not assume state-level requirements are met — note that state laws (e.g., California Prop 65, state food labeling laws) may impose additional obligations
- For combination products or novel ingredients, recommend pre-market consultation with FDA
- If label was previously subject to a warning letter, cross-check all cited deficiencies against current label

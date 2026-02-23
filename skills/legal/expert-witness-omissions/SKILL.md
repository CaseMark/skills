---
name: expert-witness-omissions
description: Analyzes expert witness reports, depositions, and testimony transcripts to identify medical records the expert failed to review, cite, or address. Cross-references the expert's stated materials-reviewed list against the full case medical record set to surface omissions that contradict opinions, reveal pre-existing conditions, expose selective review, or undermine Daubert/Frye admissibility. Produces a tiered omissions register, methodology critique, bias pattern analysis, and strategic recommendations for cross-examination, motions to exclude, and rebuttal expert focus areas. Use in personal injury or medical malpractice litigation during discovery, pre-trial, or trial preparation when challenging or defending expert witness credibility.
tags:
  - analysis
  - litigation
---

# Expert Witness Medical Records Omissions Analysis

Identifies gaps in an expert's medical record review to support impeachment, exclusion motions, and rebuttal strategy.

## Prerequisites

1. **Expert materials** — reports, deposition transcripts, and any disclosed materials-reviewed list
2. **Complete medical record set** — all records in the case file (clinical notes, labs, imaging, operative reports, pharmacy records, consult notes, etc.)
3. **Case context** — the expert's stated opinions and the claims or defenses they support

## Output Structure

### 1. Materials Reconciliation Table

| Record / Document | Date | In Case File | Cited by Expert | Gap |
|---|---|---|---|---|
| {Record name / provider} | {Date} | ✓ | ✗ | Omitted |

List every record in the case file. Flag all not cited or addressed by the expert.

---

### 2. Omissions Register

For each omitted record, provide:

| Field | Detail |
|---|---|
| **Record** | Name, date, provider, Bates/page cite |
| **Expert's assertion** | Verbatim quote + transcript/report cite where expert claims thorough review or makes the contradicted factual claim |
| **Omitted content** | Key findings, values, diagnoses, or clinical events |
| **Significance tier** | Critical / High / Moderate / Low (see below) |
| **Inadvertent or strategic** | Assessment with reasoning |

**Significance Tiers:**

| Tier | Description |
|---|---|
| **Critical** | Directly contradicts the expert's core opinion or a key factual assertion |
| **High** | Documents pre-existing conditions, alternative causation, or treatment decisions the expert ignored |
| **Moderate** | Fills timeline gaps or undermines methodology without negating the opinion outright |
| **Low** | Minor oversight unlikely to affect substantive conclusions |

---

### 3. Methodology Critique

Address each point:
- Did the expert provide a complete, dated materials-reviewed list?
- Does the expert's chronology of events align with the actual medical timeline?
- Did the expert acknowledge or explain any record gaps?
- Are there factual assertions in the report that are contradicted by records the expert claims to have reviewed?

---

### 4. Bias / Pattern Analysis

Identify patterns across omissions and characterize as **confirmation bias**, **selective review**, or **inadvertent oversight**:

| Pattern | Records Involved | Characterization |
|---|---|---|
| Systematic exclusion of pre-incident records | | |
| Selective citation of favorable test results, omission of contradictory values | | |
| Treating physician notes omitted where they conflict with retained expert | | |
| Single-provider reliance while ignoring other treating sources | | |

---

### 5. Strategic Recommendations

**Cross-Examination**
- List targeted questions anchored to each Critical and High omission
- Sequence: establish foundation (expert claims thorough review) → confront with specific omitted record → force acknowledgment or explanation

**Daubert / Frye Motion**
- Flag omissions that undermine the reliability of the expert's methodology under FRE 702(b) (*Daubert v. Merrell Dow Pharms.*, 509 U.S. 579 (1993)) [VERIFY for applicable circuit/state standard]
- Assess whether selective review rises to **exclusion** or **weight-only** argument
- Note if the opinion rests on incomplete or cherry-picked facts sufficient for a Rule 702 challenge

**Rebuttal Expert Focus Areas**
- Enumerate records the opposing expert omitted that a rebuttal expert must affirmatively address
- Timeline corrections required
- Alternative causation or diagnosis pathways to develop

## Guidelines

- Maintain objectivity — distinguish genuine credibility threats from minor oversights; not every omission is bad faith
- Note Daubert vs. Frye jurisdiction: federal courts and most states apply Daubert; a minority still use Frye [VERIFY state]
- Flag any records that are themselves incomplete, illegible, or appear to have missing pages
- Label output as attorney work product
- Applies equally to plaintiff-side and defense expert scrutiny

---
name: awa-compliance-audit
description: >-
  Produces a defensible Animal Welfare Act (AWA) compliance audit for
  USDA/APHIS‑regulated exhibitors, dealers, research facilities, carriers, and
  intermediate handlers. Maps inspection citations to verified `9 C.F.R. Parts
  1–3` requirements, analyzes recurrence and severity patterns
  (Indirect/Direct/Critical), evaluates core compliance programs (Program of
  Veterinary Care, IACUC, records, housing, transport), and outputs a
  prioritized corrective action plan with documentation artifacts and
  enforcement‑aware language. Use when auditing AWA compliance, reviewing USDA
  inspection reports (Form 7002), preparing for license/renewal, diligence, or
  enforcement risk assessment. Trigger keywords: Animal Welfare Act, AWA,
  USDA, APHIS, inspection report, Form 7002, IACUC, PVC, exhibitor, dealer,
  research facility, animal care standards.
tags:
  - analysis
  - litigation
---

# AWA Compliance Audit (USDA/APHIS)

Produces an enforcement-aware AWA compliance audit and corrective action plan tied to verified CFR requirements.

## Prerequisites

1. Facility status: USDA license/registration class and number, regulated activities, covered species, sites.
2. Inspection/enforcement record: all Form 7002 reports (3–5 years), warnings, investigations, settlements, ALJ decisions.
3. Operating evidence: PVC signed by AV, SOPs, treatment logs, A&D records (Forms 7001/7020), ID system, environmental/sanitation logs, training, staffing, incident reports, maintenance, enclosure specs.
4. Research materials (if applicable): IACUC minutes, protocols, Search for Alternatives documentation.
5. Governing authorities verified in `https://www.ecfr.gov/`: AWA statute (7 U.S.C. § 2131 et seq.) [VERIFY], `9 C.F.R. Parts 1–3` (species subparts) [VERIFY], APHIS guidance if cited [VERIFY].
6. If any item is missing, stop and request it before analysis.

## Output Structure / Process

1. **Applicability Statement**
   1. Identify license class, sites, species inventory, regulated activities.
   2. Map applicable `9 C.F.R. Part 2` admin requirements and Part 3 species subparts [VERIFY].
   3. Flag ambiguity in facility classification and recommend confirmation.

2. **Citation Map (Inspection → CFR → Evidence)**
   - Build a table for every cited item in Form 7002 reports.

| Report Date | NCI Type | CFR Cite (Verified) | Inspector Observation (Quote) | Facility Evidence | Analysis | Recurrence |
| --- | --- | --- | --- | --- | --- | --- |

3. **Severity and Pattern Analysis**
   - Classify each issue by USDA NCI level: Indirect, Direct, Critical [VERIFY source if not in report].
   - Identify recurrence by CFR section and time window.
   - Assign internal risk tier: Low, Medium, High (explicitly internal, not USDA).

| Pattern | CFR Cite | Recurrence Count | NCI Severity | Likely Driver | Risk Tier |
| --- | --- | --- | --- | --- | --- |

4. **Program Deep-Dive**
   - **PVC/AV Oversight**: verify authority, signatures, visit cadence, treatment documentation [VERIFY `9 C.F.R. § 2.40`].
   - **Species Subparts**: confirm standards for each species; avoid applying general standards to species-specific rules.
   - **Housing/Sanitation/Environment**: structural integrity, drainage, ventilation, water, feed, pest control.
   - **Records/ID/Traceability**: acquisition/disposition, identification, health certifications [VERIFY `9 C.F.R. §§ 2.75, 2.78`].
   - **IACUC** (research): protocol review, semiannual inspection, alternatives search [VERIFY `9 C.F.R. § 2.31`].
   - **Transport/Carriers**: handling, containment, carrier obligations [VERIFY].

5. **Corrective Action Plan (CAP)**
   - Create a CAP table with immediate, short-term, and structural remediation.

| Finding | CFR Cite | Root Cause | Immediate Fix (0–14 days) | System Fix (30–90 days) | Owner | Proof Artifact |
| --- | --- | --- | --- | --- | --- | --- |

6. **Audit Memo Structure**
   1. Executive Summary
   2. Facility Profile and Applicability
   3. Inspection History Timeline
   4. Findings by Regulatory Domain
   5. Pattern Analysis and Root Causes
   6. Corrective Action Plan
   7. Record Retention and Self-Audit Plan
   8. Appendix: Citation Map and Source List

7. **Quality Control Checklist**
   - Every legal requirement tied to `eCFR` text with verified CFR cite.
   - Every factual statement tied to a report, record, or interview (labeled).
   - Gaps in records explicitly stated.
   - CAP includes owners, dates, and proof artifacts.
   - Language avoids admissions unless instructed.

## Guidelines

- Verify all CFR citations in `https://www.ecfr.gov/`; mark any uncertain cite as `[VERIFY]`.
- Do not invent USDA guidance, penalty ranges, or enforcement thresholds; label as `[VERIFY]` if referenced.
- Treat inspection reports as discoverable; use precise, non-conclusory language.
- Avoid stating “in violation” unless directed; use “USDA cited noncompliance with…”.
- If mixed operations create ambiguity, state the ambiguity and its compliance impact.
- If animal welfare risk is imminent, flag for immediate action and expert consultation.
- Distinguish AWA scope from state/local overlays; note that stricter state laws may apply.
- Preserve privilege: label as attorney work product when appropriate; limit distribution.
- Output requires attorney review before external use.

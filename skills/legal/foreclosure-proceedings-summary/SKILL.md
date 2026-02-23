---
name: foreclosure-proceedings-summary
description: Generates structured, chronological summaries of U.S. foreclosure proceedings from case documents. Extracts parties, property details, loan information, procedural timeline, judicial decisions, critical deadlines, and current status. Flags bankruptcy stays, loss mitigation holds, standing challenges, RESPA/TILA compliance issues, and procedural irregularities. Distinguishes judicial vs. non-judicial foreclosure procedures. Use when assessing foreclosure case posture for lender representation, borrower defense, or real estate transactions affected by pending foreclosure actions.
tags:
  - litigation
  - summarization
  - summary
---

# Foreclosure Proceedings Summary

Produces a structured case summary from foreclosure documents for rapid attorney review of procedural posture, deadlines, and next steps.

## Prerequisites

1. **Court filings** — complaint/petition, summons, proof of service, answer, motions, orders
2. **Notices** — notice of default, notice of sale, notice to occupants/junior lienholders
3. **Loan documents** — promissory note, mortgage/deed of trust, payment history
4. **Orders and judgments** — scheduling orders, judgment of foreclosure, sale confirmation orders
5. **Any bankruptcy filings** or loss mitigation correspondence, if applicable

## Output Structure

### 1. Case Overview

| Field | Detail |
|---|---|
| Court & Case No. | |
| Plaintiff/Lender | |
| Defendant/Borrower | |
| Property Owner (if different) | |
| Property Description | Full legal description + address |
| Original Loan Amount & Date | |
| Amount in Default | |
| Foreclosure Type | Judicial / Non-Judicial |

---

### 2. Procedural Timeline

Chronological table of all significant events:

| Date | Event | Legal Significance |
|---|---|---|
| | Initial default | |
| | Notice of default issued | |
| | Foreclosure complaint filed / Notice of trustee's sale recorded | |
| | Service of process completed | |
| | Answer / responsive pleadings filed | |
| | Motions practice (MTD, MSJ, etc.) | |
| | Hearings / conferences | |
| | Mediation / settlement discussions | |
| | Judgment of foreclosure entered | |
| | Sale scheduled / conducted | |

---

### 3. Key Judicial Decisions

For each order or ruling: date, ruling, court's reasoning, and practical impact on the proceeding.

---

### 4. Critical Dates & Deadlines

| Date | Deadline / Event | Status |
|---|---|---|
| | Redemption period expiration | |
| | Foreclosure sale date | |
| | Response deadline (pending motions) | |
| | Trial / hearing dates | |
| | Jurisdiction-specific statutory deadlines | |

---

### 5. Current Status & Next Steps

- **Current procedural posture** — where in the foreclosure process the matter stands
- **Immediate actions required** — by which party, by when
- **Projected timeline** to resolution or sale

---

### 6. Flags & Issues

Check all that apply and note specifics:

- [ ] **Bankruptcy filing** — automatic stay in effect? Relief from stay sought/granted?
- [ ] **Loss mitigation / loan modification** — application pending, foreclosure paused?
- [ ] **Standing challenge** — note of transfer, MERS issues, securitization chain
- [ ] **Predatory lending / TILA / RESPA** — compliance issues raised
- [ ] **Notice defects** — proper notice to junior lienholders, occupants, co-borrowers?
- [ ] **Procedural irregularities** — missed statutory deadlines, defective service
- [ ] **Deficiency judgment** — permitted under applicable state law?
- [ ] **Right of redemption** — statutory period and expiration

## Guidelines

- **Judicial vs. non-judicial**: Explicitly identify the foreclosure mechanism; procedures, timelines, and available defenses differ materially by state
- **Jurisdiction**: U.S. only; flag the state and note whether it is a judicial-foreclosure state [VERIFY applicable state statute]
- **Monetary figures**: State all amounts exactly as appearing in source documents; do not round or estimate
- **Citation discipline**: Reference specific document names and page numbers for key facts and dates
- **Objectivity**: Use neutral, factual language suitable for use by plaintiff or defense counsel
- **Federal overlays**: Note RESPA (12 U.S.C. § 2605), TILA (15 U.S.C. § 1601), and CFPB loss mitigation rules (12 C.F.R. § 1024.41) where implicated [VERIFY current regulations]

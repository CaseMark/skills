---
name: plea-agreement-summary
description: Generates structured summaries of criminal plea agreements, extracting charges (original vs. plea), factual basis, sentencing recommendations, waivers, cooperation provisions, collateral consequences, and breach terms. Use when summarizing plea deals, preparing clients for plea colloquy, or creating quick-reference digests of negotiated resolutions in criminal defense matters.
tags:
  - litigation
  - summarization
  - summary
---

# Plea Agreement Summary

Produces a structured quick-reference summary of a criminal plea agreement for attorneys, clients, and court personnel.

## Prerequisites

1. **Plea agreement document** — fully executed or draft
2. **Original charging document** — complaint, indictment, or information (to compare original vs. plea charges)
3. **Applicable sentencing guidelines** — federal or state, if referenced in the agreement

## Output Structure

Generate the summary using the following sections. Use tables for charges and sentencing terms. Omit any section that has no corresponding content in the agreement.

### 1. Case Identification

| Field | Value |
|-------|-------|
| Defendant | Name, DOB, case number |
| Jurisdiction | Court, county/district |
| Prosecutor | Name, office |
| Defense Counsel | Name, firm |
| Date of Agreement | |

### 2. Charges Comparison

| # | Original Charge | Statute | Max Penalty | Plea Charge | Statute | Max Penalty | Disposition |
|---|----------------|---------|-------------|-------------|---------|-------------|-------------|
| 1 | | | | | | | Guilty/Nolo/Dismissed |

- Note any counts dismissed, reduced, or amended as part of the agreement.

### 3. Factual Basis

Summarize the defendant's admissions and stipulated facts supporting each plea count. Keep concise but sufficient to establish the factual predicate. Flag any disputed facts or reservations.

### 4. Sentencing Terms

| Term | Details |
|------|---------|
| Incarceration | Duration, concurrent/consecutive, credit for time served |
| Probation/Supervised Release | Duration, conditions |
| Fines | Amount, payment schedule |
| Restitution | Amount, recipients, payment schedule |
| Community Service | Hours, deadline |
| Special Conditions | Treatment, counseling, geographic restrictions, etc. |

- State whether the agreement is **binding on the court** (Fed. R. Crim. P. 11(c)(1)(C) type) or **advisory/recommendation only** (11(c)(1)(B) type).
- Note any joint recommendation vs. prosecution-only cap vs. open sentencing.

### 5. Waivers

Checklist — mark each as included or not:

- [ ] Right to jury trial
- [ ] Right to appeal conviction
- [ ] Right to appeal sentence (above/below stipulated range)
- [ ] Post-conviction/habeas corpus relief
- [ ] Suppression motions
- [ ] Other (specify)

Note any preserved rights or conditional waivers.

### 6. Cooperation Provisions

If applicable:

- Scope of cooperation (testimony, debriefings, undercover work)
- Government's obligations (5K1.1 motion, immunity, sentence reduction)
- Use limitations on defendant's statements (Fed. R. Evid. 410 / Fed. R. Crim. P. 11(f) protections)
- Safety/protection arrangements

### 7. Collateral Consequences

Flag any consequences **explicitly addressed** in the agreement:

- [ ] Immigration consequences (deportation, inadmissibility)
- [ ] Sex offender registration (tier, duration)
- [ ] Firearm prohibition
- [ ] Professional licensing impact
- [ ] Civil asset forfeiture
- [ ] Loss of voting rights
- [ ] Other civil disabilities

### 8. Breach Provisions

- What constitutes breach (new offenses, failure to cooperate, false statements)
- Government remedies upon breach (reinstate charges, withdraw recommendations, use statements)
- Notice/cure requirements, if any

### 9. Special Provisions

Capture anything non-standard:

- Deferred adjudication or diversion terms
- Conditional dismissal triggers
- Sealed or confidential provisions
- Co-defendant coordination terms

### 10. Key Dates & Deadlines

| Event | Date/Deadline |
|-------|---------------|
| Sentencing hearing | |
| Restitution payments begin | |
| Compliance reporting | |
| Probation start | |

## Guidelines

- **Plain language for client accessibility** — define legal terms parenthetically on first use, but keep the document precise enough for practitioners.
- **Monetary amounts, dates, and statutory citations must be exact** — never paraphrase numbers or round figures.
- **Flag ambiguities** — if a provision is unclear or internally inconsistent, note it with `[AMBIGUOUS — verify with full agreement]`.
- **Do not editorialize** — summarize what the agreement says, not whether the terms are favorable.
- **Distinguish binding vs. advisory terms** — this is the single most critical distinction for client counseling.
- **Immigration consequences** — if the agreement is silent on immigration impact and the defendant may be a non-citizen, flag with `[WARNING: Agreement silent on immigration consequences — Padilla v. Kentucky requires advisement]`.

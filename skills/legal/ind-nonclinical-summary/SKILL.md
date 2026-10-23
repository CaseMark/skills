---
name: ind-nonclinical-summary
language: en
description: Drafts the nonclinical sections of an FDA IND in Common Technical Document format from primary study reports, namely the Module 2.4 Nonclinical Overview and the Module 2.6 Written and Tabulated Summaries for pharmacology, pharmacokinetics and toxicology. Builds a study inventory, reconciles conflicting values, tabulates NOAELs and exposure multiples, and supports first-in-human starting-dose selection for small molecules and therapeutic proteins, with a source citation for every value. Use when asked to summarize nonclinical, preclinical, pharmacology, ADME, PK or toxicology reports, write CTD 2.4 or 2.6, prepare an IND pharmacology/toxicology section, or calculate HED, MRSD or safety margins. Draft for qualified expert review. Pilot, pending expert review.
tags:
  - regulatory
  - drafting
  - summary
  - summarization
---

# IND Nonclinical Overview and Summaries (CTD 2.4 and 2.6)

Turns a set of primary nonclinical study reports into the nonclinical sections of an IND in Common Technical Document (CTD) format: the Module 2.4 Nonclinical Overview and the Module 2.6 Written and Tabulated Summaries. It covers small molecules and therapeutic proteins, including monoclonal antibodies. The deliverable is a study inventory, ranked issues, the drafted sections, a calculation ledger and a reviewer checklist. It is a draft for a qualified toxicologist or regulatory affairs professional. It is never submission-ready.

## Pilot Status

This skill is in pilot. Its regulatory content was checked against primary guidance (see `references/primary-sources.md`) but has not yet been reviewed by a qualified toxicologist or regulatory affairs professional. Treat every output as a draft, and expect the reviewer to resolve each `[VERIFY]` and INFERENCE item.

## Scope and Hand-offs

- Whole-IND assembly, Form 1571, CMC and protocols: `ind-application`.
- Investigator's Brochure: `investigator-brochure`. Draft this skill's Module 2.6 first and build the brochure's nonclinical section from it so the numbers match.
- NDA or BLA Module 2: the heading structure is the same, but depth differs (full carcinogenicity and reproductive programs); see `nda-drug-application`, which gives a table-level 2.4 view inside a whole-application skill. This skill is the IND-stage drafting path for 2.4 and 2.6 from raw reports.
- Summaries of a finished submission package for reviewers or executives: `regulatory-submission-summary`. This skill drafts the nonclinical sections themselves from study reports; it does not summarize a completed package.
- Not covered: antibody-drug conjugates, oligonucleotides, cell and gene therapies, vaccines, radiopharmaceuticals, and endogenous proteins used at physiologic levels. Tell the user the modality is outside this skill and stop at the inventory.

## Ground Rules

1. **Draft only.** Never state or imply the output is ready to file. Every output ends with the reviewer checklist from `references/output-template.md`.
2. **Cite every value.** Use two layers. Inline, use the CTD form `(Table X.X, Study ID)` pointing to the tabulated summary. Then add the source locator `[Study ID, Section, Table, p.]` to the report itself. A value without both is not drafted.
3. **No estimates.** If a report does not give a parameter, write `Not reported in <Study ID>`. Never fill a gap from memory, from another study or from a class analogy. Published literature may be used only with a full citation and the label "literature".
4. **Calculate only from cited inputs.** HED, MRSD and exposure multiples are calculated, not extracted. Show the formula, the inputs with their citations, and label the result `calculated`. Human dose and exposure projections come from the sponsor; if absent, write `[SPONSOR INPUT REQUIRED]` and leave the margin blank.
5. **Name conflicts, do not resolve them silently.** Within a study, rank sources: signed final report text and any study director amendment, then data tables, then appendices, then slides or summaries. Show both values, say which controls, and list the conflict in the issues section.
6. **Summaries are factual; the Overview interprets.** Module 2.6 is a factual synopsis. Clinical relevance, safety margins, starting-dose logic and implications for safe use go in Module 2.4.
7. **State GLP status per study.** Use `GLP`, `non-GLP` or `not stated`, with the reason when the report gives one. Do not call a non-GLP study a deficiency; flag it for the sponsor, who must give the statement or reason the regulation requires for each covered study.
8. **Say "nonclinical".** Include in vitro and other non-animal data on equal footing. Do not assume every study uses animals.
9. **Mark what you cannot confirm with `[VERIFY]`.** Regulatory statements in the references were checked against primary text; items tagged `[VERIFY]` or INFERENCE in `references/primary-sources.md` were not. Never state them as settled; carry each one you rely on into the reviewer checklist.
10. **Use the CTD presentation order and one set of units.** In vitro before in vivo; by species, then route (intended human route first), then duration (shortest first). Convert units consistently and keep the original in the card.

## Workflow

### Step 0: Intake

Ask for what is missing, then proceed with what was given and list the gaps.

1. Modality: small molecule or therapeutic protein. Read `references/modality-pathways.md`.
2. Population and plan: healthy volunteers or patients, indication (note oncology), route, first dose, maximum dose, duration.
3. Sponsor human projections: expected exposure (AUC, Cmax) at first and maximum dose, and the basis, if any.
4. The report set, the sponsor's template if any, and any prior Module 2 text.

### Step 1: Inventory and extraction

Read `references/study-inventory-and-extraction.md`. Build the inventory table and assign each study to a CTD section. Write one extraction card per study before drafting; for more than about ten reports, extract study by study so no draft depends on holding every report in context. Draft only from the cards.

### Step 2: Reconcile

Apply the reconciliation rules in the same reference: text versus tables, study director amendments, sex-specific and day-specific values, recovery groups, unit mismatches, formulation or batch differences. Record every conflict.

### Step 3: Calculations

Read `references/exposure-and-starting-dose.md`. Build the exposure-multiple table and the starting-dose derivation for the pathway chosen in Step 0, or mark them pending sponsor input.

### Step 4: Draft Module 2.6

Read `references/ctd-module-2-structure.md`. Write 2.6.1 to 2.6.7 in order. Keep each written summary factual and include the Brief Summary, Discussion and Conclusions and Tables and Figures headings. Where a section has no data at this stage, keep the heading and state that no study was conducted and why, if the sponsor said.

### Step 5: Draft Module 2.4

Write the six Overview headings from the structure reference. This is where the integrated assessment lives: testing strategy and species justification, relevance of findings, exposure comparison with humans, target organs and monitoring implications, and the starting-dose rationale.

### Step 6: Issues and review pack

Rank the issues by severity, complete the calculation ledger, and produce the reviewer checklist.

## Required Output Format

Produce these six parts in order, using `references/output-template.md`.

1. **Study inventory.** One row per report with section, species, GLP status, completion date and any amendment.
2. **Issues and gaps.** Ranked by severity, each with its citation and who can resolve it.
3. **Module 2.6.** Written and tabulated summaries.
4. **Module 2.4.** The Nonclinical Overview.
5. **Calculation ledger.** Every calculated value with formula, inputs, citations and the label `calculated`.
6. **Reviewer checklist.** What the qualified reviewer must confirm.

Example of a drafted value and a gap:

```
Rat 28-day repeat-dose study, NOAEL 30 mg/kg/day (Table 2.6.7.7, TX-2024-001)
[TX-2024-001, Section 8.2, Table 11, p. 71]. Day 28 AUC0-24 in males 41.2 ug.h/mL
[TX-2024-001, Table 14, p. 88]. Female AUC0-24: Not reported in TX-2024-001.
```

## Troubleshooting

- **Report text and tables disagree.** Keep both in the card, apply rule 5, list the conflict. Do not average.
- **Study has a study director amendment.** Use the amended values and cite the amendment, as the final report is corrected by amendment.
- **AUC given per sex or per day.** Keep each separate. Pick the basis for margins by rule (same parameter, same day, same matrix as the human projection) and state it.
- **No human exposure projection.** Draft everything else, leave margins and MRSD marked `[SPONSOR INPUT REQUIRED]`, and list it first in the issues.
- **Scanned or low-quality PDFs.** Mark extracted numbers `[VERIFY: OCR]` and list the file.
- **Only one relevant species for a protein.** ICH S6 allows one relevant species in justified cases; state the evidence of relevance in the species justification and flag it for the reviewer.
- **User asks to fill a gap from analogs or literature.** Allow only with a full citation and the label "literature"; otherwise keep `Not reported`.

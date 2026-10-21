---
name: investigator-brochure
language: en
description: Drafts a sponsor's Investigator's Brochure for an IND or clinical trial of a drug or biologic under 21 CFR 312.23(a)(5), 312.55 and ICH E6, from nonclinical study reports or Module 2 summaries, CMC documents, protocols and any human data. Covers the summary, introduction, properties and formulation, nonclinical studies, effects in humans, and the summary of data and guidance for the investigator, including the reference safety information that decides whether an adverse event is expected. Use when preparing, updating or annually revising an investigator brochure, or converting nonclinical summaries into brochure sections. Not for investigator CVs, Form FDA 1572 or investigator agreements.
tags:
  - regulatory
  - drafting
  - summarization
---

# Investigator's Brochure

Drafts the Investigator's Brochure (IB): the compilation of clinical and nonclinical data on an investigational product that is relevant to its study in humans, written so investigators understand the rationale for the protocol's dose, regimen and safety monitoring. It covers drugs and biologics. The deliverable is a draft IB, a source and consistency log, and a reviewer checklist. It is a draft for the sponsor's medically qualified editor and the disciplines that generated the data. It is never final.

## Scope and Hand-offs

- Nonclinical detail: `ind-nonclinical-summary`. When its Module 2.6 output exists, build the IB nonclinical section from it so every number matches; do not re-extract from study reports.
- Whole-IND assembly and Form 1571: `ind-application`.
- Investigator agreements and site contracts: `clinical-trial-investigator-agreement` and `investigator-agreement`.
- Informed consent: `informed-consent-form-clinical-trial`.
- Not an investigator CV, biographical sketch or credential packet.
- Modalities outside small molecules and therapeutic proteins (cell and gene therapy, vaccines, antibody-drug conjugates, oligonucleotides): draft the structure but tell the user the nonclinical and safety sections need modality-specific input.

## Ground Rules

1. **Draft only.** Never present the output as final. The IB needs a medically qualified person involved in drafting, and approval of content by the disciplines that generated the data.
2. **Concise, objective, balanced, non-promotional.** Present data so a clinician can make an independent risk-benefit assessment. No unsupported efficacy claims, no adjectives that sell.
3. **Cite every value.** Nonclinical figures, human data and safety findings carry `[Study ID, Section, Table, p.]` to the source, or the Module 2.6 citation when built from it.
4. **No estimates.** If a source does not give a value, write `Not reported in <Study ID>`. Calculated values are labeled `calculated` with formula and inputs. Sponsor facts that are missing are `[SPONSOR INPUT REQUIRED]`.
5. **Reference safety information is required.** Include a list of adverse reactions with frequency and nature, because it is the reference for deciding whether a suspected serious adverse reaction is expected. Label each entry's basis: observed in humans, anticipated from nonclinical findings, or reported with the drug class. For a product with no human data, the framing of the list is the sponsor's and regulatory affairs' decision, not yours; draft it as a proposal until they record it. Read `references/reference-safety-information.md`.
6. **Keep protocol content in the protocol.** The IB tells investigators the risks and the tests, observations and precautions that may be needed. Stopping rules, dose-modification algorithms and eligibility criteria belong in the protocol; the IB points to it.
7. **Control the edition.** Title page carries the edition number, the edition it supersedes, the release date and the data cut-off date. The IB is reviewed at least annually.
8. **Say "nonclinical".** Include in vitro and other non-animal data on equal footing.
9. **Mark what you cannot confirm with `[VERIFY]`.** References were checked against primary text; items tagged `[VERIFY]` or INFERENCE in `references/primary-sources.md` were not. Never state them as settled; carry each one you rely on into the reviewer checklist.

## Workflow

### Step 0: Intake

Ask for what is missing, then proceed and list the gaps.

1. Product identity: research number, chemical and generic names, modality, sponsor.
2. New IB or update; if an update, the current edition, its data cut-off and what is new.
3. Human data: none (first-in-human) or completed and ongoing studies.
4. Inputs: Module 2.6 text or study reports, CMC documents, protocol, any existing IB or sponsor template.
5. Whether a marketed product is being studied for a new use (that needs an IB specific to the new use unless the sponsor gives a rationale for a single IB).

### Step 1: Fix the structure

Read `references/ib-structure-and-content.md`. Use the ICH heading order. Numbering is the sponsor's choice; the ICH example numbering is only an example.

### Step 2: Properties and formulation

Draft from CMC documents: substance description with structural formula, relevant physical, chemical and pharmaceutical properties, formulation and excipients (justified if clinically relevant), storage and handling for the site pharmacy, and structural similarities to known compounds.

### Step 3: Nonclinical studies

Summarize methodology, results and the relevance to humans for pharmacology, pharmacokinetics and metabolism, and toxicology, using the headings in the structure reference. Tabulate wherever possible. Compare effective and non-toxic doses in the same species, in blood or tissue levels (or human equivalent dose) rather than mg/kg where possible, and relate them to the proposed human dosing.

### Step 4: Effects in humans

First-in-human: state that no human studies have been conducted and refer to the nonclinical basis for the starting dose. Otherwise summarize pharmacokinetics, safety and efficacy, and marketing experience, with a table of adverse drug reactions across trials.

### Step 5: Reference safety information and guidance for the investigator

Read `references/reference-safety-information.md` and `references/guidance-for-the-investigator.md`. Draft the reference safety list, then the summary of data and guidance: possible risks and adverse reactions, specific tests, observations and precautions, recognition and treatment of adverse reactions and overdose, and the safety margins table.

### Step 6: Summary and front matter

Write the Summary last, preferably within two pages. Then the title page, confidentiality statement (if the sponsor wants one), table of contents, abbreviations and the references at the end of each chapter.

### Step 7: Consistency check and update log

Check that every number in the Summary and the guidance section appears in the body with the same value, that doses match the protocol, and that the reference safety list matches the human and nonclinical sections. For an update, produce the summary of changes against the prior edition.

## Required Output Format

Use `references/output-template.md`. Produce:

1. **The draft IB** in ICH heading order with the title page.
2. **Source and consistency log:** each section's inputs, conflicts found, `[VERIFY]` and `[SPONSOR INPUT REQUIRED]` items.
3. **Summary of changes** (updates only).
4. **Reviewer checklist** for the medically qualified editor and data owners.

Example of a nonclinical entry and a safety-guidance entry:

```
Rat 28-day repeat-dose study: NOAEL 30 mg/kg/day; hepatocellular hypertrophy at
100 mg/kg/day, reversible after a 14-day recovery period [TX-2024-001, Section 8.2, Table 11, p. 71].
Monitoring: liver transaminases at screening, before each dose escalation and at
the intervals set in the protocol (see Protocol Section 9.3).
```

## Troubleshooting

- **No human data.** Write the Effects in Humans section as a first-in-human statement. Draft the reference safety list as a labeled proposal, `[SPONSOR INPUT REQUIRED: RSI framing]`, until the sponsor and regulatory affairs record how it is framed; do not decide that yourself.
- **Nonclinical summary and study reports differ.** Use the study report and amendments, list the conflict, and tell the owner of the summary.
- **Sponsor asks for stopping rules or dose-modification tables in the IB.** Offer a pointer to the protocol section instead; if the sponsor insists, include only what matches the protocol word for word and log it.
- **Existing IB uses different headings.** Keep the sponsor's headings if they cover the same content, and map each to the ICH order in the log.
- **Page target requested.** Length follows the data. State that the guideline sets none, and keep the Summary within two pages.
- **Important new safety information arrives between editions.** It may need to reach investigators and possibly IRBs and regulators before the next revision; flag it to the sponsor rather than waiting for the annual update.

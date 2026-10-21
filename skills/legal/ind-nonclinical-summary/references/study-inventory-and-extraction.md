# Study Inventory, Extraction and Reconciliation

How to build the study inventory, what each extraction card contains, and how to reconcile conflicting values before drafting.

## Contents

- Inventory fields
- Section assignment
- GLP status
- Extraction card
- Reconciliation rules
- Units and exposure basis

## Inventory Fields

One row per report:

| Field | Notes |
|---|---|
| Study or report ID | As printed on the report; never invent one |
| Title | |
| Test article, lot, formulation, salt or form | Needed for comparability across studies |
| Test facility | |
| Test system | Species, strain, sex, age, or cell line and assay system |
| Route, regimen, duration | |
| GLP status | See below |
| Start and completion dates | From the report |
| Amendments | Study director amendments, with date and what changed |
| CTD section | See next table |
| Pivotal or non-pivotal | Pivotal means the definitive GLP studies M3(R2) specifies for the clinical plan |

## Section Assignment

| Study content | CTD section |
|---|---|
| Receptor binding, functional potency, disease-model efficacy | 2.6.2.2 Primary Pharmacodynamics |
| Off-target panels, secondary functional effects | 2.6.2.3 Secondary Pharmacodynamics |
| CNS, cardiovascular (including in vitro IKr/hERG and in vivo QT where relevant) and respiratory studies | 2.6.2.4 Safety Pharmacology |
| Bioanalytical method validation | 2.6.4.2 Methods of Analysis |
| Single and repeat-dose PK, bioavailability | 2.6.4.3 Absorption |
| Tissue distribution, protein binding, placental transfer | 2.6.4.4 Distribution |
| Metabolite profiling, in vitro metabolism, CYP induction and inhibition | 2.6.4.5 Metabolism |
| Mass balance, bile, milk | 2.6.4.6 Excretion |
| Single-dose and repeat-dose toxicity with toxicokinetics | 2.6.6.2, 2.6.6.3 |
| Genotoxicity | 2.6.6.4 |
| Carcinogenicity | 2.6.6.5 |
| Fertility, embryo-fetal, pre- and postnatal, juvenile | 2.6.6.6 |
| Local tolerance | 2.6.6.7 |
| Immunotoxicity, antigenicity, phototoxicity, impurity or metabolite qualification, mechanistic | 2.6.6.8 |

A study that serves two sections (for example, a toxicity study with embedded safety pharmacology endpoints) is listed in both and cross-referenced.

## GLP Status

- Record `GLP` only when the report carries a statement of compliance with 21 CFR Part 58 (or an equivalent regime the report names), and quote the statement's location.
- Record `non-GLP` when the report says so or states exploratory intent.
- Record `not stated` when the report is silent. Do not infer.
- Part 58 defines a covered nonclinical laboratory study as an in vivo or in vitro experiment studied prospectively to determine safety, and excludes basic exploratory studies. The sponsor decides which studies are covered; list every non-GLP study for that decision.
- Record any report item describing circumstances that may have affected data quality or integrity (a final report must describe them) in the issues list.

## Extraction Card

Write one card per study before any drafting. Every value carries its locator `[Study ID, Section, Table, p.]`.

```
Study ID / title:
Test article, lot, formulation:
Test system and group sizes (n per sex per group):
Doses (units as printed), route, regimen, duration, recovery groups:
GLP statement (quote and locator) or "not stated":
Amendments to the final report (date, what changed):
Key results:
  Clinical signs / mortality:
  Body weight, food:
  Clinical pathology (haematology, chemistry, urinalysis):
  Organ weights, gross and microscopic pathology:
  Target organs; reversibility after recovery:
  NOAEL (as stated by the report; do not re-derive) and its basis:
Toxicokinetics: parameter, day, sex, dose, value, unit, locator
Immunogenicity (proteins): incidence, titre, neutralizing, effect on exposure
Deviations that may have affected data (from the report):
Not reported: list every standard parameter the report omits
Conflicts noticed in the report itself:
```

## Reconciliation Rules

Run these before drafting; record each hit in the issues list.

1. **Text versus tables.** Where the narrative and a data table differ, show both values and apply the source ranking in the SKILL ground rules. Never choose silently.
2. **Amendments.** A study director amendment corrects the final report. Use the amended value and cite the amendment.
3. **Sex and day.** Keep sex-specific and day-specific exposure values separate. Do not average unless the report did, and say so.
4. **NOAEL wording.** Use the NOAEL the report states and the basis it gives. If the report gives NOEL, LOAEL or no NOAEL, report that term; do not relabel. Where the report's NOAEL appears to conflict with its own findings, list it as an issue rather than correcting it.
5. **Recovery groups.** Report reversibility separately from main-phase findings.
6. **Formulation and lot.** If the pharmacology, PK and toxicology studies used different formulations or batches, say so in the Brief Summary of 2.6.4 and in the 2.4 comparability or strategy discussion.
7. **Species relevance.** For proteins, record the evidence that each species is pharmacologically relevant (binding, receptor or epitope expression, functional assay). A study in a species with no such evidence is reported but flagged.
8. **Cross-study duplicates.** If two reports describe the same study (for example, a draft and a final), use the final and list the draft as superseded.

## Units and Exposure Basis

- Keep the original unit in the card; add a converted value in the working unit and record the conversion. Typical pairs: ng/mL and ug/mL (divide by 1000); mg/kg and mg/m2 (see `exposure-and-starting-dose.md`).
- Record whether concentrations are total or unbound, in plasma or serum or blood, and for which analyte (parent, metabolite, total antibody). Never compare values across different bases.
- Record the AUC interval (0-24h, 0-t, 0-inf) and the day it was measured.

# IB Structure and Content

The ICH heading order for an Investigator's Brochure, what each section holds, and where each nonclinical section comes from. Source status is in `primary-sources.md`.

## Contents

- Heading order
- Front matter
- Nonclinical studies section
- Effects in humans section
- Mapping to Module 2.6
- Biologics notes
- Length and style

## Heading Order

ICH E6 lists these sections, each with literature references at the end of the chapter. Numbering is the sponsor's choice. The ICH example numbers Summary 2, Introduction 3 and so on, and is only an example.

| Section | Content |
|---|---|
| Table of contents | Numbered hierarchy; abbreviations list is useful |
| Summary | Brief, preferably not over two pages. The significant physical, chemical, pharmaceutical, pharmacological, toxicological, pharmacokinetic, metabolic and clinical information relevant to the stage of development |
| Introduction | Chemical name (and generic and trade names when approved), all active ingredients, pharmacological class and expected position in it, rationale for the research, anticipated indication, and the general approach to evaluating the product |
| Physical, chemical and pharmaceutical properties and formulation | Substance description with structural formula; relevant properties; formulation and excipients, justified if clinically relevant; storage and handling; structural similarities to known compounds |
| Nonclinical studies | See below |
| Effects in humans | See below |
| Summary of data and guidance for the investigator | See `guidance-for-the-investigator.md` |

## Front Matter

- Title page: sponsor name; identity of each investigational product (research number, chemical or generic name, trade name where permitted and wanted); release date; edition number and the edition it supersedes; data cut-off date.
- Confidentiality statement: optional; tells recipients to treat the IB as confidential for the investigator, site staff, regulators and the IRB or IEC.
- Signature page: optional.

## Nonclinical Studies Section

Open with an introduction: results of all relevant nonclinical pharmacology, toxicology, pharmacokinetic and metabolism studies in summary form, with methodology, results and a discussion of relevance to the investigated product and possible unfavourable and unintended effects in humans.

Where known, for each study give: species; number and sex per group; unit dose; dose interval; route; duration of dosing; systemic distribution; duration of post-exposure follow-up; and results (nature and frequency, severity, time to onset, reversibility, duration of effects, dose response). Use tables and listings wherever possible.

Then discuss the most important findings, including dose response, relevance to humans and aspects to be studied in humans. Compare effective and non-toxic doses in the same species (therapeutic index) and relate them to the proposed human dosing. Compare in blood or tissue levels, or human equivalent dose, rather than mg/kg where possible.

Subsections:

1. **Nonclinical pharmacology.** Therapeutic activity (efficacy models, receptor binding, specificity) and safety (pharmacological actions beyond the intended effect), including significant metabolites.
2. **Pharmacokinetics and product metabolism in animals.** All species studied: absorption and local and systemic bioavailability of the product and metabolites, biotransformation and disposition, and the relationship to pharmacological and toxicological findings.
3. **Toxicology.** Headings, where appropriate: single dose; repeated dose; genotoxicity; carcinogenicity; reproductive and developmental toxicity; local tolerance (irritancy, sensitization); other studies. Report the NOAEL and target organs in each species and the reversibility after recovery, as the studies state them.

## Effects in Humans Section

First-in-human: state that no human studies have been conducted and refer to the nonclinical basis for the starting dose.

Otherwise: introduction with a summary of each completed trial where possible and use outside trials such as marketing experience; then

1. Pharmacokinetics and product metabolism in humans: pharmacokinetics, bioavailability (absolute where possible, relative otherwise), population subgroups (sex, age, organ impairment), interactions (product-product, food), other data.
2. Safety and efficacy: safety, pharmacodynamics, efficacy and dose response from prior trials; a tabular summary of adverse drug reactions across trials and indications; differences in patterns across indications or subgroups; the possible risks and adverse reactions anticipated from this product and related products, and precautions or special monitoring.
3. Marketing experience: countries where marketed or approved, significant information from marketed use, and countries where approval was refused or the product withdrawn.

## Mapping to Module 2.6

| IB section | Source in the `ind-nonclinical-summary` output |
|---|---|
| Nonclinical pharmacology | 2.6.2 and its tabulated summary |
| Pharmacokinetics and product metabolism in animals | 2.6.4 |
| Toxicology | 2.6.6 and 2.4 Toxicology (target organs, exposure multiples) |
| Safety margins table | 2.4 exposure-multiple table |

Condense; do not copy. Keep numbers identical and cite the same studies.

## Biologics Notes

- State species relevance for each toxicity species and the evidence for it.
- Report anti-product antibody findings and their effect on exposure and toxicity.
- Record that standard genotoxicity and carcinogenicity bioassays were not conducted, with the reason, rather than omitting the headings.

## Length and Style

- Concise, simple, objective, balanced and non-promotional.
- Content varies with development stage; ICH sets no page target.
- An IB for a marketed product studied for a new use is specific to that use, unless the sponsor documents a rationale for one IB.

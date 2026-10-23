# Modality Pathways

What the primary guidelines expect for each modality, so the drafted Overview tests the package against the right standard. Use it to decide which gaps to flag, not to decide what the sponsor must have done. Status of each statement is recorded in `primary-sources.md`.

## Contents

- Choose the pathway
- Comparison table
- Oncology overlay (patients with advanced cancer)
- Cardiac safety by modality
- Gap flags

## Choose the Pathway

1. Small molecule: use the small-molecule column (ICH M3(R2), S2(R1), S7A, S7B).
2. Therapeutic protein or monoclonal antibody: use the protein column (ICH S6(R1), with M3(R2) deferring to S6 for biotechnology-derived products).
3. Either, if the first-in-human trial is in patients with advanced cancer: apply the oncology overlay (ICH S9) on top.
4. Any other modality: out of scope; say so.

## Comparison Table

| Topic | Small molecule | Therapeutic protein or antibody |
|---|---|---|
| Species for general toxicity | Two mammalian species, one non-rodent; duration equal to or longer than the clinical trial, up to the maximum recommended duration in M3(R2) Table 1 | Relevant species only: one in which the product is pharmacologically active through the receptor or epitope. Normally two relevant species; one may suffice when justified (for example, only one is relevant). Studies in non-relevant species are discouraged |
| Evidence of relevance | Comparability of absorption, distribution, metabolism and excretion across species (FDA starting-dose guidance) | Binding and functional data across species, receptor or epitope distribution |
| Core safety pharmacology | CNS, cardiovascular, respiratory before first human exposure (S7A, S7B); in vivo endpoints may be added to toxicity studies | Evaluated in relevant species; may be integrated into toxicity studies (S6(R1)) |
| Genotoxicity | Gene-mutation assay supports single-dose trials; add a chromosomal-damage assessment for multiple-dose trials; complete battery before Phase II (M3(R2)). Standard battery has two options (S2(R1), small molecules only) | Standard studies not applicable and not needed; studies only where a concern exists (for example, an organic linker) |
| Carcinogenicity | Studies recommended for the indication are conducted to support the marketing application; results go in with a clinical trial only where there is a significant cause for concern, and long clinical duration alone is not one (M3(R2) s.10, with ICH S1A) | Standard bioassays generally inappropriate; product-specific assessment where duration, population or biology raises concern (for example, growth factors, immunosuppressants) |
| Immunogenicity | Not expected | Measure and characterize anti-product antibodies in repeat-dose studies; correlate with PK, PD and toxicity |
| Reproductive toxicity | Studies appropriate to the exposed population (M3(R2) s.11). Men can join Phase I and II before the male fertility study, which is due before large-scale or long-duration trials. Women of childbearing potential: conditions in M3(R2) s.11.3 (for example, precautions against pregnancy and preliminary data from two species for short, limited-size trials); read that section for the sponsor's route | Design per the reproductive provisions of ICH S6(R1) `[VERIFY]`; M3(R2) notes monoclonal antibodies with low embryo-fetal exposure during organogenesis may have developmental studies in Phase III |
| Recovery | Characterize potential reversibility when appropriate (M3(R2) general principles) | Include to judge reversibility; complete recovery is not essential; a recovery period solely to assess immunogenicity is not necessary |
| Starting dose | NOAEL, converted to HED, from the most appropriate species (default most sensitive), divided by a safety factor | HED from the most appropriate species (relevance may override sensitivity); compare with the pharmacologically active dose; MABEL for products with immune agonist properties |

## Oncology Overlay (Patients with Advanced Cancer, ICH S9)

- NOAEL or NOEL studies are not considered essential. Phase I may dose to a maximum tolerated dose and dose-limiting toxicity.
- A recovery study is called for when severe toxicity occurs at about clinical exposure and recovery cannot be predicted scientifically; complete recovery is not essential.
- Stand-alone safety pharmacology studies are not called for; specific concerns go to S7A and S7B studies.
- Genotoxicity studies are not essential to support trials.
- Embryofetal studies are not essential to support trials in patients with advanced cancer.
- Small molecules: general toxicology usually uses rodents and non-rodents; in certain cases one relevant rodent species can be enough. Proteins: follow S6 for species.
- Start dose, common approach for small molecules: 1/10 of the severely toxic dose in 10% of rodents (STD10), or 1/6 of the highest non-severely toxic dose (HNSTD) if the non-rodent is the most appropriate species. HNSTD is the highest dose with no evidence of lethality, life-threatening toxicity or irreversible findings. Convert by body surface area for most small molecules.
- Biopharmaceuticals with immune agonist properties: consider MABEL. HNSTD may be appropriate for other biopharmaceuticals, taking account of binding affinity differences and pharmacology (S9 Q&A).
- Do not frame the package around NOAEL margins when this overlay applies; frame it around STD10, HNSTD, MTD and dose-limiting toxicity as the studies report them.

## Cardiac Safety by Modality

The ICH E14/S7B Q&As (R1) state a framework by modality, and say its principles can be read across modalities with S7A, M3, S6 and S9:

- Monoclonal antibodies and large targeted proteins, and amino acid polymers of naturally occurring amino acids: delayed ventricular repolarization through direct hERG interaction is not likely, so no S7B in vitro hERG assay or in vivo QT assessment is required. Record this as a scientific rationale; do not leave the section blank.
- Small molecules and other modalities that cross the cell membrane and can reach the channel pore: an in vitro hERG assay and an in vivo QT assessment, preferably integrated into the general toxicology study, with qualified alternative assays possible.
- Conjugates: if the moieties separate in the circulation, assess each moiety.
- Regional adoption of the R1 revision is `[VERIFY]`; state which Q&A version the sponsor cited.

## Gap Flags

Flag, do not conclude, when the report set shows any of these:

- Core battery missing for a small molecule before first human exposure.
- A small molecule with only one toxicity species and no justification.
- A protein with toxicity data only in a species with no relevance evidence.
- Repeat-dose duration shorter than the planned clinical duration, with no justification.
- Antibody assay data absent in repeat-dose protein studies.
- Pharmacologically active dose or MABEL data absent for a protein or an immune agonist.
- Genotoxicity battery missing for a multiple-dose small-molecule trial.
- A non-GLP pivotal study without a stated reason.

# Exposure Multiples and Starting-Dose Calculations

How to calculate exposure multiples, the human equivalent dose (HED) and the maximum recommended starting dose (MRSD) without inventing inputs. Every result here is `calculated`, never extracted. Source status is in `primary-sources.md`.

## Contents

- Inputs the sponsor must supply
- Exposure multiples
- HED and MRSD for healthy volunteers
- Conversion table
- Safety factor
- Other pathways
- Calculation ledger entry

## Inputs the Sponsor Must Supply

- Planned first dose and maximum dose, route, regimen, duration, and population.
- Projected human exposure (AUC, Cmax) at the first and maximum dose, the analyte and matrix, and how it was projected.
- Pharmacologically active dose or minimal anticipated biological effect level (MABEL) estimates, where used.

If any input is missing, write `[SPONSOR INPUT REQUIRED]` in the affected cell and list it at the top of the issues. Do not project human exposure yourself.

## Exposure Multiples

1. Choose one basis per comparison: same parameter (AUC over the same interval, or Cmax), same analyte, same matrix, total or unbound for both sides.
2. Take the animal value at the NOAEL (or the dose the pathway uses) from the toxicokinetic data, by sex and by day. Do not average unless the report did.
3. Multiple = animal exposure at the dose divided by projected human exposure at the dose of interest. Compute one multiple at the first dose and one at the maximum dose.
4. Convert units before dividing and record the conversion (for example, ng/mL to ug/mL divide by 1000).
5. Where the report gives no exposure for the dose, write `Not reported in <Study ID>` and leave the multiple blank. A mg/kg comparison is a fallback only when exposure is unavailable, and must be labeled as such.

Table layout:

| Species, sex | Study | Dose (mg/kg/day) | Day | AUC0-24 (ug.h/mL) | Cmax (ng/mL) | Human AUC at first / max dose | Multiple at first / max | Source |
|---|---|---|---|---|---|---|---|---|

## HED and MRSD for Healthy Volunteers

This follows FDA's guidance for initial trials in adult healthy volunteers. It does not address starting doses in patients, endogenous proteins at physiologic levels or prophylactic vaccines.

1. For each relevant toxicity study, take the NOAEL the report states.
2. Convert each NOAEL to an HED. For most systemically administered products, normalize to body surface area: divide the animal dose in mg/kg by the factor in the table below, or multiply by the second factor. For species or weights not listed, HED = animal dose in mg/kg x (animal weight in kg / human weight in kg) to the power 0.33. For listed species at standard weights, use the table, not the formula; the two differ by about 15% for a 0.15 kg rat.
3. Choose one species. The default is the species with the lowest HED (most sensitive). Evidence that another species is more appropriate may override this: differences in absorption, distribution, metabolism or excretion, class experience, or for proteins, expression of the relevant receptor or epitope. State the evidence.
4. Divide that HED by a safety factor to get the MRSD in mg/kg. The result is the upper limit of recommended starting doses; a lower starting dose is always an option.
5. Compare the MRSD with the pharmacologically active dose where one is available. If the pharmacologic HED is lower than the MRSD, consider lowering the starting dose. For products whose toxicity arises from exaggerated pharmacology (for example, vasodilators, anticoagulants, monoclonal antibodies, growth factors), the pharmacologically active dose may be the more sensitive indicator.
6. Scaling by body weight (HED equals NOAEL in mg/kg) needs justification: NOAELs at a similar mg/kg dose across species. Without it, use the surface-area approach.

## Conversion Table (Assumes a 60 kg Human)

| Species | km | Divide animal dose (mg/kg) by | Multiply animal dose (mg/kg) by |
|---|---|---|---|
| Mouse | 3 | 12.3 | 0.08 |
| Hamster | 5 | 7.4 | 0.13 |
| Rat | 6 | 6.2 | 0.16 |
| Ferret | 7 | 5.3 | 0.19 |
| Guinea pig | 8 | 4.6 | 0.22 |
| Rabbit | 12 | 3.1 | 0.32 |
| Dog | 20 | 1.8 | 0.54 |
| Monkey (cynomolgus, rhesus, stumptail) | 12 | 3.1 | 0.32 |
| Marmoset | 6 | 6.2 | 0.16 |
| Squirrel monkey | 7 | 5.3 | 0.19 |
| Baboon | 20 | 1.8 | 0.54 |
| Micro-pig | 27 | 1.4 | 0.73 |
| Mini-pig | 35 | 1.1 | 0.95 |

Human km is 37. mg/kg to mg/m2: multiply by km.

## Safety Factor

- The guidance says to consider a factor of at least 10 as the default. State the factor used and the reason.
- Increase it for safety concerns or design shortcomings in the animal studies.
- A factor below 10 can be justified for well-characterized classes (same route, schedule, duration, similar metabolism and toxicity across species), for toxicities that are easy to monitor, reversible and predictable with a shallow dose-response, or where the NOAEL came from longer exposure than the planned clinical schedule. The toxicology must then be of high quality; list the justification for the reviewer.
- Never state the factor as a fixed rule in the draft.

## Other Pathways

- Therapeutic proteins and immune agonists: add a MABEL estimate and the pharmacologically active dose from the sponsor, and relate the starting dose to whichever is lowest. For a healthy-volunteer start, the EMA first-in-human guideline expects exposure below the pharmacologically active dose unless a robust rationale supports higher.
- Patients with advanced cancer (ICH S9): start dose of 1/10 STD10 in rodents or 1/6 HNSTD in non-rodents, converted by body surface area for most small molecules; do not build the derivation on a NOAEL.
- Where several approaches are shown, say which one the sponsor chose and list the others as comparators.

## Calculation Ledger Entry

Every calculated value appears in the ledger with these fields:

```
Quantity:            HED from rat NOAEL
Formula:             animal dose (mg/kg) / 6.2
Inputs:              NOAEL 30 mg/kg/day [Study ID, Section, Table, p.]; factor 6.2 [conversion table]
Result:              4.8 mg/kg   (calculated)
Rounding:            state the rule used (here, two significant figures)
Basis / assumptions: 60 kg human; body surface area scaling
Reviewer to confirm: species choice, safety factor, human exposure source
```

Illustrative arithmetic only: 30 / 6.2 = 4.84, which rounds to 4.8 mg/kg; with a safety factor of 10 the MRSD would be 0.48 mg/kg.

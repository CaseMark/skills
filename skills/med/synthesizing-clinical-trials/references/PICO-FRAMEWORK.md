# PICO Framework Reference

## Overview

PICO structures clinical questions to enable systematic evidence searching.

| Element | Definition | Examples |
|---------|-----------|----------|
| **P** — Population | Who are the patients? | Adults with type 2 diabetes, children age 5-12 with asthma |
| **I** — Intervention | What is being considered? | Metformin 1000mg daily, CBT therapy, laparoscopic surgery |
| **C** — Comparison | What is the alternative? | Placebo, standard care, open surgery, no treatment |
| **O** — Outcome | What is being measured? | HbA1c reduction, mortality, hospital readmission rate |

## Extended Variants

| Variant | Extra Element | Use When |
|---------|--------------|----------|
| PICO**T** | **T**imeframe | Duration matters (e.g., 6-month outcomes) |
| PICO**S** | **S**tudy type | Limiting to specific designs (e.g., RCTs only) |
| PICO**D** | **D**omain | Specifying clinical setting |

## Constructing Effective PICO Questions

### Good PICO
> **P**: Adults aged 65+ with newly diagnosed atrial fibrillation
> **I**: Direct oral anticoagulants (DOACs) — apixaban, rivarelbaban, edoxaban
> **C**: Warfarin with INR monitoring
> **O**: Ischemic stroke incidence at 2 years

### Weak PICO
> **P**: Elderly patients
> **I**: Blood thinners
> **C**: Other blood thinners
> **O**: Stroke

The weak version lacks specificity needed for a focused search.

## From PICO to Search Strategy

| PICO Element | Search Terms | Boolean |
|-------------|-------------|---------|
| P | "atrial fibrillation" OR "AF" OR "AFib" | AND |
| I | "apixaban" OR "rivaroxaban" OR "DOAC" OR "direct oral anticoagulant" | AND |
| C | "warfarin" OR "vitamin K antagonist" OR "VKA" | AND |
| O | "stroke" OR "cerebrovascular accident" OR "ischemic event" | |

## Common Pitfalls

- **Too broad P**: "patients with heart disease" — narrows nothing
- **Missing C**: Without a comparator, you can't assess relative effectiveness
- **Composite O**: "morbidity and mortality" — better to separate these
- **Ignoring harms**: Include adverse events as a secondary outcome

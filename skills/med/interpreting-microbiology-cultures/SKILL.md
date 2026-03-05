---
name: interpreting-microbiology-cultures
description: Structures microbiology result interpretation with susceptibility patterns and resistance mechanisms. Use when reading culture results, interpreting susceptibility data, or identifying resistance patterns.
tags:
  - analysis
  - pathology
metadata:
  author: casemark
  practice_areas:
    - Pathology
    - Laboratory Medicine
  document_types:
    - Interpretation Report
  skill_modes:
    - Analysis
    - Interpretation
---

# Interpreting Microbiology Cultures

Structures microbiology result interpretation with susceptibility patterns and resistance mechanisms.

## Why This Skill Exists

Microbiology culture interpretation directly determines antibiotic therapy selection, infection control interventions, and public health reporting. Delays in identifying resistant organisms, failure to recognize contamination versus true infection, and incorrect susceptibility reporting contribute to antimicrobial resistance (estimated 35,000+ deaths per year in the US per CDC) and treatment failures. The Clinical and Laboratory Standards Institute (CLSI) M100 document sets annual breakpoint updates for antimicrobial susceptibility testing (AST), and laboratories must apply current breakpoints to ensure therapeutic relevance.

CAP accreditation (Microbiology MIC checklist series) requires compliance with CLSI methodology, documented organism identification verification, and antimicrobial susceptibility reporting standards. CLIA mandates result verification, quality control of media and reagents, and competency assessment for microbiology technologists. State and federal public health regulations require reporting of notifiable organisms (CDC/NNDSS list). This skill ensures systematic interpretation of culture results with appropriate clinical and regulatory context.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **Specimen type** — Blood, urine, respiratory (sputum, BAL, tracheal aspirate), wound/tissue, CSF, stool, sterile body fluid, or other? Default: blood culture.
2. **Collection method** — Proper collection technique documented (e.g., clean-catch midstream, venipuncture, CT-guided aspirate)? Default: assume proper collection.
3. **Clinical context** — Suspected infection site, immunocompromised status, antibiotic history, indwelling devices? Default: not provided; flag [VERIFY].
4. **Time to positivity** — For blood cultures, what was the time to detection? Default: not applicable (non-blood specimen).
5. **Gram stain result** — Was a preliminary Gram stain performed and reported? Default: yes.
6. **Prior cultures** — Previous culture results from this patient? Default: none on file.
7. **Antimicrobial therapy** — Current antibiotics the patient is receiving? Default: unknown; flag [VERIFY].

### Documents to Request

- Culture requisition with specimen type and collection method
- Gram stain result and preliminary report
- Final culture identification and susceptibility report
- Patient medication list (current antibiotics)
- Clinical notes (fever curve, WBC trend, imaging findings)
- Prior microbiology results for trending
- Infection control alerts (MDRO history, isolation status)
- CLSI M100 current edition breakpoint tables

---

## Step 1: Specimen Quality Assessment and Gram Stain Correlation

Assess specimen adequacy before interpreting culture results:

**Sputum quality (Bartlett/Murray-Washington criteria):**

| Grade | WBCs per LPF | Epithelial Cells per LPF | Interpretation |
|---|---|---|---|
| Acceptable | > 25 | < 10 | Lower respiratory origin; culture meaningful |
| Borderline | 10-25 | 10-25 | Interpret with caution |
| Reject | < 10 | > 25 | Oropharyngeal contamination; request recollection |

**Blood culture considerations:**
- Adequate volume: 20-30 mL per set (2 sets recommended per episode)
- Time to positivity: < 12 hours suggests high-grade bacteremia; > 72 hours may indicate contamination or slow-growing organisms
- Number of positive bottles: Multiple positive bottles with the same organism strongly supports true bacteremia

**Gram stain correlation**: The Gram stain should correlate with culture growth. A Gram stain showing gram-positive cocci in clusters with growth of Staphylococcus aureus is concordant. Discordance (e.g., Gram-negative rods on smear but only gram-positive growth) warrants investigation for fastidious organisms, anaerobes, or pretreatment effect.

---

## Step 2: Organism Identification Interpretation

Evaluate the identification result in clinical context:

**True pathogen vs. contamination vs. colonization:**

| Specimen Type | Likely Pathogen | Likely Contaminant | Assessment Approach |
|---|---|---|---|
| Blood | S. aureus, E. coli, Klebsiella, Candida | CoNS (single bottle), Corynebacterium, Cutibacterium | Number of positive sets, time to positivity, clinical correlation |
| Urine | >= 10^5 CFU/mL single organism | Mixed flora, < 10^3 CFU/mL | Colony count, symptom correlation, pyuria |
| Sputum | S. pneumoniae, H. influenzae, MRSA | Normal oral flora | Sputum quality score, predominance on Gram stain |
| Wound | S. aureus, Streptococcus, GNR | Mixed skin flora in superficial swabs | Collection method (tissue > swab), clinical signs |
| CSF | Any organism | CoNS (rare, if shunt present) | Essentially no contamination tolerance |

**Reporting clinically significant vs. insignificant isolates:**
- Report all isolates from normally sterile sites (blood, CSF, joint fluid).
- For respiratory specimens, report predominant organisms consistent with Gram stain morphology.
- For urine, apply quantitative criteria (>= 10^5 CFU/mL or >= 10^3 CFU/mL for catheterized specimens per IDSA guidelines).

---

## Step 3: Antimicrobial Susceptibility Interpretation

Apply current CLSI M100 breakpoints and interpretive criteria:

**CLSI interpretive categories:**

| Category | Definition | Clinical Implication |
|---|---|---|
| S (Susceptible) | MIC at or below susceptible breakpoint | Standard dosing regimen expected to be effective |
| SDD (Susceptible-Dose Dependent) | MIC requires higher-than-standard dosing | Effective only with optimized dosing (renal function-dependent) |
| I (Intermediate) | MIC falls between S and R breakpoints | May be effective at higher doses or concentrated body sites |
| R (Resistant) | MIC above resistant breakpoint | Not expected to be effective at any achievable dose |

**Critical resistance phenotypes to flag:**

| Phenotype | Organism | Detection | Clinical Action |
|---|---|---|---|
| MRSA | S. aureus | Cefoxitin disk/MIC, mecA/mecC PCR | Contact precautions, vancomycin or alternatives |
| ESBL | E. coli, Klebsiella | Ceftriaxone R + confirmatory (CLSI) | Carbapenems preferred; avoid cephalosporins |
| CRE (CPE) | Enterobacterales | Meropenem MIC >= 2, mCIM/eCIM | Infection control alert, ID consult, novel agents |
| VRE | Enterococcus | Vancomycin MIC >= 32 | Contact precautions, linezolid or daptomycin |
| MDR Pseudomonas | P. aeruginosa | Resistance to >= 3 classes | ID consult, combination therapy consideration |
| MDR Acinetobacter | A. baumannii | Resistance to carbapenems | Contact precautions, polymyxins, novel agents |

---

## Step 4: Selective and Cascade Reporting

Apply institutional antibiogram and cascade reporting policies:

- **Cascade (selective) reporting**: Report narrower-spectrum agents first. If the organism is susceptible to a first-line agent (e.g., ampicillin for E. faecalis), do not automatically report broader agents (e.g., vancomycin). Release broader agents only if first-line is resistant.
- **Suppressed agents**: Per CLSI M100 guidelines and institutional policy, suppress certain drug-bug combinations that are intrinsically resistant (e.g., do not report cephalosporins for Enterococcus) or therapeutically inappropriate.
- **Antibiogram integration**: Compare individual isolate susceptibility to institutional antibiogram for patterns. Flag emerging resistance trends.
- **Combination testing**: For MDR organisms, consider synergy testing or checkerboard assays when requested by infectious disease consult.

---

## Step 5: Report Construction and Notification

Structure the final microbiology report:

1. **Specimen**: Type, collection date/time, collection method.
2. **Gram stain**: Morphology description and preliminary interpretation.
3. **Culture result**: Organism identification with method (MALDI-TOF, conventional biochemicals, molecular).
4. **Susceptibility report**: MIC or zone size with CLSI interpretation category. Cascade-reported per policy.
5. **Comments**: Clinical significance assessment, resistance mechanism if identified, ID consult recommendation for MDR organisms.
6. **Critical value notification**: STAT notification for blood culture positivity, CSF culture positivity, and any organism from a normally sterile site.
7. **Public health reporting**: Notify if organism is on CDC/NNDSS notifiable disease list or state-mandated reporting list.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Has specimen adequacy been assessed and documented (sputum quality score, blood culture volume, urine colony count)?
2. Is the organism identification correlated with the Gram stain finding?
3. Are CLSI M100 current-edition breakpoints applied for all susceptibility interpretations?
4. Have critical resistance phenotypes (MRSA, ESBL, CRE, VRE) been flagged with appropriate infection control alerts?
5. Are cascade/selective reporting rules applied per institutional antibiogram policy?

---

## Quality Audit

- [ ] Specimen adequacy assessed per specimen-type criteria
- [ ] Gram stain result documented and correlated with culture growth
- [ ] Organism identification method documented (MALDI-TOF, biochemical, molecular)
- [ ] CLSI M100 current-edition breakpoints applied for AST
- [ ] Intrinsically resistant drug-bug combinations suppressed
- [ ] Cascade/selective reporting applied per institutional policy
- [ ] Critical resistance phenotypes flagged (MRSA, ESBL, CRE, VRE, MDR-PA)
- [ ] Blood culture positivity reported as critical value with STAT notification
- [ ] Time to positivity documented for blood cultures
- [ ] Contamination vs. true pathogen assessment documented
- [ ] Notifiable organisms reported to public health authority
- [ ] QC of media, reagents, and AST panels performed per CLSI/CAP
- [ ] Antibiogram contribution data submitted for annual compilation

---

## Guidelines

- Always assess specimen quality before interpreting culture results; reject inadequate sputum specimens per Murray-Washington criteria and request recollection
- Correlate the Gram stain morphology with culture growth; discordance may indicate fastidious organisms, anaerobes, or prior antibiotic effect requiring additional workup
- Apply current-year CLSI M100 breakpoints; using outdated breakpoints can result in susceptibility miscategorization, particularly for SDD category organisms
- Flag all critical resistance phenotypes (MRSA, ESBL, CRE, VRE) immediately to infection control — do not wait for final susceptibility reporting
- Apply cascade reporting to promote antibiotic stewardship; always report the narrowest-spectrum effective agent first
- For blood cultures, a single positive bottle with a common skin contaminant (CoNS, Corynebacterium, Cutibacterium acnes) in a patient with low clinical suspicion likely represents contamination; require two or more positive sets for significance
- Report notifiable organisms to public health within the mandated timeframe (typically 24 hours for urgent pathogens, 5 business days for routine)
- Review and update the institutional antibiogram annually and use it to guide empiric therapy recommendations in culture comments

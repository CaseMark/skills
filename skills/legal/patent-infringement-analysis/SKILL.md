---
name: patent-infringement-analysis
description: Generates a structured patent infringement analysis report mapping patent claims to accused product features via claim charts. Covers claim construction under Phillips, literal infringement, doctrine of equivalents, validity defenses, and strategic recommendations. Use when analyzing patent infringement, preparing claim charts, evaluating IP litigation risk, or assessing licensing and design-around strategies.
tags:
  - analysis
  - litigation
---

# Patent Infringement Analysis Report

Produces a technical and legal report evaluating whether an accused product or process infringes asserted patent claims, suitable for litigation counsel, in-house teams, or technical experts.

## Prerequisites

1. **Asserted patent(s)** — full specification, claims, file history, prosecution documents, amendments, office action responses
2. **Accused product/process documentation** — specs, manuals, marketing materials, drawings, photos, schematics, source code, reverse engineering reports
3. **Prior art references** — patents, publications, technical standards relevant to the technology
4. **Identification of asserted claims** — which independent and dependent claims are at issue

## Output Structure

### 1. Executive Summary (max 2 pages)

| Element | Content |
|---|---|
| Overall conclusion | Qualified assessment: "strong likelihood," "probable," "unlikely," or "no infringement" |
| Per-claim assessment | Bottom-line for each independent claim and significant dependents |
| Recommendations | Cease activity / seek license / litigate / design-around / post-grant proceedings |
| Critical risks | Willfulness exposure, SOL deadlines, related litigation |
| Key uncertainties | Ambiguous terms, missing technical info, unsettled legal questions |

### 2. Patent Overview

Include:
- **Bibliographic data** — patent number, title, issue/filing/priority dates, inventors, assignee, family members
- **Technical field** — industry, problem addressed, inventive concept, advantages over prior art (draw from spec)
- **Prosecution history highlights** — amendments, narrowing arguments, disclaimer/estoppel events, canceled claims
- **Asserted claims** — list with dependency relationships, rationale for selection
- **Patent status** — litigation history, post-grant proceedings, terminal disclaimers

### 3. Claim Construction

For each disputed term, apply **Phillips v. AWH Corp.** framework:

| Source | Analysis |
|---|---|
| Claim language | Ordinary meaning to POSITA; context within claim and other claims |
| Specification | Explicit definitions, "as used herein" statements, consistent usage, lexicography |
| Prosecution history | Amendments to overcome prior art, distinguishing arguments, disclaimer/estoppel |
| Claim differentiation | Presume different claims have different scope; not a hard rule |
| Extrinsic evidence | Expert testimony, dictionaries, treatises — less weight than intrinsic |

Present as table:

| Claim Term | Proposed Construction | Support (cite col:ln or prosecution doc + page) |
|---|---|---|

**Special considerations:**
- Flag ambiguous terms with alternative constructions and impact on infringement outcome
- For **§ 112(f) means-plus-function** limitations: identify claimed function → corresponding structure in spec → equivalents

### 4. Accused Product Description

- Overview: product name, model, purpose, market, high-level operation
- Feature-by-feature description paralleling claim structure
- Cite evidence precisely: document title, page/section, figure number, code file:line
- Note multiple versions/configurations and which are analyzed
- Identify non-observable features (algorithms, internal logic) requiring further investigation
- Flag information gaps and recommend discovery/testing to fill them

### 5. Element-by-Element Infringement Analysis

For each asserted claim, produce a **claim chart**:

| # | Claim Limitation (as construed) | Accused Product Feature (with evidence citation) | Literal? | DOE? |
|---|---|---|---|---|

**Literal infringement analysis:**
- All-elements rule: every limitation must be met
- Cite specific evidence for each correspondence
- Avoid conclusory statements — explain *why* a feature meets the limitation

**Doctrine of equivalents (for limitations not literally met):**
- Apply function-way-result test OR insubstantial differences test
- Check limitations on DOE:

| DOE Limitation | Test |
|---|---|
| Prosecution history estoppel | Did applicant narrow claim by amendment? Presumption of surrender; rebuttable per Festo |
| Vitiation | Would DOE eliminate the limitation entirely? |
| Dedication to public | Disclosed in spec but not claimed? Johnson & Johnston |
| All-limitations rule | Apply DOE per-element, not to invention as a whole |

**Infringement theories (as applicable):**
- **Direct** — § 271(a): single entity performs all limitations
- **Inducement** — § 271(b): active inducement + knowledge + specific intent
- **Contributory** — § 271(c): material component + no substantial non-infringing uses + knowledge

**Per-claim conclusion:** State infringement likelihood with qualification and basis.

### 6. Validity Considerations

Patents presumed valid (§ 282); invalidity requires clear and convincing evidence (litigation) or preponderance (PTAB).

| Defense | Analysis Framework |
|---|---|
| **Anticipation (§ 102)** | Single reference disclosing every limitation; element-by-element comparison; check statutory bars |
| **Obviousness (§ 103)** | Graham factors: scope of prior art, differences, POSITA level, secondary considerations (commercial success, long-felt need, failure of others, copying) |
| **Subject matter eligibility (§ 101)** | Alice/Mayo two-step: directed to abstract idea/natural phenomenon? → inventive concept? |
| **§ 112 defenses** | Written description, enablement, definiteness |

Flag uncited prior art not before the examiner (strong IPR candidates).

### 7. Defenses, Risks, and Strategy

**Equitable defenses:**
- Laches — unreasonable delay + prejudice
- Equitable estoppel — misleading conduct + reliance + detriment
- Implied license — conduct, prior dealings, authorized purchase
- Patent exhaustion / first sale
- Inequitable conduct — materiality + intent to deceive (clear and convincing)

**Damages assessment:**

| Factor | Analysis |
|---|---|
| Lost profits | Panduit: demand, absence of substitutes, capability, quantifiable profit |
| Reasonable royalty | Georgia-Pacific factors; hypothetical negotiation |
| Apportionment | Entire market value rule applicability; isolate patented feature value |
| Marking (§ 287) | Did patent owner mark products? Pre-notice damages at risk |
| Enhanced damages | Willfulness risk; consider opinion of counsel (not required post-Knorr-Bremse but valuable) |

**Strategic considerations:**
- Litigation cost/timeline estimate (typically $2M-5M+ through trial, 2-3 years)
- Design-around feasibility: engineering effort, cost, timeline, risk of other patents
- Licensing: reasonable royalty range based on comparables
- IPR timing: one-year deadline post-complaint service
- Forum selection: venue under TC Heartland; relative advantages
- Business factors: revenue at stake, competitive impact, relationship considerations

### 8. Conclusion and Recommendations

- Synthesize per-claim infringement likelihood integrating construction + analysis + validity
- Candid strengths/weaknesses assessment
- Prioritized next steps by urgency and cost-effectiveness
- Information gaps requiring further investigation (reverse engineering, expert analysis, prior art search, discovery)
- Time-sensitive actions: cease activity, document preservation, opinion of counsel, IPR filing deadlines

## Guidelines

- Maintain neutral, analytical tone acknowledging both strengths and weaknesses
- Cite all evidence precisely: patent col:ln, prosecution doc date + page, product doc title + section, cases in Bluebook format
- Use `[VERIFY]` for any legal citation not confirmed from source materials
- Distinguish between what is known from evidence and what requires further investigation
- Do not overstate confidence — qualify assessments based on evidence strength
- Address both legal and business dimensions in recommendations
- For means-plus-function claims, always identify structure + equivalents (narrower than general DOE)
- Flag willfulness risk early if accused infringer has knowledge of patent
- Target report length: 20-50 pages depending on complexity and number of claims

---
name: answer-with-invalidity-contentions
description: Drafts a defendant's Answer with Invalidity Contentions in response to a U.S. patent infringement complaint. Covers FRCP 8 admissions/denials, affirmative defenses, and Patent Local Rule 3-3 invalidity contentions with claim charts under 35 U.S.C. §§ 101, 102, 103, and 112. Use during the pleadings phase of U.S. federal patent litigation when representing a defendant responding to a patent infringement suit, asserting prior art, anticipation, obviousness, written description, enablement, or indefiniteness defenses.
tags:
  - drafting
  - litigation
  - pleading
---

# Answer with Invalidity Contentions

Drafts a patent defendant's combined answer and Patent Local Rule 3-3 invalidity contentions, responding to each complaint allegation while establishing a comprehensive invalidity record for trial.

## Prerequisites

1. **Complaint** — all numbered paragraphs requiring response
2. **Asserted patent(s)** — specification, claims, and prosecution history
3. **Identified prior art** — patents, publications, products, or public uses with dates
4. **Jurisdiction** — identify district court to apply correct local patent rules (PLR 3-3 or equivalent)
5. **Effective filing date** — determine pre-AIA vs. AIA § 102 framework (pre-AIA if filing date < March 16, 2013)
6. **Accused product/method details** — for non-infringement admissions and denials

## Output Structure

### 1. Caption & Introduction
- Full party names as in complaint; civil action number; division
- Title: `DEFENDANT'S ANSWER AND INVALIDITY CONTENTIONS`
- Jury demand if not previously filed (FRCP 38)
- Opening paragraph: defendant denies infringement of any valid, enforceable claim; asserts all claims invalid

---

### 2. Admissions and Denials (FRCP 8(b))

Respond paragraph-by-paragraph, mirroring complaint numbering.

| Response Type | When to Use | Example Language |
|---|---|---|
| **Admit** | Objectively verifiable facts (jurisdiction, patent issuance, inventor identity) | "Defendant admits that U.S. Patent No. X was issued on [date]." |
| **Admit in part / Deny in part** | Allegations mixing fact and legal conclusion | "Defendant admits it manufactures [product] but denies that product infringes any valid claim." |
| **Lack of knowledge** (FRCP 8(b)(5)) | Matters peculiarly within plaintiff's knowledge | "Defendant lacks sufficient knowledge to admit or deny; this operates as a denial." |
| **Deny** | False factual allegations and all legal conclusions | "Defendant denies." |

- Address each sub-part of compound paragraphs individually
- Close section: "All allegations not expressly admitted are denied." (FRCP 8(b)(6) — unanswered allegations are deemed admitted)

---

### 3. Affirmative Defenses

Number each defense separately. Apply *Twombly/Iqbal* plausibility standard with brief factual predicates.

| # | Defense | Key Language |
|---|---|---|
| 1 | Non-infringement | No literal infringement; no infringement under doctrine of equivalents |
| 2 | Invalidity — §§ 101, 102, 103, 112 | Claim charts in § 5 below; all grounds pled in the alternative |
| 3 | Unenforceability — Inequitable conduct | Material misrepresentation/omission to USPTO; particularity per FRCP 9(b) reserved pending discovery |
| 4 | Prosecution laches / Equitable estoppel | If prosecution history supports delay-based defense |
| 5 | License / Exhaustion / Implied license | If authorized sale or course of dealing supports |
| 6 | Failure to state a claim | If complaint omits which claims are asserted, literal vs. DOE, or indirect infringement specifics |
| 7 | Statute of limitations | 35 U.S.C. § 286 (6-year bar) |
| 8 | Unclean hands / Waiver / Estoppel | As facts support |

> **Note:** Defenses not raised in the answer may be waived under FRCP 8(c). Err toward inclusion for any colorable basis.

---

### 4. Counterclaims (if applicable)
- Declaratory judgment of non-infringement (28 U.S.C. § 2201)
- Declaratory judgment of invalidity
- State jurisdictional basis separately from original complaint

---

### 5. Invalidity Contentions

Organized by statutory ground. Each contention must include: (a) reference identification, (b) prior art qualification, (c) claim chart.

#### Prior Art Reference Header Block
```
Reference: [Title], [All Authors/Inventors], [Publication/Issue Date],
           [Publisher/Assignee], [Patent No. / DOI / Pub. No.]
Prior Art Basis: [AIA § 102(a)(1)/(a)(2) | Pre-AIA § 102(a)/(b)/(e)/(g)]
```

---

#### § 102 — Anticipation Claim Charts

One chart per reference per claim. All limitations must be mapped.

| Claim Limitation | Prior Art Disclosure (cite col:line or pg:¶) | Analysis |
|---|---|---|
| [Preamble] | [Reference p. X, ¶ Y] | [Why this discloses the limitation] |
| [Element 1a] | [Reference col. 3:12–25] | [Mapping explanation] |
| [Element 1b] | … | … |

- If reference is a patent: presumed enabling
- If NPL: address *In re Wands* enablement factors (quantity of experimentation, working examples, state of art, predictability, claim breadth)
- For disputed claim terms: show anticipation under any reasonable construction

---

#### § 103 — Obviousness Claim Charts

Apply *Graham v. John Deere Co.*, 383 U.S. 1 (1966):

1. **Scope and content of prior art** — identify primary + secondary references
2. **Differences between art and claims** — which limitations require combination
3. **Level of ordinary skill** — define POSITA (education + experience in field)
4. **Objective indicia** — preemptively address secondary considerations

Motivation to combine (*KSR Int'l Co. v. Teleflex Inc.*, 550 U.S. 398 (2007)):
- Explicit suggestion in references
- Problem-solution obviousness
- Finite number of identified, predictable solutions ("obvious to try")
- Known elements combined according to established functions

| Claim Limitation | Primary Ref. (cite) | Secondary Ref. (cite) | Rationale to Combine |
|---|---|---|---|
| [Element 1a] | Ref. A, col. 2:10 | — | Taught by Ref. A alone |
| [Element 1b] | — | Ref. B, p. 5 | POSITA would combine: [specific motivation] |

**Secondary considerations rebuttal checklist:**
- [ ] Commercial success → attributable to non-claimed features/marketing
- [ ] Long-felt need → prior art already suggested solution
- [ ] Failure of others → lack of motivation, not impossibility
- [ ] Unexpected results → predictable to POSITA

---

#### § 112 Contentions

| Ground | Standard | What to Identify |
|---|---|---|
| **§ 112(a) Written Description** | Inventor possessed full claim scope at filing | Broad claim terms unsupported by narrow-only spec embodiments |
| **§ 112(a) Enablement** | No undue experimentation (*In re Wands*) | Apply 8 Wands factors; focus on claim breadth vs. spec disclosure |
| **§ 112(b) Indefiniteness** | Not reasonably certain to POSITA (*Nautilus, Inc. v. Biosig Instruments*, 572 U.S. 898 (2014)) | Purely subjective terms, relative terms without reference, functional language without bounds |
| **§ 112(f) Means-plus-function** | Spec must disclose corresponding structure | Identify nonce words ("means," "mechanism," "unit"); show missing structure |

---

#### § 101 — Patent-Eligible Subject Matter (if applicable)
Apply *Alice/Mayo* two-step:
1. Directed to abstract idea / law of nature / natural phenomenon?
2. Inventive concept beyond routine/conventional activity?

---

### 6. Prayer for Relief

- Judgment: no infringement (literal or DOE) of any valid, enforceable claim
- Judgment: all asserted claims invalid under §§ 101, 102, 103, 112
- Judgment: patent unenforceable (if inequitable conduct pled)
- Dismissal with prejudice; costs and expenses
- Attorneys' fees under 35 U.S.C. § 285 (exceptional case)
- Declaratory relief (non-infringement, invalidity)
- Such other relief as the Court deems just and proper

---

### 7. Signature Block (FRCP 11)
```
[Attorney Name], Bar No. [X]
[Firm Name]
[Address] | [Phone] | [Fax] | [Email]
Attorney for Defendant [Full Legal Name]
```
Check local rules: some jurisdictions require corporate verification signed under penalty of perjury.

---

## Guidelines

- **Completeness is mandatory**: Federal Circuit may preclude invalidity theories not in initial contentions; omissions at PLR 3-3 stage can be fatal at trial
- **Simultaneous production**: Prior art references must be produced to plaintiff concurrently with service of contentions (unless publicly available)
- **Page limits**: Most districts cap invalidity contentions at 35–50 pages; check local rules before finalizing
- **Pre-AIA vs. AIA**: Confirm effective filing date before applying § 102 framework; pre-AIA subsections (a)/(b)/(e)/(g) differ materially from AIA § 102(a)(1)/(a)(2)
- **Internal consistency**: Admitted facts in §2 must not contradict factual predicates in §3 or §5
- **Verify all citations**: Confirm statute versions, case holdings, and PLR rule numbers for the specific district [VERIFY local PLR numbering if not PLR 3-3]
- **Jurisdiction**: U.S. federal courts only; ITC proceedings have different procedural rules

---
name: animal-law-case-summary
description: >
  Produces litigation-grade case summaries for animal law disputes covering
  cruelty/neglect prosecutions, ownership/custody, dangerous animal designations,
  veterinary malpractice, and service/assistance animal accommodations. Builds
  exhibit-cited factual timelines, maps evidence to statutory elements, evaluates
  expert and veterinary evidence, and assesses remedies with jurisdiction-specific
  legal research. Use when summarizing animal law cases, analyzing animal cruelty
  charges, pet custody disputes, dangerous dog hearings, veterinary malpractice
  claims, or assistance animal accommodation matters. Also trigger when the user
  mentions animal forfeiture, bite liability, wildlife possession, or asks for
  help understanding an animal-related court filing.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Animal Law Case Summary

## Why This Skill Exists

Animal law disputes span criminal, civil, administrative, and regulatory forums — each with distinct burdens of proof, remedies, and deadlines that are easy to conflate. Dangerous dog appeal windows can be as short as 5 days, forfeiture bond deadlines are strict, and the animal's legal classification (property, property-plus, or best-interest standard) controls standing, damages, and available relief. A case summary that fails to surface these distinctions or collapses allegations into findings creates real malpractice risk. This skill produces a structured, evidence-grounded summary that connects record citations to legal elements and realistic remedies across the full spectrum of animal law.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Jurisdiction** — state, county, and forum (state/federal/administrative)
2. **Procedural posture** — pre-suit, pleadings, TRO/PI, discovery, SJ, trial, sentencing, appeal
3. **Parties and animal identification** — species, breed, microchip/license numbers, current custody
4. **Core record** — varies by matter type (see minimum record table below)
5. **Intended audience** — attorney work product, client-facing, or public/educational
6. **Relief sought**

### Minimum Record by Matter Type

| Matter Type | Required Documents |
|---|---|
| **Civil litigation** | Complaint/petition + exhibits, answer/counterclaims, TRO/PI papers, court orders, key discovery, depositions/declarations, expert reports, scheduling order |
| **Criminal cruelty** | Charging instrument, probable cause affidavit, incident reports/body cam, chain-of-custody docs, ACO/shelter logs, veterinary/necropsy reports, diversion conditions |
| **Service/assistance animal** | Lease/HOA rules/accommodation policy, accommodation request + correspondence, verification documents, incident reports, internal decision records |
| **Veterinary malpractice** | Complete vet records (all providers), expert opinions on standard of care, purchase/adoption docs, loss documentation |

**If the user doesn't respond**, apply and clearly label these defaults: attorney work product audience; procedural posture as stated or inferred from documents; all matter-type classifications that appear applicable. Mark content based on user description as "[VERIFY]."

---

## Step 1: Classify and Lock Procedural Posture

Classify into one or more archetypes:

- Criminal cruelty/neglect
- Civil forfeiture/impound challenge
- Dangerous animal designation
- Ownership/title dispute (replevin, conversion, declaratory relief)
- Veterinary malpractice / consumer protection
- Landlord-tenant/HOA pet dispute
- Service animal (ADA Title III) / assistance animal (FHA) accommodation
- Wildlife/exotics possession and permitting
- Agricultural animal welfare enforcement
- Animal-related torts (bite, nuisance, premises liability)

Write a **caption block**: court/agency, case number, judge/ALJ, filing date, next date.

**Critical checks:**
- Do not collapse allegations into findings
- Identify current animal custody/placement
- Surface all deadlines — dangerous dog appeals can be 5–10 days [VERIFY]
- Check for jurisdiction-specific "best interest" statutes (e.g., CA Fam. Code § 2605) [VERIFY]

---

## Step 2: Build Record-Grounded Factual Timeline

Chronological timeline with exhibit-level citations. For each event:

| Field | Requirement |
|---|---|
| Date/time | Exact when available |
| Actor | Who observed or acted |
| Source | Document name + pinpoint cite (page, ¶, Bates) |
| Disputes | Note conflicting accounts |

Use neutral, observable descriptions (body condition scores, environmental conditions — not conclusory characterizations). Track both **chain of title** (ownership documentation) and **chain of care** (daily maintenance, medical oversight, bonding history).

Include exculpatory facts the opposing side will highlight.

---

## Step 3: Map Claims/Charges to Elements and Evidence

For each claim, charge, or violation:

| Component | Detail |
|---|---|
| **Legal standard** | Statute + elements |
| **Burden** | BRD (criminal), preponderance (most civil), clear & convincing (some injunctive) [VERIFY] |
| **Key disputed elements** | Identify the element most likely to be contested |
| **Supporting evidence** | Exhibits mapped to each element |
| **Weaknesses** | Evidence undermining or gaps |
| **Anticipated defenses** | At least two opposition attack vectors |

**Jurisdiction-specific element checks:**
- Cruelty: identify mens rea requirement (intent/recklessness/negligence/strict liability) + statutory exemptions (veterinary practice, agriculture, hunting, research)
- Dog bite: strict liability vs. negligence; provocation/trespass/assumption-of-risk defenses
- Accommodation: separate ADA "service animal" (task-trained dog only, 28 C.F.R. § 36.104) from FHA "assistance animal" (broader, 24 C.F.R. § 100.204) — never conflate

---

## Step 4: Research and Verify Governing Law

**Anti-hallucination protocol:** Every cited authority must be verified via research or marked [VERIFY].

Key federal frameworks:

| Framework | Citation | Key Provision |
|---|---|---|
| Animal Welfare Act | 7 U.S.C. § 2131 et seq. | Federal animal welfare standards |
| Endangered Species Act | 16 U.S.C. § 1531 et seq. | Protected species |
| ADA Title III (service animals) | 28 C.F.R. § 36.104, § 36.302(c) | Task-trained dogs only |
| FHA (assistance animals) | 24 C.F.R. § 100.204; HUD FHEO-2020-01 | Broader; includes ESAs |
| ACAA (air travel) | 14 C.F.R. Part 382 | Now aligned with ADA definitions [VERIFY] |

For state/local law: locate exact cruelty statute, dangerous dog statute, pet custody statute (if any), and municipal ordinances. Confirm text and effective dates — municipal codes change frequently.

For each authority: short parenthetical + verification URL. Use Bluebook format if requested.

---

## Step 5: Analyze Evidence Quality

Evaluate each expert/professional witness:

| Factor | Assessment |
|---|---|
| Qualifications | As stated in record |
| Methods | Peer-reviewed or subjective? |
| Admissibility | Daubert (federal/most states) or Frye [VERIFY for jurisdiction]; FRE 702 |
| Contested assumptions | Alternative etiologies, incomplete record review |

**Evidence-specific checks:**
- Veterinary opinions: did expert review full prior history, diagnostics, treatment records?
- Digital evidence (texts, social media, adoption listings): authenticity, metadata, completeness
- Photographs: metadata, photographer identity, fair depiction
- Physical evidence/necropsy: chain-of-custody issues
- Lay witness observations: distinguish from medical conclusions
- Vet malpractice: identify locality-specific standard of care

---

## Step 6: Remedies, Damages, and Settlement Posture

Map each available remedy to its legal mechanism:

| Remedy Category | Considerations |
|---|---|
| **Ownership** | Replevin/claim-and-delivery, conversion damages, injunctive relief |
| **Criminal** | Penalties, animal disposition orders, cost-of-care reimbursement (state-specific) [VERIFY], ownership bans |
| **Dangerous dog** | Euthanasia mandatory vs. alternatives (behavioral requirements, muzzling, insurance, confinement)? Stay pending appeal? [VERIFY] |
| **Accommodation** | Injunctive relief, damages, fees |
| **Damages** | Market value only or intrinsic/companionship value? Statutory/punitive damages? Attorney's fees? [VERIFY for jurisdiction] |
| **Collateral** | Housing, professional licenses, immigration |

Address bond/forfeiture deadlines and settlement leverage tied to animal's current placement.

---

## Step 7: Draft Final Summary

Use these sections:

1. **Overview** — 2–3 sentence case description
2. **Parties and Animals** — identification, relationships, current custody
3. **Procedural Posture** — caption block + status
4. **Key Facts (Timeline)** — exhibit-cited chronology
5. **Claims/Charges and Governing Law** — element mapping
6. **Evidence Strengths and Weaknesses** — candid assessment
7. **Key Disputes** — contested issues
8. **Remedies and Risk Assessment** — realistic outcomes
9. **Next Steps and Deadlines** — action items with dates
10. **Key Takeaways** — non-advocacy, action-oriented paragraph

State the animal's legal status in the jurisdiction explicitly (property, property-plus, best-interest standard).

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial summary, ask:

1. Does this match the right case, parties, and procedural posture?
2. Are there record documents I should incorporate that weren't provided?
3. Should I expand any section (e.g., deeper remedies analysis, expert evidence critique, timeline detail)?
4. Who is the final audience, and should privilege markings or redactions be adjusted?

---

## Quality Audit

- Every factual assertion traceable to a record cite or labeled as assumption/[VERIFY]
- Allegations distinguished from findings throughout — no conclusory characterizations
- All deadlines surfaced with date and uncertainty flagged
- Element mapping complete for each claim/charge
- Evidence quality analysis covers all expert/professional witnesses
- At least two opposition attack vectors identified per claim
- Animal's legal classification stated explicitly
- Remedies tied to legal mechanisms with jurisdiction verification
- Chain of title and chain of care both tracked
- No invented case citations — every authority verified or marked [VERIFY]
- ADA service animal vs. FHA assistance animal never conflated

---

## Guidelines

- **Neutrality**: distinguish allegations vs. findings vs. stipulations vs. inference throughout
- **Adversarial resilience**: identify top 3 vulnerabilities in client's position candidly; identify at least 2 opposition attack vectors on standing/ownership/key elements
- **Citation integrity**: every material factual assertion traceable to a record cite; every legal authority verified or marked [VERIFY]
- **Audience calibration**: adjust tone, privilege handling, and strategic candor based on identified audience
- **Scope**: this is a case summary — not a memorandum, motion, demand letter, or press statement
- **Privilege**: label attorney work product appropriately; redact sensitive details (mental health, addresses, microchip numbers) in client-facing versions
- **Conflicts**: flag if a party (e.g., nonprofit/shelter) has dual roles as both representative and witness
- **Defamation risk**: stick to record-supported facts; caution against publication without counsel review
- **Deadline sensitivity**: animal law deadlines can be very short (5–10 days for dangerous dog appeals); always surface and flag deadline uncertainty
- **Property status**: always state the animal's legal classification in the jurisdiction — this affects standing, remedies, and damages

**Required disclaimer on every output:**

> THIS SUMMARY REQUIRES INDEPENDENT ATTORNEY VERIFICATION OF ALL CITATIONS, LOCAL CODES, AND FACTUAL ASSERTIONS, AND DOES NOT CONSTITUTE LEGAL ADVICE.

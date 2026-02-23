---
name: counterclaim-crossclaim
description: Drafts court-ready counterclaims and crossclaims for commercial litigation. Analyzes case documents to build factual timelines, identifies compulsory vs. permissive counterclaim requirements, ensures procedural compliance with federal and state rules, and structures causes of action with proper element pleading. Use when a defendant needs to assert affirmative claims against the plaintiff or crossclaims against co-defendants during the pleadings phase.
tags:
  - drafting
  - litigation
  - pleading
---

# Counterclaim & Crossclaim

Drafts a comprehensive counterclaim and/or crossclaim pleading that asserts the defendant's affirmative claims against the plaintiff or co-defendants, satisfying all procedural and substantive pleading requirements.

## Prerequisites

1. **Original complaint** — full text with case caption, case number, court, and filing date
2. **Case documents** — contracts, correspondence, invoices, emails, expert reports, photographs, and other evidence
3. **Party information** — names, roles, addresses, and relationships among all parties (including co-defendants for crossclaims)
4. **Jurisdictional details** — court, applicable rules of civil procedure, local rules, and formatting requirements
5. **Relevant legal authority** — statutes, regulations, and case law supporting each intended cause of action

## Output Structure

### Phase 1: Document Review & Fact Extraction

| Task | Details |
|------|---------|
| Extract case identifiers | Court name, caption, case number, all party designations |
| Build chronological timeline | Contracts formed → performance due → breaches → damages → communications → plaintiff's wrongful conduct |
| Identify counterclaim targets | Claims against plaintiff from same transaction/occurrence (compulsory) or related matters (permissive) |
| Identify crossclaim targets | Co-defendants liable under contribution, indemnification, or independent theories |
| Catalog damages evidence | Specific amounts, dates incurred, causation chain, continuing damages |

### Phase 2: Procedural Compliance

- [ ] Determine compulsory vs. permissive counterclaim status (FRCP 13(a)/(b) or state equivalent)
- [ ] Confirm crossclaim arises from same transaction/occurrence or common questions (FRCP 13(g) or state equivalent)
- [ ] Verify statute of limitations for each cause of action
- [ ] Check jurisdictional basis: supplemental jurisdiction for counterclaims; independent or supplemental for crossclaims
- [ ] Confirm local rules: caption format, margins, font, spacing, page limits, paragraph numbering, e-filing requirements
- [ ] Determine if verification is required (party vs. attorney verification)
- [ ] Check heightened pleading requirements (e.g., FRCP 9(b) for fraud — who, what, when, where, how)

### Phase 3: Document Assembly

```
CAPTION
  — Mirror original complaint format
  — Add new designations: Counterclaimant, Counter-Defendant, Cross-Claimant, Cross-Defendant
  — Title: "COUNTERCLAIM AND CROSSCLAIM" (or separate documents if local rules require)

INTRODUCTORY STATEMENT
  — Identify filing party and capacity
  — Cite authorizing rule (FRCP 13 / state equivalent)
  — State compulsory or permissive nature
  — For crossclaims: identify co-defendant targets and legal basis

JURISDICTIONAL ALLEGATIONS
  — Subject matter jurisdiction (same basis as complaint or independent)
  — Supplemental jurisdiction if applicable (28 U.S.C. § 1367) [VERIFY]
  — Amount in controversy
  — Venue

PARTIES
  — Full identification with roles in underlying transaction
  — For crossclaim defendants: describe relationship creating liability

FACTUAL ALLEGATIONS (numbered paragraphs)
  1. Incorporate by reference admissions from original complaint
  2. Deny/qualify inaccurate allegations with specificity
  3. Present new facts chronologically supporting affirmative claims
  4. Allege damages with specificity: nature, timing, causation, amount

CAUSES OF ACTION (separately numbered counts)
  Format: "COUNT [N]: [Legal Theory] ([Counterclaim/Crossclaim] Against [Party])"
  Each count must:
    — Incorporate relevant factual paragraphs by reference
    — State and satisfy each element of the claim
    — Cite controlling authority (statutes + leading cases)
    — For contribution: allege cross-defendant's fault percentage
    — For contractual indemnity: quote indemnification clause
    — For common law indemnity: allege relationship creating obligation

PRAYER FOR RELIEF
  — Compensatory damages (specific amount or "to be proven at trial")
  — Punitive damages (if authorized; check jurisdiction-specific pleading rules)
  — Injunctive/declaratory relief (draft with specificity for court order)
  — Attorney's fees and costs (cite contractual or statutory basis)
  — Pre/post-judgment interest (cite applicable rate)
  — Catch-all: "such other and further relief as the Court deems just and proper"
  — Separate subsections for counterclaim vs. crossclaim relief

VERIFICATION (if required)
  — Party declaration under penalty of perjury
  — "True of own knowledge except on information and belief"

SIGNATURE BLOCK
  — Attorney name, bar number, firm, address, phone, fax, email
  — "Attorney for Defendant/Counterclaimant/Cross-Claimant [Name]"

CERTIFICATE OF SERVICE
  — All parties/counsel, addresses, method, date
```

### Cause of Action Element Checklist

| Claim Type | Required Elements |
|------------|-------------------|
| Breach of Contract | Formation → terms → plaintiff's performance → defendant's breach → causation → damages |
| Fraud/Misrepresentation | False statement → materiality → scienter → reliance → causation → damages (plead with particularity) |
| Contribution | Common liability → cross-defendant's proportionate fault → right to apportion |
| Contractual Indemnity | Indemnification clause → triggering event → covered claims → proper notice |
| Common Law Indemnity | Special relationship → passive vs. active fault → right to shift liability |
| Unjust Enrichment | Benefit conferred → defendant's knowledge → inequity of retention |

## Guidelines

- **Compulsory counterclaim rule**: Failure to assert a compulsory counterclaim typically results in waiver — flag any potentially compulsory claims to the attorney
- **Alternative pleading**: Permitted under FRCP 8(d)(2); label clearly as "in the alternative" without conceding primary theory
- **Tone**: Professional and persuasive; avoid inflammatory language
- **Consistency**: Party names, dates, amounts, and contract references must match source documents exactly
- **Cross-references**: Verify all internal paragraph and exhibit references are accurate
- **Exhibits**: Attach referenced contracts and key documents; ensure exhibit labels match references in text
- **Relation back**: Counterclaims generally relate back to the original complaint filing date for limitations purposes, but verify jurisdiction-specific rules
- **All citations must be verified** — mark any uncertain citation with `[VERIFY]`
- **Do not fabricate facts** — plead only from provided case documents

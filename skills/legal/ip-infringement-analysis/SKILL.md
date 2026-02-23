---
name: ip-infringement-analysis
description: Conducts comprehensive IP infringement analysis across patents, trademarks, copyrights, and trade secrets. Performs claim-by-claim patent comparisons, likelihood-of-confusion trademark tests, substantial similarity copyright assessments, and trade secret misappropriation evaluations. Use for infringement opinions, pre-filing assessments, cease-and-desist support, licensing disputes, or settlement valuation in IP litigation.
tags:
  - analysis
  - litigation
---

# IP Infringement Analysis

Produces a structured infringement memorandum evaluating whether use of protected IP constitutes actionable infringement, with element-by-element analysis, defense assessment, and remedies quantification.

## Prerequisites

1. **IP registrations/filings** — patents (with claims), trademark registrations, copyright registrations, or trade secret identification documents
2. **Accused instrumentality** — product specs, screenshots, source code, marketing materials, or service descriptions for the allegedly infringing product/activity
3. **Prosecution history** (patents) — file wrapper, claim amendments, examiner rejections
4. **Prior art or third-party references** — if available
5. **Relevant agreements** — licenses, NDAs, employment/non-compete agreements, assignment records
6. **Correspondence** — cease-and-desist letters, licensing negotiations, any admissions
7. **Jurisdiction and procedural posture** — where filed or anticipated, statute of limitations status

## Output Structure

### Section 1: IP Rights Identification

| Field | Detail |
|-------|--------|
| IP Type | Patent / Trademark / Copyright / Trade Secret |
| Registration/Application No. | |
| Filing/Priority Date | |
| Owner/Claimant | |
| Key Claims/Mark/Work Description | |
| Status (active, expired, pending) | |

### Section 2: Accused Activity

| Field | Detail |
|-------|--------|
| Accused party | |
| Product/service/activity | |
| Date of first use | |
| Geographic scope | |
| Commercial context | |

### Section 3: Type-Specific Analysis

Select the applicable framework(s):

#### A. Patent Infringement

- [ ] **Claim construction** — construe disputed terms using Phillips v. AWH Corp., 415 F.3d 1303 (Fed. Cir. 2005) [VERIFY] framework
- [ ] **Literal infringement** — all-elements rule, limitation-by-limitation comparison
- [ ] **Doctrine of equivalents** — function-way-result or insubstantial differences test; prosecution history estoppel check (Festo Corp. v. Shoketsu Kinzoku Kogyo Kabushiki Co. [VERIFY])
- [ ] **Means-plus-function** — identify § 112(f) limitations, corresponding structure
- [ ] **Indirect infringement** — induced (§ 271(b)): knowledge + specific intent; contributory (§ 271(c)): material component with no substantial non-infringing use
- [ ] **Validity challenges** — anticipation (§ 102), obviousness (§ 103), enablement/written description (§ 112)

**Claim Chart Format:**

| Claim Element | Accused Feature | Literal? | DOE? | Notes |
|---------------|----------------|----------|------|-------|
| [Limitation 1] | | Y/N | Y/N | |
| [Limitation 2] | | Y/N | Y/N | |

#### B. Trademark Infringement

Apply the circuit-appropriate likelihood-of-confusion factors:

| Factor | Analysis | Weight |
|--------|----------|--------|
| Similarity of marks (sight, sound, meaning, commercial impression) | | |
| Relatedness of goods/services | | |
| Strength of senior mark (inherent + acquired distinctiveness) | | |
| Evidence of actual confusion | | |
| Defendant's intent | | |
| Consumer sophistication | | |
| Channels of trade / marketing convergence | | |
| Likelihood of expansion into related markets | | |

- [ ] **Dilution** — if famous mark: blurring (§ 1125(c)) or tarnishment analysis
- [ ] **Defenses** — descriptive fair use, nominative fair use, First Amendment

#### C. Copyright Infringement

- [ ] **Ownership** — valid registration, chain of title
- [ ] **Access** — direct or circumstantial evidence of access to the work
- [ ] **Substantial similarity** — extrinsic test (objective, filterable elements) + intrinsic test (subjective, ordinary observer)
- [ ] **Idea/expression filtration** — exclude ideas, facts, scènes à faire, merger doctrine elements
- [ ] **De minimis use** — whether copying falls below actionable threshold

**Fair Use (17 U.S.C. § 107):**

| Factor | Analysis | Favors |
|--------|----------|--------|
| Purpose and character (transformative?) | | P / D |
| Nature of copyrighted work | | P / D |
| Amount and substantiality used | | P / D |
| Market effect | | P / D |

#### D. Trade Secret Misappropriation

- [ ] **Identification** — describe each claimed trade secret with specificity
- [ ] **Qualification** — independent economic value from secrecy + reasonable secrecy measures
- [ ] **Misappropriation method** — improper means (theft, breach of duty, espionage) or breach of confidentiality obligation
- [ ] **Inevitable disclosure** — applicable only in jurisdictions recognizing the doctrine; requires showing high degree of similarity between roles
- [ ] **Restrictive covenants** — NDA/non-compete scope, enforceability, temporal/geographic limits

### Section 4: Defenses & Vulnerabilities

| Defense | Applicability | Risk Level |
|---------|--------------|------------|
| Statute of limitations / laches | | High/Med/Low |
| Estoppel (prosecution, equitable, licensee) | | |
| Exhaustion / first sale | | |
| Independent creation / reverse engineering | | |
| Invalidity / unenforceability | | |
| Fair use / nominative use | | |
| Unclean hands | | |

### Section 5: Remedies Assessment

| Remedy | Availability | Estimated Range |
|--------|-------------|-----------------|
| Lost profits | | |
| Reasonable royalty | | |
| Disgorgement of profits | | |
| Statutory damages | | |
| Enhanced/treble damages (willfulness) | | |
| Attorneys' fees (exceptional case) | | |
| Preliminary injunction (eBay factors) | | |
| Permanent injunction | | |

### Section 6: Overall Assessment & Recommendation

| Item | Assessment |
|------|-----------|
| Infringement likelihood | Strong / Moderate / Weak |
| Strongest arguments for infringement | |
| Greatest vulnerabilities | |
| Recommended course of action | Litigate / Settle / License / Monitor |
| Settlement valuation range | |

## Guidelines

- Analyze each IP type separately when multiple types are at issue
- Apply the all-elements rule strictly for patents — a single missing limitation defeats literal infringement on that claim
- Identify the correct circuit's likelihood-of-confusion factors for trademark (Polaroid, Sleekcraft, Lapp, etc.)
- For copyright, always filter unprotectable elements before applying substantial similarity
- Cite controlling authority from the relevant jurisdiction; flag persuasive-only authority from other circuits
- Use `[VERIFY]` for any citation not confirmed against source documents
- Do not opine on ultimate legal conclusions without qualifying confidence level
- Flag any privilege, work-product, or ethical issues (e.g., analyzing a current client's competitor where conflicts may exist)
- Note when foreign IP rights or international treaties (Paris Convention, Berne Convention, TRIPS) may be implicated
- All damages estimates are preliminary and should be validated by economic expert analysis

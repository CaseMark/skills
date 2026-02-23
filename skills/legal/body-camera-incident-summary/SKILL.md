---
name: body-camera-incident-summary
description: >-
  Transforms police body camera transcripts into a structured 10-section legal
  summary with timestamp-cited verbatim statements, constitutional issue
  spotting, evidence inventory, and probable cause articulation. Maintains
  strict neutrality for use by prosecutors, defense counsel, judges, and civil
  rights litigators. Covers Fourth Amendment search and seizure, Fifth
  Amendment Miranda compliance, use of force under Graham v. Connor, chain of
  custody, and Brady/Giglio disclosure issues. Use during discovery, pre-trial
  preparation, or trial to rapidly verify key events, admissions, and officer
  observations from body cam footage. Trigger keywords: body camera, BWC, body
  worn camera, police video, officer footage, incident summary, use of force
  review, criminal defense.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Body Camera Incident Summary

Transforms police body camera transcripts into a 10-section legal summary with timestamp-cited verbatim statements, constitutional issue spotting, and evidence documentation for criminal defense, prosecution, and civil rights litigation.

## Prerequisites

1. **Transcript(s)** — complete body camera transcript(s); if multiple officers, load all feeds
2. **Supplemental materials** (optional) — incident reports, dispatch logs, officer statements; clearly distinguish source when citing
3. **Matter phase** — discovery, pre-trial, or trial (affects analytical emphasis)

## Output Structure

Produce all 10 sections in order. Every factual claim must be cited `[HH:MM:SS]`. All dialogue is verbatim — never paraphrase. Flag recording gaps (muted audio, obstructed view, interrupted footage) at the point they occur.

---

### 1. Case Information

| Field | Content |
|-------|---------|
| Date / Time | Recording start with time zone if discernible |
| Officers | Full name, badge number, role (primary / backup / supervisor / K-9 / FTO) |
| Location | Full address or intersection, city, county, state |
| Tracking IDs | Case no., incident no., CAD no. |
| Duration | Final timestamp; note if recording began after contact or ended before disposition |
| Technical deficiencies | Muted segments, obstructed views, interrupted recording |

If information is absent from the transcript, state it is absent — do not infer.

---

### 2. Executive Summary

4–6 sentence narrative answering:
- **Initiating event** — traffic stop (observed violation), dispatch call, Terry stop (articulable RS factors), warrant service, or community caretaking
- **Escalation / de-escalation arc**
- **Disposition** — arrested (charges), cited and released, or released without action
- **Primary legal issues** — 4th Amendment stop/search, Miranda compliance, Graham v. Connor force, qualified immunity exposure

---

### 3. Participant Identification

For each person:
- **Subjects**: name/alias `[timestamp]`, probation/parole status, outstanding warrants (jurisdiction, type), medical/mental health/intoxication indicators
- **Officers**: name, badge, role; trainee/FTO relationship if applicable
- **Third parties**: relationship to primary subject; whether separately detained, questioned, or released

---

### 4. Chronological Timeline

Strict chronological narrative with `[HH:MM:SS]` at each inflection point:

| Milestone | What to document |
|-----------|-----------------|
| Initiating event | Articulated basis — violation, RS factors, dispatch info |
| Search discussions | Complete officer dialogue revealing legal theory being developed |
| Detention → arrest | Officer's PC statement; formal arrest language |
| Miranda | Verbatim warnings + subject's response to each component |
| Each search | Scope, areas/containers examined, stated legal justification, temporal relation to consent or PC |
| Use of force | Commands (exact language) → subject response type (passive / active / aggressive) → each force application by type → interval between command and force → injury complaints / medical response |
| Contraband discovery | Plain view vs. consent vs. SITA vs. other; ownership claims or disclaimers verbatim |
| Database / dispatch | Warrant hits, information received, effect on PC development |
| Supervisor arrival | Timestamp; stated purpose |
| Evidence collection | On-scene chain of custody actions |

Cross-reference timestamps across multiple camera angles for force incidents and searches.

---

### 5. Constitutional & Procedural Analysis

**4th Amendment**
- **Stop validity**: Traffic stop — *Whren v. United States*; Terry stop — totality of circumstances, *Terry v. Ohio*; extension beyond original purpose — *Rodriguez v. United States*
- **Consent search**: Exact consent language + subject response; voluntariness factors under *Schneckloth v. Bustamonte* (continued detention, show of force, failure to advise right to refuse)
- **PC warrantless search**: Specific articulable facts; *Carroll v. United States* (vehicle); inventory — standardized policy vs. investigative pretext
- **Search incident to arrest**: Temporal/spatial compliance; *Arizona v. Gant* (vehicle); *Riley v. California* (cell phone)
- **K-9**: Sniff justification; detention duration to facilitate sniff; alert description; handler certification (*Florida v. Harris* reliability)

**5th Amendment / Miranda**
- Custody attachment moment (reasonable person standard)
- Verbatim warnings — flag any deviation from standard formulation
- Waiver assessment — knowing/voluntary/intelligent (*Colorado v. Connelly*)
- Rights invocations — exact language; officer compliance with *Edwards v. Arizona* / *Davis v. United States*
- Post-invocation questioning → suppression flag

**Use of Force — Graham v. Connor**
- Severity of crime; immediate threat to officer or public; active resistance or flight
- Force modality proportionality to resistance level
- Temporal gap: compliance → continued force application
- Officer's contemporaneous force justification verbatim; flag post-hoc rationalization

**Arrest Authority**
- PC articulation at moment of arrest
- Warrant confirmation or warrantless felony/misdemeanor analysis

**Additional issues as applicable**: 1st Amendment (recording police), 6th Amendment (counsel invocation), state constitutional provisions providing greater protection, *Brady v. Maryland* / *Giglio v. United States* disclosure obligations

---

### 6. Physical Evidence Catalog

| # | Item description | Discovery timestamp | Location found | Legal basis | Ownership claims / disclaimers | Chain of custody actions |
|---|-----------------|-------------------|---------------|-------------|-------------------------------|------------------------|
| 1 | | | | | | |

- **Controlled substances**: suspected type, form, color, packaging, field test result, weight if measured, personal use vs. distribution indicators
- **Firearms**: type, make/model, loaded status, rounds chambered, serial number documentation
- **Currency**: denomination breakdown, total, civil forfeiture warnings given
- **Paraphernalia**: specific items, residue, usable quantities

---

### 7. Verbatim Statements & Legal Admissions

Format: `"[exact quote]" — [SPEAKER] [HH:MM:SS]`

Organize by category:

| Category | Examples |
|----------|---------|
| **Admissions / inculpatory** | Ownership, knowledge, participation |
| **Exculpatory / denials** | Innocent possession, alibi, witness identification |
| **Rights invocations** | Search refusal, silence, counsel request — note officer's immediate response |
| **Inconsistent statements** | Present chronologically to show evolution or contradiction |
| **Excited utterances** | Note circumstances establishing reliability for hearsay exception analysis |
| **Statements to third parties** | Overheard by officers; not Miranda-protected |
| **Comprehension / capacity disclosures** | Intoxication, mental health, language barrier — affects waiver voluntariness |

For lengthy statements, excerpt critical language with ellipses; never paraphrase any statement that may bear on legal interpretation.

---

### 8. Officer Observations & Probable Cause Articulation

| Type | What to capture |
|------|----------------|
| Olfactory | Odor description, source location, fresh vs. burnt; alcohol (breath vs. vehicle interior distinction) |
| Visual | Furtive movements (specific description + temporal relation to stop); plain view items (officer vantage point); impairment indicators |
| Auditory | Slurred speech, sounds of items moving/concealed, overheard conversations |
| Training/experience interpretations | Verbatim — "based on X years in narcotics, this packaging is consistent with distribution" |
| Standardized tests | FSTs administered + performance description; PBT numerical result; DRE findings; refusals and advisements |
| Threat/safety assessments | Weapon bulges, aggressive posturing, tactical disadvantages, environmental factors justifying protective measures |

Reproduce contemporaneous RS/PC articulation verbatim. Flag where officer explanation appears to be post-hoc rationalization of an investigative hunch.

---

### 9. Incident Disposition & Post-Arrest Procedures

- **Arrests**: all charges in order articulated (felony/misdemeanor); enhancements (school zone, priors, gang allegations)
- **Citations**: violation cited; court date instructions
- **Releases**: officer's stated reason for no enforcement action (may reveal evidentiary weakness)
- **Vehicles**: impound basis; inventory search procedures; release to third party (identity, authorization verified)
- **Evidence**: lab submissions (test type requested); safekeeping property (recovery instructions given); currency (forfeiture procedure)
- **Transport**: destination (jail / lockup / medical facility); injuries treated; medical clearance before booking
- **Post-arrest statements**: Miranda status at time of statement; patrol vehicle admissions (no Miranda required)
- **Victims / witnesses**: contact info collected; injury documentation; protective order information provided

---

### 10. Critical Issues for Further Legal Review

Flag each issue with a category tag and specify: the specific facts, the legal framework implicated, and the recommended next step.

| Tag | Issue type |
|-----|-----------|
| `[SUPPRESS]` | Potential 4th/5th Amendment violation warranting suppression motion |
| `[MIRANDA]` | Equivocal invocation requiring *Davis* analysis; post-invocation questioning |
| `[FORCE]` | Disproportionate force; Graham v. Connor excessive force claim |
| `[GAP]` | Audio/video deficiency at critical moment — specify what was missed |
| `[CONFLICT]` | Timestamp/narrative inconsistency; officer vs. subject account divergence |
| `[DISCOVERY]` | Brady/Giglio material; informant disclosure; prior contacts requiring file review |
| `[POLICY]` | Deviation from department policy; supervisory or municipal liability exposure |
| `[WITNESS]` | Bystander needing location; chain of custody deficiency |
| `[EXPERT]` | Training/certification requiring personnel file review or expert qualification |

---

## Guidelines

- **Neutrality**: Document inculpatory and exculpatory evidence with equal precision; no editorial characterization
- **Multiple feeds**: Cross-reference timestamps across camera angles for all use-of-force and search events
- **Absent information**: Affirmatively state when foundational data is not in the transcript — never infer or speculate
- **Verbatim standard**: Never paraphrase rights invocations, consent exchanges, or admissions — legal consequences turn on precise wording
- **Jurisdiction**: US; note when state constitutional provisions may provide greater protection than the federal floor
- **Uncertain citations**: Mark with `[VERIFY]` any case citation or statutory reference not confirmed from the transcript

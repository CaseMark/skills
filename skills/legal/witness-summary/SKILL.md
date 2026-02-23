---
name: witness-summary
description: Generates structured summaries of witness statements for litigation, extracting chronological narratives, key facts, credibility indicators, admissibility concerns, and evidentiary value. Use when summarizing witness statements, deposition transcripts, witness testimony, or preparing witness examination outlines during discovery, pre-trial, or trial phases.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Witness Statement Summary

Produces a structured, reference-ready summary of one or more witness statements for use in case preparation, deposition planning, and trial strategy.

## Prerequisites

1. **Witness statement(s)** — transcripts, declarations, affidavits, or deposition excerpts
2. **Case context** — claims at issue, parties, and key disputed facts (if available)
3. **Related exhibits** — documents referenced in or attached to the statement (if available)

## Output Structure

### 1. Executive Summary

| Field | Content |
|---|---|
| Witness name | Full name, role (party / fact witness / expert) |
| Relationship to case | Connection to parties and events |
| Statement type | Declaration, deposition, interview, affidavit |
| Date of statement | When given; date(s) of events described |
| Bottom line | 2-3 sentences: what this witness establishes and its strategic significance |

### 2. Witness Background

- Biographical details relevant to credibility or weight
- Relationship to parties
- Basis of knowledge (percipient, expert, custodian, etc.)
- Prior involvement in related proceedings

### 3. Chronological Fact Narrative

Present the witness's account as a chronological table:

| Date/Time | Location | Event/Observation | Certainty | Corroboration |
|---|---|---|---|---|
| Specific date | Where | What the witness describes | High / Hedged / Uncertain | Supporting or conflicting evidence |

- Preserve specific factual assertions (names, numbers, sequences)
- Flag hedging language verbatim (e.g., "I believe," "to the best of my recollection")
- Note gaps or periods the witness cannot account for

### 4. Key Evidentiary Points

Organize by legal significance:

- **Admissions** — statements against interest or acknowledging elements of opposing claims
- **Corroborations** — testimony that aligns with other witnesses or documentary evidence
- **Contradictions** — conflicts with other witness accounts, documents, or prior statements by this witness
- **Unique facts** — information only this witness provides

### 5. Admissibility Concerns

Flag each issue with the relevant rule:

| Issue | Detail | Rule |
|---|---|---|
| Hearsay | Quote or paraphrase the statement-within-a-statement | FRE 801-807 |
| Opinion / speculation | Lay opinion exceeding FRE 701 scope | FRE 701-702 |
| Authentication gaps | Referenced documents not yet authenticated | FRE 901 |
| Privilege risk | Statements potentially implicating attorney-client or work product | — |
| Character / propensity | Testimony that may trigger FRE 404 issues | FRE 404 |

### 6. Credibility Assessment

| Factor | Observation |
|---|---|
| Internal consistency | Contradictions within the statement itself |
| External consistency | Alignment with documentary or physical evidence |
| Bias / motive | Financial interest, relationship to party, litigation motivation |
| Demeanor indicators | Certainty, qualifications, volunteered vs. elicited testimony |
| Impeachment material | Prior inconsistent statements, convictions (FRE 609), bias |

### 7. Strategic Assessment

- **Strengths** — what this testimony establishes favorably
- **Vulnerabilities** — lines of cross-examination or rebuttal
- **Recommended follow-up** — additional discovery, corroborating evidence to obtain, deposition topics

## Guidelines

- Preserve factual specificity — never generalize away dates, amounts, or names
- Quote significant language verbatim with transcript/paragraph citations
- When summarizing multiple witnesses, use consistent format and flag inter-witness conflicts explicitly
- For multi-witness sets, add a **Conflict Matrix** cross-referencing disputed facts across witnesses
- Do not editorialize beyond credibility and strategic observations — keep factual sections neutral
- Adapt evidentiary rules to applicable jurisdiction when specified (default: U.S. federal)
- If the statement references exhibits or documents not provided, note them as **[NOT REVIEWED]**

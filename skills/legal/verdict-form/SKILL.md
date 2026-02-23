---
name: verdict-form
description: Drafts comprehensive civil trial verdict forms structuring jury questions for each cause of action, affirmative defenses, conditional damages, comparative fault, and special interrogatories. Enforces plain-language phrasing, logical conditional flow, proper captioning, and jurisdiction-appropriate signature blocks. Use when preparing verdict forms, special verdict forms, jury interrogatories, or general verdict forms with interrogatories during trial preparation.
tags:
  - drafting
  - litigation
  - pleading
---

# Verdict Form

Drafts a trial-ready verdict form that guides jury deliberations through structured questions on liability, affirmative defenses, and damages for each cause of action.

## Prerequisites

1. **Complaint / operative pleading** — all causes of action and elements
2. **Answer / affirmative defenses** — complete defense list including any comparative fault allegations
3. **Jury instructions** — draft or final set, for terminology alignment
4. **Damages evidence summary** — categories of damages supported by evidence
5. **Local rules** — jurisdiction-specific verdict form requirements (signature rules, special verdict mandates)

## Output Structure

### 1. Caption

Mirror the caption from operative pleadings exactly:

```
[COURT NAME]
[DIVISION, if applicable]

[PLAINTIFF NAME(S)],
        Plaintiff(s),
  v.                                    Case No. [XXXXXXX]
[DEFENDANT NAME(S)],
        Defendant(s).

                    VERDICT FORM
```

### 2. Introductory Statement

```
We, the jury, duly empaneled and sworn in the above-entitled action,
hereby return the following verdict:
```

### 3. Liability Questions

For each cause of action, draft a sequentially numbered question:

| Element | Requirement |
|---------|-------------|
| Phrasing | Plain language — no legal jargon (e.g., "breached the contract" not "material breach of the subject agreement") |
| Burden | State applicable burden ("proven by a preponderance of the evidence") |
| Answer format | Yes ___ / No ___ with adequate white space |
| Ordering | Follow logical claim dependency — foundational claims first |

### 4. Affirmative Defense Questions

For each complete-bar affirmative defense, insert a conditional question:

```
If you answered "Yes" to Question [X], answer the following:

Question [N]: Has the defendant proven that [defense] applies?

    Yes ___    No ___

If you answered "Yes," skip to the Signature section.
If you answered "No," proceed to Question [N+1].
```

### 5. Damages Section

Condition all damages questions on liability findings:

```
If you answered "Yes" to Question [X] (liability) and "No" to
Question [Y] (affirmative defense), answer the following damages
questions. Otherwise, skip to the Signature section.
```

Draft separate dollar-amount lines for each damages category:

| Category | When to Include |
|----------|----------------|
| Compensatory (general) | Always if liability found |
| Compensatory (special) | Lost profits, medical expenses, property damage — itemize separately |
| Consequential | If pled and supported by evidence |
| Punitive | Only after predicate findings (malice/fraud/oppression per applicable state law) |

Punitive damages template:

```
Question [N]: Did [defendant] act with [malice/fraud/oppression]?
    Yes ___    No ___

If "Yes" to Question [N]:
Question [N+1]: What amount of punitive damages, if any, do you award?
    $ _______________
```

### 6. Comparative Fault / Apportionment

If at issue, include percentage allocation:

```
Question [N]: What percentage of fault do you assign to each party?
(Must total 100%)

    [Plaintiff]:   ____%
    [Defendant 1]: ____%
    [Defendant 2]: ____%
              Total: 100%
```

### 7. Special Interrogatories

Add numbered questions for any court-required factual findings:
- Good faith determinations
- Notice compliance
- Conditions precedent
- Timeliness / statute of limitations

### 8. Signature Block

```
We, the jury, certify that this is our verdict.

Dated: _______________

_______________________________
Presiding Juror / Foreperson (Signature)

_______________________________
Presiding Juror / Foreperson (Print Name)
```

> **Note:** Check local rules — some jurisdictions require all jurors to sign; others require only the foreperson.

## Guidelines

- **Sequential numbering** — number all questions continuously across sections; do not restart per section
- **Cross-reference jury instructions** — every question must use identical terminology and elements as the jury charge
- **Conditional flow** — every skip instruction must be explicit ("If No, skip to Question [N]")
- **Completeness check** — the form must cover every claim + every complete-bar defense so the court can enter judgment from answers alone
- **Avoid inconsistent verdicts** — structure conditionals to prevent logically contradictory answers
- **Formatting** — consistent fonts, clear visual separation between questions, bold sparingly for instructions only
- **Jurisdiction adaptation** — verify local form requirements, especially for punitive damages predicates and signature requirements

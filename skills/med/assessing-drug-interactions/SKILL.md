---
name: assessing-drug-interactions
description: Evaluates medication lists for drug-drug interactions with severity ratings, mechanisms, and clinical management recommendations. Use when performing medication reconciliation, reviewing polypharmacy patients, or checking new prescription safety.
tags:
  - analysis
  - pharmacology
  - patient-safety
metadata:
  author: casemark
  practice_areas:
    - Pharmacy
    - Clinical Pharmacology
  document_types:
    - Medication List
    - Interaction Report
  skill_modes:
    - Analysis
    - Assessment
---

# Assessing Drug Interactions

Produces interaction matrices from medication lists.

## Workflow

1. **Normalize** medication list — map brand to generic, confirm doses
2. **Check** pairwise interactions — severity (contraindicated/major/moderate/minor)
3. **Identify** mechanism for each interaction (CYP450, QT prolongation, serotonergic, etc.)
4. **Assess** clinical significance — is the interaction theoretical or clinically relevant at these doses?
5. **Recommend** — monitoring, dose adjustment, timing separation, or substitution

## Output Template

```markdown
## Drug Interaction Assessment

### Medication List
| # | Medication | Dose | Frequency | Indication |
|---|-----------|------|-----------|------------|

### Interactions Found

#### [Severity]: [Drug A] + [Drug B]
- **Mechanism**: [Pharmacokinetic/pharmacodynamic mechanism]
- **Clinical Effect**: [What could happen]
- **Risk Level**: [Contraindicated / Major / Moderate / Minor]
- **Management**: [Recommended action]

### Summary Matrix
| | Drug 1 | Drug 2 | Drug 3 | ... |
|---|--------|--------|--------|-----|
| Drug 1 | — | [severity] | [severity] | |

### High-Priority Alerts
- [Interactions requiring immediate attention]
```

## Key Rules

- Always note the interaction mechanism, not just the severity label
- Distinguish pharmacokinetic (absorption, metabolism) from pharmacodynamic interactions
- Consider cumulative effects (multiple QT-prolonging drugs, multiple serotonergic drugs)
- Note renal/hepatic function if available — affects many interaction severities
- Flag duplicate therapeutic classes (two SSRIs, two NSAIDs, etc.)

For CYP450 substrate/inhibitor/inducer tables, see [references/CYP450-REFERENCE.md](references/CYP450-REFERENCE.md).

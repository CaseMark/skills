---
name: evaluating-diagnostic-accuracy
description: Calculates and interprets diagnostic test performance metrics including sensitivity, specificity, predictive values, and likelihood ratios from study data. Use when evaluating new diagnostic tests, comparing test performance, or interpreting test results in clinical context.
tags:
  - analysis
  - diagnostics
  - biostatistics
metadata:
  author: casemark
  practice_areas:
    - Laboratory Medicine
    - Clinical Research
  document_types:
    - Diagnostic Test Evaluation
  skill_modes:
    - Calculation
    - Analysis
---

# Evaluating Diagnostic Accuracy

Computes diagnostic test performance from study data.

## Workflow

1. **Construct** 2x2 table from study data
2. **Calculate** intrinsic measures — sensitivity, specificity
3. **Calculate** predictive values — PPV, NPV (note: prevalence-dependent)
4. **Calculate** likelihood ratios — LR+, LR- (prevalence-independent)
5. **Interpret** clinical utility — what does this test actually tell you?
6. **Compare** to alternatives if available

## Calculations

```
                Disease+    Disease-
Test+           TP          FP          → PPV = TP/(TP+FP)
Test-           FN          TN          → NPV = TN/(FN+TN)
                ↓           ↓
            Sens=TP/(TP+FN) Spec=TN/(FP+TN)

LR+ = Sensitivity / (1 - Specificity)
LR- = (1 - Sensitivity) / Specificity
```

## Output Template

```markdown
## Diagnostic Test Evaluation: [Test Name] for [Condition]

### 2x2 Table
|  | Disease+ | Disease- | Total |
|--|----------|----------|-------|
| Test+ | [TP] | [FP] | |
| Test- | [FN] | [TN] | |

### Performance Metrics
| Metric | Value | 95% CI | Interpretation |
|--------|-------|--------|----------------|
| Sensitivity | | | |
| Specificity | | | |
| PPV | | | |
| NPV | | | |
| LR+ | | | |
| LR- | | | |
| Accuracy | | | |

### Clinical Interpretation
- **Best Use**: [Screening vs. confirmation vs. rule-out]
- **At Prevalence [X]%**: [How PPV/NPV change]
- **Compared to [Alternative]**: [If available]
```

## Key Rules

- PPV and NPV depend on prevalence — always note the study prevalence
- LR+ > 10 and LR- < 0.1 are strong; report the strength
- A highly sensitive test is best for ruling OUT (SnNOut)
- A highly specific test is best for ruling IN (SpPIn)
- Spectrum bias: performance varies across disease severity
- Always consider the clinical context — no test exists in isolation

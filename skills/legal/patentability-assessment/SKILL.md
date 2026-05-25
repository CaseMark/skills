---
name: patentability-assessment
description: Preliminary patentability assessment evaluating novelty and non-obviousness before formal prosecution
tags:
  - practice: patent
  - document: analysis
  - mode: analysis
---

# Patentability Assessment

Provide a preliminary assessment of whether an invention likely meets patentability requirements.

## Prerequisites
- Invention disclosure document (PDF, DOC, DOCX)
- Key technical features description
- Competing products or prior art known to the inventor

## Workflow
1. **Parse**: Extract technical features from invention disclosure
2. **Search**: Conduct broad patentability search across patent and NPL databases
3. **Evaluate**: For each feature, assess:
   - Is it novel? (no single reference discloses all elements)
   - Is it non-obvious? (would a POSITA find the combination obvious)
4. **Score**: Assign patentability score (high/medium/low) with rationale
5. **Recommend**: Suggest claim strategies to overcome identified references

## Pitfalls
- This is preliminary, not a formal legal opinion — mark it as such
- Don't claim definitively that something IS or IS NOT patentable
- Focus on the combination of features, not individual elements
- Be honest about close prior art — it's better to flag it early

---
name: patent-prior-art-analysis
description: Conduct comprehensive prior art searches and generate invalidation reports for patent applications and existing patents
tags:
  - practice: patent
  - document: analysis
  - mode: research
---

# Patent Prior Art Analysis

Identify and analyze prior art references that anticipate or render a patent claim obvious.

## Prerequisites
- Patent UCID or application number
- Independent and dependent claims
- Invention disclosure or technical description
- Key technical features (one per line)

## Workflow
1. **Search**: Run semantic search across patent and non-patent literature using technical features
2. **Filter**: Exclude references beyond the priority date and excluded citations
3. **Analyze**: For each candidate reference, assess anticipation vs. obviousness
4. **Map**: Create a claims mapping chart showing which claims each reference teaches
5. **Report**: Generate structured invalidation report with:
   - Technical summaries of each reference
   - Anticipation analysis per claim
   - Obviousness analysis combining references
   - Confidence scores for each mapping

## Pitfalls
- Don't confuse novelty with non-obviousness; document both separately
- Always verify the reference's priority date is before the claimed invention
- Exclude references that are merely cited by the patent without being prior art
- Avoid over-indexing on keyword overlap — semantics matter more than vocabulary

---
name: GC Easy Prompt Legal
description: Advanced prompt engineering for legal research, analysis, and document review
tags:
  practice_area: [legal-research, regulatory]
  document_type: [memo, analysis, brief]
  skill_mode: [drafting, analysis, research]
---

# GC Easy Prompt Legal

AI-native prompt composition for legal tasks that turns simple natural language requests into precise, citable legal analysis.

## Prerequisites

- Legal domain knowledge in target practice area
- Access to authoritative legal sources (cases, statutes, regulations)
- SOC 2-compliant AI infrastructure for confidential matters

## Workflow

1. **Intent capture**: Receive natural language legal request (e.g., "analyze NDAs for non-compete risk")
2. **Prompt expansion**: Transform into structured multi-step prompt with explicit reasoning chain, source references, and output format requirements
3. **Multi-model routing**: Select appropriate LLM (5-model ensemble: GPT-5, Claude, Gemini, legal fine-tuned, domain-specific) based on task complexity and practice area
4. **Source grounding**: Attach authoritative legal citations (cases, statutes, regulations) as structured references
5. **Output assembly**: Return structured analysis with verifiable exact quotes (character-level precision) and confidence scores

## Pitfalls

- Don't let the AI hallucinate citations — every quote must be traceable to a source
- Multi-model routing should default to conservative model for high-stakes litigation work
- Easy Prompt should NEVER replace attorney judgment on legal strategy or ethical obligations
- Confidential matter classification must be enforced before any prompt is sent to external models

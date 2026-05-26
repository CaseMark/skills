---
name: deepjudge-agile-workflows
description: Design LLM-powered AI workflows for repetitive legal operations — multi-step research, document synthesis, and cross-referencing across matter files.
tags: [legal-ops, regulatory]
skill_mode: [drafting, analysis]
---

# Legal AI Workflow Design

## Prerequisites
- Catalog of repetitive legal tasks in the practice area
- Available data sources (documents, APIs, internal systems)

## Workflow
1. Inventory the repetitive task: inputs, decision points, outputs, stakeholders
2. Decompose into discrete steps; identify which need LLM reasoning vs. rule-based logic
3. Design the workflow graph: trigger → retrieve → reason → act → review
4. Specify guardrails: LLM-agnostic reasoning, data source constraints, audit logging
5. Draft the workflow specification with fallback human review points

## Pitfalls
- Never fully automate without a human-in-the-loop checkpoint on consequential outputs
- Keep workflows LLM-agnostic; don't hardcode model-specific behaviors
- Log every retrieval and action for auditability

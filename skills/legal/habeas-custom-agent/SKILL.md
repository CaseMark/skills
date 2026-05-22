---
name: custom-legal-agent-builder
language: en
description: >-
  Designs and deploys custom AI agents tailored to a specific practice
  area and house style. Use when building practice-area-specific legal
  assistants that produce outputs matching a firm's tone, formatting
  standards, and analytical approach. Trigger keywords: custom legal AI,
  practice area agent, house style AI, legal AI customization, firm-specific
  assistant, branded legal research agent.
tags:
  - research
  - drafting
  - legal-ops
---

# Custom Legal Agent Builder

Architects practice-area-specific AI agents with firm-level tone, style,
and analytical preferences baked into the workflow.

## Prerequisites
- Practice area definition (e.g., employment litigation, IP, family law)
- House style guide (tone, formatting, citation standards)
- Sample output documents (past memos, briefs, research reports)
- Firm-specific research databases or preferred sources

## Workflow
1. **Practice Area Definition** — Map the scope of queries, document
  types, and research sources the agent will handle.
2. **Style Alignment** — Ingest house style documents and past outputs
  to calibrate tone, structure, citation format, and language preferences.
3. **Source Configuration** — Configure the agent to prioritize
  firm-preferred sources (cases, statutes, internal precedents).
4. **Guardrails & Constraints** — Set limits on citation fabrication,
  hallucination mitigation rules, and jurisdiction scope.
5. **Testing & Calibration** — Run the agent against sample questions,
  compare output to partner-level work, adjust prompts and constraints.
6. **Deployment** — Integrate into the firm's workflow tools with
  user-facing interface, access controls, and usage monitoring.

## Pitfalls
- Do not over-constrain the agent — balance precision with flexibility
  for novel legal questions.
- House style should cover citation format, tone, and structure but
  not override legal accuracy.
- Regularly audit agent outputs for drift from style and accuracy.
- Always maintain attorney review gate for agent-generated content.

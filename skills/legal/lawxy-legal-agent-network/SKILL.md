---
name: legal-agent-network
description: Orchestrate specialized AI agents to draft, redline, and research legal documents under human control with rule-based governance
tags:
  - practice_area: corporate
  - document_type: agreement, letter
  - skill_mode: drafting
---

# Legal Agent Network — Multi-Agent Drafting & Research

Coordinate autonomous AI agents to handle parallel legal tasks under controlled rules, with human oversight at each gate.

## Prerequisites

- Clear task decomposition (what agents do, in what order)
- Human-in-the-loop approval gates defined
- Agent role definitions (researcher, drafter, redliner, compliance checker)
- Access to relevant precedent and firm knowledge base

## Workflow

1. Define the task graph: which agents run, which depend on which outputs
2. Launch parallel agents for independent subtasks (e.g., research + contract review simultaneously)
3. Each agent works under explicit rules: acceptable clauses, prohibited language, citation requirements
4. Agent outputs are collected and presented for human review at each gate
5. Human approves, rejects, or modifies outputs before advancing to next stage
6. Final assembled document incorporates all approved agent outputs with full audit trail

## Pitfalls

- Agents must never auto-advance past a human gate without explicit approval
- Rule conflicts between agents (e.g., drafter suggests a clause compliance checker flags) must surface to human
- Over-parallelization can create conflicting drafts; serialize when task dependencies exist
- Always maintain agent provenance in the final document for auditability

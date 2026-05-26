---
name: trustplane-compliance-audit
description: Generate audit-ready compliance reports for LLM deployments covering EU AI Act, NIST AI RMF, SOC 1, HIPAA, and GDPR requirements.
tags: [compliance, regulatory]
skill_mode: [drafting, analysis]
---

# LLM Compliance Audit Report Generation

## Prerequisites
- Audit logs of all LLM interactions (prompts, completions, enforcement actions)
- Registry of deployed models and their risk classifications
- Current regulatory framework requirements

## Workflow
1. Compile the AI inventory: all models, use cases, data sources, and ownership
2. Extract enforcement data from audit logs: block rates, warning rates, attack patterns
3. Map compliance evidence to each framework requirement (EU AI Act articles, NIST functions, SOC controls)
4. Generate narrative analysis explaining the risk posture and control effectiveness
5. Produce framework-specific report sections with traceable evidence references

## Pitfalls
- Never extrapolate beyond logged data — if it's not in the audit log, it's not proven
- Separate compliance evidence from compliance claims; only report verified controls
- Update reports whenever model configurations or data sources change

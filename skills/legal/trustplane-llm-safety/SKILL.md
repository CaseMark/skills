---
name: trustplane-llm-safety
description: Draft safety policies and prompt inspection rules for LLM deployments — detect PII, prompt injection, impersonation, and sensitive data exposure.
tags: [compliance, regulatory]
skill_mode: [drafting, analysis]
---

# LLM Safety Policy & Prompt Inspection Rules

## Prerequisites
- Knowledge of the LLM use case and data sensitivity classification
- Applicable regulatory frameworks (EU AI Act, GDPR, HIPAA, etc.)

## Workflow
1. Classify the LLM deployment by risk tier (minimal, limited, high, unacceptable)
2. Define forbidden input categories: PII, PHI, confidential business data, prompt injections
3. Draft threshold-based detection rules for each risk category with confidence scoring
4. Specify enforcement actions per category: ALLOW, WARN, BLOCK
5. Design audit logging requirements capturing every prompt, completion, and enforcement decision

## Pitfalls
- Don't block legitimate business queries with overly broad PII rules — tune thresholds
- Ensure prompt-hacking detection covers multi-turn and indirect injection patterns
- Log all enforcement decisions with reason codes for regulator review

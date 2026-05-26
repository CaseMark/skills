---
name: trustplane-prompt-inspection
description: Review and classify LLM prompts against safety, compliance, and data governance policies — categorize risk, flag policy violations, and recommend actions.
tags: [compliance, regulatory]
skill_mode: [analysis, research]
---

# Prompt Classification & Risk Analysis

## Prerequisites
- Published safety policy with defined risk categories and thresholds
- Access to prompt content and associated model configuration

## Workflow
1. Parse the prompt for content categories: PII, PHI, sensitive data, prompt injection, impersonation
2. Score each category on a 0-1 confidence scale against defined thresholds
3. Classify the overall prompt: clean, warn, or block based on combined scores
4. Document the classification rationale with category scores and matched rules
5. Recommend action: pass through, add warning, or block with reason

## Pitfalls
- Don't classify a prompt solely on keyword matching — context matters (e.g., SSN in a redacted filing vs. raw data)
- Distinguish between prompt-hacking intent and accidental policy violations
- Maintain consistent scoring across all categories for audit comparability

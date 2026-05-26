# FedRAMP Security Plan & Control Implementation Plan Drafting

## Prerequisites
- Target system architecture and deployment model (cloud/on-prem/hybrid)
- Existing security controls inventory or assessment results
- FedRAMP baseline level (Low/Moderate/High)
- Agency sponsor requirements (if applicable)

## Workflow
1. Determine FedRAMP baseline level from system categorization (FIPS 199/53)
2. Map applicable controls from NIST SP 800-53 to FedRAMP control catalog
3. For each control, draft the Security Plan section covering:
   - Control intent and implementation approach
   - Responsible parties (roles: CSP, AO, ISSO, CISO)
   - Implementation artifacts (policies, procedures, technical configs)
   - Inherited vs. shared vs. individual control designation
4. Generate the Control Implementation Plan (CIP) with implementation timeline
5. Flag gaps where controls lack documentation or technical evidence
6. Output structured FedRAMP Security Plan sections ready for human review

## Pitfalls
- Controls are inherited/shared/individual — misclassification causes AO rejection
- SP 800-53 Rev 5 has different numbering than Rev 4 — ensure version alignment
- FedRAMP requires family-specific implementation notes (AC, AU, CA, CM, etc.)
- Don't draft controls that are outside the system boundary
- Always reference current FedRAMP Control Baselines, not deprecated versions

## Tags
practice_area: regulatory
document_type: policy, checklist
skill_mode: drafting

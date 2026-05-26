# RMF Authorization Package Evidence Package Organization

## Prerequisites
- System Security Plan (SSP) or draft
- List of all controls assigned to the system
- Available evidence sources (config snapshots, logs, policy docs, test results)

## Workflow
1. Parse the SSP to extract each control and its implementation statement
2. For every control in the package (SSP, SARA, SAR, PP&RL, Plan of Actions):
   - Identify required evidence artifacts per control family
   - Cross-reference against available evidence inventory
   - Mark as: present, partial, missing, or stale
3. Organize evidence into the standard RMF package structure:
   - SSP — system description, boundary diagram, data flow
   - SARA — security assessment results with test evidence
   - POA&M — remediation plan for findings
   - SAP — authorizing official decision package
   - Related plans (PP&RL, contingency, continuity)
4. Generate a traceability matrix: control → evidence → assessor notes
5. Highlight any controls with insufficient evidence for the planned assessment type
6. Output the organized evidence index ready for human verification

## Pitfalls
- Evidence must be current — snapshots older than 90 days need refreshing
- Continuous monitoring evidence (SCUM, automated scanning) is now expected
- SARA requires actual test procedures, not just policy references
- Authority to Operate (ATO) packages differ by AO — know the sponsor's format
- POA&M entries need realistic milestones and realistic remediation dates

## Tags
practice_area: regulatory
document_type: checklist
skill_mode: analysis

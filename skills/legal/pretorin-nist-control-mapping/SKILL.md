# Cross-Framework Security Control Mapping & Gap Analysis

## Prerequisites
- List of applicable frameworks (FedRAMP, DoD RMF, NIST 800-53, CMMC, ISO 27001)
- Current system security posture documentation
- Existing control evidence or assessment reports

## Workflow
1. Identify all applicable frameworks and their current baseline versions
2. For each security control in the target framework:
   - Find equivalent controls across all other frameworks
   - Build a cross-reference mapping table (control ID → equivalents)
   - Flag controls unique to one framework that lack cross-walks
3. Assess implementation status for each mapped group:
   - Fully implemented (all frameworks satisfied)
   - Partially implemented (some frameworks have evidence, others need work)
   - Not implemented (gap — needs remediation plan)
4. Generate a prioritized remediation backlog ranked by framework dependency
5. Output a matrix showing control coverage across all frameworks

## Pitfalls
- DoD RMF (DFARS 7012) has additional controls beyond standard NIST 800-53
- CMMC 2.0 maps to NIST 800-171 (not 800-53) — don't conflate the two
- Control enhancements (e.g., AC-2(3)) have different numbering — preserve full IDs
- Some frameworks require supplementary guidance documents (RMF Guide, CNSS 1253)
- CMMC third-party assessments vs. self-assessments have different control sets

## Tags
practice_area: regulatory
document_type: checklist, analysis
skill_mode: analysis

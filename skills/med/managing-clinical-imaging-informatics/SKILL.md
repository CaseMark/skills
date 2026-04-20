---
name: managing-clinical-imaging-informatics
language: en
description: Structures radiology informatics workflows with PACS integration and DICOM standards. Use when managing imaging informatics, integrating PACS systems, or implementing DICOM workflows.
tags:
  - management
  - health-informatics
metadata:
  author: casemark
  practice_areas:
    - Health Informatics
    - Health IT
    - Clinical Informatics
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Clinical Imaging Informatics

Structures radiology and clinical imaging informatics workflows covering PACS administration, DICOM standards compliance, enterprise image exchange, vendor neutral archives, and the integration of imaging data with EHR and clinical analytics systems.

## Why This Skill Exists

Medical imaging generates over 3.6 billion studies annually in the US alone, producing petabytes of data that must be acquired, stored, distributed, interpreted, and archived according to DICOM standards. Imaging informatics failures have direct patient safety consequences: studies routed to wrong patients, prior exams unavailable for comparison reads, DICOM metadata errors causing misidentification, and broken RIS-PACS-EHR integrations creating ordering gaps. The migration from facility-centric PACS to enterprise imaging platforms and vendor neutral archives (VNAs) adds architectural complexity. This skill provides a structured approach to managing imaging informatics infrastructure and workflows.


The imaging informatics landscape is evolving rapidly with the adoption of cloud PACS, AI-assisted interpretation, 3D post-processing, and enterprise imaging strategies that extend beyond radiology to include cardiology, pathology, dermatology, and ophthalmology. Managing this complexity requires structured approaches to standards compliance, integration architecture, and clinical workflow optimization.
---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **Imaging infrastructure** --- What systems compose the imaging environment? (PACS vendor and version, RIS, VNA, enterprise viewer, 3D post-processing, AI integration platform)
2. **Modalities** --- Which imaging modalities are in scope? (CT, MRI, X-ray, Ultrasound, Mammography, Nuclear Medicine, PET, Fluoroscopy, Cardiology ECHO/Cath, Dermatology, Pathology)
3. **Volume** --- Annual study volume, average study size, and storage growth rate
4. **Integration points** --- How does imaging connect to the EHR? (DICOM Modality Worklist, HL7 ORM/ORU for orders/results, embedded viewer, FHIR ImagingStudy resources, XDS-I for cross-enterprise exchange)
5. **Current challenges** --- What problems drive this work? (Study routing errors, slow image retrieval, storage capacity, enterprise imaging consolidation, AI integration, cloud migration)
6. **Compliance requirements** --- MQSA for mammography, ACR accreditation requirements, state licensing for teleradiology, FDA requirements for imaging AI/CAD
7. **Multi-site considerations** --- Is this a single facility or a multi-site enterprise? Are there remote reading or teleradiology workflows?

### Required Documents

- Imaging system architecture diagram (PACS, RIS, VNA, EHR, AI, modalities)
- DICOM conformance statements for all major systems
- Current imaging routing rules and AE title configuration
- Storage and archival policies (online, nearline, archive retention periods)
- Imaging interface inventory (DICOM, HL7, FHIR connections)
- Imaging AI/CAD product inventory with FDA clearance documentation

8. **Non-radiology imaging** --- Are non-radiology imaging departments in scope? (Cardiology ECHO, GI endoscopy, dermatology photos, wound care imaging, ophthalmology OCT)
9. **Research imaging** --- Are there research imaging workflows that require separate data management or de-identification?

### Imaging Volume Reference

| Modality | Typical Study Size | Annual Growth Rate |
|---|---|---|
| Chest X-ray | 10-30 MB | 3-5% |
| CT (standard) | 100-500 MB | 5-8% |
| MRI | 200 MB-1 GB | 5-8% |
| 3D Mammography (DBT) | 1-3 GB | 10-15% |
| Cardiac CT/MRI | 500 MB-2 GB | 8-12% |
| PET/CT | 1-4 GB | 5-8% |
| Whole Slide Imaging (Pathology) | 2-10 GB per slide | 20-30% |
---

## Step 1 --- Audit DICOM Infrastructure

Assess the technical foundation:

- **AE title management** --- Inventory all DICOM Application Entity titles: source device, destination system, network address, port, and accepted transfer syntaxes. Identify orphaned AE titles (configured but no traffic), misconfigured routing (studies going to wrong destinations), and missing entries (new modalities not configured)
- **DICOM conformance validation** --- For each system-to-system DICOM connection, verify conformance statement compatibility: supported SOP classes (Storage, Query/Retrieve, Modality Worklist, MPPS), transfer syntaxes (Explicit VR Little Endian, JPEG 2000, JPEG-LS), and character set support
- **Modality Worklist** --- Verify that all modalities receive worklist entries from the RIS/EHR. Worklist failures cause technologists to manually enter patient demographics at the modality, introducing identity errors (wrong patient on study, misspelled names, incorrect MRN)
- **MPPS (Modality Performed Procedure Step)** --- Verify that modalities send MPPS messages to confirm study completion, enabling automated study tracking and dose reporting
- **DICOM metadata quality** --- Sample 100 studies across modalities and verify: Patient ID matches EHR MRN, patient name format is consistent, Accession Number is populated and matches RIS order, Study Description is accurate, and Referring Physician is populated

- **Network performance testing** --- Measure DICOM transfer rates between all major system pairs. Baseline: CT studies should transfer from modality to PACS in < 60 seconds, prior study prefetch should complete before the patient reaches the reading station
---

## Step 2 --- Design Enterprise Imaging Architecture

Structure the target-state imaging platform:

- **Vendor Neutral Archive (VNA)** --- Design the VNA as the long-term image repository decoupled from the diagnostic PACS. Define: storage tiers (hot/warm/cold based on study age and access frequency), lifecycle policies (online for 3-5 years, nearline for 5-10 years, archive for retention period), and migration strategy from legacy PACS archives
- **Enterprise image exchange** --- Implement cross-site image sharing using IHE XDS-I (Cross-Enterprise Document Sharing for Imaging) or DICOMweb WADO-RS for web-based retrieval. Define prefetch rules for scheduled patients with relevant priors at other sites
- **EHR integration** --- Configure imaging-EHR integration pathways: embedded PACS viewer launch from EHR (context-sharing via patient, accession, or study UID), diagnostic report display (HL7 ORU or FHIR DiagnosticReport with ImagingStudy reference), and thumbnail/key image display in the patient chart
- **DICOMweb services** --- Implement RESTful DICOM services (WADO-RS, STOW-RS, QIDO-RS) for modern integrations: AI platform image retrieval, research data access, mobile viewing, and FHIR-based image references
- **Cloud and hybrid architectures** --- For cloud PACS or hybrid cloud-on-premise designs, address: image upload bandwidth requirements, latency for diagnostic reading, data residency and HIPAA BAA with cloud provider, and disaster recovery

- **Non-radiology enterprise imaging** --- Extend the imaging platform to non-radiology departments: cardiology ECHO/cath images, GI endoscopy video, dermatology clinical photos, wound care documentation images, and pathology whole slide images. Each department has unique workflow, display, and storage requirements
---

## Step 3 --- Manage Imaging AI and CAD Integration

Integrate AI tools into the imaging workflow:

- **FDA clearance verification** --- Confirm that each imaging AI product has appropriate FDA 510(k) clearance or De Novo classification. Document the cleared indication, input modality, and intended use. AI products without FDA clearance cannot be used for clinical diagnosis
- **Integration architecture** --- Implement AI integration using DICOM-based routing: PACS routes studies to AI server via DICOM Send, AI processes and returns results as DICOM Secondary Capture, DICOM SR (Structured Report), or DICOM Presentation State. Alternatively, use DICOMweb WADO-RS for AI platforms that pull images on demand
- **Workflow integration** --- Define where AI results appear: as a flag on the radiologist worklist (priority boost for positive findings), as overlay annotations on the diagnostic viewer, as a structured report in the EHR, or as a notification to the ordering clinician
- **Performance monitoring** --- Track AI system metrics: processing time per study, positive finding rate, false positive rate (estimated from radiologist override data), system availability, and failure rate. Compare against the vendor's published performance claims
- **Clinical governance** --- Ensure imaging AI is reviewed by the organization's AI/ML governance committee. Define: who reviews AI output (must be interpreted by a qualified radiologist), documentation requirements (how AI assistance is noted in the report), and feedback mechanism for incorrect AI findings

- **AI results documentation** --- Define how AI findings are documented in the radiology report: separate AI findings section, inline annotation reference, or addendum. Ensure the radiologist's independent interpretation is clearly distinguished from AI output
---

## Step 4 --- Implement Quality and Compliance Controls

Ensure imaging operations meet regulatory and quality standards:

- **Dose monitoring** --- Implement radiation dose tracking using DICOM dose structured reports (Dose SR). Set dose reference levels (DRLs) per the ACR and compare institutional dose distributions against national benchmarks. Alert when individual studies exceed DRL thresholds
- **MQSA compliance (Mammography)** --- For mammography programs, verify compliance with the Mammography Quality Standards Act: equipment performance testing, image quality review, radiologist qualification tracking, consumer notification letter management, and annual MQSA inspection readiness
- **Image quality assurance** --- Establish QA protocols for image quality: phantom scanning schedules per modality, image quality review criteria, and technologist feedback when quality standards are not met
- **Study integrity monitoring** --- Implement automated checks for: patient ID mismatches between DICOM header and RIS/EHR (wrong patient on study), duplicate studies (same patient, same exam, same date), orphan studies (images in PACS without a corresponding order), and studies with missing key images
- **Retention compliance** --- Enforce image retention policies aligned with state medical record retention laws (vary by state, typically 7-10 years for adults, until age of majority + 7 years for pediatric) and payer-specific requirements

- **Disaster recovery for imaging** --- Implement imaging-specific DR: replicate critical imaging data (last 30 days minimum) to a geographically separate site, maintain read-only PACS viewer capability during primary system outage, and define recovery time objective (RTO) and recovery point objective (RPO) specific to imaging systems
---

## Step 5 --- Optimize Radiologist Workflow

Improve reading efficiency and quality:

- **Worklist optimization** --- Configure intelligent worklist sorting: priority based on clinical urgency (stat, urgent, routine), study type grouping for batch reading efficiency, AI triage flags to prioritize studies with positive findings
- **Hanging protocol management** --- Maintain modality and exam-specific hanging protocols that display images in the radiologist's preferred layout. Audit hanging protocol usage and update based on radiologist feedback and new exam types
- **Prior study prefetch** --- Configure automated retrieval of relevant prior studies from VNA or external sources based on exam type and clinical context. Relevant priors reduce unnecessary follow-up recommendations and improve diagnostic accuracy
- **Structured reporting** --- Implement structured reporting templates using RSNA reporting templates where available. Structured reports improve downstream data extraction for quality measurement, AI training, and clinical decision support
- **Turnaround time monitoring** --- Track study-to-report turnaround times by modality, priority, and radiologist. Alert when TAT exceeds organizational SLA (e.g., 30 minutes for stat CT, 24 hours for routine X-ray)

- **Report turnaround time targets by priority and modality** ---

| Priority | CT/MRI | X-ray | Ultrasound | Nuclear Medicine |
|---|---|---|---|---|
| Stat | 30 minutes | 30 minutes | 30 minutes | 60 minutes |
| Urgent | 2 hours | 2 hours | 2 hours | 4 hours |
| Routine | 24 hours | 24 hours | 24 hours | 48 hours |
| Screening | 48-72 hours | N/A | N/A | N/A |
---

## Checkpoint B --- Imaging Informatics Review

Before declaring imaging infrastructure changes production-ready:

- [ ] All DICOM routing rules are tested with production-representative studies
- [ ] Modality Worklist delivery is verified for all modalities
- [ ] DICOM metadata quality meets organizational standards (patient ID accuracy > 99.9%)
- [ ] VNA migration preserves all image data with verified DICOM header integrity
- [ ] EHR-PACS integration launches correctly from the patient chart
- [ ] AI integration delivers results within defined latency targets
- [ ] Dose monitoring is operational with DRL alerts configured
- [ ] Disaster recovery and failover procedures are tested

- [ ] Non-radiology imaging departments are connected to the enterprise imaging platform (if in scope)
- [ ] DICOM transfer performance meets defined benchmarks for all modality-to-PACS connections
- [ ] Imaging disaster recovery has been tested within the last 12 months
---

## Quality Audit

- [ ] DICOM conformance statements are on file for all systems
- [ ] AE title inventory is current and matches production configuration
- [ ] Imaging AI products have documented FDA clearance for their intended use
- [ ] MQSA compliance documentation is current for mammography programs
- [ ] Radiation dose monitoring is active with reference levels configured
- [ ] Image retention policies comply with state and federal requirements
- [ ] Study routing error rate is measured and below organizational threshold (< 0.1%)
- [ ] Turnaround time metrics are tracked and reported
- [ ] Enterprise imaging architecture documentation is current

- [ ] AI results are documented in a standardized format within radiology reports
- [ ] Non-radiology imaging workflows are validated for each connected department
- [ ] Storage capacity projections account for 3-5 year growth with advanced modality adoption
- [ ] Critical exam notification workflow is validated for stat findings requiring immediate clinical action
---

## Guidelines

- DICOM metadata errors are patient safety events. A study attributed to the wrong patient can lead to treatment decisions based on another patient's imaging. Implement pre-verification (Modality Worklist) and post-verification (automated DICOM header-to-RIS matching) as dual safety nets
- Vendor Neutral Archives protect against PACS vendor lock-in. Always store the authoritative copy of images in a VNA with a standards-based interface, not solely in the diagnostic PACS
- Imaging AI is an assist tool, not an autonomous diagnostic agent. Every AI finding must be reviewed by a qualified radiologist before clinical action. Document this workflow requirement in policy
- DICOMweb (WADO-RS, STOW-RS, QIDO-RS) is the modern integration standard. Prefer DICOMweb over legacy DICOM C-FIND/C-MOVE for new integrations, especially for web-based viewers and AI platforms
- Storage planning must account for exponential growth. Advanced modalities (cardiac MRI, 3D mammography, PET/CT) generate study sizes 10-100x larger than conventional modalities. Plan storage capacity 3-5 years ahead
- Cross-enterprise image exchange is a patient safety issue, not a convenience feature. A patient presenting to the ED without access to prior imaging receives redundant studies with unnecessary radiation exposure and diagnostic delay
- For teleradiology, ensure DICOM images are transmitted with lossless compression. Lossy compression (JPEG) may introduce artifacts that affect diagnosis, particularly for mammography and subtle findings
- Structured radiology reports (using RSNA templates and RadLex terminology) are the foundation for imaging data analytics, quality measurement, and AI training. Invest in structured reporting adoption early

- Enterprise imaging is the strategic direction: every clinical image should be accessible from a single platform regardless of the originating department. Siloed departmental PACS create care fragmentation and data loss
- For pathology whole slide imaging (WSI), storage requirements are 10-100x larger than radiology per study. Plan storage architecture for WSI as a separate capacity tier
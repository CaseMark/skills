"""
Medical (agentskills.med) taxonomy: 20 subgroups, 20-40 skills each.

Each subgroup is analogous to a legal practice area (e.g., "intellectual property",
"court motions"). Skills within encode semi-structured agentic workflows for
moving and processing/synthesizing information in medical/healthcare spaces.

Naming: gerund form, lowercase-hyphenated, max 64 chars.
"""

MEDICAL_TAXONOMY = {
    # ─── 1. EMERGENCY MEDICINE ───────────────────────────────────────
    "Emergency Medicine": {
        "description": "Acute care workflows for emergency department triage, assessment, and disposition",
        "practice_areas": ["Emergency Medicine"],
        "skills": [
            (
                "triaging-emergency-presentations",
                "Applies ESI triage methodology to assign acuity levels based on presenting complaints, vital signs, and resource needs. Use when triaging ED patients, assigning acuity scores, or prioritizing emergency cases.",
            ),
            (
                "managing-trauma-assessments",
                "Conducts structured primary and secondary trauma surveys following ATLS methodology. Use when assessing trauma patients, documenting trauma workups, or coordinating trauma team activations.",
            ),
            (
                "interpreting-emergency-ecgs",
                "Analyzes 12-lead ECGs for acute findings requiring emergent intervention. Use when reading emergency ECGs, identifying STEMI patterns, or flagging critical arrhythmias.",
            ),
            (
                "documenting-emergency-encounters",
                "Structures ED visit documentation with chief complaint, MDM, and disposition rationale. Use when charting emergency visits, documenting medical decision-making, or creating ED notes.",
            ),
            (
                "calculating-emergency-risk-scores",
                "Computes validated risk scores (HEART, PERC, Wells, Ottawa, CURB-65) from clinical data. Use when calculating clinical decision scores, risk-stratifying ED patients, or applying clinical prediction rules.",
            ),
            (
                "managing-acute-chest-pain",
                "Guides chest pain workup following ACS pathways with troponin timing and disposition criteria. Use when evaluating chest pain, running ACS protocols, or determining observation vs. discharge.",
            ),
            (
                "managing-acute-stroke",
                "Follows time-critical stroke pathway from door-to-needle with NIHSS scoring and tPA criteria. Use when managing stroke alerts, calculating NIHSS, or coordinating thrombolytic decisions.",
            ),
            (
                "evaluating-abdominal-emergencies",
                "Structures abdominal pain workups with differential by quadrant and surgical consultation criteria. Use when assessing acute abdomen, determining imaging needs, or identifying surgical emergencies.",
            ),
            (
                "managing-pediatric-emergencies",
                "Adapts emergency protocols for pediatric patients using weight-based dosing and Broselow methodology. Use when treating pediatric emergencies, calculating pediatric doses, or managing pediatric resuscitations.",
            ),
            (
                "coordinating-emergency-transfers",
                "Structures EMTALA-compliant inter-facility transfer documentation and stabilization requirements. Use when arranging emergency transfers, ensuring EMTALA compliance, or documenting transfer decisions.",
            ),
            (
                "managing-toxicology-emergencies",
                "Identifies toxidromes and guides decontamination and antidote protocols. Use when managing overdoses, identifying toxidromes, or consulting poison control protocols.",
            ),
            (
                "documenting-resuscitation-events",
                "Creates structured code documentation with timestamps, interventions, and ROSC criteria. Use when documenting cardiac arrests, recording resuscitation timelines, or completing code sheets.",
            ),
            (
                "managing-psychiatric-emergencies",
                "Guides acute psychiatric assessment including safety evaluation and involuntary hold criteria. Use when evaluating psychiatric emergencies, assessing suicidality, or initiating involuntary holds.",
            ),
            (
                "interpreting-emergency-imaging",
                "Structures systematic review of emergency CT, X-ray, and ultrasound findings. Use when interpreting emergent imaging, documenting critical findings, or communicating results to teams.",
            ),
            (
                "managing-airway-emergencies",
                "Follows difficult airway algorithm with RSI protocols and backup airway planning. Use when managing difficult airways, planning rapid sequence intubation, or documenting airway management.",
            ),
            (
                "managing-sepsis-bundles",
                "Tracks sepsis bundle compliance with lactate timing, fluid resuscitation, and antibiotic administration. Use when managing sepsis protocols, tracking bundle elements, or documenting sepsis care.",
            ),
            (
                "evaluating-syncope",
                "Risk-stratifies syncope presentations using San Francisco, Canadian, and OESIL rules. Use when evaluating syncope, determining admission criteria, or risk-stratifying fainting episodes.",
            ),
            (
                "managing-anaphylaxis",
                "Guides anaphylaxis recognition and epinephrine-first treatment protocol with observation timing. Use when managing allergic reactions, treating anaphylaxis, or planning post-anaphylaxis observation.",
            ),
            (
                "performing-emergency-procedures",
                "Documents procedural indications, consent, technique, and complications for ED procedures. Use when performing emergency procedures, documenting procedural notes, or recording bedside procedures.",
            ),
            (
                "managing-environmental-emergencies",
                "Guides workup for heat stroke, hypothermia, drowning, and envenomation. Use when managing environmental injuries, treating temperature-related emergencies, or assessing envenomation.",
            ),
        ],
    },
    # ─── 2. HOSPITAL MEDICINE / INPATIENT CARE ───────────────────────
    "Hospital Medicine": {
        "description": "Inpatient care workflows for admission, rounding, discharge, and transitions",
        "practice_areas": ["Hospital Medicine", "Internal Medicine"],
        "skills": [
            (
                "writing-admission-orders",
                "Generates structured admission order sets with diagnosis-specific protocols and safety checks. Use when admitting patients, creating admission orders, or setting up inpatient care plans.",
            ),
            (
                "summarizing-discharge-notes",
                "Transforms hospital discharge paperwork into structured patient summaries with medications, follow-up appointments, activity restrictions, and warning signs. Use when processing discharge documents, creating patient handoffs, or preparing transition-of-care summaries.",
            ),
            (
                "conducting-daily-rounds",
                "Structures systematic rounding documentation with overnight events, assessment, and plan updates. Use when documenting daily rounds, updating inpatient plans, or preparing rounding notes.",
            ),
            (
                "managing-hospital-handoffs",
                "Creates structured handoff communications using I-PASS methodology for shift transitions. Use when performing sign-outs, creating handoff documents, or transitioning patient care between providers.",
            ),
            (
                "reconciling-inpatient-medications",
                "Compares admission, inpatient, and discharge medication lists to identify discrepancies. Use when performing medication reconciliation, identifying med changes, or verifying discharge prescriptions.",
            ),
            (
                "coordinating-multidisciplinary-rounds",
                "Synthesizes input from nursing, pharmacy, PT/OT, social work, and case management into unified care plans. Use when conducting interdisciplinary rounds, coordinating care teams, or documenting team-based decisions.",
            ),
            (
                "managing-length-of-stay",
                "Tracks admission milestones against expected LOS benchmarks with barrier identification. Use when managing length of stay, identifying discharge barriers, or optimizing bed utilization.",
            ),
            (
                "documenting-procedure-notes",
                "Creates structured procedure documentation with indications, technique, findings, and complications. Use when documenting inpatient procedures, recording procedural details, or writing procedure notes.",
            ),
            (
                "managing-inpatient-consultations",
                "Structures consultation requests and responses with specific clinical questions and recommendations. Use when requesting consults, responding to consultations, or documenting specialist input.",
            ),
            (
                "tracking-clinical-deterioration",
                "Implements early warning score monitoring (NEWS, MEWS) with escalation criteria. Use when monitoring clinical deterioration, calculating early warning scores, or triggering rapid response criteria.",
            ),
            (
                "managing-code-status-discussions",
                "Documents goals-of-care conversations with code status decisions and advance directive alignment. Use when discussing code status, documenting goals-of-care, or recording advance directive conversations.",
            ),
            (
                "preparing-transfer-summaries",
                "Creates comprehensive transfer documentation for ICU-to-floor or facility-to-facility transitions. Use when transferring patients between units, preparing transfer notes, or coordinating level-of-care changes.",
            ),
            (
                "managing-observation-stays",
                "Tracks observation status criteria, time-based requirements, and conversion-to-inpatient triggers. Use when managing observation patients, determining inpatient conversion, or documenting observation criteria.",
            ),
            (
                "coordinating-social-work-needs",
                "Identifies psychosocial barriers to discharge and coordinates social work interventions. Use when assessing social needs, coordinating community resources, or planning post-discharge support.",
            ),
            (
                "documenting-informed-consent",
                "Structures informed consent documentation with risks, benefits, alternatives, and patient understanding confirmation. Use when obtaining informed consent, documenting consent discussions, or verifying consent completeness.",
            ),
            (
                "managing-fall-prevention",
                "Implements fall risk assessment (Morse, Hendrich) with intervention protocols. Use when assessing fall risk, implementing prevention strategies, or documenting fall prevention measures.",
            ),
            (
                "managing-venous-thromboembolism-prophylaxis",
                "Applies VTE risk assessment (Padua, Caprini) with appropriate prophylaxis selection. Use when assessing VTE risk, selecting prophylaxis regimens, or documenting DVT prevention.",
            ),
            (
                "tracking-hospital-acquired-conditions",
                "Monitors and documents hospital-acquired infections, pressure injuries, and other preventable conditions. Use when tracking HACs, documenting nosocomial events, or reporting patient safety indicators.",
            ),
            (
                "managing-nutrition-support",
                "Assesses nutritional status and coordinates enteral/parenteral nutrition protocols. Use when evaluating nutritional needs, initiating feeding protocols, or managing TPN orders.",
            ),
            (
                "conducting-mortality-reviews",
                "Structures mortality case reviews with root cause analysis and system improvement recommendations. Use when conducting M&M reviews, analyzing adverse outcomes, or documenting mortality cases.",
            ),
        ],
    },
    # ─── 3. PRIMARY CARE ─────────────────────────────────────────────
    "Primary Care": {
        "description": "Outpatient workflows for preventive care, chronic disease management, and wellness",
        "practice_areas": ["Family Medicine", "Internal Medicine", "Primary Care"],
        "skills": [
            (
                "conducting-annual-wellness-visits",
                "Structures Medicare Annual Wellness Visit documentation with HRA, prevention plan, and advance care planning. Use when performing wellness visits, documenting AWVs, or creating personalized prevention plans.",
            ),
            (
                "managing-hypertension",
                "Guides JNC/ACC hypertension management with staging, treatment algorithms, and monitoring schedules. Use when managing blood pressure, titrating antihypertensives, or creating hypertension care plans.",
            ),
            (
                "managing-diabetes-mellitus",
                "Structures diabetes management with ADA standards including A1c targets, medication algorithms, and complication screening. Use when managing diabetes, adjusting insulin regimens, or tracking glycemic control.",
            ),
            (
                "screening-preventive-health",
                "Applies USPSTF screening recommendations by age, sex, and risk factors. Use when ordering preventive screenings, creating screening schedules, or applying evidence-based prevention guidelines.",
            ),
            (
                "managing-chronic-pain",
                "Guides multimodal chronic pain management with opioid risk assessment and functional goals. Use when managing chronic pain, assessing opioid risk, or creating pain management plans.",
            ),
            (
                "interpreting-routine-labs",
                "Analyzes comprehensive metabolic panels, CBCs, lipid panels, and thyroid function with clinical correlation. Use when reviewing outpatient labs, identifying abnormalities, or correlating lab trends.",
            ),
            (
                "managing-depression-screening",
                "Administers and interprets PHQ-9 with severity-based treatment pathways and safety assessment. Use when screening for depression, interpreting PHQ scores, or initiating mental health treatment.",
            ),
            (
                "conducting-pre-operative-evaluations",
                "Structures pre-surgical risk assessment using ACC/AHA guidelines with cardiac and pulmonary clearance. Use when performing preop evaluations, assessing surgical risk, or providing medical clearance.",
            ),
            (
                "managing-obesity",
                "Guides comprehensive obesity management with BMI tracking, lifestyle interventions, medication options, and surgical referral criteria. Use when managing weight, counseling on obesity, or evaluating bariatric surgery candidacy.",
            ),
            (
                "managing-asthma",
                "Structures asthma management per NAEPP guidelines with stepwise therapy and action plans. Use when managing asthma, adjusting controller medications, or creating asthma action plans.",
            ),
            (
                "managing-copd",
                "Guides COPD management using GOLD classification with inhaler selection and exacerbation prevention. Use when managing COPD, selecting inhalers, or preventing exacerbations.",
            ),
            (
                "coordinating-care-transitions",
                "Manages post-hospitalization follow-up with medication reconciliation and readmission prevention. Use when following up after discharge, preventing readmissions, or coordinating transitional care.",
            ),
            (
                "managing-thyroid-disorders",
                "Guides thyroid evaluation with TSH interpretation, medication titration, and nodule workup protocols. Use when managing hypothyroidism, evaluating thyroid nodules, or adjusting levothyroxine.",
            ),
            (
                "counseling-smoking-cessation",
                "Structures 5As smoking cessation intervention with pharmacotherapy selection and motivational interviewing. Use when counseling on tobacco use, prescribing cessation aids, or documenting quit attempts.",
            ),
            (
                "managing-osteoporosis",
                "Applies FRAX scoring with DXA interpretation and treatment algorithms for bone health. Use when assessing fracture risk, interpreting bone density, or selecting osteoporosis treatment.",
            ),
            (
                "managing-chronic-kidney-disease",
                "Tracks CKD staging with eGFR trends, nephrology referral criteria, and medication adjustments. Use when managing CKD, monitoring renal function, or adjusting renally-dosed medications.",
            ),
            (
                "documenting-telemedicine-visits",
                "Structures telehealth encounter documentation with technology modality, clinical limitations, and follow-up planning. Use when documenting virtual visits, recording telemedicine encounters, or managing remote patient care.",
            ),
            (
                "managing-geriatric-assessments",
                "Conducts comprehensive geriatric assessment covering cognition, function, falls, polypharmacy, and goals. Use when evaluating elderly patients, performing geriatric assessments, or managing complex older adults.",
            ),
            (
                "managing-pediatric-well-visits",
                "Structures well-child visits with age-appropriate milestones, immunization tracking, and anticipatory guidance. Use when conducting pediatric checkups, tracking development, or documenting well-child exams.",
            ),
            (
                "managing-vaccine-schedules",
                "Applies CDC immunization schedules with catch-up protocols and contraindication screening. Use when managing vaccinations, creating catch-up schedules, or documenting immunization decisions.",
            ),
        ],
    },
    # ─── 4. SURGERY ──────────────────────────────────────────────────
    "Surgery": {
        "description": "Perioperative workflows for surgical planning, documentation, and post-operative management",
        "practice_areas": ["General Surgery", "Surgical Subspecialties"],
        "skills": [
            (
                "writing-operative-reports",
                "Creates structured operative notes with findings, technique, specimens, and estimated blood loss. Use when dictating operative reports, documenting surgical procedures, or recording intraoperative findings.",
            ),
            (
                "conducting-preoperative-planning",
                "Structures surgical planning with imaging review, risk stratification, and equipment/team requirements. Use when planning surgeries, reviewing preoperative imaging, or coordinating surgical teams.",
            ),
            (
                "managing-postoperative-orders",
                "Generates postoperative order sets with pain management, DVT prophylaxis, diet advancement, and activity progression. Use when writing post-op orders, managing surgical recovery, or creating post-procedure protocols.",
            ),
            (
                "documenting-surgical-pathology-requests",
                "Structures surgical pathology requisitions with clinical history, specimen description, and specific diagnostic questions. Use when submitting pathology specimens, writing pathology requisitions, or requesting special studies.",
            ),
            (
                "managing-surgical-complications",
                "Classifies and documents surgical complications using Clavien-Dindo grading with management protocols. Use when managing post-surgical complications, grading adverse events, or documenting complication management.",
            ),
            (
                "conducting-surgical-time-outs",
                "Structures WHO surgical safety checklist completion with sign-in, time-out, and sign-out documentation. Use when performing surgical time-outs, completing safety checklists, or documenting pre-incision verification.",
            ),
            (
                "managing-wound-care",
                "Guides wound assessment, classification, and treatment selection with documentation requirements. Use when managing surgical wounds, classifying wound types, or selecting wound care protocols.",
            ),
            (
                "writing-surgical-consultation-notes",
                "Creates structured surgical consultation responses with assessment and surgical candidacy determination. Use when responding to surgical consults, evaluating surgical candidates, or documenting surgical recommendations.",
            ),
            (
                "managing-postoperative-pain",
                "Structures multimodal pain management with ERAS protocols and opioid stewardship documentation. Use when managing post-surgical pain, implementing ERAS pathways, or tracking opioid use.",
            ),
            (
                "coordinating-surgical-scheduling",
                "Manages surgical scheduling with block time utilization, equipment needs, and team coordination. Use when scheduling surgeries, managing OR block time, or coordinating surgical resources.",
            ),
            (
                "managing-enhanced-recovery-protocols",
                "Implements ERAS pathway elements with compliance tracking across preop, intraop, and postop phases. Use when applying ERAS protocols, tracking pathway compliance, or optimizing surgical recovery.",
            ),
            (
                "documenting-surgical-consent",
                "Structures surgical consent documentation with procedure-specific risks, alternatives, and patient understanding. Use when obtaining surgical consent, documenting risk discussions, or verifying consent elements.",
            ),
            (
                "managing-drain-output",
                "Tracks surgical drain output with removal criteria and complication recognition. Use when monitoring drains, documenting drain output, or determining drain removal timing.",
            ),
            (
                "conducting-morbidity-mortality-reviews",
                "Structures surgical M&M conference presentations with case analysis and system improvement recommendations. Use when presenting M&M cases, analyzing surgical outcomes, or documenting quality improvement.",
            ),
            (
                "managing-surgical-site-infections",
                "Classifies SSIs using CDC criteria with treatment protocols and reporting requirements. Use when identifying surgical infections, classifying SSI depth, or implementing SSI treatment.",
            ),
            (
                "documenting-trauma-surgery",
                "Creates trauma surgery documentation with injury severity scoring and damage control principles. Use when documenting trauma operations, calculating ISS, or recording damage control sequences.",
            ),
            (
                "managing-bariatric-surgery-pathways",
                "Structures bariatric surgery evaluation with insurance requirements, preoperative optimization, and post-surgical nutrition protocols. Use when evaluating bariatric candidates, documenting insurance criteria, or managing post-bariatric care.",
            ),
            (
                "managing-transplant-evaluations",
                "Guides transplant candidacy evaluation with organ-specific criteria and listing documentation. Use when evaluating transplant candidates, documenting listing criteria, or coordinating transplant workups.",
            ),
            (
                "writing-discharge-instructions-surgical",
                "Creates procedure-specific discharge instructions with activity restrictions, wound care, and return precautions. Use when writing post-surgical discharge instructions, creating patient education materials, or documenting surgical aftercare.",
            ),
            (
                "managing-robotic-surgery-documentation",
                "Documents robotic-assisted procedures with system setup, docking, console time, and conversion criteria. Use when documenting robotic procedures, recording system parameters, or noting robotic-specific complications.",
            ),
        ],
    },
    # ─── 5. DIAGNOSTIC IMAGING / RADIOLOGY ───────────────────────────
    "Radiology": {
        "description": "Imaging interpretation, reporting, and workflow management",
        "practice_areas": ["Radiology", "Diagnostic Imaging"],
        "skills": [
            (
                "reporting-chest-radiographs",
                "Structures systematic chest X-ray interpretation with standardized reporting and critical findings communication. Use when reading chest X-rays, creating radiology reports, or documenting CXR findings.",
            ),
            (
                "reporting-ct-scans",
                "Structures CT scan interpretation by body region with standardized measurement and comparison techniques. Use when interpreting CT studies, creating CT reports, or documenting cross-sectional findings.",
            ),
            (
                "reporting-mri-studies",
                "Structures MRI interpretation with sequence-specific analysis and standardized reporting. Use when reading MRI studies, creating MRI reports, or analyzing multisequence findings.",
            ),
            (
                "reporting-ultrasound-studies",
                "Structures ultrasound interpretation with measurement protocols and ACR guidelines. Use when reading ultrasound exams, documenting sonographic findings, or creating US reports.",
            ),
            (
                "classifying-imaging-findings",
                "Applies standardized classification systems (BI-RADS, LI-RADS, TI-RADS, Lung-RADS, PI-RADS) to imaging findings. Use when categorizing imaging findings, applying RADS classifications, or determining follow-up recommendations.",
            ),
            (
                "tracking-incidental-findings",
                "Manages incidental finding follow-up using ACR White Paper recommendations. Use when tracking incidentalomas, scheduling follow-up imaging, or managing unexpected findings.",
            ),
            (
                "protocolling-imaging-studies",
                "Selects appropriate imaging protocols based on clinical indication and patient factors. Use when choosing imaging protocols, selecting contrast parameters, or determining appropriate study type.",
            ),
            (
                "measuring-tumor-response",
                "Applies RECIST 1.1 and iRECIST criteria for tumor measurement and treatment response assessment. Use when measuring tumor response, applying RECIST criteria, or documenting treatment effects.",
            ),
            (
                "documenting-critical-results",
                "Structures critical result communication with documentation requirements and closed-loop verification. Use when communicating critical findings, documenting urgent results, or verifying critical result acknowledgment.",
            ),
            (
                "interpreting-musculoskeletal-imaging",
                "Structures MSK imaging interpretation with fracture classification and joint assessment protocols. Use when reading MSK imaging, classifying fractures, or documenting orthopedic findings.",
            ),
            (
                "interpreting-neuroradiology",
                "Structures brain and spine imaging interpretation with stroke, mass, and degenerative disease assessment. Use when reading neuroimaging, evaluating stroke imaging, or documenting intracranial findings.",
            ),
            (
                "managing-contrast-reactions",
                "Guides contrast reaction grading, treatment, and premedication protocols for future studies. Use when managing contrast reactions, planning premedication, or documenting adverse contrast events.",
            ),
            (
                "performing-image-guided-procedures",
                "Documents image-guided biopsy, drainage, and injection procedures with technique and specimens. Use when performing IR procedures, documenting image-guided interventions, or recording procedural details.",
            ),
            (
                "reviewing-prior-comparisons",
                "Structures comparison with prior imaging studies to identify interval changes and trends. Use when comparing imaging studies, identifying interval changes, or tracking disease progression.",
            ),
            (
                "managing-radiation-dose",
                "Tracks and optimizes radiation exposure using reference levels and ALARA principles. Use when monitoring radiation dose, optimizing CT protocols, or documenting dose reduction efforts.",
            ),
            (
                "interpreting-pediatric-imaging",
                "Adapts imaging interpretation for pediatric anatomy with age-appropriate normal variants. Use when reading pediatric imaging, differentiating normal variants, or documenting pediatric-specific findings.",
            ),
            (
                "reporting-nuclear-medicine-studies",
                "Structures nuclear medicine and PET/CT interpretation with SUV measurement and staging correlation. Use when reading nuclear medicine studies, interpreting PET findings, or documenting radiotracer uptake.",
            ),
            (
                "performing-quality-assurance-reviews",
                "Structures radiology peer review and quality assurance with discrepancy classification. Use when conducting peer review, classifying discrepancies, or documenting QA findings.",
            ),
            (
                "managing-radiology-worklists",
                "Prioritizes and triages radiology worklists based on clinical urgency and study type. Use when managing reading worklists, prioritizing urgent studies, or optimizing radiology workflow.",
            ),
            (
                "creating-teaching-files",
                "Curates and annotates imaging cases for educational purposes with clinical correlation. Use when creating teaching files, annotating educational cases, or building case libraries.",
            ),
        ],
    },
    # ─── 6. PATHOLOGY / LABORATORY MEDICINE ──────────────────────────
    "Pathology": {
        "description": "Laboratory analysis, tissue diagnosis, and quality workflows",
        "practice_areas": ["Pathology", "Laboratory Medicine"],
        "skills": [
            (
                "interpreting-surgical-pathology",
                "Structures surgical pathology reports with diagnosis, staging, margins, and prognostic markers. Use when interpreting biopsies, creating pathology reports, or documenting tissue diagnoses.",
            ),
            (
                "interpreting-cytology-specimens",
                "Structures cytology interpretation with Bethesda system for cervical and other body site classifications. Use when reading cytology, applying Bethesda classifications, or documenting cytologic findings.",
            ),
            (
                "analyzing-flow-cytometry",
                "Interprets flow cytometry panels for hematologic malignancy classification and minimal residual disease. Use when analyzing flow cytometry, classifying lymphomas/leukemias, or documenting immunophenotyping.",
            ),
            (
                "interpreting-molecular-pathology",
                "Structures molecular test interpretation including NGS panels, FISH, and PCR-based assays. Use when interpreting molecular results, reporting genetic variants, or documenting molecular findings.",
            ),
            (
                "managing-blood-bank-compatibility",
                "Guides blood product compatibility testing with antibody identification and crossmatch protocols. Use when managing blood bank testing, resolving antibody workups, or selecting compatible products.",
            ),
            (
                "interpreting-coagulation-studies",
                "Structures coagulation test interpretation with mixing studies and inhibitor identification. Use when interpreting coag panels, evaluating bleeding disorders, or analyzing mixing study results.",
            ),
            (
                "performing-autopsy-protocols",
                "Structures autopsy examination with organ system review, cause-of-death determination, and documentation. Use when performing autopsies, documenting autopsy findings, or determining cause of death.",
            ),
            (
                "managing-laboratory-quality-control",
                "Tracks QC data with Westgard rules and corrective action documentation. Use when managing lab QC, interpreting Westgard violations, or documenting corrective actions.",
            ),
            (
                "interpreting-microbiology-cultures",
                "Structures microbiology result interpretation with susceptibility patterns and resistance mechanisms. Use when reading culture results, interpreting susceptibility data, or identifying resistance patterns.",
            ),
            (
                "staging-malignancies",
                "Applies AJCC/UICC TNM staging with pathologic parameters and prognostic groupings. Use when staging cancers, applying TNM criteria, or documenting pathologic staging.",
            ),
            (
                "interpreting-immunohistochemistry",
                "Guides IHC panel selection and interpretation for tumor classification and prognostication. Use when ordering IHC panels, interpreting staining patterns, or classifying tumors by immunophenotype.",
            ),
            (
                "validating-new-laboratory-tests",
                "Structures test validation with precision, accuracy, linearity, and reference range establishment. Use when validating new assays, documenting method comparisons, or establishing reference ranges.",
            ),
            (
                "managing-specimen-integrity",
                "Evaluates specimen adequacy and rejection criteria with pre-analytical quality documentation. Use when assessing specimen quality, documenting rejection reasons, or managing pre-analytical errors.",
            ),
            (
                "interpreting-urinalysis",
                "Structures complete urinalysis interpretation with microscopy correlation and clinical significance. Use when interpreting UA results, correlating microscopy findings, or evaluating renal function markers.",
            ),
            (
                "interpreting-hematology-smears",
                "Structures peripheral blood smear review with morphologic descriptions and differential correlation. Use when reading blood smears, describing cell morphology, or correlating with CBC findings.",
            ),
            (
                "managing-critical-laboratory-values",
                "Tracks critical value notification with documentation requirements and clinical correlation. Use when reporting critical lab values, verifying notification, or documenting critical result acknowledgment.",
            ),
            (
                "interpreting-genetic-testing",
                "Structures genetic test result interpretation with variant classification (ACMG criteria) and clinical actionability. Use when interpreting genetic results, classifying variants, or documenting genetic findings.",
            ),
            (
                "managing-proficiency-testing",
                "Tracks proficiency testing results with remediation for unacceptable performance. Use when managing PT programs, analyzing PT results, or documenting corrective actions for PT failures.",
            ),
            (
                "interpreting-toxicology-screens",
                "Structures drug screen interpretation with confirmation testing and clinical correlation. Use when interpreting drug screens, managing confirmatory testing, or documenting toxicology results.",
            ),
            (
                "performing-frozen-section-analysis",
                "Guides intraoperative frozen section evaluation with rapid diagnostic protocols and communication. Use when performing frozen sections, providing intraoperative diagnoses, or communicating preliminary results.",
            ),
        ],
    },
    # ─── 7. PHARMACY / MEDICATION MANAGEMENT ─────────────────────────
    "Pharmacy": {
        "description": "Medication management, formulary decisions, and pharmaceutical care workflows",
        "practice_areas": ["Clinical Pharmacy", "Pharmacy"],
        "skills": [
            (
                "assessing-drug-interactions",
                "Identifies clinically significant drug-drug, drug-food, and drug-disease interactions with severity grading and management recommendations. Use when checking drug interactions, evaluating polypharmacy risks, or managing medication combinations.",
            ),
            (
                "managing-anticoagulation-therapy",
                "Guides anticoagulation selection, dosing, monitoring, and bridging protocols. Use when managing warfarin, DOACs, or heparin therapy, or planning periprocedural anticoagulation.",
            ),
            (
                "conducting-antimicrobial-stewardship",
                "Reviews antibiotic appropriateness with spectrum optimization, de-escalation, and duration recommendations. Use when reviewing antibiotic use, recommending de-escalation, or conducting antibiotic time-outs.",
            ),
            (
                "managing-pharmacokinetic-dosing",
                "Calculates individualized drug doses using pharmacokinetic parameters (vancomycin, aminoglycosides, phenytoin). Use when performing PK calculations, adjusting drug levels, or calculating loading/maintenance doses.",
            ),
            (
                "reviewing-medication-safety",
                "Identifies high-alert medication risks with ISMP guidelines and safety barriers. Use when reviewing high-risk medications, implementing safety checks, or preventing medication errors.",
            ),
            (
                "managing-formulary-evaluations",
                "Structures drug formulary reviews with efficacy, safety, cost-effectiveness, and therapeutic interchange analysis. Use when evaluating formulary additions, conducting P&T reviews, or analyzing therapeutic alternatives.",
            ),
            (
                "reconciling-medications",
                "Compares medication lists across care settings to identify discrepancies, duplications, and omissions. Use when performing medication reconciliation, identifying med discrepancies, or verifying discharge prescriptions.",
            ),
            (
                "managing-controlled-substances",
                "Tracks controlled substance prescribing with PDMP review, risk assessment, and compliance monitoring. Use when managing controlled substances, reviewing PDMP data, or monitoring opioid prescribing.",
            ),
            (
                "managing-chemotherapy-protocols",
                "Verifies chemotherapy orders against regimen protocols with dose calculations and toxicity monitoring. Use when reviewing chemo orders, calculating BSA-based doses, or tracking treatment toxicity.",
            ),
            (
                "managing-parenteral-nutrition",
                "Structures TPN order review with macronutrient calculations, compatibility checks, and monitoring protocols. Use when reviewing TPN orders, calculating nutrition requirements, or managing parenteral feeding.",
            ),
            (
                "counseling-patient-education",
                "Structures medication counseling with key points, administration instructions, and adherence strategies. Use when counseling patients on medications, creating medication guides, or preparing patient education materials.",
            ),
            (
                "managing-adverse-drug-reactions",
                "Classifies and documents adverse drug reactions with causality assessment (Naranjo) and reporting. Use when evaluating ADRs, assessing drug causality, or reporting adverse events.",
            ),
            (
                "converting-medication-routes",
                "Calculates IV-to-oral conversions and opioid equianalgesic dosing. Use when converting medication routes, calculating equianalgesic doses, or transitioning IV to oral therapy.",
            ),
            (
                "managing-renal-dose-adjustments",
                "Adjusts medication doses based on renal function using CrCl/eGFR calculations. Use when adjusting for renal impairment, calculating CrCl-based doses, or managing medications in kidney disease.",
            ),
            (
                "managing-hepatic-dose-adjustments",
                "Guides medication adjustments for hepatic impairment using Child-Pugh classification. Use when adjusting for liver disease, evaluating hepatic metabolism, or managing medications in cirrhosis.",
            ),
            (
                "reviewing-biosimilar-interchangeability",
                "Evaluates biosimilar products for therapeutic interchange with clinical evidence review. Use when evaluating biosimilars, planning therapeutic switches, or analyzing biosimilar evidence.",
            ),
            (
                "managing-drug-shortages",
                "Identifies therapeutic alternatives during drug shortages with clinical equivalence assessment. Use when managing drug shortages, finding alternative therapies, or implementing shortage protocols.",
            ),
            (
                "managing-medication-use-evaluations",
                "Structures medication use evaluations with criteria development, data collection, and intervention tracking. Use when conducting MUEs, evaluating prescribing patterns, or measuring medication use quality.",
            ),
            (
                "managing-immunization-protocols",
                "Guides immunization administration with screening, scheduling, and documentation requirements. Use when administering vaccines, screening for contraindications, or documenting immunizations.",
            ),
            (
                "managing-pain-management-protocols",
                "Structures multimodal pain management with non-opioid-first approaches and patient-controlled analgesia. Use when managing acute pain, implementing PCA protocols, or designing multimodal pain regimens.",
            ),
        ],
    },
    # ─── 8. ONCOLOGY ─────────────────────────────────────────────────
    "Oncology": {
        "description": "Cancer care workflows from diagnosis through treatment and survivorship",
        "practice_areas": [
            "Medical Oncology",
            "Hematology-Oncology",
            "Radiation Oncology",
        ],
        "skills": [
            (
                "staging-cancer-diagnoses",
                "Applies AJCC 8th edition TNM staging with pathologic and clinical stage documentation. Use when staging cancers, applying TNM classifications, or documenting cancer stage.",
            ),
            (
                "reviewing-treatment-protocols",
                "Evaluates NCCN guideline-concordant treatment plans with evidence levels and alternatives. Use when reviewing cancer treatment plans, checking NCCN compliance, or evaluating treatment options.",
            ),
            (
                "managing-chemotherapy-toxicity",
                "Grades treatment toxicity using CTCAE v5.0 with dose modification and supportive care protocols. Use when grading chemo toxicity, applying CTCAE criteria, or managing treatment side effects.",
            ),
            (
                "interpreting-tumor-markers",
                "Tracks tumor marker trends with diagnostic and monitoring interpretive frameworks. Use when tracking tumor markers, interpreting biomarker trends, or monitoring treatment response.",
            ),
            (
                "documenting-tumor-board-presentations",
                "Structures multidisciplinary tumor board case presentations with radiology, pathology, and treatment synthesis. Use when preparing tumor board cases, presenting MDT discussions, or documenting consensus recommendations.",
            ),
            (
                "managing-clinical-trial-eligibility",
                "Screens patients against clinical trial inclusion/exclusion criteria with documentation. Use when screening trial candidates, checking eligibility criteria, or documenting trial enrollment decisions.",
            ),
            (
                "managing-survivorship-care",
                "Creates survivorship care plans with surveillance schedules, late effects monitoring, and wellness recommendations. Use when creating survivorship plans, scheduling cancer surveillance, or documenting long-term follow-up.",
            ),
            (
                "managing-palliative-care-integration",
                "Guides palliative care consultation timing and symptom management integration with curative therapy. Use when integrating palliative care, managing cancer symptoms, or coordinating concurrent curative and palliative treatment.",
            ),
            (
                "calculating-performance-status",
                "Documents ECOG and Karnofsky performance status with treatment eligibility implications. Use when assessing performance status, documenting ECOG scores, or evaluating treatment candidacy.",
            ),
            (
                "managing-radiation-therapy-planning",
                "Structures radiation treatment planning documentation with dose constraints and target volumes. Use when documenting radiation plans, reviewing dose constraints, or coordinating radiation therapy.",
            ),
            (
                "managing-immunotherapy-protocols",
                "Guides immune checkpoint inhibitor management with irAE recognition and grading. Use when managing immunotherapy, monitoring for irAEs, or treating immune-related toxicity.",
            ),
            (
                "interpreting-genomic-profiling",
                "Structures comprehensive genomic profiling interpretation with actionable mutations and matched therapies. Use when reviewing genomic test results, identifying targeted therapy options, or interpreting NGS panels.",
            ),
            (
                "managing-bone-marrow-transplant",
                "Guides BMT/SCT workflow from conditioning through engraftment monitoring and GVHD assessment. Use when managing transplant patients, monitoring engraftment, or assessing GVHD.",
            ),
            (
                "managing-cancer-pain",
                "Structures cancer pain assessment with WHO ladder application and breakthrough dosing. Use when managing cancer pain, titrating opioids, or implementing cancer pain protocols.",
            ),
            (
                "documenting-cancer-registry",
                "Abstracts cancer cases for registry submission with required data elements and coding standards. Use when abstracting cancer cases, coding registry data, or documenting cancer reporting.",
            ),
            (
                "managing-oncologic-emergencies",
                "Guides recognition and management of spinal cord compression, tumor lysis, SVC syndrome, and hypercalcemia. Use when managing oncologic emergencies, treating tumor lysis, or recognizing cord compression.",
            ),
            (
                "coordinating-multidisciplinary-cancer-care",
                "Synthesizes surgical, medical, and radiation oncology inputs into coordinated treatment timelines. Use when coordinating multimodal treatment, scheduling sequential therapies, or managing treatment timelines.",
            ),
            (
                "managing-end-of-life-care",
                "Guides end-of-life transitions with hospice referral criteria, comfort care protocols, and family communication. Use when transitioning to end-of-life care, initiating hospice, or managing comfort-focused treatment.",
            ),
            (
                "tracking-treatment-response",
                "Monitors treatment response using imaging criteria, biomarkers, and clinical assessment with documentation. Use when assessing treatment response, documenting disease status, or tracking progression.",
            ),
            (
                "managing-hereditary-cancer-syndromes",
                "Guides hereditary cancer risk assessment with genetic testing criteria and management recommendations. Use when evaluating hereditary cancer risk, ordering genetic testing, or managing high-risk patients.",
            ),
        ],
    },
    # ─── 9. MENTAL HEALTH / PSYCHIATRY ───────────────────────────────
    "Psychiatry": {
        "description": "Mental health assessment, treatment planning, and crisis management",
        "practice_areas": ["Psychiatry", "Psychology", "Behavioral Health"],
        "skills": [
            (
                "conducting-psychiatric-evaluations",
                "Structures comprehensive psychiatric evaluation with MSE, diagnostic formulation, and risk assessment. Use when performing psychiatric assessments, documenting mental status exams, or creating diagnostic formulations.",
            ),
            (
                "assessing-suicide-risk",
                "Applies Columbia Suicide Severity Rating Scale and structured risk assessment frameworks. Use when assessing suicide risk, documenting safety evaluations, or creating safety plans.",
            ),
            (
                "managing-psychotropic-medications",
                "Guides psychotropic prescribing with evidence-based selection, monitoring, and titration schedules. Use when selecting psychotropics, managing medication trials, or documenting psychiatric pharmacotherapy.",
            ),
            (
                "documenting-mental-status-exams",
                "Creates structured MSE documentation covering appearance, behavior, speech, mood, thought, cognition, and insight. Use when documenting mental status, writing MSE sections, or describing psychiatric findings.",
            ),
            (
                "creating-treatment-plans-psychiatric",
                "Structures psychiatric treatment plans with diagnoses, goals, interventions, and measurable outcomes. Use when creating psychiatric treatment plans, setting therapeutic goals, or documenting treatment modalities.",
            ),
            (
                "managing-involuntary-commitments",
                "Guides involuntary hold documentation with dangerousness criteria and patient rights requirements. Use when initiating involuntary holds, documenting commitment criteria, or managing psychiatric detentions.",
            ),
            (
                "conducting-cognitive-assessments",
                "Administers and interprets cognitive screening tools (MoCA, MMSE, SLUMS) with dementia evaluation. Use when screening for cognitive impairment, administering MoCA/MMSE, or evaluating dementia.",
            ),
            (
                "managing-substance-use-disorders",
                "Structures SUD assessment with ASAM criteria placement, MAT protocols, and recovery planning. Use when assessing substance use, applying ASAM criteria, or managing medication-assisted treatment.",
            ),
            (
                "conducting-forensic-evaluations",
                "Structures forensic psychiatric evaluations for competency, insanity, and civil commitment proceedings. Use when performing forensic evaluations, assessing competency, or documenting forensic opinions.",
            ),
            (
                "managing-eating-disorders",
                "Guides eating disorder assessment with medical stability criteria and treatment level determination. Use when evaluating eating disorders, assessing medical stability, or determining treatment level.",
            ),
            (
                "managing-adhd-assessments",
                "Structures ADHD evaluation with symptom scales, behavioral observation, and differential diagnosis. Use when evaluating ADHD, administering rating scales, or documenting ADHD assessments.",
            ),
            (
                "managing-psychological-trauma-assessments",
                "Guides trauma-informed assessment with PTSD screening and trauma history documentation. Use when assessing trauma exposure, screening for PTSD, or documenting trauma history.",
            ),
            (
                "managing-electroconvulsive-therapy",
                "Documents ECT treatment parameters, seizure quality, and cognitive monitoring protocols. Use when managing ECT treatments, documenting treatment parameters, or monitoring ECT outcomes.",
            ),
            (
                "managing-acute-psychiatric-crises",
                "Guides acute agitation management with de-escalation and emergency medication protocols. Use when managing psychiatric crises, treating acute agitation, or implementing emergency interventions.",
            ),
            (
                "conducting-capacity-evaluations",
                "Assesses medical decision-making capacity with Appelbaum criteria documentation. Use when evaluating decision-making capacity, documenting capacity assessments, or determining informed consent ability.",
            ),
            (
                "managing-child-psychiatry",
                "Adapts psychiatric evaluation and treatment for pediatric patients with developmental considerations. Use when evaluating children psychiatrically, managing pediatric medications, or documenting child psychiatric assessments.",
            ),
            (
                "managing-geriatric-psychiatry",
                "Addresses psychiatric care in elderly patients with medical comorbidity and polypharmacy considerations. Use when managing psychiatric conditions in elderly, evaluating behavioral disturbances, or adjusting geriatric psychotropics.",
            ),
            (
                "documenting-psychotherapy-notes",
                "Structures psychotherapy documentation meeting billing and clinical requirements. Use when documenting therapy sessions, writing progress notes, or recording psychotherapy interventions.",
            ),
            (
                "managing-psychiatric-consultation-liaison",
                "Structures C-L psychiatry assessments for medical-surgical inpatients with delirium, capacity, and behavioral concerns. Use when performing psych consults on medical floors, assessing delirium, or managing behavioral issues in medical patients.",
            ),
            (
                "managing-disability-evaluations",
                "Structures psychiatric disability assessments with functional limitations and work capacity documentation. Use when evaluating psychiatric disability, documenting functional limitations, or completing disability forms.",
            ),
        ],
    },
    # ─── 10. CARDIOLOGY ──────────────────────────────────────────────
    "Cardiology": {
        "description": "Cardiovascular assessment, intervention, and chronic management workflows",
        "practice_areas": [
            "Cardiology",
            "Interventional Cardiology",
            "Electrophysiology",
        ],
        "skills": [
            (
                "interpreting-electrocardiograms",
                "Systematically interprets 12-lead ECGs with rate, rhythm, axis, intervals, and morphology analysis. Use when reading ECGs, documenting EKG interpretations, or identifying cardiac arrhythmias.",
            ),
            (
                "interpreting-echocardiograms",
                "Structures echocardiographic interpretation with chamber measurements, valve assessment, and functional parameters. Use when reading echo reports, documenting cardiac function, or evaluating valve disease.",
            ),
            (
                "managing-heart-failure",
                "Guides GDMT optimization for HFrEF and HFpEF with medication titration and monitoring schedules. Use when managing heart failure, titrating GDMT, or optimizing HF medications.",
            ),
            (
                "managing-atrial-fibrillation",
                "Structures AF management with CHA2DS2-VASc scoring, anticoagulation selection, and rate/rhythm control strategies. Use when managing AFib, calculating stroke risk, or selecting anticoagulation.",
            ),
            (
                "interpreting-cardiac-catheterization",
                "Structures cath lab report interpretation with hemodynamics, angiographic findings, and intervention documentation. Use when reviewing cath reports, documenting PCI procedures, or interpreting hemodynamic data.",
            ),
            (
                "managing-acute-coronary-syndromes",
                "Guides ACS management pathways with TIMI/GRACE scoring and intervention timing. Use when managing STEMI/NSTEMI, risk-stratifying ACS, or coordinating cath lab activation.",
            ),
            (
                "managing-cardiac-devices",
                "Interprets pacemaker and ICD interrogation data with programming optimization documentation. Use when reviewing device interrogations, managing pacemaker settings, or documenting ICD therapies.",
            ),
            (
                "conducting-stress-test-interpretation",
                "Interprets exercise and pharmacologic stress tests with Duke treadmill score and nuclear findings. Use when reading stress tests, interpreting nuclear perfusion, or documenting exercise tolerance.",
            ),
            (
                "managing-valvular-heart-disease",
                "Guides valve disease severity assessment with intervention criteria and surveillance schedules. Use when evaluating valve disease, assessing surgical/interventional timing, or monitoring valve function.",
            ),
            (
                "managing-cardiac-rehabilitation",
                "Structures cardiac rehab prescriptions with exercise parameters and risk stratification. Use when prescribing cardiac rehab, setting exercise targets, or monitoring rehab progress.",
            ),
            (
                "managing-lipid-therapy",
                "Guides statin selection and intensity with ASCVD risk calculation and LDL targets. Use when managing lipids, calculating cardiovascular risk, or optimizing lipid-lowering therapy.",
            ),
            (
                "managing-hypertensive-emergencies",
                "Guides urgent blood pressure management with target reduction rates and IV medication protocols. Use when managing hypertensive crises, selecting IV antihypertensives, or monitoring acute BP reduction.",
            ),
            (
                "interpreting-ambulatory-monitoring",
                "Structures Holter and event monitor interpretation with arrhythmia burden quantification. Use when reading Holter monitors, interpreting event recorders, or quantifying arrhythmia burden.",
            ),
            (
                "managing-peripheral-vascular-disease",
                "Guides PVD assessment with ABI interpretation and intervention referral criteria. Use when evaluating peripheral vascular disease, interpreting ABI studies, or managing claudication.",
            ),
            (
                "managing-pulmonary-hypertension",
                "Structures PH evaluation with right heart catheterization interpretation and treatment classification. Use when evaluating pulmonary hypertension, interpreting RHC data, or classifying PH by WHO group.",
            ),
            (
                "managing-cardiac-imaging-protocols",
                "Selects appropriate cardiac imaging modality based on clinical question and pretest probability. Use when choosing cardiac imaging, selecting stress testing modality, or ordering cardiac CT/MRI.",
            ),
            (
                "managing-endocarditis-workup",
                "Guides endocarditis evaluation using modified Duke criteria with blood culture timing and imaging. Use when evaluating for endocarditis, applying Duke criteria, or coordinating endocarditis workup.",
            ),
            (
                "managing-aortic-disease",
                "Guides aortic aneurysm and dissection evaluation with surveillance intervals and intervention thresholds. Use when monitoring aortic aneurysms, evaluating aortic dissection, or determining intervention timing.",
            ),
            (
                "managing-cardiac-risk-preoperative",
                "Applies ACC/AHA perioperative cardiac evaluation algorithm with functional capacity and risk indices. Use when performing cardiac preop evaluation, calculating RCRI, or assessing perioperative cardiac risk.",
            ),
            (
                "managing-congenital-heart-disease-adults",
                "Structures ACHD evaluation with lesion-specific monitoring and pregnancy risk assessment. Use when managing adult congenital heart disease, evaluating ACHD patients, or assessing pregnancy risk in CHD.",
            ),
        ],
    },
    # ─── 11. OBSTETRICS & GYNECOLOGY ─────────────────────────────────
    "Obstetrics and Gynecology": {
        "description": "Reproductive health workflows from prenatal care through gynecologic oncology",
        "practice_areas": ["Obstetrics", "Gynecology", "Maternal-Fetal Medicine"],
        "skills": [
            (
                "managing-prenatal-care",
                "Structures prenatal visit documentation with gestational age tracking, screening schedules, and risk assessment. Use when documenting prenatal visits, tracking pregnancy milestones, or managing prenatal screening.",
            ),
            (
                "interpreting-fetal-monitoring",
                "Interprets electronic fetal monitoring using NICHD nomenclature with category classification and intervention criteria. Use when reading fetal heart tracings, classifying EFM patterns, or documenting intrapartum monitoring.",
            ),
            (
                "managing-labor-and-delivery",
                "Structures labor documentation with cervical change tracking, partogram management, and delivery summary. Use when managing labor progress, documenting cervical exams, or creating delivery summaries.",
            ),
            (
                "documenting-cesarean-sections",
                "Creates structured C-section operative reports with indication, technique, and estimated blood loss. Use when documenting cesarean deliveries, recording operative findings, or writing C-section reports.",
            ),
            (
                "managing-high-risk-pregnancies",
                "Guides management of preeclampsia, gestational diabetes, and other high-risk conditions with monitoring protocols. Use when managing high-risk pregnancies, monitoring preeclampsia, or managing GDM.",
            ),
            (
                "managing-postpartum-care",
                "Structures postpartum assessment with hemorrhage risk, lactation support, and mood screening. Use when managing postpartum recovery, screening for PPD, or documenting postpartum visits.",
            ),
            (
                "managing-gynecologic-screening",
                "Applies ASCCP cervical cancer screening guidelines with HPV co-testing and colposcopy indications. Use when managing cervical screening, applying ASCCP guidelines, or determining colposcopy need.",
            ),
            (
                "managing-contraception-counseling",
                "Guides contraception selection with medical eligibility criteria (MEC) and effectiveness counseling. Use when counseling on contraception, applying MEC categories, or selecting appropriate methods.",
            ),
            (
                "managing-menopause",
                "Structures menopause evaluation and hormone therapy decision-making with risk-benefit analysis. Use when managing menopausal symptoms, evaluating HRT candidacy, or documenting menopause management.",
            ),
            (
                "managing-abnormal-uterine-bleeding",
                "Guides AUB evaluation using PALM-COEIN classification with workup algorithms. Use when evaluating abnormal bleeding, applying PALM-COEIN classification, or managing AUB workup.",
            ),
            (
                "managing-pelvic-pain",
                "Structures pelvic pain evaluation with differential diagnosis and endometriosis assessment. Use when evaluating chronic pelvic pain, assessing for endometriosis, or managing pelvic pain workup.",
            ),
            (
                "managing-fertility-evaluations",
                "Structures infertility workup with ovarian reserve testing, semen analysis, and treatment algorithms. Use when evaluating infertility, ordering fertility workup, or managing reproductive planning.",
            ),
            (
                "managing-ectopic-pregnancy",
                "Guides ectopic pregnancy evaluation with beta-hCG trending and management algorithms. Use when evaluating ectopic pregnancy, trending beta-hCG, or managing ectopic treatment decisions.",
            ),
            (
                "managing-gynecologic-oncology",
                "Structures gynecologic cancer evaluation with staging, treatment planning, and surveillance. Use when managing gynecologic cancers, staging ovarian/uterine malignancies, or planning treatment.",
            ),
            (
                "managing-miscarriage",
                "Guides miscarriage evaluation with ultrasound criteria and management options documentation. Use when managing pregnancy loss, documenting miscarriage evaluation, or counseling on management options.",
            ),
            (
                "managing-sexually-transmitted-infections",
                "Guides STI screening, treatment, and partner notification using CDC guidelines. Use when managing STIs, selecting treatment regimens, or documenting STI screening.",
            ),
            (
                "documenting-ultrasound-obstetric",
                "Structures obstetric ultrasound reporting with biometry, anatomy survey, and growth assessment. Use when reporting OB ultrasounds, documenting fetal anatomy, or tracking fetal growth.",
            ),
            (
                "managing-gestational-diabetes",
                "Guides GDM screening, glucose monitoring, and insulin therapy with delivery timing criteria. Use when managing gestational diabetes, interpreting glucose logs, or planning GDM delivery timing.",
            ),
            (
                "managing-breastfeeding-support",
                "Structures lactation assessment with latch evaluation and common problem management. Use when assessing breastfeeding, managing lactation difficulties, or documenting lactation support.",
            ),
            (
                "managing-pelvic-floor-disorders",
                "Guides pelvic floor assessment with POP-Q staging and treatment algorithm documentation. Use when evaluating pelvic organ prolapse, staging PFDs, or managing incontinence.",
            ),
        ],
    },
    # ─── 12. PEDIATRICS ──────────────────────────────────────────────
    "Pediatrics": {
        "description": "Child and adolescent health workflows from newborn through adolescence",
        "practice_areas": ["Pediatrics", "Neonatology", "Adolescent Medicine"],
        "skills": [
            (
                "managing-newborn-assessments",
                "Structures newborn examination with Apgar scoring, gestational age assessment, and initial screening. Use when examining newborns, documenting birth assessments, or performing initial newborn evaluations.",
            ),
            (
                "tracking-developmental-milestones",
                "Applies ASQ and CDC milestone tracking with referral criteria for developmental delays. Use when tracking development, screening for delays, or documenting milestone achievement.",
            ),
            (
                "managing-neonatal-intensive-care",
                "Structures NICU documentation with ventilation parameters, feeding advancement, and discharge readiness criteria. Use when managing NICU patients, documenting ventilator settings, or tracking feeding progression.",
            ),
            (
                "managing-pediatric-asthma",
                "Applies stepwise pediatric asthma management with age-appropriate device selection and action plans. Use when managing childhood asthma, selecting pediatric inhalers, or creating asthma action plans.",
            ),
            (
                "managing-pediatric-infections",
                "Guides pediatric infection management with weight-based dosing and duration recommendations. Use when treating pediatric infections, calculating weight-based antibiotics, or managing common childhood infections.",
            ),
            (
                "managing-immunization-schedules",
                "Applies CDC pediatric immunization schedule with catch-up protocols and contraindication screening. Use when managing pediatric vaccines, scheduling catch-up immunizations, or screening for contraindications.",
            ),
            (
                "managing-failure-to-thrive",
                "Structures FTT evaluation with growth curve analysis, caloric calculations, and workup algorithms. Use when evaluating poor growth, calculating caloric needs, or managing failure to thrive.",
            ),
            (
                "managing-childhood-obesity",
                "Guides pediatric weight management with BMI percentile tracking and family-based interventions. Use when managing childhood obesity, tracking BMI percentiles, or implementing weight management plans.",
            ),
            (
                "screening-adolescent-health",
                "Structures adolescent well-visit with HEEADSSS assessment and confidential health screening. Use when conducting adolescent visits, performing HEEADSSS screening, or managing teen health concerns.",
            ),
            (
                "managing-pediatric-fever",
                "Guides age-stratified fever evaluation with Rochester, Philadelphia, and step-by-step protocols. Use when evaluating febrile infants, applying fever protocols, or managing pediatric fever workup.",
            ),
            (
                "managing-jaundice-neonatal",
                "Applies AAP hyperbilirubinemia guidelines with phototherapy thresholds and Bhutani nomogram. Use when managing neonatal jaundice, interpreting bilirubin levels, or determining phototherapy need.",
            ),
            (
                "managing-pediatric-diabetes",
                "Guides type 1 diabetes management in children with insulin adjustment algorithms and school plans. Use when managing pediatric T1DM, adjusting insulin doses, or creating diabetes school plans.",
            ),
            (
                "managing-pediatric-seizures",
                "Structures seizure evaluation with EEG interpretation and anticonvulsant selection for pediatric populations. Use when evaluating pediatric seizures, interpreting pediatric EEGs, or selecting anticonvulsants for children.",
            ),
            (
                "managing-child-abuse-screening",
                "Guides child maltreatment assessment with mandatory reporting documentation and forensic considerations. Use when screening for child abuse, documenting suspicious injuries, or completing mandatory reports.",
            ),
            (
                "managing-attention-deficit-disorders",
                "Structures ADHD evaluation in children with behavioral rating scales and medication trials. Use when evaluating pediatric ADHD, interpreting Vanderbilt/Conners scales, or managing stimulant therapy.",
            ),
            (
                "managing-allergic-conditions-pediatric",
                "Guides pediatric allergy evaluation with testing interpretation and immunotherapy considerations. Use when evaluating pediatric allergies, interpreting allergy testing, or managing food allergy action plans.",
            ),
            (
                "managing-pediatric-growth-disorders",
                "Evaluates short stature and growth velocity with bone age interpretation and endocrine workup. Use when evaluating growth disorders, interpreting growth curves, or ordering growth workup.",
            ),
            (
                "managing-pediatric-behavioral-health",
                "Screens for and manages common pediatric behavioral and emotional conditions with school coordination. Use when screening pediatric mental health, coordinating with schools, or managing behavioral concerns.",
            ),
            (
                "managing-sports-physicals",
                "Structures pre-participation physical evaluations with cardiac screening and clearance decisions. Use when performing sports physicals, screening for cardiac conditions, or documenting athletic clearance.",
            ),
            (
                "managing-pediatric-dermatology",
                "Identifies and manages common pediatric skin conditions with visual diagnosis and treatment protocols. Use when evaluating pediatric rashes, managing eczema, or treating common skin conditions in children.",
            ),
        ],
    },
    # ─── 13. MEDICAL CODING & BILLING ────────────────────────────────
    "Medical Coding and Billing": {
        "description": "Clinical coding, charge capture, and revenue cycle workflows",
        "practice_areas": [
            "Medical Coding",
            "Revenue Cycle",
            "Health Information Management",
        ],
        "skills": [
            (
                "coding-medical-encounters",
                "Assigns ICD-10-CM diagnosis codes and CPT/HCPCS procedure codes with supporting documentation validation. Use when coding medical visits, selecting diagnosis codes, or assigning procedure codes.",
            ),
            (
                "auditing-coding-accuracy",
                "Reviews coded encounters for accuracy using OIG compliance guidelines and CMS documentation requirements. Use when auditing medical codes, reviewing coding accuracy, or conducting compliance audits.",
            ),
            (
                "managing-evaluation-management-coding",
                "Applies 2021+ E/M guidelines with medical decision-making or time-based code selection. Use when coding E/M services, determining MDM level, or selecting E/M codes.",
            ),
            (
                "coding-surgical-procedures",
                "Assigns CPT surgical codes with modifier selection and bundling/unbundling rules. Use when coding surgeries, applying surgical modifiers, or navigating NCCI edits.",
            ),
            (
                "managing-modifier-applications",
                "Guides appropriate modifier use (25, 59, 76, 77, etc.) with documentation requirements. Use when applying CPT modifiers, justifying modifier use, or resolving modifier-related denials.",
            ),
            (
                "abstracting-clinical-documentation",
                "Extracts codeable diagnoses and procedures from clinical notes with specificity capture. Use when abstracting medical records, identifying codeable conditions, or capturing documentation specificity.",
            ),
            (
                "managing-drg-optimization",
                "Optimizes MS-DRG assignment through accurate principal diagnosis selection and CC/MCC capture. Use when optimizing DRGs, capturing comorbidities, or improving case mix index.",
            ),
            (
                "coding-radiology-services",
                "Assigns radiology CPT codes with professional/technical component and supervision level documentation. Use when coding imaging studies, applying 26/TC modifiers, or coding interventional procedures.",
            ),
            (
                "managing-coding-denials",
                "Analyzes claim denials and structures appeal documentation with supporting clinical evidence. Use when appealing denied claims, analyzing denial patterns, or preparing appeal documentation.",
            ),
            (
                "managing-risk-adjustment-coding",
                "Captures HCC codes for risk adjustment with annual assessment and documentation requirements. Use when coding for risk adjustment, capturing HCC conditions, or managing RAF scores.",
            ),
            (
                "coding-emergency-services",
                "Assigns ED-specific E/M codes with critical care time documentation and procedure coding. Use when coding ED visits, documenting critical care, or coding ED procedures.",
            ),
            (
                "managing-cdi-programs",
                "Structures clinical documentation improvement queries with compliant physician engagement. Use when writing CDI queries, improving documentation specificity, or managing CDI programs.",
            ),
            (
                "coding-behavioral-health-services",
                "Assigns behavioral health procedure codes with time-based requirements and modifier application. Use when coding therapy sessions, applying psychiatric codes, or documenting behavioral health services.",
            ),
            (
                "managing-charge-capture",
                "Reviews charge capture completeness with missed charge identification and revenue recovery. Use when auditing charge capture, identifying missing charges, or improving revenue integrity.",
            ),
            (
                "coding-telehealth-services",
                "Assigns telehealth-specific codes with place of service, modifier, and technology requirements. Use when coding virtual visits, applying telehealth modifiers, or documenting telemedicine services.",
            ),
            (
                "managing-compliance-audits",
                "Structures coding compliance audit programs with sampling methodology and corrective action plans. Use when conducting compliance audits, designing audit samples, or implementing corrective actions.",
            ),
            (
                "coding-anesthesia-services",
                "Assigns anesthesia codes with time documentation, base/time unit calculation, and physical status modifiers. Use when coding anesthesia, calculating anesthesia units, or applying physical status modifiers.",
            ),
            (
                "managing-bundling-rules",
                "Navigates NCCI edits and CMS bundling policies with correct coding initiative compliance. Use when checking bundling rules, resolving NCCI edits, or managing component coding.",
            ),
            (
                "coding-laboratory-services",
                "Assigns laboratory CPT codes with panel construction and specimen-specific modifiers. Use when coding lab tests, building lab panels, or applying laboratory modifiers.",
            ),
            (
                "managing-payer-specific-coding",
                "Adapts coding practices for payer-specific requirements (Medicare, Medicaid, commercial) and LCD/NCD compliance. Use when navigating payer-specific rules, checking LCD/NCD coverage, or managing payer variations.",
            ),
        ],
    },
    # ─── 14. CLINICAL RESEARCH ───────────────────────────────────────
    "Clinical Research": {
        "description": "Research protocol design, regulatory compliance, and data management",
        "practice_areas": ["Clinical Research", "Biostatistics", "Regulatory Affairs"],
        "skills": [
            (
                "designing-clinical-trials",
                "Structures clinical trial protocol design with study type selection, endpoint definition, and power calculation. Use when designing trials, writing protocols, or calculating sample sizes.",
            ),
            (
                "writing-irb-submissions",
                "Creates IRB submission packages with protocol summaries, consent forms, and risk-benefit analysis. Use when submitting to IRB, preparing ethics applications, or writing consent documents.",
            ),
            (
                "managing-informed-consent-research",
                "Structures research consent documentation with required elements and vulnerable population protections. Use when creating research consents, managing consent processes, or documenting informed consent.",
            ),
            (
                "conducting-literature-reviews-systematic",
                "Performs systematic literature review following PRISMA guidelines with search strategy documentation. Use when conducting systematic reviews, documenting search strategies, or performing PRISMA analyses.",
            ),
            (
                "analyzing-clinical-trial-data",
                "Structures clinical trial data analysis with primary endpoint evaluation and safety reporting. Use when analyzing trial results, evaluating endpoints, or preparing statistical reports.",
            ),
            (
                "managing-adverse-event-reporting-research",
                "Documents research adverse events with causality assessment and regulatory reporting timelines. Use when reporting research AEs, assessing causality, or managing safety reporting.",
            ),
            (
                "writing-clinical-study-reports",
                "Creates ICH E3-compliant clinical study reports with required sections and data presentation. Use when writing CSRs, formatting study reports, or preparing regulatory submissions.",
            ),
            (
                "managing-data-safety-monitoring",
                "Structures DSMB operations with interim analysis protocols and stopping rules. Use when managing DSMBs, conducting interim analyses, or implementing stopping criteria.",
            ),
            (
                "conducting-meta-analyses",
                "Performs meta-analysis with heterogeneity assessment, forest plot generation, and GRADE evidence grading. Use when conducting meta-analyses, assessing heterogeneity, or grading evidence quality.",
            ),
            (
                "managing-regulatory-submissions",
                "Structures FDA/EMA regulatory submission packages with CTD format compliance. Use when preparing regulatory submissions, organizing CTD modules, or compiling FDA packages.",
            ),
            (
                "managing-good-clinical-practice",
                "Applies GCP/ICH principles to clinical research operations with compliance monitoring. Use when ensuring GCP compliance, training on ICH guidelines, or auditing research practices.",
            ),
            (
                "analyzing-pharmacovigilance-data",
                "Structures post-marketing safety surveillance with signal detection and PSUR reporting. Use when analyzing safety signals, preparing PSURs, or managing pharmacovigilance data.",
            ),
            (
                "managing-clinical-trial-budgets",
                "Structures trial budget development with per-patient costs, site fees, and sponsor negotiations. Use when budgeting clinical trials, negotiating site contracts, or tracking research expenditures.",
            ),
            (
                "designing-observational-studies",
                "Structures observational study designs (cohort, case-control, cross-sectional) with bias mitigation strategies. Use when designing observational research, mitigating bias, or planning epidemiologic studies.",
            ),
            (
                "managing-biospecimen-protocols",
                "Documents biospecimen collection, processing, storage, and tracking with chain-of-custody requirements. Use when managing biospecimens, designing collection protocols, or tracking samples.",
            ),
            (
                "interpreting-biostatistics",
                "Structures statistical analysis interpretation with p-value, confidence interval, and effect size reporting. Use when interpreting study statistics, explaining statistical results, or reviewing biostatistical analyses.",
            ),
            (
                "managing-clinical-data-quality",
                "Structures data quality management with query resolution, source data verification, and audit trails. Use when managing clinical data quality, resolving data queries, or conducting SDV.",
            ),
            (
                "writing-grant-applications-research",
                "Structures NIH/foundation grant applications with specific aims, significance, and innovation sections. Use when writing research grants, preparing NIH applications, or structuring grant proposals.",
            ),
            (
                "managing-research-compliance",
                "Monitors research compliance with federal regulations (21 CFR, 45 CFR 46) and institutional policies. Use when ensuring research compliance, managing regulatory requirements, or conducting compliance reviews.",
            ),
            (
                "conducting-health-economics-research",
                "Structures cost-effectiveness and health economic analyses with QALY calculations and model validation. Use when conducting health economics research, calculating QALYs, or building economic models.",
            ),
        ],
    },
    # ─── 15. NURSING ─────────────────────────────────────────────────
    "Nursing": {
        "description": "Nursing assessment, care planning, and clinical workflow management",
        "practice_areas": ["Nursing", "Advanced Practice", "Nurse Practitioner"],
        "skills": [
            (
                "conducting-nursing-assessments",
                "Structures head-to-toe nursing assessments with system-by-system documentation and abnormal findings. Use when performing nursing assessments, documenting patient evaluations, or creating assessment narratives.",
            ),
            (
                "creating-nursing-care-plans",
                "Develops NANDA-I nursing care plans with nursing diagnoses, outcomes (NOC), and interventions (NIC). Use when creating care plans, selecting nursing diagnoses, or planning nursing interventions.",
            ),
            (
                "documenting-nursing-notes",
                "Structures nursing progress notes with SBAR communication and clinical narrative documentation. Use when writing nursing notes, documenting patient updates, or creating SBAR communications.",
            ),
            (
                "managing-medication-administration",
                "Guides safe medication administration with rights verification, timing, and documentation requirements. Use when administering medications, documenting med administration, or managing medication timing.",
            ),
            (
                "managing-wound-assessment-nursing",
                "Structures wound assessment with measurement, staging, and treatment plan documentation. Use when assessing wounds, staging pressure injuries, or documenting wound care.",
            ),
            (
                "managing-patient-education",
                "Structures patient/family education with teach-back verification and health literacy assessment. Use when providing patient education, documenting teaching, or assessing learning comprehension.",
            ),
            (
                "managing-pain-assessment-nursing",
                "Applies pain assessment scales (NRS, Wong-Baker, FLACC, BPS) with intervention documentation and reassessment. Use when assessing pain, selecting pain scales, or documenting pain management.",
            ),
            (
                "managing-infection-control",
                "Implements infection prevention protocols with isolation precautions and surveillance documentation. Use when managing infection control, implementing isolation, or documenting infection prevention.",
            ),
            (
                "managing-iv-therapy",
                "Guides IV access assessment, site management, and complication monitoring with documentation. Use when managing IV therapy, assessing IV sites, or documenting infusion monitoring.",
            ),
            (
                "conducting-discharge-planning-nursing",
                "Coordinates nursing discharge planning with medication teaching, follow-up scheduling, and resource coordination. Use when planning discharge, coordinating post-discharge care, or documenting discharge teaching.",
            ),
            (
                "managing-restraint-documentation",
                "Documents restraint use with clinical justification, monitoring requirements, and regular reassessment. Use when documenting restraint use, monitoring restrained patients, or justifying restraint continuation.",
            ),
            (
                "managing-rapid-response-nursing",
                "Structures rapid response team activation criteria and nursing documentation during rapid response events. Use when activating rapid response, documenting RRT events, or recognizing deterioration.",
            ),
            (
                "managing-blood-product-administration",
                "Guides blood product administration with verification, monitoring, and transfusion reaction management. Use when administering blood products, monitoring transfusions, or managing transfusion reactions.",
            ),
            (
                "managing-central-line-care",
                "Structures central line maintenance with bundle compliance and infection prevention documentation. Use when managing central lines, documenting line care, or tracking bundle compliance.",
            ),
            (
                "managing-skin-integrity",
                "Conducts Braden scale assessment with pressure injury prevention interventions and documentation. Use when assessing skin integrity, calculating Braden scores, or implementing pressure injury prevention.",
            ),
            (
                "managing-patient-safety-events",
                "Documents patient safety events with root cause identification and incident reporting requirements. Use when reporting safety events, documenting incidents, or analyzing near-misses.",
            ),
            (
                "managing-nurse-staffing-acuity",
                "Applies patient acuity classification with staffing ratio calculations and resource allocation. Use when assessing patient acuity, calculating staffing needs, or managing nurse assignments.",
            ),
            (
                "managing-perioperative-nursing",
                "Structures perioperative nursing documentation with pre/intra/post-operative assessments and counts. Use when documenting OR nursing care, performing surgical counts, or managing perioperative documentation.",
            ),
            (
                "managing-telemetry-monitoring",
                "Interprets telemetry rhythm strips with documentation requirements and escalation criteria. Use when monitoring telemetry, documenting rhythm interpretations, or recognizing alarm conditions.",
            ),
            (
                "managing-nursing-quality-metrics",
                "Tracks nursing quality indicators (NDNQI, HCAHPS) with performance improvement documentation. Use when monitoring nursing quality, tracking NDNQI metrics, or managing quality improvement.",
            ),
        ],
    },
    # ─── 16. HEALTHCARE COMPLIANCE & REGULATION ──────────────────────
    "Healthcare Compliance": {
        "description": "Regulatory compliance, privacy, and healthcare law workflows",
        "practice_areas": ["Healthcare Compliance", "HIPAA", "Healthcare Regulation"],
        "skills": [
            (
                "auditing-hipaa-compliance",
                "Conducts HIPAA compliance assessments with Privacy Rule, Security Rule, and Breach Notification analysis. Use when auditing HIPAA compliance, assessing privacy practices, or reviewing security controls.",
            ),
            (
                "managing-privacy-breach-response",
                "Guides HIPAA breach investigation with risk assessment, notification requirements, and remediation documentation. Use when managing data breaches, assessing breach risk, or documenting breach response.",
            ),
            (
                "conducting-stark-law-analysis",
                "Evaluates physician self-referral arrangements against Stark Law exceptions with documentation. Use when analyzing Stark compliance, evaluating referral arrangements, or documenting exception applicability.",
            ),
            (
                "conducting-anti-kickback-analysis",
                "Evaluates payment arrangements against Anti-Kickback Statute safe harbors with documentation. Use when analyzing AKS compliance, evaluating compensation arrangements, or documenting safe harbor applicability.",
            ),
            (
                "managing-compliance-programs",
                "Structures OIG-model compliance program elements with effectiveness measurement and reporting. Use when building compliance programs, implementing OIG guidance, or measuring program effectiveness.",
            ),
            (
                "managing-emtala-compliance",
                "Evaluates emergency department practices against EMTALA requirements with documentation checklists. Use when assessing EMTALA compliance, reviewing MSE requirements, or documenting transfer obligations.",
            ),
            (
                "conducting-false-claims-analysis",
                "Evaluates billing practices for False Claims Act risk with qui tam and voluntary disclosure considerations. Use when assessing FCA risk, evaluating billing compliance, or considering self-disclosure.",
            ),
            (
                "managing-conditions-of-participation",
                "Monitors CMS Conditions of Participation compliance with survey readiness documentation. Use when preparing for CMS surveys, tracking CoP compliance, or managing survey readiness.",
            ),
            (
                "managing-informed-consent-compliance",
                "Evaluates informed consent practices against state law requirements and institutional policies. Use when auditing consent processes, reviewing consent form adequacy, or managing consent compliance.",
            ),
            (
                "managing-medical-staff-credentialing",
                "Structures credentialing verification with primary source documentation and privilege delineation. Use when processing credentials, verifying qualifications, or managing privilege requests.",
            ),
            (
                "managing-risk-management-healthcare",
                "Structures healthcare risk management with incident investigation, claims analysis, and loss prevention strategies. Use when managing healthcare risk, investigating incidents, or developing loss prevention programs.",
            ),
            (
                "managing-quality-reporting",
                "Structures CMS quality reporting (MIPS, HEDIS, CQMs) with measure specification and data validation. Use when reporting quality measures, managing MIPS submissions, or validating quality data.",
            ),
            (
                "managing-accreditation-compliance",
                "Tracks Joint Commission/HFAP/DNV accreditation standards compliance with survey preparation. Use when preparing for accreditation, tracking standards compliance, or managing survey readiness.",
            ),
            (
                "managing-clinical-trial-compliance",
                "Evaluates clinical trial regulatory compliance with FDA/IRB requirements and audit readiness. Use when auditing trial compliance, preparing for FDA inspections, or managing regulatory requirements.",
            ),
            (
                "managing-telehealth-compliance",
                "Evaluates telehealth program compliance with state licensing, prescribing, and reimbursement requirements. Use when assessing telehealth compliance, reviewing licensure requirements, or managing virtual care regulations.",
            ),
            (
                "managing-substance-abuse-confidentiality",
                "Applies 42 CFR Part 2 substance abuse confidentiality requirements with consent and disclosure protocols. Use when managing SUD records, applying Part 2 requirements, or handling substance abuse confidentiality.",
            ),
            (
                "managing-medical-records-compliance",
                "Evaluates medical records practices against retention, access, and amendment requirements. Use when auditing medical records, managing record retention, or processing amendment requests.",
            ),
            (
                "managing-billing-compliance",
                "Structures billing compliance programs with audit methodology and corrective action protocols. Use when auditing billing practices, managing compliance programs, or implementing corrective actions.",
            ),
            (
                "managing-workplace-safety-healthcare",
                "Tracks OSHA healthcare requirements including bloodborne pathogen, TB, and violence prevention programs. Use when managing OSHA compliance, implementing safety programs, or documenting exposure incidents.",
            ),
            (
                "managing-state-regulatory-compliance",
                "Monitors state-specific healthcare regulatory requirements including licensing, reporting, and scope of practice. Use when tracking state regulations, managing licensure requirements, or monitoring regulatory changes.",
            ),
        ],
    },
    # ─── 17. HEALTH INFORMATICS / HIT ────────────────────────────────
    "Health Informatics": {
        "description": "Health IT, data interoperability, and clinical decision support workflows",
        "practice_areas": ["Health Informatics", "Health IT", "Clinical Informatics"],
        "skills": [
            (
                "mapping-clinical-terminologies",
                "Maps between clinical terminologies (ICD-10, SNOMED CT, LOINC, RxNorm) with semantic equivalence validation. Use when mapping medical codes, converting between terminologies, or validating code mappings.",
            ),
            (
                "managing-ehr-implementations",
                "Structures EHR implementation planning with workflow analysis, data migration, and go-live readiness. Use when planning EHR deployments, managing system migrations, or preparing for go-live events.",
            ),
            (
                "designing-clinical-decision-support",
                "Creates CDS rule specifications with trigger conditions, evidence base, and alert fatigue mitigation. Use when designing CDS alerts, specifying clinical rules, or optimizing alert systems.",
            ),
            (
                "managing-health-data-exchange",
                "Structures health information exchange with HL7 FHIR, C-CDA, and interoperability requirements. Use when managing data exchange, implementing FHIR APIs, or ensuring interoperability.",
            ),
            (
                "analyzing-clinical-data-warehouses",
                "Structures clinical data warehouse queries for quality measurement, research, and operational analytics. Use when querying clinical data, building analytics reports, or extracting research datasets.",
            ),
            (
                "managing-patient-portal-content",
                "Creates patient-facing health information content with health literacy and accessibility standards. Use when developing portal content, writing patient communications, or managing digital health tools.",
            ),
            (
                "validating-clinical-data-quality",
                "Structures data quality assessment with completeness, accuracy, and consistency validation. Use when auditing clinical data, assessing data quality, or validating data integrity.",
            ),
            (
                "managing-clinical-natural-language-processing",
                "Structures clinical NLP pipeline design with entity extraction and assertion detection specifications. Use when designing clinical NLP, extracting entities from notes, or building text analysis pipelines.",
            ),
            (
                "managing-population-health-analytics",
                "Structures population health analysis with risk stratification and care gap identification. Use when analyzing population health, stratifying patient risk, or identifying care gaps.",
            ),
            (
                "managing-clinical-registries",
                "Structures clinical registry data collection with quality measure calculation and reporting. Use when managing clinical registries, submitting registry data, or calculating quality measures.",
            ),
            (
                "managing-health-data-governance",
                "Structures health data governance programs with stewardship roles, policies, and data quality standards. Use when establishing data governance, defining data stewardship, or managing data policies.",
            ),
            (
                "managing-predictive-analytics-clinical",
                "Evaluates and deploys clinical predictive models with validation, bias assessment, and monitoring. Use when evaluating prediction models, assessing algorithmic bias, or deploying clinical ML.",
            ),
            (
                "managing-ehr-optimization",
                "Identifies EHR optimization opportunities through usage analysis and workflow improvement. Use when optimizing EHR workflows, reducing click burden, or improving EHR usability.",
            ),
            (
                "managing-interoperability-standards",
                "Tracks and implements healthcare interoperability standards (ONC, TEFCA, Information Blocking). Use when ensuring interoperability compliance, implementing TEFCA, or managing information blocking rules.",
            ),
            (
                "managing-clinical-imaging-informatics",
                "Structures radiology informatics workflows with PACS integration and DICOM standards. Use when managing imaging informatics, integrating PACS systems, or implementing DICOM workflows.",
            ),
            (
                "managing-telemedicine-technology",
                "Evaluates and implements telemedicine technology platforms with clinical workflow integration. Use when selecting telehealth platforms, integrating virtual care technology, or managing telemedicine infrastructure.",
            ),
            (
                "managing-clinical-documentation-improvement",
                "Designs CDI programs with NLP-assisted query generation and documentation quality metrics. Use when implementing CDI programs, designing documentation queries, or measuring documentation quality.",
            ),
            (
                "managing-health-ai-governance",
                "Structures AI/ML governance for healthcare applications with validation, monitoring, and ethical frameworks. Use when governing health AI, validating clinical models, or managing AI ethics in healthcare.",
            ),
            (
                "managing-cybersecurity-healthcare",
                "Structures healthcare cybersecurity programs with PHI protection, incident response, and risk assessment. Use when managing healthcare cybersecurity, protecting health data, or conducting security risk assessments.",
            ),
            (
                "managing-digital-health-evaluations",
                "Evaluates digital health tools and apps with clinical evidence assessment and integration planning. Use when evaluating health apps, assessing digital therapeutics, or planning digital health integration.",
            ),
        ],
    },
    # ─── 18. PUBLIC HEALTH / EPIDEMIOLOGY ────────────────────────────
    "Public Health": {
        "description": "Population health, epidemiology, and public health response workflows",
        "practice_areas": ["Public Health", "Epidemiology", "Preventive Medicine"],
        "skills": [
            (
                "conducting-disease-surveillance",
                "Structures disease surveillance systems with case definitions, reporting requirements, and trend analysis. Use when monitoring disease trends, managing surveillance data, or analyzing reportable conditions.",
            ),
            (
                "investigating-disease-outbreaks",
                "Guides outbreak investigation using CDC steps with case definition, epidemiologic curve, and control measures. Use when investigating outbreaks, analyzing epidemic curves, or implementing control measures.",
            ),
            (
                "analyzing-epidemiological-data",
                "Structures epidemiologic analysis with incidence, prevalence, rate calculations, and statistical inference. Use when calculating disease rates, analyzing epi data, or interpreting population statistics.",
            ),
            (
                "managing-contact-tracing",
                "Structures contact tracing operations with case investigation, contact identification, and monitoring protocols. Use when conducting contact tracing, managing case investigations, or monitoring exposed contacts.",
            ),
            (
                "assessing-community-health-needs",
                "Conducts community health needs assessment with data collection, analysis, and priority identification. Use when assessing community health, prioritizing health needs, or planning health interventions.",
            ),
            (
                "managing-vaccination-campaigns",
                "Plans mass vaccination campaigns with logistics, cold chain management, and adverse event monitoring. Use when planning vaccination drives, managing immunization logistics, or monitoring VAERS.",
            ),
            (
                "conducting-health-impact-assessments",
                "Structures health impact assessment with exposure evaluation and risk characterization. Use when assessing health impacts, evaluating environmental exposures, or characterizing population risk.",
            ),
            (
                "managing-pandemic-response",
                "Structures pandemic response planning with surge capacity, resource allocation, and communication protocols. Use when planning pandemic response, managing surge operations, or coordinating emergency health responses.",
            ),
            (
                "analyzing-social-determinants-of-health",
                "Maps social determinants affecting health outcomes with intervention strategy development. Use when analyzing SDOH, mapping community resources, or designing social health interventions.",
            ),
            (
                "managing-environmental-health-assessments",
                "Structures environmental health evaluations with exposure assessment and risk communication. Use when assessing environmental health risks, evaluating contamination, or communicating environmental findings.",
            ),
            (
                "designing-health-education-programs",
                "Structures health education program design with behavior change theory and outcome evaluation. Use when designing health education, planning health promotion, or evaluating educational programs.",
            ),
            (
                "managing-maternal-child-health-programs",
                "Structures MCH program management with Title V indicators and outcome tracking. Use when managing MCH programs, tracking perinatal outcomes, or monitoring child health indicators.",
            ),
            (
                "conducting-health-equity-analyses",
                "Analyzes health disparities with demographic stratification and equity-focused intervention planning. Use when analyzing health disparities, assessing equity, or designing health equity interventions.",
            ),
            (
                "managing-emergency-preparedness",
                "Structures public health emergency preparedness with hazard vulnerability and response planning. Use when planning emergency preparedness, conducting vulnerability assessments, or developing response plans.",
            ),
            (
                "managing-chronic-disease-programs",
                "Structures chronic disease prevention programs with evidence-based intervention selection and outcome tracking. Use when managing chronic disease programs, selecting prevention interventions, or tracking population outcomes.",
            ),
            (
                "analyzing-vital-statistics",
                "Structures vital records analysis with birth, death, and demographic trend reporting. Use when analyzing vital statistics, interpreting mortality data, or reporting demographic trends.",
            ),
            (
                "managing-infectious-disease-programs",
                "Structures infectious disease control programs with prevention, testing, and treatment access protocols. Use when managing ID programs, implementing STI prevention, or coordinating TB control.",
            ),
            (
                "conducting-program-evaluation-public-health",
                "Structures program evaluation using CDC framework with process, outcome, and impact assessment. Use when evaluating public health programs, measuring program effectiveness, or conducting logic model analysis.",
            ),
            (
                "managing-global-health-programs",
                "Structures international health program design with WHO guidelines and cross-cultural considerations. Use when managing global health initiatives, applying WHO frameworks, or designing international health programs.",
            ),
            (
                "managing-occupational-health-surveillance",
                "Structures workplace health surveillance with exposure monitoring, screening programs, and OSHA reporting. Use when managing occupational health, monitoring workplace exposures, or tracking occupational injuries.",
            ),
        ],
    },
    # ─── 19. DENTAL / ORAL HEALTH ────────────────────────────────────
    "Dental Medicine": {
        "description": "Oral health assessment, treatment planning, and dental practice workflows",
        "practice_areas": ["General Dentistry", "Oral Surgery", "Periodontics"],
        "skills": [
            (
                "conducting-dental-examinations",
                "Structures comprehensive dental examinations with periodontal charting, caries assessment, and oral cancer screening. Use when performing dental exams, documenting oral findings, or creating dental records.",
            ),
            (
                "creating-dental-treatment-plans",
                "Structures dental treatment planning with phasing, cost estimation, and alternative options presentation. Use when creating treatment plans, phasing dental work, or presenting treatment options.",
            ),
            (
                "documenting-dental-procedures",
                "Creates structured dental procedure notes with tooth-specific documentation and material specifications. Use when documenting dental procedures, recording treatment details, or creating dental records.",
            ),
            (
                "managing-dental-radiograph-interpretation",
                "Structures dental radiograph interpretation with caries detection, bone level assessment, and pathology identification. Use when reading dental X-rays, identifying radiographic pathology, or documenting dental imaging findings.",
            ),
            (
                "managing-periodontal-assessments",
                "Structures periodontal evaluation with probing depths, attachment levels, and disease classification. Use when conducting periodontal assessments, classifying gum disease, or documenting periodontal status.",
            ),
            (
                "managing-endodontic-cases",
                "Guides root canal evaluation and treatment documentation with pulp/periapical diagnosis and outcome assessment. Use when evaluating endodontic cases, documenting root canal treatments, or assessing treatment outcomes.",
            ),
            (
                "managing-oral-surgery-cases",
                "Structures oral surgery documentation with extraction complexity assessment and complication management. Use when documenting extractions, assessing surgical complexity, or managing oral surgery complications.",
            ),
            (
                "managing-dental-emergencies",
                "Guides emergency dental assessment with triage protocols and immediate management documentation. Use when managing dental emergencies, triaging urgent dental conditions, or documenting emergency dental care.",
            ),
            (
                "managing-orthodontic-assessments",
                "Structures orthodontic evaluation with classification, treatment options, and progress documentation. Use when evaluating orthodontic needs, classifying malocclusion, or documenting treatment progress.",
            ),
            (
                "managing-dental-implant-planning",
                "Structures implant evaluation with bone assessment, treatment planning, and surgical documentation. Use when planning dental implants, assessing bone adequacy, or documenting implant procedures.",
            ),
            (
                "managing-pediatric-dental-care",
                "Adapts dental evaluation and treatment for pediatric patients with behavior management documentation. Use when treating pediatric dental patients, managing child behavior, or documenting pediatric dental care.",
            ),
            (
                "managing-prosthodontic-cases",
                "Structures prosthodontic evaluation with crown, bridge, and denture planning documentation. Use when planning prosthetic restorations, documenting impression techniques, or managing prosthetic treatment.",
            ),
            (
                "managing-dental-insurance-coding",
                "Assigns CDT codes with procedure-specific documentation and insurance submission requirements. Use when coding dental procedures, submitting dental claims, or managing CDT code selection.",
            ),
            (
                "managing-dental-infection-control",
                "Implements OSHA and CDC dental infection control guidelines with sterilization monitoring documentation. Use when managing dental infection control, documenting sterilization, or maintaining infection prevention compliance.",
            ),
            (
                "managing-tmj-disorders",
                "Structures TMD evaluation with clinical and imaging assessment, classification, and treatment protocols. Use when evaluating TMJ disorders, classifying TMD, or documenting TMJ treatment.",
            ),
            (
                "managing-dental-pharmacology",
                "Guides dental prescribing with local anesthetic selection, antibiotic prophylaxis, and pain management. Use when prescribing dental medications, selecting local anesthetics, or managing dental pain.",
            ),
            (
                "managing-dental-sedation",
                "Documents conscious sedation with patient selection, monitoring parameters, and recovery assessment. Use when providing dental sedation, documenting sedation monitoring, or managing sedation recovery.",
            ),
            (
                "managing-dental-laboratory-coordination",
                "Structures dental lab communications with prescription specifications and quality assessment. Use when coordinating with dental labs, writing lab prescriptions, or evaluating lab work quality.",
            ),
            (
                "managing-dental-quality-assurance",
                "Structures dental practice quality assessment with peer review and outcomes tracking. Use when conducting dental QA, performing peer review, or tracking treatment outcomes.",
            ),
            (
                "managing-dental-medical-integration",
                "Evaluates medical-dental interactions with systemic disease impact on dental treatment planning. Use when managing medically complex dental patients, adjusting treatment for systemic disease, or coordinating medical-dental care.",
            ),
        ],
    },
    # ─── 20. REHABILITATION / PHYSICAL THERAPY ───────────────────────
    "Rehabilitation Medicine": {
        "description": "Physical, occupational, and speech therapy assessment and treatment workflows",
        "practice_areas": [
            "Physical Therapy",
            "Occupational Therapy",
            "Rehabilitation Medicine",
        ],
        "skills": [
            (
                "conducting-functional-assessments",
                "Structures functional capacity evaluation with standardized measures and activity limitation documentation. Use when assessing functional status, measuring mobility, or documenting activity levels.",
            ),
            (
                "creating-rehabilitation-treatment-plans",
                "Develops rehabilitation treatment plans with goals, interventions, and measurable outcome milestones. Use when creating rehab plans, setting therapy goals, or planning intervention progressions.",
            ),
            (
                "managing-range-of-motion-assessments",
                "Documents goniometric measurements with active/passive ROM and comparison to normative values. Use when measuring joint ROM, documenting mobility assessments, or tracking ROM progress.",
            ),
            (
                "managing-strength-testing",
                "Structures manual muscle testing and dynamometry with grading and functional correlation. Use when testing muscle strength, grading MMT, or documenting strength assessment.",
            ),
            (
                "managing-gait-analysis",
                "Structures observational and instrumented gait analysis with deviation identification and intervention planning. Use when analyzing gait patterns, documenting gait deviations, or planning gait interventions.",
            ),
            (
                "managing-neurological-rehabilitation",
                "Structures neurorehab assessment with standardized scales (FIM, Barthel, NIHSS) and recovery tracking. Use when managing neurological rehab, documenting recovery progress, or applying neurorehab scales.",
            ),
            (
                "managing-cardiac-rehabilitation-therapy",
                "Structures cardiac rehab exercise prescription with monitoring parameters and progression criteria. Use when prescribing cardiac rehab exercise, monitoring exercise response, or documenting rehab progression.",
            ),
            (
                "managing-pulmonary-rehabilitation",
                "Structures pulmonary rehab with exercise prescription, dyspnea management, and outcome measurement. Use when managing pulmonary rehab, prescribing breathing exercises, or tracking respiratory outcomes.",
            ),
            (
                "managing-orthopedic-rehabilitation",
                "Structures post-surgical and injury rehab protocols with phase-based progression and return-to-activity criteria. Use when managing orthopedic rehab, following surgical protocols, or determining return-to-sport readiness.",
            ),
            (
                "managing-pain-rehabilitation",
                "Structures chronic pain rehabilitation with functional restoration and multidisciplinary coordination. Use when managing pain rehab, implementing functional restoration, or coordinating pain programs.",
            ),
            (
                "managing-pediatric-rehabilitation",
                "Adapts rehabilitation assessment and intervention for pediatric developmental needs with family-centered approaches. Use when providing pediatric rehab, addressing developmental delays, or managing childhood rehabilitation.",
            ),
            (
                "managing-occupational-therapy-assessments",
                "Structures OT evaluation with ADL assessment, adaptive equipment needs, and work readiness evaluation. Use when conducting OT assessments, evaluating ADL independence, or recommending adaptive equipment.",
            ),
            (
                "managing-speech-therapy-assessments",
                "Structures speech-language evaluation with articulation, language, swallowing, and cognitive-communication assessment. Use when conducting speech evaluations, assessing swallowing function, or documenting communication disorders.",
            ),
            (
                "managing-vestibular-rehabilitation",
                "Structures vestibular assessment with positional testing and customized exercise programs. Use when evaluating vestibular disorders, performing Dix-Hallpike testing, or designing vestibular exercise programs.",
            ),
            (
                "managing-prosthetic-rehabilitation",
                "Structures prosthetic evaluation with device selection, fitting documentation, and functional training. Use when managing prosthetic rehab, documenting device fitting, or tracking prosthetic training progress.",
            ),
            (
                "managing-spinal-cord-injury-rehabilitation",
                "Structures SCI rehab with ASIA classification, functional expectations, and complication prevention. Use when managing SCI rehab, documenting ASIA scores, or planning SCI recovery goals.",
            ),
            (
                "managing-traumatic-brain-injury-rehabilitation",
                "Structures TBI rehab with Rancho Los Amigos scoring and cognitive rehabilitation protocols. Use when managing TBI rehab, tracking Rancho levels, or implementing cognitive therapy.",
            ),
            (
                "managing-home-health-rehabilitation",
                "Structures home health therapy documentation with homebound status justification and discharge criteria. Use when documenting home health therapy, justifying homebound status, or planning home-based rehab.",
            ),
            (
                "managing-workers-compensation-rehabilitation",
                "Structures workers comp rehab documentation with functional capacity evaluation and return-to-work planning. Use when managing work injury rehab, performing FCEs, or documenting return-to-work status.",
            ),
            (
                "managing-rehabilitation-outcome-measurement",
                "Tracks rehabilitation outcomes using standardized tools with program effectiveness reporting. Use when measuring rehab outcomes, benchmarking program results, or reporting rehabilitation quality.",
            ),
        ],
    },
}

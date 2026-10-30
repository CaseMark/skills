# Breach Determination Rules

Rules for deciding whether an incident is a notifiable breach, and under which regime. Each rule names its authority; `references/primary-sources.md` records where and when it was checked (October 30, 2026). Deadlines, thresholds and state rules are in `references/notification-clocks.md`.

## Contents

1. Regime map
2. Discovery and imputed knowledge
3. Order of the threshold questions
4. The secured-PHI safe harbor (encryption and destruction)
5. The three exceptions
6. The four-factor risk assessment
7. Ransomware and other malware
8. 42 C.F.R. Part 2 records
9. FTC Health Breach Notification Rule (non-HIPAA health apps)
10. Outcome vocabulary

## 1. Regime map

Run every regime that applies; each gets its own row in the determination summary.

| Who holds the data | Regime | Notifies whom | Authority |
|---|---|---|---|
| HIPAA covered entity (provider that conducts standard transactions, health plan, clearinghouse) | HIPAA Breach Notification Rule | Individuals, HHS, media (more than 500 residents of a State or jurisdiction) | 45 C.F.R. 164.400-414 |
| Business associate or subcontractor business associate | Same rule, notice runs up the chain | The covered entity (or the upstream business associate); the BAA may add shorter terms | 45 C.F.R. 164.410; the BAA |
| Part 2 program (federally assisted SUD program), whether or not it is a covered entity | Part 2 breach provision, applying HIPAA subpart D "in the same manner" | Patients, HHS (Part 2 portal), media | 42 C.F.R. 2.16(b), 2.11 |
| Qualified service organization (QSO) of a Part 2 program | No regulatory notice duty; the QSO agreement governs | The Part 2 program, by contract | 89 FR 12472 preamble (QSO discussion) |
| Vendor of personal health records, PHR related entity, third party service provider (not a covered entity and not acting as a business associate) | FTC Health Breach Notification Rule | Individuals, FTC, media (500 or more residents); service providers notify the vendor | 16 C.F.R. Part 318 |
| Any entity holding residents' personal information | State breach statutes, each with its own definitions and clocks | Residents, often the attorney general, sometimes other agencies | State law; see the clocks file |
| California licensed clinics, health facilities, home health agencies, hospices | Facility reporting statute | CDPH and the patient | Cal. Health & Safety Code 1280.15 |

The FTC rule does not apply to a covered entity or to an entity "to the extent that it engages in activities as a business associate" (16 C.F.R. 318.1(a)). A company can be a business associate for one product line and a PHR vendor for another; decide per data flow.

## 2. Discovery and imputed knowledge

- A breach is treated as discovered on the first day it is known to the covered entity, or by exercising reasonable diligence would have been known to it. Knowledge of any workforce member or agent, other than the person committing the breach, is the entity's knowledge (45 C.F.R. 164.404(a)(2); federal common law of agency).
- The clock starts when the incident is first known, "not when the investigation of the incident is complete, even if it is initially unclear whether the incident constitutes a breach" (74 FR 42740, 42750; restated in the 2013 Omnibus preamble). Letting the investigation lag can itself be unreasonable delay; 60 days is an outer limit.
- The date the privacy officer, compliance, counsel or leadership learned of the incident is not discovery unless no one earlier knew or should have known. A front-desk employee, a nurse manager or an IT analyst who saw the event starts the clock.
- Business associates: discovery is the first day known to the business associate or any employee, officer or agent of it (164.410(a)(2)). If the business associate is the covered entity's agent, its discovery is imputed to the covered entity, which must notify from the date the business associate discovered the breach; if it is not an agent, the covered entity's clock runs from the business associate's notice (78 FR 5566, 5656). Agency is fact-specific: the BAA's terms count, but the essential factor is the covered entity's right to control the business associate's conduct, such as the right to give interim instructions (78 FR 5566, 5582). A BAA clause calling the vendor an "independent contractor" does not settle it; when facts are mixed, compute both clocks.
- A lost or stolen device does not justify waiting for recovery (78 FR 5566, 5647).
- Discovery is a finding of fact from the record. Never move it to the date an investigation closed, a memo was signed or a committee met.

## 3. Order of the threshold questions

1. Is the information PHI (or Part 2 records, PHR identifiable health information, or a state-law data element)?
2. Was there an acquisition, access, use or disclosure not permitted under the Privacy Rule (45 C.F.R. part 164 subpart E), or under Part 2 for Part 2 records?
3. Was the information unsecured? If secured under the HHS guidance, no notification duty arises under HIPAA (Section 4).
4. Does one of the three exceptions apply (Section 5)? The entity must document why.
5. Otherwise the event is presumed a breach unless the four-factor assessment demonstrates a low probability of compromise (Section 6). The entity carries the burden of proof (164.414(b)) and must keep documentation sufficient to meet it (164.530(j)(1)(iv)).

An entity may notify without performing a risk assessment (HHS Breach Notification Rule page).

## 4. The secured-PHI safe harbor (encryption and destruction)

HHS guidance (hhs.gov breach notification guidance, content last reviewed July 26, 2013):

- Electronic PHI is secured if encrypted as defined in 45 C.F.R. 164.304 and "such confidential process or key that might enable decryption has not been breached". Decryption tools should be stored separately from the data. Data at rest: consistent with NIST SP 800-111. Data in motion: NIST SP 800-52, 800-77 or 800-113, or others that are FIPS 140-2 validated.
- Destruction: paper shredded or destroyed so it cannot be read or reconstructed (redaction does not count); electronic media cleared, purged or destroyed consistent with NIST SP 800-88.
- The safe harbor fails when: the key, password, PIN or recovery key was with the device or is otherwise compromised; the device was powered on and unlocked (full-disk encryption decrypts transparently for the logged-in user, per the HHS ransomware fact sheet, July 11, 2016); only some copies were encrypted (email, backups, sync folders, removable media); or the product or configuration is not shown to meet the guidance. An IT statement that a device "was encrypted" is a claim to verify, not proof; with no proof, treat the PHI as unsecured.
- State statutes define "encrypted" and key compromise in their own words (for example Cal. Civ. Code 1798.82(a)(1) reaches encrypted data when the key or security credential was acquired). Test each state separately.

## 5. The three exceptions (45 C.F.R. 164.402, paragraph (1) of "breach")

| Exception | Every condition must hold | Common misuse |
|---|---|---|
| (i) Unintentional acquisition, access or use by a workforce member or person acting under the entity's authority | Good faith; within the scope of authority; no further use or disclosure not permitted by the Privacy Rule | Applied to snooping (a receptionist browsing a friend's chart is not excepted; 74 FR 42740, 42748) or to a recipient who forwarded or kept the data |
| (ii) Inadvertent disclosure between persons each authorized to access PHI at the same covered entity, business associate or organized health care arrangement | Sender authorized to access PHI; recipient authorized to access PHI at the same entity or OHCA (not necessarily the same PHI); no further impermissible use or disclosure | Applied because both people are "workforce", when the recipient's role has no PHI access, or applied across separate legal entities |
| (iii) Good faith belief that the unauthorized recipient could not reasonably have retained the information | A documented basis (for example papers handed to the wrong patient and taken back at once) | Applied to a mailed letter, an email, or a fax that reached an outside party and was not returned unread |

Misdirected PHI inside the workforce is not automatically excepted. Test each condition against the recipient's actual access rights and conduct, and document the basis (78 FR 5566, 5641).

## 6. The four-factor risk assessment

Address every factor with evidence, then weigh them together (164.402(2); 78 FR 5566, 5644: the analysis "must address each factor"; assessments must be "thorough, completed in good faith", with reasonable conclusions).

| Factor | Evidence to cite | Weak reasoning to reject |
|---|---|---|
| 1. Nature and extent of the PHI, including identifiers and likelihood of re-identification | Data elements, sensitivity (SUD, HIV, mental health, reproductive, genetic, SSN, financial), volume | Calling clinical data low risk because no SSN was involved |
| 2. The unauthorized person who used or received it | Identity, whether bound by HIPAA or a confidentiality duty, motive | Treating an unknown thief or threat actor as neutral |
| 3. Whether the PHI was actually acquired or viewed | Forensics, access logs, device return analysis, mail logs | "No evidence of misuse" or "no evidence of exfiltration" where logs are missing or incomplete |
| 4. Extent to which the risk has been mitigated | Return or destruction, signed attestation, recipient's reliability | Relying on factor 4 alone; an attestation from an unknown or untrusted recipient |

If the assessment does not demonstrate a low probability of compromise, notification is required. A conclusion that is chosen first and supported afterward is not a risk assessment; this skill does not write one.

## 7. Ransomware and other malware

HHS fact sheet (July 11, 2016): when ePHI is encrypted by ransomware, a breach has occurred because the ePHI was acquired (taken into the attacker's possession or control); a breach is presumed unless the entity demonstrates a low probability of compromise under the four factors. Forensics should establish the malware variant, its behavior, exfiltration attempts and propagation. Absence of exfiltration evidence is relevant to factor 3 but does not by itself demonstrate a low probability, especially with log gaps.

## 8. 42 C.F.R. Part 2 records

- Since the compliance date of the 2024 final rule (February 16, 2026; 89 FR 12472, Feb. 16, 2024, effective April 16, 2024), 45 C.F.R. part 160 and subpart D of part 164 apply to Part 2 programs for breaches of unsecured records "in the same manner" as to covered entities (42 C.F.R. 2.16(b)). "Breach" has the HIPAA meaning; "unsecured record" uses the same HHS guidance (42 C.F.R. 2.11).
- A Part 2 program that is not a HIPAA covered entity still must notify. OCR began accepting Part 2 breach reports on February 16, 2026 through the HHS portal (HHS press release, Feb. 13, 2026; HHS breach reporting page, last reviewed Feb. 13, 2026).
- QSOs have no regulatory notice duty; the preamble expects programs to impose one in the QSO agreement.
- When a covered entity also runs a Part 2 program, identify the Part 2 records separately: whether a use or disclosure was permitted is tested against Part 2 as well as the Privacy Rule `[VERIFY]` (see the primary-sources list).

## 9. FTC Health Breach Notification Rule (non-HIPAA health apps)

- Applies to vendors of personal health records, PHR related entities and third party service providers that are not covered entities and not acting as business associates (16 C.F.R. 318.1, 318.2; amended 89 FR 47028, May 30, 2024, effective July 29, 2024).
- "Breach of security" is acquisition of unsecured PHR identifiable health information without the individual's authorization and includes an unauthorized disclosure (for example sharing with an advertising platform without authorization). Unauthorized access is presumed to be acquisition unless the entity has reliable evidence that there was not, or could not reasonably have been, unauthorized acquisition. There is no four-factor low-probability test.
- Discovery: first day known or reasonably should have been known to any employee, officer or other agent other than the person committing the breach (318.3(c)).
- Notice content adds the identity of third parties that acquired the data, where known, and requires two or more contact methods (318.6).

## 10. Outcome vocabulary

Use these labels verbatim, one per regime row:

- Not an impermissible use or disclosure
- Not a breach: PHI secured (encryption or destruction safe harbor)
- Not a breach: exception (i) applies / exception (ii) applies / exception (iii) applies
- Not a breach: low probability of compromise demonstrated
- Presumed breach: notification required
- Cannot determine

Add "provisional pending <facts>" when an unchecked fact could change the result, and name who can supply it.

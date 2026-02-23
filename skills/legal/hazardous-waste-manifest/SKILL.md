---
name: hazardous-waste-manifest
description: Drafts a Uniform Hazardous Waste Manifest (EPA Form 8700-22) compliant with RCRA, EPA, and DOT requirements. Assembles generator, transporter, and TSDF information to create a complete chain-of-custody tracking document for hazardous waste shipments from generation through final disposal. Enforces 40 CFR Parts 261–265 waste coding, DOT shipping classification under 49 CFR Parts 171–180, required certification language, and discrepancy reporting fields. Use when preparing regulatory tracking documents for hazardous materials transportation, waste disposal compliance, or RCRA manifest packages.
tags:
  - drafting
  - regulatory
---

# Hazardous Waste Manifest (EPA Form 8700-22)

Drafts a RCRA-compliant Uniform Hazardous Waste Manifest establishing chain of custody from waste generation through final disposal.

## Prerequisites

1. **Generator EPA ID** — issued under 40 CFR Part 262; physical address of generation site
2. **Transporter records** — EPA ID, DOT registration, and permit status for each carrier in the chain
3. **TSDF authorization** — facility name, EPA ID, and state permits confirming acceptance of the specific waste type/quantity
4. **Waste characterization** — DOT proper shipping name, EPA hazardous waste codes (40 CFR Part 261), quantity (weight and volume), container count/type, hazard class, packing group
5. **Emergency contact** — 24-hour response number (CHEMTREC or company-specific line)

## Output Structure

### 1. Generator Information
| Field | Requirement |
|---|---|
| Legal business name | Full legal name of generating entity |
| Generation site address | Physical address (not mailing) |
| EPA ID number | 40 CFR Part 262 registration |
| Primary contact phone | Business hours |
| 24-hour emergency contact | Required for transport incidents |

### 2. Transporter Information *(repeat block per carrier)*
| Field | Requirement |
|---|---|
| Company legal name | As registered with EPA |
| Business address | — |
| EPA ID number | 40 CFR Part 263 |
| DOT registration number | 49 CFR Parts 171–180 |
| Signature/date block | Acknowledgment of custody receipt |

### 3. Designated Facility (TSDF)
| Field | Requirement |
|---|---|
| Facility legal name | As permitted |
| Physical address | — |
| EPA ID number | — |
| State permit numbers | Include DTSC or equivalent state authority numbers |
| Permitted waste types | Confirm alignment with waste codes on manifest |

> Verify TSDF is authorized for the specific waste type and quantity; confirm land disposal restriction (LDR) compliance and applicable treatment standards before designating facility.

### 4. Waste Description
| Field | Requirement |
|---|---|
| DOT proper shipping name | Per 49 CFR Part 172 |
| EPA hazardous waste codes | Four-digit codes from 40 CFR Part 261 |
| Quantity | Weight (kg/lbs) AND volume (liters/gallons) |
| Container type and count | DOT-approved container specifications |
| Physical/chemical form | Solid, liquid, sludge, etc. |
| Hazard class / packing group | DOT classification |
| Special handling requirements | If applicable |

### 5. Emergency Response & Certifications
- **24-hour emergency number**: CHEMTREC (1-800-424-9300) or company-specific line
- **Generator certification** (verbatim per 40 CFR 262.23):
  > *"I hereby declare that the contents of this consignment are fully and accurately described above by the proper shipping name, and are classified, packed, marked and labeled/placarded, and are in all respects in proper condition for transport according to applicable international and national governmental regulations. If export shipment and I am the Primary Exporter, I certify that the contents of this consignment conform to the terms of the attached EPA Acknowledgment of Consent."*

  Include the generator's waste minimization certification attesting that volume/toxicity reduction program is in place and disposal method minimizes threats to human health and environment.

### 6. Signatures & Discrepancy Reporting
- Signature blocks for: generator authorized representative → each transporter → receiving facility operator (each with date)
- Discrepancy report fields per **40 CFR 264.72 / 265.72**:
  - [ ] Quantity variation (significant vs. non-significant)
  - [ ] Container damage or count mismatch
  - [ ] Waste type or description discrepancy
  - [ ] Unacceptable waste notation
  - Space for facility to document irregularities triggering additional reporting obligations

### 7. Copy Distribution
Prepare copies for:
1. Generator's records (retained)
2. Each transporter (one per carrier)
3. Designated facility (TSDF)
4. Return copy to generator as proof of delivery/disposal

## Guidelines

- **Uniform manifest required**: Final document must conform to EPA Uniform Hazardous Waste Manifest format under 40 CFR Part 262, Subpart B
- **State overlays**: Some states (e.g., California, New York) require state-specific manifest forms or additional fields — check applicable state environmental agency requirements before finalizing
- **Multi-transporter chains**: Each transporter must have a separate signed acknowledgment block; verify all carriers hold current EPA and DOT credentials
- **LDR compliance**: Confirm that designated TSDF is authorized for the applicable land disposal restriction treatment standards before manifest execution
- **Discrepancy threshold**: Significant quantity discrepancies trigger facility notification obligations to the applicable EPA regional office — flag for attorney review if discrepancies arise
- **Retention**: Generator must retain manifest copies for minimum 3 years per 40 CFR 262.40 [VERIFY current retention period against any recent RCRA amendments]

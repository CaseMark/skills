---
name: bill-of-lading
description: >-
  Drafts a U.S. ocean Bill of Lading (B/L) that functions as receipt, contract
  of carriage, and document of title, with COGSA/Hague-Visby-aware clauses,
  negotiability designation, and charge allocation. Use when drafting or
  reviewing a bill of lading, master/house B/L, ocean carriage terms, shipment
  documentation, or title transfer in international trade. Trigger keywords:
  bill of lading, B/L, ocean carriage, COGSA, Hague-Visby, negotiable,
  straight, master bill, house bill.
tags:
  - agreement
  - drafting
  - regulatory
---

# Bill of Lading

Produce a complete B/L that accurately memorializes shipment, allocates risk, and complies with the governing carriage regime.

## Prerequisites

1. Shipper/consignee/notify party legal names, addresses, and contact details
2. Booking confirmation, vessel/voyage details, ports, and delivery terms
3. Packing list, commercial invoice, marks/numbers, weights, and measurements
4. Incoterms and freight payment terms (prepaid/collect), currency, and charges
5. Insurance/declared value instructions and any special handling requirements
6. Hazardous materials data (UN number, IMDG class) if applicable

## Output Structure / Process

Use the sections below in order. Populate from source documents only.

### Document Header

| Field | Required | Notes |
| --- | --- | --- |
| B/L Number | Yes | Unique identifier |
| B/L Type | Yes | `Negotiable` or `Straight (Non-negotiable)` |
| Issue Place/Date | Yes | City, country, date |
| Carrier | Yes | Legal name and address |
| Shipper | Yes | Legal name and address |
| Consignee | Yes | Legal name and address |
| Notify Party | Optional | If applicable |
| Vessel/Voyage | Optional | If known |
| Booking No. | Optional | If provided |
| Container/Seal Nos. | Optional | If applicable |

### Shipment Routing

| Field | Required | Notes |
| --- | --- | --- |
| Place of Receipt | Yes | Terminal or facility |
| Port of Loading | Yes | Port code if available |
| Port of Discharge | Yes | Port code if available |
| Place of Delivery | Yes | Final destination |
| Transshipment | Optional | List intermediate ports |

### Cargo Description

| Field | Required | Notes |
| --- | --- | --- |
| Description of Goods | Yes | Trade description; do not speculate |
| HS Code | Optional | If provided |
| Marks/Numbers | Optional | As on packages |
| Packages/Units | Yes | Count and unit type |
| Gross Weight | Yes | With unit |
| Measurement | Optional | CBM or other |
| Packaging | Optional | Type and condition |
| Declared Value | Optional | If higher liability requested |
| Special Handling | Optional | Fragile, reefer, etc. |
| HazMat | Conditional | IMDG class, UN number |

### Freight and Charges

| Field | Required | Notes |
| --- | --- | --- |
| Freight Term | Yes | Prepaid or Collect |
| Rate Basis | Yes | Per container/weight/measure |
| Additional Charges | Optional | THC, docs, fuel, security |
| Currency | Yes | ISO currency code |
| Payment Due | Optional | Date or upon release |

### Core Clauses Checklist

- Receipt in apparent good order and condition unless claused
- Carrier duty of due diligence to make vessel seaworthy
- Limitation of liability per COGSA $500 per package or customary freight unit unless higher value declared and paid [VERIFY]
- Notice of loss/damage timing (apparent vs concealed) [VERIFY]
- Time bar for suit (COGSA one year from delivery or due date) [VERIFY]
- Exceptions to liability (perils of the sea, act of God, inherent vice, shipper fault)
- General average clause and security for GA contributions
- Carrier lien for unpaid freight/charges
- Governing law and forum or arbitration clause
- Himalaya clause extending defenses to agents/subcontractors
- Both-to-blame collision clause if used by carrier

### Negotiability and Originals

- State number of originals issued and effect of surrender of one original
- If straight B/L, state non-negotiable and identify consignee
- If electronic B/L, specify system and rules governing eBL transfer

### Signature Blocks

- Carrier or agent signature, name, title, date
- Shipper signature if required by carrier practice
- Clausing space for exceptions to condition/quantity

### Output Template

```text
BILL OF LADING (B/L)
B/L No.: [_____]
Type: [Negotiable / Straight (Non-negotiable)]
Issue Place/Date: [_____]

Carrier: [Name, Address]
Shipper: [Name, Address]
Consignee: [Name, Address]
Notify Party: [Name, Address]

Place of Receipt: [_____]
Port of Loading: [_____]
Port of Discharge: [_____]
Place of Delivery: [_____]
Vessel/Voyage: [_____]
Booking No.: [_____]
Container/Seal Nos.: [_____]

Goods Description: [_____]
Marks/Numbers: [_____]
Packages/Units: [_____]
Gross Weight: [_____]
Measurement: [_____]
Declared Value: [_____]
Special Handling: [_____]
HazMat: [UN/IMDG if applicable]

Freight Term: [Prepaid/Collect]
Rate Basis: [_____]
Additional Charges: [_____]
Currency: [_____]
Payment Due: [_____]

Clauses: [COGSA/Hague-Visby regime, limitations, time bar, GA, lien, forum]
Originals: [#] originals issued; surrender of one renders others void
Signatures: Carrier/Agent [_____], Shipper [_____]
```

## Guidelines

- Do not invent data; mirror packing list, booking, and shipper instructions.
- If using Hague-Visby or other regime, state it expressly and remove conflicting COGSA language. [VERIFY]
- For letters of credit, issue a clean B/L only if no visible damage; otherwise clause accurately.
- Align freight term and Incoterms with buyer/seller responsibilities.
- If multimodal or door-to-door, clarify scope and liability regime for each leg.
- Confirm that any declared value matches carrier requirements for increased liability.
- Treat HS codes, weights, and counts as shipper-provided; avoid guarantees.
- Flag any jurisdiction-specific mandates or carrier standard terms that must be attached.

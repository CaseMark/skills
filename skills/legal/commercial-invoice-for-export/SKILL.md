---
name: commercial-invoice-for-export
description: Drafts a compliant Commercial Invoice for Export — the cornerstone document for international trade customs clearance, letter of credit payment, and multi-jurisdictional regulatory scrutiny. Enforces precise party identification, Incoterms 2020 compliance, HS tariff classification, country-of-origin determination, export control referencing, and certification language. Use when preparing export documentation for customs authorities, freight forwarders, banks, or insurance underwriters.
tags:
  - agreement
  - drafting
  - regulatory
---

# Commercial Invoice for Export

Drafts a legally precise export commercial invoice satisfying customs, banking (L/C), logistics, and insurance requirements simultaneously.

## Prerequisites

1. **Purchase order / proforma invoice** — agreed pricing, quantity, product specs
2. **Sales contract or L/C** — payment terms, special notations, latest shipment date
3. **Export license** (if controlled goods) — license number, expiration, ECCN or USML category
4. **Shipping instructions** — Incoterm, named place/port, carrier details
5. **Origin documentation** — country of manufacture, FTA qualification basis if claiming preference

## Output Structure

### 1. Header & Invoice Reference

| Field | Requirement |
|---|---|
| Invoice Number | Sequential, non-duplicative; traceable in export compliance/accounting systems |
| Invoice Date | DD/MM/YYYY for most international markets; MM/DD/YYYY if US-only transaction |
| Cross-references | Bill of lading / AWB number, packing list ref, certificate of origin number |

---

### 2. Party Identification

**Exporter / Shipper**
- Full legal registered name (not trade name or DBA unless that is the registered name)
- Complete registered address: street, suite, city, state/province, postal code, country
- Tax ID / EIN / VAT registration number / export registration number
- International telephone (with country + area code) and designated customs/shipping email

**Consignee / Importer**
- Full legal name as registered in destination country
- Delivery or customs clearance address (include FTZ designation, bonded warehouse code, or SEZ indicator if applicable)
- Importer tax ID in destination-country format (EU VAT, CA BN, US EIN, etc.)
- Import license number or customs broker reference if required
- Authorized contact: name, title, direct phone, email

> All party details must match purchase orders, L/C, import permits, and AES/EEI filings character-for-character.

---

### 3. Commercial & Shipping Terms

| Field | Format |
|---|---|
| Incoterms 2020 | Three-letter code + full named place. Example: `FOB Shanghai Port, China` or `DDP 123 Industrial Blvd, Toronto, Ontario M1M 1M1, Canada` |
| Currency | Transaction currency; unit prices must reflect all costs included under the Incoterm |
| Payment Terms | Net days, L/C reference, D/P, D/A, etc. |

---

### 4. Goods Description & Valuation

Each line item must include:

| Column | Requirement |
|---|---|
| Description | Specific technical detail — no vague terms like "machine parts" or "electronics." Include: commercial name, dimensions with units, material/composition, model/part number, brand, intended use, manufacturing process if classification-relevant |
| HS / HTS Code | 6-digit HS minimum; extend to 8–10 digits per destination country schedule. Verify against current tariff schedule; flag classification risk for high-duty or controlled items |
| Country of Origin | Legal determination (substantial transformation / tariff shift / RVC as applicable); not simply exporter's location |
| Quantity & UOM | Metric units preferred (kg, MT, L, m², m³); include both shipping units (cartons, pallets) and item count |
| Unit Price | Must match proforma/PO/L/C exactly |
| Line Total | Quantity × Unit Price; verify arithmetic |

**Totals block:**
- Subtotals by product category (if multiple)
- Total merchandise value
- Freight, insurance (itemized or included per Incoterm — state clearly)
- **Net weight** (goods only, excl. packaging) in kg
- **Gross weight** (goods + all packaging/pallets) in kg

---

### 5. FTA / Preferential Origin (if applicable)

- Identify the FTA (USMCA, CPTPP, EU agreement, ASEAN, bilateral)
- State the applicable rule of origin satisfied (tariff shift, RVC threshold, specific process)
- Reference certificate of origin number, issuing authority, and date
- Note: exporter must hold approved-exporter status if required by the FTA

---

### 6. Export Control Notation (if applicable)

For EAR- or ITAR-controlled goods:
```
Export Control Classification Number (ECCN): [ECCN]
License Number: [number] | Expiration: [date]
— OR —
License Exception: [cite exception, e.g., EAR99 / NLR]
USML Category: [category] (ITAR)
```

---

### 7. Certification & Signature Block

Include verbatim or substantively equivalent declaration:

> *"I hereby certify that the information contained in this invoice is true, correct, and complete; that the goods are of the country of origin stated; that the prices shown are the actual transaction value with no undisclosed considerations; and that this shipment is in full compliance with applicable export control regulations, trade laws, economic sanctions, and anti-boycott requirements of the exporting country. I understand that civil and criminal penalties may be imposed for false or fraudulent statements."*

Signature block fields:
- Handwritten signature line
- Printed name
- Title
- Date (jurisdiction-appropriate format)
- Company seal / chamber stamp / notarization space (if required by destination country or L/C)

---

## Guidelines

- **L/C compliance**: Verify every invoice element against L/C field-by-field — description, quantity, value, Incoterm, latest shipment date, and any special notations. Any discrepancy risks payment refusal without amendment.
- **No generic descriptions**: Customs undervaluation or misclassification penalties apply to vague descriptions. Use HS-aligned language.
- **Tariff code verification**: HS codes and duty rates change. For high-value or controlled goods, recommend binding tariff ruling from destination-country customs authority or licensed customs broker review.
- **Origin ≠ exporter location**: Multi-country production requires documented substantial transformation, tariff shift, or RVC analysis.
- **Recordkeeping**: Retain invoice and all supporting documents for 5 years (US EAR requirement); 5–10 years in other jurisdictions. Must be audit-ready.
- **Missing information**: If any required field cannot be determined from uploaded documents, identify the gap, explain the compliance risk, and request the information before issuing.
- **Weights**: Always provide both net and gross weight; required by most customs authorities for duty assessment and freight calculation.

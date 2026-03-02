# AML Red Flag Typologies

Categorized reference for transaction screening. Each typology includes indicators and the activity patterns that trigger it.

> **Usage:** During Step 2 of the `auditing-aml-transactions` skill, screen transaction data against each applicable category below. Cite typology names exactly when documenting findings.

---

## 1. Structuring (Smurfing)

Deliberate breaking of transactions to avoid CTR filing thresholds or other reporting requirements.

| Indicator | Description |
|---|---|
| Sub-threshold cash deposits | Multiple cash deposits just below $10,000 across one or more days |
| Multiple-branch deposits | Same-day cash deposits at different branches of the same institution |
| Multiple-account deposits | Splitting deposits across several accounts held by the same or related parties |
| Declining amounts | Sequential deposits that decrease in amount (e.g., $9,500 → $9,200 → $8,800) suggesting awareness of aggregation |
| Third-party structuring | Multiple unrelated individuals depositing cash into the same account |
| ATM structuring | Repeated ATM cash deposits just below reporting thresholds |

---

## 2. Rapid Movement of Funds

Funds deposited and moved out quickly with no apparent holding period or business purpose.

| Indicator | Description |
|---|---|
| Immediate wire-out | Funds deposited (cash, check, ACH) and wired out within 24-48 hours |
| Pass-through activity | Account used as conduit — credits closely match debits with minimal balance retained |
| Funnel account | Multiple deposits from various geographic locations followed by rapid consolidation and withdrawal |
| Layering transfers | Funds moved through multiple accounts or institutions in quick succession to obscure origin |
| Deposit-and-withdraw cycle | Repeated pattern of deposit followed by same-day cash withdrawal of similar amount |

---

## 3. Cash-Intensive Activity

Unusual cash transaction patterns inconsistent with customer profile or business type.

| Indicator | Description |
|---|---|
| Cash volume inconsistent with business | Cash deposits significantly exceed expected levels for the stated business type |
| Cash-intensive business with no cash explanation | Business type not typically cash-intensive but generates large cash volumes |
| Large cash exchanges | Exchanging large volumes of small-denomination bills for large denominations (or vice versa) |
| Structured cash purchases | Purchasing monetary instruments (cashier's checks, money orders) in amounts just below reporting thresholds |
| Cash deposits to business account for personal use | Business account cash deposits followed by personal expenditures |

---

## 4. Geographic Risk

Transactions involving jurisdictions with elevated money laundering or terrorist financing risk.

| Indicator | Description |
|---|---|
| FATF high-risk jurisdictions | Transactions with countries on the FATF list of high-risk and non-cooperative jurisdictions |
| OFAC-sanctioned countries | Any nexus to comprehensively sanctioned countries (North Korea, Iran, Cuba, Syria, Crimea region) |
| Drug-source countries | Wire activity to/from known drug-source or drug-transit countries with no apparent business purpose |
| Tax haven layering | Funds routed through multiple offshore financial centers with no business justification |
| Cross-border inconsistency | Customer with no stated international business conducting frequent cross-border wires |
| Correspondent banking risk | Transactions through respondent banks in high-risk jurisdictions (nested correspondent risk) |

---

## 5. Shell Company & Layering

Use of legal entities to obscure beneficial ownership or the source/destination of funds.

| Indicator | Description |
|---|---|
| Opaque ownership | Entity with nominee directors, bearer shares, or complex multi-jurisdictional ownership |
| No physical presence | Business entity with no employees, office, or inventory at stated address |
| Mismatched activity | Entity activity inconsistent with stated business purpose (e.g., consulting firm receiving large cash deposits) |
| Rapid entity formation | Multiple entities formed in quick succession and used for transactions before establishing operations |
| Round-tripping | Funds sent to entity offshore and returned as a "loan" or "investment" to the same beneficial owner |
| Intercompany transfers | Complex web of transfers among related entities with no clear commercial purpose |

---

## 6. Wire Transfer Red Flags

Suspicious patterns specific to wire transfer activity.

| Indicator | Description |
|---|---|
| Round-dollar wires | Frequent wire transfers in round amounts inconsistent with commercial invoicing |
| Amended wire instructions | Frequent changes to beneficiary information or intermediary banks |
| Cover payment anomalies | Wire routing that obscures originator or beneficiary through cover/serial payment methods |
| Unrelated third-party wires | Incoming/outgoing wires involving parties with no apparent relationship to account holder |
| High-volume low-value wires | Large number of small wires to the same destination (potential structuring of wire activity) |
| Wires to/from personal accounts for business | Business-purpose wires routed through personal accounts |

---

## 7. Trade-Based Money Laundering (TBML)

Manipulation of trade transactions to transfer value or disguise illicit proceeds.

| Indicator | Description |
|---|---|
| Over/under invoicing | Invoice amounts significantly above or below fair market value for the goods described |
| Phantom shipments | Trade documents for goods that were never shipped or do not exist |
| Multiple invoicing | Same goods invoiced multiple times to justify multiple payments |
| Commodity misrepresentation | Goods described on documents differ from actual goods shipped |
| Mismatched trade partners | Trade between parties with no logical commercial relationship |
| Black market peso exchange indicators | Payments for goods made by unrelated third parties in a different country |

---

## 8. Behavioral & Account Red Flags

Customer behavior and account characteristics that suggest awareness of detection efforts.

| Indicator | Description |
|---|---|
| Reluctance to provide information | Customer avoids or delays providing KYC documentation, beneficial ownership, or source of funds |
| Unusual knowledge of reporting | Customer asks about CTR thresholds, SAR filing, or monitoring systems |
| Frequent address/contact changes | Account information changed repeatedly to prevent contact or obscure identity |
| Multiple SSN/TIN usage | Same individual associated with multiple identification numbers |
| Dormant account reactivation | Long-dormant account suddenly receives large deposits followed by rapid outflows |
| Sudden change in activity pattern | Transaction volume, type, or geography changes dramatically without explanation |
| Account opened and closed quickly | Account opened, used for a burst of activity, then closed within a short period |
| Power of attorney abuse | Third party with POA conducting transactions inconsistent with account holder's profile |

---

## 9. Insider / Collusion Indicators

Signs that an institution employee may be facilitating or ignoring suspicious activity.

| Indicator | Description |
|---|---|
| Override patterns | Employee repeatedly overrides transaction monitoring alerts for the same customer |
| Threshold coaching | Employee advises customer on how to avoid triggering reports |
| Personal relationship | Employee has undisclosed personal or financial relationship with customer |
| Exception processing | Employee processes transactions outside normal procedures without documented approval |
| Unusual account access | Employee accessing accounts outside their job function or branch |

---

## 10. Emerging Typologies

Newer patterns recognized by FinCEN advisories and FATF reports.

| Indicator | Description |
|---|---|
| Virtual currency nexus | Fiat-to-crypto on-ramp/off-ramp transactions with no stated purpose; transactions with unhosted wallets |
| Human trafficking indicators | Payments to online classified sites, hotels, and travel in patterns consistent with trafficking (see FinCEN FIN-2020-A008) |
| COVID/disaster fraud | PPP/EIDL loan proceeds used inconsistently with stated purpose; rapid diversion of relief funds |
| Ransomware payments | Large, urgent wire or crypto payments to unfamiliar parties following a cybersecurity incident |
| Professional money laundering networks | Use of professional gatekeepers (lawyers, accountants, real estate agents) to layer funds through legitimate-appearing transactions |
| Real estate ML | All-cash real estate purchases through LLCs, rapid flipping, or purchases significantly above/below market value |

---

## Severity Classification Guide

When assigning severity to identified red flags:

| Severity | Criteria |
|---|---|
| **High** | Multiple typologies present; activity cannot be explained by stated business purpose; involves OFAC/sanctions nexus, structuring, or insider indicators; dollar amounts are material |
| **Medium** | Single typology present with corroborating factors; activity is unusual but may have partial explanation; moderate dollar amounts |
| **Low** | Isolated indicator that may be explained by legitimate activity; minimal dollar amounts; no corroborating factors |

> **Note:** A cluster of Low-severity indicators can collectively warrant a High-severity disposition. Always assess the totality of activity, not individual flags in isolation.

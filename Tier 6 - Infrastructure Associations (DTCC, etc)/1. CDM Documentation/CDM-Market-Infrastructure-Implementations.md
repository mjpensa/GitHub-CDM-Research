# CDM Market Infrastructure Implementations

## Overview

This document tracks financial market infrastructure organizations that have implemented or are actively supporting CDM adoption.

---

## Production Implementations

### JSCC (Japan Securities Clearing Corporation)

| Field | Details |
|-------|---------|
| **Organization** | Japan Securities Clearing Corporation |
| **Type** | Central Counterparty (CCP) |
| **Status** | Production |
| **Announcement** | January 2025 |
| **Significance** | First CCP globally to adopt CDM/DRR in production |
| **Use Case** | Digital Regulatory Reporting |

### JPX (Japan Exchange Group)

| Field | Details |
|-------|---------|
| **Organization** | Japan Exchange Group |
| **Type** | Exchange |
| **Status** | Production Parallel |
| **Use Case** | CDM-based DRR for regulatory reporting |
| **Significance** | First financial institution in Japan to adopt DRR |

### BNP Paribas

| Field | Details |
|-------|---------|
| **Organization** | BNP Paribas |
| **Type** | Global Bank |
| **Status** | Production |
| **Go-Live** | November 2022 |
| **Jurisdiction** | US (CFTC) |
| **Significance** | First company globally to go live with DRR under CFTC amended swap data reporting rules |
| **Repository** | DTCC swap data repository |

### JPMorgan Chase

| Field | Details |
|-------|---------|
| **Organization** | JPMorgan Chase |
| **Type** | Global Bank / CDM Maintainer |
| **Status** | Production |
| **Announcement** | October 2024 |
| **Use Case** | Primary reporting mechanism using CDM/DRR |
| **Role** | Also serves as CDM maintainer on FINOS |

---

## Infrastructure Partners

### DTCC (Depository Trust & Clearing Corporation)

| Field | Details |
|-------|---------|
| **Organization** | DTCC |
| **Type** | Post-trade infrastructure |
| **Role** | DRR validation partner |
| **Partnership** | REGnosys partnership for DRR report validation |
| **Function** | Validates DRR reports generated via Rosetta against DTCC repositories |
| **Collaboration** | Worked with Barclays and ICMA on post-trade use cases |

### SWIFT

| Field | Details |
|-------|---------|
| **Organization** | SWIFT |
| **Type** | Messaging network |
| **Role** | Standards alignment |
| **Integration** | CDM designed to align with FIX and ISO 20022 messaging |
| **Note** | CDM core model remains vendor/protocol agnostic |

---

## Active Development Partners

### Goldman Sachs

| Field | Details |
|-------|---------|
| **Organization** | Goldman Sachs |
| **Type** | Global Bank |
| **Status** | Testing/Development |
| **Role** | FINOS member actively supporting DRR development |

### Barclays

| Field | Details |
|-------|---------|
| **Organization** | Barclays |
| **Type** | Global Bank |
| **Contribution** | DerivHack host (2018, 2019) |
| **Use Cases** | Developed 7 post-trade use cases with DTCC and ICMA |
| **Scope** | Front-to-back trade flow simulation, client account portfolio allocations |

---

## Regulatory Adoption

### Jurisdictions with DRR Support

| Jurisdiction | Regulator | Status |
|--------------|-----------|--------|
| **United States** | CFTC | Production (since Nov 2022) |
| **European Union** | ESMA (EMIR, MiFIR) | Supported |
| **United Kingdom** | FCA (UK EMIR, UK MiFIR) | Supported |
| **Japan** | JFSA | Production |
| **Australia** | ASIC | Supported (Oct 2024) |
| **Singapore** | MAS | Supported (Oct 2024) |
| **Hong Kong** | SFC/HKMA | Planned |
| **Canada** | Various | Planned |
| **Switzerland** | FINMA | Planned |

### UK Digital Regulatory Reporting Pilot

| Field | Details |
|-------|---------|
| **Regulators** | FCA, Bank of England |
| **Status** | Pilot Phase 2 completed |
| **Timeline** | Tech sprints 2016-2017, Phase 1 2018, Phase 2 2019 |
| **Technology** | ISDA CDM 2.0 deployed |
| **Programme** | Transforming Data Collection (TDC) |

---

## Technology Vendors in Production

| Vendor | Role | CDM Integration |
|--------|------|-----------------|
| **REGnosys** | Rosetta platform provider | Core technology partner |
| **TradeHeader** | CDM maintainer | Implementation services |
| **Digital Asset** | DLT platform | CDM-native smart contracts |
| **Tokenovate** | Tokenization | CDM for tokenized assets |

---

## Key Milestones

| Date | Milestone |
|------|-----------|
| Nov 2022 | BNP Paribas first CFTC DRR production |
| Feb 2023 | CDM transferred to FINOS |
| Nov 2023 | CDM 5.0 release |
| Apr 2024 | DRR extended to UK, Australia, Singapore |
| Jun 2025 | CDM 6.0 release |
| Oct 2024 | JPMorgan implements CDM/DRR as primary reporting |
| Jan 2025 | JSCC announces CDM/DRR adoption |

---

## Sources

- ISDA Press Releases: https://www.isda.org/category/infrastructure/common-domain-model/
- FINOS CDM Blog: https://www.finos.org/blog
- Industry Perspectives on ISDA DRR (Nov 2025): https://www.isda.org/a/LhRgE/Industry-Perspectives-on-the-ISDA-DRR-Unlocking-Efficiency-Accuracy-and-Strategic-Value.pdf

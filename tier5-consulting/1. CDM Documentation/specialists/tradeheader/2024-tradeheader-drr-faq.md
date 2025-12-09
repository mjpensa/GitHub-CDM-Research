# DRR: Frequently Asked Questions

**Source:** TradeHeader
**Published:** December 5, 2024
**Author:** Marc Gratacos
**URL:** https://www.tradeheader.com/blog/drr-frequently-asked-questions

---

## Introduction

ISDA Digital Regulatory Reporting (DRR) represents an industry framework designed to digitize, standardize, and automate regulatory reporting for derivatives transactions. The framework leverages the Common Domain Model (CDM) to convert agreed-upon regulatory interpretations into executable code, improving implementation efficiency and reducing costs. TradeHeader co-created both CDM and DRR, actively participating in working groups and development efforts.

---

## Q&A Section

### 1. What is DRR?
DRR is ISDA's framework for digitalizing, standardizing, and automating regulatory reporting for derivatives. It substantially decreases the time, resources, and expenses required to implement reporting regulations across multiple jurisdictions.

### 2. What is the difference between DRR and CDM?
CDM is a standardized, machine-readable blueprint for representing derivatives transactions throughout their lifecycle. DRR applies CDM's standardized representation to implement reporting logic and validation across multiple jurisdictions.

### 3. How do firms implement DRR?
DRR distributes Java libraries implementing free-to-use industry-standard reporting logic. Firms must integrate these libraries into their reporting systems, utilizing reporting logic developed from participating firms' collective interpretation.

### 4. How do we map FpML or my internal data format to DRR?
Three mapping approaches exist:
- REGnosys's commercial translation service
- Commercial Extract, Transform, Load (ETL) solutions
- Custom-built mapping implementations

### 5. Who is managing DRR?
ISDA supports DRR development. The ISDA DRR Steering Committee, formed by participating financial institutions, establishes project scope and priorities.

### 6. Who is contributing to DRR? Do I need to become an ISDA member to contribute?
Contributing institutions include BNP Paribas, Pictet Group, Standard Chartered, and JPMorgan. Contribution doesn't require ISDA membership; participants must adhere to project licensing requirements.

### 7. Are all contributed changes added directly to the public version of the DRR model?
No. Changes undergo careful review by ISDA Peer Review working groups (US & Europe, and Asia) to ensure regulatory compliance and industry-wide acceptance.

### 8. How is DRR being distributed?
Currently distributed in Java, the model is developed using Rune DSL, with an open-source code generator automatically creating Java distributions.

### 9. Is DRR open source?
DRR is not open source but remains free-to-use for both ISDA and non-ISDA members.

### 10. Who has implemented DRR?
BNP Paribas, Pictet Group, and JPMorgan have implemented CDM and DRR in production environments.

### 11. What jurisdictions does it cover?
Current coverage includes CFTC, ESMA (EMIR), JFSA, FCA, ASIC, and MAS.

### 12. Are there plans to cover more jurisdictions?
Yes. ISDA committed to expansion; 2025 development includes CSA, HKMA, US SEC, ESMA+FCA (MiFIR), and FINMA.

### 13. Is reporting eligibility included in DRR?
Currently, DRR does not cover reporting eligibility—the determination of whether transactions require regulatory reporting.

### 14. Does DRR include business validation rules from the regulators?
Yes, DRR incorporates business validation rules extracted from regulations and some Trade Repositories.

### 15. Does DRR produce ISO 20022 message format?
Yes, DRR generates appropriate reports in ISO 20022 format as required by certain regulators.

### 16. Could DRR be extended or customized?
Yes, through two approaches:
- Extending/customizing the model using Rune DSL syntax
- Extending/customizing generated Java code

### 17. Where are custom extensions placed?
Custom extensions should occupy separate namespaces/files from the public model, ensuring clarity and facilitating version upgrades.

### 18. Can the DRR access external data?
Yes, DRR supports API call integration for retrieving external data sources. Implementation responsibility—including API key management—falls to the using firm.

### 19. What is the relationship between ISDA and TradeHeader?
TradeHeader serves as a technology provider to ISDA, offering advisory and implementation services on CDM and DRR development, plus training to firms.

### 20. Where can I download the DRR distribution?
Downloads available at the DRR documentation site. Additional resources include ISDA website materials and YouTube explainer videos.

---

*Original source: TradeHeader*
*Collected: December 2025*

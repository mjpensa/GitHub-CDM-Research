# Official ISDA Documents Related to CDM on GitHub

This document catalogs all official ISDA (International Swaps and Derivatives Association) documents related to the CDM (Common Domain Model) available on GitHub.

## 1. Primary Official Repository

### FINOS Common Domain Model
**Repository**: https://github.com/finos/common-domain-model

The official, actively maintained CDM repository hosted under FINOS (Fintech Open Source Foundation). The sponsoring Trade Associations (ISDA, ISLA and ICMA) have commissioned REGnosys to provide the CDM Release Management Service.

#### Key Documents in this Repository:

| Document | Description |
|----------|-------------|
| [README.md](https://github.com/finos/common-domain-model/blob/master/README.md) | Main project overview, CDM purpose and design principles |
| [CONTRIBUTING.md](https://github.com/finos/common-domain-model/blob/master/CONTRIBUTING.md) | Contribution guidelines |
| [GOVERNANCE.md](https://github.com/finos/common-domain-model/blob/master/GOVERNANCE.md) | Roles (Maintainers, Editors, Participants), working groups, decision-making |
| [LICENSE.md](https://github.com/finos/common-domain-model/blob/master/LICENSE.md) | Community Specification License 1.0 |
| [NOTICE.md](https://github.com/finos/common-domain-model/blob/master/NOTICE.md) | Copyright notices, ISDA licensing history |
| [Participants.md](https://github.com/finos/common-domain-model/blob/master/Participants.md) | List of project participants |
| [ROADMAP.md](https://github.com/finos/common-domain-model/blob/master/ROADMAP.md) | Strategic roadmap with ICMA, ISDA, and ISLA contributions |
| [RELEASE.md](https://github.com/finos/common-domain-model/blob/master/RELEASE.md) | Release management documentation |
| [SCOPE.md](https://github.com/finos/common-domain-model/blob/master/SCOPE.md) | Project scope definition |

#### Directory Structure:
- **docs/** - Comprehensive documentation
- **rosetta-source/** - Model source files in Rosetta DSL
- **examples/** - Usage examples
- **tests/** - Test files
- **website/** - CDM documentation website source

#### Latest Releases:
- **v7.0.0-dev.62** (Dec 5, 2024) - Legal Agreements refactoring
- **v5.30.0** (Dec 5, 2024) - Reference Data Model with EntityIdentifier support
- **v6.12.0** (Nov 26, 2024) - FpML Confirmation to CDM mapping

---

## 2. Legacy ISDA CDM License

### freight-trust/cdm
**Repository**: https://github.com/freight-trust/cdm

Contains the official **ISDA CDM License Version 2.0** (effective February 26, 2019).

#### Key Documents:
| Document | Description |
|----------|-------------|
| [ISDA_CDMTM_License_Version_2.0](https://github.com/freight-trust/cdm/blob/master/ISDA_CDMTM_License_Version_2.0) | Official ISDA CDM License text |

#### License Key Provisions:
- Grants worldwide, royalty-free, non-exclusive license
- Allows use within larger works without modifications
- Prohibits misleading use of "ISDA" or "ISDA CDM" designations
- New York law governance with JAMS arbitration

---

## 3. ISDA Definitions and Standards

### manifoldfinance/isda
**Repository**: https://github.com/manifoldfinance/isda

Contains ISDA definitions, functions, and data types documentation.

#### Documentation Categories:

**Functions (Business Logic)**:
- Equity Derivatives: NewEquitySwapProduct, EquityPriceObservation, RateOfReturn
- Lifecycle Events: Execute, FormContract, Reset, Allocate, Settle, Terminate
- Calculations: EquityCashSettlementAmount, EquityPerformance

**Data Types**:
- Product specifications (AmericanExercise, BermudaExercise, EuropeanExercise)
- Agreement types (MasterAgreement, MasterConfirmation, CreditSupportAgreement)
- Financial instruments (bonds, options, swaps, CDS)

---

## 4. CDM Event Specification Module

### digital-asset-archive/lib-cdm-event-specification-module
**Repository**: https://github.com/digital-asset/lib-cdm-event-specification-module

An extension to the ISDA CDM schema that standardizes the process of generating valid CDM event messages.

#### Key Documents:
| Document | Description |
|----------|-------------|
| [docs/autogen/CdmTypes.md](https://github.com/digital-asset-archive/lib-cdm-event-specification-module/blob/master/docs/autogen/CdmTypes.md) | Auto-generated CDM type documentation |

**License**: Apache-2.0

---

## 5. CDM DAML Implementation

### digital-asset-archive/ex-cdm-swaps
**Repository**: https://github.com/digital-asset-archive/ex-cdm-swaps

DAML implementation of ISDA CDM for swaps.

#### Key Files:
| File | Description |
|------|-------------|
| [daml/Org/Isda/Cdm/Classes.daml](https://github.com/digital-asset-archive/ex-cdm-swaps/blob/master/daml/Org/Isda/Cdm/Classes.daml) | ISDA CDM classes in DAML |

---

## 6. Rosetta DSL (CDM Foundation)

### REGnosys/rosetta-dsl
**Repository**: https://github.com/REGnosys/rosetta-dsl

The Domain-Specific Language used to define the CDM. Originally developed by ISDA/REGnosys.

#### Background:
- Developed starting in 2017, first deployed in 2018
- Initially sponsored by ISDA for derivatives post-trade operations
- Open-sourced in 2019 alongside the CDM

---

## 7. Additional Implementations

### TypeScript CDM Implementation
**Repository**: https://github.com/mvanmeerbeck/ts-cdm

TypeScript implementation of the ISDA CDM model.

---

## 8. Related FINOS Resources

### finos/legend (Goldman Sachs & ISDA Collaboration)
**Issue**: https://github.com/finos/legend/issues/305

Documentation of GS-ISDA-REGnosys work sessions for CDM integration with Legend platform.

---

## Official External Resources

| Resource | URL |
|----------|-----|
| CDM Official Documentation | https://cdm.finos.org/ |
| ISDA CDM Page | https://www.isda.org/cdm/ |
| CDM Downloads | https://cdm.finos.org/docs/download/ |
| Legacy CDM Portal (pre-4.0.0) | https://portal.cdm.rosetta-technology.io/#/ |

---

## Licensing History

| Period | License |
|--------|---------|
| Pre-4.0.0 | ISDA CDM License (Version 2.0) |
| 4.0.0+ (Feb 2023) | Community Specification License 1.0 (under FINOS) |

---

## Working Groups & Governance

The CDM has several active working groups documented on GitHub:

1. **CDM Derivatives Products and Business Events Working Group**
   - https://github.com/finos/common-domain-model/issues/3122

2. **CDM Collateral Working Group**
   - https://github.com/finos/common-domain-model/issues/3121

3. **CDM Tokenized Assets Working Group**
   - https://github.com/finos/common-domain-model/discussions/4011

4. **CDM Design Principles Discussion**
   - https://github.com/finos/common-domain-model/discussions/2422

---

## Key GitHub Topics for Discovery

- https://github.com/topics/common-domain-model
- https://github.com/topics/isda

---

*Document generated: December 7, 2025*
*Source: GitHub repositories and ISDA/FINOS official resources*

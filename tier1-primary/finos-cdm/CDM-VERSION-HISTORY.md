# CDM Version History and Release Documentation

**Date:** December 2025
**Source:** FINOS CDM GitHub Repository, CDM Documentation
**Classification:** Version History

---

## Overview

This document provides comprehensive version history for the Common Domain Model (CDM), including release states, version timeline, and key features of major releases.

---

## Release State Definitions

The CDM uses the following release states:

| State | Description |
|-------|-------------|
| **Development** | Versions from "main" branch still under development. All tests pass but model may evolve. |
| **Production** | Latest stable version - "latest and greatest" that everyone should upgrade to. Target ~1 year lifecycle. |
| **Maintenance** | Previous Production version. Only critical bug fixes and regulatory requirement changes. |
| **Unsupported/End of Life** | No bug fixes or support. May perform security scans but no remediation. |

**Target:** Maximum 1 development version, 1 production version, and 1 maintenance version at any time.

---

## Current Version Status (December 2025)

| Version Series | Status | Notes |
|----------------|--------|-------|
| **7.0.0-dev.x** | Development | Major refactoring release |
| **6.x.x** | Production | Current stable version |
| **5.x.x** | Maintenance | Previous production version |

---

## Version 7.x Series (Development)

### 7.0.0-dev.62 (December 5, 2025)
**Focus:** Legal Agreements

- Legal Agreements refactoring: Enhanced CSA and CTA Elections
- Refactored `CreditSupportAgreementElections` into base type with specialized subtypes:
  - `CreditSupportAgreementElectionsBase`
  - `CreditSupportAgreementInitialMarginElections`
  - `CreditSupportAgreementVariationMarginElections`
  - `CreditSupportAgreementLegacyElections`
- Refactored `CreditSupportObligations` similarly
- Refactored `CalculationandTiming` similarly
- Updates to cardinality and descriptions

### 7.0.0-dev.61 (December 2, 2025)
- Securities Lending FIX samples added to Rosetta Visualisations

### 7.0.0-dev.60 (December 2, 2025)
**Focus:** Product Model

- Observable price sub types introduced via new `PriceSubTypeEnum`
- Enhanced `PriceSchedule` with optional `priceSubType` attribute
- Removed `cashPrice` from `PriceSchedule`
- Added `premiumType` directly

### 7.0.0-dev.59 (December 1, 2025)
**Focus:** Securities Lending

- Securities Lending examples added (cash collateral, non-cash collateral variants)

### 7.0.0-dev.58 (November 27, 2025)
- Product Model: `ScheduledTransferEnum` renamed "PrincipalPayment" to "Principal"

### 7.0.0-dev.56 (November 20, 2025)
**Focus:** Legal Agreement Model

- Restructured `PartyContactInformation`
- New `ContactInformationElection` base type with specialized subtypes

### 7.0.0-dev.55 (November 17, 2025)
- Added/modified product qualification functions for swaps and forwards

---

## Version 6.x Series (Production)

### 6.12.0 (November 26, 2025)
- FpML Confirmation to CDM ingest functions with regression testing
- `MarginAffiliate` added to `PartyRoleEnum`

### 6.0.0 (Major Release)
**Key Features:**
- Over 100 functional and technical enhancements
- Asset Refactoring initiative
- Streamlined financial product modeling
- Enhanced support for all transaction types
- Addressed years of accumulated inconsistencies
- Second major update since FINOS hosting

---

## Version 5.x Series (Maintenance)

### 5.30.0 (December 5, 2025)
- Reference Data Model expanded with Legal Entity Identifier Type Support
- New `EntityIdentifierTypeEnum` supporting RED, CountryCode, Other identifier types
- Added `MarginAffiliate` to `PartyRoleEnum` per CFTC requirements

### 5.0.0 (Major Release)
**Key Features:**
- First major release under FINOS governance
- FINOS hosting began February 2023
- Established open source governance model
- Community Specification License 1.0 adoption

---

## Pre-FINOS Era (Historical)

### CDM Origins
- **2017:** ISDA began CDM initiative
- **2018-2019:** DerivHack hackathons demonstrated CDM on DLT platforms
- **February 2023:** CDM transitioned to FINOS as open standard

---

## 2025 CDM Roadmap

The 2025 roadmap is jointly sponsored by FINOS, ICMA, ISDA, and ISLA.

### Key Focus Areas

| Area | Initiative |
|------|------------|
| **Regulatory Reporting** | DRR expansion to new jurisdictions (Hong Kong, Canada, MiFIR) |
| **Collateral Management** | Collateral eligibility standardization |
| **Legal Documentation** | Document digitization (ISDA Master Agreements, CSAs) |
| **Securities Lending** | Enhanced GMSLA support with ISLA |
| **Repo/Bonds** | Continued ICMA collaboration |

---

## Version Compatibility Matrix

| CDM Version | Rosetta DSL | Java | Python | Scala |
|-------------|-------------|------|--------|-------|
| 7.x (dev) | Latest | 17+ | 3.10+ | 2.13+ |
| 6.x | Latest | 11+ | 3.10+ | 2.13+ |
| 5.x | Supported | 11+ | 3.9+ | 2.13+ |

---

## Breaking Changes

### 7.0.0 Breaking Changes (Expected)
- Legal Agreement model restructuring
- `CreditSupportAgreementElections` hierarchy change
- `PriceSchedule` attribute changes (`cashPrice` removal)
- Enum value renames in `ScheduledTransferEnum`

### 6.0.0 Breaking Changes
- Asset model refactoring
- Product model changes
- Type hierarchy changes

---

## Migration Guidance

### 5.x to 6.x Migration
- Review Asset Refactoring changes
- Update product model references
- Test all qualification functions

### 6.x to 7.x Migration (Future)
- Legal Agreement model updates required
- Price handling changes
- Contact information model updates

---

## Release Schedule (2024-2025)

Based on CDM Release Guidelines Task Force (July 2024):

| Version Type | Frequency | Notes |
|--------------|-----------|-------|
| Development | Continuous | From main branch |
| Production | ~Annual | Minimum 1 year lifecycle |
| Maintenance | As needed | Critical fixes only |

---

## Resources

| Resource | URL |
|----------|-----|
| CDM Releases | https://github.com/finos/common-domain-model/releases |
| CDM Documentation | https://cdm.finos.org/ |
| Roadmap | https://github.com/finos/common-domain-model/blob/master/ROADMAP.md |
| Contributing | https://github.com/finos/common-domain-model/blob/master/CONTRIBUTING.md |

---

## Maintainers

Current CDM maintainers (as of December 2025):

| Organization | Representatives |
|--------------|-----------------|
| ICMA | Gabriel Callsen, Tom Healey |
| ISDA | Vernon Alden-Smith, Eleonora Acuna, David Shone, Lyteck Lynhiavu |
| ISLA | Adrian Dale, Chris Rayner |
| REGnosys | Minesh Patel, Leo Labeis, Hugo Hills |
| TradeHeader | Manuel Martos, Marc Gratacos |
| JPMorgan Chase | Nicholas Moger |

---

*Compiled: December 2025*
*Sources: FINOS CDM GitHub Repository, CDM Documentation*

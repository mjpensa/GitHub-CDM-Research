# Tom Healey ICMA CDM Showcase 2025

*Converted from: Tom-Healey_ICMA_CDM-Showcase-2025.pdf*

---

## Page 1

CDM Showcase 2025
DLT and tokenization in repo and collateral markets: how to 
leverage the CDM and smart contracts
26 February 2025
Tom Healey, ICMA Consultant

## Page 2

2
 Facilitate the implementation of priorities of the European Repo and Collateral
Council (ERCC) and Global Repo and Collateral Forum (GRCF) and digital
transformation of capital markets more broadly.
 ICMA aligned the CDM to fully support repo best practices and industry
standards across repo products and lifecycle events.
 On-going support for standards and interfaces between the CDM and other
industry message protocols (FIX, Swift, XML) and regulatory reporting (SFTR,
OFR).
 Facilitate use of the CDM for innovative technology solutions including
distributed ledger technologies.
ICMA CDM Priorities

## Page 3

3
Repo workflows and functionalities in the CDM
GC baskets & 
Collateral 
Eligibility
Settlement 
and Transfers 
using SWIFT*
SFTR and OFR 
Reporting*
Full Repo 
Lifecycle 
Events
Web3 
Extensions*
Fixed, Float, 
Term, Open,
Evergreen, 
Extendible
Best Practices
FIX to CDM 
Mapping*
Repo 
Extensions for 
APIs
*Development and POC

## Page 4

4
 Repo Extensions
• Many get/set functions to build repo products and execute lifecycle events
• https://github.com/tomhealey-icma/repo-cdm-extension-func
 Repo Pair-off Extension
• Repo Pair-off instruction and validation
• https://github.com/tomhealey-icma/repo-cdm-pairoff-extension
 Repo Demo App
• Repo Trading App
• https://github.com/tomhealey-icma/cdm-repo-demo-app
 SFTR/OFR Extensions
• Extension and mapping CDM to OFR
• https://github.com/tomhealey-icma/repo-sftr-extensions
• https://github.com/tomhealey-icma/repo-ofr-extensions
 Repo GC Basket Builder
• Created GC basket using CDM
• https://github.com/tomhealey-icma/cdm-gc-basket-builder
CDM Repo Extensions and Demos

## Page 5

5
Repo and collateral in a DLT environment

## Page 6

6
Repo and tokenization – Recent developments
 ICMA’s GMRA Digital Assets Annex, published in August 2024, provides a standardised framework and set
of terms which can be used to document repo transactions involving digital cash, digital securities
(including tokenised traditional securities), or asset-backed digital assets.
 Recent repo transactions and announcements involving DLT-based securities and/or digital forms of cash 
include:
 Santander and JPMorgan programmable intraday repo transaction, January 2025
 Société Générale Forge and Banque de France repo transaction on a public blockchain, December 
2024
 Eurosystem trials and experiments facilitating the settlement of DLT-based transactions including 
repo in central bank money (May-November 2024)
 ABN AMRO executed four repo pilot trades, November 2024
 HQLAx, Goldman Sachs, Clearstream and Eurex Repo, November 2024
 UBS, SBI and DBS completed world’s first cross-border repo with a natively-issued digital bond fully 
executed and settled on a public blockchain, November 2023
Note: See further examples and information on ICMA’s New FinTech applications in bond markets webpage. This overview is provided by ICMA for information 
purposes only. ICMA does not endorse any of those firms or solutions listed.

## Page 7

7
The CDM fills an important gap in DLT environments
Industry Benefit DLT Capability CDM DLT Support
Reduced 
Intermediation
Standardized Event 
Processing
Greater Fungibility
Decentralization 
eliminates 
intermediaries 
DLT smart contracts 
depend on external 
event triggers
Tokens do not depend 
on location and time 
zones
CDM generates 
stateless, standardized 
events
Predefined and 
standardized lifecycle 
events
CDM standardizes 
product representations 
in a digital form

## Page 8

8
Demo Framework for integration of CDM and DLT
CDM Event 
Instructions
Execution
Termination
Roll
Rerate
Reprice/Adjust
Substitution
Shape/Pair-off
Partial Delivery
CDM Primitive 
Events
Tokenize Assets
DLT Actions
Transfer Assets
Authorizations
Compliance
Off-chain Access
Increase/Decrease
Execution
Contract Formation
Terms Change
Transfer
Reset
Quantity Change
Web3 Interface Off-chain Services
Reference Data
Asset Lockup
Reporting
Pricing/Valuation
Off-chain transfers
Serialization/Hash 
Business Event
Token Constructors
DLT Events
Off-Chain Event 
Storage
Custody

## Page 9

9
CDM demo of recording a repo transaction and 
transferring cash and collateral in a DLT environment

## Page 10

10
Repo DLT Demo using smart contracts and the CDM
CDM:
Execution and 
Contract 
Formation
Custodian 
Collateral Service
Cash Transfer 
Service
Off-chain Collateral 
Lockup
Off-chain Cash 
Lockup
CDM:
TransferEvent
1. CDM Event to create 
contractFormation
2. Call to Repo 
smartcontract to create 
repo transaction
3. Tokenize collateral and 
lockup
4. Tokenize cash and 
lockup
CDM Events On-chain smart contracts Off-chain access contracts
5. CDM event to create 
transfer instructions
6. CDM collateral 
transfer
7. CDM cash transfer
RepoTrade
SmartContract:
Collateral Token 
Smart Contract
CashToken Smart 
Contract
Execution and Contract Formation Purchase and Repurchase Settlement

## Page 11

11

## Page 12

12
ICMA contacts:
Gabriel Callsen, Senior Director
gabriel.callsen@icmagroup.org
+44 (0)20 7213 0334
Tom Healey, Consultant
tom.healey@icmagroup.org
Contacts & Resources
Useful links:
FinTech Overview
FINOS CDM GitHub repository
ICMA’s CDM webpage
ICMA CDM Demo – Automating repo 
transactions (April 2023)
Bond Data Taxonomy
DLT Bonds Working Group
FinTech newsletter
Podcasts
This presentation is provided for information purposes only and should not be relied upon as legal, financial, or other professional advice. While the 
information contained herein is taken from sources believed to be reliable, ICMA does not represent or warrant that it is accurate or complete and 
neither ICMA nor its employees shall have any liability arising from or relating to the use of this publication or its contents.
© International Capital Market Association (ICMA), Zurich, 2025. All rights reserved. No part of this publication may be reproduced or transmitted in 
any form or by any means without permission from ICMA.

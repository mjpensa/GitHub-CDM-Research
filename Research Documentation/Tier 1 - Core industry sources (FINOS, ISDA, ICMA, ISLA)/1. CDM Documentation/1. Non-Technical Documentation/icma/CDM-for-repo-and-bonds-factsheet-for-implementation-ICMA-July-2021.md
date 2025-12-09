# CDM for repo and bonds factsheet for implementation ICMA July 2021

*Converted from: CDM-for-repo-and-bonds-factsheet-for-implementation-ICMA-July-2021.pdf*

---

## Page 1

CDM Factsheet for 
Implementation
What is the CDM?
The Common Domain Model (CDM) is a standardised, machine-readable and machine-executable blueprint for how 
financial products are traded and managed across the transaction lifecycle. The product scope of the CDM includes OTC 
derivatives, cash securities, securities financing, and commodities.
A single, digital processing standard for trade events and actions enhances financial markets’ operational efficiency in 
several ways.
The CDM components
There are three sets of CDM components, as laid-out in the CDM components diagram below:
• The Rosetta DSL
• The ISDA CDM Distribution
• CDM Application
CDM Components Diagram
June 2021

## Page 2

The Rosetta DSL
The Rosetta DSL is the infrastructure component of the CDM. The CDM is a domain model written in a Domain-Specific 
Language (DSL) called Rosetta, comprising a syntax (or grammar) and code generators.
To enable adoption and implementation of the CDM by the community of industry participants, the Rosetta DSL and 
its default code generator (Java) are open source under an Apache 2.0 licence. Further code generators are also open 
source under an Apache 2.0 license, allowing industry participants to write and share code generators for any other 
language.
The Rosetta DSL documentation explains the Rosetta DSL, describes the mechanism to write and use code 
generators, and details all the modelling components available in the Rosetta syntax and their purpose, with examples 
drawn from the CDM.
CDM adoption
The CDM for repo and bonds logical model is used to generate a Java implementation containing the types and 
enumerations expressed in Rosetta, so that IT systems can natively take advantage of the collective understanding of the 
product model. The functions defined in Rosetta are also available as executable code so that common processes (e.g. 
repo execution, clearing, settlement etc.) are ready to use without implementing any business logic.
The CDM contains translation dictionaries that provide a model to model mapping between FIX 4.4 and the CDM. The 
Rosetta Translate execution engine uses these mappings to convert a data document from FIX format to CDM JSON 
format, and is freely available as a user interface and as a programmatic API.
The CDM Distribution
• The CDM distribution is openly accessible to all industry participants and can be downloaded using Rosetta. The CDM 
is distributed subject to the CDM open source licence.
• Information on how to access the CDM Java distribution can be found here: CDM Java Distribution Guidelines
ICMA contacts
Gabriel Callsen, Director
gabriel.callsen@icmagroup.org
Rowan Varrall, Associate
rowan.varrall@icmagroup.org
© International Capital Market Association 2021. This publication is provided for information purposes only and should not be relied upon as legal, financial, or other 
professional advice. While the information contained herein is taken from sources believed to be reliable, ICMA does not represent or warrant that it is accurate or complete 
and neither ICMA nor its employees shall have any liability arising from or relating to the use of this publication or its contents.
July 2021

# Stephanie Rubizhevsky Novatus Global CDM Showcase 2025

*Converted from: Stephanie-Rubizhevsky_Novatus-Global_CDM-Showcase-2025.pdf*

---

## Page 1

© 2025 | Novatus Global Strictly Private and Confidential | 1
Prepared for: CDM Showcase
CDM & DRR Reconciliations 
Powered by En:ACT
February 2025

## Page 2

© 2025 | Novatus Global Strictly Private and Confidential | 2
Executive Summary

## Page 3

© 2025 | Novatus Global Strictly Private and Confidential | 3
Executive Summary
Novatus Global’s Approach to creating this POC:
Identify a shortlist of products and jurisdictions, including EU-EMIR reportable FX Fwds and FX NDOs.
Recreate the typical use case of a source system Data Lake and map those values to the CDM.
Using CDM & DRR to 
Enhance Full Reconciliations
Key Objectives Our Approach 
• Provide a technology solution highlighting 
discrepancies in a user’s reporting against 
the DRR industry-agreed interpretations.
• Demonstrate that CDM can be effectively 
implemented using a Data Lake as the 
input.
• Providing transparency in mappings and 
breaks, making it easier to understand the 
value of the CDM & DRR initiatives.
1
2
Use Case, Key Objectives, and Approach
Prepare Data Lineage reports allowing for detailed review of a client’s mapping from source to outbound 
compared to the CDM & DRR derived values. 4
Process these samples using the Rosetta.io platform to create Trade State Report outputs to be reconciled 
against En:ACT modelled outputs. 3
• Comprehensive field-by-field Reconciliation from source data to Trade Repository data using the En:ACT platform 
allows users to have their reporting workflows independently reviewed by the Novatus team and results can easily be 
reviewed by users to understand reporting gaps.
• The combination of the CDM and DRR models enables data to be processed according to community-agreed best 
practices and can be regularly updated to keep up with new requirements to each jurisdiction.
• Integrating the CDM and DRR models into the En:ACT platform gives potential adopters of the technologies an 
opportunity to understand the benefits. Further it can provide these same users with detailed mapping breakdowns via 
the Data Lineage tab, to ensure a smooth implementation of mapping updates.

## Page 4

© 2025 | Novatus Global Strictly Private and Confidential | 4
En:ACT Platform

## Page 5

© 2025 | Novatus Global Strictly Private and Confidential | 5
B: When the toggle is green, the 
percentage of Novatus tests 
passed. When the toggle is blue, 
the number of trades that show zero 
exceptions.
Summary View Highlights
C: The number of TSR/TAR records 
tested.
B C
E
C: A count of exceptions between 
TSR data and the values derived by 
Novatus using the CDM and DRR 
transformations.
E: Total exceptions by type being 
Accuracy, Completeness, and 
Timeliness
A
A:These boxes allow the user to 
specify the month(s) and asset 
class(es) to view in the platform.
D

## Page 6

© 2025 | Novatus Global Strictly Private and Confidential | 6
C: Custom field selection allows 
users to pull up additional 
reconciliation fields for comparison.
D: The detailed breakdown shows 
the TR reported value (RPT) 
against the Novatus derived value 
(EXP).
B: This trend line shows the 
number of reconciliation exceptions 
for a given field over time.
Field-Level Reconciliation View Highlights
A B
C
D
A: A count by field name of the 
discrepancies between TR value 
and Novatus outputs.

## Page 7

© 2025 | Novatus Global Strictly Private and Confidential | 7
CDM Technical 
Implementation

## Page 8

© 2025 | Novatus Global Strictly Private and Confidential | 8
Key features of En:ACT CDM Implementation:
• Client Data Lake: Represents the common format for firms that aggregate 
several OMS platforms into a harmonized file.
• Novatus Data Model: The client Data Lake is mapped to the Novatus data 
model through a series of custom transformations.
• DRR Processor: The DRR processor maps the Novatus data model to a 
CDM/DRR JSON representation to allow it to be ingested into the Rosetta 
platform through API call.
• Rosetta Platform: Runs transaction ingestion and regime reporting functionality 
through API post requests to the Rosetta platform.
• Expected Output: Output from the DRR processor are concatenated and 
aligned with the initial mappings to the Novatus data model.
• Reconciliation Pipeline: The reconciliation process compares the expected 
output with reported data to analyze discrepancies between what DRR expects 
to be reported to the regulator and what has actually been reported.
• En:ACT Visualisation: Results from the reconciliation process are published on 
the En:ACT platform where they are visualised for client analysis.
En:ACT Platform
Rosetta Platform
Client Data Inputs

## Page 9

© 2025 | Novatus Global Strictly Private and Confidential | 9
Field-Level Reconciliations 
Using DRR

## Page 10

01
02
03
© 2025 | Novatus Global Strictly Private and Confidential | 10
Visualizing DRR on En:ACT
The Reconciliation View displays all the breaks 
in data organized by the Regime Field Name.
B C
A
A
B
C
The values under the Field Name column with 
the suffix 'RPT' represent those submitted to 
the relevant TR
The values under the Field Name column with 
the Suffix EXP represent the values that were 
derived using the CDM and DRR.

## Page 11

© 2025 | Novatus Global Strictly Private and Confidential | 11
Demo Video

## Page 12

© 2025 | Novatus Global Strictly Private and Confidential | 12

## Page 13

© 2025 | Novatus Global Strictly Private and Confidential | 13
1. En:ACT is a viable technology solution to highlight 
discrepancies in a user’s reporting against the DRR 
industry-agreed interpretations.
2. CDM can be effectively implemented using a Data Lake as 
the input and Python as the programming language.
3. En:ACT’s Data Lineage for mappings and breaks makes it 
easy to understand the value of the CDM & DRR initiatives.
Conclusions

## Page 14

Contact Us
London
60-62 Margaret Street 
LondonW1W8TF
info@novatus.global
(+44) 020 3405 9207
Sydney
Level 3,478 George Street
Sydney NSW2000
info@novatus.global
(+44)0000 000 000
Novatus Global Ltd accepts no liability for any loss occasioned to any person 
acting or refraining from action as a result of any material in this publication.
Novatus Global Ltd is a limited company registered in England and Wales with 
a registered number 11910864 and its registered office at 60-62 Margaret 
Street, London, W1W 8TF.
© 2025 Novatus Global Ltd. | All rights reserved.
© 2025 | Novatus Global Strictly Private and Confidential | 14

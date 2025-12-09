# cftc technical specification v3.2 mar 2023

*Converted from: cftc-technical-specification-v3.2-mar-2023.pdf*

---

## Page 1

CFTC Technical Specification 
Parts 43 and 45 swap data reporting and public dissemination requirements 
March 1, 2023 
Version 3.2 
The Parts 43/45 Technical Specification changes (provided in redline form) must be implemented no later than January 29, 2024. 
i

## Page 2

DOCUMENT HISTORY 
Revisions 
Date Version Description Author 
2/20/2020 1.2 Draft for Public Comment DOD 
9/17/2020 2.0 First Publication per 2020 amended rule DOD 
9/30/2021 3.0 Second Publication with revisions DOD 
8/30/2022 3.1 Limited modifications to Version 3.0 DOD 
3/1/2023 3.2 Adoption of Unique Product Identifier DOD 
ii

## Page 3

TABLE OF CONTENTS 
1 INTRODUCTION................................................................................................................................................................................................VII 
1.1 BACKGROUND................................................................................................................................................................................................................. VII 
1.2 STRUCTURE AND DESCRIPTION OF COLUMN HEADINGS.......................................................................................................................................................... VIII 
1.3 EXPLANATION OF DATA ELEMENT OR CATEGORY .................................................................................................................................................................... XI 
1.4 UNIQUE PRODUCT IDENTIFIER (UPI) .................................................................................................................................................................................. XIII 
2 TECHNICAL SPECIFICATION AND VALIDATION RULES ......................................................................................................................................... 1 
3 APPENDIX......................................................................................................................................................................................................... 38 
A. ADDITIONAL DATA ELEMENTS PUBLICLY DISSEMINATED - REQUIREMENTS FOR SDRS ONLY............................................................................................................. 38 
B. NOTIONAL AMOUNT ....................................................................................................................................................................................................... 39 
C. MAPPING OF DAY COUNT CONVENTION ALLOWABLE VALUES TO ISO 20022, FPML, AND FIX/FIXML VALUES................................................................................ 40 
D. VALUATION METHOD ...................................................................................................................................................................................................... 48 
E. COLLATERALISATION CATEGORY......................................................................................................................................................................................... 49 
F. EVENTS: VALID ACTION TYPE AND EVENT TYPE COMBINATIONS FOR PART 43 AND PART 45 REPORTING........................................................................................... 50 
4 REFERENCES ..................................................................................................................................................................................................... 61 
This Technical Specification document provides technical specifications for reporting swap data to Swap Data Repositories (SDRs) under parts 43 and 45. 
iii

## Page 4

Index of Data Elements 
A
Action type ......................................................................................................................................................................................8 
Affiliated counterparty for margin and capital indicator.................................................................................................................33 
Allocation indicator........................................................................................................................................................................27 
Amendment indicator ....................................................................................................................................................................10 
B
Block trade election indicator ........................................................................................................................................................27 
Buyer identifier ................................................................................................................................................................................6 
C
Call amount...................................................................................................................................................................................12 
Call currency .................................................................................................................................................................................12 
CDS index attachment point .........................................................................................................................................................25 
CDS index detachment point ........................................................................................................................................................25 
Central counterparty .......................................................................................................................................................................1 
Cleared............................................................................................................................................................................................1 
Clearing account origin ...................................................................................................................................................................1 
Clearing member ............................................................................................................................................................................1 
Clearing receipt timestamp .............................................................................................................................................................3 
Clearing swap USIs ........................................................................................................................................................................2 
Clearing swap UTIs.........................................................................................................................................................................2 
Collateralisation category..............................................................................................................................................................33 
Counterparty 1 (reporting counterparty)..........................................................................................................................................4 
Counterparty 1 financial entity indicator..........................................................................................................................................5 
Counterparty 2 ................................................................................................................................................................................5 
Counterparty 2 financial entity indicator..........................................................................................................................................5 
Counterparty 2 identifier source......................................................................................................................................................5 
Currency of initial margin collected...............................................................................................................................................36 
Currency of initial margin posted ..................................................................................................................................................34 
Currency of variation margin collected..........................................................................................................................................37 
Currency of variation margin posted.............................................................................................................................................37 
Custom basket indicator .................................................................................................................................................................8 
D
Day count convention ...................................................................................................................................................................16 
Delta..............................................................................................................................................................................................31 
Dissemination identifier.................................................................................................................................................................38 
Dissemination timestamp .............................................................................................................................................................38 
E
Effective date................................................................................................................................................................................27 
Embedded option type .................................................................................................................................................................26 
Event identifier..............................................................................................................................................................................10 
Event timestamp...........................................................................................................................................................................11 
Event type.......................................................................................................................................................................................9 
Exchange rate ..............................................................................................................................................................................20 
Exchange rate basis.....................................................................................................................................................................20 
Execution timestamp ....................................................................................................................................................................28 
Expiration date..............................................................................................................................................................................28 
F
Final contractual settlement date .................................................................................................................................................26 
First exercise date .................................................................................................................................................................xiii, 25
Fixed rate......................................................................................................................................................................................20 
Fixing date....................................................................................................................................................................................17 
Floating rate reset frequency period.............................................................................................................................................17 
Floating rate reset frequency period multiplier .............................................................................................................................17 
I
Index factor...................................................................................................................................................................................26 
Initial margin collateral portfolio code...........................................................................................................................................33 
Initial margin collected by the reporting counterparty (post-haircut) ............................................................................................ 35 
Initial margin collected by the reporting counterparty (pre-haircut).............................................................................................. 35 
Initial margin posted by the reporting counterparty (post-haircut)................................................................................................ 33 
Initial margin posted by the reporting counterparty (pre-haircut) .................................................................................................34 
J
Jurisdiction....................................................................................................................................................................................30 
L
Last floating reference reset date.................................................................................................................................................31 
Last floating reference value ........................................................................................................................................................31 
iv

## Page 5

N
New SDR identifier........................................................................................................................................................................31 
Next floating reference reset date.................................................................................................................................................31 
Non-standardized term indicator...................................................................................................................................................27 
Notional amount............................................................................................................................................................................11 
Notional amount schedule - notional amount in effect on associated effective date....................................................................11 
Notional amount schedule - unadjusted effective date of the notional amount ............................................................................12 
Notional amount schedule - unadjusted end date of the notional amount....................................................................................12 
Notional currency ..........................................................................................................................................................................11 
Notional quantity ...........................................................................................................................................................................13 
O
Option premium amount ...............................................................................................................................................................24 
Option premium currency..............................................................................................................................................................25 
Option premium payment date......................................................................................................................................................25 
Original dissemination identifier....................................................................................................................................................38 
Original swap SDR identifier...........................................................................................................................................................3 
Original swap USI ...........................................................................................................................................................................3 
Original swap UTI ...........................................................................................................................................................................3 
Other clearing exemptions - Counterparty 1...................................................................................................................................4 
Other clearing exemptions – Counterparty 2 ..................................................................................................................................4 
Other payment amount .................................................................................................................................................................18 
Other payment currency ...............................................................................................................................................................18 
Other payment date ......................................................................................................................................................................18 
Other payment payer ....................................................................................................................................................................19 
Other payment receiver ................................................................................................................................................................19 
Other payment type ......................................................................................................................................................................18 
P
Package identifier .........................................................................................................................................................................14 
Package indicator .........................................................................................................................................................................14 
Package transaction price.............................................................................................................................................................15 
Package transaction price currency..............................................................................................................................................15 
Package transaction price notation...............................................................................................................................................15 
Package transaction spread .........................................................................................................................................................15 
Package transaction spread currency ..........................................................................................................................................16 
Package transaction spread notation ...........................................................................................................................................16 
Payer identifier ................................................................................................................................................................................6 
Payment frequency period ............................................................................................................................................................19 
Payment frequency period multiplier.............................................................................................................................................20 
Platform identifier ..........................................................................................................................................................................29 
Portfolio containing non-reportable component indicator .............................................................................................................33 
Post-priced swap indicator............................................................................................................................................................21 
Price..............................................................................................................................................................................................21 
Price currency ...............................................................................................................................................................................22 
Price notation ................................................................................................................................................................................22 
Price unit of measure ...................................................................................................................................................................22 
Prime brokerage transaction indicator..........................................................................................................................................29 
Prior USI (for one-to-one and one-to-many relations between transactions)............................................................................... 29 
Prior UTI (for one-to-one and one-to-many relations between transactions)............................................................................... 29 
Put amount ...................................................................................................................................................................................13 
Put currency .................................................................................................................................................................................13 
Q
Quantity frequency .......................................................................................................................................................................13 
Quantity frequency multiplier........................................................................................................................................................13 
Quantity unit of measure ..............................................................................................................................................................14 
R
Receiver identifier...........................................................................................................................................................................7 
Reporting timestamp ....................................................................................................................................................................28 
S
Seller identifier................................................................................................................................................................................6 
Settlement currency .....................................................................................................................................................................26 
Settlement location.......................................................................................................................................................................27 
Spread ..........................................................................................................................................................................................23 
Spread currency ...........................................................................................................................................................................23 
Spread notation ............................................................................................................................................................................24 
Strike price....................................................................................................................................................................................24 
Strike price currency/currency pair...............................................................................................................................................24 
Strike price notation......................................................................................................................................................................24 
Submitter identifier .........................................................................................................................................................................7 
T
Total notional quantity ..................................................................................................................................................................14 
U
Unique product identifier (UPI) .....................................................................................................................................................26 
Unique Product Identifier FISN.....................................................................................................................................................38 
Unique Product Identifier underlier name.....................................................................................................................................38 
Unique Swap Identifier (USI)........................................................................................................................................................30 
Unique Transaction Identifier (UTI) ..............................................................................................................................................30 
v

## Page 6

Valuation method .........................................................................................................................................................................32 V Valuation timestamp.....................................................................................................................................................................32 
Variation margin collateral portfolio code .....................................................................................................................................36 
Valuation amount ..........................................................................................................................................................................32 Variation margin collected by the reporting counterparty (pre-haircut) ........................................................................................ 37
Valuation currency ........................................................................................................................................................................32 Variation margin posted by the reporting counterparty (pre-haircut) ........................................................................................... 36 
vi

## Page 7

1 Introduction 
1.1 Background 
Under the Dodd-Frank Wall Street Reform and Consumer Protection Act, the CFTC passed several data-related swaps rules, including 17 CFR parts 43 and 45, which mandated the reporting of 
swap data contracts to SDRs and the public dissemination of swap data, with the goal of bringing transparency to a previously opaque swaps market. 
Internationally, in 2009 the G20 leaders agreed that all over-the-counter (OTC) derivatives contracts should be reported to trade repositories (TRs)1 to further the goals of improving transparency, 
mitigating systemic risk and preventing market abuse. Aggregation of the data being reported across TRs would help authorities to obtain a comprehensive view of the OTC derivatives market and 
its activity. In September 2014, the Financial Stability Board (FSB) published the Aggregation Feasibility Study Group (AFSG) report, endorsing certain recommendations relating to the aggregation 
of TR data, including developing global guidance on harmonization of data elements that are reported to TRs and are important to global aggregation across jurisdictions. The CPMI-IOSCO 
working group for harmonization of critical OTC derivatives data elements was set up to implement some of the key recommendations of the 2014 FSB AFSG report and has developed global 
guidance regarding the definition, format and usage of critical OTC derivatives data elements reported to TRs, including the unique transaction identifier (UTI), the unique product identifier (UPI) 
and other critical data elements (also known as CDE). 
The CFTC’s Technical Specification uses the Revised CDE Technical Guidance - version 2: Harmonisation of critical OTC derivatives data elements (other than UTI and UPI)2 (referred to as CDE 
Technical Guidance), as its base, with a majority of the data elements sourced from this CDE Technical Guidance. 
This Technical Specification provides the definition, format, allowable values and validation rules for the data elements that are required to be reported to the SDRs by reporting parties under the 
revised part 45 rule. For data elements in the CDE Technical Guidance (“CDE data elements”) adopted by the CFTC (the data element name, definition, format, and allowable values), the CFTC has 
taken them on as written/prescribed by CDE. Where additional guidance is needed for CFTC reporting requirements, that guidance is provided in a footnote for that data element. This Technical 
Specification also provides the data elements required to be reported and publicly disseminated under the part 43 rule, and any dissemination requirements for SDRs for public reporting. 
Please forward questions regarding format, content, and transmission of part 43 and part 45 data submissions to CFTC at CFTCSwapsTechSpec@CFTC.gov. 
1 Throughout this Technical Specification, references to “trade repositories” in CDE data element should be read to mean SDRs. 2 See Revised CDE Technical Guidance – version 2 - Harmonisation of critical OTC derivative data elements (other than UTI and UPI), September 2021, https://www.leiroc.org/publications/gls/roc_20210922.pdf 
vii

## Page 8

1.2 Structure and Description of Column Headings 
The Technical Specification and Validation Rules table starting on page 1 contains two main areas: Technical Specification and Validation Rules and Dissemination Rules. The details of these 
main areas are described in this section below. 
1.2.1 Technical Specification 
(1) 
# 
(2) 
Source 
(3) 
Category 
Technical Specification 
(4) 
Data Element 
Name 
(5) 
Definition for Data 
Element 
(6) 
Format 
(7) 
Allowable 
Values 
(8) Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation 
Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation and 
Dissemination 
Rules 
CR
IR
FX
EQ
CO 
(1) #: all data elements are assigned a number for ease of reference. The data element number is referenced throughout the document and in the part 43 and part 45 rule appendices. 
(2) Source: this column will contain either “CDE” or “CFTC”. “CDE” refers to a data element in the published CDE Technical Guidance. “CFTC” refers to a data element not in the 
published CDE Technical Guidance and sourced from the CFTC. 
(3) Category: data elements are grouped by topic or category. 
(4) Data Element Name: data element names used in this document may be, but are not required to be used literally. 
(5) Definition for Data Element: for CDE data elements, the definition is sourced from the CDE Technical Guidance, with footnotes added to provide clarity based on the CFTC’s 
jurisdictional requirements. 
(6) Format: see Table 1 below that illustrates the meaning of formats used throughout the Technical Specification. 
Format Content in brief Additional Explanation Example(s) 
YYYY-MM-DD Date YYYY = four-digit year 
MM = two-digit month 
DD = two-digit day 
2015-07-06 
(corresponds to 6 July 2015) 
YYYY-MM￾DDThh:mm:ssZ 
Date and time YYYY, MM, DD as above 
hh = two-digit hour (00 through 23) (am/pm NOT allowed) 
mm = two-digit minute (00 through 59) 
ss = two-digit second (00 through 59) 
T is fixed and indicates the beginning of the time element. 
Z is fixed and indicates that times are expressed in UTC 
(Coordinated Universal Time) and not in local time. 
2014-11-05T13:15:30Z 
(corresponds to 5 November 
2014, 1:15:30 pm, Coordinated 
Universal time, or 5 November 
2014, 8:15:30 am US Eastern 
Standard Time) 
Num(25,5) Up to 25 numerical 
characters including up 
to five decimal places 
The length is not fixed but limited to 25 numerical characters 
including up to five numerical characters after the decimal 
point. 
Should the value have more than five digits after the decimal, 
reporting counterparties should round half-up. 
1352.67 
12345678901234567890.12345 
1234567890123456789012345 
0 
– 20000.25 
– 0.257 
viii

## Page 9

Num(5)3 Up to five numerical 
characters, no decimals 
are allowed 
The length is not fixed but limited to five numerical characters. 12345 
123 
20 
Char(3) Three alphanumeric 
characters 
The length is fixed at three alphanumeric characters. USD 
X1X 
999 
Varchar(25) Up to 25 alphanumeric 
characters 
The length is not fixed but limited at up to 25 alphanumerical 
characters. No special characters are permitted. If permitted, it 
would be explicitly stated in the format of the data element. 
asgaGEH3268EFdsagtTRCF543 
aaaaaaaaaa 
x 
Boolean Boolean characters Either “True” or “False” True 
False 
Table 1 – Explanation of formats used in the Technical Specification 
(7) Allowable Values: for each of the data elements, where applicable, only the specified allowable values are acceptable for submission to the SDRs. Any reported value that is not in 
the allowable values list should be rejected by the SDRs’ data validation procedures. If the allowable value specifies a predefined structure such as LEI4 code followed by an identifier 
(i.e., Natural person identifier), the SDR’s validation must also include a check to ensure the LEI code is published by the GLEIF. 
(8) Validation Rules and Dissemination Rules: see section 1.2.2 below. 
1.2.2 Validation Rules and Dissemination Rules 
This section explains the columns in (8) Validation Rules and Dissemination Rules. Nothing in this Technical Specification should be read to prohibit an SDR from limiting the number of data 
elements required to be submitted, to a subset of part 43 or 45 data elements, for Action Type TERM, PRTO, and EROR5. Submission of all parts 43 and 45 data elements is mandatory for all other 
Action Types. 
(8) Validation Rules and Dissemination Rules 
(8a) 
P43/P45 
Asset Class (8b) 
Part 45 SDR Validation 
Rules 
P45 End of Day (8c) 
P43 Reported (8d)
(8e) 
Part 43 SDR Validation and 
Dissemination Rules 
CR
IR
FX
EQ
CO 
(8a) P43/P45 Asset Class: These five columns specify which asset class each data element is required to be reported. The Technical Guidance, Harmonisation of the Unique Product 
Identifier6 (referred to as UPI Technical Guidance) refers to UPI reference data elements, including Asset Class, which is defined as an indication of “whether the asset, benchmark or 
3 Num(5) format is equivalent to Num(5,0) used in this Technical Specification and does not allow decimals. 4 Legal entity identifiers – refer to § 45.6 5 No updates to the term(s) of the trade may be made for action type TERM, PRTO, or EROR submissions. 
6 See Technical Guidance, Harmonisation of the Unique Product Identifier, September 2017, https://www.leiroc.org/publications/gls/roc_20170901.pdf 
ix

## Page 10

another derivatives contract underlying a derivatives contract is, or references, an equity, rate, credit, commodity or foreign exchange asset.” These columns are applicable to publicly 
disseminated transactions (part 43) and both transaction reporting and end-of-day reporting (part 45). 
For this Technical Specification, CR = credit, IR = rates, FX = foreign exchange, EQ = equities and CO = commodities. 
(8b) Part 45 SDR Validation Rules: In accordance with § 49.10(c), Duty to validate SDR data. This column specifies the validation rule(s) the SDRs must apply to each data element for 
transaction reporting, and end-of-day valuation and collateral reporting for all asset classes. The validation rules in this column are the minimum conditions that must be met. It is 
possible the data element may be reported for scenarios outside of what is listed in the validation rules column (for example, a value may be provided where there is an 
else {blank}. It may be interpreted as “else optional”). The validation rules may vary by asset class, transactions, and end-of-day submissions. For certain data elements, additional 
cross validation with other related data element(s) is also specified. For product-specific validation rules, see section 1.4 below. 
(8c) P45 End of Day: This column specifies the data elements that are required for end-of-day Collateral or Valuation reporting with a “Y” or “N”. 
(8d) P43 Reported: In accordance with part 43 rule, SDRs must publicly disseminate certain swap transaction and pricing data to enhance transparency and price discovery. This column 
indicates the data elements required to be reported to the SDR with a “Y”, and those not required to be reported with an “N”. 
(8e) Part 43 SDR Validation and Dissemination Rules: For the data elements that are required to be publicly disseminated, and in accordance with § 49.10, this column specifies 
validation rules that the SDR must perform and certain rules that must be applied by the SDR when disseminating to the public. The SDR disseminating the data, per their own 
procedures, must round and cap the reported notional or principal amount pursuant to § 43.4. When notional or principal amount is capped, the SDR must proportionally scale other 
applicable fields that are disseminated to avoid fingerprinting and distortion. 
In order to increase consistency in reporting and improve the quality of swap data maintained at SDRs, a set of validation rules have been prescribed for each data element for all swap reporting. 
The SDRs are required to apply these validations as part of SDR’s acceptance of data pursuant to § 49.10(c) – Duty to validate SDR Data. Each data element is prescribed with Mandatory, 
Conditionally mandatory, Optional, and Not required along with validation rules. Below Table 2 provides definitions for each validation code. 
Value Definition 
M Mandatory: The data element is strictly required. Any additional validation rules must also 
be applied, if specified. 
C 
Conditionally mandatory: The data element is required if the specific conditions set out in 
the validation rules are met. Any additional validation rules must also be applied, if 
specified. 
O Optional: The data element shall be reported if applicable for the transaction. Any 
additional validation rules specified may be applied, when populated. 
NR Not required: The data element is not required to be reported. 
Table 2 - Definitions of validations 
x

## Page 11

1.3 Explanation of Data Element or Category 
1.3.1 Direction 
The CDE Technical Guidance provides two options/approaches for reporting Direction.
7 The CFTC has adopted the Buyer/Seller and Payer/Receiver approach and not the Direction 1/Direction 2 
approach. The reporting counterparty should NOT report both Buyer/Seller and Receiver/Payer for a given transaction but instead adopt the appropriate data element(s) for the type of instrument 
reported. 
1.3.2 Notional amount schedules 
For the Notional amount schedule related data elements (#33 - #35), the reporting counterparty must adhere to the implementation procedures established by the SDR. 
1.3.3 Repeating data elements or leg-based products 
Depending on the product being reported or market convention, a multi-leg or multi-stream product could report a particular data element more than once. An example is Notional amount (#31) 
which could be reported as Notional amount–leg 1 and Notional amount–leg 2 by the submitter depending on the applicability to the product. Unless the data element is listed as “Leg,” it cannot 
be reported more than once with the exception of ‘Other payments’ related data elements (Refer to Section 1.3.6). Generally speaking the validations included in the Technical Specification for leg￾based data elements are meant to apply to the first leg (Leg 1). It should not, however, be presumed the validations apply to the second leg (Leg 2) similarly. This is due in large part to the 
conditionality between leg fields and in light of the fact that SDR-specific data elements can alter the application of the published validations in ways not contemplated in the Technical 
Specification. Given this, SDRs may incorporate other validations for leg-level data elements, should they deem it necessary. For products where the multi-leg or multi-stream concept is not 
applicable, report values in the designated data element for the first leg (Leg 1) for all fields that are specified as leg-based data elements. 
1.3.4 Reporting multiple values 
Data elements that require reporting of multiple values in a single data element can be reported using a delimiter between the reported values. An example below uses a semi-colon for Clearing 
swap UTIs [#6] which requires multiple UTIs resulting from clearing. The choice of delimiter is left to the discretion of the SDR and the reporting counterparties must adhere to the implementation 
procedures established by the SDR to whom it reports. 
Data element Reported values Explanation 
Clearing swap UTI LCZ7XYGSLJUHFXXNXD88123456789; LCZ7XYGSLJUHFXXNXD880000000111 2 UTIs separated by ‘;’ and each reported value passes validation 
rules for format and allowable value of the data element 
Table 3 - Example showing how multiple values can be reported 
1.3.5 Events category 
Harmonization of data elements related to lifecycle events was not included in the CDE Technical Guidance but is required under CFTC swaps reporting. Reporting of swaps life cycle events is 
identified by the combination of the action taken (Action type [#26]) for a transaction and the reason (Event type [#27]) for the action. Related transactions are linked using unique identifiers; for 
example, Prior USI [#100] and Prior UTI [#101] are used for linking one-to-one and one-to-many relationship between transactions. Event identifier [#29] is also used for linking many-to-many 
relationship between transactions for specified situations. 
7 Refer to data element, Direction (2.13) in Revised CDE Technical Guidance – version 2: Harmonisation of critical OTC derivative data elements (other than UTI and UPI) –September 2021, 
https://www.leiroc.org/publications/gls/roc_20210922.pdf 
xi

## Page 12

Appendix F illustrates how different lifecycle events should be reported in transaction reporting and end-of-day (valuation and collateral) reporting with 15 examples showing how Action type and 
Event type combinations should be used to report various events. 
1.3.6 Payments category – Other payments 
A number of the data elements in the ‘Payment’ category (CDE data elements Other payment type [#57], Other payment amount [#58], Other payment currency [#59], Other payment date [#60], 
Other payment payer [#61], and Other payment receiver [#62]) capture some types of payments linked to the derivative transaction but that are not regular periodic payments. This set of data 
elements could be reported multiple times in the case of multiple payments. 
Unique 
transaction 
identifier (UTI) 
Other payment 
amount 1 
Other 
payment 
type 1 
Other 
payment 
currency 1 
Other 
payment 
date 1 
Other payment 
payer 1 
Other payment 
receiver 1 
Other payment 
amount 2 
Other 
payment 
type 2 
Other 
payment 
currency 2 
Other payment 
date 2 
Other payment 
payer 2 
Other payment 
receiver 2 
LEIRCP-1111 100 000 UWIN CCY 2019-03-01 LEI-COUNTERPTY1 LEI-COUNTERPTY2 50 000 PEXH CCY 2019-03-01 LEI-COUNTERPTY1 LEI-COUNTERPTY2 
Table 4 - Example showing how a set of data elements could be reported 
1.3.7 Offshore Currency 
There are multiple currency data elements in the Technical Specification that reference ISO 4217, but ISO 4217 does not include a method to report off-shore currency. The Settlement location 
(#90) data element helps differentiate the onshore currency from the offshore currency. For example, an FX swap transaction that involves an “offshore currency” such as Chinese Yuan (Renminbi) 
trading in offshore market (i.e., Hong Kong), the ISO 4217 currency code for Chinese Yuan Renminbi, CNY, is required to be reported along with Settlement location data element (see below). 
Notional currency Settlement location 
CNY HK 
Table 5 - Reporting offshore currency using Settlement location 
The offshore currency for CNY is often represented as ‘CNH’ in the marketplace, but it is not an official ISO currency code, so it should not be reported. 
xii

## Page 13

1.4 Unique Product Identifier (UPI)8 
The term “Unique product identifier” as used in this Technical Specification corresponds to the term “UPI code” in the UPI Technical Guidance9. 
1.4.1 Reporting to an SDR for the Credit, Rates, FX and Equities asset classes10 
For the Credit, Rates, FX and Equities asset classes, report the Unique Product Identifier (UPI) [#87]. 
1.4.2 Reporting to an SDR for the Commodities asset class 
For the Commodities asset class, report product-related data elements as specified by the relevant SDR until the Commission designates a UPI pursuant to § 45.7 for the Commodities asset class. 
1.4.3 Validation rules 
Product specific validation rules are based on the UPI reference data elements as provided by UPI service provider11 and defined in ISO 4914 Standard.
12 Until the Commission designates a UPI for 
the Commodities asset class, each SDR should implement the validation rules based on that SDR’s equivalent data element that it receives for that product attribute. 
These validation rules are specified for transaction, collateral, and valuation reporting in column (8b), Part 45 SDR Validation Rules. 
The convention used to reference UPI reference data elements in the validation rule is “UPI.[reference data element name]”. In the example below, it uses UPI reference data element, Instrument 
Type, from the ISO 4914 Standard to specify whether a transaction is an option transaction.
13 
Data element name Validation rule Explanation 
First exercise date C if UPI.[Instrument type] = ‘Option’, else 
{blank} 
‘First exercise date’ is conditionally required to be populated if the 
transaction is an option, otherwise, it can be blank. 
Table 6 - Example of product specific validation rule 
1.4.4 Public Dissemination 
For the Credit, Rates, FX, and Equities asset classes, SDRs will publicly disseminate the UPI along with the UPI Service Provider issued FISN [#D4] and UPI Underlier Name [#D5]. For the 
Commodities asset class, SDRs will continue to publicly disseminate the product-related data elements unique to each SDR until the Commission designates a UPI for the Commodities asset class. 
8 Refer to § 45.7 (Unique product identifiers) for more details. 9 See Technical Guidance, Harmonisation of the Unique Product Identifier, September 2017, https://www.leiroc.org/publications/gls/roc_20170901.pdf 10 Refer to the Commission order designating a unique product identifier for swaps in the Credit, Rates, FX and Equities asset classes. Order Designating the Unique Product Identifier and Product Classification 
System to be Used in Recordkeeping and Swap Data Reporting, 88 Fed. Reg. 11790 (Feb. 24, 2023). 11 UPI service provider is Derivatives Service Bureau (DSB) – https://www.anna-dsb.com/upi/ 12 ISO 4914 Unique product identifier (UPI) – https://www.iso.org/standard/80506.html 13 Allowable values assigned to UPI reference data elements will be determined by the UPI service provider although the actual values, while equivalent, may differ from the values that appear in this document. 
xiii

## Page 14

2 Technical Specification and Validation Rules 
Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
1 CDE Clearing Cleared Indicator of whether the transaction has been cleared, or is intended to be cleared, 
by a central counterparty14. 
Char(1) • Y = Yes, centrally cleared, for beta and 
gamma transactions.15 
• N = No, not centrally cleared. 
• I = Intent to clear, for alpha16 
transactions that are planned to be 
submitted to clearing. 
M M M M M Transaction 
M 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
2 CDE Clearing Central 
counterparty 
Identifier of the central counterparty (CCP) that cleared the transaction. 
This data element is not applicable if the value of the data element “Cleared” is “N” 
(“No, not centrally cleared”) or “I” (“Intent to clear”). 
Char(20) ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
C C C C C Transaction 
C if [Cleared] = ‘Y’, When 
populated, the value shall 
match the value in 
[Counterparty 1 (reporting 
counterparty)]; 
NR if [Cleared] = ‘N’; 
O if [Cleared] = ‘I’17 
Collateral 
NR 
Valuation 
NR 
N N 
3 CFTC Clearing Clearing account 
origin 
Indicator of whether the clearing member acted as principal for a house trade or an 
agent for a customer trade. 
Char(4) • HOUS = House 
• CLIE = Client 
C C C C C Transaction 
C if [Cleared] = ‘Y’; 
NR if [Cleared] = ‘N’ or ‘I’ 
Collateral 
NR 
Valuation 
NR 
N N 
4 CDE Clearing Clearing member Identifier of the clearing member through which a derivative transaction was 
cleared at a central counterparty. 
• Char(20), for an LEI 
code 
• Varchar(72), for 
natural persons who 
are acting as private 
individuals (not eligible 
• ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
• For natural persons who are acting as 
private individuals (not eligible for an LEI 
C C C C C Transaction 
C if [Cleared] = ‘Y’; 
NR if [Cleared] = ‘N’ or ‘I’ 
N N 
14 Throughout this Technical Specification, references to “central counterparty” in CDE data elements should be read to mean “derivatives clearing organizations” and “exempt derivatives clearing organizations.” 15 Throughout this Technical Specification, references to “beta and gamma transactions” in CDE data elements should be read to mean “clearing swaps.” 16 Throughout this Technical Specification, references to “alpha transactions” in CDE data elements should be read to mean “original swaps.” 17 For CFTC jurisdiction, this data element is optional when the value of the data element “Cleared” is “I” (“Intent to clear”) 
CFTC Technical Specification Version 3.2 1

## Page 15

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
This data element is applicable to cleared transactions under both the agency for an LEI per the per the ROC Statement – Individuals Collateral 
clearing model and the principal clearing model.18 ROC Statement - Acting in a Business Capacity): LEI of the NR 
• In the case of the principal clearing model, the clearing member is identified as 
clearing member and also as a counterparty in both transactions resulting from 
clearing: (i) in the transaction between the central counterparty and the clearing 
member; and (ii) in the transaction between the clearing member and the 
counterparty to the original alpha transaction. 
• In the case of the agency clearing model, the clearing member is identified as 
Individuals Acting in a 
Business Capacity19) 
and for Privacy Law 
Identifier (PLI). 
reporting counterparty followed by a 
unique identifier assigned and 
maintained consistently by the reporting 
counterparty for that natural person(s) for 
regulatory reporting purpose. 
• Privacy Law Identifier (PLI) 
Valuation 
NR 
clearing member but not as the counterparty to transactions resulting from clearing. 
Under this model, the counterparties are the central counterparty and the client. 
This data element is not applicable if the value of the data element “Cleared” is “N” 
(“No, not centrally cleared”) or “I” (“Intent to clear”). 
5 CFTC Clearing Clearing swap USIs The unique swap identifiers (USI) of each clearing swap that replaces the original 
swap that was submitted for clearing to the derivatives clearing organization, other 
than the USI for the swap currently being reported (as “USI” data element below). 
Varchar(42) Refer to: CFTC USI Data Standard20 
Up to 42 alphanumeric characters 
C C C C C Transaction 
C if ([Cleared] = ‘Y’ or 
([Cleared] = ‘I’ and [Action type] 
= ‘TERM’)) and [Event type] = 
‘CLRG’ and [Clearing swap 
UTIs] is not populated, else 
{blank}; 
NR if [Cleared] = ‘N’ 
Collateral 
NR 
Valuation 
NR 
N N 
6 CFTC Clearing Clearing swap UTIs The unique transaction identifiers (UTI) of each clearing swap that replaces the 
original swap that was submitted for clearing to the derivatives clearing 
organization, other than the UTI for the swap currently being reported (as “UTI” 
data element below). 
Varchar(52) ISO 23897 Unique transaction identifier 
Up to 52 alphanumeric characters 
C C C C C Transaction 
C if ([Cleared] = ‘Y’ or 
([Cleared] = ‘I’ and [Action type] 
= ‘TERM’)) and [Event type] = 
‘CLRG’ and [Clearing swap 
USIs] is not populated, else 
{blank}; 
NR if [Cleared] = ‘‘N’ 
Collateral 
NR 
Valuation 
NR 
N N 
18 Reporting counterparties should report “clearing swaps” according to the agency clearing model. 19 ROC Statement – Individuals Acting in a Business Capacity, ROC Statement - Individuals Acting in a Business Capacity 20 Throughout this Technical Specification, references to “CFTC USI Data Standard” should refer to the Unique Swap Identifier (USI) Data Standard, 
https://www.cftc.gov/sites/default/files/idc/groups/public/@swaps/documents/dfsubmission/usidatastandards100112.pdf 
CFTC Technical Specification Version 3.2 2

## Page 16

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
7 CFTC Clearing Original swap USI The unique swap identifier (USI) of the original swap21 submitted for clearing to the 
derivatives clearing organization that is replaced by clearing swaps. 
Varchar(42) Refer to CFTC USI Data Standard 
Up to 42 alphanumeric characters 
C C C C C Transaction 
C if ([Cleared] = ‘Y’ and [Action 
type] = ‘NEWT’ and [Event 
type] = ‘CLRG’) and [Original 
Swap UTI] is not populated, 
else {blank}; 
NR if [Cleared] = ‘N’ or ‘I’ 
Collateral 
NR 
Valuation 
NR 
N N 
8 CFTC Clearing Original swap UTI The unique transaction identifier (UTI) of the original swap22 submitted for clearing 
to the derivatives clearing organization that is replaced by clearing swaps. 
Varchar(52) ISO 23897 Unique transaction identifier 
Up to 52 alphanumeric characters 
C C C C C Transaction 
C if ([Cleared] = ‘Y’ and [Action 
type] = ‘NEWT’ and [Event 
type] = ‘CLRG’) and [Original 
Swap USI] is not populated, 
else {blank}; 
NR if [Cleared] = ‘N’ or ‘I’ 
Collateral 
NR 
Valuation 
NR 
N N 
9 CFTC Clearing Original swap SDR 
identifier 
Identifier of the swap data repository (SDR) to which the original swap was 
reported23. 
Char(20) ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
C C C C C Transaction 
C if ([Cleared] = ‘Y’ or 
([Cleared] = ‘I’ [Action type] = 
‘TERM’)) and [Event type] = 
‘CLRG’, else {blank}; 
NR if [Cleared] = ‘N’ 
Collateral 
NR 
Valuation 
NR 
N N 
10 CFTC Clearing Clearing receipt 
timestamp 
The date and time, expressed in UTC, the original swap was received by the 
derivatives clearing organization (DCO) for clearing and recorded by the DCO’s 
system. 
YYYY-MM￾DDThh:mm:ssZ, 
based on UTC. 
Any valid date/time based on ISO 8601 
Date and time format. 
C C C C C Transaction 
C if ([Cleared] = ‘Y’ or 
([Cleared] = ‘I’ and [Action type] 
= ‘TERM’)) and [Event type] = 
'CLRG', else {blank}; 
N N 
21 For transactions where no original swap USI is available or not provided, a value of “NOTAVAILABLE” can be used. 22 For transactions where no original swap UTI is available or not provided, a value of “NOTAVAILABLE” can be used. 23 For transactions where no original swap SDR identifier is available or not provided, a value of “NOTAVAILABLE” can be used. 
CFTC Technical Specification Version 3.2 3

## Page 17

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
NR if [Cleared] = ‘N’ 
Collateral 
NR 
Valuation 
NR 
11 CFTC Clearing Clearing exceptions 
and exemptions -
Counterparty 1 
Identifies the type of clearing exception or exemption that the Counterparty 1 has 
elected. 
All applicable exceptions and exemptions must be selected. 
The values may be repeated as applicable. 
Char(4) • ENDU = End-user exception, § 50.50 
• AFFL = Inter-affiliate exemption, § 
50.52 
• SMBK = Small bank exemption, § 
50.50(d) 
• COOP = Cooperative exemption, § 
50.51 
• NOAL = No-action Letter 
• OTHR = Other exceptions or 
exemptions, not including no-action letter 
relief 
O O O O O Transaction 
O if [Cleared] = ‘N’; 
NR if [Cleared] = ‘Y’ or ‘I’ 
Collateral 
NR 
Valuation 
NR 
N N 
12 CFTC Clearing Clearing exceptions 
and exemptions – 
Counterparty 2 
Identifies the type of the clearing exception or exemption that the Counterparty 2 
has elected. 
All applicable exceptions and exemptions must be selected. 
The values may be repeated as applicable. 
Char(4) • ENDU = End-user exception, § 50.50 
• AFFL = Inter-affiliate exemption, § 
50.52 
• SMBK = Small bank exemption, § 
50.50(d) 
• COOP = Cooperative exemption, § 
50.51 
• NOAL = No-action letter 
• OTHR = Other exceptions or 
exemptions, not including no-action letter 
relief 
O O O O O Transaction 
O if [Cleared] = ‘N’; 
NR if [Cleared] = ‘Y’ or ‘I’ 
Collateral 
NR 
Valuation 
NR 
N N 
13 CDE Counterparty Counterparty 1 
(reporting 
counterparty) 
Identifier of the counterparty to an OTC derivative transaction24 who is fulfilling its 
reporting obligation via the report in question. 
In jurisdictions where both parties must report the transaction, the identifier of 
Counterparty 1 always identifies the reporting counterparty. 
In the case of an allocated derivative transaction executed by a fund manager on 
behalf of a fund, the fund, and not the fund manager is reported as the 
counterparty. 
• Char(20), for an LEI 
code 
• Varchar(72), for 
natural persons who 
are acting as private 
individuals (not eligible 
for an LEI per the 
ROC Statement -
Individuals Acting in a 
Business Capacity25). 
• ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
• For natural persons who are acting as 
private individuals (not eligible for an LEI 
per the ROC Statement – Individuals 
Acting in a Business Capacity): LEI of the 
reporting counterparty followed by a 
unique identifier assigned and 
maintained consistently by the reporting 
counterparty for that natural person(s) for 
regulatory reporting purpose. 
M M M M M Transaction 
M 
Collateral 
M 
Valuation 
M 
Y Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Do not 
disseminate 
24 Throughout this Technical Specification, references to “OTC derivatives” in CDE data elements should be read to mean swaps. 25 ROC Statement – Individuals Acting in a Business Capacity, ROC Statement - Individuals Acting in a Business Capacity. 
CFTC Technical Specification Version 3.2 4

## Page 18

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
14 CDE Counterparty Counterparty 226 Identifier of the second counterparty27 to an OTC derivative transaction. 
In the case of an allocated derivative transaction executed by a fund manager on 
behalf of a fund, the fund, and not the fund manager is reported as the 
counterparty. 
• Char(20), for an LEI 
code 
• Varchar(72), for 
natural persons who 
are acting as private 
individuals (not eligible 
for an LEI per the 
ROC Statement -
Individuals Acting in a 
Business Capacity28) 
and for Privacy Law 
Identifier (PLI). 
• ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
• For natural persons who are acting as 
private individuals (not eligible for an LEI 
per the ROC Statement – Individuals 
Acting in a Business Capacity): LEI of the 
reporting counterparty followed by a 
unique identifier assigned and 
maintained consistently by the reporting 
counterparty for that natural person(s) for 
regulatory reporting purpose. 
• Privacy Law Identifier (PLI)29 
M M M M M Transaction 
M 
Collateral 
M 
Valuation 
M 
Y Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Do not 
disseminate 
15 CFTC Counterparty Counterparty 2 
identifier source 
Source used to identify the Counterparty 2. Char(4) • LEID = Legal Entity Identifier 
• NPID = Natural Person Identifier, to 
identify person who are acting as private 
individuals, not business entities 
• PLID = Privacy Law Identifier30 
M M M M M Transaction 
M 
Collateral 
M 
Valuation 
M 
Y Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Do not 
disseminate 
16 CFTC Counterparty Counterparty 1 
financial entity 
indicator 
Indicator of whether Counterparty 1 is a financial entity as defined in CEA § 
2(h)(7)(C). 
Boolean • True 
• False 
C C C C C Transaction 
C if [Cleared] = ‘N’ or ‘I’; 
NR if [Cleared] = ‘Y’ 
Collateral 
NR 
Valuation 
NR 
N N 
17 CFTC Counterparty Counterparty 2 
financial entity 
indicator 
Indicator of whether Counterparty 2 is a financial entity as defined in CEA § 
2(h)(7)(C). 
Boolean • True 
• False 
M M M M M Transaction 
M 
Collateral 
NR 
Valuation 
NR 
N N 
26 In the case of a swap transaction for pre-allocated block executed by a fund manager on behalf of a fund, the fund manager is reported as the counterparty. 27 Only one counterparty should be reported. In cases where multiple counterparties are legally responsible as the second counterparty (such as an obligated group, for example), report only one of the counterparties and use the 
same counterparty for all continuation data and lifecycle events. 28 ROC Statement – Individuals Acting in a Business Capacity, ROC Statement - Individuals Acting in a Business Capacity 29 Throughout this Technical Specification, Privacy Law Identifier (PLI) has been added as an allowable value for all Counterparty 2 (#14) associated data elements 30 Throughout this Technical Specification, for references to “Privacy Law Identifiers,” refer to DMO Letter No. 17-16, http://www.cftc.gov/idc/groups/public/@lrlettergeneral/documents/letter/17-16.pdf 
CFTC Technical Specification Version 3.2 5

## Page 19

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
18 CDE Counterparty Buyer identifier Identifier of the counterparty that is the buyer, as determined at the time of the 
transaction. 
A non-exhaustive list of examples of instruments for which this data element could 
apply are: 
• most forwards and forward-like contracts (except for foreign exchange forwards 
and foreign exchange non-deliverable forwards) 
• most options and option-like contracts including swaptions, caps and floors 
• credit default swaps (buyer/seller of protection) 
• variance, volatility and correlation swaps 
• contracts for difference and spreadbets 
This data element is not applicable to instrument types covered by data elements 
Payer identifier and Receiver identifier. 
• Char(20), for an LEI 
code 
• Varchar(72), for 
natural persons who 
are acting as private 
individuals (not eligible 
for an LEI per the 
ROC Statement – 
Individuals Acting in a 
Business Capacity) 
and for Privacy Law 
Identifier (PLI). 
• ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
• For natural persons who are acting as 
private individuals (not eligible for an LEI 
per the ROC Statement – Individuals 
Acting in a Business Capacity): LEI of the 
reporting counterparty followed by a 
unique identifier assigned and 
maintained consistently by the reporting 
counterparty for that natural person(s) for 
regulatory reporting purpose. 
• Privacy Law Identifier (PLI) 
C C C C C Transaction 
C if [Payer identifier] and 
[Receiver identifier] are not 
populated, else {blank}; 
When populated, the value 
shall match the value in 
[Counterparty 1 (reporting 
counterparty)] or [Counterparty 
2] 
Collateral 
NR 
Valuation 
NR 
N N 
19 CDE Counterparty Seller identifier Identifier of the counterparty that is the seller, as determined at the time of the 
transaction. 
A non-exhaustive list of examples of instruments for which this data element could 
apply are: 
• most forwards and forward-like contracts (except for foreign exchange forwards 
and foreign exchange non-deliverable forwards) 
• most options and option-like contracts including swaptions, caps and floors 
• credit default swaps (buyer/seller of protection) 
• variance, volatility and correlation swaps 
• contracts for difference and spreadbets 
This data element is not applicable to instrument types covered by data elements 
Payer identifier and Receiver identifier. 
• Char(20), for an LEI 
code 
• Varchar(72), for 
natural persons who 
are acting as private 
individuals (not eligible 
for an LEI per the 
ROC Statement – 
Individuals Acting in a 
Business Capacity) 
and for Privacy Law 
Identifier (PLI). 
• ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
• For natural persons who are acting as 
private individuals (not eligible for an LEI 
per the ROC Statement – Individuals 
Acting in a Business Capacity): LEI of the 
reporting counterparty followed by a 
unique identifier assigned and 
maintained consistently by the reporting 
counterparty for that natural person(s) for 
regulatory reporting purpose. 
• Privacy Law Identifier (PLI) 
C C C C C Transaction 
C if [Payer identifier] and 
[Receiver identifier] are not 
populated, else {blank}; 
When populated, the value 
shall match the value in 
[Counterparty 1 (reporting 
counterparty)] or [Counterparty 
2] 
Collateral 
NR 
Valuation 
NR 
N N 
20 CDE Counterparty Payer identifier 
[Payer identifier– 
Leg 1] 
[Payer identifier– 
Leg 2] 
Identifier of the counterparty of the payer leg as determined at the time of the 
transaction. 
A non-exhaustive list of examples of instruments for which this data element could 
apply are: 
• most swaps and swap-like contracts including interest rate swaps31, credit total 
return swaps, and equity swaps (except for credit default swaps, variance, 
volatility, and correlation swaps) 
• foreign exchange swaps, forwards, non-deliverable forwards 
This data element is not applicable to instrument types covered by data elements 
Buyer identifier and Seller identifier. 
• Char(20), for an LEI 
code 
• Varchar(72), for 
natural persons who 
are acting as private 
individuals (not eligible 
for an LEI per the 
ROC Statement – 
Individuals Acting in a 
Business Capacity) 
and for Privacy Law 
Identifier (PLI). 
• ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
• For natural persons who are acting as 
private individuals (not eligible for an LEI 
per the ROC Statement – Individuals 
Acting in a Business Capacity): LEI of the 
reporting counterparty followed by a 
unique identifier assigned and 
maintained consistently by the reporting 
counterparty for that natural person(s) for 
regulatory reporting purpose. 
• Privacy Law Identifier (PLI) 
C C C C C Transaction 
C if [Buyer identifier] and 
[Seller identifier] are not 
populated, else {blank}; 
When populated, the value 
shall match the value in 
[Counterparty 1 (reporting 
counterparty)] or [Counterparty 
2] 
Collateral 
NR 
Valuation 
NR 
N N 
31 For fixed-floating interest rate swaps, the payer is the counterparty paying the fixed rate 
CFTC Technical Specification Version 3.2 6

## Page 20

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
21 CDE Counterparty Receiver identifier 
[Receiver identifier￾Leg 1] 
[Receiver identifier￾Leg 2] 
Identifier of the counterparty of the receiver leg as determined at the time of the 
transaction. 
A non-exhaustive list of examples of instruments for which this data element could 
apply are: 
• most swaps and swap-like contracts including interest rate swaps32, credit total 
return swaps, and equity swaps (except for credit default swaps, variance, 
volatility, and correlation swaps) 
• foreign exchange swaps, forwards, non-deliverable forwards 
This data element is not applicable to instrument types covered by data elements 
Buyer identifier and Seller identifier. 
• Char(20), for an LEI 
code 
• Varchar(72), for 
natural persons who 
are acting as private 
individuals (not eligible 
for an LEI per the 
ROC Statement – 
Individuals Acting in a 
Business Capacity) 
and for Privacy Law 
Identifier (PLI). 
• ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
• For natural persons who are acting as 
private individuals (not eligible for an LEI 
per the ROC Statement – Individuals 
Acting in a Business Capacity): LEI of the 
reporting counterparty followed by a 
unique identifier assigned and 
maintained consistently by the reporting 
counterparty for that natural person(s) for 
regulatory reporting purpose. 
• Privacy Law Identifier (PLI) 
C C C C C Transaction 
C if [Buyer identifier] and 
[Seller identifier] are not 
populated, else {blank}; 
When populated, the value 
shall match the value in 
[Counterparty 1 (reporting 
counterparty)] or [Counterparty 
2] 
Collateral 
NR 
Valuation 
NR 
N N 
22 CFTC Counterparty Submitter identifier Identifier of the entity submitting the data to the swap data repository (SDR). 
The Submitter identifier will be the same as the reporting counterparty or swap 
execution facility (SEF), unless they use a third-party service provider to submit the 
data to SDR in which case, report the identifier of the third-party service provider. 
Char(20) ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
M M M M M Transaction 
M 
Collateral 
M 
Valuation 
M 
Y Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Do not 
disseminate 
23 CFTC Counterparty Counterparty 1 Indicator of whether Counterparty 1 is: Boolean • True M M M M M Transaction N N 
federal entity 
indicator (1) One of the following entities: 
a) An entity established pursuant to federal law, including, but not limited to, the 
• False M 
Collateral 
following: 
i. An “agency” as defined in 5 U.S.C. § 551(1), a federal instrumentality, or 
a federal authority; 
ii. A government corporation (examples: as such term is defined in 5 
NR 
Valuation 
NR 
U.S.C. § 103(1) or in 31 U.S.C. § 9101); 
iii. A government-sponsored enterprise (example: as such term is defined in 
2 U.S.C. § 622(8)); 
iv. A federally funded research and development center on the master list 
referenced in 48 CFR 35.017-6; and 
v. An executive department listed in 5 U.S.C. § 101; or 
b) An entity chartered pursuant to federal law after formation (example: an 
organization listed in title 36 of the U.S. Code); or 
(2) An entity that was established by, or at the direction of, one or more of the 
entities listed in clause (1), or has an ultimate parent listed in its LEI reference data 
that is an entity listed in clause (1) or in the first part of this clause (2). 
Notwithstanding the foregoing, the Counterparty 1 federal entity indicator data 
element does not include federally chartered depository institutions. 
32 For fixed-floating interest rate swaps, the receiver is the counterparty receiving the fixed rate 
CFTC Technical Specification Version 3.2 7

## Page 21

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
24 CFTC Counterparty Counterparty 2 Indicator of whether Counterparty 2 is: Boolean • True M M M M M Transaction N N 
federal entity 
indicator (1) One of the following entities: 
a) An entity established pursuant to federal law, including, but not limited to, the 
following: 
• False M 
Collateral 
NR 
i. An “agency” as defined in 5 U.S.C. § 551(1), a federal instrumentality, or 
a federal authority; 
ii. A government corporation (examples: as such term is defined in 5 
U.S.C. § 103(1) or in 31 U.S.C. § 9101); 
iii. A government-sponsored enterprise (example: as such term is defined in 
2 U.S.C. § 622(8)); 
iv. A federally funded research and development center on the master list 
referenced in 48 CFR 35.017-6; and 
v. An executive department listed in 5 U.S.C. § 101; or 
b) An entity chartered pursuant to federal law after formation (example: an 
organization listed in title 36 of the U.S. Code); or 
(2) An entity that was established by, or at the direction of, one or more of the 
entities listed in clause (1), or has an ultimate parent listed in its LEI reference data 
that is an entity listed in clause (1) or in the first part of this clause (2). 
Notwithstanding the foregoing, the Counterparty 2 federal entity indicator data 
element does not include federally chartered depository institutions. 
Valuation 
NR 
25 CFTC Custom 
baskets 
Custom basket 
indicator 
Indicator of whether the swap transaction is based on a custom basket. Boolean • True 
• False 
M M M M M Transaction 
M 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
26 CFTC Events Action type33 Type of action taken on the swap transaction or type of end-of-day reporting. 
Actions may include, but are not limited to, new, modify, correct, error, terminate, 
revive, transfer out, valuation, and collateral. 
New: An action that reports a new swap transaction. It applies to the first message 
relating to a new USI or UTI. 
Modify: An action that modifies the state of a previously submitted transaction 
(e.g., credit event) or changes a term of a previously submitted transaction due to a 
newly negotiated modification (amendment) or updates previously missing 
information (e.g., post price swap). It does not include correction of a previous 
transaction. 
Char(4) • NEWT = New 
• MODI = Modify 
• CORR = Correct 
• EROR = Error 
• TERM = Terminate 
• REVI = Revive 
• PRTO = Transfer out 
• VALU = Valuation 
• MARU = Collateral 
M M M M M Transaction 
M, for valid Action type and 
Event type Combination, see 
table in Appendix F. 
Collateral 
M, must equal ‘MARU’ 
Valuation 
M, must equal ‘VALU’ 
Y Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
For valid Action 
type and Event 
type Combination 
for public 
dissemination, see 
table in Appendix 
F. 
33 Only one Action type value is allowed per submission. Multiple Action type values should not be submitted in one transaction report. For example, if a data element needs to be corrected on a previously submitted transaction 
that is getting terminated, the Correct (CORR) value should be submitted as a separate submission prior to the submission of the Terminate (TERM) transaction. 
CFTC Technical Specification Version 3.2 8

## Page 22

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
Correct: An action that corrects erroneous data of a previously submitted 
transaction. 
Error: An action of cancellation of a wrongly submitted entire transaction in case it 
never came into existence or was not subject to part 43/part 45 reporting 
requirements but was reported erroneously, or a cancellation of duplicate report. 
Terminate: An action that closes an existing transaction because of a new event 
(e.g., Compression, Novation). This does not apply to transactions that terminate at 
contractual maturity date. 
Revive: An action that reinstates a swap transaction that was reported as error or 
terminated by mistake. 
Transfer out: An action that transfers swap transaction from one SDR to another 
SDR (change of swap data repository). 
Valuation: An update to valuation data. There will be no corresponding Event type. 
Collateral: An update to collateral margin data. There will be no corresponding 
Event type. 
Refer to appendix F for event model sample scenarios. 
27 CFTC Events Event type Explanation or reason for the action being taken on the swap transaction. Char(4) • TRAD = Trade C C C C C Transaction N Y Validation 
Events may include, but are not limited to, trade, novation, compression or risk 
reduction exercise, early termination, clearing, exercise, allocation, clearing and 
allocation, credit event, and transfer. 
Trade: A creation or modification of a transaction. 
Novation34: A novation legally moves partial or all of the financial risks of a swap 
from a transferor to a transferee and has the effect of terminating/modifying the 
original transaction and creating a new transaction to identify the exposure 
between the transferor/transferee and remaining party. 
Compression or Risk Reduction Exercise: Compressions and risk reduction 
exercises generally have the effect of terminating or modifying (i.e., reducing the 
• NOVA = Novation 
• COMP = Compression or Risk 
Reduction 
• ETRM = Early termination 
• CLRG = Clearing 
• EXER = Exercise 
• ALOC = Allocation 
• CLAL = Clearing & Allocation 
• CREV = Credit event 
• PTNG = Transfer 
• CORP = Corporate event 
• UPDT = Upgrade 
C, for valid Action type and 
Event type Combination, see 
table in Appendix F. 
Collateral 
NR 
Valuation 
NR 
Same as part 45 
(Transaction) 
Dissemination 
For valid Action 
type and Event 
type Combination 
for public 
dissemination, see 
table in Appendix 
F 
notional value) a set of existing transactions and of creating a set of new 
transaction(s). These processes result in largely the same exposure of market risk 
that existed prior to the event for the counterparty. 
Early termination: Termination of an existing swap transaction prior to scheduled 
termination or maturity date. 
Clearing: Central clearing is a process where a derivatives clearing organization 
interposes itself between counterparties to contracts, becoming the buyer to every 
seller and the seller to every buyer. It has the effect of terminating an existing 
34 Novation – see definition in § 45.1(a) 
CFTC Technical Specification Version 3.2 9

## Page 23

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
transaction between the buyer and the seller and thereby ensuring the 
performance of open contracts. 
Exercise: The process by which a counterparty fully or partially exercises their 
rights specified in the contract of an option or a swaption. 
Allocation35: The process by which an agent, having facilitated a single swap 
transaction on behalf of several clients, allocates a portion of the executed swap to 
the clients. 
Clearing and Allocation: A simultaneous clearing and allocation event in a 
derivatives clearing organization. 
Credit event: An event or trigger that results in the termination or modification of 
the state of a previously submitted credit derivative transaction. Applies only to 
credit derivatives. 
Transfer36: The process by which a swap is transferred to another SDR that has 
the effect of the closing of the swap transaction at one SDR or opening of the same 
swap transaction using the same UTI/USI in a different SDR (new). 
Corporate event: A corporate action on equity underlying that impacts the 
transactions on that equity. 
Upgrade: An upgrade of an outstanding transaction performed in order to ensure 
its conformity with the amended reporting requirements. 
28 CFTC Events Amendment 
indicator 
Indicator of whether the modification of the swap transaction reflects newly agreed 
upon term(s) from the previously negotiated terms. 
Boolean • True 
• False 
C C C C C Transaction 
C if [Action type] = ‘MODI’, else 
{blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
29 CFTC Events Event identifier Unique37 identifier to link swap transactions resulting from an event may be, but is 
not limited to, compression, and credit event. The unique identifier may be 
assigned by the reporting counterparty or a service provider. 
Varchar(52) ISO 17442 Legal Entity Identifier (LEI) 
code of the entity assigning the event 
identifier followed by a unique identifier 
up to 32 characters. 
C C C C C Transaction 
C if [Event type] = ‘COMP’ or 
‘CREV’, else {blank} 
Collateral 
NR 
Valuation 
NR 
N N 
35 Allocation – see definition in § 45.1(a) 36 Transfer – A reporting counterparty may change the swap data repository to which the transaction is reported pursuant to rule § 45.10(d). 37 The identifier which relates to the same event should be unique per event. 
CFTC Technical Specification Version 3.2 10

## Page 24

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
30 CFTC Events Event timestamp Date and time of occurrence of the event as determined by the reporting 
counterparty or a service provider.38 
In the case of a clearing event, date and time when the original swap is accepted 
by the derivative clearing organization (DCO) for clearing and recorded by the 
DCO’s system should be reported in this data element. 
The time element is as specific as technologically practicable. 
YYYY-MM￾DDThh:mm:ssZ, 
based on UTC39. 
Any valid date/time based on ISO 8601 
Date and time format. 
M M M M M Transaction 
M, the value shall be equal to 
or later than the value in 
[Execution timestamp] 
Collateral 
M 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
31 CDE Notional 
amounts and 
quantities 
Notional amount40 
[Notional amount￾Leg 1] 
[Notional amount￾Leg 2] 
For each leg of the transaction, where applicable: 
- for OTC derivative transactions negotiated in monetary amounts, amount 
specified in the contract. 
- for OTC derivative transactions negotiated in non-monetary amounts, refer to 
appendix B for converting notional amounts for non-monetary amounts. 
In addition: 
• For OTC derivative transactions with a notional amount schedule, the initial 
notional amount, agreed by the counterparties at the inception of the transaction, is 
reported in this data element. 
• For OTC foreign exchange options, in addition to this data element, the amounts 
are reported using the data elements Call amount and Put amount. 
• For amendments or lifecycle events41, the resulting outstanding notional amount 
is reported; (steps in notional amount schedules are not considered to be 
amendments or lifecycle events); 
• Where the notional amount is not known when a new transaction is reported, the 
notional amount is updated as it becomes available. 
Num(25,5) Any value 42 M M M M M Transaction 
M, for FX, if UPI.[Instrument 
type] = ‘Option’, the value shall 
match the value in [Call 
amount] or [Put amount] 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
32 CDE Notional 
amounts and 
quantities 
Notional currency 
[Notional currency￾Leg 1] 
[Notional currency￾Leg 2] 
For each leg of the transaction, where applicable: currency in which the notional 
amount is denominated. 
Char(3) Currencies included in ISO 4217 
Currency codes. 
M M M M M Transaction 
M, for FX, if UPI.[Instrument 
type] = ‘Option’, the value shall 
match the value in [Call 
currency] or [Put currency] 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
33 CDE Notional 
amounts and 
quantities 
Notional amount 
schedule - notional 
amount in effect on 
For each leg of the transaction, where applicable: 
for OTC derivative transactions negotiated in monetary amounts with a notional 
amount schedule: 
Num(25,5) Any value greater than or equal to zero. O C O O O Transaction - IR 
C if UPI.[Notional schedule] ≠
‘Constant’, else {blank} 
N Y Validation 
Same as part 45 
(Transaction) 
38 In the case of collateral update (Action type = ‘MARU’), this is the date for which the information contained in the report is provided. Time portion should be reported as “00:00:00”. 39 Both the date and time portion are required to be reported. If the time portion is not available, report “00:00:00” for the time portion. 40 Notional amount for CDS should reflect the gross amount and not the net amount after reflecting version incrementing due to a credit event 41 In the case of a lifecycle event that is a full termination before the swap maturity date, the full terminated value should be reported in the notional data element. 42 “99999999999999999999.99999” is accepted when the value is not available at the time of reporting. 25 numerical characters including decimals. 
CFTC Technical Specification Version 3.2 11

## Page 25

Technical Specification Validation Rules and Dissemination Rules 
# Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
CO 
associated effective 
date 
[Notional amount in 
effect on associated 
effective date-Leg 
1] 
[Notional amount in 
effect on associated 
effective date-Leg 
2] 
• Notional amount which becomes effective on the associated unadjusted effective 
date. 
The initial notional amount and associated unadjusted effective and end date are 
reported as the first values of the schedule. 
This data element is not applicable to OTC derivative transactions with notional 
amounts that are condition- or event-dependent. The currency of the varying 
notional amounts in the schedule is reported in Notional currency. 
Collateral 
NR 
Valuation 
NR 
Dissemination 
Disseminate only 
the first 10 
reported values of 
the schedule 
34 CDE Notional 
amounts and 
quantities 
Notional amount 
schedule -
unadjusted effective 
date of the notional 
amount 
[Effective date of 
the notional 
amount-Leg 1] 
[Effective date of 
the notional 
amount-Leg 2] 
For each leg of the transaction, where applicable: 
for OTC derivative transactions negotiated in monetary amounts with a notional 
amount schedule: 
• Unadjusted date on which the associated notional amount becomes effective 
This data element is not applicable to OTC derivative transactions with notional 
amounts that are condition- or event-dependent. The currency of the varying 
notional amounts in the schedule is reported in Notional currency. 
YYYY-MM-DD, based 
on UTC. 
Any valid date based on ISO 8601 Date 
and time format. 
C C C C C Transaction 
C if [Notional amount schedule 
- notional amount in effect on 
associated effective date] is 
populated, else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
Transaction) 
issemination 
isseminate only 
he first 10 
eported values of 
he schedule 
(
D
D
t
r
t
35 CDE Notional 
amounts and 
quantities 
Notional amount 
schedule -
unadjusted end 
date of the notional 
amount 
[End date of the 
notional amount￾Leg 1] 
[End date of the 
notional amount￾Leg 2] 
For each leg of the transaction, where applicable: 
for OTC derivative transactions negotiated in monetary amounts with a notional 
amount schedule: 
• Unadjusted end date of the notional amount 
(not applicable if the unadjusted end date of a given schedule’s period is back-to￾back with the unadjusted effective date of the subsequent period). 
This data element is not applicable to OTC derivative transactions with notional 
amounts that are condition- or event-dependent. The currency of the varying 
notional amounts in the schedule is reported in Notional currency. 
YYYY-MM-DD, based 
on UTC. 
Any valid date based on ISO 8601 Date 
and time format. 
C C C C C Transaction 
C if [Notional amount schedule 
- notional amount in effect on 
associated effective date] is 
populated, else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate only 
the first 10 
reported values of 
the schedule 
36 CDE Notional 
amounts and 
quantities 
Call amount For foreign exchange options, the monetary amount that the option gives the right 
to buy. 
Num(25,5) Any value greater than zero. N 
R 
N 
R 
C N 
R 
N 
R 
Transaction - FX 
C if UPI.[Instrument type] = 
‘Option’, at least one is 
required: ([Call amount] or [Put
amount]) 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
37 CDE Notional 
amounts and 
quantities 
Call currency For foreign exchange options, the currency in which the Call amount is 
denominated. 
Char(3) Currencies included in ISO 4217 
Currency codes. 
N 
R 
N 
R 
C N 
R 
N 
R 
Transaction - FX 
C if [Call amount] is populated,
else {blank} 
N Y Validation 
Same as part 45 
(Transaction) 
 ecruSo
ya Dd of n 45 E P
dterope43 RP
IR
FX
QE
CFTC Technical Specification Version 3.2 12

## Page 26

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
Collateral 
NR 
Valuation 
NR 
Dissemination 
Disseminate 
38 CDE Notional 
amounts and 
quantities 
Put amount For foreign exchange options, the monetary amount that the option gives the right 
to sell. 
Num(25,5) Any value greater than zero. N 
R 
N 
R 
C N 
R 
N 
R 
Transaction – FX 
C if UPI.[Instrument type] = 
‘Option’, at least one is 
required: ([Call amount] or [Put 
amount]) 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
39 CDE Notional 
amounts and 
quantities 
Put currency For foreign exchange options, the currency in which the Put amount is 
denominated. 
Char(3) Currencies included in ISO 4217 
Currency codes. 
N 
R 
N 
R 
C N 
R 
N 
R 
Transaction – FX 
C if [Put amount] is populated, 
else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
40 CFTC Notional 
amounts and 
quantities 
Notional quantity 
[Notional quantity￾Leg 1] 
[Notional quantity￾Leg 2] ] 
For each leg of the swap transaction, where applicable, for swap transactions 
negotiated in non-monetary amounts with fixed notional quantity for each schedule 
period (i.e., 50 barrels per month). 
The frequency is reported in Quantity frequency and the unit of measure is 
reported in Quantity unit of measure. 
Num(25,5) Any value greater than or equal to zero. N 
R 
N 
R 
N 
R 
N 
R 
O Transaction – CO 
O 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
41 CFTC Notional 
amounts and 
quantities 
Quantity 
frequency43 
[Quantity frequency￾Leg 1] 
[Quantity frequency￾Leg 2] 
The rate at which the quantity is quoted on the swap transaction. e.g., hourly, daily, 
weekly, monthly. 
Char(4) • HOUL = Hourly 
• DAIL = Daily 
• WEEK = Weekly 
• MNTH = Monthly 
• ONDE = OnDemand 
• YEAR = Yearly 
• EXPI = End of term 
• ADHO = Ad hoc which applies when 
payments are irregular 
N 
R 
N 
R 
N 
R 
N 
R 
C Transaction - CO 
C if [Notional quantity] is 
populated, else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
42 CFTC Notional 
amounts and 
quantities 
Quantity frequency 
multiplier 
[Quantity frequency 
multiplier-Leg 1] 
The number of time units for the Quantity frequency. Num(3,0) Any value greater than or equal to zero. N 
R 
N 
R 
N 
R 
N 
R 
C Transaction - CO 
C if [Quantity frequency] ≠ 
‘ONDE’ or ‘ADHO’, else {blank} 
Collateral 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
43 To represent quarterly, report [Quantity frequency] = ‘MNTH’ and [Quantity frequency multiplier] = ‘3’. For semi-annual, report [Quantity frequency] = ‘MNTH’ and [Quantity frequency multiplier] = ‘6’. 
CFTC Technical Specification Version 3.2 13

## Page 27

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
[Quantity frequency 
multiplier-Leg 2] 
Valuation 
NR 
43 CDE Notional 
amounts and 
quantities 
Quantity unit of 
measure 
[Quantity unit of 
measure-Leg 1] 
[Quantity unit of 
measure-Leg 2] 
For each leg of the transaction, where applicable: unit of measure in which the 
Total notional quantity and Notional quantity are expressed. 
Varchar(4) ISO 20022 UnitOfMeasureCode codeset 
or other SDR approved UOM codeset 
N 
R 
N 
R 
N 
R 
M M Transaction – EQ/CO 
M 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
44 CDE Notional 
amounts and 
quantities 
Total notional 
quantity 
[Total notional 
quantity-Leg 1] 
[Total notional 
quantity-Leg 2] 
For each leg of the transaction, where applicable: aggregate Notional quantity of 
the underlying asset for the term of the transaction. 
Where the Total notional quantity is not known when a new transaction is reported, 
the Total notional quantity is updated as it becomes available. 
Num(25,5) Any value greater than or equal to zero.44 N 
R 
N 
R 
N 
R 
M M Transaction – EQ/CO 
M 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
45 CFTC Packages Package indicator Indicator of whether the swap transaction is part of a package transaction. Boolean • True 
• False 
M M M M M Transaction 
M 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
46 CDE Packages Package identifier45 Identifier (determined by the reporting counterparty) in order to connect 
• two or more transactions that are reported separately by the reporting 
counterparty, but that are negotiated together as the product of a single economic 
agreement. 
• two or more reports pertaining to the same transaction whenever jurisdictional 
reporting requirement does not allow the transaction to be reported with a single 
report to TRs. 
A package46 may include reportable and non-reportable transactions. 
This data element is not applicable 
• if no package is involved, or 
• to allocations 
Varchar(100) Up to 100 alphanumeric characters.47 C C C C C Transaction 
C if [Package indicator] = 
‘True’, else {blank} 
Collateral 
NR 
Valuation 
NR 
N N 
44 ”99999999999999999999.99999” is accepted when the value is not available. 25 numerical characters including decimals. 45 To report a collar, this field should be populated to link the cap and floor legs. To report a straddle, this field should be populated to link the payer swaption and receiver swaption legs. 46 In addition, a “package transaction” also includes a transaction involving two or more instruments: (1) that is executed between two or more counterparties; (2) that is priced or quoted as one economic transaction with 
simultaneous or near simultaneous execution of all components; (3) where the execution of each component is contingent upon the execution of all other components; (4) where each component is assigned a Unique Swap 
Identifier (USI) or Unique Transaction Identifier (UTI); and (5) each component is reported separately. 47 “UNKNOWN” is accepted when the value is not available. 
CFTC Technical Specification Version 3.2 14

## Page 28

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
Where the Package identifier is not known when a new transaction is reported, the 
Package identifier is updated as it becomes available. 
47 CDE Packages Package 
transaction price 
Traded price of the entire package in which the reported derivative transaction is a 
component. 
This data element is not applicable if 
• no package is involved, or 
• package transaction spread is used 
Prices and related data elements of the transactions (Price currency, Price 
notation, Price unit of measure) that represent individual components of the 
package are reported when available. 
The Package transaction price may not be known when a new transaction is 
reported but may be updated later. 
• Num(18,13), if 
Package transaction 
price notation = 1 
• Num(11,10), if 
Package transaction 
price notation = 3 
• Any value, if Package transaction price 
notation = 1 
• Any value expressed as decimal (e.g., 
0.0257 instead of 2.57%), if Package 
transaction price notation = 348 49 
C C C C C Transaction 
C if [Package indicator] = ‘True’ 
and [Package transaction 
spread] is not populated, else 
{blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
48 CDE Packages Package 
transaction price 
currency 
Currency in which the Package transaction price is denominated. 
This data element is not applicable if 
• no package is involved, or 
• Package transaction spread is used, or 
• Package transaction price notation = 3 
Char(3) Currencies included in ISO 4217 
Currency codes. 
C C C C C Transaction 
C if [Package transaction price 
notation] = ‘1’, else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
49 CDE Packages Package 
transaction price 
notation 
Manner in which the Package transaction price is expressed. 
This data element is not applicable if 
• no package is involved, or 
• Package transaction spread is used 
Char(1) • 1 = Monetary amount 
• 3 = Decimal50 
C C C C C Transaction 
C if [Package transaction price] 
is populated, else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
50 CDE Packages Package 
transaction spread 
Traded price of the entire package in which the reported derivative transaction is a 
component of a package transaction. 
Package transaction price when the price of the package is expressed as a spread, 
difference between two reference prices. 
This data element is not applicable if 
• no package is involved, or 
• Num(18,13), if 
Package transaction 
spread notation = 1 
• Num(11,10), if 
Package transaction 
spread notation = 3 
• Num(5), if Package 
• Any value, if Package transaction 
spread notation = 1 
• Any value expressed as decimal (eg 
0.0257 instead of 2.57%), Package 
spread price notation = 352 
• Any integer value expressed in basis 
C C C C C Transaction 
C if [Package indicator] = ‘True’ 
and [Package transaction price] 
is not populated, else {blank} 
Collateral 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
48 The allowable values are restricted based on CFTC’s jurisdictional requirements. 49 Default value with all 9’s, for any of the allowable formats, is accepted when the value is unknown. When [Package transaction price notation] = ‘1’ use “99999.9999999999999” (18 numerical characters including 13 decimal 
places). When [Package transaction price notation] = ‘3’ use “9.9999999999” (11 numerical characters including 10 decimal places). 50 The allowable values are restricted based on CFTC’s jurisdictional requirements. 52 The allowable values are restricted based on CFTC’s jurisdictional requirements. 
CFTC Technical Specification Version 3.2 15

## Page 29

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
• Package transaction price is used 
Spread and related data elements of the transactions (spread currency, Spread 
notation) that represent individual components of the package are reported when 
available. 
Package transaction spread may not be known when a new transaction is reported 
but may be updated later.51 
transaction spread 
notation = 4 
points (eg 257 instead of 2.57%), if 
Package transaction spread notation = 4 
Valuation 
NR 
51 CDE Packages Package 
transaction spread 
currency 
Currency in which the Package transaction spread is denominated. 
This data element is not applicable if 
• no package is involved, or 
• Package transaction price is used, or 
• Package transaction spread notation = 3, or = 4 
Char(3) Currencies included in ISO 4217 
Currency codes. 
C C C C C Transaction 
C if [Package transaction 
spread notation] = '1', else 
{blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
52 CDE Packages Package 
transaction spread 
notation 
Manner in which the Package transaction spread is expressed. 
This data element is not applicable if 
• no package is involved, or 
• Package transaction price is used. 
Char(1) • 1 = Monetary amount 
• 3 = Decimal53 
• 4 = Basis points 
C C C C C Transaction 
C if [Package transaction 
spread] is populated, else 
{blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
53 CDE Payments Day count 
convention 
[Fixed rate day 
count convention￾leg 1] 
[Fixed rate day 
count convention￾leg 2] 
[Floating rate day 
count convention￾leg 1] 
[Floating rate-day 
count convention￾leg 2] 
For each leg of the transaction, where applicable: day count convention (often also 
referred to as day count fraction or day count basis or day count method) that 
determines how interest payments are calculated. It is used to compute the year 
fraction of the calculation period, and indicates the number of days in the 
calculation period divided by the number of days in the year. 
Char(4) • A001 
• A002 
• A003 
• A004 
• A005 
• A006 
• A007 
• A008 
• A009 
• A010 
• A011 
• A012 
• A013 
• A014 
• A015 
• A016 
O O O C C Transaction – CR/IR/FX 
O 
Transaction – CO/EQ 
C if [Payment frequency period] 
is populated, else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
51 Default value with all 9’s, for any of the allowable formats, is accepted when the value is unknown. When [Package transaction price notation] = ‘1’ use “99999.9999999999999” (18 numerical characters including 13 decimal 
places). When [Package transaction price notation] = ‘3’ use “9.9999999999” (11 numerical characters including 10 decimal places). When [Package transaction spread notation] = ‘4’ use “99999” (5 numerical characters with no 
decimal places). 
53 The allowable values are restricted based on CFTC’s jurisdictional requirements. 
CFTC Technical Specification Version 3.2 16

## Page 30

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
• A017 
• A018 
• A019 
• A020 
• NARR 
For a description of the allowable values 
see Appendix C. 
54 CFTC Payments Fixing date 
[Fixing date-Leg 1] 
[Fixing date-Leg 2] 
Describes the specific date when a non-deliverable forward as well as various 
types of FX OTC options such as cash-settled options that will "fix" against a 
particular exchange rate, which will be used to compute the ultimate cash 
settlement. 
YYYY-MM-DD Any valid date based on ISO 8601 Date 
and time format. 
O O C O O Transaction – CR/IR/EQ/CO 
O 
Transaction - FX 
C if (UPI.[Instrument type] = 
‘Forward’ or ‘Option’) and 
UPI.[Delivery type] = ‘Cash’, 
else {blank} 
Collateral 
NR 
Valuation 
NR 
N N 
55 CFTC Payments Floating rate reset 
frequency period 
[Floating rate reset 
frequency period￾leg 1] 
[Floating rate reset 
frequency period￾leg 2] 
For each floating leg of the swap transaction, where applicable, time unit 
associated with the frequency of resets, e.g., day, week, month, year or term of the 
stream. 
Char(4) • DAIL = Daily 
• WEEK = Weekly 
• MNTH = Monthly 
• YEAR = Yearly 
• ADHO = Ad hoc which applies when 
payments are irregular 
• EXPI = Payment at term 
O C O O O Transaction – CR/FX/EQ/CO 
O 
Transaction - IR 
C if UPI.[Instrument type] = 
‘Swap’ and UPI Underlier type] 
≠ ‘Fixed - Fixed’, else {blank} 
When populated with ‘EXPI’, 
[Floating rate reset frequency 
period multiplier] must be ‘1’ 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
56 CFTC Payments Floating rate reset 
frequency period 
multiplier 
[Floating rate reset 
frequency period 
multiplier-leg 1] 
[Floating rate reset 
frequency period 
multiplier-leg 2] 
For each floating leg of the swap transaction, where applicable, number of time 
units (as expressed by the Floating rate reset frequency period) that determines 
the frequency at which periodic payment dates for reset occur. For example, a 
transaction with reset payments occurring every two months is represented with a 
Floating rate reset frequency period of “MNTH” (monthly) and a Floating rate reset 
frequency period multiplier of 2. 
This data element is not applicable if the Floating rate reset frequency period is 
“ADHO”. If Floating rate reset frequency period is “EXPI”, then the Floating rate 
reset frequency period multiplier is 1. If the reset frequency period is intraday, then 
the Floating rate reset frequency period is “DAIL” and the Floating rate reset 
frequency period multiplier is 0. 
Num(3,0) Any value greater than or equal to zero. C C C C C Transaction 
C if [Floating rate reset 
frequency period] ≠ ‘ADHO’, 
else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
CFTC Technical Specification Version 3.2 17

## Page 31

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
57 CDE Payments Other payment type Type of Other payment amount. 
Option premium payment is not included as a payment type as premiums for option 
are reported using the option premium dedicated data element. 
Char(4) • UFRO = Upfront Payment, i.e., the 
initial payment made by one of the 
counterparties either to bring a 
transaction to fair value or for any other 
reason that may be the cause of an off￾market transaction 
• UWIN = Unwind or Full termination, i.e., 
the final settlement payment made when 
a transaction is unwound prior to its end 
date; Payments that may result due to 
full termination of derivative 
transaction(s) 
• PEXH = Principal Exchange, i.e., 
Exchange of notional values for cross￾currency swaps 
C O O O O Transaction - CR 
C, at least one is required: 
([Fixed rate] or [Spread] or 
[Other payment type] = 
‘UFRO’). 
Allowable values ‘UWIN’ and 
‘PEXH’ are optional and 
independent of the above 
condition 
Transaction – IR/FX/EQ/CO 
O 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
58 CDE Payments Other payment 
amount54 
Payment amounts with corresponding payment types to accommodate 
requirements of transaction descriptions from different asset classes. 
Num(25,5) Any value greater than or equal to zero. C C C C C Transaction 
C if [Other payment type] is 
populated, else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
59 CDE Payments Other payment 
currency 
Currency in which Other payment amount is denominated. Char(3) Currencies included in ISO 4217 
Currency codes. 
C C C C C Transaction 
C if [Other payment amount] is 
populated, else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
60 CDE Payments Other payment date Unadjusted date on which the Other payment amount is paid. YYYY-MM-DD, based 
on UTC. 
Any valid date based on ISO 8601 Date 
and time format. 
C C C C C Transaction 
C if [Other payment amount] is 
populated, else {blank} 
Collateral 
NR 
Valuation 
NR 
N N 
54 The set of data elements related to other payments (Other payment type [#57], Other payment amount [#58], Other payment currency [#59], Other payment date [#60], Other payment payer [#61], Other payment receiver 
[#62]) can be reported multiple times in the case of multiple payments. 
CFTC Technical Specification Version 3.2 18

## Page 32

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
61 CDE Payments Other payment 
payer 
Identifier of the payer of Other payment amount. • Char(20), for an LEI 
code 
• Varchar(72), for 
natural persons who 
are acting as private 
individuals (not eligible 
for an LEI per the 
ROC Statement – 
Individuals Acting in a 
Business Capacity) 
and for Privacy Law 
Identifier (PLI). 
• ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
• For natural persons who are acting as 
private individuals (not eligible for an LEI 
per the ROC Statement – Individuals 
Acting in a Business Capacity): LEI of the 
reporting counterparty followed by a 
unique identifier assigned and 
maintained consistently by the reporting 
counterparty for that natural person(s) for 
regulatory reporting purpose. 
• Privacy Law Identifier (PLI) 
C C C C C Transaction 
C if [Other payment amount] is 
populated, else {blank} 
Collateral 
NR 
Valuation 
NR 
N N 
62 CDE Payments Other payment 
receiver 
Identifier of the receiver of Other payment amount. • Char(20), for and LEI 
code 
• Varchar(72), for 
natural persons who 
are acting as private 
individuals (not eligible 
for an LEI per the 
ROC Statement – 
Individuals Acting in a 
Business Capacity) 
and for Privacy Law 
Identifier (PLI). 
• ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
• For natural persons who are acting as 
private individuals (not eligible for an LEI 
per the ROC Statement – Individuals 
Acting in a Business Capacity): LEI of the 
reporting counterparty followed by a 
unique identifier assigned and 
maintained consistently by the reporting 
counterparty for that natural person(s) for 
regulatory reporting purpose. 
• Privacy Law Identifier (PLI) 
C C C C C Transaction 
C if [Other payment amount] is 
populated, else {blank} 
Collateral 
NR 
Valuation 
NR 
N N 
63 CDE Payments Payment frequency 
period55 
[Fixed rate payment 
frequency period￾Leg 1] 
[Fixed rate payment 
frequency period￾Leg 2] [Floating rate 
payment frequency 
period-Leg 1] 
[Floating rate 
payment frequency 
period-Leg 2] 
For each leg of the transaction, where applicable: time unit associated with the 
frequency of payments, e.g., day, week, month, year or term of the stream. 
Char(4) • DAIL = Daily 
• WEEK = Weekly 
• MNTH = Monthly 
• YEAR = Yearly 
• ADHO = Ad hoc which applies when 
payments are irregular 
• EXPI 56 = Payment at term 
O O N 
R 
O O Transaction – CR/IR/EQ/CO 
O, when populated with ‘EXPI, 
[Payment frequency period 
multiplier] must be ‘1’ 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
55 To represent quarterly payment, report [Payment frequency period] = ‘MNTH’ and [Payment frequency period multiplier] = ‘3’. For semi-annual payment, report [Payment frequency period] = ‘MNTH’ and [Payment frequency 
period multiplier] = ‘6’. 
56 Throughout this Technical Specification, for the allowable value ‘EXPI’ in frequency period related data elements, two different descriptions ‘Payment at term’ and ‘End of term’ are being used which in essence has the same 
meaning and represents the frequency/rate of payment/quantity. 
CFTC Technical Specification Version 3.2 19

## Page 33

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
64 CDE Payments Payment frequency 
period multiplier 
[Fixed rate payment 
frequency period 
multiplier-Leg 1] 
[Fixed rate payment 
frequency period 
multiplier-Leg 2] 
[Floating rate 
payment frequency 
period multiplier￾Leg 1] 
[Floating rate 
payment frequency 
period multiplier￾Leg 2] 
For each leg of the transaction, where applicable: number of time units (as 
expressed by the Payment frequency period) that determines the frequency at 
which periodic payment dates occur. For example, a transaction with payments 
occurring every two months is represented with a Payment frequency period of 
“MNTH” (monthly) and a Payment frequency period multiplier of 2. 
This data element is not applicable if the Payment frequency period is “ADHO.” If 
Payment frequency period is “EXPI”, then the Payment frequency period multiplier 
is 1. If the Payment frequency is intraday, then the Payment frequency period is 
“DAIL” and the Payment frequency multiplier is 0. 
Num(3,0) Any value greater than or equal to zero. C C N 
R 
C C Transaction – CR/IR/EQ/CO 
C if [Payment frequency period] 
≠ ‘ADHO’, else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
65 CDE Prices Exchange rate57 Exchange rate between the two different currencies specified in the OTC derivative 
transaction agreed by the counterparties at the inception of the transaction, 
expressed as the rate of exchange from converting the unit currency into the 
quoted currency. 
In the example 0.9426 USD/EUR, USD is the unit currency and EUR is the quoted 
currency; USD 1 = EUR 0.9426. 
Num(18,13) Any value greater than zero. N 
R 
N 
R 
M N 
R 
N 
R 
Transaction – FX 
M 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
66 CDE Prices Exchange rate 
basis 
Currency pair and order in which the exchange rate is denominated, expressed as 
unit currency/quoted currency. In the example 0.9426 USD/EUR, USD is the unit 
currency and EUR is the quoted currency, USD 1 = EUR 0.9426. 
Char(3)/Char(3); [Unit 
currency/Quoted 
currency], without 
restricting the currency 
pair ordering (i.e., the 
exchange rate basis 
may be USD/EUR or 
EUR/USD. 
Any pair of currencies included in ISO 
4217 Currency codes. 
N 
R 
N 
R 
M N 
R 
N 
R 
Transaction – FX 
M 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
67 CDE Prices Fixed rate 
[Fixed rate-Leg 1] 
[Fixed rate-Leg 2] 
For each leg of the transaction, where applicable: for OTC derivative transactions 
with periodic payments, per annum rate of the fixed leg(s). 
Num(11,10) Positive and negative values expressed 
as decimal (e.g., 0.0257 instead of 
2.57%)58 
C C N 
R 
N 
R 
C Transaction - CR 
C if [Spread] is not populated 
and [Other payment type] ≠
‘UFRO’, and [Post-priced swap 
indicator] = ‘False’, and 
UPI.[Instrument type] ≠
‘Option’, else {blank} 
Transaction - IR 
C if [Spread] is not populated 
and [Post-priced swap 
indicator] = ‘False’, and 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
57 For FX, forward exchange rate would be reported in this data element. 58 The allowable values are restricted based on CFTC’s jurisdictional requirements. 
CFTC Technical Specification Version 3.2 20

## Page 34

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
UPI.[Instrument type] ≠
‘Option’, else {blank} 
Transaction - CO 
C if [Price] or [Spread] is not 
populated and [Post-priced 
swap indicator] = ‘False’, and 
UPI.[Instrument type] ≠
‘Option’, else {blank} 
Collateral 
NR 
Valuation 
NR 
68 CFTC Prices Post-priced swap 
indicator 
Indicator of whether the swap transaction satisfies the definition of “post-priced 
swap” in § 43.2(a) of the Commission’s regulations. 
Boolean • True59 
• False 
M M M M M Transaction 
M 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
69 CDE Prices Price60 Price specified in the OTC derivative transaction. It does not include fees, taxes or 
commissions. 
For commodity fixed/float swaps and similar products with periodic payments, this 
data element refers to the fixed price of the fixed leg(s). 
For commodity and equity forwards and similar products, this data element refers 
• Num(18,13), if Price 
notation = 1 
• Num(11,10), if Price 
notation = 3 
• Any value, if Price notation = 1 
• Any value expressed as decimal (e.g., 
0.0257 instead of 2.57%), if Price 
notation = 361 
N 
R 
N 
R 
N 
R 
C C Transaction - EQ 
C if [Spread] is not populated 
and [Post-priced swap 
indicator] = ‘False’, and 
UPI.[Instrument type] ≠ 
‘Option’, else {blank} 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
to the forward price of the underlying or reference asset. 
For equity swaps, portfolios swaps, and similar products, this data element refers 
to the initial price of the underlying or reference asset. 
For contracts for difference and similar products, this data element refers to the 
initial price of the underlier. 
This data element is not applicable to: 
• Interest rate swaps and forward rate agreements, as it is understood that the 
information included in the data elements Fixed rate and Spread may be 
interpreted as the price of the transaction. 
• Interest rate options and interest rate swaptions as it is understood that the 
information included in the data elements Strike price and Option premium may be 
interpreted as the price of the transaction. 
• Commodity basis swaps and the floating leg of commodity fixed/float swaps as it 
is understood that the information included in the data element Spread may be 
Transaction - CO 
C if ([Fixed rate] or [Spread] is 
not populated) and [Post-priced 
swap indicator] = ‘False’, and 
UPI.[Instrument type] ≠
‘Option’, else {blank} 
Collateral 
NR 
Valuation 
NR 
59 For transactions where the swap price is not known at the time to execution, those unknown swap price-related fields can be reported as blank until such time that the price is known. 60 While Price (#69) captures the prices at which counterparties negotiate contracts, market prices are reflected in the valuation amounts. 61 The allowable values are restricted based on CFTC’s jurisdictional requirements. 
CFTC Technical Specification Version 3.2 21

## Page 35

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
interpreted as the price of the transaction. 
• Foreign exchange swaps, forwards and options, as it is understood that the 
information included in the data elements Exchange rate, Strike price, and Option 
premium may be interpreted as the price of the transaction. 
• Equity options as it is understood that the information included in the data 
elements Strike price and Option premium may be interpreted as the price of the 
transaction. 
• Credit default swaps and credit total return swaps, as it is understood that the 
information included in the data elements Fixed rate, Spread and Upfront payment 
(Other payment type: Upfront payment) may be interpreted as the price of the 
transaction. 
• Commodity options, as it is understood that the information included in the data 
elements Strike price and Option premium may be interpreted as the price of the 
transaction. 
Where the price is not known when a new transaction is reported, the price is 
updated as it becomes available. 
For transactions that are part of a package, this data element contains the price of 
the component transaction where applicable. 
70 CDE Prices Price currency Currency in which the price is denominated. 
Price currency is only applicable if Price notation = 1. 
Char(3) Currencies included in ISO 4217 
Currency codes. 
N 
R 
N 
R 
N 
R 
C C Transaction - EQ/CO 
C if [Price notation] = ‘1’, else 
{blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
71 CDE Prices Price notation Manner in which the price is expressed. Char(1) • 1 = Monetary amount 
• 3 = Decimal62 
N 
R 
N 
R 
N 
R 
C C Transaction - EQ/CO 
C if [Price] is populated, else 
{blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
72 CDE Prices Price unit of 
measure 
Unit of measure in which the price is expressed. Varchar(4) ISO 20022 UnitOfMeasureCode codeset 
or other SDR approved UOM codeset 
N 
R 
N 
R 
N 
R 
C C Transaction - EQ/CO 
C if [Price] is populated, else 
{blank} 
Collateral 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
62 The allowable values are restricted based on CFTC’s jurisdictional requirements. 
CFTC Technical Specification Version 3.2 22

## Page 36

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
Valuation 
NR 
73 CDE Prices Spread63 
[Spread-Leg 1] 
[Spread-Leg 2] 
For each leg of the transaction, where applicable: for OTC derivative transactions 
with periodic payments (e.g., interest rate fixed/float swaps, interest rate basis 
swaps, commodity swaps), 
• spread on the individual floating leg(s) index reference price, in the case where 
there is a spread on a floating leg(s). For example, USD-LIBOR-BBA plus .03 or 
WTI minus USD 14.65; or 
• difference between the reference prices of the two floating leg indexes. For 
• Num(18,13), if 
Spread notation = 1 
• Num(11,10), if 
Spread notation = 3 
• Num(5), if Spread 
notation = 4 
• Any value, if Spread notation = 1 
• Any value expressed as decimal (e.g., 
0.0257 instead of 2.57%), if Spread 
notation = 364 
• Any integer value expressed in basis 
points (e.g., 257 instead of 2.57%), if 
Spread notation = 4 
C C N 
R 
C C Transaction - CR 
C if [Fixed rate] is not 
populated and [Other payment 
type] ≠ ‘UFRO’, and [Post￾priced swap indicator] = ‘False’, 
and UPI.[Instrument type] ≠
‘Option’, else {blank} 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
. 
example, the 9.00 USD “Spread” for a WCS vs. WTI basis swap where WCS is 
priced at 43 USD and WTI is priced at 52 USD. 
Transaction - IR 
C if [Fixed rate] is not 
populated and [Post-priced 
swap indicator] = ‘False’, and 
UPI.[Instrument type] ≠
‘Option’, else {blank} 
Transaction - EQ 
C if [Price] is not populated, 
and [Post-priced swap 
indicator] = ‘False’, and 
UPI.[Instrument type] ≠ 
‘Option’, else {blank} 
Transaction - CO 
C if [Price] or [Fixed rate] is not 
populated and [Post-priced 
swap indicator] = ‘False’, and 
UPI.[Instrument type] ≠
‘Option’, else {blank} 
Collateral 
NR 
Valuation 
NR 
74 CDE Prices Spread currency 
[Spread currency￾Leg 1] 
[Spread currency￾Leg 2] 
For each leg of the transaction, where applicable: currency in which the spread is 
denominated. 
This data element is only applicable if Spread notation = 1. 
Char(3) Currencies included in ISO 4217 
Currency codes. 
C C N 
R 
C C Transaction - CR/IR/EQ/CO 
C if [Spread notation] = ‘1’, else 
{blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
63 For equity swaps, portfolio swaps, and contract for difference (CFDs), report the weighted overall spread for the basket instead of individual legs. 64 The allowable values are restricted based on CFTC’s jurisdictional requirements. 
CFTC Technical Specification Version 3.2 23

## Page 37

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
75 CDE Prices Spread notation 
[Spread notation￾Leg 1] 
[Spread notation￾Leg 2] 
For each leg of the transaction, where applicable: manner in which the spread is 
expressed. 
Char(1) • 1 = Monetary amount 
• 3 = Decimal
65 
• 4 = Basis points 
C C N 
R 
C C Transaction - CR/IR/EQ/CO 
C if [Spread] is populated, else 
{blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
76 CDE Prices Strike price • For options other than FX options, swaptions and similar products, price at which 
the owner of an option can buy or sell the underlying asset of the option. 
• For foreign exchange options, exchange rate at which the option can be 
exercised, expressed as the rate of exchange from converting the unit currency 
into the quoted currency. In the example 0.9426 USD/EUR, USD is the unit 
currency and EUR is the quoted currency; USD 1 = EUR 0.9426. 
Where the strike price is not known when a new transaction is reported, the strike 
price is updated as it becomes available. 
• For volatility and variance swaps and similar products, the volatility strike price is 
reported in this data element. 
• Num(18,13), if Strike 
price notation = 1 
• Num(11,10), if Strike 
price notation = 3 
• Any value (e.g., USD 6.39) expressed 
as 6.39, for equity options, commodity 
options, foreign exchange options and 
similar products, if Strike price notation = 
1 
• Any value expressed as decimal (e.g., 
0.021 instead of 2.1%), for interest rate 
options, interest rate and credit 
swaptions quoted in spread, and similar 
products, if Strike price notation = 366 
C C C C C Transaction 
C if [Post-priced swap 
indicator] = ‘False’ and 
UPI.[Instrument type] = 
‘Option’, else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
77 CDE Prices Strike price 
currency/currency 
pair 
For equity options, commodity options, and similar products, currency in which the 
strike price is denominated. 
For foreign exchange options: Currency pair and order in which the strike price is 
expressed. It is expressed as unit currency/quoted currency. In the example 
0.9426 USD/EUR, USD is the unit currency and EUR is the quoted currency, USD 
1 = EUR 0.9426 
Strike price currency/currency pair is only applicable if Strike price notation = 1. 
• Char(3) 
• For foreign exchange 
options: 
Char(3)/Char(3); [Unit 
currency/Quoted 
currency] without 
restricting the currency 
pair ordering (i.e., the 
Strike price currency 
pair may be USD/EUR 
or EUR/USD). 
Currencies included in ISO 4217 
Currency codes. 
C C C C C Transaction 
C if [Strike price notation] = ‘1’, 
else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
78 CDE Prices Strike price notation Manner in which the strike price is expressed. Char(1) • 1 = Monetary amount 
• 3 = Decimal67 
C C C C C Transaction 
C if [Strike price] is populated, 
else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
79 CDE Prices Option premium 
amount 
For options and swaptions of all asset classes, monetary amount paid by the 
option buyer. 
This data element is not applicable if the instrument is not an option or does not 
embed any optionality. 
Num(25,5) Any value greater than or equal to zero. C C C C C Transaction 
C if UPI.[Instrument type] = 
‘Option’, else {blank} 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
65 The allowable values are restricted based on CFTC’s jurisdictional requirements. 66 The allowable values are restricted based on CFTC’s jurisdictional requirements. 67 The allowable values are restricted based on CFTC’s jurisdictional requirements. 
CFTC Technical Specification Version 3.2 24

## Page 38

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
Collateral 
NR 
Valuation 
NR 
80 CDE Prices Option premium 
currency 
For options and swaptions of all asset classes, currency in which the option 
premium amount is denominated. This data element is not applicable if the 
instrument is not an option or does not embed any optionality. 
Char(3) Currencies included in ISO 4217 
Currency codes. 
C C C C C Transaction 
C if [Option premium amount] > 
0, else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
81 CDE Prices Option premium 
payment date 
Unadjusted date on which the option premium is paid. YYYY-MM-DD, based 
on UTC. 
Any valid date based on ISO 8601 Date 
and time format. 
C C C C C Transaction 
C if [Option premium amount] > 
0, else {blank} 
Collateral 
NR 
Valuation 
NR 
N N 
82 CDE Prices First exercise date First unadjusted date during the exercise period in which an option can be 
exercised. 
For European-style options, this date is same as the Expiration date. For 
American-style options, the first possible exercise date is the unadjusted date 
included in the Execution timestamp. 
For knock-in options, where the first exercise date is not known when a new 
transaction is reported, the first exercise date is updated as it becomes available. 
This data element is not applicable if the instrument is not an option or does not 
embed any optionality. 
YYYY-MM-DD, based 
on UTC. 
Any valid date based on ISO 8601 Date 
and time format. 
C C C C C Transaction 
C if UPI.[Instrument type] = 
‘Option’, else {blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
83 CDE Product CDS index 
attachment point 
Defined lower point at which the level of losses in the underlying portfolio reduces 
the notional of a tranche. For example, the notional in a tranche with an attachment 
point of 3% will be reduced after 3% of losses in the portfolio have occurred. This 
data element is not applicable if the transaction is not a CDS tranche transaction 
(index or custom basket). 
Num(11,10) Any value between 0 and 1 (including 0 
and 1), expressed as decimal (e.g., 0.05 
instead of 5%). 
C N 
R 
N 
R 
N 
R 
N 
R 
Transaction - CR 
C if UPI.[ Underlier type] = 
‘Index tranche’, else {blank}; 
When populated, the value 
shall be less than the value in 
[CDS index detachment point]; 
Collateral 
NR 
Valuation 
NR 
N N 
84 CDE Product CDS index 
detachment point 
Defined point beyond which losses in the underlying portfolio no longer reduce the 
notional of a tranche. For example, the notional in a tranche with an attachment 
point of 3% and a detachment point of 6% will be reduced after there have been 
3% of losses in the portfolio. 6% losses in the portfolio deplete the notional of the 
tranche. This data element is not applicable if the transaction is not a CDS tranche 
transaction (index or custom basket). 
Num(11,10) Any value between 0 and 1 (including 0 
and 1), expressed as decimal (e.g., 0.05 
instead of 5%). 
C N 
R 
N 
R 
N 
R 
N 
R 
Transaction - CR 
C if UPI.[ Underlier type] = 
‘Index tranche’, else {blank}; 
When populated, the value 
shall be greater than the value 
N N 
CFTC Technical Specification Version 3.2 25

## Page 39

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
in [CDS index attachment 
point] 
Collateral 
NR 
Valuation 
NR 
85 CFTC Product Index factor The index version factor or percent, expressed as a decimal value, that multiplied 
by the Notional amount yields the notional amount covered by the seller of 
protection for credit default swap. 
Num(11,10) Any value between 0 and 1 (including 0 
and 1), expressed as decimal (e.g., 0.05 
instead of 5%). 
C N 
R 
N 
R 
N 
R 
N 
R 
Transaction - CR 
C if UPI Underlier type] = 
‘Index’ or ‘Index tranche’, else 
{blank} 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
86 CFTC Product Embedded option 
type 
Type of option or optional provision embedded in a contract. Char(4) • MDET = Mandatory early termination 
• OPET = Optional early termination 
• CANC = Cancelable 
• EXTD = Extendible 
• OTHR = Other 
O O O O O Transaction 
O 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
87 CFTC Product Unique product 
identifier68 
A unique set of characters that represents a particular OTC derivative. The 
Commission will designate a UPI pursuant to part 45.7. 
Char(12) ISO 4914 Unique product identifier 
A list of allowable values and their format 
will be published by the UPI issuer. 
M M M M N 
R 
Transaction – CR, IR, FX, EQ 
M 
Collateral 
NR 
Valuation – CR, IR, FX, EQ 
M 
Y Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
88 CDE Settlement Final contractual 
settlement date 
Unadjusted date as per the contract, by which all transfer of cash or assets should 
take place and the counterparties should no longer have any outstanding 
obligations to each other under that contract. 
For products that may not have a final contractual settlement date (e.g., American 
options), this data element reflects the date by which the transfer of cash or asset 
would take place if termination were to occur on the expiration date. 
YYYY-MM-DD, based 
on UTC. 
Any valid date based on ISO 8601 Date 
and time format. 
M M M M M Transaction 
M, When populated, the value 
shall be equal to or later than 
the value in [Expiration date] 
Collateral 
NR 
Valuation 
NR 
N N 
89 CDE Settlement Settlement currency 
[Settlement 
currency-Leg 1] 
Currency for the cash settlement of the transaction when applicable. Char(3) Currencies included in ISO 4217 
Currency codes. 
C C C C C Transaction 
C if UPI.[Delivery type] = 
‘Cash’, else {blank} 
N Y Validation 
Same as part 45 
(Transaction) 
68 Until the Commission designates a UPI for the commodity asset class pursuant to part 45, continue reporting product data elements according to the internal product identifier or product description used by the swap data 
repository to which the swap is reported. When the Commission designates a UPI for the commodity asset class pursuant to part 45, report the UPI. 
CFTC Technical Specification Version 3.2 26

## Page 40

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
[Settlement 
currency-Leg 2] 
For multi-currency products that do not net, the settlement currency of each leg. 
This data element is not applicable for physically settled products (e.g., physically 
settled swaptions). 
Collateral 
NR 
Valuation 
NR 
Dissemination 
Disseminate 
90 CDE Settlement Settlement location Place of settlement of the transaction as stipulated in the contract. This data 
element is only applicable for transactions that involve an offshore currency (i.e. a 
currency which is not included in the ISO 4217 currency list, for example CNH). 
Char(2) ISO 3166 Country codes69 O O O O O Transaction 
O 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
91 CFTC Transaction 
related 
Allocation indicator Indicator of whether the swap transaction is intended to be allocated, will not be 
allocated, or is a post allocation transaction. 
Char(4) • POST = An indication that the 
transaction is the result of an allocation. 
• PREA = An indication that the 
transaction is to be allocated. 
• UNAL = An indication that the 
transaction is not a post-allocated 
transaction and/or is not to be allocated. 
M M M M M Transaction 
M 
Collateral 
NR 
Valuation 
NR 
N N 
92 CFTC Transaction 
related 
Non-standardized 
term indicator 
Indicator of whether the swap transaction has one or more additional term(s) or 
provision(s), other than those disseminated to the public pursuant to part 43, that 
materially affect(s) the price of the swap transaction. 
Boolean • True 
• False 
C C C C C Transaction 
C if [Cleared] = ‘N’; 
NR if [Cleared] = ‘Y’ or ‘I’ 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
93 CFTC Transaction 
related 
Block trade election 
indicator 
Indicator of whether an election has been made to report the swap transaction as a 
block transaction by the reporting counterparty or as calculated by either the swap 
data repository acting on behalf of the reporting counterparty or by using a third 
party. 
Boolean • True = an election has been made 
• False = no election has been made or 
not applicable as a block trade 
M M M M M Transaction 
M 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
94 CDE Transaction 
related 
Effective date70 Unadjusted date at which obligations under the OTC derivative transaction come 
into effect, as included in the confirmation. 
YYYY-MM-DD, based 
on UTC. 
Any valid date based on ISO 8601 Date 
and time format. 
M M M M M Transaction 
M 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
69 CFTC requires ISO country code to be reported using two-letter code (alpha-2). 70 For commodities swaps, report the pricing start date. 
CFTC Technical Specification Version 3.2 27

## Page 41

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
95 CDE Transaction 
related 
Expiration date71 Unadjusted date at which obligations under the OTC derivative transaction stop 
being effective, as included in the confirmation. Early termination does not affect 
this data element. 
YYYY-MM-DD, based 
on UTC. 
Any valid date based on ISO 8601 Date 
and time format. 
M M M M M Transaction 
M, when populated, the value 
shall be equal to or later than 
the value in [Effective date] 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
96 CDE Transaction 
related 
Execution 
timestamp 
Date and time a transaction was originally executed, resulting in the generation of 
a new UTI. This data element remains unchanged throughout the life of the UTI.72 
YYYY-MM￾DDThh:mm:ssZ, 
based on UTC73. If the 
time element is not 
required in a particular 
jurisdiction, time may 
be dropped given that 
– in the case of 
representations with 
reduced accuracy – 
ISO 8601 allows the 
complete 
representation to be 
omitted, the omission 
starting from the 
extreme right-hand 
side (in the order from 
the least to the most 
significant). 
Any valid date/time based on ISO 8601 
Date and time format. 
M M M M M Transaction 
M 
Collateral 
NR 
Valuation 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
97 CDE Transaction 
related 
Reporting 
timestamp74 
Date and time of the submission of the report to the trade repository. YYYY-MM￾DDThh:mm:ssZ, 
based on UTC. 
Any valid date/time based on ISO 8601 
Date and time format. 
M M M M M Transactions 
M, the value shall be equal to 
or later than the value in 
[Execution timestamp] 
Collateral 
M 
Valuation 
M 
Y Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Do not 
disseminate 
98 CDE Transaction 
related 
Platform identifier Identifier of the trading facility (e.g., exchange, multilateral trading facility, swap 
execution facility) on which the transaction was executed. 
Char(4) ISO 10383 Segment Market Identifier 
Code75. 
C C C C C Transaction 
C if [Cleared] = ‘N’ or ‘I’; 
N Y Validation 
71 For commodities swaps, report the pricing end date. 72 For clearing swaps, the execution timestamp is the date and time when the DCO accepts the original swap. 73 Both the date and time portion are required to be reported. 74 Reporting timestamp (#97) is recorded and reported by the submitter. 75 Where the Segment MIC does not exist, use the Operating MIC. 
CFTC Technical Specification Version 3.2 28

## Page 42

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
If no trading facility was involved in the 
transaction: 
• XOFF, for transactions in listed 
instruments 
• XXXX, for transactions in instruments 
that are not listed in any venue 
• BILT, if the reporting counterparty 
cannot determine whether the instrument 
is listed or not, as per jurisdictional 
requirements. 
NR if [Cleared] = ‘Y’ 
Collateral 
NR 
Valuation 
NR 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
99 CFTC Transaction 
related 
Prime brokerage 
transaction indicator 
Indicator of whether the swap transaction satisfies the definition of “mirror swap” or 
“trigger swap” in § 43.2(a) of the Commission’s regulations. 
Boolean • True 
• False 
C C C C C Transaction 
C if [Cleared] = ‘N’ or ‘I’; 
NR if [Cleared] = ‘Y’ 
Collateral 
NR 
N Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Disseminate 
Valuation 
NR 
100 CFTC Transaction 
related 
Prior USI (for one￾to-one and one-to￾many relations 
between 
transactions) 
Unique swap identifier (USI) assigned to the predecessor transaction that has 
given rise to the reported transaction due to a lifecycle event, in a one-to-one 
relation between transactions (e.g., in the case of a novation, when a transaction is 
terminated, and a new transaction is generated) or in a one-to-many relation 
between transactions (e.g., in clearing or if a transaction is split into several 
different transactions). 
This data element is not applicable when reporting many-to-one and many-to-many 
relations between transactions (e.g., in the case of a compression). 
Varchar(42) Refer to: CFTC USI Data Standard 
Up to 42 alphanumeric characters 
C C C C C Transaction 
C if [Action type] = ‘NEWT’ and 
([Event type] = ‘NOVA’ or 
‘CLRG’ or ‘EXER’ or ‘ALOC’ or 
‘CLAL’) and [Prior UTI (for one￾to-one and one-to-many 
relations between 
transactions)] is not populated, 
else {blank} 
N N 
Collateral 
NR 
Valuation 
NR 
101 CDE Transaction 
related 
Prior UTI (for one￾to-one and one-to￾many relations 
between 
transactions) 
UTI assigned to the predecessor transaction that has given rise to the reported 
transaction due to a lifecycle event, in a one-to-one relation between transactions 
(e.g., in the case of a novation, when a transaction is terminated, and a new 
transaction is generated) or in a one-to-many relation between transactions (e.g., 
in clearing or if a transaction is split into several different transactions). 
This data element is not applicable when reporting many-to-one and many-to-many 
relations between transactions (e.g., in the case of a compression). 
Varchar(52) ISO 23897 Unique transaction identifier 
Up to 52 alphanumeric characters 
C C C C C Transaction 
C if [Action type] = ‘NEWT’ and 
([Event type] = ‘‘NOVA’ or 
‘CLRG’ or ‘EXER’ or ‘ALOC’ or 
‘CLAL’) and [Prior USI (for one￾to-one and one-to-many 
relations between 
transactions)] is not populated, 
else {blank} 
N N 
Collateral 
NR 
Valuation 
NR 
CFTC Technical Specification Version 3.2 29

## Page 43

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
102 CFTC Transaction 
related 
Unique swap 
identifier (USI) 
The USI is a unique identifier assigned to all swap transactions which identifies the 
transaction (the swap and its counterparties) uniquely throughout its duration. It 
consists of a namespace and a transaction identifier. 
Varchar(42) Refer to: CFTC USI Data Standard76 
Up to 42 alphanumeric characters 
C C C C C Transaction 
C if [Unique transaction 
identifier (UTI)] is not 
populated, else {blank} 
Collateral 
C if [Initial margin collateral 
portfolio code] = 
‘TRANSACTIONLEVEL’ and 
[Unique transaction identifier 
(UTI)] is not populated, else 
{blank} 
Valuation 
C if [Unique transaction 
identifier (UTI)] is not 
populated, else {blank} 
Y Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Do not 
disseminate 
103 CFTC Transaction 
related 
Unique transaction 
identifier (UTI) 
A unique identifier assigned to all swap transactions which identifies the swap 
uniquely throughout its lifecycle and used for all recordkeeping and all swap data 
reporting pursuant to § 45.5. A UTI is comprised of the LEI of the generating entity 
and a unique alphanumeric code. 
Varchar(52) ISO 23897 Unique transaction identifier 
Up to 52 alphanumeric characters 
C C C C C Transaction 
C if [Unique swap identifier 
(USI)] is not populated, else 
{blank} 
Collateral 
C if [Initial margin collateral 
portfolio code] = 
‘TRANSACTIONLEVEL’ and 
[Unique swap identifier (USI)] is 
not populated, else {blank} 
Valuation 
C if [Unique swap identifier 
(USI)] is not populated, else 
{blank} 
Y Y Validation 
Same as part 45 
(Transaction) 
Dissemination 
Do not 
disseminate 
104 CFTC Transaction 
related 
Jurisdiction The jurisdiction(s) that is requiring the reporting of the swap transaction. Char(4) • CFTC = Commodity Futures Trading 
Commission 
• SECH = U.S. Securities and Exchange 
Commission 
• MIXX = Mixed 
M M M M M Transaction 
M 
Collateral 
NR 
Valuation 
NR 
Y N 
76 Throughout this Technical Specification, references to “CFTC USI Data Standard” should refer to the USI Data Standard, 
https://www.cftc.gov/sites/default/files/idc/groups/public/@swaps/documents/dfsubmission/usidatastandards100112.pdf 
CFTC Technical Specification Version 3.2 30

## Page 44

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
105 CFTC Transfer New SDR identifier Identifier of the new swap data repository where the swap transaction is transferred 
to. 
Char(20) ISO 17442 Legal Entity Identifier (LEI) 
code that is included in the LEI data as 
published by the Global LEI Foundation 
(GLEIF, www.gleif.org/). 
C C C C C Transaction 
C if [Event type] = ‘PTNG’, else 
{blank} 
Collateral 
NR 
Valuation 
NR 
N N 
106 CFTC Valuation Next floating 
reference reset date 
[Next floating 
reference reset 
date-Leg 1] 
[Next floating 
reference reset 
date-Leg 2] 
The nearest date in the future that the floating reference resets on. YYYY-MM-DD Any valid date based on ISO 8601 Date 
and time format. 
O O O O O Transaction 
NR 
Collateral 
NR 
Valuation 
O 
Y N 
107 CFTC Valuation Last floating 
reference value 
[Last floating 
reference value-Leg 
1] 
[Last floating 
reference value-Leg 
2] 
The most recent sampling of the value of the floating reference for to determine 
cash flow. Ties to Last floating reference reset date data element. 
Num(11,10) Positive and negative values expressed 
as decimal (e.g., 0.0257 instead of 
2.57%) 
O O O O O Transaction 
NR 
Collateral 
NR 
Valuation 
O 
Y N 
108 CFTC Valuation Last floating 
reference reset date 
[Last floating 
reference reset 
date-Leg 1] 
[Last floating 
reference reset 
date-Leg 2] 
The date of the most recent sampling of the floating reference to determine cash 
flow. Ties to Last floating reference value data element. 
YYYY-MM-DD Any valid date based on ISO 8601 Date 
and time format. 
O O O O O Transaction 
NR 
Collateral 
NR 
Valuation 
O 
Y N 
109 CDE Valuation Delta77 The ratio of the change in the price of an OTC derivative transaction to the change 
in the price of the underlier, at the time a new transaction is reported or when a 
change in the notional amount is reported. 
Num(25,5) Any value. C C C C C Transaction 
NR 
Collateral 
NR 
Valuation 
C if UPI.[Instrument type] = 
‘Option’, else {blank} 
Y N 
77 Delta must be reported daily regardless of whether there is a change in the value since the last reporting. 
CFTC Technical Specification Version 3.2 31

## Page 45

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
110 CDE Valuation Valuation amount78 Current value of the outstanding contract. 
Valuation amount is expressed as the exit cost of the contract or components of 
the contract, i.e., the price that would be received to sell the contract (in the market 
in an orderly transaction at the valuation date). 
Num(25,5) Any value. M M M M M Transaction 
NR 
Collateral 
NR 
Valuation 
M 
Y N 
111 CDE Valuation Valuation currency Currency in which the valuation amount is denominated. Char(3) Currencies included in ISO 4217 
Currency codes. 
M M M M M Transaction 
NR 
Collateral 
NR 
Valuation 
M 
Y N 
112 CDE Valuation Valuation method Source and method used for the valuation of the transaction by the reporting 
counterparty. 
If at least one valuation input is used that is classified as mark-to-model in 
appendix D, then the whole valuation is classified as mark-to-model. 
If only inputs are used that are classified as mark-to-market in appendix D, then the 
whole valuation is classified as mark-to-market. 
Char(4) • MTMA = Mark-to-market 
• MTMO = Mark-to-model 
• CCPV = Central counterparty’s 
valuation 
(Classification of valuation inputs are 
provided in Appendix D) 
M M M M M Transaction 
NR 
Collateral 
NR 
Valuation 
M, when populated with 
‘CCPV’, [Cleared] must be ‘Y’. 
Y N 
113 CDE Valuation Valuation 
timestamp 
Date and time of the last valuation marked to market, provided by the central 
counterparty (CCP)79 or calculated using the current or last available market price 
of the inputs. 
If for example a currency exchange rate is the basis for a transaction’s valuation, 
then the valuation timestamp reflects the moment in time that exchange rate was 
current. 
YYYY-MM￾DDThh:mm:ssZ, 
based on UTC80. If the 
time element is not 
required in a particular 
jurisdiction, time may 
be dropped given that 
– in the case of 
representations with 
reduced accuracy – 
ISO 8601 allows the 
complete 
representation to be 
omitted, the omission 
starting from the 
extreme right-hand 
side (in the order from 
the least to the most 
significant). 
Any valid date/time based on ISO 8601 
Date and time format. 
M M M M M Transaction 
NR 
Collateral 
NR 
Valuation 
M 
Y N 
78 Valuation amount must be reported daily regardless of whether there is a change in the value since the last reporting. 79 Reported by the derivatives clearing organization (DCO) for cleared swaps and by the swap dealer for uncleared swaps 80 The timestamp portion is not required to be represented for Valuation timestamp. The format must be reported as YYYY-MM-DD. 
CFTC Technical Specification Version 3.2 32

## Page 46

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
114 CFTC Collateral 
and margins 
Affiliated 
counterparty for 
margin and capital 
indicator 
Indicator of whether the current counterparty is deemed an affiliate for U.S. margin 
and capital rules (as per § 23.159). 
Boolean 
• True 
• False 
M M M M M Transaction 
NR 
Collateral 
M 
Valuation 
NR 
Y N 
115 CDE Collateral 
and margins 
Collateralisation 
category 
Indicator of whether a collateral agreement (or collateral agreements) between the 
counterparties exists (uncollateralised/partially collateralised/one-way 
collateralised/fully collateralised). This data element is provided for each 
transaction or each portfolio, depending on whether the collateralisation is 
performed at the transaction or portfolio level, and is applicable to both cleared and 
uncleared transactions. 
Char(4) • UNCL 
• PRC1 
• PRC2 
• PRCL 
• OWC1 
• OWC2 
• OWP1 
• OWP2 
• FLCL 
The names and definitions for these 
allowable values are provided in 
Appendix E 
M M M M M Transaction 
NR 
Collateral 
M81 
Valuation 
NR 
Y N 
116 CFTC Collateral 
and margins 
Initial margin 
collateral portfolio 
code 
If collateral is reported on a portfolio basis, a unique code assigned by the 
reporting counterparty to the portfolio that tracks the aggregate initial margin of a 
set of open swap transactions. This data element is not applicable if the 
collateralisation was performed on a transaction level basis, or if there is no 
collateral agreement, or if no collateral is posted or received. 
The portfolio code is required for both collateral reporting and valuation reporting in 
order to link the 2 data sets. 
Varchar(52) Up to 52 alphanumeric characters.82 M M M M M Transaction 
O83 
Collateral 
M 
Valuation 
M 
Y N 
117 CFTC Collateral 
and margins 
Portfolio containing 
non-reportable 
component indicator 
If collateral is reported on a portfolio basis, indicator of whether the collateral 
portfolio includes swap transactions exempt from reporting. 
Boolean • True 
• False 
M M M M M Transaction 
NR 
Collateral 
M 
Valuation 
NR 
Y N 
118 CDE Collateral 
and margins 
Initial margin posted 
by the reporting 
counterparty (post￾haircut) 
Monetary value of initial margin that has been posted by the reporting counterparty, 
including any margin that is in transit and pending settlement unless inclusion of 
such margin is not allowed under the jurisdictional requirements. 
Num(25,5) Any value greater than or equal to zero. C C C C C Transaction 
NR 
Collateral 
Y N 
81 The “M” in the “Part 43/45 Asset Class” column is for collateral reporting only. 82 If collateralization was performed on a transaction level basis, “TRANSACTIONLEVEL” is accepted. “NOTAPPLICABLE” is accepted if (i) collateralization was performed on a portfolio basis and there is no IM portfolio code, or (ii) it 
is a submission from a DCO. 
83 The “M” in the “Part 43/45 Asset Class” column is for collateral and valuation reporting only. 
CFTC Technical Specification Version 3.2 33

## Page 47

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
If the collateralisation is performed at portfolio level, the initial margin posted 
relates to the whole portfolio; if the collateralisation is performed for single 
transactions, the initial margin posted relates to such single transaction. 
This refers to the total current value of the initial margin after application of the 
haircut (if applicable), rather than to its daily change. 
The data element refers both to uncleared and centrally cleared transactions. For 
centrally cleared transactions, the data element does not include default fund 
contributions, nor collateral posted against liquidity provisions to the central 
counterparty, i.e., committed credit lines. 
If the initial margin posted is denominated in more than one currency, those 
amounts are converted into a single currency chosen by the reporting counterparty 
and reported as one total value. 
C if ([Collateralisation category] 
= ‘OWC1’ or ‘OWP1’ or 
‘FLCL’), else {blank}84 
Valuation 
NR 
119 CDE Collateral 
and margins 
Initial margin posted 
by the reporting 
counterparty (pre￾haircut) 
Monetary value of initial margin that has been posted by the reporting counterparty, 
including any margin that is in transit and pending settlement unless inclusion of 
such margin is not allowed under the jurisdictional requirements. 
If the collateralisation is performed at portfolio level, the initial margin posted 
Num(25,5) Any value greater than or equal to zero. C C C C C Transaction 
NR 
Collateral 
C if ([Collateralisation category] 
Y N 
relates to the whole portfolio; if the collateralisation is performed for single 
transactions, the initial margin posted relates to such single transaction. 
This refers to the total current value of the initial margin, rather than to its daily 
change. 
The data element refers both to uncleared and centrally cleared transactions. 
For centrally cleared transactions, the data element does not include default fund 
contributions, nor collateral posted against liquidity provisions to the central 
counterparty, i.e., committed credit lines. 
If the initial margin posted is denominated in more than one currency, those 
amounts are converted into a single currency chosen by the reporting counterparty 
and reported as one total value. 
= ‘OWC1’ or ‘OWP1’ or 
‘FLCL’), else {blank}85 
Valuation 
NR 
120 CDE Collateral 
and margins 
Currency of initial 
margin posted86 
Currency in which the initial margin posted is denominated. 
If the initial margin posted is denominated in more than one currency, this data 
element reflects one of those currencies into which the reporting counterparty has 
chosen to convert all the values of posted initial margins. 
Char(3) Currencies included in ISO 4217 
Currency codes. 
C C C C C Transaction 
NR 
Collateral 
C if [Initial margin posted by the 
reporting counterparty (post￾Y N 
84 In the case where collateral agreement(s) exists but no initial margin is exchanged primarily between the counterparties (e.g., because the exposure doesn’t meet the negotiated threshold) for a given portfolio, report zero until 
such time an exchange/transfer occurs. 
85 In the case where collateral agreement(s) exists but no initial margin is exchanged primarily between the counterparties (e.g., because the exposure doesn’t meet the negotiated threshold) for a given portfolio, report zero until 
such time an exchange/transfer occurs. 
86 For portfolio with multiple currencies, it must be converted in to a single currency chosen by the reporting counterparty and reported. 
CFTC Technical Specification Version 3.2 34

## Page 48

Technical Specification Validation Rules and Dissemination Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
CR
IR
FX
EQ
CO 
haircut)] or [Initial margin 
posted by the reporting 
counterparty (pre-haircut)] is 
populated, else {blank} 
Valuation 
NR 
121 CDE Collateral 
and margins 
Initial margin 
collected by the 
reporting 
counterparty (post￾haircut) 
Monetary value of initial margin that has been collected by the reporting 
counterparty, including any margin that is in transit and pending settlement unless 
inclusion of such margin is not allowed under the jurisdictional requirements. 
If the collateralisation is performed at portfolio level, the initial margin collected 
relates to the whole portfolio; if the collateralisation is performed for single 
Num(25,5) Any value greater than or equal to zero. 
87 
C C C C C Transaction 
NR 
Collateral 
C if ([Collateralisation category] 
= ‘OWC2’ or ‘OWP2’ or 
Y N 
transactions, the initial margin collected relates to such single transaction. 
This refers to the total current value of the initial margin after application of the 
haircut (if applicable), rather than to its daily change. 
The data element refers both to uncleared and centrally cleared transactions. For 
centrally cleared transactions, the data element does not include collateral 
collected by the central counterparty as part of its investment activity. 
If the initial margin collected is denominated in more than one currency, those 
amounts are converted into a single currency chosen by the reporting counterparty 
and reported as one total value. 
‘FLCL’), else {blank} 
Valuation 
NR 
122 CDE Collateral 
and margins 
Initial margin 
collected by the 
reporting 
counterparty (pre￾haircut) 
Monetary value of initial margin that has been collected by the reporting 
counterparty, including any margin that is in transit and pending settlement unless 
inclusion of such margin is not allowed under the jurisdictional requirements. 
If the collateralisation is performed at portfolio level, the initial margin collected 
relates to the whole portfolio; if the collateralisation is performed for single 
Num(25,5) Any value greater than or equal to zero. 
88 
C C C C C Transaction 
NR 
Collateral 
C if ([Collateralisation category] 
= ‘OWC2’ or ‘OWP2’ or 
Y N 
transactions, the initial margin collected relates to such single transaction. 
This refers to the total current value of the initial margin, rather than to its daily 
change. 
The data element refers both to uncleared and centrally cleared transactions. For 
centrally cleared transactions, the data element does not include collateral 
collected by the central counterparty as part of its investment activity. 
‘FLCL’), else {blank} 
Valuation 
NR 
87 In the case where collateral agreement(s) exists but no initial margin is exchanged primarily between the counterparties (e.g., because the exposure doesn’t meet the negotiated threshold) for a given portfolio, report zero until 
such time an exchange/transfer occurs. 
88 In the case where collateral agreement(s) exists but no initial margin is exchanged primarily between the counterparties (e.g., because the exposure doesn’t meet the negotiated threshold) for a given portfolio, report zero until 
such time an exchange/transfer occurs. 
CFTC Technical Specification Version 3.2 35

## Page 49

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
If the initial margin collected is denominated in more than one currency, those 
amounts are converted into a single currency chosen by the reporting counterparty 
and reported as one total value. 
123 CDE Collateral 
and margins 
Currency of initial 
margin collected89 
Currency in which the initial margin collected is denominated. 
If the initial margin collected is denominated in more than one currency, this data 
element reflects one of those currencies into which the reporting counterparty has 
chosen to convert all the values of collected initial margins. 
Char(3) Currencies included in ISO 4217 
Currency codes. 
C C C C C Transaction 
NR 
Collateral 
C if [Initial margin collected by 
the reporting counterparty 
(post-haircut)] or [Initial margin 
collected by the reporting 
counterparty (pre-haircut)] is 
populated, else {blank} 
Valuation 
NR 
Y N 
124 CFTC Collateral 
and margins 
Variation margin 
collateral portfolio 
code 
If collateral is reported on a portfolio basis, a unique code assigned by the 
reporting counterparty to the portfolio that tracks the aggregate variation margin 
related to a set of open swap transactions. This data element is not applicable if 
the collateralisation was performed on a transaction level basis, or if there is no 
collateral agreement, or if no collateral is posted or received. 
The portfolio code is required for both collateral reporting and valuation reporting in 
order to link the 2 data sets. 
Varchar(52) Up to 52 alphanumeric characters.90 M M M M M Transaction 
O91 
Collateral 
M 
Valuation 
M 
Y N 
125 CDE Collateral 
and margins 
Variation margin 
posted by the 
reporting 
counterparty (pre￾haircut)92 
Monetary value of the variation margin posted by the reporting counterparty 
(including the cash-settled one), and including any margin that is in transit and 
pending settlement unless inclusion of such margin is not allowed under the 
jurisdictional requirements. 
Contingent variation margin is not included. 
If the collateralisation is performed at portfolio level, the variation margin posted 
relates to the whole portfolio; if the collateralisation is performed for single 
transactions, the variation margin posted relates to such single transaction. 
This data element refers to the total current value of the variation margin, 
cumulated since the first reporting of variation margins posted for the 
portfolio/transaction. 
Num(25,5) Any value greater than or equal to zero. C C C C C Transaction 
NR 
Collateral 
C if ([Collateralisation category] 
= ‘PRC1’ or ‘PRCL’ or ‘OWC1’ 
or ‘OWP1’ or ‘OWP2’ or 
‘FLCL’), else {blank}93 
Valuation 
NR 
Y N 
89 For portfolio with multiple currencies, it must be converted in to a single currency chosen by the reporting counterparty and reported. 90 If collateralization was performed on a transaction level basis, “TRANSACTIONLEVEL” is accepted. “NOTAPPLICABLE” is accepted if (i) collateralization was performed on a portfolio basis and there is no VM portfolio code, or (ii) it 
is a submission from a DCO. 
91 The “M” in the “Part 43/45 Asset Class” column is for collateral and valuation reporting only. 92 This data element must be reported daily regardless of whether there is a change in the value since the last reporting. 93 In the case where collateral agreement(s) exists but no variation margin is exchanged primarily between the counterparties (e.g., because the exposure doesn’t meet the negotiated threshold) for a given portfolio, report zero 
until such time an exchange/transfer occurs. 
CFTC Technical Specification Version 3.2 36

## Page 50

Technical Specification Validation Rules and Dissemination Rules 
P43/P45 
Asset Class 
Part 45 SDR 
Validation Rules 
P45 End of Day
P43 Reported
Part 43 SDR 
Validation 
and 
Dissemina￾tion Rules 
# 
Source
Category Data Element 
Name Definition for Data Element Format Allowable Values 
CR
IR
FX
EQ
CO 
If the variation margin posted is denominated in more than one currency, those 
amounts are converted into a single currency chosen by the reporting counterparty 
and reported as one total value. 
126 CDE Collateral 
and margins 
Currency of 
variation margin 
posted 
Currency in which the variation margin posted is denominated. 
If the variation margin posted is denominated in more than one currency, this data 
element reflects one of those currencies into which the reporting counterparty has 
chosen to convert all the values of posted variation margins. 
Char(3) Currencies included in ISO 4217 
Currency codes. 
C C C C C Transaction 
NR 
Collateral 
C if [Variation margin posted by 
the reporting counterparty (pre￾haircut)] is populated, else 
{blank} 
Valuation 
NR 
Y N 
127 CDE Collateral 
and margins 
Variation margin 
collected by the 
reporting 
counterparty (pre￾haircut)94 
Monetary value of the variation margin collected by the reporting counterparty 
(including the cash-settled one), and including any margin that is in transit and 
pending settlement unless inclusion of such margin is not allowed under the 
jurisdictional requirements. 
Contingent variation margin is not included. 
If the collateralisation is performed at portfolio level, the variation margin collected 
relates to the whole portfolio; if the collateralisation is performed for single 
transactions, the variation margin collected relates to such single transaction. 
This refers to the total current value of the variation margin, cumulated since the 
first reporting of collected variation margins for the portfolio/ transaction. 
If the variation margin collected is denominated in more than one currency, those 
amounts are converted into a single currency chosen by the reporting counterparty 
and reported as one total value. 
Num(25,5) Any value greater than or equal to zero. C C C C C Transaction 
NR 
Collateral 
C if ([Collateralisation category] 
= ‘PRC2’ or ‘PRCL’ or ‘OWC2 
or ‘OWP1’ or ‘OWP2’ or 
‘FLCL’), else {blank}95 
Valuation 
NR 
Y N 
128 CDE Collateral 
and margins 
Currency of 
variation margin 
collected 
Currency in which the variation margin collected is denominated. 
If the variation margin collected is denominated in more than one currency, this 
data element reflects one of those currencies into which the reporting counterparty 
has chosen to convert all the values of collected variation margins. 
Char(3) Currencies included in ISO 4217 
Currency codes. 
C C C C C Transaction 
NR 
Collateral 
C if [Variation margin collected 
by the reporting counterparty 
(pre- haircut)] is populated, 
else {blank} 
Valuation 
NR 
Y N 
94 This data element must be reported daily regardless of whether there is a change in the value since the last reporting. 95 In the case where collateral agreement(s) exists but no variation margin is exchanged primarily between the counterparties (e.g., because the exposure doesn’t meet the negotiated threshold) for a given portfolio, report zero 
until such time an exchange/transfer occurs. 
CFTC Technical Specification Version 3.2 37

## Page 51

Appendices for parts 43 and 45 Technical Specification 
3 Appendix 
A.Additional data elements publicly disseminated - requirements for SDRs only 
The following data elements are additional public dissemination requirements for the SDRs. 
# Category Data Element Name Definition for Data Element Format Allowable Values 
Asset Class Dissemination Rule 
CR
IR
FX
EQ
CO 
D1 Dissemination Related Dissemination identifier SDR generated unique and random identifier for each 
publicly disseminated message. 
Varchar(52) Up to 52 alphanumeric 
characters 
M M M M M 
D2 Dissemination Related Original dissemination 
identifier 
For action types other than “New”, this identifier will hold 
the Dissemination identifier of the original, publicly￾disseminated swap transaction and pricing data. 
Varchar(52) Up to 52 alphanumeric 
characters 
C C C C C C if ([Action type] = ‘CORR’ or ‘EROR’ or 
‘TERM’ or ‘REVI’ or (‘MODI’ and [Amendment 
indicator] = ‘True’)), else {blank} 
D3 Dissemination Related Dissemination timestamp Date and time, to the nearest second, that an SDR 
publicly disseminates, as defined in § 43.2. 
YYYY-MM￾DDThh:mm:ssZ, based on 
UTC 
Any valid date/time based on ISO 
8601 Date and time format. 
M M M M M 
D4 Dissemination Related UPI FISN ISO 18774 Financial Instrument Short Name issued by 
the UPI Service Provider 
Varchar(35) Valid ISO 18774 value M M M M N 
R 
D5 Dissemination Related UPI Underlier Name Name of the asset or index underlying the product 
corresponding to the UPI 
A list of allowable values and their format will be published by 
the UPI Service Provider 
M M M M N 
R 
CFTC Technical Specification Version 3.2 38

## Page 52

Appendices for parts 43 and 45 Technical Specification 
B.Notional amount 
From Revised CDE Technical Guidance – version 2: Harmonisation of critical OTC derivatives data elements (other than UTI and UPI)96, 2.70 Notional amount. 
Product Converted Amount 
Equity options and similar products Product of the strike price and the number of shares or index units 
Equity forwards and similar products Product of the forward price and the number of shares or index units 
Equity dividend swaps and similar products Product of the period fixed strike and the number of shares or index units 
Equity swaps, portfolio swaps, and similar products Product of the initial price and the number of shares or index units 
Equity variance swaps and similar products Variance amount 
Equity volatility swaps and similar products Vega notional amount 
Equity CFDs and similar products Product of the initial price and the number of shares or index units 
Commodity options and similar products Product of the strike price, and the total notional quantity 
Commodity forwards and similar products Product of the forward price and the total notional quantity 
Commodity fixed/float swaps and similar products Product of the fixed price and the total notional quantity 
Commodity basis swaps and similar products Product of the last available spot price at the time of the transaction of the underlying 
asset of the leg with no spread and the total notional quantity of the leg with no spread 
Commodity swaptions and similar products Notional amount of the underlying contract 
Commodity CFDs and similar products Product of the initial price and the total notional quantity 
Notes to the conversion table for OTC derivative transactions negotiated in non-monetary amounts: 
Note 1: for transactions where the quantity unit of measure differs from the price unit of measure, the price or total quantity is converted to a unified unit of measure.
Note 2: if applicable to the transaction, the notional amount reflects any multipliers and option entitlements. 
Note 3: for basket-type contracts, the notional amount of the transaction is the sum of the notional amounts of each constituent of the basket. 
96 Revised CDE Technical Guidance – version 2: Harmonisation of critical OTC derivatives data elements (other than UTI and UPI), https://www.leiroc.org/publications/gls/roc_20210922.pdf 
CFTC Technical Specification Version 3.2 39

## Page 53

Appendices for parts 43 and 45 Technical Specification 
C.Mapping of Day count convention allowable values to ISO 20022, FpML, and FIX/FIXML values 
From Revised CDE Technical Guidance – version 2: Harmonisation of critical OTC derivatives data elements (other than UTI and UPI)97, Annex 1, Table 4. 
Allow 
able 
value 
ISO 20022 name ISO 20022 definition98 
FIX/ 
FIXML99 
code 
value 
FIX/FIXML 
code value 
description 
FIX/FIXML definition FpML 
100 code FpML definition 
A001 IC30360ISDAor30360American 
BasicRule 
Method whereby interest is calculated based 
on a 30-day month and a 360-day year. 
Accrued interest to a value date on the last day 
of a month shall be the same as to the 30th 
calendar day of the same month, except for 
February, and provided that the interest period 
started on a 30th or a 31st. This means that a 
31st is assumed to be a 30th if the period 
started on a 30th or a 31st and the 28 Feb (or 
29 Feb for a leap year) is assumed to be the 
28th (or 29th). This is the most commonly used 
30/360 method for US straight and convertible 
bonds. 
1 30/360 
(30U/360 
Bond Basis) 
Mainly used in the United States with 
the following date adjustment rules: (1) 
If the investment is End-Of-Month and 
Date1 is the last day of February and 
Date2 is the last day of February, then 
change Date2 to 30; (2) If the 
investment is End-Of-Month and Date1 
is the last day of February, then change 
Date1 to 30;(3) If Date2 is 31 and Date1 
is 30 or 31, then change Date2 to 30;(4) 
If Date1 is 31, then change Date1 to 30. 
See also 2006 ISDA Definitions, Section 
4.16. Day Count Fraction, paragraph (f). 
[Symbolic name: ThirtyThreeSixtyUS] 
30/360 Per 2006 ISDA Definitions, Section 4.16. Day Count 
Fraction, paragraph (f) or Annex to the 2000 ISDA 
Definitions (June 2000 Version), Section 4.16. Day Count 
Fraction, paragraph (e). The number of days in the 
Calculation Period or Compounding Period in respect of 
which payment is being made divided by 360, calculated 
on a formula basis as follows: Day Count Fraction = 
[360*(Y2-Y1) + 30*(M2-M1) + (D2-D1)]/360 “D1” is the 
first calendar day, expressed as a number, of the 
Calculation Period or Compounding Period, unless such 
number would be 31, in which case D1, will be 30; and 
“D2” is the calendar day, expressed as a number, 
immediately following the last day included in the 
Calculation Period or Compounding Period, unless such 
number would be 31 and D1 is greater than 29, in which 
case D2 will be 30101 
A002 IC30365 Method whereby interest is calculated based 
on a 30-day month in a way similar to the 
30/360 (basic rule) and a 365-day year. 
Accrued interest to a value date on the last day 
of a month shall be the same as to the 30th 
calendar day of the same month, except for 
February. This means that a 31st is assumed to 
be the 30th and the 28 Feb (or 29 Feb for a 
leap year) is assumed to be the 28th (or 29th). 
97 https://www.leiroc.org/publications/gls/roc_20210922.pdf 98 The information contained in this column refers to the ISO 20022 data dictionary. 99 The source of information contained in this column is FIX Trading Community, http://fiximate.fixtrading.org/latestEP/ 100 The definitions contained herein are copyright 2006 by International Swaps and Derivatives Association, Inc. (ISDA) and reproduced by permission of ISDA. All Rights Reserved. 101 Note that the algorithm defined for this day count fraction has changed between the 2000 ISDA Definitions and 2006 ISDA Definitions. See Introduction to the 2006 ISDA Definitions for further information relating to this change. 
CFTC Technical Specification Version 3.2 40

## Page 54

Appendices for parts 43 and 45 Technical Specification 
Allow 
able 
value 
ISO 20022 name ISO 20022 definition98 
FIX/ 
FIXML99 
code 
value 
FIX/FIXML 
code value 
description 
FIX/FIXML definition FpML 
100 code FpML definition 
A003 IC30Actual Method whereby interest is calculated based 
on a 30-day month in a way similar to the 
30/360 (basic rule) and the assumed number 
of days in a year in a way similar to the 
Actual/Actual (ICMA). Accrued interest to a 
value date on the last day of a month shall be 
the same as to the 30th calendar day of the 
same month, except for February. This means 
that the 31st is assumed to be the 30th and 28 
Feb (or 29 Feb for a leap year) is assumed to 
be the 28th (or 29th). The assumed number of 
days in a year is computed as the actual 
number of days in the coupon period 
multiplied by the number of interest payments 
in the year. 
A004 Actual360 Method whereby interest is calculated based 6 Act/360 The actual number of days between ACT/360 Per 2006 ISDA Definitions, Section 4.16. Day Count 
on the actual number of accrued days in the Date1 and Date2, divided by 360. See Fraction, paragraph (e) or Annex to the 2000 ISDA 
interest period and a 360-day year. also 2006 ISDA Definitions, Section Definitions (June 2000 Version), Section 4.16. Day Count 
4.16. Day Count Fraction, paragraph (e). 
[Symbolic name: ActThreeSixty] 
Fraction, paragraph (d). 
The actual number of days in the Calculation Period or 
Compounding Period in respect of which payment is 
being made divided by 360. 
A005 Actual365Fixed Method whereby interest is calculated based 7 Act/365 The actual number of days between ACT/365 Per 2006 ISDA Definitions, Section 4.16. Day Count 
on the actual number of accrued days in the (FIXED) Date1 and Date2, divided by 365. See .FIXED Fraction, paragraph (d) or Annex to the 2000 ISDA 
interest period and a 365-day year. also 2006 ISDA Definitions, Section 
4.16. Day Count Fraction, paragraph (d). 
Definitions (June 2000 Version), Section 4.16. Day Count 
Fraction, paragraph (c). 
[Symbolic name: The actual number of days in the Calculation Period or 
ActThreeSixtyFiveFixed] Compounding Period in respect of which payment is 
being made divided by 365. 
CFTC Technical Specification Version 3.2 41

## Page 55

Appendices for parts 43 and 45 Technical Specification 
Allow 
able 
value 
ISO 20022 name ISO 20022 definition98 
FIX/ 
FIXML99 
code 
value 
FIX/FIXML 
code value 
description 
FIX/FIXML definition FpML 
100 code FpML definition 
A006 ActualActualICMA Method whereby interest is calculated based 
on the actual number of accrued days and the 
assumed number of days in a year, i.e., the 
actual number of days in the coupon period 
multiplied by the number of interest payments 
in the year. If the coupon period is irregular 
(first or last coupon), it is extended or split into 
quasi-interest periods that have the length of a 
regular coupon period and the computation is 
operated separately on each quasi-interest 
period and the intermediate results are 
summed up. 
9 Act/Act 
(ICMA) 
The denominator is the actual number 
of days in the coupon period multiplied 
by the number of coupon periods in 
the year. Assumes that regular coupons 
always fall on the same day of the 
month where possible. See also 2006 
ISDA Definitions, Section 4.16. Day 
Count Fraction, paragraph (c). 
[Symbolic name: ActActICMA] 
ACT/AC 
T.ICMA 
Per 2006 ISDA Definitions, Section 4.16. Day Count 
Fraction, paragraph (c). This day count fraction code is 
applicable for transactions booked under the 2006 ISDA 
Definitions. Transactions under the 2000 ISDA Definitions 
should use the ACT/ACT.ISMA code instead. 
A fraction equal to "number of days accrued/number of 
days in year", as such terms are used in Rule 251 of the 
statutes, by-laws, rules and recommendations of the 
International Capital Markets Association (the “ICMA Rule 
Book”), calculated in accordance with Rule 251 of the 
ICMA Rule Book as applied to non-US dollar￾denominated straight and convertible bonds issued after 
31 December 1998, as though the interest coupon on a 
bond were being calculated for a coupon period 
corresponding to the Calculation Period or Compounding 
Period in respect of which payment is being made. 
A007 IC30E360orEuroBondBasismod 
el1 
Method whereby interest is calculated based 
on a 30-day month and a 360-day year. 
Accrued interest to a value date on the last day 
of a month shall be the same as to the 30th 
calendar day of the same month. This means 
that the 31st is assumed to be the 30th and 
the 28 Feb (or 29 Feb for a leap year) is 
assumed to be equivalent to 30 Feb. However, 
if the last day of the maturity coupon period is 
the last day of February, it will not be assumed 
to be the 30th. It is a variation of the 30/360 
(ICMA) method commonly used for 
eurobonds. The usage of this variation is only 
relevant when the coupon periods are 
scheduled to end on the last day of the month. 
5 30E/360 
(ISDA) 
Date adjustment rules are: (1) if Date1 
is the last day of the month, then 
change Date1 to 30; (2) if D2 is the last 
day of the month (unless Date2 is the 
maturity date and Date2 is in February), 
then change Date2 to 30. See also 2006 
ISDA Definitions, Section 4.16. Day 
Count Fraction, paragraph (h). 
[Symbolic name: ThirtyEThreeSixtyISDA] 
30E/360 
.ISDA 
Per 2006 ISDA Definitions, Section 4.16. Day Count 
Fraction, paragraph (h). Note the algorithm for this day 
count fraction under the 2006 ISDA Definitions is 
designed to yield the same results in practice as the 
version of the 30E/360 day count fraction defined in the 
2000 ISDA Definitions. See Introduction to the 2006 ISDA 
Definitions for further information relating to this change. 
The number of days in the Calculation Period or 
Compounding Period in respect of which payment is 
being made divided by 360, calculated on a formula basis 
as follows: Day Count Fraction = [360*(Y2-Y1) + 30*(M2-
M1) + (D2-D1)]/360. “D1” is the first calendar day, 
expressed as a number, of the Calculation Period or 
Compounding Period, unless such number would be 31, 
in which case D1, will be 30; “D2” is the calendar day, 
expressed as a number, immediately following the last 
day included in the Calculation Period or Compounding 
Period, unless such number would be 31, in which case D2 
will be 30. 
CFTC Technical Specification Version 3.2 42

## Page 56

Appendices for parts 43 and 45 Technical Specification 
Allow 
able 
value 
ISO 20022 name ISO 20022 definition98 
FIX/ 
FIXML99 
code 
value 
FIX/FIXML 
code value 
description 
FIX/FIXML definition FpML 
100 code FpML definition 
A008 ActualActualISDA Method whereby interest is calculated based 
on the actual number of accrued days of the 
interest period that fall (falling on a normal 
year, year) divided by 365, added to the actual 
number of days of the interest period that fall 
(falling on a leap year, year) divided by 366. 
11 Act/Act 
(ISDA) 
The denominator varies depending on 
whether a portion of the relevant 
calculation period falls within a leap 
year. For the portion of the calculation 
period falling in a leap year, the 
denominator is 366 and for the portion 
falling outside a leap year, the 
denominator is 365. See also 2006 ISDA 
Definitions, Section 4.16. Day Count 
Fraction, paragraph (b). 
[Symbolic name: ActActISDA] 
ACT/AC 
T.ISDA 
Per 2006 ISDA Definitions, Section 4.16. Day Count 
Fraction, paragraph (b) or Annex to the 2000 ISDA 
Definitions (June 2000 Version), Section 4.16. Day Count 
Fraction, paragraph (b). Note that going from FpML 2.0 
Recommendation to the FpML 3.0 Trial Recommendation 
the code in FpML 2.0 “ACT/365.ISDA” became 
“ACT/ACT.ISDA”. 
The actual number of days in the Calculation Period or 
Compounding Period in respect of which payment is 
being made divided by 365 (or, if any portion of that 
Calculation Period or Compounding Period falls in a leap 
year, the sum of (i) the actual number of days in that 
portion of the Calculation Period or Compounding Period 
falling in a leap year divided by 366 and (ii) the actual 
number of days in that portion of the Calculation Period 
or Compounding Period falling in a non-leap year divided 
by 365). 
A009 Actual365LorActuActubasisRul 
e 
Method whereby interest is calculated based 
on the actual number of accrued days and a 
365-day year (if the coupon payment date is 
NOT in a leap year) or a 366-day year (if the 
coupon payment date is in a leap year). 
14 Act/365L The number of days in a period equal 
to the actual number of days .The 
number of days in a year is 365, or if 
the period ends in a leap year 366. 
Used for sterling floating rate notes. 
May also be referred to as ISMA Year. 
See also 2006 ISDA Definitions, Section 
4.16. Day Count Fraction, paragraph (i). 
[Symbolic name: ActThreeSixtyFiveL] 
ACT/365 
L 
Per 2006 ISDA Definitions, Section 4.16. Day Count 
Fraction, paragraph (i). 
The actual number of days in the Calculation Period or 
Compounding Period in respect of which payment is 
being made divided by 365 (or, if the later Period End 
Date of the Calculation Period or Compounding Period 
falls in a leap year, divided by 366). 
CFTC Technical Specification Version 3.2 43

## Page 57

Appendices for parts 43 and 45 Technical Specification 
Allow 
able 
value 
ISO 20022 name ISO 20022 definition98 
FIX/ 
FIXML99 
code 
value 
FIX/FIXML 
code value 
description 
FIX/FIXML definition FpML 
100 code FpML definition 
A010 ActualActualAFB Method whereby interest is calculated based 
on the actual number of accrued days and a 
366-day year (if 29 Feb falls in the coupon 
period) or a 365-day year (if 29 Feb does not 
fall in the coupon period). If a coupon period is 
longer than one year, it is split by repetitively 
separating full year subperiods counting 
backwards from the end of the coupon period 
(a year backwards from 28 Feb being 29 Feb, if 
it exists). The first of the subperiods starts on 
the start date of the accrued interest period 
and thus is possibly shorter than a year. Then 
the interest computation is operated 
separately on each subperiod and the 
intermediate results are summed up. 
8 Act/Act 
(AFB) 
The actual number of days between 
Date1 and Date2, the denominator is 
either 365 (if the calculation period 
does not contain 29 February) or 366 (if 
the calculation period includes 29 
February). See also AFB Master 
Agreement for Financial Transactions -
Interest Rate Transactions (2004) in 
Section 4. Calculation of Fixed Amounts 
and Floating Amounts, paragraph 7 
Day Count Fraction, subparagraph (i). 
[Symbolic name: ActActAFB] 
ACT/AC 
T.AFB 
The Fixed/Floating Amount will be calculated in 
accordance with the "BASE EXACT/EXACT" day count 
fraction, as defined in the “Définitions Communes 
plusieurs Additifs Techniques” published by the 
Association Francaise des Banques in September 1994. 
The denominator is either 365 (if the calculation period 
does not contain 29 February) or 366 (if the calculation 
period includes 29 February) – where a period of longer 
than one year is involved, two or more calculations are 
made: interest is calculated for each full year, counting 
backwards from the end of the calculation period, and the 
remaining initial stub period is treated in accordance with 
the usual rule. When counting backwards for this purpose, 
if the last day of the relevant period is 28 February, the 
full year should be counted back to the previous 28 
February unless 29 February exists, in which case, 29 
February should be used. 
A011 IC30360ICMAor30360basicrule Method whereby interest is calculated based 
on a 30-day month and a 360-day year. 
Accrued interest to a value date on the last day 
of a month shall be the same as to the 30th 
calendar day of the same month, except for 
February. This means that the 31st is assumed 
to be the 30th and 28 Feb (or 29 Feb for a leap 
year) is assumed to be the 28th (or 29th). It is 
the most commonly used 30/360 method for 
non-US straight and convertible bonds issued 
before 1 January 1999. 
4 30E/360 
(Eurobond 
Basis) 
Also known as 30/360.ISMA, 30S/360, 
or Special German. Date adjustment 
rules are: (1) If Date1 falls on the 31st, 
then change it to the 30th; (2) If Date2 
falls on the 31st, then change it to the 
30th. See also 2006 ISDA Definitions, 
Section 4.16. Day Count Fraction, 
paragraph (g). 
[Symbolic name: ThirtyEThreeSixty] 
30E/360 Per 2006 ISDA Definitions, Section 4.16. Day Count 
Fraction, paragraph (g) or Annex to the 2000 ISDA 
Definitions (June 2000 Version), Section 4.16. Day Count 
Fraction, paragraph (f). Note that the algorithm defined 
for this day count fraction has changed between the 2000 
ISDA Definitions and 2006 ISDA Definitions. See 
Introduction to the 2006 ISDA Definitions for further 
information relating to this change. 
CFTC Technical Specification Version 3.2 44

## Page 58

Appendices for parts 43 and 45 Technical Specification 
Allow 
able 
value 
ISO 20022 name ISO 20022 definition98 
FIX/ 
FIXML99 
code 
value 
FIX/FIXML 
code value 
description 
FIX/FIXML definition FpML 
100 code FpML definition 
A012 IC30E2360orEurobondbasismo 
del2 
Method whereby interest is calculated based 
on a 30-day month and a 360-day year. 
Accrued interest to a value date on the last day 
of a month shall be the same as to the 30th 
calendar day of the same month, except for 
the last day of February whose day of the 
month value shall be adapted to the value of 
the first day of the interest period if the latter 
is higher and if the period is one of a regular 
schedule. This means that the 31st is assumed 
to be the 30th and 28 Feb of a non-leap year is 
assumed to be equivalent to 29 Feb when the 
first day of the interest period is the 29th, or to 
30 Feb when the first day of the interest period 
is the 30th or the 31st. The 29th day of 
February in a leap year is assumed to be 
equivalent to 30 Feb when the first day of the 
interest period is the 30th or the 31st. Similarly, 
if the coupon period starts on the last day of 
February, it is assumed to produce only one 
day of interest in February as if it was starting 
on 30 Feb when the end of the period is the 
30th or the 31st, or two days of interest in 
February when the end of the period is the 
29th, or three days of interest in February 
when it is 28 Feb of a non-leap year and the 
end of the period is before the 29th. 
A013 IC30E3360orEurobondbasismo 
del3 
Method whereby interest is calculated based 
on a 30-day month and a 360-day year. 
Accrued interest to a value date on the last day 
of a month shall be the same as to the 30th 
calendar day of the same month. This means 
that the 31st is assumed to be the 30th and 28 
Feb (or 29 Feb for a leap year) is assumed to 
be equivalent to 30 Feb. It is a variation of the 
30E/360 (or Eurobond basis) method where 
the last day of February is always assumed to 
be the 30th, even if it is the last day of the 
maturity coupon period. 
CFTC Technical Specification Version 3.2 45

## Page 59

Appendices for parts 43 and 45 Technical Specification 
Allow 
able 
value 
ISO 20022 name ISO 20022 definition98 
FIX/ 
FIXML99 
code 
value 
FIX/FIXML 
code value 
description 
FIX/FIXML definition FpML 
100 code FpML definition 
A014 Actual365NL Method whereby interest is calculated based 15 NL365 The number of days in a period equal 
on the actual number of accrued days in the 
interest period, excluding any leap day from 
to the actual number of days, with the 
exception of leap days (29 February) 
the count, and a 365-day year. which are ignored. The number of days 
in a year is 365, even in a leap year. 
[Symbolic name: NLThreeSixtyFive] 
A015 ActualActualUltimo Method whereby interest is calculated based 10 Act/Act The Act/Act (ICMA Ultimo) differs from ACT/AC The Fixed/Floating Amount will be calculated in 
on the actual number of days in the coupon (ICMA Act/Act (ICMA) method only that it T.ISMA accordance with Rule 251 of the statutes, by-laws, rules 
period divided by the actual number of days in 
the year. This method is a variation of the 
Ultimo) assumes that regular coupons always 
fall on the last day of the month. 
and recommendations of the International Securities 
Market Association, as published in April 1999, as applied 
ActualActualICMA method with the exception [Symbolic name: ActActISMAUltimo] to straight and convertible bonds issued after 31 
that it assumes that the coupon always falls on December 1998, as though the Fixed/Floating Amount 
the last day of the month. Method equal to 
ACT/ACT.ISMA in the FpML model and Act/Act 
were the interest coupon on such a bond. This day count 
fraction code is applicable for transactions booked under 
(ICMA Ultimo) in the FIX/FIXML model. the 2000 ISDA Definitions. Transactions under the 2006 
ISDA Definitions should use the ACT/ACT.ICMA code 
instead. 
A016 IC30EPlus360 Method whereby interest is calculated based 
on a 30-day month and a 360-day year. 
Accrued interest to a value date on the last day 
of a month shall be the same as to the 30th 
calendar day of the same month. This means 
that the 31st is assumed to be the 30th and 28 
13 30E+/360 Variation on 30E/360. Date adjustment 
rules: (1) If Date1 falls on the 31st, then 
change it to the 30th; (2) If Date2 falls 
on the 31st, then change it to 1 and 
increase Month2 by one, i.e., next 
month. 
Feb (or 29 Feb for a leap year) is assumed to 
be equivalent to 30 Feb. This method is a 
variation of the 30E360 method with the 
[Symbolic name: ThirtyEPlusThreeSixty] 
exception that if the coupon falls on the last 
day of the month, change it to 1 and increase 
the month by 1 (i.e., next month). Method 
equal to ThirtyEPlusThreeSixty in the FIX/FIXML 
model. 
A017 Actual364 Method whereby interest is calculated based 
on the actual number of accrued days in the 
interest period divided by 364. Method equal 
to Act364 in the FIX/FIXML model. 
17 Act/364 The actual number of days between 
Date1 and Date2, divided by 364. 
[Symbolic name: Act364] 
CFTC Technical Specification Version 3.2 46

## Page 60

Appendices for parts 43 and 45 Technical Specification 
Allow 
able 
value 
ISO 20022 name ISO 20022 definition98 
FIX/ 
FIXML99 
code 
value 
FIX/FIXML 
code value 
description 
FIX/FIXML definition FpML 
100 code FpML definition 
A018 Business252 Method whereby interest is calculated based 12 BUS/252 Used for Brazilian real swaps, which is BUS/252 The number of Business Days in the Calculation Period or 
on the actual number of business days in the 
interest period divided by 252. Usage: Brazilian 
based on business days instead of 
calendar days. The number of business 
Compounding Period in respect of which payment is 
being made divided by 252. 
Currency Swaps. Method equal to BUS/252 in days divided by 252. 
the FpML model and BusTwoFiftyTwo in the [Symbolic name: BusTwoFiftyTwo] 
FIX/FIXML model. 
A019 Actual360NL Method whereby interest is calculated based 
on the actual number of accrued days in the 
interest period, excluding any leap day from 
the count, and a 360-day year. 
16 NL360 This is the same as Act/360, with the 
exception of leap days (29 February) 
which are ignored. 
[Symbolic name: NLThreeSixty] 
A020 1/1 If parties specify the Day Count Fraction to be 0 1/1 If parties specify the Day Count 1/1 Per 2006 ISDA Definitions, Section 4.16. Day Count 
1/1 then in calculating the applicable amount, Fraction to be 1/1 then in calculating Fraction, paragraph (a) or Annex to the 2000 ISDA 
1 is simply input into the calculation as the 
relevant Day Count Fraction. See also 2006 
the applicable amount, 1 is simply 
input into the calculation as the 
Definitions (June 2000 Version), Section 4.16. Day Count 
Fraction, paragraph (a). 
ISDA Definitions, Section 4.16. Day Count relevant Day Count Fraction. See also 
Fraction, paragraph (a). 2006 ISDA Definitions, Section 4.16. 
Day Count Fraction, paragraph (a). 
[Symbolic name: OneOne] 
NARR Narrative Other method. Other FIX/FIXML code values not listed 
above and FIX/FIXML code values that 
are reserved for user extensions, in the 
range of integer values of 100 and 
higher. 
CFTC Technical Specification Version 3.2 47

## Page 61

Appendices for parts 43 and 45 Technical Specification 
D.Valuation method 
From Revised CDE Technical Guidance – version 2: Harmonisation of critical OTC derivatives data elements (other than UTI and UPI)102, 2.28 Valuation method. 
Classification of valuation inputs 
Bucket Input used Valuation method103 
1 Quoted prices in active markets for identical assets or liabilities that the entity can access at the measurement date [IFRS 
13:76/ASC 820-10-35-40]. A quoted market price in an active market provides the most reliable evidence of fair value and is 
used without adjustment to measure fair value whenever available, with limited exceptions. [IFRS 13:77/ASC 820-10-35-41] 
An active market is a market in which transactions for the asset or liability take place with sufficient frequency and volume to 
provide pricing information on an ongoing basis. [IFRS 13: Appendix A/ASC 820-10-20]. 
Mark-to-market 
2 Quoted prices for similar assets or liabilities in active markets [IFRS 13:81/ASC 820-10-35-47] (other than quoted market 
prices included within bucket 1 that are observable for the asset or liability, either directly or indirectly) 
Mark-to-market 
3 Quoted prices for identical or similar assets or liabilities in markets that are not active [IFRS 13:81/ASC 820-10-35-48(b)] 
(other than quoted market prices included within bucket 1 that are observable for the asset or liability, either directly or 
indirectly). 
Mark-to-model – historic prices from inactive 
markets should not be directly used 
4 Inputs other than quoted prices that are observable for the asset or liability, for example interest rates and yield curves 
observable at commonly quoted intervals, implied volatilities, credit spreads [IFRS 13:81/ASC 820-10-35-48(c)] (other than 
quoted market prices included within bucket 1 that are observable for the asset or liability, either directly or indirectly) 
Mark-to-market 
5 Inputs that are derived principally from or corroborated by observable market data by correlation or other means (“market￾corroborated inputs”) [IFRS 13:81/ASC 820-10-35-48(d)] (other than quoted market prices included within bucket 1 that are 
observable for the asset or liability, either directly or indirectly). 
Mark-to-model – the inputs can be derived 
“principally” from observable market data, meaning 
that unobservable inputs can be used 
6 Unobservable inputs for the asset or liability. [IFRS 13:86/ASC 820-10-35-52] 
Unobservable inputs are used to measure fair value to the extent that relevant observable inputs are not available, thereby 
allowing for situations in which there is little, if any, market activity for the asset or liability at the measurement date. An 
entity develops unobservable inputs using the best information available in the circumstances, which might include the 
entity’s own data, taking into account all information about market participant assumptions that is reasonably available. 
[IFRS 13:87-89/ASC 820-10-35-53 - 35-54A] 
Mark-to-model – unobservable inputs are used 
102 Revised CDE Technical Guidance – version 2: Harmonisation of critical OTC derivatives data elements (other than UTI and UPI), https://www.leiroc.org/publications/gls/roc_20210922.pdf 103 The classification provided in this column is independent from IFRS 13/ASC 820 and is for the sole purpose of reporting critical data elements of OTC derivative transactions. 
CFTC Technical Specification Version 3.2 48

## Page 62

Appendices for parts 43 and 45 Technical Specification 
E.Collateralisation category 
From Revised CDE Technical Guidance – version 2: Harmonisation of critical OTC derivatives data elements (other than UTI and UPI)104, 2.47 Collateralisation category. 
Value Name Definition 
UNCL Uncollateralised There is no collateral agreement between the counterparties or the collateral agreement(s) between the counterparties stipulates 
that no collateral (neither initial margin nor variation margin) has to be posted with respect to the derivative transaction. 
PRC1 Partially collateralised: Counterparty 1 only The collateral agreement(s) between the counterparties stipulates that the reporting counterparty regularly posts only variation 
margin and that the other counterparty does not post any margin with respect to the derivative transaction. 
PRC2 Partially collateralised: Counterparty 2 only The collateral agreement(s) between the counterparties stipulates that the other counterparty regularly posts only variation 
margin and that the reporting counterparty does not post any margin with respect to the derivative transaction. 
PRCL Partially collateralised The collateral agreement(s) between the counterparties stipulates that both counterparties regularly post only variation margin 
with respect to the derivative transaction. 
OWC1 One-way collateralised: Counterparty 1 only The collateral agreement(s) between the counterparties stipulates that the reporting counterparty posts the initial margin and 
regularly posts variation margin and that the other counterparty does not post any margin with respect to the derivative 
transaction. 
OWC2 One-way collateralised: Counterparty 2 only The collateral agreement(s) between the counterparties stipulates that the other counterparty posts the initial margin and 
regularly posts variation margin and that the reporting counterparty does not post any margin with respect to the derivative 
transaction. 
OWP1 One-way/partially collateralised: Counterparty 1 The collateral agreement(s) between the counterparties stipulates that the reporting counterparty posts the initial margin and 
regularly posts variation margin and that the other counterparty regularly posts only variation margin. 
OWP2 One-way/partially collateralised: Counterparty 2 The collateral agreement(s) between the counterparties stipulates that the other counterparty posts the initial margin and 
regularly posts variation margin and that the reporting counterparty regularly posts only variation margin. 
FLCL Fully collateralised The collateral agreement(s) between the counterparties stipulates that both counterparties post initial margin and regularly post 
variation margin with respect to the derivative transaction. 
104 Revised CDE Technical Guidance – version 2: Harmonisation of critical OTC derivatives data elements (other than UTI and UPI), https://www.leiroc.org/publications/gls/roc_20210922.pdf 
CFTC Technical Specification Version 3.2 49

## Page 63

Not allowed for either P45 or P43 
 
 
Appendices for parts 43 and 45 Technical Specification 
F.Events: Valid Action type and Event type combinations for part 43 and part 45 reporting 
The table below, ‘Valid Action type and Event type combinations’, displays all valid and allowable combinations for Action type [#26] and Event type [#27] allowable values. Rows list all allowable Action 
types and columns list all allowable Event types. White and gray boxes with a check symbol () indicate if the given combination is allowed for part 43 and/or part 45 reporting. All other combinations 
are expected to be rejected by the SDRs. For guidance on publicly reportable swap transactions, refer to § 43.2 (a). 
Action type & 
Event type 
combinations 
Event Type 
Trade 
(TRAD) 
Novation 
(NOVA) 
Compression 
or Risk 
Reduction 
Exercise105 
(COMP) 
Early 
Termination 
(ETRM) 
Clearing 
(CLRG) 
Exercise 
(EXER) 
Allocation 
(ALOC) 
Clearing 
& 
Allocation 
(CLAL) 
Credit 
Event 
(CREV) 
Transfer 
(PTNG) 
Corporate 
Event 
(CORP) 
Upgrade 
(UPDT) 
Action Type106 
New (NEWT)          107 
Modify (MODI)        
Correct (CORR) 
Terminate (TERM)         
Error (EROR) 
Revive (REVI) 
Transfer out (PRTO)108 
Valuation (VALU) 
Collateral (MARU) 


Allowed for P45 but not allowed for P43 
Allowed for both P43 and P45 
Table 7 - Valid Action type and Event type combinations 
105 This event type is allowed for P43 as some risk reduction exercises may result in a publicly reportable transaction. 106 Correct (CORR), Error (EROR), and Revive (REVI) Action types do not associate with any Event type and are allowed for both part 43 and part 45 reporting. Valuation (VALU) and Collateral (MARU) Action types also do not 
associate with any Event type and are allowed only for part 45 end-of-day reporting. 107 NEWT-UPDT is used for upgrading existing ‘exotic’, ‘complex’, or ‘non-standard’ swaps to accurately report and comply with the CFTC Technical Specification. 108 Any live or dead (terminated or expired) swap can be transferred out except for the swaps that are previously reported as an error. Once a swap is reported as 'transfer out' to a SDR no further submission is allowed to the same 
SDR for that swap unless the transaction is transferred back in to the same SDR. Combination ‘NEWT-PTNG’ should be used in this case. 
CFTC Technical Specification Version 3.2 50

## Page 64

Appendices for parts 43 and 45 Technical Specification 
1. Allowable Action type sequences 
Reporting of lifecycle event is facilitated by reporting of Action type [#26] 
and Event type [#27] combinations. The allowable action type sequence is 
established to avoid illogical submissions by the reporting counterparties. 
SDR validation rules should perform checks to ensure SDR permits certain 
action types after the last action type has been reported. If a submission is 
reported with an action type that is not possible based on the last action 
type submission, the validation rule must reject that submission. What 
action types are allowed is depicted in 2 separate flow diagrams for part 
45 reporting (Figure 1) and part 43 reporting (Figure 2). 
PART 45 REPORTING: PERMITTED ACTION TYPE SEQUENCES FOR LIFECYCLE 
REPORTING 
• If a swap is in an open state, certain action types are permitted as 
depicted in the diagram: MODI, CORR, VALU, MARU, PRTO, EROR, and 
TERM. 
• If a swap is in a terminated state, certain action types are permitted as 
depicted in the diagram: MODI, CORR, VALU, MARU, EROR, and REVI. 
• If a swap is in an errored state, only REVI action type is permitted, 
• If a swap is in an expired or matured state, certain action types are 
permitted as depicted in the diagram: MODI, CORR, EROR,VALU, 
MARU. 
Figure 1 - Permitted Action type sequencs for Part 45 Reporting 
CFTC Technical Specification Version 3.2 51

## Page 65

Appendices for parts 43 and 45 Technical Specification 
PART 43 REPORTING: PERMITTED ACTION TYPE SEQUENCES FOR LIFECYCLE REPORTING 
Similar to reporting for Part 45, lifecycle event is supported by Action type [#26] and Event type [#27] 
combinations for Part 43 reporting. The allowable action types are depicted in Figure 2. 
Figure 2 - Permitted Action type sequences for Part 43 Reporting 
CFTC Technical Specification Version 3.2 52

## Page 66

Appendices for parts 43 and 45 Technical Specification 
2. Examples of allowable Action type and Event type combinations 
This section provides 15 examples of different Action type and Event type combinations for transaction reporting and daily end-of-day reporting. The examples are for illustration purposes only and 
are not an exhaustive list of all possible swap lifecycle events. They also illustrate how different actions and events are publicly disseminated by the SDR pursuant to part 43 real-time public reporting. 
Examples 1 through 13 illustrates how different lifecycle events are reported in transaction reporting. Each row represents a submission to the SDR with a sample of data elements represented for 
illustration purposes. The last 3 columns represent SDR generated data elements and are used in illustrating which submission shall be publicly disseminated by the SDR pursuant to part 43 reporting. 
Examples 14 and 15 illustrate daily end-of-day valuation and collateral reporting. These submissions are not applicable for part 43 reporting.
** The examples do not include all data elements required to be reported and only include data elements relevant to illustrate the Action type and Event type combination. 
Example 1 - New-Modify (amendment, update), Correction 
Example 2 - Error and Revive 
Example 3 - Early termination 
Example 4 - Full novation 
Example 5 - Partial novation 
Example 6 - Clearing 
Example 7 - Compression 
Example 8 - Exercise (Cash settled)
Example 9 - Exercise (Partially exercised, physically settled) 
Example 10 - Exercise (Cancellable option)
Example 11 - Allocation 
Example 12 - Credit event
Example 13 - Transfer transaction from one SDR to another SDR 
Example 14 - Daily Valuation reporting (Action type = VALU) 
Example 15 - Daily Collateral and margin reporting (Action type = MARU) 
CFTC Technical Specification Version 3.2 53

## Page 67

Appendices for parts 43 and 45 Technical Specification 
Sample scenarios for transaction reporting for life cycle events 
Example 1 - New-Modify (amendment, update), Correction 
This example illustrates how the different [Action type]-[Event type] combination is used to report changes to the previously submitted transaction. There are 3 types of changes [Update, Correction, 
and Amendment] that are explained in this example. 
Submission 1: A new transaction is reported with the unique transaction identifier, LEI1RPT0001AAAA, as New-Trade (NEWT-TRAD) combination. 
Submission 2: A mutually agreed change to the notional amount is reported as Modify-Trade (MODI-TRAD) with [Amendment indicator] = ‘True’. This is an amendment. 
Submission 3: A missing information, ‘Other payment type’, is reported as Modify-Trade (MODI-TRAD) combination with [Amendment indicator] = ‘False’. This is an update. 
Submission 4: A misreported information in ‘Other payment type’ from previous submission is corrected from “UWIN” to “UFRO” in this submission and reported with [Action type] = ‘CORR’ without an event type.
This is a correction. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event identifier 
[#29] 
Unique 
transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 1 
(reporting 
counterparty) 
[#13] 
Counterparty 
2 
[#14] 
Other 
payment 
type 
[#57] 
Dissemination 
identifier 
[#D1] 
Original 
dissemination 
identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
1 NEWT TRAD 2018-04-01T14:15:36Z LEI1RPT0001AAAA 10000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 ABCD001 2018-04-01T14:18:36Z 
2 MODI TRAD True 2018-04-02T10:22:10Z LEI1RPT0001AAAA 9000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 ABCD002 ABCD001 2018-04-02T10:25:10Z 
3 MODI TRAD False 2018-04-03T15:01:02Z LEI1RPT0001AAAA 9000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 UWIN Not Disseminated 
4 CORR 2018-04-04T17:20:30Z LEI1RPT0001AAAA 9000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 UFRO ABCD003 ABCD001 2018-04-04T17:24:30Z 
Table 8 – Examples of reporting of New, Modify, and Correction transaction 
Example 2 - Error and Revive 
This example illustrates how to report that the previous submission was submitted in error. This action will effectively remove the USI/UTI from the SDR’s system. 
Submission 1: A new transaction is reported with the unique transaction identifier, LEI1RPT0001BBBB, as New-Trade (NEWT-TRAD) combination. 
Submission 2: The previous transaction was submitted in error to CFTC and the removal is reported with [Action type] = ‘EROR’ without any event type. 
Submission 3: The previous submission was a mistake and transaction should be submitted to CFTC and the revive action is reported as [Action type] = ‘REVI’ without any event type. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event identifier 
[#29] 
Unique 
transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 
1 (reporting 
counterparty) 
[#13] 
Counterparty 
2 
[#14] 
Dissemination 
identifier 
[#D1] 
Original 
dissemination 
identifier 
[#D2] 
Dissemination timestamp 
[#D3] 
1 NEWT TRAD 2018-04-01T10:15:36Z LEI1RPT0001BBBB 10000 2018-04-01T10:15:36Z LEI1RPT0001 LEI2CP0002 ABCD004 2018-04-01T10:20:36Z 
2 EROR 2018-04-02T10:30:10Z LEI1RPT0001BBBB 10000 2018-04-01T10:15:36Z LEI1RPT0001 LEI2CP0002 ABCD005 ABCD004 2018-04-02T10:34:10Z 
3 REVI 2018-04-02T11:00:00Z LEI1RPT0001BBBB 10000 2018-04-01T10:15:36Z LEI1RPT0001 LEI2CP0002 ABCD004R 2018-04-02T11:02:00Z 
Table 9 - Reporting of Error and Revive transaction 
Example 3 - Early termination 
This example illustrates how to report a transaction terminated before the scheduled end date of the transaction, [Expiration date], as agreed by the involved counterparties of the transaction. 
Submission 1: A new transaction is reported with the unique transaction identifier, LEI1RPT0001KKKK as New-Trade (NEWT-TRAD) combination. 
CFTC Technical Specification Version 3.2 54

## Page 68

Appendices for parts 43 and 45 Technical Specification 
Submission 2: The previously reported transaction is terminated and is reported as Terminate-Early termination (TERM-ETRM) combination. The [Event timestamp] captures the date and time of when the 
transaction is terminated by the reporting counterparty which will be earlier than the [Expiration date] of the transaction. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event identifier 
[#29] 
Unique transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 1 
(reporting 
counterparty) 
[#13] 
Counterparty 2 
[#14] 
Expiration 
date 
[#95] 
Disseminatio 
n identifier 
[#D1] 
Original 
dissemination 
identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
1 NEWT TRAD 2018-04-01T14:15:36Z LEI1RPT0001KKKK 10000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 2025-04-01 ABCD006 2018-04-01T14:18:36Z 
2 TERM ETRM 2019-12-12T14:57:10Z LEI1RPT0001KKKK 10000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 2025-04-01 ABCD007 ABCD006 2019-12-12T14:59:10Z 
Table 10 – Reporting of transaction terminated prior to the expiration or maturity date 
Example 4 - Full novation 
This example illustrates how full novation is reported when the reporting counterparty transfers all of its rights, liabilities, duties, and obligations under the swap to another legal party. 
Submission 1: A new transaction is reported with the unique transaction identifier, LEI1RPT0001CCCC, as New-Trade (NEWT-TRAD) combination. 
Submission 2: Reporting counterparty (LEI1RPT0001) novates the transaction to a new reporting counterparty and the original transaction, LEI1RPT0001CCCC, is now terminated and reported as Terminate￾Novation (TERM-NOVA) combination. 
Submission 3: A new transaction is reported as New-Novation (NEWT-NOVA) combination with a new unique transaction identifier, LEI3RPT0003CCCC. The UTI of the original transaction (now terminated) is 
reported in the [Prior UTI] of this transaction and a new reporting counterparty (LEI3RPT0003) is reported with this submission. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event identifier 
[#29] 
Unique transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 1 
(reporting 
counterparty) 
[#13] 
Counterparty 
2 
[#14] 
Dissemination 
identifier 
[#D1] 
Original dissemination 
identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
1 NEWT TRAD 2018-04-01T14:15:36Z LEI1RPT0001CCCC 13000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 ABCD008 2018-04-01T14:20:36Z 
2 TERM NOVA 2018-04-03T13:00:00Z LEI1RPT0001CCCC 13000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 ABCD009 ABCD008 2018-04-03T13:05:00Z 
3 NEWT NOVA 2018-04-03T13:00:00Z LEI3RPT0003CCCC LEI1RPT0001CCCC 13000 2018-04-03T13:00:00Z LEI1RPT0003 LEI2CP0002 ABCD010 2018-04-03T13:05:00Z 
Table 11 - Reporting of Full Novation transaction 
Example 5 - Partial novation 
This example illustrates how partial novation is reported when the reporting counterparty transfers part of its rights, liabilities, duties, and obligations under the swap to another legal party. 
Submission 1: A new transaction is reported with the unique transaction identifier, LEI1RPT0001DDDD as New-Trade (NEWT-TRAD) combination. 
Submission 2: Reporting counterparty (LEI1RPT0001) partially novates the transaction to a new reporting counterparty and the update to original transaction is reported as Modify-Novation (MODI-NOVA) 
combination with [Amendment indicator] = ‘True’ and a reduced notional amount of ‘8000’. The transaction continues to be active. 
Submission 3: A new transaction is reported as New-Novation (NEWT-NOVA) combination with a new unique transaction identifier, LEI3RPT0003DDDD. The original reporting counterparty (LEI1RPT0001) novated 
and transferred the obligations for the allocated amount of ‘5000’ to a new reporting counterparty (LEI3RPT0003) and the UTI of the original transaction is reported in the [Prior UTI] of this transaction. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event identifier 
[#29] 
Unique transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 1 
(reporting 
counterparty) 
[#13] 
Counterparty 
2 
[#14] 
Dissemination 
identifier 
[#D1] 
Original 
dissemination 
identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
1 NEWT TRAD 2018-04-01T12:10:10Z 
2018-04-04T14:00:10Z 
LEI1RPT0001DDDD 
LEI1RPT0001DDDD 
13000 
8000 
2018-04-01T12:10:10Z 
2018-04-01T12:10:10Z 
LEI1RPT0001 
LEI1RPT0001 
LEI2CP0002 
LEI2CP0002 
ABCD011 
ABCD012 ABCD011 
2018-04-01T12:12:10Z 
2 MODI NOVA True 2018-04-04T14:07:10Z 
3 NEWT NOVA 2018-04-04T14:00:10Z LEI3RPT0003DDDD LEI1RPT0001DDDD 5000 2018-04-04T14:00:10Z LEI3RPT0003 LEI2CP0002 ABCD013 2018-04-04T14:07:10Z 
CFTC Technical Specification Version 3.2 55

## Page 69

Appendices for parts 43 and 45 Technical Specification 
Table 12 - Reporting of Partial Novation transaction 
Example 6 - Clearing novation 
This example illustrates how original swap and clearing swaps are reported when the original swap is cleared by a derivative clearing organization. 
Submission 1: A new transaction is reported with the unique transaction identifier, LEI1RPT0001ALPHA as New-Trade (NEWT-TRAD) combination with [Cleared] = ‘I’ (intent to clear). 
Submission 2: Upon clearing acceptance, the original swap transaction is extinguished and reported as Terminate-Clearing (TERM-CLRG) combination. 
Submission 3, 4: Simultaneously, two new clearing swaps are created that replaces the original swap. These two transactions are reported as New-Clearing (NEWT-CLRG) combination by the DCO as the reporting 
counterparty and the UTI of the original swap is reported in the [Prior UTI] of these transactions. Execution timestamp of clearing swap is the time when the original swap is accepted by the DCO. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event identifier 
[#29] 
Unique transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 1 
(reporting 
counterparty) 
[#13] 
Counterparty 
2 
[#14] 
Cleared 
[#1] 
Dissemination 
identifier 
[#D1] 
Original 
dissemination 
identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
1 NEWT TRAD 2018-04-01T14:15:36Z LEI1RPT001ALPHA 10000 2018-04-01T14:15:36Z LEI1RPT001 LEI2CP002 I ABCD014 2018-04-01T14:17:36Z 
2 TERM CLRG 2018-04-01T16:00:10Z LEI1RPT001ALPHA 10000 2018-04-01T14:15:36Z LEI1RPT001 LEI2CP002 I ABCD015 ABCD014 2018-04-01T16:03:10Z 
3 NEWT CLRG 2018-04-01T16:00:10Z LEI1DCO01BETA LEI1RPT001ALPHA 10000 2018-04-01T16:00:10Z LEI1DCO LEI1RPT001 Y Not Disseminated 
4 NEWT CLRG 2018-04-01T16:00:10Z LEI1DCO01GAMMA LEI1RPT001ALPHA 10000 2018-04-01T16:00:10Z LEI1DCO LEI2CP002 Y Not Disseminated 
Table 13 - Reporting of Clearing Novation transaction 
Example 7 - Compression 
This example illustrates how transactions involved in a portfolio compression event are reported. In this case, many-to-one relations between transactions, three transactions are compressed into a 
single transaction. In order to link the pre- and post-compression transactions, Event identifier is reported instead of the prior UTI. 
Submission 1, 2 and 3: Three new transactions are reported with different unique transaction identifiers as New-Trade (NEWT-TRAD) combination. 
Submission 4, 5 and 6: All three transactions are terminated as a result of compression and are reported as Terminate-Compression (TERM-COMP) combination as separate submissions. [Event identifier] is 
reported for all terminated transactions to link with the resulted new transaction. 
Submission 7: The new compressed transaction is reported as New-Compression (NEWT-COMP) combination with a new unique transaction identifier and a new execution timestamp. The same [Event identifier] 
as the terminated pre-compression transactions is reported in this post-compression transaction to link the compression event and the notional amount is reduced as a result of compression. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event identifier 
[#29] 
Unique transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 1 
(reporting 
counterparty) 
[#13] 
Counterparty 
2 
[#14] 
Dissemination 
identifier 
[#D1] 
Original 
dissemination 
identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
1 NEWT TRAD 2018-04-01T14:15:36Z LEI1RPT0001EEE 10000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 ABCD016 2018-04-01T14:20:36Z 
2 NEWT 
NEWT 
TRAD 
TRAD 
2018-04-01T14:20:36Z 
2018-04-01T14:21:36Z 
LEI1RPT0001FFF 
LEI1RPT0001GGG 
6000 
5000 
2018-04-01T14:20:36Z 
2018-04-01T14:21:36Z 
LEI1RPT0001 
LEI1RPT0001 
LEI2CP0002 
LEI2CP0002 
ABCD017 
ABCD018 
2018-04-01T14:22:36Z 
3 2018-04-01T14:25:36Z 
4 TERM 
TERM 
COMP 
COMP 
2018-04-03T18:00:00Z 
2018-04-03T18:00:00Z 
LEI01-EVENTID1 
LEI01-EVENTID1 
LEI1RPT0001EEE 
LEI1RPT0001FFF 
10000 
6000 
2018-04-01T14:15:36Z 
2018-04-01T14:20:36Z 
LEI1RPT0001 
LEI1RPT0001 
LEI2CP0002 
LEI2CP0002 
Not Disseminated 
5 Not Disseminated 
6 TERM 
NEWT 
COMP 
COMP 
2018-04-03T18:00:00Z 
2018-04-03T18:00:00Z 
LEI01-EVENTID1 
LEIS1-EVENTID1 
LEI1RPT0001GGG 
LEI1RPT0003EFG 
5000 
16000 
2018-04-01T14:21:36Z 
2018-04-03T18:00:00Z 
LEI1RPT0001 
LEI1RPT0001 
LEI2CP0002 
LEI2CP0002 
Not Disseminated 
7 Not Disseminated 
Table 14 - Reporting of Portfolio Compression transaction 
CFTC Technical Specification Version 3.2 56

## Page 70

Appendices for parts 43 and 45 Technical Specification 
Example 8 - Exercise (Cash settled) 
This example illustrates how an exercise of cash-settled option transaction is reported. 
Submission 1: A new European style option transaction is reported with the unique transaction identifier, LEI1RPT0001HHH, as New-Trade (NEWT-TRAD) combination. 
Submission 2: When the option holder fully exercises the transaction and cash settles the transaction, it results in termination of the transaction as Terminate-Exercise (TERM-EXER) combination and no new 
transaction is created. Note that the date on the [Event timestamp] is the same as the date in [Expiration date] for a European style option. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event identifier 
[#29] 
Unique transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 1 
(reporting 
counterparty) 
[#13] 
Counterparty 2 
[#14] 
Expiration 
date 
[#95] 
Dissemination 
identifier 
[#D1] 
Original 
dissemination 
identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
1 NEWT TRAD 2018-04-01T14:15:36Z LEI1RPT0001HHH 13000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 2019-04-01 ABCD021 2018-04-01T14:19:36Z 
2 TERM EXER 2019-04-01T15:01:01Z LEI1RPT0001HHH 13000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 2019-04-01 ABCD022 ABCD021 2019-04-01T15:04:01Z 
Table 15 - Reporting of Cash Settled Exercised Option transaction 
Example 9 - Exercise (Partially exercised, physically settled) 
This example illustrates how a ‘partial exercise’ option transaction is reported. 
Submission 1: A new American style transaction is reported with the unique transaction identifier, LEI1RPT0001IIII, as New-Trade (NEWT-TRAD) combination. The underlying is a swap. 
Submission 2: When the reporting counterparty of the transaction partially (5000) exercises the option as specified in the contract of the option transaction, the existing transaction is reported with the remaining 
notional amount (11000) as Modify-Exercise (MODI-EXER) combination with [Amendment indicator] = ‘False’. Note that the option holder still holds the rights to exercise the remaining notional amount. 
Submission 3: Since the option holder exercised and entered into the transaction, a new unique transaction identifier, LEI1RPT0001IIIIEx, is reported as New-Exercise (NEWT-EXER) combination with the partially 
exercised notional amount (5000). The UTI of the previous transaction is reported in the [Prior UTI] of the new transaction. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event identifier 
[#29] 
Unique transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 
1 (reporting 
counterparty) 
[#13] 
Counterparty 
2 
[#14] 
Expiration 
date 
[#95] 
Dissemination 
identifier 
[#D1] 
Original 
dissemination 
identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
1 NEWT TRAD 2018-05-01T10:15:36Z LEI1RPT0001IIII 16000 2018-05-01T10:15:36Z LEI1RPT0001 LEI2CP0002 2021-12-30 ABCD023 2018-05-01T10:17:36Z 
2 MODI EXER False 2019-04-01T13:01:01Z LEI1RPT0001IIII 11000 2018-05-01T10:15:36Z LEI1RPT0001 LEI2CP0002 2021-12-30 Not Disseminated 
3 NEWT EXER 2019-04-01T13:01:01Z LEI1RPT0001IIIIEx LEI1RPT0001IIII 5000 2019-04-01T13:01:01Z LEI1RPT0001 LEI2CP0002 2021-12-30 ABCD024 2019-04-01T13:03:01Z 
Table 16 - Reporting of Partially Exercised Option transaction 
Example 10 - Exercise (Cancellable option) 
This example illustrates how a ‘partial exercise’ of a cancellable option (Embedded option type = CANC) is reported. 
Submission 1: A new transaction for a cancellable option ([Embedded option type] = ‘CANC’) transaction is reported with the unique transaction identifier, LEI1RPT0001JJJJ, as New-Trade (NEWT-TRAD) 
combination. 
Submission 2: When the option holder of the transaction exercises its rights specified in the contract to partially exercise the transaction for the amount of ‘4000’, the existing transaction is reported as Modify￾Exercise (MODI-EXER) combination with [Amendment indicator] = ‘False’ and the remaining notional amount of ‘12000’. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event 
identifier 
[#29] 
Unique 
transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 1 
(reporting 
counterparty) 
[#13] 
Counterparty 
2 
[#14] 
Embedded 
option 
type 
[#86] 
Dissemination 
identifier 
[#D1] 
Original 
disseminatio 
n identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
CFTC Technical Specification Version 3.2 57

## Page 71

1 
2 
NEWT 
MODI 
TRAD 
EXER False 
2018-04-01T14:15:36Z 
2019-04-01T14:34:07Z 
LEI1RPT0001JJJJ 
LEI1RPT0001JJJJ 
16000 
12000 
2018-04-01T14:15:36Z 
2018-04-01T14:15:36Z 
LEI1RPT0001 
LEI1RPT0001 
LEI2CP0002 
LEI2CP0002 
CANC 
CANC 
ABCD025 
Not Disseminat
2018-04-01T14:18:36Z 
ed 
Appendices for parts 43 and 45 Technical Specification 
Table 17 - Reporting of Cancellable Option Exercise transaction 
Example 11 - Allocation 
This example illustrates how pre- and post- ‘Allocation’ swaps are reported. 
Submission 1: A new pre-allocation transaction is reported with the unique transaction identifier, LEI1RPT0001ALPHA, as New-Trade (NEWT-TRAD) combination with [Allocation indicator] = ‘PREA’. 
Submission 2: Upon allocation by the allocation agent, the pre-allocation swap transaction is terminated as Terminate-Allocation (TERM-ALOC) combination. 
Submission 3, 4: Simultaneously, two new post allocation swap transactions are created that replaces the pre-allocation swap. These two transactions are reported as New-Allocation (NEWT-ALOC) combination
by the reporting counterparty and the UTI of the pre-allocation swap is reported in the [Prior UTI] of these transactions. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event 
identifier 
[#29] 
Unique transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 
1 (reporting 
counterparty) 
[#13] 
Counterparty 
2 
[#14] 
Allocation 
indicator 
[#91] 
Disseminatio 
n identifier 
[#D1] 
Original 
dissemination 
identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
1 NEWT TRAD 2018-04-01T14:15:36Z LEI1RPT001PREAA 10000 2018-04-01T14:15:36Z LEI1RPT001 LEIFUNDMGR PREA ABCD030 2018-04-01T14:17:36Z 
2 TERM ALOC 
ALOC 
2018-04-01T16:00:10Z 
2018-04-01T16:00:10Z 
LEI1RPT001PREAA 
LEI1RPT001POST1 LEI1RPT001PREAA 
10000 
7000 
2018-04-01T14:15:36Z 
2018-04-01T16:00:10Z 
LEI1RPT001 
LEI1RPT001 
LEIFUNDMGR 
LEI2CP00A1 
PREA 
POST 
Not Disseminated 
3 NEWT Not Disseminated 
4 NEWT ALOC 2018-04-01T16:00:10Z LEI1RPT001POST2 LEI1RPT001PREAA 3000 2018-04-01T16:00:10Z LEI1RPT001 LEI3CP00A2 POST Not Disseminated 
Table 18 - Reporting of pre- and post- Allocation transactions 
Example 12 - Credit event 
This example illustrates how attributes of transactions are reported when a credit event in a constituent (not the counterparties109) of the Credit Index transaction takes place. 
Submission 1 and 2: Two new Credit Index transactions are reported with different unique transaction identifiers, as New-Trade (NEWT-TRAD) combination. 
Submission 3 and 4: When a credit event processing for reference entity in a Credit Index transaction occurs that impacts both transactions reported in submissions 1 and 2, both transactions are reported as 
Modify-Credit event (MODI-CREV) combination with [Amendment indicator] = ‘True’. The [Event identifier] is reported to identify the credit event that triggered this change to the transaction. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event identifier 
[#29] 
Unique 
transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 1 
(reporting 
counterparty) 
[#13] 
Counterparty 
2 
[#14] 
Dissemination 
identifier 
[#D1] 
Original 
dissemination 
identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
1 NEWT TRAD 2018-04-01T14:15:36Z LEI1RPT0001LLL 20000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 ABCD019 2018-04-01T14:18:36Z 
2 NEWT TRAD 2018-04-01T15:01:30Z LEI1RPT0001MMM 18000 
20000 
2018-04-01T15:01:30Z 
2018-04-01T14:15:36Z 
LEI1RPT0001 
LEI1RPT0001 
LEI2CP0002 
LEI2CP0002 
ABCD020 
DEFAU01 ABCD019 
2018-04-01T15:05:30Z 
3 MODI CREV True 2018-12-12T15:01:02Z LEI+EVENT_ID 2018-12-12T15:02:02Z 110 LEI1RPT0001LLL 
4 MODI CREV True 2018-12-12T15:01:02Z LEI+EVENT_ID LEI1RPT0001MMM 18000 2018-04-01T15:01:30Z LEI1RPT0001 LEI2CP0002 DEFAU02 ABCD020 2018-12-12T15:02:02Z 
Table 19 - Reporting of Credit Event 
109 In the case of a corporate event of the non-reporting counterparty, the transaction should be reported as Modify-Trade (MODI-TRAD) combination. 110 For credit events, the unique identifier is typically assigned to the transaction with the entity experiencing credit event and assigned by a third party service provider. 
CFTC Technical Specification Version 3.2 58

## Page 72

Appendices for parts 43 and 45 Technical Specification 
Example 13 - Transfer transaction from one SDR to another SDR 
The first table, Table 20 - Reporting of transferred transaction to the old SDR, illustrates the transactions reported to the old SDR (before transferring to the new SDR). And the second table, Table 21 -
Reporting of transferred transaction to the new SDR, illustrates the transaction reported to the new SDR as part of the transfer process. 
Submission 1 and 2: Two records from Example 1 are shown. 
Submission 3: The reporting counterparty changes the swap data repository by informing the old SDR by reporting [Action type] = ‘PRTO’, [Event type] = ‘PTNG’ and [New SDR identifier] = ‘LEISDR2’. These 3 
value combination is an indication that this transaction (UTI) will no longer be reported, effectively removing the active transaction from the SDR. 
Submission 4: At the same time, the reporting counterparty transfers the existing transaction to the new SDR, LEISDR2, by reporting with [Action type] = ‘NEWT’ and [Event type] = ‘PTNG’. Note that the 
transaction is reported using the same UTI and same execution timestamp; in addition, all required continuation data are reported. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event identifier 
[#29] 
Unique transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 
1 (reporting 
counterparty) 
[#13] 
Counterparty 2 
[#14] 
New SDR 
identifier 
[#105] 
Dissemination 
identifier 
[#D1] 
Original 
dissemination 
identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
1 NEWT TRAD 2018-04-01T14:15:36Z LEI1RPT0001AAAA 10000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 ABCD027 2018-04-01T14:17:36Z 
2 MODI TRAD True 2018-04-02T10:22:10Z LEI1RPT0001AAAA 9000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 ABCD028 ABCD027 2018-04-02T10:26:10Z 
3 PRTO PTNG 2018-10-01T17:00:00Z LEI1RPT0001AAAA 9000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 LEISDR2 Not Disseminated 
Table 20 - Reporting of transferred transaction to the old SDR 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Amendment 
indicator 
[#28] 
Event timestamp 
[#30] 
Event identifier 
[#29] 
Unique transaction 
identifier (UTI) 
[#103] 
Prior UTI (for one-to￾one and one-to-many 
relations between 
transactions) [#101] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 
1 (reporting 
counterparty) 
[#13] 
Counterparty 2 
[#14] 
New SDR 
identifier 
[#105] 
Dissemination 
identifier 
[#D1] 
Original 
dissemination 
identifier 
[#D2] 
Dissemination 
timestamp 
[#D3] 
4 NEWT PTNG 2018-10-01T17:00:00Z LEI1RPT0001AAAA 9000 2018-04-01T14:15:36Z LEI1RPT0001 LEI2CP0002 LEISDR2 Not Disseminated 
Table 21 - Reporting of transferred transaction to the new SDR 
Sample scenarios for end of day daily reporting for valuation and collateral 
The table below lists four transactions that are used for illustrating end of day reporting of valuation and collateral. 
Submission 1 and 2: These two transactions are collateralised at the portfolio level by reporting [Collateral portfolio code] = ‘PORT001’. 
Submission 3 and 4: These two transactions are collateralised at the transaction level and do not have portfolio codes to be reported. 
Row 
Action 
type 
[#26] 
Event 
type 
[#27] 
Event timestamp 
[#30] 
Unique transaction 
identifier (UTI) 
[#103] 
Initial margin collateral 
portfolio code 
[#116] 
Variation margin 
collateral portfolio code 
[#124] 
Notional 
amount 
[#31] 
Execution timestamp 
[#96] 
Counterparty 1 
(reporting counterparty) 
[#13] 
Counterparty 2 
[#14] 
1 NEWT TRAD 2019-04-01T10:15:10Z LEI1RPT0001OOOO PORT001 VM- PORT001 10000 2019-04-01T10:15:10Z LEI1RPT0001 LEI2CP0002 
2 NEWT TRAD 2019-04-01T10:15:10Z LEI1RPT0001PPPP PORT001 VM- PORT001 12000 
13000 
2019-04-01T10:15:10Z 
2019-04-01T10:15:10Z 
LEI1RPT0001 
LEI1RPT0001 
LEI2CP0002 
3 NEWT TRAD 2019-04-01T10:15:10Z LEI1RPT0001QQQQ TRANSACTIONLEVEL TRANSACTIONLEVEL LEI3CP0003 
4 NEWT TRAD 2019-04-01T10:15:10Z LEI1RPT0001RRRR TRANSACTIONLEVEL NOTAPPLICABLE 14000 2019-04-01T10:15:10Z LEI1RPT0001 LEI3CP0003 
Table 22 - Reporting Transactions with Portfolio Codes 
Example 14 - Daily Valuation reporting (Action type = VALU) 
This example illustrates how the end of day reporting of valuation related data elements are reported to the SDR. 
CFTC Technical Specification Version 3.2 59

## Page 73

Appendices for parts 43 and 45 Technical Specification 
Submission 1 to 4: All required valuation related data elements are reported for each unique transaction identifier (UTI) using [Action type] = ‘VALU’. In addition, if a transaction is collateralised at the portfolio 
level (1 and 2), applicable portfolio code is reported using [Collateral portfolio code] = ‘PORT001’. Transactions collateralised at the transaction level (3 and 4) are reported using [Collateral portfolio code] = 
‘TRANSACTIONLEVEL’ 
Row 
Action 
type 
[#26] 
Unique transaction 
identifier (UTI) 
[#103] 
Initial margin collateral 
portfolio code 
[#116] 
Variation margin 
collateral portfolio code 
[#124] 
Valuation 
amount 
[#110] 
Valuation 
currency 
[#111] 
Valuation 
method 
[#112] 
Valuation timestamp 
[#113] 
Counterparty 1 
(reporting 
counterparty) [#13] 
Counterparty 2 
[#14] 
1 VALU LEI1RPT0001OOOO PORT001 VM- PORT001 11000 USD MTMA 2019-05-02T23:59:59Z LEI1RPT0001 LEI2CP0002 
2 VALU LEI1RPT0001PPPP 
LEI1RPT0001QQQQ 
PORT001 
TRANSACTIONLEVEL 
VM- PORT001 
TRANSACTIONLEVEL 
5000 
2500 
USD 
USD 
MTMA 
MTMO 
2019-05-02T23:59:59Z 
2019-05-02T23:59:59Z 
LEI1RPT0001 
LEI1RPT0001 
LEI2CP0002 
3 VALU LEI3CP0003 
4 VALU LEI1RPT0001RRRR TRANSACTIONLEVEL NOTAPPLICABLE 3750 USD MTMO 2019-05-02T23:59:59Z LEI1RPT0001 LEI3CP0003 
Table 23 - Reporting End of Day for Valuation 
Example 15 - Daily Collateral and margin reporting (Action type = MARU) 
This example illustrates how the end of day reporting of collateral and margin related data elements are reported to the SDR. 
Submission 1: All required collateral and margin related data elements are reported for each portfolio code at the end of the day using [Action type] = ‘MARU’. The two transactions in Table 22 - Reporting 
Transactions with Portfolio Codes that are collateralised at the portfolio level are reported as a single submission with the portfolio code. The UTIs are not reported since the two transactions are collateralised at 
the portfolio level. 
Submission 2 and 3: The two transactions in Table 22 - Reporting Transactions with Portfolio Codes that are collateralised at the transaction level are reported for each unique transaction identifier (UTI), 
LEI1RPT0001QQQQ and LEI1RPT0001RRRR, at the end of the day using [Action type] = ‘MARU’, and [Collateral portfolio code] = ‘TRANSACTIONLEVEL’. 
Row Action Type 
[#26] 
Unique transaction 
identifier (UTI) 
[#103] 
Collateralisation 
category 
[#115] 
Initial margin collateral 
portfolio code 
[#116] 
Variation margin 
collateral portfolio code 
[#124] 
Initial margin 
collected 
(post-haircut) 
[#121] 
Initial margin 
collected 
(pre-haircut) 
[#122] 
Currency of 
initial margin 
collected 
[#123] 
Variation margin 
collected (pre￾haircut) 
[#127] 
Currency of 
Variation margin 
collected 
[#128] 
Counterparty 1 
[#13] 
Counterparty 2 
[#14] 
1 MARU {blank} FLCL PORT001 VM- PORT001 100000 160000 USD 100000 USD LEI1RPT0001 LEI2CP0002 
2 MARU LEI1RPT0001QQQQ FLCL TRANSACTIONLEVEL TRANSACTIONLEVEL 100000 160000 USD 100000 USD LEI1RPT0001 LEI3CP0003 
3 MARU LEI1RPT0001RRRR FLCL TRANSACTIONLEVEL TRANSACTIONLEVEL 50000 55000 USD 0 USD LEI1RPT0001 LEI3CP0003 
Table 24 - Reporting Daily End of Day Collateral and Margin 
CFTC Technical Specification Version 3.2 60

## Page 74

Appendices for parts 43 and 45 Technical Specification 
4 References 
1. Revised CDE Technical Guidance – version 2: Harmonisation of critical OTC derivatives data elements (other than UTI and UPI), September 2021 
2. https://www.leiroc.org/publications/gls/roc_20210922.pdfCPMI IOSCO Technical Guidance: Harmonization of Unique Transaction Identifier, February 2017 
https://www.iosco.org/library/pubdocs/pdf/IOSCOPD557.pdf 
3. CPMI IOSCO Technical Guidance: Harmonisation of Unique Product Identifier, September 2017 
https://www.iosco.org/library/pubdocs/pdf/IOSCOPD580.pdf 
4. ISO 20022 Universal financial industry message scheme 
https://www.iso20022.org/ 
5. CFTC USI Data Standards, October 2012 
https://www.cftc.gov/sites/default/files/idc/groups/public/@swaps/documents/dfsubmission/usidatastandards100112.pdf 
6. CFTC Letter No. 17-16 for “privacy law identifiers”, March 2017 
http://www.cftc.gov/idc/groups/public/@lrlettergeneral/documents/letter/17-16.pdf 
7. ANNA DSB UPI Product Definitions 
https://www.anna-dsb.com/upi-product-definitions/ 
8. ISO 4914 Unique product identifier (UPI) 
https://www.iso.org/standard/80506.html 
CFTC Technical Specification Version 3.2 61

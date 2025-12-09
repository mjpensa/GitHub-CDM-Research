# jfsa otc derivatives reporting guidelines 2022

*Converted from: jfsa-otc-derivatives-reporting-guidelines-2022.pdf*

---

## Page 1

[Provisional Translation] 
The original texts of the Guidelines are prepared in Japanese, and 
this translation is only provisional. The translation is to be used 
solely as reference material to aid the understanding of the 
Guidelines and is subject to any future changes. 
Guidelines for Creating, Recordkeeping and Reporting
of Transaction Information specified in Article 4(1) of
the Cabinet Office Order on the Regulation of Over-the￾Counter Derivatives Transactions, etc.
December 2022
Financial Services Agency of Japan

## Page 2

1
Under Article 156 - 63 and Article 156 - 64 of the FIEA, Financial Instruments Clearing
Organization, etc. (meaning a Financial Instruments Clearing Organization or a Foreign
Financial Instruments Clearing Organization; the same applies hereafter) and Financial
Instruments Business Operators, etc. (Financial Instruments Business Operators or
Registered Financial Institutions; the same applies hereafter) must provide transaction
information to a Trade Repository, etc. (meaning a Trade Repository (hereinafter referred
to as the "TR" ) or Designated Foreign Trade Repository; the same applies hereafter).
In addition, under Article 156 - 65 of the FIEA, the TR must prepare and preserve
records on matters specified in Article 4, Paragraph 1 of the Cabinet Office Order with
respect to the transaction information provided by a Financial Instruments Clearing
Organization, etc. and a Financial Instruments Business Operator, etc., Financial
Institutions, etc., and report the retained transaction information to the Prime Minister.
These Guidelines provide the TR, the Financial Instruments Clearing Organization, etc.
and the Financial Instruments Business Operator, etc., with details of matters specified
in Article 4, Paragraph 1 of the Cabinet Office Order.
【Attachment 1】
"Definition and Interpretation of the matters to be reported" shows the definition and
interpretation, etc. of the matters specified in Article 4, Paragraph 1 of the Cabinet Office
Order. When reporting to TR, etc., a Financial Instruments Clearing Organization, etc.
and a Financial Instruments Business Operator, etc., are requested to check the content
of Attachment 1 "Definition and Interpretation of the matters to be reported" as necessary.
Please refer to “CFTC Technical Specification Parts 43 and 45 swap data reporting and
public dissemination requirements August 30, 2022 Version 3.1” for the items below.
“ Mapping of Day count convention allowable values to ISO 20022, FpML, and
FIX/FIXML values”, “Valuation method”, “Collateralisation category”, “Notional amount”
Please refer to the “Harmonisation of critical OTC derivatives data elements (other than
UTI and UPI) Revised CDE Technical Guidance – version 3” published by the ROC for
※ The following terms used in the text are as follows :
FIEA: Financial Instruments and Exchange Act (Act No.25 of 1948)
Cabinet Office Order: Cabinet Office Order on the Regulation of Over-the-Counter
Derivatives Transactions (Cabinet Office Order No.48 of 2012)

## Page 3

2
the“Allowable Combinations of Action/Event Type Grid.”
【Attachment 2】
For specific generation rules and methods, etc. please refer to Attachment 2: "How to
determine the generation of Unique Transaction Identifier (UTI) ".
【Treatment of Existing Transactions】
Over-the-Counter Transactions of Derivatives that were traded before the effective
date of these Guidelines (April 1, 2024) and have not matured as of the effective date
(Existing Transactions), shall be deemed to have changed in the matters prescribed in
Article 4, Paragraph 1 of the Cabinet Office Order on the effective date, and the details
stated in these Guidelines regarding the changed matters shall be updated / provided
as follows:
A. Transaction information provided or reported prior to the effective date:
Please provide the changed transaction information to the TR, etc. within 180 days from
the effective date.
*1 With respect to newly prescribed reporting matters, if you do not hold the relevant transaction information, you may
leave this matter blank. However, in order to accumulate transaction information, a Financial Instruments Clearing
Organization, etc. and a Financial Instruments Business Operator, etc. are requested to provide to TR, etc. the
transaction information on matters provisionally determined by TR, etc. on the effective date.
*2 Please provide evaluation information and collateral information at the time of provision to the TR, etc. (provided,
however, this does not preclude provision from the effective date).
B. If the maturity date is reached before the provision of the transaction information:
After the effective date, if the maturity date is reached before the provision of the
transaction information in A, it is not necessary to update and provide the transaction
information thereafter.
C. Treatment of cases where the day of the transaction (including the day when
obligations are assumed by the Financial Instruments Clearing Organization, etc.)
executed is before the effective date of when the transaction information is submitted:
A change in transaction information shall be deemed to have occurred on the effective
date, and the transaction information shall be provided to the TR, etc. by the reporting
deadline (April 3, 2024) counting from the effective date.

## Page 4

3
Established on December 9, 2022
Effective April 1, 2024

## Page 5

Definition and Interpretation of the matters to be reported
December 2022
Financial Services Agency of Japan
Attachment１

## Page 6

List of Reporting Matters
Data Element Name Source Data Element Name Source
1 Effective date CDE 39 Valuation amount CDE
2 Expiration date CDE 40 Valuation currency CDE
3 Early termination date CDE 41 Valuation timestamp CDE
4 Reporting timestamp CDE 42 Valuation method CDE
5 Execution timestamp CDE 44 Collateral portfolio indicator CDE
45 Initial margin posted by the reporting counterparty (pre-haircut) CDE
46 Initial margin posted by the reporting counterparty (post-haircut) CDE
Data Element Name Source 47 Currency of initial margin posted CDE
6 Entity responsible for reporting ESMA 48 Initial margin collected by the reporting counterparty (pre-haircut) CDE
7 Counterparty 1 (reporting counterparty) CDE 49 Initial margin collected by the reporting counterparty (post-haircut) CDE
8 Counterparty 2 CDE 50 Currency of initial margin collected CDE
9 Counterparty 2 identifier type CDE 51 Variation margin posted by the reporting counterparty (pre-haircut) CDE
10 Direction 1（Buyer/Seller） CDE 52 Variation margin posted by the reporting counterparty (post-haircut) CDE
11 Direction 2 （Payer/Receiver） CDE 53 Currency of variation margin posted CDE
12 Submitter identifier CFTC 54 Variation margin collected by the reporting counterparty (pre-haircut) CDE
13 New SDR identifier CFTC 55 Variation margin collected by the reporting counterparty (post-haircut) CDE
14 Original swap SDR identifier CFTC 56 Currency of variation margin collected CDE
57 Excess collateral posted by the reporting counterparty CDE
58 Currency of excess collateral posted CDE
Data Element Name Source 59 Excess collateral collected by the reporting counterparty CDE
15 Cleared CDE 60 Currency of excess collateral collected CDE
16 Central counterparty CDE 61 Collateralisation category CDE
17 Clearing member CDE 62 Initial margin collateral portfolio code CFTC
18 Platform identifier CDE 63 Variation margin collateral portfolio code CFTC
19 Confirmed CDE
20 Final contractual settlement date CDE Matters relating to transaction prices ;
21 Settlement currency CDE Data Element Name Source
22 Clearing account origin CFTC 64 Price CDE
23 Original swap UTI CFTC 65 Price currency CDE
24 Clearing receipt timestamp CFTC 66 Price notation CDE
25 Unique transaction identifier (UTI) CFTC 67 Price unit of measure CDE
26 Prior UTI (for one-to-one and one-to-many relations between transactions) CDE 68 Price schedules - Unadjusted effective date of the price CDE
69 Price schedules - Unadjusted end date of the price CDE
Data Element Name Source
27 Day count convention CDE 71 Fixed rate CDE
28 Payment frequency period CDE 72 Spread CDE
29 Payment frequency period multiplier CDE 73 Spread currency CDE
30 Fixing date CFTC 74 Spread notation CDE
31 Floating rate reset frequency period CFTC 75 Strike price CDE
32 Floating rate reset frequency period multiplier CFTC 76 Strike price currency/currency pair CDE
33 Other payment amount CDE 77 Strike price notation CDE
34 Other payment type CDE 78 Strike price schedules - Unadjusted effective date of the strike price CDE
35 Other payment currency CDE 79 Strike price schedules - Unadjusted end date of the strike price CDE
36 Other payment date CDE
37 Other payment payer CDE
38 Other payment receiver CDE 81 Option premium amount CDE
82 Option premium currency CDE
83 Option premium payment date CDE
84 First exercise date CDE
85 Exchange rate CDE
86 Exchange rate basis CDE
Matters relating to the date and time of executing a transaction, the date and time of evaluating a contract pertaining to a
transaction, and other matters relating to the date and time pertaining to a transaction ; Appraisal value and valuation method of contracts pertaining to transactions, and matters related to collateral and margins ;
Appraisal value and valuation method of contracts pertaining to transactions, and matters related to collateral and margins ;
Matters concerning the assumption of obligations, settlement, and identification of transactions by financial instruments clearing
organizations, etc. ;
The method of calculating the number of days in transactions, the periodicity of regular monetary payments, and other matters
related to payments ; 70 Price schedules - Price in effect between the unadjusted effective date and unadjusted end date inclusive CDE
80
Strike price schedules - Strike price in effect between the unadjusted effective date and unadjusted end date
inclusive.
CDE
1

## Page 7

List of Reporting Matters
Data Element Name Source Data Element Name Source
87 Notional amount CDE 129 Contract type ESMA
88 Call amount CDE 130 Option style ESMA
89 Put amount CDE 131 Option type ESMA
90 Notional currency CDE 132 Package identifier CDE
91 Call currency CDE 133 Package transaction price CDE
92 Put currency CDE 134 Package transaction price currency CDE
93 Quantity unit of measure CDE 135 Package transaction price notation CDE
136 Package transaction spread CDE
137 Package transaction spread currency CDE
138 Package transaction spread notation CDE
139 Package indicator CFTC
97 Total notional quantity CDE
Data Element Name Source
101 Action type CFTC
102 Event type CFTC
103 Event identifier CFTC
104 Event timestamp CFTC
Data Element Name Source
105 Index factor CFTC
106 Embedded option type CFTC
108 Delivery type ESMA
109 Asset Class ESMA
110 Underlying identification type ESMA
111 Underlying identification ESMA
112 Indicator of the underlying index ESMA
113 Name of the underlying index ESMA
114 Reference entity ESMA
115 Indicator of the floating rate ESMA
116 Name of the floating rate ESMA
117 Floating rate reference period – time period ESMA
118 Floating rate reference period – multiplier ESMA
119 Derivative based on crypto-assets ESMA
120 Maturity date of the underlying ESMA
121 Seniority（CD） ESMA
122 Series （CD) ESMA
123 Version（CD) ESMA
124 CDS index attachment point CDE
125 CDS index detachment point CDE
126 Custom basket code CDE
127 Identifier of the basket's constituents CDE
128 Basket constituent identifier source CDE
96 Notional amount schedule - unadjusted end date of the notional amount CDE
100
Notional quantity schedules - Notional quantity which becomes effective on the associated unadjusted effective
date
CDE
98 Notional quantity schedules - Unadjusted date on which the associated notional quantity becomes effective CDE
99 Notional quantity schedules - Unadjusted end date of the notional quantity CDE
CDE
Matters relating to transaction prices ;
95 Notional amount schedule - unadjusted effective date of the notional amount CDE
Whether it is a new transaction, a change, or a cancellation transaction, and other matters related to the process of transactions ;
Matters concerning types of contracts pertaining to transactions ;
Matters related to the agreed financial indicators and other subject matter of transactions ;
94 Notional amount schedule - notional amount in effect on associated effective date
※ Delta and UPI are excluded from the reporting matters as of April 1, 2024.The timing of implementation
will be determined in light of future international discussions. These two elements will be included for
reporting under matter 43 and 107, respectively. Therefore, matters 43 and 107 are omitted in the list of
matters.
※Matters and allowable values for each data elements will be revised in light of future international
discussions.
2

## Page 8

Basic view of the table
＃
Data Element Name
Enter "Leg1, Leg2" if
reporting is required for
Leg1 and Leg2 respectively.
Definition of data elements
Tolerances for each data
element
Points to note in reporting
Source of the original text where
details of matters are specified
Reference source matter
number
Content in brief Example(s)
Date
2015-07-06
(corresponds to 6 July 2015)
Date and time
2014-11-05T13:15:30Z
(corresponds to 5 November
2014, 1:15:30 pm, Coordinated
Universal time)
Up to 25 numerical
characters including up to
five decimal places
1352.67
12345678901234567890.1234
5
1234567890123456789012345
0
– 20000.25
– 0.257
Up to five numerical
characters, no decimals are
allowed
12345
123
20
Three alphanumeric
characters
USD
X1X
999
Up to 25 alphanumeric
characters
asgaGEH3268EFdsagtTRCF5
43
aaaaaaaaaa
x
Boolean characters
True
False
YYYY-MM-DDThh:mm:ssZ
Definition of data elements
Allowable values for each data
element
Basic view of the Allowable values for each data element
Format Additional Explanation
YYYY-MM-DD
YYYY = four-digit year
MM = two-digit month
DD = two-digit day
Leg1,Leg2
Varchar(25)
The length is not fixed but limited at up to 25 alphanumerical characters. No special characters are
permitted. If permitted, it would be explicitly stated in the format of the data element.
Boolean Either “True” or “False”
Num(25,5)
The length is not fixed but limited to 25 numerical characters including up to five numerical characters after
the decimal point.
Should the value have more than five digits after the decimal, reporting counterparties should round half￾up.
Num(5) The length is not fixed but limited to five numerical characters.
Char(3) The length is fixed at three alphanumeric characters.
YYYY, MM, DD as above
hh = two-digit hour (00 through 23) (am/pm NOT allowed)
mm = two-digit minute (00 through 59)
ss = two-digit second (00 through 59)
T is fixed and indicates the beginning of the time element.
Z is fixed and indicates that times are expressed in UTC (Coordinated Universal Time) and not in local
time.
Data Element Name Remarks Source
※ Abbreviations used in this guideline refers to the following documents :
CDE: Harmonisation of critical OTC derivatives data elements (other than UTI and UPI) Revised CDE Technical Guidance – version 3
CFTC: CFTC Technical Specification Parts 43 and 45 swap data reporting and public dissemination requirements August 30, 2022 Version 3.1
ESMA: Final Report Technical standards on reporting, data quality, data access and registration of Trade Repositories under EMIR REFIT 17 December 2020
※ The following terms used in the text are as follows :
FSA Notification No. 105 : Designation of Transactions and Loans Designated by the Commissioner of the Financial Services Agency Excluded from Transactions Subject to Financial Instruments
Obligation Assumption Service (FSA Notification No. 105 of 2011)
CCP：Central Counterparty.
3

## Page 9

＃
1 Effective date
Unadjusted date at which obligations under the OTC derivative transaction come into effect,
as included in the confirmation.
YYYY-MM-DD（UTC）
If the effective date is not stated in the confirmation,
report the Execution date. If the Execution date is not
stated, report the Trade Date.
Otherwise, the definition used by the internal
management of each financial institution is permitted.
CDE 2.1
2 Expiration date
Unadjusted date at which obligations under the OTC derivative transaction stop being
effective, as included in the confirmation. Early termination does not affect this data element.
YYYY-MM-DD（UTC）
If a contract is early terminated, the date of when the
early termination occurred is to be entered in the Early
termination date column, and the expiration date
determined at the time of the original execution shall
continue to be entered in the Expiration date column.
CDE 2.2
3
Early termination
date
Effective date of the early termination (expiry) of the reported transaction.
This data element is applicable if the termination of the transaction occurs prior to its maturity
due to an ex-interim decision of a counterparty (or counterparties).
Examples of early terminations (expiry) are: negotiated early termination; early termination
under an optional early termination provision (“mutual put”); novation; offsetting (netting)
transaction; option exercise; compression; early termination clause specified in the original
contract which is a callable swap (bought embedded option); mutual credit break.
YYYY-MM-DD（UTC）
Early termination includes the exercise of options
(including Swaption). This applies to cases where options
are exercisable at any time during the term, such as
American-type options. In such cases, enter the effective
date when the rights are exercised.
Offsetting (netting) transactions have the same effect as
early termination, however reporting is not required
unless the position held by the financial institution is
offsetted and cleared out.
CDE 2.3
4
Reporting
timestamp
Date and time of the submission of the report to the trade repository.
YYYY-MM-DDThh:mm:ssZ
（UTC）
System input time, data generation time, and system
connection time are to be considered as acceptable
values.
In addition, if determining the time up to the seconds is
impossible due to system restrictions, setting the
seconds to "00" shall be acceptable.
If it can be determined that the reporting date and time
are the same as the trade date, then Trade Date, may be
used as a substitute value. (If different, substitution will
not be permitted.)
CDE 2.4
5
Execution
timestamp
Date and time a transaction was originally executed, resulting in the generation of a new UTI.
This data element remains unchanged throughout the life of the UTI.
YYYY-MM-DDThh:mm:ssZ
（UTC）
System input time, data generation time, and system
connection time are to be considered as acceptable
values.
In addition, if determining the time up to the seconds is
impossible due to system restrictions, setting the
seconds to "00" shall be acceptable.
If it can be determined that the reporting date and time
are the same as the trade date, then Trade Date, may be
used as a substitute value. (If different, substitution will
not be permitted.)
CDE 2.5
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
4

## Page 10

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
6
Entity responsible
for reporting
The identifier of the financial institution that is the reporting obligation.
ISO 17442 Legal Entity
Identifier (LEI)
Char(20)
Reporting party of the trades will be determined based on
the identifier reported for "Entity responsible for reporting"
and by "Submitter identifier".
Examples of who the reporting party is:
[Case 1] Where a party to a transaction is other than a
fund (normal case)
・"Entity responsible for reporting" = Financial institution
with reporting obligation and involved in the transaction
as Counterparty 1
・"Counterparty 1 (reporting counterparty)" = Same as
above
・"Submitter identifier" = Same as above
[Case 2] Where a trading party is a fund
・"Entity responsible for reporting" = Trust Bank LEI
・"Counterparty 1 (reporting counterparty)" = Fund LEI
・"Submitter identifier" = Trust bank LEI
[Case 3] Reporting party is an agent, etc. (where a
regional bank requests the Trust Bank, etc. to report)
・"Entity responsible for reporting" = Financial institution
with reporting obligation and involved in the transaction
as Counterparty 1
・"Counterparty 1 (reporting counterparty)" = Same as
above
・"Submitter identifier" = LEI of the agent acting as the
service provider for reporting
ESMA 3
7
Counterparty 1
(reporting
counterparty)
Identifier of the counterparty to an OTC derivative transaction who is fulfilling its reporting
obligation via the report in question.
In jurisdictions where both parties must report the transaction, the identifier of Counterparty 1
always identifies the reporting counterparty.
In the case of an allocated derivative transaction executed by a fund manager on behalf of a
fund, the fund and not the fund manager is reported as the counterparty.
ISO 17442 Legal Entity
Identifier (LEI)
Char(20)
The fund reports its LEI.
CDE 2.6
5

## Page 11

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
8 Counterparty 2
Identifier of the second counterparty to an OTC derivative transaction.
In the case of an allocated derivative transaction executed by a fund manager on behalf of a
fund, the fund and not the fund manager is reported as the counterparty.
ISO 17442 Legal Entity
Identifier (LEI)
Char(20)
Varchar(72), for natural
persons who are acting as
private individuals (not
eligible for an LEI per the
ROC Statement -
Individuals Acting in a
Business Capacity).
The fund reports its LEI.
If LEI cannot be obtained, a tentative LEI is permitted.
Tentative LEI must have a unique alphanumeric string to
ensure the party can be uniquely identified.
Examples for assigning tentative LEI:
[In the case of financial institutions]
Tentative LEI = Party LEI + Counterparty BIC Code
[In the case of corporations and individuals]
Tentative LEI = Trading Party LEI + Unique
Alphanumeric Code (Control number assigned by the
financial institution, etc.)
If a fund LEI is yet to be obtained, the Trust Bank must
share a tentative LEI for the fund (Trust Bank LEI +
Unique Alphanumeric Code) with its counterparty
financial institution.
Enter the LEI of the clearing organization if the company
transacts with a clearing organization prescribed in JFSA
Notification No.105.
CDE 2.7
9
Counterparty 2
identifier type
Indicator of whether LEI was used to identify the Counterparty 2.
• True, for Legal entities
• False, for natural persons
who are acting as private
individuals (not eligible for
an LEI per the ROC
Statement - Individuals
Acting in a Business
Capacity)
Under the CDE Guidance, legal entity is to be reported
as "True" and individual as "False". However, for cases
where a tentative LEI is used to report for a legal entity, it
should be reported as "False".
CDE 2.8
10
Direction 1
（Buyer/Seller）
Indicator of whether the reporting counterparty is the buyer or the seller as determined at the
time of the transaction.
A non-exhaustive list of examples of instruments for which this data element could apply are:
• most forwards and forward-like contracts (except for foreign exchange forwards and foreign
exchange non-deliverable forwards)
• most options and option-like contracts including swaptions, caps and floors
• credit default swaps (buyer/seller of protection)
• variance, volatility and correlation swaps
• contracts for difference and spreadbets
This data element is not applicable to instrument types covered by data elements Direction 2.
Char(4)
• BYER = buyer
• SLLR = seller
CDE 2.13.1
6

## Page 12

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
11
Direction 2
（Payer/Receiver）
Leg1,Leg2
Indicator of whether the reporting counterparty is the payer or the receiver of the Leg as
determined at the time of the transaction.
A non-exhaustive list of examples of instruments for which this data element could apply are:
• most swaps and swap-like contracts including interest rate swaps, credit total return swaps,
and equity swaps (except for credit default swaps, variance, volatility, and correlation swaps)
• foreign exchange swaps, forwards, non-deliverable forwards
This data element is not applicable to instrument types covered by data elements Direction 1.
Char(4)
・MAKE = payer (for each
Leg)
・TAKE = receiver (for each
Leg)
CDE 2.13.2
12 Submitter identifier
Identifier of the entity submitting the data to the swap data repository (SDR).
The Submitter identifier will be the same as the reporting counterparty, unless they use a
third-party service provider to submit the data to SDR in which case, report the identifier of
the third-party service provider.
ISO 17442 Legal Entity
Identifier (LEI)
Char（20）
See "Entity responsible for reporting".
Applicable for central counterparty and financial
institutions.
If reporting is conducted using a platform, then the
platform is deemed to be the submitter.
CFTC 22
13 New SDR identifier Identifier of the new swap data repository where the swap transaction is transferred to.
ISO 17442 Legal Entity
Identifier (LEI)
Char（20）
If unapplicable, leave it blank. CFTC 105
14
Original swap SDR
identifier
Identifier of the swap data repository (SDR) to which the original swap was reported.
ISO 17442 Legal Entity
Identifier (LEI)
Char（20）
Applicable for central counterparty and financial
institutions.
CFTC 9
7

## Page 13

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
15 Cleared
Indicator of whether the transaction has been cleared, or is intended to be cleared, by a
central counterparty.
• Y= yes, centrally cleared,
for beta and gamma
transactions.
• N= no, not centrally
cleared.
• I= intent to clear, for alpha
transactions that are
planned to be submitted to
clearing.
"N" will be acceptable if "I" cannot be distinguished due
to system limitation.
If N or I, it is to be reported by the financial institution. If
Yes, it is to be reported by the central counterparty.
However, if the financial institution conducts a transaction
with a clearing organization prescribed in Financial
Services Agency Notification No. 105, the financial
institution must report the transaction information as a
bilateral transaction, even if it is a clearing transaction.
Examples of reporting transactions with the central
counterparty prescribed in JFSA Notification No. 105 are
as follows :
(Example : The following items are mandatory)
15 Cleared Y
16 LEI of central counterparty
17 LEI of the clearing member
22 Clearing account origin
23 Orginal swap UTI for alpha transaction
CDE 2.14
16
Central
counterparty
Identifier of the central counterparty that cleared the transaction.
This data element is not applicable if the value of the data element “Cleared” is “N” (“No, not
centrally cleared”) or “I” (“Intent to clear”).
ISO 17442 Legal Entity
Identifier (LEI)
Char(20)
Reported by central counterparty. However, when a
financial institution conducts a transaction with a central
counterparty prescribed in JFSA Notification No. 105, the
financial institution must report the transaction
information as a bilateral transaction, even if it is a
clearing transaction.
CDE 2.15
17 Clearing member
Identifier of the clearing member through which a derivative transaction was cleared at a
central counterparty.
This data element is applicable to cleared transactions under both the agency clearing model
and the principal clearing model.
• In the case of the principal clearing model, the clearing member is identified as clearing
member and also as a counterparty in both transactions resulting from clearing: (i) in the
transaction between the central counterparty and the clearing member; and (ii) in the
transaction between the clearing member and the counterparty to the original alpha
transaction.
• In the case of the agency clearing model, the clearing member is identified as clearing
member but not as the counterparty to transactions resulting from clearing. Under this model,
the counterparties are the central counterparty and the client.
This data element is not applicable if the value of the data element “Cleared” is “N” (“No, not
centrally cleared”) or “I” (“Intent to clear”).
ISO 17442 Legal Entity
Identifier (LEI)
Char(20)
Reported by central counterparty. However, when a
financial institution conducts a transaction with a central
counterparty prescribed in JFSA Notification No. 105, the
financial institution must report the transaction
information as a bilateral transaction, even if it is a
clearing transaction.
(If clearing is concentrated through a clearing broker,
report the identifiers of the clearing brokers.）
CDE 2.16
8

## Page 14

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
18 Platform identifier
Identifier of the trading facility (eg multilateral trading facility, swap execution facility) on which
the transaction was executed.
ISO 10383 Segment Market
Identifier Code (MIC)
Char(4)
If no trading facility was
involved in the transaction:
• XOFF, for transactions in
listed instruments
• XXXX, for transactions in
instruments that are not
listed in any venue
• BILT, if the reporting
counterparty cannot
determine whether the
instrument is listed or not,
as per jurisdictional
requirements.
In Japan, an electronic trading platform operator is
applicable as a swap execution facility.
This may also be applicable for reporting when facilities
in the United States and Europe are used.
The CDE and CFTC Technical Specifications definitions
include, but are not limited to, MTFs and SEFs.
Referencing to the examples used in the definition,
Japanese electronic trading platform operators will need
to be included for reporting.
CDE 2.17
19 Confirmed
For new reportable transactions (as defined by the CPMI-IOSCO Technical Guidance:
Harmonisation of the Unique Transaction Identifier), whether the Legally binding terms of an
OTC derivatives contract were documented and agreed upon (confirmed) or not
(unconfirmed). If documented and agreed, whether such confirmation was done:
• via a shared confirmation facility or platform, or a private/bilateral electronic system
(electronic);
• via a human-readable written document, such as fax, paper or manually processed e-mails
(non- electronic).
• NCNF = unconfirmed
• ECNF = electronic
• YCNF = non-electronic
In cases where it is difficult to ascertain the status of the
agreement through paper confirmation, it is acceptable to
report as non-electronic (YCNF) with agreement (DONE),
However, this will be limited to cases where the status
can be promptly confirmed post agreement.
In cases where it is already known in advance that it will
take some time before an agreement can be reached, it
is expected to be reported as unconfirmed (NCNF) and
then changed to non-electronic (YCNF) post agreement.
CDE 2.18
20
Final contractual
settlement date
Unadjusted date as per the contract, by which all transfer of cash or assets should take place
and the counterparties should no longer have any outstanding obligations to each other
under that contract.
For products that may not have a final contractual settlement date (eg American options), this
data element reflects the date by which the transfer of cash or asset would take place if
termination were to occur on the expiration date.
YYYY-MM-DD（UTC） CDE 2.19
9

## Page 15

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
21 Settlement currency Leg1,Leg2
Currency for the cash settlement of the transaction when applicable.
For multicurrency products that do not net, the settlement currency of each Leg.
This data element is not applicable for physically settled products (eg physically settled
swaptions).
ISO 4217
Char(3)
Offshore currencies are to be reported as onshore
currency.
For products denominated in multiple currencies which
do not net (i.e. currency swaps that exchange JPY and
foreign currency), reporting data must consist of two
separate records (receipt and payment).
CDE 2.20
22
Clearing account
origin
Indicator of whether the clearing member acted as principal for a house trade or an agent for
a customer trade.
• HOUS=House
• CLIE=Client
Reported by central counterparty. However, when a
financial institution conducts a transaction with a central
counterparty prescribed in JFSA Notification No. 105, the
financial institution must report the transaction
information as a bilateral transaction, even if it is a
clearing transaction.
CFTC 3
23 Original swap UTI
The unique transaction identifier (UTI) of the original swap submitted for clearing to the
derivatives clearing organization (DCO) that is replaced by clearing swaps.
Varchar(52)
UTI
Reported by central counterparty. However, when a
financial institution conducts a transaction with a central
counterparty prescribed in JFSA Notification No. 105, the
financial institution must report the transaction
information as a bilateral transaction, even if it is a
clearing transaction.
CFTC 8
24
Clearing receipt
timestamp
The date and time, expressed in UTC, the original swap was received by the derivatives
clearing organization (DCO) for clearing and recorded by the DCO’s system.
YYYY-MM-DDThh:mm:ssZ
（UTC）
Reported by central counterparty. However, when a
financial institution conducts a transaction with a central
counterparty prescribed in JFSA Notification No. 105, the
financial institution must report the transaction
information as a bilateral transaction, even if it is a
clearing transaction.
CFTC 10
25
Unique transaction
identifier (UTI)
Requiring the reporting of the UTI.
Varchar(52)
UTI
CFTC 103
10

## Page 16

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
26
Prior UTI (for one￾to-one and one-to￾many relations
between
transactions)
UTI assigned to the predecessor transaction that has given rise to the reported transaction
due to a lifecycle event, in a one-to-one relation between transactions (eg in the case of a
novation, when a transaction is terminated, and a new transaction is generated) or in a one￾to-many relation between transactions (eg in clearing or if a transaction is split into several
different transactions).
This data element is not applicable when reporting many-to-one and many-to-many relations
between transactions (eg in the case of a compression).
Varchar(52）
UTI
This is applicable to one to-many or one to-one novation
transactions.
In addition to novation, it is to be applied to new
transactions arising from the exercise of swap rights for
swaptions and clearing transactions (β and γ
transactions) reported by central counterparty.
Additionally, in the case of novation, it is to be reported in
cases where a new financial institution joins the contract
(step-in party).
However, in cases where no UTI has been assigned in
the past, or it is physically difficult to obtain the Prior UTI,
a tentative Prior UTI (unique number established by each
financial institution) may be used.
CDE 2.96
27
Day count
convention
Fixed rate day
count
convention
Leg1,Leg2
Floating rate
day count
convention
Leg1Leg2
For each Leg of the transaction, where applicable: day count convention (often also referred
to as day count fraction or day count basis or day count method) that determines how interest
payments are calculated. It is used to compute the year fraction of the calculation period, and
indicates the number of days in the calculation period divided by the number of days in the
year.
Char(4)
• A001
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
• A017
• A018
• A019
• A020
• NARR
To be reported for fixed and variable convention, and for
Leg1 and Leg2.
CDE 2.22
11

## Page 17

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
28
Payment frequency
period
Fixed rate
payment
frequency
period
Leg1,Leg 2
Floating rate
payment
frequency
period Leg
1,Leg 2
For each Leg of the transaction, where applicable: time unit associated with the frequency of
payments, eg day, week, month, year or term of the stream.
Ｃｈａｒ(4)
• DAIL = daily
• WEEK = weekly
• MNTH = monthly
• YEAR = yearly
• ADHO = ad hoc which
applies when payments are
irregular
• EXPI = payment at term
To be reported for fixed and variable convention, and for
Leg1 and Leg2.
CDE 2.23
29
Payment frequency
period multiplier
Fixed rate
payment
frequency
period
multiplier Leg
1,Leg 2
Floating rate
payment
frequency
period
multiplier Leg
1,Leg 2
For each Leg of the transaction, where applicable: number of time units (as expressed by the
payment frequency period) that determines the frequency at which periodic payment dates
occur. For example, a transaction with payments occurring every two months is represented
with a payment frequency period of “MNTH” (monthly) and a payment frequency period
multiplier of 2.
This data element is not applicable if the payment frequency period is “ADHO”. If payment
frequency period is “EXPI”, then the payment frequency period multiplier is 1. If the payment
frequency is intraday, then the payment frequency period is “DAIL” and the payment
frequency multiplier is 0.
Any value greater than or
equal to zero.
Num(3,0)
To be reported for fixed and variable convention, and for
Leg1 and Leg2.
CDE 2.24
30 Fixing date Leg1,Leg2
Describes the specific date when a non-deliverable forward as well as various types of FX
OTC options such as cash-settled options that will "fix" against a particular exchange rate,
which will be used to compute the ultimate cash settlement.
YYYY-MM-DD(UTC) CFTC 54
31
Floating rate reset
frequency period
Leg1,Leg2
For each floating Leg of the swap transaction, where applicable, time unit associated with the
frequency of resets, e.g., day, week, month, year or term of the stream.
Ｃｈａｒ(4)
・DAIL = Daily
• WEEK = Weekly
• MNTH = Monthly
• YEAR = Yearly
• ADHO = Ad hoc which
applies when payments are
irregular
• EXPI = Payment at term
CFTC 55
12

## Page 18

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
32
Floating rate reset
frequency period
multiplier
Leg1,Leg2
For each floating Leg of the swap transaction, where applicable, number of time units (as
expressed by the Floating rate reset frequency period) that determines the frequency at
which periodic payment dates for reset occur. For example, a transaction with reset
payments occurring every two months is represented with a Floating rate reset frequency
period of “MNTH” (monthly) and a Floating rate reset frequency period multiplier of 2 This
data element is not applicable if the Floating rate reset frequency period is “ADHO”.
If Floating rate reset frequency period is “EXPI”, then the Floating rate reset frequency period
multiplier is 1. If the reset frequency period is intraday, then the Floating rate reset frequency
period is “DAIL” and the Floating rate reset frequency period multiplier is 0.
Any value greater than or
equal to zero.
Num(3,0)
CFTC 56
33
Other payment
amount
Payment amounts with corresponding payment types to accommodate requirements of
transaction descriptions from different asset classes.
Num(25,5)
Exchange of principal amount is reported as both receipt
and payment.
With respect to the exchange of principal amount for
currency swaps, following is an example of how to handle
the principal amount difference arising for a Mark-to-Market
type transaction.
Example : If the initial USD principal is 1 and the spot at
execution time is 110, then the JPY principal is fixed at
110. Assuming that the interest payment period is three
months and the spot after three months is 100, the new
principal amount in U.S. dollars is 1.1, which is calculated
by dividing the fixed principal amount in yen of 110 by the
spot amount of 100, and the change in the principal amount
in U.S. dollars (0.1) shall be received and paid.
For above example the expected values would be to:
・ Report the difference as other payment amount.
・ Report "modify" and other payment type as "PEXH". Also,
report the new principal amount in notional amount.
In the above example :
Notional Amount: USD 1.1
Other payment Type: PEXH
Other payment amount: USD 0.1
CDE 2.83
13

## Page 19

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
34 Other payment type
Type of Other payment amount.
Option premium payment is not included as a payment type as premiums for option are
reported using the option premium dedicated data element.
Char(4)
• UFRO = Upfront Payment,
ie the initial payment made
by one of the counterparties
either to bring a transaction
to fair value or for any other
reason that may be the
cause of an off-market
transaction
• UWIN = Unwind or Full
termination, ie the final
settlement payment made
when a transaction is
unwound prior to its end
date; Payments that may
result due to full termination
of derivative transaction(s)
• PEXH = Principal
Exchange, ie Exchange of
notional values for cross￾currency swaps
Exchange of principal amount is to be reported as both
receipt and payment.
CDE 2.84
35
Other payment
currency
Currency in which Other payment amount is denominated.
ISO 4217
Char(3)
CDE 2.85
36 Other payment date Unadjusted date on which the other payment amount is paid. YYYY-MM-DD（UTC） CDE 2.86
14

## Page 20

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
37
Other payment
payer
Identifier of the payer of Other payment amount.
Char(20), for an LEI code
If LEI cannot be obtained, a
tentative LEI is permitted.
(Varchar(72))
[In the case of financial institutions]
Tentative LEI = Party LEI + Counterparty BIC Code
[In the case of corporations and individuals]
Tentative LEI = Trading Party LEI + Unique
Alphanumeric Code (Control number assigned by the
financial institution, etc.)
Tentative LEI must have a unique alphanumeric string to
ensure the party can be uniquely identified.The fund
reports its LEI.
CDE 2.87
38
Other payment
receiver
Identifier of the receiver of Other payment amount.
Char(20), for an LEI code
If LEI cannot be obtained, a
tentative LEI is permitted.
(Varchar(72))
[In the case of financial institutions]
Tentative LEI = Party LEI + Counterparty BIC Code
[In the case of corporations and individuals]
Tentative LEI = Trading Party LEI + Unique
Alphanumeric Code (Control number assigned by the
financial institution, etc.)
Tentative LEI must have a unique alphanumeric string to
ensure the party can be uniquely identified.The fund
reports its LEI.
CDE 2.88
39 Valuation amount Current value of the outstanding contract without applying any valuation adjustments.
Any value.
Num(25,5)
Valuation amount does not take into account the various
valuation adjustments such as CVA (Credit Valuation
Adjustment). Amount to be reported is to be the pre￾adjusted valuation amount.
CDE 2.25
40 Valuation currency Currency in which the valuation amount is denominated.
Currencies included in ISO
4217.
Char(3)
CDE 2.26
15

## Page 21

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
41
Valuation
timestamp
Date and time of the last valuation marked to market, provided by the central counterparty or
calculated using the current or last available market price of the inputs. If for example a
currency exchange rate is the basis for a transaction’s valuation, then the valuation
timestamp reflects the moment in time that exchange rate was current.
YYYY-MM-DDThh:mm:ssZ
（UTC）
Valuation time period specified by each financial
institution is permitted.
CDE 2.27
42 Valuation method
Source and method used for the valuation of the transaction by the reporting counterparty.
If at least one valuation input is used that is classified as mark-to-model, then the whole
valuation is classified as mark-to-model.
If only inputs are used that are classified as mark-to-market, then the whole valuation is
classified as mark-to-market.
Char(4)
• MTMA= mark-to-market
• MTMO= mark-to-model
• CCPV= central
counterparty’s valuation
CDE 2.28
44
Collateral portfolio
indicator
Indicator of whether the collateralisation was performed on a portfolio basis. By “on a portfolio
basis”, it is meant a set of transactions that are margined together (either on a net or a gross
basis) contrary to the scenario where the margin is calculated and posted for each individual
transaction separately.
Boolean: True or False
• True, if collateralised on a
portfolio basis
• False, if not part of a
portfolio
True, if collateralisation has been set for each parties
involved in the transaction.
Whether or not the collateralisation is set will be
assumed based on CSA agreement, however it should
also include any independently created collateral
agreements other than CSA agreement.
True, if there is a collateral agreement that covers more
than one transaction even if there is only one currently
outstanding balance.
CDE 2.29
45
Initial margin
posted by the
reporting
counterparty (pre￾haircut)
Monetary value of initial margin that has been posted by the reporting counterparty, including
any margin that is in transit and pending settlement unless inclusion of such margin is not
allowed under the jurisdictional requirements.
If the collateralisation is performed at portfolio level, the initial margin posted relates to the
whole portfolio; if the collateralisation is performed for single transactions, the initial margin
posted relates to such single transaction.
This refers to the total current value of the initial margin, rather than to its daily change. The
data element refers both to uncleared and centrally cleared transactions.
For centrally cleared transactions, the data element does not include default fund
contributions, nor collateral posted against liquidity provisions to the central counterparty, ie
committed credit lines.
If the initial margin posted is denominated in more than one currency, those amounts are
converted into a single currency chosen by the reporting counterparty and reported as one
total value.
Any value greater than or
equal to zero.
Num(25,5)
Collateral reporting shall be separate from transaction
reporting.
If the collateralisation is performed at portfolio level, then
the portfolio code and the amount of collateral (gross
amount) should be reported together at the time of
collateral reporting.
CDE 2.31
16

## Page 22

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
46
Initial margin
posted by the
reporting
counterparty (post￾haircut)
Monetary value of initial margin that has been posted by the reporting counterparty, including
any margin that is in transit and pending settlement unless inclusion of such margin is not
allowed under the jurisdictional requirements.
If the collateralisation is performed at portfolio level, the initial margin posted relates to the
whole portfolio; if the collateralisation is performed for single transactions, the initial margin
posted relates to such single transaction.
This refers to the total current value of the initial margin after application of the haircut (if
applicable), rather than to its daily change.
The data element refers both to uncleared and centrally cleared transactions. For centrally
cleared transactions, the data element does not include default fund contributions, nor
collateral posted against liquidity provisions to the central counterparty, ie committed credit
lines.
If the initial margin posted is denominated in more than one currency, those amounts are
converted into a single currency chosen by the reporting counterparty and reported as one
total value.
Any value greater than or
equal to zero.
Num(25,5)
Collateral reporting shall be separate from transaction
reporting.
If the collateralisation is performed at portfolio level, then
the portfolio code and the amount of collateral (gross
amount) should be reported together at the time of
collateral reporting.
CDE 2.32
47
Currency of initial
margin posted
Currency in which the initial margin posted is denominated.
If the initial margin posted is denominated in more than one currency, this data element
reflects one of those currencies into which the reporting counterparty has chosen to convert
all the values of posted initial margins.
Currencies included in ISO
4217.
Char(3)
CDE 2.33
48
Initial margin
collected by the
reporting
counterparty (pre￾haircut)
Monetary value of initial margin that has been collected by the reporting counterparty,
including any margin that is in transit and pending settlement unless inclusion of such margin
is not allowed under the jurisdictional requirements.
If the collateralisation is performed at portfolio level, the initial margin collected relates to the
whole portfolio; if the collateralisation is performed for single transactions, the initial margin
collected relates to such single transaction.
This refers to the total current value of the initial margin, rather than to its daily change.
The data element refers both to uncleared and centrally cleared transactions. For centrally
cleared transactions, the data element does not include collateral collected by the central
counterparty as part of its investment activity.
If the initial margin collected is denominated in more than one currency, those amounts are
converted into a single currency chosen by the reporting counterparty and reported as one
total value.
Any value greater than or
equal to zero.
Num(25,5)
Collateral reporting shall be separate from transaction
reporting.
If the collateralisation is performed at portfolio level, then
the portfolio code and the amount of collateral (gross
amount) should be reported together at the time of
collateral reporting.
CDE 2.34
17

## Page 23

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
49
Initial margin
collected by the
reporting
counterparty (post￾haircut)
Monetary value of initial margin that has been collected by the reporting counterparty,
including any margin that is in transit and pending settlement unless inclusion of such margin
is not allowed under the jurisdictional requirements.
If the collateralisation is performed at portfolio level, the initial margin collected relates to the
whole portfolio; if the collateralisation is performed for single transactions, the initial margin
collected relates to such single transaction.
This refers to the total current value of the initial margin after application of the haircut (if
applicable), rather than to its daily change.
The data element refers both to uncleared and centrally cleared transactions. For centrally
cleared transactions, the data element does not include collateral collected by the central
counterparty as part of its investment activity.
If the initial margin collected is denominated in more than one currency, those amounts are
converted into a single currency chosen by the reporting counterparty and reported as one
total value.
Any value greater than or
equal to zero.
Num(25,5)
Collateral reporting shall be separate from transaction
reporting.
If the collateralisation is performed at portfolio level, then
the portfolio code and the amount of collateral (gross
amount) should be reported together at the time of
collateral reporting.
CDE 2.35
50
Currency of initial
margin collected
Currency in which the initial margin collected is denominated.
If the initial margin collected is denominated in more than one currency, this data element
reflects one of those currencies into which the reporting counterparty has chosen to convert
all the values of collected initial margins.
Currencies included in ISO
4217.
Char(3)
CDE 2.36
51
Variation margin
posted by the
reporting
counterparty (pre￾haircut)
Monetary value of the variation margin posted by the reporting counterparty (including the
cash-settled one), and including any margin that is in transit and pending settlement unless
inclusion of such margin is not allowed under the jurisdictional requirements.
Contingent variation margin is not included.
If the collateralisation is performed at portfolio level, the variation margin posted relates to the
whole portfolio; if the collateralisation is performed for single transactions, the variation
margin posted relates to such single transaction.
This data element refers to the total current value of the variation margin, cumulated since
the first reporting of variation margins posted for the portfolio/transaction.
If the variation margin posted is denominated in more than one currency, those amounts are
converted into a single currency chosen by the reporting counterparty and reported as one
total value.
Any value greater than or
equal to zero.
Num(25,5)
Collateral reporting shall be separate from transaction
reporting.
If the collateralisation is performed at portfolio level, then
the portfolio code and the amount of collateral (gross
amount) should be reported together at the time of
collateral reporting.
CDE 2.37
18

## Page 24

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
52
Variation margin
posted by the
reporting
counterparty (post￾haircut)
Monetary value of the variation margin posted by the reporting counterparty (including the
cash-settled one), and including any margin that is in transit and pending settlement unless
inclusion of such margin is not allowed under the jurisdictional requirements.
Contingent variation margin is not included.
If the collateralisation is performed at portfolio level, the variation margin posted relates to the
whole portfolio; if the collateralisation is performed for single transactions, the variation
margin posted relates to such single transaction.
This data element refers to the total current value of the variation margin after application of
the haircut (if applicable), cumulated since the first reporting of posted variation margins for
the portfolio/transaction.
If the variation margin posted is denominated in more than one currency, those amounts are
converted into a single currency chosen by the reporting counterparty and reported as one
total value.
Any value greater than or
equal to zero.
Num(25,5)
Collateral reporting shall be separate from transaction
reporting.
If the collateralisation is performed at portfolio level, then
the portfolio code and the amount of collateral (gross
amount) should be reported together at the time of
collateral reporting.
CDE 2.38
53
Currency of
variation margin
posted
Currency in which the variation margin posted is denominated.
If the variation margin posted is denominated in more than one currency, this data element
reflects one of those currencies into which the reporting counterparty has chosen to convert
all the values of posted variation margins.
Currencies included in ISO
4217.
Char(3)
CDE 2.39
54
Variation margin
collected by the
reporting
counterparty (pre￾haircut)
Monetary value of the variation margin collected by the reporting counterparty (including the
cash- settled one), and including any margin that is in transit and pending settlement unless
inclusion of such margin is not allowed under the jurisdictional requirements.
Contingent variation margin is not included.
If the collateralisation is performed at portfolio level, the variation margin collected relates to
the whole portfolio; if the collateralisation is performed for single transactions, the variation
margin collected relates to such single transaction.
This refers to the total current value of the variation margin, cumulated since the first
reporting of collected variation margins for the portfolio/transaction.
If the variation margin collected is denominated in more than one currency, those amounts
are converted into a single currency chosen by the reporting counterparty and reported as
one total value.
Any value greater than or
equal to zero.
Num(25,5)
Collateral reporting shall be separate from transaction
reporting.
If the collateralisation is performed at portfolio level, then
the portfolio code and the amount of collateral (gross
amount) should be reported together at the time of
collateral reporting.
CDE 2.40
19

## Page 25

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
55
Variation margin
collected by the
reporting
counterparty (post￾haircut)
Monetary value of the variation margin collected by the reporting counterparty (including the
cash- settled one), and including any margin that is in transit and pending settlement unless
inclusion of such margin is not allowed under the jurisdictional requirements.
Contingent variation margin is not included.
If the collateralisation is performed at portfolio level, the variation margin collected relates to
the whole portfolio; if the collateralisation is performed for single transactions, the variation
margin collected relates to such single transaction.
This refers to the total current value of the variation margin collected after application of the
haircut (if applicable), cumulated since the first reporting of collected variation margins for the
portfolio/transaction.
If the variation margin collected is denominated in more than one currency, those amounts
are converted into a single currency chosen by the reporting counterparty and reported as
one total value.
Any value greater than or
equal to zero.
Num(25,5)
Collateral reporting shall be separate from transaction
reporting.
If the collateralisation is performed at portfolio level, then
the portfolio code and the amount of collateral (gross
amount) should be reported together at the time of
collateral reporting.
CDE 2.41
56
Currency of
variation margin
collected
Currency in which the variation margin collected is denominated.
If the variation margin collected is denominated in more than one currency, this data element
reflects one of those currencies into which the reporting counterparty has chosen to convert
all the values of collected variation margins.
Currencies included in ISO
4217.
Char(3)
CDE 2.42
57
Excess collateral
posted by the
reporting
counterparty
Monetary value of any additional collateral posted by the reporting counterparty separate and
independent from initial and variation margin. This refers to the total current value of the
excess collateral before application of the haircut (if applicable), rather than to its daily
change.
Any initial or variation margin amount posted that exceeds the required initial margin or
required variation margin, is reported as part of the initial margin posted or variation margin
posted respectively rather than included as excess collateral posted.
For centrally cleared transactions, excess collateral is reported only to the extent it can be
assigned to a specific portfolio or transaction.
Any value greater than or
equal to zero.
Num(25,5)
By definition, excess collateral should be managed
separately from both initial margin and variation margin.
(Example : Independent Amount)
CDE 2.43
58
Currency of excess
collateral posted
Currency in which the excess collateral posted is denominated.
If the excess collateral posted is denominated in more than one currency, this data element
reflects one of those currencies into which the reporting counterparty has chosen to convert
all the values of posted excess collateral.
Currencies included in ISO
4217.
Char(3)
By definition, excess collateral should be managed
separately from both initial margin and variation margin.
(Example : Independent Amount)
CDE 2.44
20

## Page 26

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
59
Excess collateral
collected by the
reporting
counterparty
Monetary value of any additional collateral collected by the reporting counterparty separate
and independent from initial and variation margin. This data element refers to the total current
value of the excess collateral before application of the haircut (if applicable), rather than to its
daily change.
Any initial or variation margin amount collected that exceeds the required initial margin or
required variation margin, is reported as part of the initial margin collected or variation margin
collected respectively, rather than included as excess collateral collected.
For centrally cleared transactions excess collateral is reported only to the extent it can be
assigned to a specific portfolio or transaction.
Any value greater than or
equal to zero.
Num(25,5)
By definition, excess collateral should be managed
separately from both initial margin and variation margin.
(Example : Independent Amount)
CDE 2.45
60
Currency of excess
collateral collected
Currency in which the excess collateral collected is denominated.
If the excess collateral is denominated in more than one currency, this data element reflects
one of those currencies into which the reporting counterparty has chosen to convert all the
values of collected excess collateral.
Currencies included in ISO
4217.
Char(3)
By definition, excess collateral should be managed
separately from both initial margin and variation margin.
(Example : Independent Amount)
CDE 2.46
61
Collateralisation
category
Indicator of whether a collateral agreement (or collateral agreements) between the
counterparties exists (uncollateralised/partially collateralised/one-way collateralised/fully
collateralised). This data element is provided for each transaction or each portfolio,
depending on whether the collateralisation is performed at the transaction or portfolio level,
and is applicable to both cleared and uncleared transactions.
Char(4) CDE 2.47
62
Initial margin
collateral portfolio
code
If collateral is reported on a portfolio basis, a unique code assigned by the reporting
counterparty to the portfolio that tracks the aggregate initial margin of a set of open swap
transactions.
This data element is not applicable if the collateralisation was performed on a transaction
level basis, or if there is no collateral agreement, or if no collateral is posted or received.
The portfolio code is required for both collateral reporting and valuation reporting in order to
link the 2 data sets.
Varchar(52)
Report the unique code assigned by the financial
institution.
If collateralisation is performed separately for each
parties involved in the transaction, report the code per
each party.
CFTC 116
63
Variation margin
collateral portfolio
code
If collateral is reported on a portfolio basis, a unique code assigned by the reporting
counterparty to the portfolio that tracks the aggregate variation margin related to a set of
open swap transactions.
This data element is not applicable if the collateralisation was performed on a transaction
level basis, or if there is no collateral agreement, or if no collateral is posted or received.
The portfolio code is required for both collateral reporting and valuation reporting in order to
link the 2 data sets.
Varchar(52)
Report the unique code assigned by the financial
institution.
If collateralisation is performed separately for each
parties involved in the transaction, report the code per
each party.
CFTC 124
21

## Page 27

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
64 Price
Price specified in the OTC derivative transaction. It does not include fees, taxes or commissions.
For commodity fixed/float swaps and similar products with periodic payments, this data element refers to the
fixed price of the fixed Leg(s).
For commodity and equity forwards and similar products, this data element refers to the forward price of the
underlying or reference asset.
For equity swaps, portfolios swaps, and similar products, this data element refers to the initial price of the
underlying or reference asset.
For contracts for difference and similar products, this data element refers to the initial price of the underlier.
This data element is not applicable to:
• Interest rate swaps and forward rate agreements, as it is understood that the information included in the
data elements Fixed rate and Spread may be interpreted as the price of the transaction.
• Interest rate options and interest rate swaptions, as it is understood that the information included in the data
elements Strike price and Option premium may be interpreted as the price of the transaction.
• Commodity basis swaps and the floating Leg of commodity fixed/float swaps, as it is understood that the
information included in the data element Spread may be interpreted as the price of the transaction.
• Foreign exchange swaps, forwards and options, as it is understood that the information included in the data
elements Exchange rate, Strike price, and Option premium may be interpreted as the price of the
transaction.
• Equity options, as it is understood that the information included in the data elements Strike price and Option
premium may be interpreted as the price of the transaction.
• Credit default swaps and credit total return swaps, as it is understood that the information included in the
data elements Fixed rate, Spread and Upfront payment (Other payment type: Upfront payment) may be
interpreted as the price of the transaction.
• Commodity options, as it is understood that the information included in the data elements Strike price and
Option premium may be interpreted as the price of the transaction.
Where the price is not known when a new transaction is reported, the price is updated as it becomes
available.
For transactions that are part of a package, this data element contains the price of the component
transaction where applicable.
•Num(18,13), any value, if
Price notation = 1
• Num(11,10), any value
expressed as decimal (eg
0.0257 instead of 2.57%), if
Price notation = 3
CDE 2.50
65 Price currency
Currency in which the price is denominated.
Price currency is only applicable if Price notation = 1.
Currencies included in ISO
4217.
Char(3)
CDE 2.51
66 Price notation Manner in which the price is expressed.
Char(1)
• 1 = monetary amount
• 3 = decimal
The above allowable values
might be restricted based on
jurisdictional requirements
(eg certain jurisdictions
might require the value to
be reported as a decimal
instead of percentage).
CDE 2.52
22

## Page 28

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
67
Price unit of
measure
Unit of measure in which the price is expressed.
Char(4)
ISO 20022:
UnitOfMeasureCode
codeset
CDE 2.53
68
Price schedules -
Unadjusted
effective date of the
price
YYYY-MM-DD（UTC）
Applicable for products where the prices will vary
throughout the life of transaction. For those products that
are not applicable, reporting is not required.
CDE 2.54.1
69
Price schedules -
Unadjusted end
date of the price
YYYY-MM-DD（UTC）
Applicable for products where the prices will vary
throughout the life of transaction. For those products that
are not applicable, reporting is not required.
CDE 2.54.2
70
Price schedules -
Price in effect
between the
unadjusted
effective date and
unadjusted end
date inclusive
・ Num(18,13) , if Price
notation = 1
・Num(11,10), if Price
notation = 3
Applicable for products where the prices will vary
throughout the life of transaction. For those products that
are not applicable, reporting is not required.
CDE 2.54.3
71 Fixed rate Leg1,Leg2
For each Leg of the transaction, where applicable: for OTC derivative transactions with
periodic payments, per annum rate of the fixed Leg(s).
・Num(11,10)
• Positive and negative
values expressed as
decimal (eg 0.0257 instead
of 2.57%).
In case the receipt and payment amount is fixed, it is to
be converted into a rate.
CDE 2.55
For OTC derivative transactions with prices varying throughout the life of the transaction:
• 68: Unadjusted effective date of the price
• 69: Unadjusted end date of the price
(not applicable if the unadjusted end date of a given schedule’s period is back-to-back with
the unadjusted effective date of the subsequent period)
• 70: Price in effect between the unadjusted effective date and unadjusted end date inclusive.
Price schedule is only applicable if the price varies per schedule.
The currency, notation, and unit of measure for the varying prices in the schedule are
reported in Price currency, Price notation, and Price unit of measure data elements.
23

## Page 29

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
72 Spread Leg1,Leg2
For each Leg of the transaction, where applicable: for OTC derivative transactions with
periodic payments (eg interest rate fixed/float swaps, interest rate basis swaps, commodity
swaps),
• spread on the individual floating Leg(s) index reference price, in the case where there is a
spread on a floating Leg(s). For example, USD-LIBOR-BBA plus .03 or WTI minus USD
14.65; or
• difference between the reference prices of the two floating Leg indexes. For example, the
9.00 USD “Spread” for a WCS vs. WTI basis swap where WCS is priced at 43 USD and WTI
is priced at 52 USD.
• Num(18,13), any value, if
Spread notation = 1
• Num(11,10), any value
expressed as decimal (eg
0.0257 instead of 2.57%), if
Spread notation = 3
• Num(5), any integer value
expressed in basis points
(eg 257 instead of 2.57%), if
Spread notation = 4
CDE 2.57
73 Spread currency Leg1,Leg2
For each Leg of the transaction, where applicable: currency in which the spread is
denominated. This data element is only applicable if Spread notation = 1.
Currencies included in ISO
4217.
Char(3)
CDE 2.58
74 Spread notation Leg1,Leg2 For each Leg of the transaction, where applicable: manner in which the spread is expressed.
Char(1)
• 1 = monetary amount
• 3 = decimal
• 4 = basis points
The above allowable values
might be restricted based on
jurisdictional requirements
(eg certain jurisdictions
might require the value to
be reported as a decimal
instead of percentage).
CDE 2.59
24

## Page 30

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
75 Strike price
• For options other than FX options, swaptions and similar products, price at which the owner
of an option can buy or sell the underlying asset of the option.
• For foreign exchange options, exchange rate at which the option can be exercised,
expressed as the rate of exchange from converting the unit currency into the quoted
currency. In the example 0.9426 USD/EUR, USD is the unit currency and EUR is the quoted
currency; USD 1 = EUR 0.9426.Where the strike price is not known when a new transaction
is reported, the strike price is updated as it becomes available.
• For volatility and variance swaps and similar products the volatility strike price is reported in
this data element.
•Num(18,13), any value (eg
USD 6.39) expressed as
6.39, for equity options,
commodity options, foreign
exchange options and
similar products, if Strike
price notation = 1.
• Num(11,10,), any value
expressed as decimals (eg
0.021 instead of 2.1%), for
interest rate options, interest
rate and credit swaptions
quoted in spread, and
similar products, if Strike
price notation = 3.
In the case of over-the-counter derivatives transactions
with a Strike Price schedule, report the Strike Price as of
the commencement of the transaction.
CDE 2.60
76
Strike price
currency/currency
pair
For equity options, commodity options, and similar products, currency in which the strike
price is denominated.
For foreign exchange options: Currency pair and order in which the strike price is expressed.
It is expressed as unit currency/quoted currency. In the example 0.9426 USD/EUR, USD is
the unit currency and EUR is the quoted currency, USD 1 = EUR 0.9426
Strike price currency/currency pair is only applicable if Strike price notation = 1.
Currencies included in ISO
4217.
Char(3)
For foreign exchange
options: Char(3)/Char(3);
[Unit currency/Quoted
currency] without restricting
the currency pair ordering
(ie the Strike price currency
pair may be USD/EUR or
EUR/USD).
CDE 2.61
77 Strike price notation Manner in which the Strike price is expressed.
Char(1)
• 1 = monetary amount
• 3=decimal
The above allowable values
might be restricted based on
jurisdictional requirements
(eg certain jurisdictions
might require the value to
be reported as a decimal
instead of percentage).
CDE 2.62
25

## Page 31

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
78
Strike price
schedules -
Unadjusted
effective date of the
strike price
YYYY-MM-DD（UTC）
Applicable for products where the Strike price will vary
throughout the life of transaction. For those products that
are not applicable, reporting is not required.
CDE 2.63.1
79
Strike price
schedules -
Unadjusted end
date of the strike
price
YYYY-MM-DD（UTC）
Applicable for products where the Strike price will vary
throughout the life of transaction. For those products that
are not applicable, reporting is not required.
CDE 2.63.2
80
Strike price
schedules - Strike
price in effect
between the
unadjusted
effective date and
unadjusted end
date inclusive.
Any value greater than zero.
・Num(18,13), any value (eg
USD 6.39) expressed as
6.39, for equity options,
commodity options, foreign
exchange options and
similar products if Strike
price notation = 1.
・Num(11,10), any value
expressed as decimal (eg
0.021 instead of 2.1%), for
interest rate options, interest
rate and credit swaptions
quoted in spread, and
similar products, if Strike
price notation = 3.
Applicable for products where the Strike price will vary
throughout the life of transaction. For those products that
are not applicable, reporting is not required.
(Reporting is not required if Strike Price is not stated.)
CDE 2.63.3
81
Option premium
amount
For options and swaptions of all asset classes, monetary amount paid by the option buyer.
This data element is not applicable if the instrument is not an option or does not embed any
optionality.
Num(25,5)
Any value greater than or
equal to zero.
CDE 2.64
82
Option premium
currency
For options and swaptions of all asset classes, currency in which the option premium amount
is denominated. This data element is not applicable if the instrument is not an option or does
not embed any optionality.
Currencies included in ISO
4217.
Char(3)
CDE 2.65
For options, swaptions and similar products with strike prices varying throughout the life of
the transaction:
• 78: Unadjusted effective date of the strike price
• 79: Unadjusted end date of the strike price
(not applicable if the unadjusted end date of a given schedule’s period is back-to-back with
the unadjusted effective date of the subsequent period)
• 80: Strike price in effect between the unadjusted effective date and unadjusted end date
inclusive.
Strike price schedule is only applicable if the strike price varies per schedule.
The currency for the varying strike prices in the schedule is reported in Strike price currency
data element.
26

## Page 32

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
83
Option premium
payment date
Unadjusted date on which the option premium is paid. YYYY-MM-DD（UTC）
If option premiums are paid in installments, report the first
payment date.
CDE 2.66
84 First exercise date
First unadjusted date during the exercise period in which an option can be exercised.
For European-style options, this date is same as the Expiration date. For American-style
options, the first possible exercise date is the unadjusted date included in the execution
timestamp.
For knock-in options, where the first exercise date is not known when a new transaction is
reported, the first exercise date is updated as it becomes available.
This data element is not applicable if the instrument is not an option or does not embed any
optionality.
YYYY-MM-DD（UTC） CDE 2.67
85 Exchange rate
Exchange rate between the two different currencies specified in the OTC derivative
transaction agreed by the counterparties at the inception of the transaction, expressed as the
rate of exchange from converting the unit currency into the quoted currency. In the example
0.9426 USD/EUR, USD is the unit currency and EUR is the quoted currency; USD 1 = EUR
0.9426.
Any value greater than zero.
Num(18,13) CDE 2.68
86
Exchange rate
basis
Currency pair and order in which the exchange rate is denominated, expressed as unit
currency/quoted currency. In the example 0.9426 USD/EUR, USD is the unit currency and
EUR is the quoted currency, USD 1 = EUR 0.9426.
Char(3)/Char(3); [Unit
currency/Quoted currency],
without restricting the
currency pair ordering (ie
the exchange rate basis
may be USD/EUR or
EUR/USD).
Any pair of currencies
included in ISO 4217.
CDE 2.69
27

## Page 33

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
87 Notional amount Leg1,Leg2
For each Leg of the transaction, where applicable:
- for OTC derivative transactions negotiated in monetary amounts, amount specified in the
contract.
- for OTC derivative transactions negotiated in non-monetary amounts.
• For OTC derivative transactions with a notional amount schedule, the initial notional
amount, agreed by the counterparties at the inception of the transaction, is reported in this
data element.
• For OTC foreign exchange options, in addition to this data element, the amounts are
reported using the data elements Call amount and Put amount. For amendments or lifecycle
events, the resulting outstanding notional amount is reported; (steps in notional amount
schedules are not considered to be amendments or lifecycle events);
• Where the notional amount is not known when a new transaction is reported, the notional
amount is updated as it becomes available.
Num(25,5)
For products denominated in multiple currencies which
are not netted (i.e. currency swaps that exchange JPY
and foreign currency), reporting data must consist of two
separate records (receipt and payment).
CDE 2.70
88 Call amount For foreign exchange options, the monetary amount that the option gives the right to buy.
Any value greater than zero.
Num(25,5)
This item is limited to currency options for which there
are call amounts and put amounts. Call Amount/Put
Amount will report the same amount as Notional Amount
- Leg1/Leg2.
CDE 2.72
89 Put amount For foreign exchange options, the monetary amount that the option gives the right to sell.
Any value greater than zero.
Num(25,5)
This item is limited to currency options for which there
are call amounts and put amounts. Call Amount/Put
Amount will report the same amount as Notional Amount
- Leg1/Leg2.
CDE 2.73
90 Notional currency Leg1,Leg2
For each Leg of the transaction, where applicable: currency in which the notional amount is
denominated.
Currencies included in ISO
4217.
Char(3)
For products denominated in multiple currencies which
are not netted (i.e. currency swaps that exchange JPY
and foreign currency), reporting data must consist of two
separate records (receipt and payment).
CDE 2.74
91 Call currency For foreign exchange options, the currency in which the Call amount is denominated.
Currencies included in ISO
4217.
Char(3)
If Call Amount and Put Amount are reported, call
currency and put currency is expected to be reported for
all option transactions.
CDE 2.75
28

## Page 34

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
92 Put currency For foreign exchange options, the currency in which the Put amount is denominated.
Currencies included in ISO
4217.
Char(3)
If Call Amount and Put Amount are reported, call
currency and put currency is expected to be reported for
all option transactions.
CDE 2.76
93
Quantity unit of
measure
Leg1,Leg2
For each Leg of the transaction, where applicable: unit of measure in which the Total notional
quantity and the Notional quantity schedules are expressed.
Char(4)
ISO 20022:
UnitOfMeasureCode
codeset
CDE 2.77
29

## Page 35

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
94
Notional amount
schedule - notional
amount in effect on
associated effective
date
Leg1,Leg2 Num(25,5)
Reported for over-the-counter derivative transactions
negotiated in monetary amounts with a notional amount
schedule, and the notional amount is expected vary.
For swaps involving accumulation and amortization of the
notional amount:
・ The initial notional amount agreed to by the parties at
the commencement of the transaction is to be reported
as Notional amount.
・ In addition, Notional amount schedule etc. should be
reported at the time of commencement of transactions.
・ In the event of any subsequent changes to the
schedule,
report the changed notional amount schedule by
selecting "ACTION TYPE" to "MODI" and "EVENT
TYPE" to "TRAD". (There is no need to change the
Notional amount schedule, if there is no change from the
original schedule)
・ The initial notional amount reported at the start of the
transaction will remain the same.
CDE 2.78.3
95
Notional amount
schedule -
unadjusted
effective date of the
notional amount
Leg1,Leg2 YYYY-MM-DD（UTC）
Reported for over-the-counter derivative transactions
negotiated in monetary amounts with a notional amount
schedule, and the notional amount is expected to vary.
CDE 2.78.1
96
Notional amount
schedule -
unadjusted end
date of the notional
amount
Leg1,Leg2 YYYY-MM-DD（UTC）
Reported for over-the-counter derivative transactions
negotiated in monetary amounts with a notional amount
schedule, and the notional amount is expected to vary.
CDE 2.78.2
For each Leg of the transaction, where applicable:
for OTC derivative transactions negotiated in monetary amounts with a notional amount
schedule:
• 95: Unadjusted date on which the associated notional amount becomes effective
• 96: Unadjusted end date of the notional amount
(not applicable if the unadjusted end date of a given schedule’s period is back-to-back with
the unadjusted effective date of the subsequent period)
• 94: Notional amount which becomes effective on the associated unadjusted effective date.
The initial notional amount and associated unadjusted effective and end date are reported as
the first values of the schedule.
This data element is not applicable to OTC derivative transactions with notional amounts that
are condition- or event-dependent. The currency of the varying notional amounts in the
schedule is reported in Notional currency.
30

## Page 36

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
97
Total notional
quantity
Leg1,Leg2
For each Leg of the transaction, where applicable: aggregate Notional quantity of the
underlying asset for the term of the transaction.
Where the Total notional quantity is not known when a new transaction is reported, the Total
notional quantity is updated as it becomes available.
Any value greater than or
equal to zero.
Num(25,5)
CDE 2.79
98
Notional quantity
schedules -
Unadjusted date on
which the
associated notional
quantity becomes
effective
Leg1,Leg2 YYYY-MM-DD（UTC）
Reported for over-the-counter derivative transactions
negotiated in non-monetary amounts with a notional
quanity schedule, and the notional quantity is expected to
vary.
CDE 2.80.1
99
Notional quantity
schedules -
Unadjusted end
date of the notional
quantity
Leg1,Leg2 YYYY-MM-DD（UTC）
Reported for over-the-counter derivative transactions
negotiated in non-monetary amounts with a notional
quanity schedule, and the notional quantity is expected to
vary.
CDE 2.80.2
100
Notional quantity
schedules -
Notional quantity
which becomes
effective on the
associated
unadjusted
effective date
Leg1,Leg2
Any value greater than or
equal to zero.
Num(25,5)
Reported for over-the-counter derivative transactions
negotiated in non-monetary amounts with a notional
quanity schedule, and the notional quantity is expected to
vary.
CDE 2.80.3
For each Leg of the transaction, where applicable: for OTC derivative transactions negotiated
in non- monetary amounts with a Notional quantity schedule
• 98: Unadjusted date on which the associated notional quantity becomes effective
• 99: Unadjusted end date of the notional quantity
(not applicable if the unadjusted end date of a given schedule’s period is back-to-back with
the unadjusted effective date of the subsequent period);
• 100: Notional quantity which becomes effective on the associated unadjusted effective date.
The initial notional quantity and associated unadjusted effective and end date are be reported
as the first values of the schedule.
This data element is not applicable to OTC derivative transactions with notional quantities
that are condition- or event-dependent.
The quantity unit of measure for the varying notional quantities in the schedule is reported in
Quantity unit of measure.
31

## Page 37

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
101 Action type
Type of action taken on the swap transaction or type of end-of-day reporting.
Actions may include, but are not limited to, new, modify, correct, error, terminate, revive,
transfer out, valuation, and collateral.
New: An action that reports a new swap transaction.
It applies to the first message relating to a new UTI.
Modify: An action that modifies the state of a previously submitted transaction (e.g., credit
event) or changes a term of a previously submitted transaction due to a newly negotiated
modification (amendment) or updates previously missing information (e.g., post price swap).
It does not include correction of a previous transaction.
Correct:
An action that corrects erroneous data of a previously submitted transaction.
Error: An action of cancellation of a wrongly submitted entire transaction in case it never
came into existence or was not subject to the reporting requirements but was reported
erroneously, or a cancellation of duplicate report.
Terminate: An action that closes an existing transaction because of a new event (e.g.,
Compression, Novation).
This does not apply to transactions that terminate at contractual maturity date.
Revive: An action that reinstates a swap transaction that was reported as error or terminated
by mistake.
Transfer out:
An action that transfers swap transaction from one SDR to another SDR (change of swap
data repository).
Valuation: An update to valuation data.
There will be no corresponding Event type.
Collateral: An update to collateral margin data.
There will be no corresponding Event type.
• NEWT = New
• MODI = Modify
• CORR = Correct
• EROR = Error
• TERM = Terminate
• REVI = Revive
• PRTO = Transfer out
• VALU = Valuation
• MARU = Collateral
Status for reporting items such as "LEI" and "Confirm" could
change during contract period. For those updates which does
not involve contractual changes or error corrections, use
Action Type: Modify.
If New, Correct, or Modify occurs on the same day as the
valuation for a same transaction, report the correction and
valuation separately.
[Specific example]
(Specific example 1) Where an equity option transaction is
knocked-out (currently reported as modify with a notional
amount of 0)
Report "ACTION TYPE" as "Terminate (TERM)" and "EVENT
TYPE" as "Early Termination (EART)".
(Specific Example 2) Where a customer cancels an equity
option transaction (currently reported as cancel)
Report "ACTION TYPE" as "Terminate (TERM)" and "EVENT
TYPE" as "Early Termination (EART)".
(Specific example 3) Exercise of equity option transactions
(previously excluded from reporting)
Report "ACTION TYPE" as "Terminate (TERM)" "EVENT
TYPE" as "Exercise (EXER)".
In cases where the rights are exercised, it is expectd to be
reported as "Terminate" and "Exercise".
CFTC 26
32

## Page 38

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
102 Event type
Explanation or reason for the action being taken on the swap transaction.
Events may include, but are not limited to, trade, novation, compression or risk reduction exercise, early termination, clearing,
exercise, allocation, clearing and allocation, credit event, and transfer.
Trade: A creation or modification of a transaction.
Novation: A novation Legally moves partial or all of the financial risks of a swap from a transferor to a transferee and has the
effect of terminating/modifying the original transaction and creating a new transaction to identify the exposure between the
transferor/transferee and remaining party.
Compression or Risk Reduction Exercise: Compressions and risk reduction exercises generally have the effect of terminating
or modifying (i.e., reducing the notional value) a set of existing transactions and of creating a set of new transaction(s).
These processes result in largely the same exposure of market risk that existed prior to the event for the counterparty.
Early termination: Termination of an existing swap transaction prior to scheduled termination or maturity date.
Clearing: Central clearing is a process where a derivatives clearing organization interposes itself between counterparties to
contracts, becoming the buyer to every seller and the seller to every buyer.
It has the effect of terminating an existing transaction between the buyer and the seller and thereby ensuring the performance of
open contracts.
Exercise: The process by which a counterparty fully or partially exercises their rights specified in the contract of an option or a
swaption.
Allocation:
The process by which an agent, having facilitated a single swap transaction on behalf of several clients, allocates a portion of
the executed swap to the clients.
Clearing and Allocation:
A simultaneous clearing and allocation event in a derivatives clearing organization.
Credit event:
An event or trigger that results in the termination or modification of the state of a previously submitted credit derivative
transaction.
Applies only to credit derivatives.
Transfer:
The process by which a swap is transferred to another SDR that has the effect of the closing of the swap transaction at one
SDR or opening of the same swap transaction using the same UTI/USI in a different SDR (new).
Corporate event:
A corporate action on equity underlying that impacts the transactions on that equity.
Upgrade: An upgrade of an outstanding transaction performed in order to ensure its conformity with the amended reporting
requirements.
• TRAD = Trade
• NOVA = Novation
• COMP = Compression or
Risk Reduction
• ETRM = Early termination
• CLRG = Clearing
• EXER = Exercise
• ALOC = Allocation
• CLAL = Clearing &
Allocation
• CREV = Credit event
• PTNG = Transfer
• CORP = Corporate event
• UPDT = Upgrade
CFTC 27
103 Event identifier
Unique identifier to link swap transactions resulting from an event may be, but is not limited
to, compression, and credit event.
The unique identifier may be assigned by the reporting counterparty or a service provider.
Varchar(52)
ISO 17442 Legal Entity
Identifier (LEI) code of the
entity assigning the event
identifier followed by a
unique identifier up to 32
characters.
This element is necessary as Prior UTIs cannot be used
for compression and credit events.
Any ID assigned by a service provider is expected to be
reported. However if the assignment is done by the
reporting counterparty, then it is not expected for the
assigned ID to be shared between the parties to the
transaction.
CFTC 29
33

## Page 39

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
104 Event timestamp
Date and time of occurrence of the event as determined by the reporting counterparty or a
service provider.
In the case of a clearing event, date and time when the original swap is accepted by the
derivative clearing organization (DCO) for clearing and recorded by the DCO’s system should
be reported in this data element.
The time element is as specific as technologically practicable.
YYYY-MM-DDThh:mm:ssZ
（UTC）
System input time, data generation time, and system
connection time are to be considered as acceptable
values.
In addition, if determining the time up to the seconds is
impossible due to system restrictions, setting the
seconds to "00" shall be acceptable.
Cancellation report of α - transactions by financial
institutions do not necessarily have to match the date
and time recorded by the central counterparty's system.
The date and time recorded by the central counterparty's
system will be submitted by the central counterparty
when they report their β and γ transactions.
CFTC 30
105 Index factor
The index version factor or percent, expressed as a decimal value, that multiplied by the
Notional amount yields the notional amount covered by the seller of protection for credit
default swap.
Num(11,10)
Any value between 0 and 1
(including 0 and 1),
expressed as decimal (e.g.,
0.05 instead of 5%).
(Example)
Gross Notional amount : JPY 1 billion
Reference : Index comprised of 50 Japanese companies
(iTraxx Japan)
Notional amount for each company : JPY 20 million each
Credit event settlement : <Credit event occur for
company #1>
①Company #1 to settle for JPY 20 million
②Gross Notional amount reduced to 980 million yen,
contract to be continued
⇒ The INDEX Factor will become 98%. (Calculate
notional amount after the credit event)
INDEX Factor will be 100% at the start of the transaction,
and will become Version2 notional/Version1 notional
when the credit event occurs.
CFTC 85
106
Embedded option
type
Type of option or optional provision embedded in a contract.
• MDET = Mandatory early
termination
• OPET = Optional early
termination
• CANC = Cancelable
• EXTD = Extendible
• OTHR = Other
Embedded options are products that combines with other
options, such as callable swaps.
CFTC 86
34

## Page 40

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
108 Delivery type Indicates whether the contract is settled physically or in cash.
4 alphabetic characters:
・CASH = Cash
・PHYS = Physical
・OPTL = Optional for
counterparty or when
determined by a third party
ESMA 47
109 Asset Class Each reported contract shall be classified according to the asset class it is based on.
・CRDT = Credit
・CURR = Currency
・EQUI = Equity
・INTR = Interest Rate
・OTHR=Other
When the underlying assets of the derivatives are crypto￾assets :
Select "OTHR = Other"
ESMA 11
110
Underlying
identification type
The type of relevant underlying identifier.
1 alphabetic character:
・I = ISIN
・B = Basket
・X = Index
ESMA 13
111
Underlying
identification
The direct underlying shall be identified by using a unique identification for this underlying
based on its type. For Credit Default Swaps, the ISIN of the reference obligation should be
provided.
For underlying identification
type I: ISO 6166 ISIN 12
character alphanumeric
code For underlying
identification type X: ISO
6166 ISIN if available
If the reference asset is an index without ISIN, report the
asset under "Indicator of the underlying index".
ESMA 14
35

## Page 41

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
112
Indicator of the
underlying index
An indication of the underlying index, where available.
The indication of the floating rate index. 4 alphabetic
characters:
・ESTR = €STR
・SONA = SONIA
・SOFR = SOFR
・EONA = EONIA
・EONS = EONIA SWAP
・EURI = EURIBOR
・EUUS = EURODOLLAR
・EUCH = EuroSwiss
・GCFR = GCF REPO
・ISDA = ISDAFIX
・LIBI = LIBID
・LIBO = LIBOR
・MAAA = Muni AAA
・PFAN = Pfandbriefe
・TIBO = TIBOR
・STBO = STIBOR
・BBSW = BBSW
・JIBA = JIBAR
・BUBO = BUBOR
・CDOR = CDOR
・CIBO = CIBOR
・MOSP = MOSPRIM
・NIBO = NIBOR
・PRBO = PRIBOR
・TLBO = TELBOR
・WIBO = WIBOR
・TREA = Treasury
・SWAP = SWAP
・FUSW = Future SWAP
・EFFR = Effective Federal Funds Rate
・OBFR = Overnight Bank Funding Rate
・CZNA = CZEONIA
・TONA = TONA
・TORF = TORF
・RCTR = RBATCTR
・CORA = CORRA
・BCOL = CABROVER
・HKIO = HIBOR
・BJUO = MUTSCALM
・ETIO = JBATIBOR
・SIBO = SIBOR
・SSOR = SOR
・SORA = SORA
If the indicator of the underlying index does not exist in
the list, report the index using the "Name of the
underlying index".
ESMA 15
113
Name of the
underlying index
The full name of the underlying index as assigned by the index provider.
Up to 50 alphanumeric
characters.
If the indicator of the underlying index does not exist in
the list, report the full name of the index here.
ESMA 16
114 Reference entity Identification of the underlying reference entity.
ISO 3166 - 2 character
country code,
or
ISO 3166-2 - 2 character
country code followed
by dash “-“ and up to 3
alphanumeric character
country subdivision code,
or
ISO 17442 Legal Entity
Identifier (LEI) 20
alphanumeric character
code
ESMA 144
36

## Page 42

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
115
Indicator of the
floating rate
Leg1,Leg2 An indication of the interest rate, where available.
The indication of the floating rate index. 4 alphabetic
characters:
・ESTR = €STR
・SONA = SONIA
・SOFR = SOFR
・EONA = EONIA
・EONS = EONIA SWAP
・EURI = EURIBOR
・EUUS = EURODOLLAR
・EUCH = EuroSwiss
・GCFR = GCF REPO
・ISDA = ISDAFIX
・LIBI = LIBID
・LIBO = LIBOR
・MAAA = Muni AAA
・PFAN = Pfandbriefe
・TIBO = TIBOR
・STBO = STIBOR
・BBSW = BBSW
・JIBA = JIBAR
・BUBO = BUBOR
・CDOR = CDOR
・CIBO = CIBOR
・MOSP = MOSPRIM
・NIBO = NIBOR
・PRBO = PRIBOR
・TLBO = TELBOR
・WIBO = WIBOR
・TREA = Treasury
・SWAP = SWAP
・FUSW = Future SWAP
・EFFR = Effective Federal Funds Rate
・OBFR = Overnight Bank Funding Rate
・CZNA = CZEONIA
・TONA = TONA
・TORF = TORF
・RCTR = RBATCTR
・CORA = CORRA
・BCOL = CABROVER
・HKIO = HIBOR
・BJUO = MUTSCALM
・ETIO = JBATIBOR
・SIBO = SIBOR
・SSOR = SOR
・SORA = SORA
If the floating rate index does not exist in the list, report
the index using the "Name of the floating rate".
ESMA
84
100
116
Name of the
floating rate
Leg1,Leg2 The full name of the interest rate as assigned by the index provider.
Up to 50 alphanumeric
characters.
Use this item when the Indicator of the floating rate does
not include a floating rate index to be reported.
ESMA
85
101
117
Floating rate
reference period –
time period
Leg1,Leg2 Time period describing the reference period for the floating rate of Leg1,Leg2.
4 alphabetic characters:
・DAIL = daily
・WEEK = weekly
・MNTH = monthly
・YEAR = yearly
・ADHO = ad hoc which
applies when payments
are irregular
・EXPI = payment at term
ESMA
89
105
37

## Page 43

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
118
Floating rate
reference period –
multiplier
Leg1,Leg2 Multiplier of the time period describing the reference period for the floating rate of Leg1,Leg2.
Any integer value greater
than or equal to zero up to 3
numeric characters.
ESMA
90
106
119
Derivative based on
crypto-assets
Indicator whether the derivative is based on cryptoassets. Boolean: True or False ESMA 12
120
Maturity date of the
underlying
In case of swaptions, maturity date of the underlying swap. YYYY-MM-DD（UTC） Reported for swaptions only. ESMA 142
121 Seniority（CD） Indicates the seniority of the debt security, or debt basket or index underlying a derivative.
4 alphabetic characters
・SNDB = Senior, such as
Senior Unsecured Debt
(Corporate/Financial),
Foreign Currency Sovereign
Debt (Government),
・SBOD = Subordinated,
such as Subordinated or
Lower Tier 2 Debt (Banks),
Junior Subordinated or
Upper Tier 2 Debt (Banks),
・OTHR = Other, such as
Preference Shares or Tier 1
Capital (Banks) or other
credit derivatives
ESMA 143
122 Series （CD) The series number of the composition of the index if applicable.
Integer field up to 5
characters.
ESMA 145
38

## Page 44

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
123 Version（CD)
A new version of a series is issued if one of the constituents defaults and the index has to be
reweighted to account for the new number of total constituents within the index.
Integer field up to 5
characters.
ESMA 146
124
CDS index
attachment point
Defined lower point at which the level of losses in the underlying portfolio reduces the
notional of a tranche. For example, the notional in a tranche with an attachment point of 3%
will be reduced after 3% of losses in the portfolio have occurred. This data element is not
applicable if the transaction is not a CDS tranche transaction (index or custom basket).
Num(11,10)
Any value between 0 and 1
(including 0 and
1)expressed as decimal (eg
0.05 instead of 5%).
CDE 2.81
125
CDS index
detachment point
Defined point beyond which losses in the underlying portfolio no longer reduce the notional of
a tranche. For example, the notional in a tranche with an attachment point of 3% and a
detachment point of 6% will be reduced after there have been 3% of losses in the portfolio.
6% losses in the portfolio deplete the notional of the tranche. This data element is not
applicable if the transaction is not a CDS tranche transaction (index or custom basket).
Num(11,10)
Any value between 0 and 1
(including 0 and
1)expressed as decimal (eg
0.05 instead of 5%).
CDE 2.82
126
Custom basket
code
If the OTC derivative transaction is based on a custom basket, unique code assigned by the
structurer of the custom basket to link its constituents. This data element is not applicable if
no custom basket is involved or no unique code has been assigned to it.
Varchar(72)
LEI of the basket structurer
followed by 52 alphanumeric
characters.
A custom basket should be used for any asset class
which refers to multiple indices (i.e. first to default,
rainbow options, etc.).
CDE 2.97
127
Identifier of the
basket's
constituents
Underliers that represent the constituents of a custom basket, in line with the underlier ID
within the UPI reference data elements, as defined by the CPMI-IOSCO Technical Guidance:
Harmonisation of the Unique Product Identifier. This data element is not applicable if no
custom basket is involved.
Varchar(350)
An identifier that can be
used to determine an asset,
index or benchmark
included in a basket
Up to 350 alphanumeric
characters.
CDE 2.98
128
Basket constituent
identifier source
Source of the underliers’ identifiers that represent the constituents of a custom basket.
This data element is not applicable if no custom basket is involved.
Varchar(350)
The origin, or publisher, of
the associated basket
constituent identifier.
Up to 350 alphanumeric
characters.
CDE 2.101
39

## Page 45

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
129 Contract type Each reported contract shall be classified according to its type.
・CFDS = Financial
contracts for difference
・FRAS = Forward rate
agreements
・FUTR = Futures
・FORW = Forwards
・OPTN = Option
・SPDB = Spreadbet
・SWAP = Swap
・SWPT = Swaption
・OTHR = Other
ESMA 10
130 Option style
Indicates whether the option may be exercised only at a fixed date (European), a series of
pre-specified dates (Bermudan) or at any time during the life of the contract (American).
4 alphabetic characters:
・AMER = American
・BERM = Bermudan
・EURO = European
For Caps and Floors, report "EURO". ESMA 133
131 Option type
Indication as to whether the derivative contract is a call (right to purchase a specific
underlying asset) or a put (right to sell a specific underlying asset) or whether it cannot be
determined whether it is a call or a put at the time of execution of the derivative contract. In
case of swaptions it shall be:
- “Put”, in case of receiver swaption, in which the buyer has the right to enter into a swap as
a fixed-rate receiver.
-“Call”, in case of payer swaption, in which the buyer has the right to enter into a swap as a
fixed-rate payer. In case of Caps and Floors it shall be:
-“Put”, in case of a Floor.
-“Call”, in case of a Cap.
4 alphabetic character:
・PUTO = Put
・CALL = Call
・OTHR = where it cannot
be determined whether it is
a call or a put
ESMA 132
132 Package identifier
Identifier (determined by the reporting counterparty) in order to connect
• two or more transactions that are reported separately by the reporting counterparty, but that
are negotiated together as the product of a single economic agreement.
• two or more reports pertaining to the same transaction whenever jurisdictional reporting
requirement does not allow the transaction to be reported with a single report to TRs.
A package may include reportable and non-reportable transactions. This data element is not
applicable
• if no package is involved, or
• to allocations
Where the package identifier is not known when a new transaction is reported, the package
identifier is updated as it becomes available.
Varchar(35)
It shall be a unique identifier.
It is not expected to be shared with the parties involved
in the transaction.
CDE 2.89
40

## Page 46

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
133
Package
transaction price
Traded price of the entire package in which the reported derivative transaction is a
component. This data element is not applicable if
• no package is involved, or
• package transaction spread is used
Prices and related data elements of the transactions (Price currency, Price notation, Price
unit of measure) that represent individual components of the package are reported when
available.
The package transaction price may not be known when a new transaction is reported but
may be updated later.
• Num(18,13), any value, if
Package transaction price
notation = 1
• Num(11,10), any value
expressed as decimal (eg
0.0257 instead of 2.57%), if
Package transaction price
notation = 3
CDE 2.90
134
Package
transaction price
currency
Currency in which the Package transaction price is denominated. This data element is not
applicable if
• no package is involved, or
• Package transaction spread is used, or
• Package transaction price notation = 3
Currencies included in ISO
4217.
Char(3)
CDE 2.91
135
Package
transaction price
notation
Manner in which the Package transaction price is expressed. This data element is not
applicable if
• no package is involved, or
• Package transaction spread is used
Char(1)
• 1 = monetary amount
• 3 = decimal
The above allowable values
might be restricted based on
jurisdictional requirements
(eg certain jurisdictions
might require the value to
be reported as a decimal
instead of percentage).
CDE 2.92
41

## Page 47

＃
Source
Allowable values for each
data element
Remarks
Data Element
Name
Leg1,Leg2 Definition of data elements
136
Package
transaction spread
Traded price of the entire package in which the reported derivative transaction is a
component of a package transaction.
Package transaction price when the price of the package is expressed as a spread,
difference between two reference prices.
This data element is not applicable if
• no package is involved, or
• Package transaction price is used
Spread and related data elements of the transactions (spread currency, Spread notation) that
represent individual components of the package are reported when available.
Package transaction spread may not be known when a new transaction is reported but may
be updated later.
• Num(18,13), any value, if
Package transaction spread
notation = 1
• Num(11,10), any value
expressed as decimal (eg
0.0257 instead of 2.57%), if
Package transaction spread
notation = 3
• Num(5), any integer value
expressed in basis points
(eg 257 instead of 2.57%), if
Package transaction spread
notation = 4
CDE 2.93
137
Package
transaction spread
currency
Currency in which the Package transaction spread is denominated. This data element is not
applicable if
• no package is involved, or
• Package transaction price is used, or
• Package transaction spread notation = 3 or = 4
Currencies included in ISO
4217.
Char(3)
CDE 2,94
138
Package
transaction spread
notation
Manner in which the Package transaction spread is expressed. This data element is not
applicable if
• no package is involved, or
• Package transaction price is used
Char(1)
• 1 = monetary amount
• 3 = decimal
• 4 = basis points
The above allowable values
might be restricted based on
jurisdictional requirements
(example, certain
jurisdictions might require
the value to be reported as
a decimal instead of
percentage).
CDE 2.95
139 Package indicator Indicator of whether the swap transaction is part of a package transaction. Boolean: True or False CFTC 45
42

## Page 48

How to determine the generation
of Unique Transaction Identifier (UTI)
December 2022
Financial Services Agency of Japan
Attachment 2

## Page 49

1
１.Background and Overview
The Financial Instruments and Exchange Act (hereinafter referred to as”FIEA”)
and the Cabinet Office Order on the Regulation of Over-the-Counter Derivatives
Transactions, etc. (hereinafter referred to as”Cabinet Office Order”), which was
amended in August 2022, require financial instruments clearing organizations
(central counterparty clearing houses (CCPs)) and financial instruments business
operators (FIBOs)) to provide OTC derivatives trade data to trade repositories
(TRs). TRs are required to prepare and preserve the records concerning items
specified in Article 4(1) of the Cabinet Office Order and submit trade data to Prime
Minister. One of the items to be reported is the identification of transactions
(Unique Transaction Identifier (UTI)).
The “How to determine the generation of Unique Transaction Identifier (UTI)”
summarizes approaches related to mainly UTI generation responsibility and UTI
sharing. This document reflects discussions raised in the public-private sector
meeting, which includes the Financial Services Agency of Japan (hereinafter
referred to as the “JFSA”), financial services industry organizations, market
infrastructure providers, and financial institutions.
２.Premise
(１) Definition of terms
The definitions used in this “How to determine the generation of Unique
Transaction Identifier (UTI)” are as follows.
Terms Descriptions
Reporting Entity “Financial instruments clearing organizations” as
defined in Article 1(2)(viii) of the Cabinet Office Order
and “business operators, etc. that are subject to the
creation of trade data (transaction information)”
(BOCTDs) as defined in Article 2(4)(iv)(a) of the
Cabinet Office Order.
Non-Reporting
Entity
An entity other than the Reporting Entity.
Cross-jurisdictional
Transactions
Transactions reported in Japan and other jurisdictions.
Interest Rate
Derivatives
Interest rate swaps and interest rate options or similar
instruments.
Trading Platform Trading Platform is not defined in the “Technical
guidance: Harmonisation of the unique transaction
identifier” ("Technical Guidance") issued in 2017 by the
Committee on Payments and Market Infrastructures
and the International Organization of Securities
Commissions (“CPMI-IOSCO”). This document refers

## Page 50

2
to the Trading Platform as electronic trading platforms
(ETP) for example, and does not include CCPs.
Confirmation
Platform
The Technical Guidance refers to platforms confirming
trades electronically.
(２) UTI
UTI is a unique code that is assigned to each reportable transaction. It is
intended to prevent duplicative reporting and to facilitate global data aggregation
by regulators.
UTIs structure and format is specified in ISO 23897 as a concatenated
combination of the LEI (20 characters) of the UTI generator at the point of
generation and a unique identifier created by that entity, structured with a
maximum of 52 characters constructed solely from upper-case alphabetic
characters A-Z or the digits 0-9 (inclusive in both cases).
(Reference) Waterfall Approach under the Technical Guidance
The Technical Guidance requires the generation of new UTI not only in the
course of initial reports of new reportable transactions, but also when (i) there is
a change to either counterparty (e.g. due to clearing, etc.), or when (ii) an OTC
derivatives transaction is replaced by one or more other OTC derivatives
transactions (e.g. due to compression, netting, the transaction is split into different
transactions, etc.), whether or not they involve the same or different
counterparties.
The Technical Guidance takes a waterfall approach to determine the UTI
generator as follows.
Step Factor to consider Responsibility for UTI generation
1
Is a CCP a counterparty to this
transaction?
If so, the CCP.
Otherwise, see step 2.
2
Is a counterparty to this transaction a
clearing member of a CCP, and if so
is that clearing member acting in its
clearing member capacity for this
transaction?
If so, the clearing member.
Otherwise, see step 3.
3
Was the transaction executed on a
trading platform?
If so, the trading platform.
Otherwise, see step 4.
4
Is the transaction cross-jurisdictional
(i.e. are the counterparties to the
If so, see step 10.
Otherwise, see step 5.

## Page 51

3
Step Factor to consider Responsibility for UTI generation
transaction subject to more than one
jurisdiction’s reporting rules)?
5
Do both counterparties have
reporting obligations?
If so, see step 6.
Otherwise, see step 7.
6
Has the transaction been
electronically confirmed or will it be
and, if so, is the confirmation
platform able, willing and permitted
to generate a UTI within the required
time frame under the applicable
rules?
If so, the confirmation platform.
Otherwise, see step 7.
7
Does the jurisdiction employ a
counterparty-status-based approach
(e.g., rule definition or registration
status) for determining which entity
should have responsibility for
generating the UTI?
If so, see step 8.
Otherwise, see step 11
8
Do the counterparties have the same
regulatory status for UTI generation
purposes under the relevant
jurisdiction?
If so, see step 11.
Otherwise, see step 9
9
Do the applicable rules determine
which entity should have
responsibility for generating the UTI?
If so, the assigned entity.
Otherwise, see step 12.
10
Does one of the jurisdictions have a
sooner deadline for reporting than
the other(s)?
If so, then the UTI generation
rules of the jurisdiction with the
sooner reporting deadline should
be followed.
Otherwise, see step 11.
11
Do the counterparties have an
agreement governing which entity
should have responsibility for
generating the UTI for this
transaction?
If so, the agreed entity.
Otherwise, see step 12.
12
Has the transaction been
electronically confirmed or will it be
and, if so, is the confirmation
platform able, willing and permitted
to generate a UTI within the required
If so, the confirmation platform.
Otherwise, see step 13.

## Page 52

4 
Step Factor to consider Responsibility for UTI generation
time frame under the applicable
rules?
13
Is there a single TR to which reports
relating to the transaction have to be
made, and is that TR able, willing and
permitted to generate UTIs under the
applicable rules?
If so, the TR.
Otherwise, one of the
counterparties, based on sorting
the identifiers of the
counterparties with the characters
of the identifier reversed and
picking the counterparty that
comes first in this sort sequence.
３.Approach for UTI Generation Responsibility in Japan 
(１) Concept
The concept regarding the generation responsibility of UTIs in Japan is
described below. 
[Transactions between Reporting Entities]
(i) UTI is generated in accordance to the Technical Guidance as described
above.
(ii) Otherwise, including cases where it is practically difficult to follow (i), the
parties determine the UTI generation responsibility based on bilateral
agreement.
Other method may also be considered, such as an agreement that one party,
based on its scale, will always be the UTI generator. Excessive burdens
should be avoided. If the Trading Platform or the Confirmation Platform is
unable to generate UTI due to system trouble or other temporary reasons,
the Reporting Party needs to report a provisional UTI and then replace it with
a genuine UTI.
In case of transactions between BOCTDs, where the one’s average month￾end notional amount of outstanding OTC derivatives exceeds JPY300 billion
for the previous fiscal year from April to March while the other one is not, the
former BOCTD could be regarded as the UTI generator. This is because that
the latter one would be exempted from reporting requirements for certain
OTC derivatives defined in Article 7(3) and Article 8(4) of the Cabinet Office
order and Article 1 and 2 of the JFSA Notification No. 11 of 2021 "Financial
Instruments Business Operators, etc. and Transactions designated by the
Financial Services Agency Commissioner.”

## Page 53

5 
[Transactions between Reporting Entities and Non-Reporting Entities]
If the UTIs for transactions between Reporting Entity and Non-Reporting
Entity (certain FIBOs, non FIBOs, and Individuals, etc.) are not generated by
any platform, the Reporting Entity has responsibility for generating UTI. 
[Transactions between Non-Reporting Entities]
Transactions between non-reporting entities are not required to be reported.
(２) Consideration by financial products characteristics
The following summarizes the classification of generating parties by product in
consideration of (１) and market practice in Japan.
A. Interest Rate Derivatives, CDS
 
1 Alpha transactions are transactions between parties to the original transactions before cleared through a
CCP. When reporting beta and gamma transactions, which are transactions between a CCP and each
party to the alpha transaction executed as a result of clearing, CCPs need UTI of an alpha transaction as a
prior UTI. Therefore, UTI should be properly linked from the Trading or Confirmation Platform such as
through request for clearing (The same approach shall apply hereafter with respect to a clearing
transaction).
2
 In case where the transaction is cleared through CCPs designated by the JFSA Notification No.105 of
2011, " Designation of Transactions and Loans Designated by the Commissioner of the Financial Services
Agency Excluded from Transactions Subject to Financial Instruments Obligation Assumption Service “, a
Reporting Entity is required to report the transaction. (The same shall apply hereafter.)
(i)
Infrastructure
used in the
process of
transaction
(ii)
Cleared/
not
cleared
(iii)
Transaction
Type
UTI generator Notes
Trading
Platform
Cleared alpha
1 Trading
Platform
(*)
If the transaction is
not cleared,
contracting
counterparty shall
report as a bilateral
transaction.
beta and
gamma
CCP CCP is required to
report the
transaction.
2
Not cleared Trading
Platform (*)
Confirmation
Platform
Cleared alpha Confirmation
Platform (*)
Only if UTI is not
generated by the
Trading Platform.

## Page 54

6
* If the Trading/Confirmation platform does not agree to generate UTI, the
UTI generator should be determined in accordance to "transactions other
than the above".
B. Equity derivatives
Infrastructure
used in the process of transaction
UTI generator
Confirmation platform Confirmation platform (*)
Transactions other than the above Determined by bilateral
agreement
* If the Confirmation platform does not agree to generate UTI, the UTI
generator should be determined in accordance to "transactions other
than the above".
C. Currency options, NDF
4 and NDO
The UTI should be generated following the approach described in (1) above.
 As for swaptions, UTIs shall be generated respectively at the time of new
transactions and exercise.
 
3 For example, the paper confirmation issuer or larger Reporting Entity could be a UTI generator.
4 non-deliverable forward
If the transaction is
not cleared,
contracting
counterparty shall
report as a bilateral
transaction.
beta and
gamma
CCP CCP is required to
report the
transaction
5
.
Not cleared Confirmation
Platform (*)
Only if it is not
generated by the
Trading Platform.
Transactions other than the above Bilateral
agreement
3

## Page 55

7
(３)Cross-jurisdictional Transactions
In principle, the waterfall approach of the Technical Guidance should apply to
Cross-jurisdictional Transactions, but if it is difficult to confirm Step 10 "Does one
of the jurisdictions have a sooner deadline for reporting than the other(s)?,”
counterparties may skip and move to the step 11.
* Where it is difficult to obtain a comprehensive and accurate understanding of
the regulations to which counterparties are subject to, the above treatment is
applied, and the reporting party is not required to determine a jurisdiction
with the soonest reporting deadlines, as requested in the step 10. However,
it is necessary to negotiate with the counterparty beforehand. 
In addition, this treatment is not prioritized over the rules of other
jurisdictions, and the Reporting Party should also respect rules which the
counterparty is subject to.
４.Approach for UTI Sharing in Japan
(１) Concept
In case for transactions between Reporting Entities, both parties are required
to report the same UTI. UTI should be shared between the entities in a timely
manner and no later than the reporting deadline.
Although UTI sharing method will be decided by each transaction, this
document sets out the primary approach as follows.
Infrastructure
used in the process of transaction
Approach for UTI sharing
Trading Platform
Confirmation Platform
Confirmation Platform5
SWIFT SWIFT
6
Otherwise i.e. paper confirmation* or e-mail
* Note that operational risk is higher compared with other methods. Sharing using
electronic methods are preferred wherever possible.
In principle, UTI should be shared promptly such as at the time of execution,
since the trade data (transaction information) must be reported to the TRs within
T+2 business days. However, on the assumption that UTI should be shared in
time for reporting as much as possible, if it takes some time to share the UTI,
 
5 When a Trading Platform is used, this is limited to cases where UTIs generated by the Trading Platform
are shared via the Confirmation Platform (the same applies in "(2) A").
6 The SWIFT messages set “22M (UTI Namespace/Issuer Code)”and “22N (Transaction Identifier)" as tags
for UTI.

## Page 56

8
reporting of provisional UTI assigned by the receiving counterparty is permitted.
The provisional UTI should be replaced as soon as the genuine UTI is assigned.
(２) Consideration by financial products characteristics
Based on the concept in (１) above, this document sets out more detailed
sharing method by products characteristics as follows. For products not described
in this document, sharing method should be determined bilaterally.
A. Interest Rate Derivatives, CDS
(i) 
Infrastructure
used in the
process of
transaction
(ii)
Cleared/
not
cleared
(iii)
Transaction
Type
Approach for UTI sharing
Trading Platform Cleared alpha Confirmation Platform
beta and
gamma
To be shared via CCP reporting
tools if necessary.
Not cleared Confirmation Platform
Confirmation
Platform
Cleared alpha Confirmation Platform
beta and
gamma
To be shared via CCP reporting
tools if necessary. 
Not cleared Confirmation Platform
Transactions other than above A paper confirmation or e-mail
as example.
B. Equity derivatives
Infrastructure
used in the process of transaction
Approach for UTI sharing
Confirmation Platform Confirmation Platform
Transactions other than above Paper confirmation or e-mail
C. Currency options, NDF and NDO
Shared via SWIFT, paper confirmation or e-mail

## Page 57

9
５.Other Issues
(１) Lifecycle events that require generation of a new UTI
The determination on whether or not a new UTI is required to be generated for
each transaction should be considered in accordance with Technical Guidance.
When a transaction is terminated and replaced with one or more other
transactions, new UTIs should be used.
7 The basic approach is as follows:
(i) If new information is being reported for a legacy OTC derivatives
transaction, or some of the previously reported information has changed,
then the report should be updated using the same UTI. Examples of
situations where the previous UTI should be maintained include:
a. A revaluation or similar is reported.
b. Some previously reported information, such as whether the trade has
been confirmed, has changed.
c. The contract is an amortizing swap or similar, and the notional has
changed in accordance with the contractual terms.
d. Reporting of end-of-life events such as early termination.
8
e. Some previously reported information that was incorrect and is being
corrected unless the incorrect information is the UTI itself.
(ii) Otherwise, a new UTI should be used. Examples of this include:
a. A change to either counterparty. This includes Novation
9 or clearing
where either of the counterparty is changed to a CCP.
b. Where an OTC derivatives transaction is replaced by one or more other
transactions, regardless of whether same or different counterparties are
involved. (e.g., Compressions)
 
7 As for swaptions, a UTI shall be allocated at the time of the new transaction. Then, following the exercise
of swaptions, a new UTI shall be allocated respectively to each underlying swaps, and the existing UTI
shall be reported as prior UTI.
8 The same approach applies to partial unwind.
9
 In the case of a full novation, a new UTI should be allocated to the transaction at the time of the novation
(where the counterparty has changed), and the existing UTI of the original terminated transaction should
be reported as prior UTI. In the case of a partial novation, the UTI of the original transaction remains
unchanged. For the transaction corresponding to novation (which the counterparty has changed), new UTI
should be allocated, and the UTI of the original transaction should be reported as prior UTI.

## Page 58

10
(２)Outstanding transactions
There are two possible cases where a UTI field for outstanding transaction
needs to be updated after the new reporting requirement comes into effect:
(i) where no identifier is generated or (ii) where any relevant transaction
identifier such as Unique Swap Identifier(USI) or UTI not in line with Technical
Guidance is already generated. In the case of (i), a new UTI shall be generated
by the Reporting Entity, and in the case of (ii), the existing relevant transaction
identifier shall be reported. As for transactions executed between two or more
Reporting Entities, the newly generated UTIs for case (i) does not need to be
shared if the different newly generated UTIs are reported by each Reporting
Entities.

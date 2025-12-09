# uk emir reporting qas sep 2024

*Converted from: uk-emir-reporting-qas-sep-2024.pdf*

---

## Page 1

UK EMIR Reporting Q&As (applicable from 30 
September 2024)
Background
Under Article 9 of UK EMIR, the Bank of England and the Financial Conduct Authority (the 
FCA) (together, ‘the Authorities’) share responsibilities for the derivatives reporting 
obligation. The Bank of England is responsible for the framework for derivatives reporting 
as they apply to central counterparties (CCPs). The FCA is responsible for the reporting 
framework for all other counterparties. 
The FCA is responsible for Trade Repository (TR) requirements for procedures for 
reconciliation and to verify how complete and correct the data are.
Any subsequent references to ‘we, ‘us’ and ‘our’ in these Questions and Answers (Q&As)
should be read in this context and based on this split of responsibilities.
The draft Q&As should be read in conjunction with the FCA/Bank of England Policy 
Statement (PS 23/2) and the supporting documentation below (which are collectively 
referred to as “the new requirements”):
• The Bank of England Standards Instrument
o Note, all references to Table 1, Table 2 and Table 3 in the Q&A below refer 
to the tables in the Annex of EMIR Technical Standards on the Minimum 
Details of the Data to be Reported to Trade Repositories 2023.
• The technical specification documents:
o XML schemas under UK EMIR (applicable from 30 September 2024), 
together “the XML Schemas”
▪ Incoming messages to TRs (ZIP 4.4MB)
▪ Outgoing messages from TRs (ZIP 8.3MB)
o UK EMIR Validation Rules (applicable from 30 September 2024)
o The FCA’s European Market Infrastructure Regulation Rules (EMIRR) for 
TRs
When completed, these Q&A will be divided up into the following topics:
1. Transitional Arrangements 
2. Reconciliations
3. Errors and Omissions
4. Derivative Identifiers
5. Action and Events
6. Venues
7. Exchange Traded Derivatives
8. Margin and Collateral
9. Clearing

## Page 2

10.Position Level Reporting
11.Asset Class and Product Specific
Topics 1 to 5 are covered below. Q&As covering topics 6 to 11 are currently being 
consulted on. Following the conclusion of that consultation process in summer 2024, those 
Q&As will be finalised and added to this page. 
1. Transitional arrangements
The new requirements come into effect on 30 September 2024.
From 30 September 2024 all newly entered or modified derivative trades at both trade 
and position level will need to comply with the new requirements. 
For derivative trades entered into before 30 September 2024, there will be a 6-month 
transition period for entities responsible for reporting to update those outstanding 
derivative reports to the new requirements. This ends on 31 March 2025. 
This set of Q&As relates to the arrangements for transitioning to the updated derivative 
reporting framework under UK EMIR during the period from 30 September 2024 to 31 
March 2025. 
1.1How should derivative reports entered before 30 September 2024 that have not 
been updated to comply with the new requirements at the conclusion of the 
transition period on 31 March 2025, be treated?
Our expectation is for all entities responsible for reporting to ensure any outstanding 
derivative reports are updated to comply with the new requirements by the end of the 
transitional period on 31 March 2025.
We will monitor progress during the 6-month transition period. We expect entities 
responsible for reporting to proactively engage with us ahead of the completion of the 
transition period, with explanation, if they are at risk of not updating their outstanding 
reports to comply with the new requirements after 31 March 2025. We may consider 
using our supervisory powers in a proportionate and risk-based manner in the event of 
firms failing to meet the new requirements. 
1.2Should TRs terminate any derivative reports entered before 30 September 2024 
that have not been updated to comply with the new requirements at the 
conclusion of the transition period on 31 March 2025?
No. TRs should not unilaterally terminate outstanding derivative reports that have not 
been updated to comply with the new requirements after 31 March 2025.
TRs should take all reasonable steps to encourage entities responsible for reporting to 
ensure their outstanding derivative reports are updated to comply with the new 
requirements by the end of the transition period. However, it is the responsibility of

## Page 3

entities responsible for reporting to ensure all outstanding derivative reports comply 
with the new requirements by the end of the transitional period on 31 March 2025. 
We will monitor progress during the 6-month transition period. We expect entities 
responsible for reporting to engage with us, with explanation, if they are at risk of not 
being able to update their outstanding reports to comply with the new requirements 
after 31 March 2025. We may consider using our supervisory powers in a proportionate 
and risk-based manner where firms fail to comply with the new requirements.
1.3Will outstanding derivative reports that have not been updated to comply with 
the new requirements be subject to reconciliation during the transition period?
Yes. TRs should include all outstanding derivative reports in the reconciliation process 
(see Section 2 Reconciliation for further detail on the reconciliation process) regardless 
of whether they have been updated to comply with the new requirements or not. 
Reconciliations should be based on the new requirements. Only fields required to be 
reconciled under the new requirements should be subject to reconciliation. Fields that 
are no longer required under the new requirements do not need to be reconciled. 
We are aware this approach will result in reconciliation breaks during the 6-month 
transition period, particularly where one counterparty reporting a trade may have 
updated a report to comply with the new requirements but the other counterparty, 
reporting the same transaction, has not. However, we expect this to be a short-term 
issue, which will reduce as more reporting counterparties update their reports to 
comply with the new requirements. We will monitor progress during the 6-month 
transition period.
1.4Should TRs maintain the reconciliation status of an outstanding derivative report 
after it has been updated to comply with the new requirements?
No. The reconciliation status of outstanding derivative reports should be based on the 
most recent reconciliation. All reports subject to reconciliation should be included in the 
reconciliation process, regardless of whether they have been updated to comply with 
the new requirements. Once a report is updated to comply with the new requirements, 
a new reconciliation should take place. 
We are aware this approach will result in reconciliation breaks during the 6-month 
transition period, particularly where one counterparty reporting a trade may have 
updated a report to comply with the new requirements, but the other counterparty, 
reporting the same transaction, has not. However, we expect this to be a short-term 
issue during the transition period.
This will provide a more accurate view of reconciliation for Authorities.

## Page 4

1.5How should counterparties reporting at position level ensure outstanding 
reports are updated to comply with the new requirements, and which 
action/event type should be used in such circumstances?
Trade level derivatives that are included in a position are not outstanding and therefore 
do not need to be re-reported and updated to comply with the new requirements. Only 
the corresponding derivative at position level needs to be updated to comply with the 
new requirements, provided it is outstanding on 30 September 2024. 
As with other outstanding reports, outstanding position level reports should be updated 
to comply with the new requirements with the action type ‘Modify’ and event type 
‘Update’ before the conclusion of the transition period. However, this will not be 
necessary where counterparties have corrected or modified an outstanding report with 
the action type ‘Modify’ or ‘Correct’, since doing so will require updating the report to 
comply with the new requirements. Counterparties must ensure that outstanding 
position level reports that have not been modified or corrected during the transition 
period, regardless of whether daily valuation and collateral updates are being reported, 
are updated with the action type ‘Modify’ and the event type ‘Update’ since the daily 
valuation and collateral updates will not include details for every field. 
Counterparties should keep in mind acceptable action and event type combinations 
when reporting at position level. See also Section 5 Actions and Events.
1.6Do the XML schemas for TRs to Authorities allow for the reporting of derivatives
that have not been updated to comply with the new requirements?
Yes. We have provided a full suite of XML Schemas for reporting from 30 September 
2024 onwards. 
This includes ‘relaxed’ XML schema for the Trade State Report, Margin Derivative 
State Report, and Reconciliation Statistics Report. These permit TRs to submit details 
of all derivative reports, regardless of whether they have been updated to comply with 
the new requirements during the 6-month transition period. That is both those 
derivatives trades entered into or modified on or after 30 September 2024 that are 
subject to the new requirements and those derivative trades entered before to 30 
September 2024 which have not yet been updated to meet the new requirements.
Trade Activity, Margin Derivative Activity, Rejection Statistics, and Warning Statistics 
files must only include reports that have been updated to comply with the new 
requirements due to the ‘strict’ XML schemas that are in place for these files.
1.7In reports to the Authorities, should TRs make available details of derivative 
reports that have and have not been updated to comply with the new 
requirements?
Yes. TRs should include all derivatives reported by counterparties in the reports made 
available to Authorities, regardless of whether they have been updated to comply with

## Page 5

the new requirements or not, and where the relaxed schemas allow them to do so. See
our response to question 1.6.
1.8Do the XML Schemas for TRs to other TRs and reporting counterparties allow for 
reporting of derivatives that have not been updated to comply with the new 
requirements?
Yes, for certain types of reports where there is a ‘relaxed’ XML schema that can
accommodate derivative reports not updated to comply with the new requirements.
Specifically, the Trade State Report, Margin Derivative State Report, and Reconciliation 
Statistics Report files can include updated and non-updated contracts due to the 
relaxed schemas for these files. That is, both those derivatives trades entered into or 
modified on or after 30 September 2024 that are subject to the new requirements, and 
those derivative trades entered into before 30 September 2024 that have not yet been 
updated to meet the new requirements.
Trade Activity, Margin Derivative Activity, Rejection Statistics, and Warning Statistics 
files must only include updated reports that comply with the new requirements due to 
the ‘strict’ XML schemas that are in place for these files.
1.9In reports to other TRs and reporting counterparties, should TRs make available 
details of derivative reports that have and have not been updated to comply with 
the new requirements?
Yes. TRs should include all derivative reports in the reports made available to other 
TRs and entities responsible for reporting, regardless of whether they have been 
updated to comply with the new requirements where the type of report being shared
permits this due to the ‘relaxed’ XML schemas. See our response to question 1.8.
1.10 Will the ‘relaxed’ XML schemas be available after 31 March 2025?
No. Our expectation is that from 31 March 2025, all XML schemas will be ‘strict’. That 
is, they will only allow reports consistent with the new requirements to be reported. 
See also questions 1.1 and 1.2.
1.11 Will it be possible for outstanding derivative reports to be ported during the 
transition period?
Yes, outstanding derivative reports can be ported during the transition period. 
However, from 30 September 2024 any outstanding derivative reports that require 
porting must have been updated to comply with the new requirements. It will not be 
possible to port outstanding reports that have not been updated, as the relevant XML 
schema will only permit the sharing of updated records which comply with the new 
requirements between TRs. 
In the event a reporting counterparty wishes to move TR during the transition period, 
the reporting counterparty should ensure any outstanding derivative reports are 
updated to comply with the new requirements before porting to a new TR. Reporting

## Page 6

counterparties should keep this in mind when developing and implementing plans to 
ensure outstanding reports comply with the new requirements as it may impact 
reporting arrangements, for example, where firms use delegated reporting 
arrangements. 
2. Reconciliations
This set of Q&As relates to processes for reconciling data between TRs. TRs are required 
to establish procedures and policies to ensure the effective reconciliation of data between 
TRs and improve data quality under the FCA’s EMIRR. Entities responsible for reporting
are also required to have arrangements in place to ensure reconciliation breaks are 
resolved as soon as practicably possible (see Article 10 (3) of Technical Standards on the 
Minimum Details of the Data to be Reported to Trade Repositories 2023).
2.1How should reconciliations be performed for derivatives with 2 legs, such as 
interest rate swaps, where counterparties agree bilaterally on the sequencing of 
the legs? 
TRs should reconcile derivatives with 2 legs by reconciling each of the legs as reported 
by the counterparties. In most cases, including interest rate swaps, the 2 legs of a 
derivatives trade are not sequenced in a particular order. Accordingly, TRs should 
match the two legs using the values in the Direction of Leg 1 field (Table 1, Item 18)
with the opposite value, regardless of the order in which the legs were reported. This is
in line with the reconciliation ‘Conditions’ detailed in the UK EMIR Validation Rules 
(applicable from 30 September 2024) (‘Reconciliation Information’, Column J).
2.2 How often should TRs perform reconciliations?
As set out in PS 23/2, our expectation is for TRs to conduct reconciliations based on 
the latest reported value for each of the fields in Tables 1 and 2 of the Annex to the 
EMIR Technical Standards on the Standards, Formats, Frequency and Methods and 
Arrangements for Reporting 2023 as of the previous working day.
2.3 What information should TRs provide entities responsible for reporting to 
support the identification of reconciliation breaks and in what format should 
information on reconciliation breaks be provided?
As set out in PS 23/2, TRs are required to provide the results of the reconciliation 
process to entities responsible for reporting for each working day. This should allow 
entities responsible for reporting to easily identify and remediate reconciliation breaks. 
In terms of the format in which this information should be shared, TRs shall provide the 
results of the reconciliation process in an XML format and a template developed in 
accordance with the ISO 20022 methodology (available on the FCA’s UK EMIR 
Reporting obligation webpage). This should include information on the fields that have 
not been reconciled. However, we do not oppose TRs sending reports in other formats 
in addition to XML. TRs may take this decision individually based on the needs and 
requirements of their respective client base.

## Page 7

2.4 How should counterparties remediate reconciliation breaks?
Entities responsible for reporting are required to have arrangements in place to ensure 
the remediations of reconciliation breaks as soon as practically possible. As the nature 
and severity of reconciliation breaks will vary, we do not intend to provide prescriptive 
guidance as to when and how counterparties should remediate breaks. However, the 
expectation is that entities responsible for reporting have arrangements to remediate 
reconciliation breaks that are appropriate to the nature, scale, and complexity of their 
business.
2.5 What are the requirements for the operational elements of inter-TR 
reconciliation?
TRs must comply with the rules outlined in Section 2.3 of the FCA’s EMIRR relating to 
inter-TR reconciliation. TRs should have the flexibility to agree, between them, the best 
way in which they can meet the requirements in EMIRR 2.3 from an operational 
perspective. As such, we do not intend to provide more prescriptive guidance for TRs 
in this area at this time. However, we will continue to monitor the effectiveness of the 
inter-TR reconciliation process to determine whether further guidance may be needed. 
2.6 Can reconciliation reports differentiate between situations where a valuation 
has never been reported (‘missing’ valuations) and those in which a valuation 
has not been reported for at least 14 days (‘late’ valuations)?
No. Reconciliation reports do not distinguish between whether valuation updates are 
‘missing’ or ‘late’. 
However, it is possible under the Warnings XML schema to distinguish between 
‘missing’ valuations and ‘late’ valuations. As part of their end-of-day response 
mechanisms, TRs are required under section 2.4.1 of the FCA’s EMIRR to provide 
reporting counterparties with the outstanding derivative reports for which no valuation 
information has been reported, or the valuation information that was reported is dated 
more than 14 calendar days from the day for which the report was generated.
2.7Which fields are subject to reconciliation and reconciliation tolerance levels?
Details of the reportable fields that are subject to reconciliation and the applicable 
reconciliation tolerance levels, can be found in the UK EMIR Validation Rules 
(applicable from 30 September 2024) (‘Reconciliation Information’ sheet, Columns H￾J).
3. Errors and Omissions
Article 3 of the Technical Standards on the Minimum Details of the Data to be Reported to 
Trade Repositories 2023 requires reports to TRs to be complete and accurate. This set of
Q&As relates to the process for how counterparties should approach any errors and/or 
omissions with the UK EMIR reporting.

## Page 8

3.1What approach should entities responsible for reporting take when correcting 
errors and omissions in historic reports?
Entities with an obligation to report the details of derivative trades under Article 9 of 
UK EMIR are required to ensure that such details are complete, accurate and reported 
on time.
Entities responsible for reporting are expected to remediate all errors and omissions 
to their reports. This includes both live and matured trades regardless of age and any 
impacted position reports.
However, where remediation may be large and complex, entities responsible for 
reporting should engage bilaterally with the relevant Authority to agree a remediation 
plan that is proportionate to the complexity of the error and/or omission that requires 
remediation. 
Where any material errors or omissions are identified, entities responsible for reporting 
must notify the relevant Authority as soon as practicably possible.
• CCPs should notify the Bank of England by completing the Errors and Omissions 
form available on its website.
• All other reporting counterparties should notify the FCA by completing the Errors 
and Omissions form available on its website.
Whereas completion of the form can be performed by any party, it is the responsibility 
of the counterparty in scope of UK EMIR Article 9 reporting requirement who should 
submit the notification to the relevant Authority.
3.2What arrangements should entities responsible for reporting have in place to 
identify errors and omissions in their reported data?
At a minimum, we expect entities responsible for reporting to have systems and 
controls in place to ensure timely and complete reporting in accordance with Article 9 
of UK EMIR. 
In addition, entities responsible for reporting should ensure they have in place: 
• effective governance to oversee their UK EMIR reporting; 
• effective systems and controls to identify and remediate errors and omissions 
(including the notification of any errors and omissions to the relevant Authority); and
• arrangements with counterparties to address reconciliation breaks. 
Entities responsible for reporting should assess the materiality of any errors or 
omissions in their UK EMIR reporting (including identification of any errors and 
omissions that are to be reported to the relevant Authority) based on the size, nature, 
and complexity of their business. 
3.3How should entities responsible for reporting use the information in the 
reconciliation reports they receive from TRs?
Entities responsible for reporting should use reconciliation reports received from TRs
to validate the contents of their reports with their counterparties. All entities

## Page 9

responsible for reporting should have arrangements in place with their counterparties 
to ensure any reconciliation breaks are appropriately resolved as soon as practicably 
possible. 
The severity and drivers of reconciliation breaks will differ. As such, more prescriptive 
timelines within which entities should remediate breaks would not be appropriate for 
the remediation of certain reconciliation breaks.
3.4What is the status of reports included in the Warnings Feedback message
provided by TRs? How should entities responsible for reporting use the 
Warnings Feedback message? 
The Warnings Feedback message provided by TRs to entities responsible for 
reporting is to identify missing data and potential outlier values without rejecting the 
reports and to help reporting counterparties identify and remediate possible errors and 
omissions within reported data. The reports included within the Warnings Feedback 
message have been accepted by the TR which is reflected in its status (Acknowledged 
or ACK). 
Entities responsible for reporting should use the information provided in the Warnings 
Feedback message to monitor the accuracy of their reporting by investigating the 
potential issues. They should then confirm if remediation is required to correct any 
errors or omissions without undue delay to comply with Article 9 UK EMIR, including 
by submitting an Errors and Omissions form on the appropriate Authority’s website 
where necessary. 
3.5What are the thresholds used to identify outlier values? 
In accordance with the provisions of Section 2.4 of the FCA’s EMIRR, TRs will be 
required to notify entities responsible for reporting of any reports where the notional 
amount exceeds a threshold for that class of derivative as part of the Warning 
Feedback message. The intention of having thresholds to identify outlier values is to 
identify possible erroneous reporting of notional amounts in a particular asset class 
that would materially affect the Authorities’ view of the largest exposures in a particular 
asset class. 
To achieve this outcome, the Authorities propose to co-ordinate with UK TRs to 
implement a set of thresholds to make the Warnings Feedback message a useful and 
consistent data quality metric for both industry and Authorities. We will request that 
TRs make these thresholds available to clients in an easily accessible manner once 
they have been established.
Authorities will continue to monitor the introduction of the Warnings Feedback 
message, including the on-going effectiveness of the thresholds set. 
3.6How should derivatives reported under the old requirements and subsequently 
need to be revived be reported? 
Where a reporting counterparty uses the Revive action type to reopen a report that has 
not been updated to comply with the new requirements, for example to correct errors in 
matured trades, the reporting counterparty should provide all relevant details to update

## Page 10

the report to comply with the requirements as of the date of the revival action. This is 
the same approach as for any revived report.
Counterparties are expected to provide all the relevant data to update revived reports 
so they comply with the new requirements. But if this is not possible, counterparties are 
expected to proactively engage with us, with an explanation and a proposed solution.
4. Derivative Identifiers
Amendments to the UK EMIR reporting framework introduces new requirements for the 
use of Unique Product Identifiers (UPIs) and updated requirements relating to Unique 
Transaction Identifiers (UTIs) and Legal Entity Identifiers (LEIs). This set of Q&As gives 
further guidance on how these identifiers should be reported. 
4.1Should pre-existing UTIs be modified?
No. In line with the UK EMIR Validation Rules (applicable from 30 September 2024), 
UTIs should not be amended once they have been reported. 
As set out in CP21/31, we are not expecting the generation of new UTIs for 
outstanding trades and positions and the UK EMIR Validation Rules (applicable from 
30 September 2024) permit the use of old format UTIs to reflect this. UTIs allocated to 
a trade or position should remain the same throughout the lifetime of the trade or 
position and a new UTI should be used only if a trade or position is replaced by one or 
more trades or positions, for example following a post trade risk reduction (PTRR) 
event. Therefore, TRs should reject any modifications to pre-existing UTIs.
4.2How should UTIs be treated when they are generated by non-UK counterparties 
under different reporting requirements?
The updated UTI structure in UK EMIR is based on CPMI-IOSCO Technical Guidance 
on the Harmonisation of the Unique Transaction Identifier. UTIs generated by non-UK 
counterparties pursuant to a different reporting regime should align with the formatting 
requirements under UK EMIR meaning they can be treated in the same manner as 
UTIs generated under UK EMIR. 
Noting there may be differences in implementation timelines for the updated UTI 
structure between jurisdictions which may present issues, we will monitor progress and 
consider if further guidance is necessary.
4.3Should UTIs generated by trading venues incorporate the existing trading venue 
transaction identification code (TVTIC) as reported under UK MiFIR?
There is no requirement for UTIs generated by trading venues to incorporate the 
trading venue’s TVTIC into the UTI. In line with Article 8 of the Technical Standards on 
the Standards, Formats, Frequency and Methods and Arrangements for Reporting 
2023, UTIs must be composed of the LEI for the counterparty who generated the UTI

## Page 11

followed by a code of up to 32 characters which should be unique at the level of the 
generating entity.
While a trading venue’s TVTIC can’t be used in place of a UTI, there is nothing to 
prevent trading venues from incorporating an existing TVTIC into the UTIs it generates 
provided the UTIs continue to meet the requirements in Article 8 Technical Standards 
on the Standards, Formats, Frequency and Methods and Arrangements for Reporting 
2023.
4.4 When should International Securities Identification Numbers (ISINs), UPIs and 
Classification of Financial Instrument (CFI) codes be used in combination?
Article 7 of the Technical Standards on the Standards, Formats, Frequency and 
Methods and Arrangements for Reporting 2023, requires derivatives to be identified 
with an ISIN where the derivative is either:
• admitted to trading or traded on a trading venue; or 
• traded on a systematic internaliser (SI) and the underlying is admitted to trading 
or traded on a trading venue or an index or basket composed of instruments 
traded on a trading venue. 
Where a derivative does not meet one of these conditions it should be identified with a 
UPI, regardless of whether the derivative has an ISIN. Accordingly, ISINs and 
UPIs should not be used in combination and the UK EMIR Validation Rules (applicable
from 30 September 2024) will not permit the reporting of a UPI where an ISIN is 
provided.
CFI codes should be provided where possible for all derivatives in addition to an ISIN 
or UPI depending on whether it is admitted to trading or traded on a trading venue or 
SI.
4.5 What should be used if an ISIN does not exist for a derivative traded on a third 
country organised trading platform?
A product identifier is not required to be reported for derivatives executed on a third 
country organised trading platform if neither an ISIN nor a UPI exist.
4.6 Should fields which overlap with UPI reference data be reported?
Yes. Entities responsible for reporting must report all the applicable fields specified in 
the Technical Standards on the Minimum Details of the Data to be Reported to Trade 
Repositories 2023 including those which overlap with UPI reference data. 
However, we will continue to monitor the implementation of the UPI system under the 
UK regime and will communicate any developments accordingly.
4.7 Are TRs required to enrich reports with data derived from the UPI database?
No. TRs are not required to enrich reports as entities responsible for reporting must 
continue to report fields which overlap with UPI reference data.

## Page 12

However, we will continue to monitor the implementation of the UPI system under the 
UK regime and will communicate any developments accordingly.
4.8 Are entities responsible for reporting required to ensure the LEI of their 
counterparty has not lapsed?
No, except in the case of mandatory delegated reporting.
Article 4 of the Technical Standards on the Standards, Formats, Frequency and 
Methods and Arrangements for Reporting 2023, requires entities responsible for 
reporting to ensure the reference data related to their LEI is renewed in accordance 
with the terms of any of the accredited Local Operating Units of the Global LEI 
System.
For mandatory delegated reporting, the non-financial counterparty (NFC) is 
responsible for renewing and maintaining its LEI as explained in PS23/2. But as 
required under Article 10 of the Technical Standards on the Standards, Formats, 
Frequency and Methods and Arrangements for Reporting 2023, financial 
counterparties must have in place arrangements for due renewals by the NFC of its 
LEI to ensure accurate reporting for which the FC is solely responsible and legally 
liable. 
Accordingly, the UK EMIR Validation Rules (applicable from 30 September 2024)
require the LEI status of Counterparty 1 (Table 1, Item 4) and the Entity Responsible 
for Reporting (Table 1, Item 3) to be Issued, Pending transfer or Pending archival for 
certain action types. However, for Counterparty 2 (Table 1, Item 9) the LEI status may 
be ‘lapsed’ for certain action types. The Validation Rules provide further details as to 
what LEI status is required for the different action types.
4.9 Should TRs validate LEIs against the Global LEI Foundation (GLEIF) database 
based on the Reporting Timestamp (Table 1, Item 1) field?
Yes. TRs should, where applicable, validate LEIs against the GLEIF database as of 
the date reported in the Reporting Timestamp field.
5. Actions and Events
The combination of Action Type and Event Type clarifies the reasons why a report is made 
(e.g a new trade, an early termination, a modification due to a step-in event). The new
requirements introduce a new action type, Revive, which can be used when re-opening a 
derivative at trade or position level. This set of Q&As provides further guidance on how 
action types and events should be reported consistently. 
5.1Does the new Event Date field (Table 2, Item 153) impact how TRs should 
validate reports depending on action type?
Yes. The new Event Date field will impact TR validation of reports, dependent on 
which action type is reported. 
For details on how the Event Date is limited depending on action type, see the UK 
EMIR Validation Rules (applicable from 30 September 2024) where we detail our

## Page 13

expectations in the 'Trade validations auth.030' sheet in Table 2, Item 153 Validation 
Rules.
5.2How does the new Event Date field (Table 2, Item 153) affect how TRs validate 
records?
The Event Date field affects several TR validation steps. Primarily, it is used in 
conjunction with the Reporting Timestamp field (Table 1, Item 1) to validate the order 
of incoming submissions. The Event Date field is also used to determine whether the 
LEI status of various parties to a trade needs to be validated and, in instances where 
the Valuation Timestamp (Table 2, Item 23) field is populated, it should match the 
Event Date field.
For full details on how the Event Date field restricts other fields, see the UK EMIR 
Validation Rules (applicable from 30 September 2024) where we detail our 
expectations in the 'Trade validations auth.030' sheet and the 'Margins validations 
auth.108' sheet.
5.3What should be reported when a transaction that has been included in a position 
is identified as incorrect?
In this scenario, correction reports should be submitted for both the original 
(terminated) transaction and any impacted position reports. The transaction should not 
be revived.
Figure 5.1 illustrates a scenario where a transaction is reported incorrectly and 
subsequently compressed into a position.

## Page 14

Figure 5.1: Transaction compression and position creation
5.4 How can action type be used to get the latest state of a derivative trade?
There are four states (Not reported, Outstanding, Terminated and Errored). The state 
of a derivative contract resulting from an action depends on the latest action and the 
previous state.
Figure 5.2 illustrates how the action type and the previous state determine the current 
state of a derivative contract.

## Page 15

Figure 5.2: Allowable series of action types
This diagram has been drafted using material downloaded from the European Securities and 
Markets Authority’s (ESMA’s) website. ESMA does not endorse this publication and is in no way is 
liable for copyright or other intellectual property rights infringements nor for any damages caused 
to third parties through this publication.
5.5 What states can a trade be revived from?
As set out in Figure 5.2 (see question 5.4), trades can be revived from Terminated or 
Errored states. This includes trades that terminated due to reaching the contracted 
maturity date.
Figures 5.3 and 5.4 illustrate scenarios where transactions are revived from 
Terminated and Errored states.

## Page 16

Figure 5.3: Illustration of early termination and revive
Figure 5.4: Illustration of error and revive

## Page 17

5.6 What are the possible combinations of action and event type?
The possible combinations of action and event type, and when they can be used, are 
described in table 5.1 below.
Table 5.1: Applicability of Action type – Event type combinations
Action type Event type Applicability Comments
New Trade
When a derivative with a new UTI is created 
for the first time through a trade, and not
because of another prior event.
Combination ‘New’-‘Clearing’ should be 
used for the new derivatives resulting 
from clearing, in particular for derivatives
traded on trading venues and cleared on
the same day by a CCP.
New Step-in
When a derivative or position with a new
UTI is created for the first time
due to a step-in event.
New PTRR
When a derivative with a new UTI is created
for the first time due to a PTRR event.
Combination ‘New’-‘PTRR’ at position
level is not applicable, as any derivative
newly created due to a PTRR event is
expected to be reported at trade level 
(without prejudice to the possibility of
including such derivative subsequently 
in a position).
Combination ‘New’-‘PTRR’ can be used 
in case of rebalancing.
New Clearing
When a derivative with a new UTI is created
for the first time due to a Clearing event.
This combination also includes a 
clearing of OTC derivatives that were
previously bilaterally agreed among
counterparties and subsequently 
cleared.
New Exercise
When a derivative with a new UTI is created
for the first time due to an Exercise event.
This combination should be used when 
reporting the underlying swap following
the execution of a swaption.
New Allocation
When a derivative with a new UTI is created
for the first time due to an Allocation event.
New Inclusion in 
position
When a new position is created by inclusion
of trades in that position for the first time.
New
Corporate
Event
When a derivative or position with a new
UTI is created for the first time due to a 
corporate action on the underlying equity.

## Page 18

Action type Event type Applicability Comments
Modify
Trade
When a derivative or position with an
existing UTI is modified due to renegotiation
of the terms of the trade, because of the
changes to the terms of the trade agreed
upfront in the contract (except for when such 
changes are already reported e.g. notional
schedule) or because previously not 
available data elements become available.
Modify Step-in
When a derivative or position with an
existing UTI is modified due to a Step-in 
event.
This combination includes also a 
transfer of a derivative at trade or
position level from one CCP to 
another.
Modify PTRR
When a derivative or position with an
existing UTI is modified due to a PTRR 
event.
Combination ‘Modify’-‘PTRR’ at position
level should only be used in the case 
where CCP positions are subject to 
PTRR (rather than bilateral netting and 
subsequent reporting at position
level).
Combination ‘Modify’-‘PTRR’ can be
used in the case of compression.
Modify
Early 
termination
When a derivative or position with an
existing UTI is modified due to an early
termination agreed in advance or due to a 
partial termination.
In the case of an early termination
agreed in advance, the counterparties
should update the maturity date. In the
case of partial early termination, the 
counterparties should update the 
notional.
Modify Exercise
When a derivative or position, is amended
due to the exercise of an option or
swaption.
Modify Allocation
When a derivative with an existing UTI is 
partially allocated. This is used to report the
amended notional of the existing derivative.
Modify
Credit 
event
When a derivative or position with an
existing UTI is modified due to a Credit
event.
Modify
Inclusion in 
position
When a position with an existing UTI is
modified because of inclusion of a new
trade.
Modify
Corporate
Event
When a derivative or position with an
existing UTI is modified due to a corporate
action on the underlying equity.
Modify Update
When a derivative or position that is 
outstanding on the reporting start date is
updated to conform with the new
requirements.

## Page 19

Action type Event type Applicability Comments
Modify No event 
type 
required
When a position with an existing UTI is
modified due to more than one type of
business event that occurred intraday.
Intraday reporting is not mandatory 
for ETDs, consequently counterparties
are allowed to report ‘Modify’ at position
level without indicating the event type,
where such modification is a result of
more than one type of business event 
that occurred intraday.
Correct
No event 
type 
required
When a derivative or position with an
existing UTI, or the data related to the
collateral, is corrected because of an
earlier submission of incorrect information.
Terminate Step-in
When a derivative or position with an
existing UTI is terminated due to a step-in 
event. This is used for terminating the old 
UTI post step-in.
Terminate PTRR
When a derivative or position with an
existing UTI is terminated due to
a PTRR event. This is used for terminating
the old UTI(s) after PTRR operation.
Combination ‘Modify’-‘PTRR’ can be 
used in the case of compression.
Terminate
Early 
termination
When a derivative or position with an
existing UTI is terminated due to an early
termination (and when no other cause/event
is known as the reason for that termination).
Terminate Clearing
When a derivative with an existing UTI is
terminated due to a Clearing event. This is
used for terminating alpha trades.
In the case of OTC derivatives 
concluded bilaterally, counterparties
need to terminate the previously
reported bilateral trades (with 
combination ‘Terminate’-‘Clearing’) and
report the new cleared trades (with
combination ‘New’-‘Clearing’). This also
includes a scenario where existing 
derivatives become eligible for clearing
at a later stage.
Terminate Exercise
When a derivative with an existing UTI is
terminated due to an exercise event. For 
example, this is used for terminating
options/swaptions when these are being
exercised.
‘Terminate’ - ‘Exercise’ should not be
reported when the option is exercised on
the maturity date. More generally, only
terminations that take place at a date
prior to the maturity date should be
reported.
Terminate Allocation
When a derivative with an existing UTI is
terminated due to an allocation event. This is 
used for terminating the old UTI post 
allocation.

## Page 20

Action type Event type Applicability Comments
Terminate
Credit 
event
When a derivative or position with an
existing UTI is terminated due to a Credit 
event.
This combination should be reported
when a credit event leads to termination
and settlement of the derivatives, e.g. 
single name CDS.
Terminate
Inclusion in 
position
When a derivative or position with an 
existing UTI is terminated due to inclusion in 
a position.
A derivative at trade level that is 
immediately included into a position, 
should be reported with action type 
‘Position component’. Only when a 
derivative is included in the position after 
being reported with action type ‘New’, it 
should be reported with action type 
‘Terminate’ and event type ‘Inclusion in 
position’.
Terminate
Corporate
Event
When a derivative or position with an existing 
UTI is terminated due to a corporate action 
on the underlying equity.
Error
No event 
type 
required
When a derivative or position with an existing 
UTI is cancelled due to an earlier submission 
of incorrect information. For example, this is 
used to cancel the UTI of a derivative or 
position that should not have been reported 
(e.g. it is not a derivative transaction) or to 
cancel outstanding derivatives when the 
counterparty starts to benefit from an 
intragroup exemption.
Revive
No event 
type 
required
When a derivative or position that has been 
cancelled is reinstated due to an earlier
submission of incorrect information. For 
example, this is used to reinstate the UTI of 
a derivative or position that has been
erroneously terminated.
This action type should not be used to 
reopen a position that was previously 
netted and terminated. ‘Revive’ should 
only be used to reopen the trades that 
were terminated or cancelled by mistake
or which were cancelled due to IGT 
exemption, so that the counterparties do 
not need to regenerate a new UTI. It 
should not be used for other reporting 
scenarios. In particular in the case of 
netted position, the counterparties need 
to decide if they maintain the position 
open (and report the valuation
accordingly) or they close the position. If
the counterparties close the position and 
then they enter into another derivative 
contract of the same type and want to 
report at position level, they need to 
report a new position with a new UTI.
Valuation
No event 
type
required
When data related to the valuation are 
submitted for a derivative or position with an 
existing UTI.

## Page 21

Action type Event type Applicability Comments
Margin 
update
No event 
type
required
When data related to the collateral are 
submitted for a derivative or position with an
existing UTI.
Position 
component
No event 
type
required
When a new derivative is concluded and 
included in a position on the same day.
This table has been drafted using material downloaded from ESMA’s website. ESMA does not 
endorse this publication and is in no way is liable for copyright or other intellectual property rights 
infringements nor for any damages caused to third parties through this publication.

# hktr reporting service reference manual

*Converted from: hktr-reporting-service-reference-manual.pdf*

---

## Page 1

OTC Derivatives Trade Repository 
Reporting Service 
Reference Manual 
Date: December 2013 
Version: v.1.3

## Page 2

(This page is intentionally left blank)

## Page 3

VERSION HISTORY 
Effective Date Paragraphs Amendments 
July 2013 First issue v.1.0 
(10 December 2012) 
Not applicable 
July 2013 Updated v.1.1 
(30 April 2013) 
(1) Removed “CMU” from all 
references to the trade repository 
or its members, and replaced 
“CMU” by “HKMA” in 
references to the operator of the 
TR, to better reflect that the CMU 
and the TR are operating 
independently of each other 
(2) Changed all references to “FinNet” 
to “ICLNet” as the operation of 
FinNet was taken over by the 
HKICL in March 2013, and the 
service was renamed to become 
ICLNet 
(3) Updated 3rd and 4th paragraph of 
Clause 2 on background to reflect 
the implementation of the Interim 
Reporting Arrangement by the 
HKMA 
(4) Added the Agency Terms to be 
observed by reporting agents 
nominated by TR Members: 
 - updated 2nd and 5th paragraph 
 of Clause 7.2 
- updated Appendix TR.8 , the 
 “Agent Nomination Form” 
- added “Agency Terms” as an 
 appendix to Appendix TR.8 
- updated Appendix TR.9A to 
 align with the descriptions in 
 the updated Appendix TR.8 
(5) Revised 1st paragraph of Clause 
8.3 to clarify that part of the 
Mandatory Information required 
to be submitted to the TR is 
conditional in nature 
-i-

## Page 4

Effective Date Paragraphs Amendments 
July 2013 Updated 
(30 April 2013) 
(cont’d) 
(6) Updated the description for Global 
LEI in 2nd paragraph of the 
description for Global LEI in the 
“Identifiers for reporting or 
transacting parties” section of 
Clause 8.4 and in Note 1 of 
Appendix TR.3, to reflect the 
latest international standards on 
issuance of pre-LEIs 
(7) Added a new paragraph (last 
paragraph) to Clause 9.2 to clarify 
that the linking report produced by 
the TR system is an optional tool 
to facilitate TR Members to 
identify and resolve potential 
reporting errors 
(8) Insertion of a Personal 
Information Collection Statement 
as Annex 7 to meet the relevant 
requirements in the Personal Data 
(Privacy) Ordinance 
(9) Miscellaneous changes 
July 2013 Updated v.1.2 
(26 July 2013) 
(1) Revised the 3rd paragraph of 
Clause 4.1 in regard of change to 
member list. 
(2) Revised the 5th paragraph of 
Clause 4.1 to reflect service 
subscription information on TR 
Members will be available in the 
TR Member List. 
 
(3) Revised the 2nd paragraph of 
Clause 8.1 to require no report 
should be made when no change 
to a reported trade. 
 
(4) Revised the 3rd paragraph of 
“Maintenance of reporting or 
transacting party identifiers at the 
HKTR” under Clause 8.4 to 
-ii-

## Page 5

July 2013 Updated 
(26 July 2013) 
(Cont’d) 
reflect information on changes of 
TR Members’ third party￾assigned identifiers will be 
available to TR Members. 
(5) Updated Annex 2 Fee Scale for 
Reporting Service. 
December 2013 Updated v.1.3 
(2 December 2013) 
(1) Updated the 3rd and 4th paragraph 
of Clause 2 to reflect the 
introduction of interim reporting 
requirements by the HKMA 
(2) Updated the 5th paragraph of 
Clause 8.4 to reflect the latest 
development on the Global LEI 
System 
(3) Updated the 2nd paragraph of 
Clause 8.6 on the description of the 
service outage window of the 
HKTR 
(4) Updated the 1st and 2nd paragraph 
of Clause 9.2 to provide better 
clarity on the transaction linking 
process 
(5) Updated the notes under the table 
for identification number in 
Appendix TR.3 to reflect the latest 
development on the Global LEI 
System and to clarify the 
requirement for SWIFTBIC 
-iii-

## Page 6

(This page is intentionally left blank)

## Page 7

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 1 
CONTENTS
Clause Page
1. INTRODUCTION……………………………………………………………………….. 5 
1.1 Purpose…………………………………………………………………………………...... 5 
1.2 Contact for TR Service…………………………………………………………………….. 5 
1.3 Related Documents………………………………………………………………………... 6 
1.4 Operating Procedures……………………………………………………………………… 6 
2. BACKGROUND………………………………………………………………………….. 7 
2.1 Enquiries on Mandatory Reporting Requirements……………………………………….. 8 
3. REPORTING SERVICE……………………………...…………………………………. 9 
3.1 HKTR Reporting Service Product Scope………………………………………………….. 9 
3.2 Business Day………………………………………………………………………………. 10 
4. PARTICIPATION PROCEDURES…………………………………………………….. 11 
4.1 TR Membership……………………………………………………………………............. 11 
4.2 Operational Information…………………………………………………………………..... 12 
4.3 Obligations of TR Member………………………………………………………………… 13 
5. LEAVING THE REPORTING SERVICE……………………………..………………. 14 
5.1 Termination Notice………………………………………………………………………… 14 
5.2 Termination Arrangements………………………………………………………………… 14 
6. SUSPENSION OR TERMINATION BY THE HKTR………………………………… 15 
6.1 Suspension or Termination of Access to Service………………………………………….. 15 
7. CONNECTING TO THE HKTR………………………………………………………... 16 
7.1 Connection and Information Submission Channels………………………………………... 16 
7.2 Submission of Trade Information through an Agent………………………………………. 16 
8. TRADE INFORMATION SUBMISSION………………………………………………. 19 
8.1 Trade Information Submission Approach………………………………………………….. 19 
8.2 Responsibility of Submitting Trade Information………………………………………….. 20 
8.3 Scope of Trade Information to be Submitted………………………………………………. 21 
8.4 Format of Trade Information Submission…………………………………………………..22 
8.5 Timeframe for Trade Information Submission ……………………………………....…… .26 
8.6 HKTR System Window for Capturing Trade Information…………………...……………. 27

## Page 8

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 2 
Clause Page
9. TRADE VALIDATION AND LINKING……………………………………..…………28 
9.1 Transaction or Trade Event Validation…………………………………………………….. 28 
9.2 Transaction Linking…………………………….………………………………………….. 28 
10. REPORTING SERVICE REPORTS……………………………..…………………….. 30 
10.1 Types of Report……………………………………………………………………………. 30 
10.2 Reconciliation of Reports………………………………………………………………….. 30 
11. CONTINGENCY ARRANGEMENTS………………………………………………….. 31 
11.1 Local Terminal Service…………………………………………………………………….. 31 
11.2 Typhoon and Rainstorm Procedures……………………………………………………….. 31 
12. BILLING………………………………………………………………………………….. 32 
12.1 Settlement Arrangements………………………………………………..…………………. 32 
12.2 Billing Arrangements……………………………………………………………………… 33

## Page 9

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 3 
APPENDICES 
 Version date 
TR.1 TR Membership Application Form December 2012 
TR.2 TR Member Record of Authorized Signatures December 2012 
TR.3 TR Member Profile Maintenance Form December 2013 
TR.4 TR Member Administrative Account Setup Form December 2012 
TR.5 Broker List of TR Member December 2012 
TR.6 Designation of Hong Kong Dollar Account for Settling 
Fees and Charges 
December 2012 
TR.7 Direct Debit Limit of Settlement Bank December 2012 
TR.8 Agent Nomination Form (with Agency Terms) July 2013 
TR.9A Agent Profile Maintenance Form for Reporting Service July 2013

## Page 10

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 4 
ANNEXES 
 Version date Availability 
1 HKTR Reporting Service Product Scope July 2013 Attached 
2 Fee Scale for Reporting Service July 2013 Attached 
3 Reporting Service Agreement July 2013 Available on 
request 
4 Hong Kong Trade Repository 
Administration and Interface Development 
Guide – Reporting Service 
December 2013 Available on 
HKMA-TR 
Web 
5 HKTR Reporting Service Training 
Materials (Compact Disc) 
December 2013 Available on 
request 
6 Operating Procedures for Hong Kong 
Trade Repository – User Manual for 
Participants 
December 2013 Available on 
request 
7 Personal Information Collection Statement July 2013 Attached

## Page 11

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 5 
1. INTRODUCTION 
 This OTC Derivatives Trade Repository Reporting Service Reference Manual 
(“Manual”) describes the reporting service for over-the-counter (“OTC”) derivatives 
transactions (“Reporting Service”) provided by the OTC Derivatives Trade 
Repository (“HKTR”) of the HKMA to TR Members in accordance with, and subject 
to any limitations contained in their Reporting Service Agreements with the HKMA. 
Any of the provisions of this Manual or of circulars may be varied at any time upon 
written notice to that effect being given by the HKMA to TR Members without their 
agreements. 
1.1 Purpose 
Set out in this Manual are the procedures for TR Membership and communications, 
the security provision underlying the Reporting Service and details of the various 
processes. The Appendices at the back of this Manual provide sample forms for use 
by TR Members. 
1.2 Contact for TR Service 
 All requests for further information relating to the Reporting Service described in this 
document should be directed to: 
 
 Trade Repository, 
 Hong Kong Monetary Authority 
 55th Floor 
 Two International Finance Centre 
 8 Finance Street 
 Central 
 Hong Kong 
 Telephone : (852) 8100 3115 
 Facsimile : (852) 2878 1679 
 e-mail : hktr@hkma.gov.hk

## Page 12

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 6 
For technical support and enquiries on the operation of the computer system for 
accessing and making use of the Reporting Service, please contact the Hong Kong 
Interbank Clearing Limited (“HKICL”) at: 
 Services Support 
 Hong Kong Interbank Clearing Limited 
 Telephone : (852) 2533 1100 
 Facsimile : (852) 2533 1123 
 e-mail : hkicl@hkicl.com.hk 
1.3 Related Documents 
 The following documents issued by the HKMA may contain further information in 
relation to the operation of the Reporting Service:
(a) Operating Procedures for Hong Kong Trade Repository - User Manual for 
Participants (Administrative Functions) 
(b) Operating Procedures for Hong Kong Trade Repository - User Manual for 
Participants (Trade Functions – Reporting Service) 
(c) Operating Procedures for Hong Kong Trade Repository - User Manual for 
Participants (Trade Functions – Reporting Service - Appendix) 
(d) Hong Kong Trade Repository Administration and Interface Development Guide – 
Reporting Service (“Reporting Service AIDG”) 
1.4 Operating Procedures 
 For the sake of clarity, the term “Operating Procedures” mentioned in this Manual 
includes this OTC Derivatives Trade Repository Reporting Service Reference Manual 
and circulars issued by the HKMA from time to time.

## Page 13

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 7 
2. BACKGROUND 
The global financial crisis in 2008 triggered a global movement to improve 
transparency and reduce counterparty risks in the OTC derivatives markets, resulting 
in reforms to the OTC derivatives markets on various fronts. The reform measures 
adopted by the international regulatory community include requiring all OTC 
derivatives transactions be reported to trade repositories (“TRs”) and all standardized 
OTC derivatives transactions be cleared at central counterparty (“CCP”) clearing 
facilities. 
A TR is a centralised registry that maintains an electronic database of records of OTC 
derivatives transactions. By collecting and providing OTC derivatives transactions 
information to regulatory authorities, the TR plays a vital role in supporting 
authorities in carrying out their market surveillance responsibilities, which will help 
maintain stability of the financial systems. It also helps increase transparency in the 
market, promotes standardisation and provides a level of consistency in the quality 
and availability of transaction data. 
To meet international standards, the HKMA announced in December 2010 to 
establish a TR in Hong Kong under the Central Moneymarkets Unit (“CMU”), and 
that a link will be developed between the TR and the CCP for OTC derivatives to be 
launched by Hong Kong Exchanges and Clearing Ltd. to allow eligible transactions to 
be passed to the CCP for central clearing. The HKMA also worked in concert with 
the Government and the Securities and Futures Commission (“SFC”) to build a 
regulatory regime for the OTC derivatives markets under the Securities and Futures 
Ordinance (“SFO”), including requirements for mandatory reporting to the TR of the 
HKMA and mandatory clearing at designated CCPs. In August 2013, the HKMA 
introduced interim reporting requirements to require Licensed Banks (“LBs”) to 
report OTC derivatives transactions to the TR of the HKMA. The interim reporting 
requirements would remain in effect until the regulatory regime under the SFO takes 
effect.

## Page 14

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 8 
Under the regulatory regime to be effected by the SFO, Authorized Institutions (“AIs”) 
and Approved Money Brokers (“AMBs”) licensed and regulated by the HKMA under 
the Banking Ordinance, Licensed Corporations (“LCs”) licensed and regulated by the 
SFC under the SFO, and other Hong Kong persons involving in OTC derivatives 
transactions and meeting certain conditions will be required to report specified OTC 
derivatives transactions conducted, originated or executed by them to the HKTR. 
Under the interim reporting requirements, however, only LBs are mandatorily 
required to report, covering transactions they conduct with other LBs. Hereinafter, 
the regulatory regime to be effected by the SFO and the interim reporting 
requirements will be collectively referred to as “OTC regulatory regime”. 
The HKTR provides an electronic system for collecting, keeping and maintaining 
details of OTC derivatives transactions efficiently, securely and in conformity with 
market standards. Entities subject to mandatory reporting requirements under the 
OTC regulatory regime can discharge their reporting obligations only by reporting to 
the HKTR. 
2.1 Enquiries on Mandatory Reporting Requirements 
AIs should direct their enquiries on the mandatory reporting requirements to their 
usual supervisory contacts at the Banking Supervision Department of the HKMA. 
AMBs should direct their enquiries on the mandatory reporting requirements to their 
usual contacts at the Payment Systems Oversight and Licensing Division of the 
Banking Conduct Department of the HKMA. 
 Entities or persons other than an AI or an AMB should direct their enquiries on the 
mandatory reporting requirements to the SFC at: enquiry@sfc.hk.

## Page 15

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 9 
3. REPORTING SERVICE 
The HKTR provides service to TR Members who are or may be subject to the 
mandatory reporting requirements under the OTC regulatory regime for capturing, 
maintaining and updating the details of OTC derivatives transactions through its 
electronic system (“HKTR system”), primarily for the TR Members to discharge their 
mandatory reporting obligations. 
Transactions reported to the HKTR are effected by agreements between the parties to 
the transactions. The fact that they are reported to and maintained by the HKTR does 
not of itself confer any legally binding effect on such transactions. 
3.1 HKTR Reporting Service Product Scope 
 The types of OTC derivatives product supported by the Reporting Service of the 
HKTR (“HKTR Reporting Service Product Scope”) are basically determined with 
reference to the types of product subject to mandatory reporting under the OTC 
regulatory regime. 
Over time, new OTC derivatives products may be added to the Reporting Service as 
the scope of products subject to mandatory reporting under the OTC regulatory 
regime expands. 
The HKTR Reporting Service Product Scope can be found in Annex 1. The updated 
list is also available in the HKTR Section of the HKMA website. Changes to the list 
will be advised to TR Members through circulars. TR Members should also make 
reference to the OTC regulatory regime to ascertain, among the products supported by 
the HKTR, which products are subject to mandatory reporting.

## Page 16

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 10 
3.2 Business Day 
 The term “business day” as stipulated in this Manual means a day other than a 
Saturday, a Sunday or a day which is a general holiday as specified in the General 
Holidays Ordinance (Chapter 149 of the Laws of Hong Kong) except otherwise 
specified in the relevant chapters of this Manual.

## Page 17

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 11 
4. PARTICIPATION PROCEDURES 
4.1 TR Membership 
A reporting entity must join the HKTR as a TR Member before it can make reports of 
OTC derivatives transactions to the HKTR. 
Application for TR Membership must be made in writing to the HKTR. Prior to 
becoming a TR Member, each successful applicant is required to enter into a 
contractual agreement with the HKMA, i.e. the Reporting Service Agreement. Each 
successful applicant will be assigned and advised a unique TR Member code to 
represent its identity in the HKTR system. 
The list of TR Members and their TR Member codes can be found in the HKTR 
section of the HKMA website. The list will be updated regularly. Changes to the list 
will also be advised to TR Members. 
The Reporting Service Agreement, which incorporates the provisions of this Manual, 
as updated from time to time, together with any directions given in circulars by the 
HKMA, sets out the terms and conditions of the Reporting Service Agreement with 
which a TR Member is required to comply. 
It should be noted that apart from the Reporting Service, the HKTR may also provide 
matching and confirmation service to TR Members (“Matching and Confirmation 
Service”), primarily for facilitating them to fulfil their statutory clearing obligations 
under the OTC regulatory regime. The Matching and Confirmation Service is 
provided independently of the Reporting Service, and is subject to a different set of 
procedures. Transactions reported to the HKTR under the Reporting Service cannot 
be applied to the Matching and Confirmation Service. A TR Member may be 
subscribing to only one or both of the Services (Reporting Service and Matching and 
Confirmation Service) of the HKTR. The Service subscribed by individual Members 
is indicated in the List of TR Members published by the HKTR.

## Page 18

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 12 
4.2 Operational Information 
Before joining the Reporting Service, a TR Member must supply certain operational 
information to the HKTR by completing and submitting the following forms to the 
HKTR: 
(a) TR Membership Application Form, at Appendix TR.1 
(b) TR Member Record of Authorized Signatures form, at Appendix TR.2 
(c) TR Member Profile Maintenance Form, at Appendix TR.3 
(d) TR Member Administrative Account Setup Form, at Appendix TR.4 
(e) Broker List of TR Member (optional), at Appendix TR.5 
(f) Designation of Hong Kong Dollar Account for Settling Fees and Charges form, 
at Appendix TR.6 
(g) Direct Debit Limit of Settlement Bank form, if applicable, at Appendix TR.7 
Unless otherwise required by or agreed with the HKTR, the above completed forms 
must be submitted to the HKTR at least 10 business days before the date on which the 
TR Member can commence making use of the Reporting Service, subject to the 
completion of other relevant logistical and technical arrangements, e.g. access to 
different reporting channels (see Clause 7.1) may require different amount of lead 
time to establish. 
After the TR Membership has commenced, any changes to the operational 
information must be notified to the HKTR in writing, supported by updated version of 
the relevant forms, if applicable. Unless otherwise required by or agreed with the

## Page 19

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 13 
HKTR, TR Members should notify the HKTR a change at least 10 business days 
before the change takes effect. 
4.3 Obligations of TR Member 
 All TR Members must fulfil the following obligations: 
(a) All TR Members shall have systems in place which are complementary to the 
HKMA/HKICL’s contingency arrangements so as to enable HKMA/HKICL to 
ensure timely recovery of its usual operation in the event of occurrence of an 
adverse contingency affecting such operation. Such contingency arrangements 
shall be modified from time to time in the manner required by the HKMA, and 
the HKMA shall notify TR Members the changes accordingly. 
(b) TR Members shall participate in the contingency drills arranged by the 
HKMA/HKICL from time to time so as to verify the readiness of TR Members’ 
contingency arrangements. 
(c) TR Members shall participate in various member/simulation tests arranged by 
the HKMA/HKICL from time to time so as to prepare themselves ready for any 
new service to be launched. 
The HKMA will monitor through HKICL the performance by TR Members of these 
obligations under the arrangements. 
In the event that HKICL becomes aware of any non performance by any TR Member 
of its obligations under these arrangements, HKICL shall as soon as practicable 
inform the TR Member concerned and request it to ensure performance of the relevant 
provision, and inform the HKMA of such incident.

## Page 20

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 14 
5. LEAVING THE REPORTING SERVICE 
5.1 Termination Notice 
At least 30 calendar days’ notice in writing is required if a TR Member is to withdraw 
from the Reporting Service or terminate its TR Membership. 
5.2 Termination Arrangements 
 If a TR Member has not instructed the HKTR to quit the transactions at the HKTR (to 
signify that the Member will no longer report on the transactions) before leaving the 
Reporting Service or terminating its TR Membership, the HKTR will automatically 
apply a quit status to all the transactions of the Member on the date of the Member’s 
leaving the Service or terminating the Membership. 
After a TR Member leaves the Reporting Service, or terminates its TR Membership, 
the information of OTC derivatives transactions previously reported by the Member 
to the HKTR under the OTC regulatory regime will continue to be stored at the 
HKTR. However, the transaction records can no longer be amended or updated for 
events that happen after the date on which the TR Member leaves the Service or 
terminates the Membership.

## Page 21

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 15 
6. SUSPENSION OR TERMINATION BY THE HKTR 
6.1 Suspension or Termination of Access to Service 
Under the terms of the Reporting Service Agreement, the HKMA may suspend or 
terminate the membership of a TR Member or its access to the Reporting Service 
under specified circumstances. On suspension or termination of a TR Membership, 
the HKTR will: 
(a) prevent the TR Member from accessing the Reporting Service until the HKMA 
authorises otherwise. 
(b) inform other TR Members as soon as practicable about the suspension or 
termination. 
(c) where the TR Member subject to suspension or termination of access to the 
Reporting Service is an AI or an AMB, inform Banking Supervision 
Department or the Payment Systems Oversight and Licensing Division of the 
Banking Conduct Department of the HKMA respectively about the suspension 
or termination. 
(d) where the TR Member subject to suspension or termination of access to the 
Reporting Service is an entity or a person other than an AI or an AMB, inform 
the SFC about the suspension or termination. 
The Reporting Service will, however, continue to be in operation subject to the terms 
and conditions of the Reporting Service Agreement. Unlike in the case of termination, 
the HKTR will not apply a quit status to the transactions that the Member reported to 
the HKTR before the suspension. The transactions, however, will not be accessible 
by the Member for updating during the suspension period.

## Page 22

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 16 
7. CONNECTING TO THE HKTR 
7.1 Connection and Information Submission Channels 
 TR Members have to submit trade information of OTC derivatives transactions to the 
HKTR for reporting through the channels specified by the HKTR. All TR Members 
can submit trade information to the HKTR through internet. TR Members that are 
users of ICLNet and SWIFTNet can also submit trade information via such two 
channels. For the avoidance of doubt, TR Members may adopt multiple channels for 
the submission of trade information of different transactions, of same or different 
products, to the HKTR simultaneously. 
 The system connection and interface of TR Members with the HKTR for trade 
information submission should be developed and established in conformity with the 
specifications set out in the Reporting Service AIDG. Submission of trade 
information via the established channels must also be made in conformity with the 
standards specified in the AIDG, for example, standards of file format, file naming 
convention, configuration of parameters under different channels, user authentication, 
etc. 
7.2 Submission of Trade Information through an Agent 
The HKTR accepts TR Members to submit trade information for reporting through an 
agent. A TR Member opting to submit trade information through an agent has to 
nominate the agent to the HKTR. The agent can be a third party service vendor or 
another TR Member, including the counterparty to the TR Member in the transaction. 
TR Members may nominate an agent to the HKTR using the Agent Nomination Form 
at Appendix TR.8. The TR Member should specify the scope of information to be 
submitted by the agent on its behalf using the Agent Profile Maintenance Form for 
Reporting Service at Appendix TR.9A. The agent should acknowledge the 
nomination by the TR Member in both Forms, and supply certain operational

## Page 23

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 17 
information required by the HKTR, e.g. contact information, authorized signatories 
and technical information related to the connection and submission modes to be 
adopted by the agent. The agent should also agree to observe the terms and 
conditions for accessing the HKTR system (“Agency Terms”) specified by the HKTR 
(Appendix to Appendix TR.8). 
Subject to the agent meeting the relevant technical, logistical and documentation 
requirements to the satisfaction of the HKTR, the HKTR will confirm with the TR 
Member and the nominated agent the date for the nominated agent to commence 
reporting for the Member (in the form of the Approval Confirmation in Appendix 
TR.8). If an agent is not a TR Member, it will be assigned and advised of a unique 
Agent Code to represent its identity in the HKTR system. The HKTR system will 
reject trade information submitted by an agent on behalf of a TR Member before the 
commencement date for reporting by the agent as confirmed with the Member, or if 
the trade information submitted by the agent is not in conformity with the relevant 
standards. 
 According to the Reporting Service Agreement signed with the HKMA, the TR 
Member will assume full responsibility over the activity of its agent in accessing the 
Reporting Service on its behalf. 
 The termination of the appointment of an agent or any changes to the reporting scope 
of the agent must be notified to the HKTR in writing, supported by the updated Agent 
Profile Maintenance Form for Reporting Service, if applicable. Unless otherwise 
required by or agreed with the HKTR, TR Members should notify the HKTR a 
change at least 10 business days before the change takes effect. The Agency Terms 
applicable to an agent in respect of the agent’s appointment by a TR Member will 
cease to be effective when the agent’s appointment is terminated by the TR Member. 
 For the avoidance of doubt, a TR Member can simultaneously submit trade 
information directly and through agents. A TR Member can appoint multiple agents

## Page 24

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 18 
for submitting trade information, in same and different products. An agent can submit 
trade information on behalf of different TR Members.

## Page 25

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 19 
8. TRADE INFORMATION SUBMISSION 
8.1 Trade Information Submission Approach 
 The HKTR supports both the life-cycle approach and the snapshot approach for 
capturing and maintaining OTC derivatives transactions for reporting purposes. 
Except in the case of backloading an outstanding transaction to the HKTR, where the 
snapshot approach has to be adopted, reporting entities may opt to adopt the life-cycle 
approach or the snapshot approach for reporting trade events. For the avoidance of 
doubt, reporting entities may adopt different reporting approaches for different 
transactions. 
Under the life-cycle approach, reporting entities have to submit trade information at 
inception and on subsequent trade events individually and sequentially, in 
chronological order, as they occur until the expiry or scheduled termination of the 
transaction. Each submission made will therefore signify a single trade event. 
Reporting entities adopting the snapshot approach for reporting a transaction, on the 
other hand, have to report “snapshots” of the transaction, each may incorporate the 
effects of multiple trade events. The trade events covered by each snapshot, however, 
must take place on the same trade day. Like trade events under the life-cycle 
approach, snapshots of a transaction should be reported to the HKTR one by one 
sequentially and, in chronological order. Hereinafter, trade events under life-cycle 
reporting approach and snapshots under snapshot reporting approach are to be 
collectively referred to as “trade events”. For the avoidance of doubt, if there is no 
change to the information of a transaction reported to the HKTR, reporting entities 
should not make a report to the HKTR in respect of the transaction. 
In the case of backloading, TR Members have to submit trade information of the 
outstanding position (snapshot) of the transactions. New trade events of an 
outstanding transaction can be submitted to the HKTR only after the transaction has 
been backloaded to the HKTR.

## Page 26

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 20 
Trade events applicable to transactions in different types of OTC derivatives product 
may be different, due to differences in the economic substance and underlying of 
different products. Generally, the trade events supported by the HKTR for reporting 
include backloading, trade inception, amendment of transaction details and early 
termination of trade. In addition, TR Members may initiate requests to manage the 
trade events submitted to the HKTR, e.g. withdrawal, quit. For details of the trade 
events applicable to different products and under different circumstances, please refer 
to the Reporting Service AIDG. 
Each trade event should be backloaded or submitted to the HKTR only once. In the 
event that a TR Member is simultaneously making use of multiple channels or agents 
for trade information submission, it must ensure that there is no duplication of 
submission through the various channels and agents.
8.2 Responsibility of Submitting Trade Information 
According to the OTC regulatory regime if both transacting parties of an OTC 
derivatives transaction are subject to the mandatory reporting requirement, they are 
required to report trade information of their respective side of the transaction to the 
HKTR, except where an exemption applies, e.g. under the regulatory regime to be 
effected by the SFO, for Hong Kong persons other than an AI, LC or AMB 
transacting with an AI, LC or AMB on a transaction subject to mandatory reporting, 
they are not required to report the transaction if the transaction is reportable by the 
counterparty AI, LC or AMB. 
TR Members should make reference to and observe the requirements in the OTC 
regulatory regime in determining whether they are required to make a report on an 
OTC derivatives transaction to the HKTR.

## Page 27

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 21 
8.3 Scope of Trade Information to be Submitted 
The scope of information of a trade event of an OTC derivatives transaction required 
to be submitted to the HKTR for reporting purposes depends on the nature of the 
event, the type of product to which the transaction belongs and the relevant 
requirements of the OTC regulatory regime. The information to be reported is 
classified into mandatory and optional information. Mandatory information is 
information that a TR Member must supply to the HKTR. Mandatory information 
comprises information essential to the HKTR for administering and processing the 
transaction, e.g. purpose, event type, etc., and core transaction details, e.g. transacting 
parties, prices/rates, amounts, etc. Part of the Mandatory Information is conditional in 
nature, meaning that it is required only under specified condition(s), e.g. unique 
transaction identifier is required only if it exists for the transaction. Optional 
information is information that the TR Member can decide whether to supply together 
with the mandatory information, and mainly comprises transaction information other 
than the core details, e.g. payment and settlement conventions. 
For details of the information to be submitted for different trade events and products, 
and under different circumstances, and the classification of the information into 
mandatory and optional information, please refer to the Reporting Service AIDG. 
In response to local and international regulatory development, the scope of 
information to be submitted and the classification of the information into mandatory 
and optional information may be adjusted. The HKTR will notify TR Members of 
any changes, and update and re-issue the Reporting Service AIDG to specify the 
changes.

## Page 28

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 22 
8.4 Format of Trade Information Submission 
TR Members should observe the standards specified in the Reporting Service AIDG 
in terms of the format and contents of the information to be submitted to the HKTR 
for reporting purposes. 
Format of information submission 
Trade event records submitted to the HKTR must be in either Extensible Markup 
Language (“XML”) (the extended Financial Products Markup Language (“FpML”)) 
format or Comma Separated Value (“CSV”) format. The technical specifications for 
representing individual transaction details under the two formats, e.g. the nature, 
length and layout of the data strings, may also be different. A TR Member may opt to 
adopt the format that can best suit its requirements and technical capability. For the 
avoidance of doubt, a TR Member may opt to adopt different formats for submitting 
trade information of different transactions to the HKTR. For details of the technical 
specifications of trade information submission under the two formats, please refer to 
the Reporting Service AIDG. 
The HKTR accepts submission of a trade event request file containing records of 
multiple OTC derivatives transactions and multiple trade events of a transaction. 
When preparing and submitting files containing trade event information to the HKTR, 
reporting entities also have to observe other technical standards set out in the 
Reporting Service AIDG, e.g. file identification and authentication standards, and 
configuration standards applicable to the two information formats and different 
submission channels, i.e. internet, ICLNet and SWIFTNet. 
Contents of information submitted 
The contents of individual data strings contained in a transaction record should reflect 
the value of the corresponding transaction details applicable to or referred to in the 
trade event agreed by the transacting parties, e.g. the price/rate level, transaction

## Page 29

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 23 
amount, transaction date, etc., and may vary from one transaction to another. 
However, TR Members are required to observe the enumerations and coding schemes 
set out in the Reporting Service AIDG in representing some transaction details so as 
to facilitate processing of the transactions by the HKTR. The enumerations and 
coding schemes cover, for example, product codes, currency codes, reference rate 
codes, transacting party identifier codes, documentation codes, codes for signifying 
applicable payment or settlement conventions, etc. The majority of the codes 
specified in the enumerations and coding schemes are consistent with the practices 
and standards that have been widely adopted by the industry. 
Identifiers for reporting or transacting parties
 As set out in the enumerations and coding schemes in the Reporting Service AIDG, 
the HKTR can support several types of third party-assigned identifier for indicating 
the identity of the reporting or transacting party of a transaction. If none of such third 
party-assigned identifier is available for a party, a unique internal 
customer/counterparty reference code assigned by the reporting entity (same code to 
be used for identifying the same party in all transactions reported by the reporting 
entity) meeting the specifications in the AIDG can be used. Where a party possesses 
several types of third party-assigned identifiers, the identifier to be reported for 
indicating the identity of the party should be determined by the order of priority 
applicable to the different types of identifier specified by the HKTR, except where the 
party is a TR Member. Specifically, among the various types of third party-assigned 
identifier that may be available, the one of the highest level of priority in the 
following list should be reported to represent the identity of the party: 
1
st Priority: Global Legal Entity Identifier (“Global LEI”) issued under the Global 
LEI System established by the Regulatory Oversight Committee (ROC) 
of the Global LEI System. 
 If the Global LEI is not yet available, pre-LEI identification codes (“pre￾LEIs”) issued by pre-Local Operating Units (pre-LOUs) that have been

## Page 30

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 24 
endorsed by the ROC. The ROC will make an announcement when a 
pre-LOU is endorsed to issue pre-LEIs. The HKTR will notify TR 
Members the announcements made by the ROC. 
OR
TR Member code assigned and published by the HKTR 
2
nd Priority: SWIFT BIC (Business Identifier Code) issued by SWIFT under ISO 
9362 
3
rd Priority: Number of the Certificate of Incorporation (“CI”) (for locally 
incorporated companies)/Certificate of Registration (“CR”) (for 
companies incorporated overseas) issued by the Companies Registry of 
Hong Kong 
4
th Priority: Business Registration Number (“BRN”) issued by the Inland Revenue 
Department of Hong Kong 
Since TR Members are required to supply and update their own third party-assigned 
identifiers to the HKTR, a reporting entity can opt to report any one of such identifiers 
for a party if the party is a TR Member. The list of TR Members, their TR Member 
codes and other third party-assigned identifiers that they have registered with the 
HKTR can be found in the HKTR section of the HKMA website. The list will be 
updated regularly. Upon request of a counterparty TR Member, TR Members should 
supply the relevant identifiers to the counterparty TR Member for reporting to the 
HKTR. 
Reporting entities are not required and should not supply any identity information of 
transacting party that is a private individual. Where a transacting party is a private 
individual, reporting entities should supply to the HKTR a private and unique 
reference code for referring to the private individual (to be applied to all transactions

## Page 31

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 25 
with the same private individual), and have to indicate that the transacting party 
belongs to the private individual type. 
Maintenance of reporting or transacting party identifiers at the HKTR 
For transactions reported to the HKTR but not yet matured, TR Members are required 
to review the identifiers reported by them and update those that are no longer valid:- 
- for transactions carrying internal customer/counterparty reference codes, to 
review whether any of the third party-assigned identifiers specified by the 
HKTR have become available for the parties for whom the internal 
customer/counterparty reference codes have been reported, and replace the 
codes by the available third party-assigned identifiers of the highest level of 
priority 
- for transactions carrying third party-assigned identifiers, to review whether 
those identifiers have become invalid, e.g. the reporting or transacting party no 
longer possesses an identifier or an identifier of a higher level of priority has 
become available for the reporting or transacting party. The TR Member 
should obtain valid identifiers from the relevant parties and update the records 
at the HKTR. Again, no update is required to change any valid third party￾assigned identifiers reported for a TR Member. For the avoidance of doubt, 
after a TR Member relinquishes its Member status, the TR Member code 
reported for it should be replaced by another valid identifier according to the 
specified order of priority. 
The HKTR will notify TR Members when an entity becomes a TR Member, when a 
TR Member relinquishes the Member status or when a TR Member reports that its 
third party-assigned identifier(s) has/ have been changed, to facilitate TR Members to 
keep track of and report the appropriate identifiers arising from changes related to TR 
Member status or when any of the third party-assigned identifier(s) is no longer valid.

## Page 32

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 26 
For identifiers reported for parties that are not TR Member, TR Members should 
review and update them at least annually, say during annual reviews of the banking or 
trading facilities for the parties. The HKTR will issue half-yearly reminders to 
remind TR Members. 
Identifiers for transactions 
 To facilitate the HKTR system to link up two sides of a transaction reported by the 
two transacting TR Members, and to facilitate TR Members to efficiently identify and 
resolve potential reporting errors, TR Members on both sides of a transaction are 
required to supply a unique and same transaction identifier (“UTI”) when reporting 
their respective side of the transaction to the HKTR. To facilitate future global 
sharing and aggregation of TR data, the HKTR does not require a UTI be developed 
specifically for Hong Kong but would adopt the UTI required under other 
jurisdictions. The acceptable UTI is specified in the Reporting Service AIDG. Over 
time, UTI in other jurisdictions may be added and the HKTR will notify TR Members 
accordingly. The TR Member possessing the specified UTI should supply the UTI to 
the counterparty TR Member for reporting, e.g. when only one side of the transaction 
is subject to the reporting requirement in the relevant jurisdiction. 
 If a specified UTI is not available for a transaction, the transacting TR Members may 
opt to agree among themselves a unique link reference for the transaction and supply 
the reference as optional information to the HKTR to aid in the trade linking and error 
resolution processes. 
8.5 Timeframe for Trade Information Submission 
The HKTR has not set any minimum or maximum time limit for reporting a 
transaction or a trade event to it after the transaction or event is agreed by the 
transacting parties.

## Page 33

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 27 
TR Members, however, should observe the schedule, rules and requirements in the 
OTC regulatory regime, if any, on the time for reporting a transaction or a trade event 
to the HKTR for meeting the relevant mandatory reporting requirements. 
8.6 HKTR System Window for Capturing Trade Information 
The HKTR system is open 7 days a week and 24 hours a day for capturing 
information of OTC derivatives trades submitted by TR Members except during 
certain outage windows for system maintenance and software migration. The outage 
windows for submitting trade events to the HKTR through different channels are set 
out in the table below. 
Channel Monday to Saturday 
(Hong Kong time) 
Sunday 
(Hong Kong time) 
UI upload via SWIFTNet 
FileAct via SWIFTNet 
0:30 - 4:00 23:00 (Sat)– 12:00 
(and additional outage 
period published by 
SWIFT from time to 
time, if any) 
FTS via ICLNet 0:30 – 4:00 23:00 (Sat) – 5:00 
UI upload via Internet 0:30 – 4:00 23:00 (Sat) – 5:00 
During the Monday-to-Saturday outage windows, while TR Members will not be able 
to upload trade event request files through the user interface (“UI”) functions via the 
internet or SWIFTNet, they can continue to submit files through FileAct via 
SWIFTNet or File Transfer Service (“FTS”) via ICLNet as the files will be queued in 
the system and will be automatically captured for processing after the system resumes 
operation. 
During the Sunday outage window, the user interface (“UI”) functions via the internet 
or SWIFTNet, File Transfer Service (“FTS”) via ICLNet and FileAct via SWIFTNet 
are not available. Members will not be able to upload trade event request files during 
the period.

## Page 34

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 28 
9. TRADE VALIDATION AND LINKING 
9.1 Transaction or Trade Event Validation 
Upon receiving a trade event request file from a TR Member, the HKTR system will 
validate the format, contents and syntax of the file as well as that of the individual 
trade event records contained in the file. If an error is detected, the whole file or 
individual trade event records will be rejected, depending on whether the error occurs 
at file level or trade event record level. A response will be provided to the TR 
Members submitting the trade event request file about whether the file or individual 
trade event records have been accepted or rejected. 
 
Trade event records successfully validated will then go through the linking process. 
9.2 Transaction Linking 
To help ensure the quality of the data of OTC derivatives transactions at the HKTR, 
and to facilitate TR Members to identify and resolve potential reporting errors, the 
HKTR system will identify, compare and link up updated records of transaction 
conducted between TR Members (recognised by the HKTR system based on the 
identification numbers supplied by TR Members under the TR Member Profile 
Maintenance Form at Appendix TR.3). Updated records of transaction conducted 
between a TR Member and a non-TR Member will not be linked and will be classified 
as single-sided transactions in the HKTR system. 
The linking process will be conducted by batch mode and performed once everyday. 
For trade events of a transaction reported to have been agreed between a TR Member 
and a counterparty TR Member on a trade day, the HKTR system will aggregate the 
effect of the trade events and compute a resultant position of the transaction for the 
trade day. The HKTR system will then search for and link it up with updated position 
of the transaction of the counterparty TR Member bearing matching information (but 
in opposite direction) in a set of core transaction details (primary reporting terms) of

## Page 35

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 29 
the transaction. TR Members can check from the HKTR system those transaction 
records that have been linked. 
Where a TR Member finds that its transaction has been mistakenly linked to another 
transaction of the counterparty TR Member, e.g. the transaction should be linked to 
another transaction bearing same primary reporting terms but is different in other 
aspects, and considers it necessary to correct the link, e.g. for bringing consistency 
with internal records, the TR Member may initiate a request to relink the transaction. 
Where the primary reporting terms of an updated transaction of the TR Member 
cannot be matched with that of the counterparty TR Member, e.g. the counterparty TR 
Member has not yet reported all the trade events to the HKTR or a reporting error has 
been made by one of the transacting TR Members, the updated transaction of the TR 
Member will be deemed to be unlinked. TR Members can check from the HKTR 
system the unlinked transactions to facilitate them to identify and resolve potential 
discrepancies. 
The reports on unlinked or unmatched transactions produced by the TR system are 
optional tools to facilitate TR Members to identify and resolve potential missing or 
unmatched transactions. It is not a mandatory requirement for TR Members to make 
use of such reports to identify and resolve reporting errors, nor are TR Members 
required to resolve the transactions identified in such reports within any specified 
timeframe. TR Members, however, must have in place effective controls to ensure 
that their transactions are reported timely and accurately, and any errors in reporting 
can be promptly identified and resolved.

## Page 36

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 30 
10 REPORTING SERVICE REPORTS 
10.1 Types of Report 
There are three types of report: 
(a) System reports –generated automatically by the system. Reports are generated 
in off-line batch mode at pre-defined time or after a specific event, and can be 
delivered via file transfer or viewed/downloaded via UI function 
(b) Enquiry-Initiated User Requested reports – Reports are generated in 
background mode. Users can check report generation status, view or 
download the generated report via the View Report List function 
(c) UI Enquiry reports – Reports are tied to the enquiry functions, showing the 
same result set as the enquiry. Reports are generated in on-line real-time 
mode and then sent to the browser front-end for the user’s viewing 
Please refer to the various User Manuals for Participants of the Operating Procedures 
for Trade Repository for the summary of report list, report samples, and the schedule 
and procedures for retrieving the relevant reports through different channels and in 
different formats. 
10.2 Reconciliation of Reports 
TR Members should download all the reports under the Reporting Service and 
reconcile their reports on a daily basis. Any discrepancies should be reported to the 
HKMA as soon as practicable and in any event, not later than 7 business days from 
the date of the relevant report. If any report is reported to be incorrect, the HKMA 
will make the relevant investigation and if applicable, re-issue the report revised as 
necessary.

## Page 37

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 31 
11. CONTINGENCY ARRANGEMENTS 
11.1 Local Terminal Service 
In case a TR Member cannot access the HKTR system through its own production 
facilities due to prolonged system connectivity problems with SWIFTNet, the TR 
Member may make use of the Local Terminal Service (“LTS”) provided by the 
HKICL to access the Reporting Service. The TR Member can generate the relevant 
trade event request files from its own system, and then upload the files to the HKTR 
system directly at the terminals located at the office of the HKICL. 
LTS should be used as the last resort for accessing the Reporting Service. TR 
Members should rely on their own backup facilities for contingency operations. In 
case a TR Member needs to utilise LTS under contingency situation, the TR Member 
has to apply to the HKICL directly in accordance with the arrangements promulgated 
by the HKICL. 
11.2 Typhoon and Rainstorm Procedures 
 The Reporting Service of the HKTR will remain accessible under rainstorm and 
typhoon scenarios. TR Members can continue to send trade events to the HKTR 
system for reporting purposes. TR Members, however, should observe the schedule, 
rules and requirements in the OTC regulatory regime, if any, on the time for reporting 
a trade event to the HKTR for meeting the relevant statutory reporting requirements 
under a typhoon or rainstorm scenario.

## Page 38

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 32 
12. BILLING
In entering into an agreement for subscribing to any service of the HKTR, TR 
Members will undertake to pay a membership fee if applicable. 
TR Members using the Reporting Service will also be subject to transaction charges 
based on the usage of the HKTR system. 
The TR Membership fee and the transaction charges for the Reporting Service are set 
out in the fee scale in Annex 2. The updated scale is available in the HKTR section 
of the HKMA website. Changes to the scale will be advised to TR Members through 
circulars. 
12.1 Settlement Arrangements 
For TR Members which are also CMU Members (participants of CMU service offered 
by the CMU in respect of safe custody, recording and transfer of debt securities) and 
are direct participants in the Hong Kong dollar Real Time Gross Settlement (“RTGS”) 
system (“Direct Participant TR Members”), their fees are settled through their own 
settlement accounts maintained with the HKMA. Other TR Members are required to 
appoint a settlement bank (“Appointed Settlement Bank”) which is a CMU member 
and a direct participant in the Hong Kong dollar RTGS system for the settlement of 
their fees. 
TR Members are required to designate their settlement accounts and authorise the 
CMU to debit the fees from the designated accounts by using the Designation of Hong 
Kong Dollar Account for Settling Fees and Charges form (“Account Designation 
Form”) at Appendix TR.6. 
To enable direct debiting of fees by the CMU from the designated settlement accounts, 
Direct Participant TR Members and Appointed Settlement Banks shall authorise and 
instruct the CMU to set up direct debit limits in the CMU system. The CMU system

## Page 39

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 33 
makes reference to the last four digits of the TR Member Code (“HKTR Billing 
Code”) in referring to a TR Member in the system. Direct Participant TR Members 
should advise the CMU the direct debit limits to be set in the Account Designation 
Form at Appendix TR.6. Appointed Settlement Banks should advise the CMU the 
direct debit limits to be set for their clients in the Direct Debit Limit of Settlement 
Bank form at Appendix TR.7. 
12.2 Billing Arrangements 
All fees are invoiced in Hong Kong dollar and billed monthly to TR Members. The 
arrangements are as follows: 
(a) The total amount of fees payable will be advised to Members on the 10th day 
of the following month or next business day if the 10th is not a business day to 
the contacts for the Reporting Service specified by Members in the TR 
Member Profile Maintenance Form in Appendix TR.3. 
(b) On the business day following the billing day, Members shall ensure that 
sufficient funds are arranged in their respective settlement accounts. 
(c) The total fees will be automatically debited from the settlement account 
designated by Members (as at Appendix TR.6) on the 15th or the following 
business day if 15th is not a business day. 
(d) Upon completion of the billing process, the RTGS system will format the 
settlement advices in MT900 format and distribute to the TR Members or its 
Appointed Settlement Banks via SWIFT. The advice will bear the HKTR 
Billing Code of the TR Member concerned for reference.

## Page 40

Hong Kong Monetary Authority 
OTC Derivatives Trade Repository Reporting Service Reference Manual 
Dec 2013 v1.3 Page 34 
(This page is intentionally left blank)

## Page 41

TR Membership Application Form
To : Hong Kong Monetary Authority Date:
Facsimile: (852) 2878 1679 
 
From : 
Name of Institution 
We request for your approval for ___________________________________ (Name of the Applicant) 
to be admitted as a Member of the OTC Derivatives Trade Repository operated by the Hong Kong 
Monetary Authority (TR Member). We understand that the continuation of a TR Membership is 
subject to the TR Member’s compliance with the applicable service agreement with the Monetary 
Authority, and rules and operating procedures from time to time prescribed by the Monetary 
Authority. The Monetary Authority may suspend or terminate the membership of a TR Member in 
the event of a breach of any of the agreement, rules and operating procedures.
Applicant Institution : 
(Legal Full Name) 
Address : 
Telephone : 
Facsimile : 
Name(s) of person(s) to contact in 
respect of this application : 
e-mail address : 
_________________________ 
Authorized Signature(s) 
Company Chop 
Appendix TR.1
Hong Kong Monetary Authority 
OTC Derivatives Trade Repository 
The signed original of the completed form must be submitted to the HKMA

## Page 42

(This page is intentionally left blank)

## Page 43

TR Member Record of Authorized Signatures
To : Trade Repository, Hong Kong Monetary Authority Date: __________________ 
Address: 55/F, Two International Finance Centre, 8 Finance Street, 
 Central, Hong Kong 
Facsimile: (852) 2878 1679 
Name of TR Member :__________________________________________________________________ 
TR Member Code :________________________ Telephone Number : ________________________ 
Address :__________________________________________________________________ 
The persons in the table below are authorized to sign for and on behalf of us under (please tick as appropriate): 
 Reporting Service 
 Matching and Confirmation Service 
AUTHORIZED SIGNATURE AND/OR STAMP
NAME AND TITLE (IN BLOCK LETTERS) 
AUTHORIZED SIGNATURE AND/OR STAMP
NAME AND TITLE (IN BLOCK LETTERS) 
AUTHORIZED SIGNATURE AND/OR STAMP
NAME AND TITLE (IN BLOCK LETTERS) 
AUTHORIZED SIGNATURE AND/OR STAMP
NAME AND TITLE (IN BLOCK LETTERS) 
AUTHORIZED SIGNATURE AND/OR STAMP
NAME AND TITLE (IN BLOCK LETTERS) 
AUTHORIZED SIGNATURE AND/OR STAMP
NAME AND TITLE (IN BLOCK LETTERS) 
SIGNING INSTRUCTIONS : 
(Please add a new page if there are more authorized signatures to specify) 
____________________________ 
Authorized Signature(s) 
Company Chop
Hong Kong Monetary Authority 
OTC Derivatives Trade Repository 
Appendix TR.2
The signed original of the completed form must be submitted to the HKMA

## Page 44

(This page is intentionally left blank)

## Page 45

TR Member Profile Maintenance Form
To : Hong Kong Monetary Authority Date:
Facsimile: (852) 2878 1679 
 
From : ( ) 
Name of TR Member TR Member Code 
We refer to the appointment of our institution as a TR Member, the following are the 
information of our institution: 
Type of Institution (please tick as appropriate) 
 Institution authorized or approved under the Banking Ordinance 
 Full Licensed bank Restricted Licence Bank 
 Deposit Taking Company Approved Money Broker 
 Licensed Corporation under the Securities and Futures Ordinance 
 Others 
Place of Incorporation (please tick as appropriate) 
 Hong Kong Outside Hong Kong, please specify______________________ 
Identification number (please provide all those numbers that your institution possesses) 
Global Legal Entity Identifier or pre-LEI1
Issued by: 
________________________________________ 
SWIFT BIC (Business Identifier Code issued by 
SWIFT under ISO9362)2
Number of the Certificate of Incorporation (CI) or 
Certificate of Registration (CR) issued by the 
Companies Registry of Hong Kong3
Hong Kong Monetary Authority 
OTC Derivatives Trade Repository 
Appendix TR.3
The signed original of the completed form must be submitted to the HKMA

## Page 46

Business Registration Number (BRN) issued by the 
Inland Revenue Department of Hong Kong3
Clearing Member Code at the OTC derivatives 
CCP of the HKEx 
Notes
(1) Global Legal Entity Identifier (“Global LEI”) refers to the unique identifier for legal entity issued 
under the Global LEI System established by the Regulatory Oversight Committee (ROC) of the 
Global LEI System. If the Global LEI is not yet available, please provide pre-LEI identification 
code (“pre-LEI”) issued by a pre-Local Operating Unit that has been endorsed by the ROC for 
issuing identification codes to meet reporting and other regulatory purposes, if any. 
(2) Please provide the eight character SWIFT BIC referring to the Hong Kong office/branch of your 
institution, if any. 
(3) Please provide certified true copy of the certificate 
Contact information for Reporting Service 
 
 
Contact information for Matching and Confirmation Service 
Contact Person : 
Telephone number : 
Facsimile number : 
Address : 
 
 
Group/individual e-mail : 
 
____________________________ 
Authorized Signature(s) 
Company Chop 
Contact Person : 
Telephone number : 
Facsimile number : 
Address : 
 
 
Group/individual e-mail :

## Page 47

TR Member Administrative Account Setup Form
To : Hong Kong Monetary Authority Date:
Facsimile: (852) 2878 1679 
 
From : ( ) 
Name of TR Member TR Member Code 
We refer to the appointment of our institution as a TR Member, please set up administrative 
account(s) for our institution to access the User Interface (“UI”) of the TR system (please tick 
one or both as appropriate): 
 through Internet [Please provide SSL Client Certificate DN if this is chosen] 
 through SWIFTNet [Please provide SWIFT User DN if this is chosen] 
SSL Certificate DN: 
__________________________________________________
__________________________________________________
__________________________________________________ 
SWIFTNet User DN: 
__________________________________________________
__________________________________________________
__________________________________________________ 
____________________________ 
Authorized Signature(s) 
Company Chop
Hong Kong Monetary Authority 
OTC Derivatives Trade Repository 
Appendix TR.4
(Please also send a copy-and–paste-able copy of 
DN to the HKTR for accurate account setup 
purpose through email with a subject of “Admin 
Account Setup – TR Member Code” ) 
The signed original of the completed form must be submitted to the HKMA

## Page 48

(This page is intentionally left blank)

## Page 49

Broker List of TR Member
To : Hong Kong Monetary Authority Date:
Facsimile: (852) 2878 1679 
 
From : ( ) 
Name of TR Member TR Member Code 
The transactions of our institution may be brokered by the following broker(s): 
Broker Name Broker address
 
 
 
 
 
Broker Name Broker address
 
 
 
 
 
Broker Name Broker address
 
 
 
 
 
Broker Name Broker address
 
 
 
 
(Please add a new page if there are more brokers to specify) 
____________________________ 
Authorized Signature(s) 
Company Chop
Hong Kong Monetary Authority 
OTC Derivatives Trade Repository 
Appendix TR.5
The signed original of the completed form must be submitted to the HKMA

## Page 50

(This page is intentionally left blank)

## Page 51

Designation of Hong Kong Dollar Account for Settling Fees and Charges
To : Hong Kong Monetary Authority Date:
Facsimile: (852) 2878 1679 
 
From : ( ) 
Name of TR Member TR Member Code* 
We agree to settle the fees and charges arising from service provided by the HKTR to our 
institution by direct debit from our Hong Kong dollar settlement account specified below, on 
instructions from the Monetary Authority. 
(Please tick the appropriate box below and supply the corresponding settlement account 
information) 
 My institution is a CMU Member and a direct participant of the Hong Kong dollar 
RTGS System, please direct debit from the following settlement account of my 
institution: 
 Account Number: ____________________ 
Please set up a direct debit limit of ___________________________ in the CMU 
system for debiting the fees and charges from the above Account. 
 My institution is not a CMU Member or a direct participant of the Hong Kong dollar 
RTGS System 
Name of Settlement Bank: _______________________________ 
Our Account Number with the Settlement Bank: ___________________________ 
Contact Person and Phone Number: _______________________________ 
Hong Kong Monetary Authority 
OTC Derivatives Trade Repository 
Appendix TR.6
The signed original of the completed form must be submitted to the HKMA

## Page 52

We have given standing authorisation to the above bank to accept such instructions 
from the Monetary Authority. We have also agreed with the above settlement bank 
on the direct debit limit for our maximum settlement amount for fees and charges 
arising from the service provided by the HKTR. A direct debit limit form for our 
institution will be forwarded to you directly from our settlement bank. 
____________________________ 
Authorized Signature(s) 
Company Chop 
(*The CMU system makes reference to the last 4 digits in the TR Member Code of a TR Member in 
referring to the TR Member in the system. The 4 digits will be applied in setting up the direct debit
limit in the CMU system.)

## Page 53

Direct Debit Limit of Settlement Bank
To : Hong Kong Monetary Authority Date:
Facsimile: (852) 2878 1679 
 
From : ( ) 
Name of Settlement Bank CMU Member Code 
We have agreed with our client, ______________________________, (TR Member Code*) 
on the direct debit limit for its maximum settlement amount for the fees arising from the 
service offered by the HKTR. We have also received standing authorisation from our client 
to accept settlement instructions from the CMU. 
The settlement details of our client are as follows: 
Account Name : _________________________________________________ 
Settlement Account 
Number in our book : _________________________________________________ 
Please set up a direct debit limit of ___________________________ in the CMU system for 
debiting the fees and charges arising from the service offered by the HKTR to our client from 
the above Account. 
____________________________ 
Authorized Signature(s) 
Company Chop 
(*The CMU system makes reference to the last 4 digits in the TR Member Code of a TR Member in 
referring to the TR Member in the system. The 4 digits will be quoted in the settlement advice for 
reference.) 
Hong Kong Monetary Authority 
OTC Derivatives Trade Repository 
Appendix TR.7
The signed original of the completed form must be submitted to the HKMA

## Page 54

(This page is intentionally left blank)

## Page 55

Agent Nomination Form
To : Hong Kong Monetary Authority Date:
Facsimile: (852) 2878 1679 
 
From : ( ) 
Name of TR Member (“Member Principal”) TR Member Code 
We refer to clause 7 of the reporting service agreement between the Monetary Authority and 
our institution dated _________________ ("Reporting Service Agreement"). 
Unless defined in this form or the context otherwise requires, a term defined in the agency 
terms as appended to this form ("Agency Terms") has the same meaning in this form. 
Please be informed that the Member Principal nominates _____________________________ 
(Name of the Nominated Agent) (“Nominated Agent”) to submit trade information of OTC 
derivatives transactions of our institution to the HKTR.
The Member Principal assumes full responsibility in respect of the activities of the 
Nominated Agent in accessing the Reporting System on behalf of the Member Principal, as 
further set out in the Reporting Service Agreement. The Member Principal understands that, 
pursuant to the Reporting Service Agreement and the Agency Terms, the Monetary Authority 
may, in the Monetary Authority's sole and absolute discretion and with immediate effect, 
stop the Nominated Agent from accessing the Reporting System or the Agency Reporting 
Service in the event of a breach of any of the agreement, rules and operating procedures by 
our institution or the Nominated Agent or for any other reason in the Monetary Authority's 
sole and absolute discretion, without incurring any liability whatsoever from either the 
Member Principal or the Nominated Agent (whether under contract, in tort or otherwise). 
Details of Nominated Agent
Nominated Agent: 
(Legal Full Name) 
If Nominated Agent is a TR Member, 
its TR Member code 
Address : 
Hong Kong Monetary Authority 
OTC Derivatives Trade Repository 
Appendix TR.8
-1-
The signed original of the completed form must be submitted to the HKMA

## Page 56

Telephone : 
Facsimile : 
Name(s) of person(s) to contact in 
the Nominated Agent : 
e-mail address : 
Details of Process Agent
If the Nominated Agent is not resident, incorporated or registered in Hong Kong, the details 
of the Nominated Agent's process agent, for the purposes of clause 20 of the Agency Terms, 
are as follows: 
Name: _________________________________________ 
Address: _______________________________________ 
Telephone: _____________________________________ 
Fax: ___________________________________________ 
Date appointed: _________________________________ 
In the event the Monetary Authority approves of the appointment of the Nominated Agent, 
the Monetary Authority shall send to the Nominated Agent a confirmation of the Monetary 
Authority's approval of the nomination of the Nominated Agent and, if relevant, any 
conditions, requirements or procedures in relation to such approval, substantially in the form 
set out in page 3 of this form ("Approval Confirmation"), in any manner described in Clause 
21 (Notices) of the Agency Terms. 
The Nominated Agent agrees to be bound by the terms of the Agency Terms in the event the 
Monetary Authority sends an Approval Confirmation to the Nominated Agent. The Agency 
Terms shall take effect on the Agency Approval Date (as specified in the Approval 
Confirmation). 
_______________________________ ________________________________ 
Authorized Signature(s) of Nominated Agent Authorized Signature(s) of Member Principal 
 Company Chop Company Chop 
-2-

## Page 57

Approval Confirmation 
The Monetary Authority has, subject to the conditions below, approved the nomination of the 
Nominated Agent specified in this Agent Nomination Form on the Agency Approval Date. 
The Nominated Agent is therefore bound by the terms of the Agency Terms as of the Agency 
Approval Date. 
Date of approval (the "Agency Approval Date"): _________________________________ 
Conditions of approval 
The approval by the Monetary Authority above is subject to the following conditions: 
 
 
 
 
 
SIGN BY 
 
On behalf of the Monetary Authority 
In the presence of: 
 
Witness 
-3-

## Page 58

(This page is intentionally left blank)

## Page 59

Appendix to Agent Nomination Form
HONG KONG MONETARY AUTHORITY 
AND 
[NOMINATED AGENT] 
AGENCY TERMS

## Page 60

CONTENTS 
Clause Page
1. Definitions and Interpretation........................................................................................1 
2. Using the Agency Reporting Service.............................................................................7 
3. Charge, Payment and Tax..............................................................................................9 
4. Nominated Agent's Obligations .....................................................................................9 
5. Instructions and Users..................................................................................................10 
6. Agency Conditions.......................................................................................................11 
7. Representations and Warranties...................................................................................12 
8. Liability........................................................................................................................14 
9. Confidentiality .............................................................................................................17 
10. Offices and Branches ...................................................................................................19 
11. Personal Data ...............................................................................................................19 
12. Ownership of Intellectual Property Rights ..................................................................20 
13. Termination..................................................................................................................21 
14. Consequences of Termination......................................................................................21 
15. Force Majeure ..............................................................................................................21 
16. Assignment and Subcontracting ..................................................................................22 
17. Entire Agreement.........................................................................................................22 
18. General.........................................................................................................................23 
19. Governing Law and Jurisdiction..................................................................................23 
20. Service of Process........................................................................................................24 
21. Notices .........................................................................................................................24 
Schedule 1 Notice Details........................................................................................................26

## Page 61

BETWEEN: 
(1) THE MONETARY AUTHORITY, appointed pursuant to section 5A(1) of the 
Exchange Fund Ordinance (Chapter 66 of the Laws of Hong Kong) of 55th Floor, Two 
International Finance Centre, 8 Finance Street, Central, Hong Kong ("HKMA"); and 
(2) the person identified as the "Nominated Agent" in the Agent Nomination Form (as 
defined below) ("Nominated Agent"). 
WHEREAS: 
(A) The Nominated Agent has been nominated by the Member Principal (as defined 
below) to submit Transaction Records (as defined below) on its behalf under an 
Agency Arrangement (as defined below), and HKMA has agreed to such Agency 
Arrangement and will provide the Agency Reporting Service to the Nominated Agent 
to enable the Nominated Agent to carry out its obligations under such Agency 
Arrangement. 
(B) These Agency Terms set out the terms and conditions on which HKMA has agreed to 
provide the Agency Reporting Service to the Nominated Agent. 
THE PARTIES AGREE as follows: 
1. DEFINITIONS AND INTERPRETATION 
1.1 In these Agency Terms: 
"Affected Party" has the meaning given to it in Clause 15.1 (Force Majeure)); 
"Agency Approval Date" means the date specified as the "Agency Approval Date" in 
the Agent Nomination Form; 
"Agency Arrangement" means the arrangement between the Nominated Agent and 
the Member Principal whereby the Nominated Agent is appointed by the Member 
Principal to submit Transaction Records under the Agency Reporting Service on 
behalf of and as agent of the Member Principal;
"Agency Reporting Service" means the service to be provided by HKMA to the 
Nominated Agent to enable the Nominated Agent to, among other things: 
(a) submit Transaction Records to HKMA on behalf of the Member Principal for 
the purposes of fulfilling the Member Principal's obligations under the 
Reporting Requirements (which will be validated and (where relevant) linked 
by HKMA for the purposes of verifying the accuracy of such Transaction 
Records); 
(b) where a Transaction Record has been submitted under the Agency Reporting 
Service and the Transaction specified in such Transaction Record has been 
amended or terminated, submit an updated Transaction Record reflecting the 
relevant amendment(s) or termination; and 
(c) request reports and receive notifications of, among other things, Transaction 
1

## Page 62

2 
Records, 
through the Reporting System, in accordance with, and as further described in, these 
Agency Terms; 
"Agency Terms" mean the agreement between HKMA and the Nominated Agent, as 
constituted by, and set out in, the Agent Nomination Form, the Approval 
Confirmation, these Substantive Provisions and any Annexes, as amended, restated, 
revised, updated or supplemented from time to time;
"Agent Nomination Form" means the agent nomination form in the form 
substantially set out in Appendix TR.8 of the Reference Manual: (a) a copy of which 
has been duly executed by the Nominated Agent and the Member Principal; and (b) to 
which these Agency Terms are appended; 
"Annex" means each of the following, as amended, restated, revised, updated or 
supplemented from time to time (whether in accordance with Clause 18 (General) or 
otherwise): 
(a) Reference Manual; 
(b) Hong Kong Trade Repository Administration and Interface Development 
Guide (Reporting Service) ; and 
(c) any other material or document (whether in electronic or physical form), 
including any operational procedure, guide, instruction or manual, which is, by 
prior written notice to the Nominated Agent, designated by HKMA to be an 
Annex; 
"Approval Confirmation" means the confirmation of the approval of the Nominated 
Agent (including, if relevant, any conditions, requirements or procedures in relation to 
such approval) specified as the "Approval Confirmation" in the Agent Nomination 
Form; 
"Authority" means any governmental, regulatory, administrative or law 
enforcement body and/or court or tribunal of competent jurisdiction; 
"Business Day" means a day other than a Saturday, a Sunday or a day which is a 
general holiday as specified in the General Holidays Ordinance (Chapter 149 of the 
Laws of Hong Kong); 
"Charge" means the one-off charge of HK$10 which is payable by the Nominated 
Agent to HKMA on the Agency Approval Date; 
"Clause" has the meaning given to it in Clause 1.2.12 (Definitions and Interpretation); 
"Confidential Information" has the meaning given to it in Clause 9.1 
(Confidentiality); 
"Data Subject" has the meaning given to the expression "data subject" in the Personal 
Data (Privacy) Ordinance (Chapter 486 of the Laws of Hong Kong);

## Page 63

3 
"Direction" has the meaning given to it in Clause 2.2.2 (Using the Agency Reporting 
Service); 
"Disclosing Party" has the meaning given to it in Clause 9.1 (Confidentiality); 
"Dispute" has the meaning given to it in Clause 19.2 (Governing Law and 
Jurisdiction); 
"Force Majeure Event" means an event beyond the reasonable control of the 
Affected Party and unknown to the Affected Party at the date of these Agency Terms 
including, without limitation, strike, lock-out, labour dispute, (but excluding strikes, 
lockouts and labour disputes involving employees of the Affected Party or its 
subcontractors), act of God, war, riot, civil commotion, malicious damage (but 
excluding malicious damage involving the employees of the Affected Party or its 
subcontractors), compliance with any Law, accident, breakdown of plant or 
machinery, fire, flood and storm; 
"Hong Kong" means the Hong Kong Special Administrative Region of the People's 
Republic of China; 
"Intellectual Property Rights" means: 
(a) patents, trademarks, service marks, registered designs, applications and rights 
to apply for any of those rights, trade, business and company names, internet 
domain names and email addresses, unregistered trademarks and service 
marks, copyrights, database rights, rights in software, algorithms, source code, 
object code, know-how, rights in designs and inventions and other intellectual 
or industrial property rights; 
(b) rights under licences, consents, orders, statutes or otherwise in relation to a 
right in sub-Clause (a) above; 
(c) rights of the same or similar effect or nature as or to those in sub-Clauses (a) 
and (b) which now or in the future may subsist in any jurisdiction; and 
(d) the right to sue for any infringement of any of the foregoing rights; 
"ISDA" means the International Swaps and Derivatives Association, Inc.; 
"ISDA Master Agreement" means the standard form ISDA 2002 Master Agreement 
or the standard form 1992 ISDA Master Agreement (Multicurrency – Cross Border), 
as applicable, as published by ISDA; 
"Law" means any and all: 
(a) treaties, acts, ordinances, regulations, by laws, orders, awards, proclamations, 
directions and practice notes (whether civil, criminal or administrative) of any 
country, state, territory or Authority concerning any matters, including but not 
limited to, capital adequacy, prudential limits, liquidity, reserve assets or Tax; 
(b) authorisations, certifications, licences, consents, permits, approvals and 
requirements of organisations having jurisdiction in connection with the

## Page 64

4 
carrying out of these Agency Terms; 
(c) laws governing any contract or any other relationship; 
(d) other laws from which legal rights or obligations may arise (including without 
limitation, by way of decisions or judgments of any Authority); and 
(e) official directives, requests, guidelines, or policies (whether or not having the 
force of law) with which responsible banks generally comply in carrying on 
their business; 
"Maintenance Period" means any period of time that HKMA determines, in
HKMA's sole and absolute discretion, as a period during which HKMA's hardware or 
software systems relating to the Agency Reporting Service are non-operational, 
restricted or hampered in any manner which will, or potentially will, affect any aspect 
of HKMA's provision of the Agency Reporting Service, due to any maintenance, 
upgrade, modification or repair of such systems (whether scheduled or otherwise) or 
other similar event; 
"Member Group" means all persons whom HKMA has for the time being agreed are 
to be provided with the "Reporting Service" (each as a "Member" under the terms of a 
separate reporting service agreement, in each case between such person and HKMA 
and as such terms are defined in such reporting service agreement); 
"Member Principal" means the person identified as the "TR Member" in the Agent 
Nomination Form; 
"Nominated Agent Group" means all persons whom HKMA has for the time being 
agreed are to be provided with the "Agency Reporting Service" (each as a 
"Nominated Agent" under the terms of a separate set of agency terms, in each case 
between such person and HKMA and as such terms are defined in such agency terms), 
together with the Nominated Agent; 
"Nominated Agent User" means any individual which the Nominated Agent has 
nominated under the Reporting System as being authorised by the Nominated Agent 
to access and use the Reporting System on behalf of the Member Principal under the 
terms of, and in accordance with, these Agency Terms; 
"Officer" means an officer, employee, agent, nominee, custodian or professional 
adviser (including auditor, accountant and legal adviser) or any other person acting in 
any (duly authorised) representative capacity; 
"Party" means each of HKMA and the Nominated Agent, and "Parties" means both 
of them; 
"Personal Code" means each private and unique reference code created (or to be 
created) by: 
(a) the Member Principal; or 
(b) where authorised by the Member Principal, the Nominated Agent on behalf of 
the Member Principal,

## Page 65

5 
to reference a counterparty to a Transaction who is an individual, in accordance with 
paragraph 8.4 of the Reference Manual; 
"Personal Data" means any data or information in any form: 
(a) constituting "personal data" as defined in the Personal Data (Privacy) 
Ordinance (Chapter 486 of the Laws of Hong Kong); and/or 
(b) which may allow or assist (or potentially allow or assist) HKMA to ascertain 
the identity of any counterparty to a Transaction who is an individual 
(including without limitation, any data or information which in any way links 
or connects the Personal Code of an individual to any other data or 
information which allows or assists HKMA to ascertain the identity of such 
individual); 
"Receiving Party" has the meaning given to it in Clause 9.1 (Confidentiality); 
"Reference Manual" means the OTC Derivatives Trade Repository – Reporting 
Service Reference Manual, as revised by HKMA from time to time; 
"Reporting Requirements" means at any time: 
(a) the Securities and Futures Ordinance (Chapter 571 of the Laws of Hong Kong) 
and any subsidiary legislation made under the Securities and Futures 
Ordinance (Chapter 571 of the Laws of Hong Kong) in effect (or, as the case 
may be, expected to come into effect); and/or 
(b) any other Law, 
in each case which obliges certain persons to report certain over-the-counter 
derivatives transactions to HKMA; 
"Reporting System" means the internet-based system which allows the Nominated 
Agent to access and use the Agency Reporting Service; 
"Schedule" has the meaning given to it in Clause 1.2.12 (Definitions and 
Interpretation); 
"Substantive Provisions" means the terms and conditions of these Agency Terms 
(including any Schedules to these Agency Terms), but excluding any Annexes, as 
amended, restated, revised, updated or supplemented from time to time (whether in 
accordance with Clause 18 (General) or otherwise); 
"Taxes" of an entity means taxes (including profit, capital gain, goods and services 
and value added or indirect taxes), levies, imposts, charges and duties (including 
stamp and transaction duties) imposed by any Authority together with any related 
interest, penalties, fines and expenses in connection with them, except if imposed on, 
or calculated having regard to, such entity's overall net income; 
"Transaction" means any transaction specified in a Transaction Record; and 
"Transaction Record" means the record specifying the details (in the format

## Page 66

6 
specified under the relevant Annexes, or otherwise as specified in writing by HKMA) 
of any over-the-counter derivative transaction submitted by the Nominated Agent to 
HKMA in accordance with these Agency Terms, regardless of the status of such 
Transaction Record as indicated in the Reporting System. 
1.2 In these Agency Terms, a reference to: 
1.2.1 Clause and Schedule headings are for ease of reference only; 
1.2.2 a statutory provision includes a reference to the statutory provision as modified 
or re-enacted or both from time to time and any subordinate legislation made 
or other thing done under the statutory provision from time to time; 
1.2.3 a document is a reference to that document as modified or replaced from time 
to time; 
1.2.4 any words following the terms "including", "include", "in particular" or any 
similar expression shall be construed as illustrative and shall not limit the 
sense of the words, description, definition, phrase or term preceding those 
terms; 
1.2.5 "such as" or "for example" when introducing an example, does not limit the 
meaning of the words to which the example relates to that example or 
examples of a similar kind; 
1.2.6 a person includes a reference to any individual, company, corporation, 
unincorporated association or body (including a partnership, trust, fund, joint 
venture or consortium), government, state, agency, organisation or other entity 
whether or not having a separate legal entity; 
1.2.7 a person includes a reference to that person's legal personal representatives, 
successors and permitted assigns; 
1.2.8 the singular includes the plural and vice versa (unless the context otherwise 
requires); 
1.2.9 the masculine gender shall include the feminine and neuter and vice versa 
(unless the context otherwise requires); 
1.2.10 a time of day is a reference to the time in Hong Kong, unless expressly 
provided to the contrary; 
1.2.11 if any provision (or any part of a provision) of these Agency Terms may be or 
becomes invalid, illegal or unenforceable in any respect, that shall not affect or 
prejudice the validity, legality and enforceability of the remaining provisions 
(or the remaining parts of the relevant provision, as the case may be); and 
1.2.12 a "Clause" or "Schedule", unless the context otherwise requires, is a reference 
to a clause of or schedule to these Agency Terms. 
1.3 These Agency Terms are constituted by the Agent Nomination Form, the Approval 
Confirmation, these Substantive Provisions and any Annexes, as amended, restated,

## Page 67

7 
revised, updated or supplemented from time to time, and together they form a single 
agreement between HKMA and the Nominated Agent. 
1.4 Except where expressly stated otherwise, time shall not be of the essence for the 
supply of the Agency Reporting Service by HKMA to the Nominated Agent. 
1.5 The Nominated Agent, in consideration for HKMA permitting the Nominated Agent 
and each relevant Nominated Agent User to access and use the Reporting System in 
accordance with these Agency Terms, agrees to be bound by, and to accept the terms 
set out in, these Agency Terms. 
2. USING THE AGENCY REPORTING SERVICE 
2.1 The Nominated Agent understands, acknowledges and agrees that: 
2.1.1 the Reporting System is provided to the Nominated Agent on an "as-is" basis; 
2.1.2 HKMA shall retain exclusive control over the Reporting System; 
2.1.3 the Nominated Agent shall be responsible for obtaining and using any software, 
hardware and any other equipment necessary or desirable for it to access and 
use the Reporting System; 
2.1.4 the Member Principal shall be solely responsible for complying with the 
Member Principal's obligations under the Reporting Requirements and all or 
any other applicable Laws with respect to the reporting of transactions, record￾keeping and the maintenance of records; and 
2.1.5 the Nominated Agent shall be solely responsible for complying with, and 
HKMA makes no representation that, the Agency Reporting Service will 
satisfy, or is capable of satisfying, the Nominated Agent's obligations under 
any agreement between the Nominated Agent and the Member Principal and 
all or any other applicable Laws. 
2.2 Notwithstanding any other Clause of these Agency Terms, HKMA may, in HKMA's 
sole and absolute discretion, without incurring any liability to the Nominated Agent 
whatsoever: 
2.2.1 vary, suspend or terminate the Agency Reporting Service by giving prior 
written notice to the Nominated Agent; or 
2.2.2 refuse to act or refrain from acting on any instruction or information (including 
any instruction or information in connection with any Transaction Record or 
disclosure of Confidential Information) submitted by the Nominated Agent 
(including any Nominated Agent User) (each instruction or information, a 
"Direction"), 
in each case, including without limitation, where HKMA, in HKMA's sole and 
absolute discretion, determines or believes that: 
(a) any condition or procedure to be fulfilled or performed by the 
Nominated Agent as set out in the Approval Confirmation has not been fulfilled

## Page 68

8 
or performed; 
(b) a Direction is not given or received in the manner specified by 
HKMA; 
(c) HKMA otherwise would or would likely be in breach of, or non￾compliance with, any applicable Law; 
(d) it would not be reasonable or practicable to act on a Direction or 
provide the Agency Reporting Service; 
(e) a Direction or a set of Directions constitute(s) an abuse or misuse of 
the Agency Reporting Service, including without limitation, where HKMA, in 
HKMA's sole and absolute discretion, considers that such Direction or set of 
Directions is or are given by the Nominated Agent for any reason(s) other than to 
fulfil the Member Principal's obligations under the Reporting Requirements; 
(f) a Direction or the provision of the Agency Reporting Service 
requires any action by, or information from, HKMA: 
(i) otherwise than on a Business Day; 
(ii) during a Maintenance Period; 
(iii) at a time when a Black Rainstorm Warning is issued or may be issued or a 
typhoon signal No. 8 or greater is hoisted or may be hoisted; 
(iv) at a time when the Reporting System is, according to the Reference Manual, 
not scheduled to be in operation; 
(v) at a time when a Force Majeure Event exists or has occurred in respect of 
which HKMA is the Affected Party; or 
(vi) when any other event or circumstance exists or occurs and/or may exist or 
occur which HKMA determines may have a similar effect to one or more of 
the events or circumstances set out in paragraphs (i) to (v) above; 
(g) a Direction or the provision of the Agency Reporting Service would 
cause a breach of these Agency Terms and/or any other agreement between 
HKMA and the Nominated Agent or between HKMA and the Member Principal; 
(h) a Direction or the provision of the Agency Reporting Service is not 
in accordance with HKMA's usual business practices and procedures or any of 
HKMA's internal policies; 
(i) such variation, suspension, termination or refusal is necessary for 
HKMA to continue to provide (i) the Reporting Service to any member of the 
Member Group, or (ii) the "Agency Reporting Service" (as defined in the relevant 
agency terms) to any person within the Nominated Agent Group; and/or 
(j) a Direction (or purported Direction) has not been properly 
authorised by the Nominated Agent or a Nominated Agent User.

## Page 69

9 
3. CHARGE, PAYMENT AND TAX 
The Nominated Agent shall pay HKMA the Charge, without any deduction or 
withholding for or on account of any Tax, in the manner specified by HKMA. 
4. NOMINATED AGENT'S OBLIGATIONS 
4.1 The Nominated Agent agrees and undertakes to HKMA that it shall at all times: 
4.1.1 comply with all applicable Laws and these Agency Terms; 
4.1.2 not do anything or omit to do anything that would cause the Member Principal 
to breach the terms of the reporting service agreement between HKMA and the 
Member Principal; 
4.1.3 notify HKMA promptly in writing of any: 
(a) changes to information previously provided to HKMA, including any 
change to its name and, if applicable, its shareholders, directors or any 
material provision of its constitutive documents; 
(b) error, dispute, breach of any privacy, confidentiality or secrecy 
obligation or suspicion of fraud or illegality in connection with the 
Agency Reporting Service; and 
(c) variation, suspension or termination of the Agency Arrangement. 
For the avoidance of doubt, this Clause 4.1.3 is in addition, and without 
prejudice, to any other notification obligations of the Nominated Agent as set 
out in the Reference Manual; 
4.1.4 ensure that each Nominated Agent User is adequately experienced, trained, 
qualified and skilled for the purpose of accessing and using the Reporting 
System; 
4.1.5 ensure that access to the Reporting System will be limited to one or more 
Nominated Agent Users, each of whom shall use the Reporting System within 
the scope of his/her employment and solely for the Nominated Agent's 
business purposes; 
4.1.6 put in place and maintain effective security measures to safeguard the Agency 
Reporting Service (including the Reporting System) from: 
(a) any access or use by an unauthorised person; and 
(b) any computer virus, worm, Trojan horse, malware or other harmful 
computer code; 
4.1.7 perform all acts (including without limitation, maintaining its systems and 
participating in any drill exercises or tests in accordance with any contingency 
arrangements) as required by and in accordance with these Agency Terms 
(including any Annex);

## Page 70

10 
4.1.8 at HKMA's request, do all things and execute all instruments and documents 
and provide HKMA with all materials, evidence and information as HKMA 
may in HKMA's sole and absolute discretion consider necessary or desirable 
for giving full effect to these Agency Terms or for securing to HKMA the full 
benefit of all rights, powers and remedies conferred on HKMA under these 
Agency Terms; 
4.1.9 use the latest templates for submitting Transaction Records as notified to the 
Nominated Agent by HKMA in accordance with Clause 21 (Notices) from
time to time; 
4.1.10 to the extent permitted under applicable Law, supply HKMA with all 
information concerning the Nominated Agent that is reasonably requested by 
HKMA and is: 
(a) related to the Nominated Agent's use of the Agency Reporting Service or 
Reporting System; or 
(b) reasonably and in good faith deemed by HKMA to be necessary in 
connection with any obligation of HKMA under any agreement relating 
to the Agency Reporting Service or any applicable Law; 
4.1.11 not provide, transfer or submit any Personal Data to HKMA except where, and 
to the extent, necessary for the Nominated Agent to fulfil the Member 
Principal's obligations under the Reporting Requirements; and 
4.1.12 where the Nominated Agent provides, transfers or submits any Personal Data 
to HKMA (whether in accordance with these Agency Terms or otherwise), to: 
(a) perform all acts; and 
(b) provide HKMA with all information and assistance, 
in each case which is necessary for HKMA to fulfil HKMA's obligations 
under any applicable Law in connection with such Personal Data. 
5. INSTRUCTIONS AND USERS 
5.1 The Nominated Agent may, in accordance with the relevant Annexes, nominate one 
or more individuals, who shall be Officers of the Nominated Agent, as authorised to 
access and use the Reporting System as Nominated Agent Users. 
5.2 The Nominated Agent understands, acknowledges and agrees that: 
5.2.1 all Nominated Agent Users may be able to access all the data under the 
Transaction Records submitted by the Nominated Agent under the Reporting 
System; 
5.2.2 it shall ensure that all Nominated Agent Users act (or refrain from acting) so as 
to ensure compliance by the Nominated Agent with all its obligations set forth 
in these Agency Terms;

## Page 71

11 
5.2.3 HKMA shall be entitled, without further enquiry, to execute or otherwise act 
upon instructions or information (including without limitation, Transaction 
Records) or purported instructions or information (including without limitation, 
Transaction Records) received from each Nominated Agent User or any 
person HKMA believes in good faith to be a Nominated Agent User; 
5.2.4 all instructions received by HKMA from a Nominated Agent User or any 
person HKMA believes in good faith to be a Nominated Agent User shall be 
binding on the Nominated Agent; and 
5.2.5 the Nominated Agent shall be solely and fully responsible for the acts and 
omissions of each Nominated Agent User. 
6. AGENCY CONDITIONS 
6.1 The Nominated Agent understands, acknowledges and agrees for the benefit of 
HKMA that, notwithstanding anything else in these Agency Terms (or the reporting 
service agreement entered into between the Member Principal and HKMA): 
6.1.1 without prejudice to Clause 7.1.6 (Representations and Warranties), the 
Nominated Agent, when effecting the Agency Arrangement or otherwise 
accessing and using the Reporting System on behalf of the Member Principal, 
is at all times acting as agent of the Member Principal and not as principal; 
6.1.2 the Nominated Agent, when acting in its capacity as agent of the Member 
Principal, may only access and use the Agency Reporting Service for the 
purpose of effecting the Agency Arrangement with the Member Principal and 
therefore may only submit the Transaction Records of the Member Principal 
under the Agency Arrangement with the Member Principal (and not the 
"Transaction Records" of any other entity). For the avoidance of doubt, each 
Nominated Agent and Nominated Agent User shall not be restricted from 
submitting transaction records: 
(a) of any other member of the Member Group in its capacity as agent 
for such member of the Member Group; or 
(b) for itself as principal in respect of any transactions it has entered 
into as principal; 
6.1.3 in consideration for HKMA permitting the Nominated Agent and each relevant 
Nominated Agent User to access and use the Reporting System in accordance 
with these Agency Terms, HKMA shall in no circumstance be liable to any 
Nominated Agent or Nominated Agent User (whether under contract, in tort or 
otherwise) in connection with the Agency Arrangement; and 
6.1.4 HKMA may, in HKMA's sole and absolute discretion, at any time and with 
immediate effect: 
(a) revoke HKMA's approval of the Nominated Agent to use and access 
the Agency Reporting Service; 
(b) terminate the right of the Nominated Agent User(s) to access and

## Page 72

12 
use the Reporting System; and/or 
(c) terminate these Agency Terms, 
without incurring any liability whatsoever to either the Member Principal or the 
Nominated Agent (whether under contract, in tort or otherwise). 
6.2 Any amendment, modification, variation or termination of the Agency Arrangement 
may only be in accordance with the procedures set out in the Reference Manual and 
these Agency Terms. 
7. REPRESENTATIONS AND WARRANTIES 
7.1 The Nominated Agent represents and warrants to HKMA at all times that: 
7.1.1 it has the capacity, power and authority to enter into and perform its 
obligations under these Agency Terms; 
7.1.2 these Agency Terms constitutes the legal, valid, binding and enforceable 
obligations of the Nominated Agent; 
7.1.3 any act or omission of the Nominated Agent (including any Nominated Agent 
User) in connection with the Agency Reporting Service or the Reporting 
System (including without limitation, the access to and use of the Agency 
Reporting Service or Reporting System) does not and will not breach any 
applicable Laws; 
7.1.4 it is not aware of any matter which might or will adversely affect its ability to 
perform its contractual obligations under these Agency Terms; 
7.1.5 the execution of these Agency Terms by it, the performance by it of its 
obligations and duties under these Agency Terms and its use of the Agency 
Reporting Service (including without limitation any submission of any data by 
it to HKMA under the terms of these Agency Terms) do not and will not 
breach the terms of any agreement to which it is a party, or by which it is 
otherwise bound or any privacy, confidentiality, fiduciary or secrecy 
obligations which it owes to any party; 
7.1.6 it is entering into these Agency Terms as principal for its own benefit and not 
for the benefit of another person; 
7.1.7 it has all licences, authorisations, consents, approvals and permits required by 
all applicable Laws in order to perform its obligations under these Agency 
Terms, including without limitation, all consents required for: 
(a) any transfer or disclosure (whether or not in accordance with these 
Agency Terms) of Personal Data by the Nominated Agent to 
HKMA; 
(b) any use, handling or storage of such Personal Data by HKMA in 
accordance with these Agency Terms; and

## Page 73

13 
(c) any transfer or disclosure of such Personal Data by HKMA to: 
(i) any Authority in Hong Kong or otherwise; 
(ii) any person in connection with HKMA's provision of the 
Agency Reporting Service to the Nominated Agent; 
(iii) any person in connection with HKMA's compliance with any 
Law (including, without limitation, any Reporting 
Requirements) or any order, judgment, decision, directive or 
request of any Authority, for any purpose whatsoever 
(including without limitation, the prevention of money 
laundering, terrorist financing and other criminal activities); 
and 
(iv) otherwise in accordance with these Agency Terms (including, 
without limitation in accordance with the terms of Clause 9 
(Confidentiality)); 
7.1.8 it has not provided, transferred or submitted any Personal Data to HKMA 
except where, and to the extent, necessary for the Member Principal to fulfil 
the Member Principal's Reporting Requirements; and 
7.1.9 any Personal Data provided by the Nominated Agent to HKMA (whether in 
accordance with these Agency Terms or otherwise): 
(a) has been collected by lawful means; and 
(b) is accurate in all material respects so far as the Nominated Agent is 
aware; and 
7.1.10 there is no: 
(a) publicly available information; or 
(b) information provided directly or indirectly by the Nominated Agent 
to HKMA (save for information provided to HKMA at the request 
of HKMA in accordance with Clause 11.4 (Personal Data)), 
which would allow HKMA to be able to ascertain from the Personal Codes 
the identity of any counterparty to a Transaction who is an individual. 
7.2 HKMA does not make, and hereby expressly disclaims, any representation, warranty 
or undertaking: 
7.2.1 in respect of the Agency Reporting Service or the Reporting System; 
7.2.2 that any method of accessing the Reporting System is secure; 
7.2.3 in respect of any Agency Arrangement, and the Nominated Agent 
acknowledges and agrees that HKMA has not renewed the terms of any 
Agency Arrangement and takes no responsibility for the terms of such Agency

## Page 74

14 
Arrangement and/or any other terms agreed between the Nominated Agent and 
the Member Principal; 
7.2.4 that any Transaction or Transaction Record: 
(a) will constitute enforceable, legal, valid and binding obligations, or 
will otherwise give rise to any duly-formed and legally binding 
contract under any Laws; 
(b) will evidence any Transaction in accordance with any applicable 
documentation or master document; 
(c) is accurate or complete; or 
(d) will be successfully completed or performed; 
7.2.5 that any Transaction Record or any other data held by HKMA will be 
admissible in a court of Law or other proceeding; 
7.2.6 that any Transaction is: 
(a) required to be reported to HKMA under the Reporting
Requirements applicable to the Member Principal or otherwise in 
accordance with any applicable Law; or 
(b) compliant with any and all applicable Laws and does not breach or 
violate any applicable Law; 
7.2.7 that any party to a Transaction will fulfil its obligations under such 
Transaction to the other party; or 
7.2.8 in respect of the creditworthiness or financial position of the Member Principal, 
any member of the Member Group or any other party to a Transaction. 
8. LIABILITY 
8.1 HKMA and HKMA's Officers shall not be liable to the Nominated Agent for any 
liability, claim, loss, damage, action, proceeding, demand, cost, fee or expense of any 
kind or nature whatsoever and howsoever caused in connection with the operation by 
HKMA of the Agency Reporting Service or the Reporting System or any part thereof 
(whether or not resulting from a failure to satisfy the Member Principal's obligations 
under the Reporting Requirements), including, without limitation, any liability, claim, 
loss, damage, action, proceeding, demand, cost, fee or expense (whether or not 
resulting from a failure to satisfy the Member Principal's obligations under the 
Reporting Requirements) arising directly or indirectly from or as a result of: 
8.1.1 any inadequacy, deficiency, defect or error of the Agency Reporting Service, 
the Reporting System or any linking or validation of Transaction Records in 
relation to the Agency Reporting Service; 
8.1.2 any discrepancy between any Transaction Record and the corresponding actual 
trade data or any other relevant document or data (including without

## Page 75

15 
limitation, any confirmation or evidence of the relevant Transaction); 
8.1.3 any delay in providing or failure to provide the Agency Reporting Service or 
the Reporting System; 
8.1.4 any interruption, variation, suspension or termination of the Agency Reporting 
Service or the Reporting System (including, without limitation, arising directly 
or indirectly from HKMA exercising HKMA's rights under Clause 2.2 (Using 
the Agency Reporting Service) or otherwise); 
8.1.5 where HKMA relied, acted or refused to act or refrained from acting on any 
instruction (or purported instruction) from a Nominated Agent User or any 
person HKMA believes in good faith to be a Nominated Agent User (including 
in circumstances where such instruction or purported instruction is 
unauthorised or given by an unauthorised person) or any person HKMA 
suspects may not be a Nominated Agent User, including, without limitation, 
any reliance by HKMA in good faith on any instructions or other 
communication in person or by telephone, facsimile, email or other electronic 
means; 
8.1.6 any information howsoever provided to HKMA or any of HKMA's Officers in 
any form, including any Transaction Record, that is incomplete, erroneous or 
inaccurate; 
8.1.7 any Transaction or Transaction Record not being legal, valid, binding and/or 
enforceable (including, without limitation, where a Transaction is not capable 
of being enforced); 
8.1.8 any Transaction Record: 
(a) not complying with the Reporting Requirements or any other 
applicable Law; 
(b) not complying with and/or being consistent with the relevant ISDA 
Master Agreement or any other master agreement and/or any 
relevant ISDA-published or other definitions or protocols; 
(c) not being admissible in a court of law or other proceedings; and/or 
(d) being incorrect, including where it has been incorrectly submitted, 
recorded or stored; 
8.1.9 any virus, default, defect, deficiency or malfunction in or any breakdown, 
disruption or failure of any telecommunications, computer or other electronic 
equipment or system (whether or not owned, operated or maintained by 
HKMA or for the purpose of, or in connection with, the Agency Reporting 
Service or the Reporting System); 
8.1.10 the security, confidentiality, accuracy and reliability (or lack thereof) of any 
document, email, transaction record and any other information transferred 
through or using the Reporting System;

## Page 76

16 
8.1.11 the transfer and/or disclosure of any information by HKMA to any party in 
compliance with and/or under the terms of these Agency Terms, including 
without limitation under Clause 9 (Confidentiality) of these Agency Terms; 
8.1.12 the transmission or quality of the data, the quality and availability of any data 
transmission network or any service interruption, blockage, suspension or 
interruption in any method of transmission or means of telecommunication 
(including SWIFT), any communication line, modem connection or other 
transmission facility, including without limitation as a result of the connection 
or lack thereof to any website or any internet and/or browser-based system 
used in relation to the Agency Reporting Service or the Reporting System; 
8.1.13 the failure by the Nominated Agent to follow the most current version of these 
Agency Terms or any notice, guideline or other document communicated to it 
in accordance with Clause 21 (Notices); 
8.1.14 the occurrence of any Force Majeure Event; 
8.1.15 any act or omission of any third party including, without limitation, any other 
Authority; 
8.1.16 any act and/or omission of the Member Principal; 
8.1.17 any breach of any of the Nominated Agent's obligations under these Agency 
Terms; 
8.1.18 HKMA's compliance with any applicable Law in connection with these 
Agency Terms, the Agency Reporting Service, the Member Principal, any 
other person of the Nominated Agent Group, any member of the Member 
Group and/or any Transaction Record; and/or 
8.1.19 any act or omission of any Nominated Agent User (including without 
limitation, such Nominated Agent User's use or disclosure of any data it has 
obtained from, or in connection with, the Agency Reporting Service (including 
any Transaction Record data)), 
unless incurred directly due to the wilful default or reckless disregard of HKMA in respect of 
HKMA's obligations under these Agency Terms. 
8.2 Notwithstanding any other term of these Agency Terms, HKMA shall not be liable for 
any indirect, incidental, consequential or punitive damages, losses or costs including 
any economic loss, loss of business, loss of profit, loss of reputation, loss of 
opportunity or for any claim made against the Nominated Agent by any other party, 
even if advised of the possibility of the Nominated Agent incurring such damages, 
losses or costs. 
8.3 The Nominated Agent shall indemnify HKMA and HKMA's Officers against any 
liability, claim, loss, damage, action, proceeding, demand, cost, fee or expense of any 
kind or nature whatsoever and howsoever arising directly or indirectly from: 
8.3.1 HKMA's provision of the Agency Reporting Service to the Nominated Agent;

## Page 77

17 
8.3.2 any act or omission of the Nominated Agent, its Officers and/or its Nominated 
Agent Users (or any person HKMA reasonably believes to be the Nominated 
Agent, its Officer or its Nominated Agent User) in connection with the Agency 
Reporting Service, these Agency Terms and/or the Agency Arrangement; and 
8.3.3 any failure of the Nominated Agent (including any Nominated Agent User) to 
comply with these Agency Terms, any other obligations applicable to the 
Nominated Agent or the Member Principal, any of the Member Principal's 
obligations under the Reporting Requirements or any other applicable Law. 
8.4 Nothing in these Agency Terms shall limit or exclude HKMA's liability for death or 
personal injury caused by (i) HKMA's negligence or (ii) the negligence of HKMA's 
Officers, except as permitted by Law. 
8.5 The invalidity, illegality or unenforceability of a provision of this Clause 8 (Liability) 
does not affect or impair the continuation in force of the remainder of this Clause. 
9. CONFIDENTIALITY 
9.1 In this Clause, "Confidential Information" means all information from time to time 
disclosed (whether in writing, orally or by another means and whether directly or 
indirectly) by a Party (the "Disclosing Party") to the other Party (the "Receiving 
Party") whether before, on or after the date of these Agency Terms including, without 
limitation:
9.1.1 any Transaction Record; 
9.1.2 any data (including without limitation, any report or analysis) which may be 
produced as a result of processing any such Transaction Record; 
9.1.3 any details of the Reporting System (including without limitation, the technical 
information and specifications of the Reporting System); and 
9.1.4 any information relating to any product, service, operation, process, plan or 
intention, product information, know-how, design right, trade secret, market 
opportunity or business affairs of the Disclosing Party, 
but does not include information which: 
(a) is or becomes public information other than as a direct or indirect result of any 
breach of these Agency Terms by the Receiving Party; 
(b) is identified in writing at the time of delivery as non-confidential by the 
Disclosing Party or any of its Officers; and/or 
(c) is known by the Receiving Party before the date such information is disclosed 
to it by the Disclosing Party or is lawfully obtained by the Receiving Party 
after that date from a third party source which is, as far as the Receiving Party 
is aware, unconnected with the Disclosing Party and which, in either case, as 
far as the Receiving Party is aware, has not been obtained in breach of, and is 
not otherwise subject to, any obligation of confidentiality in relation to such 
information.

## Page 78

18 
9.2 The Receiving Party shall not transfer or disclose Confidential Information to any 
third party or use Confidential Information for any reason except as expressly 
contemplated in these Agency Terms, save that: 
9.2.1 the Receiving Party may disclose Confidential Information with the prior 
written consent of the Disclosing Party in the manner consented to; 
9.2.2 the Receiving Party may disclose Confidential Information to any of its 
Officers to the extent that such disclosure is necessary for the purposes of 
these Agency Terms and each Officer is made aware of, and complies with, 
the Receiving Party's obligations of confidentiality under these Agency Terms 
as if the Officer was a party to these Agency Terms; 
9.2.3 the Receiving Party may disclose Confidential Information to the extent 
required by any applicable Law; 
9.2.4 HKMA may publicly disclose anonymous data, including without limitation, 
aggregate positions, transaction activity or statistical data, so long as: 
(a) individual persons of the Member Group cannot be identified from 
such data; and 
(b) such data does not reveal, directly or indirectly, any confidential, 
proprietary, financial, operational or trading data of the Member 
Principal; and 
9.2.5 HKMA may use and/or disclose any Confidential Information to the extent 
necessary and/or desirable for HKMA to carry out any of HKMA's functions 
and duties. 
9.3 Without prejudice to any other term of these Agency Terms and to the fullest extent 
permitted by Law, the Receiving Party shall promptly, and in any event within 14 
Business Days, inform the Disclosing Party in writing of any disclosure of any 
Confidential Information of the Disclosing Party to any other entity besides the 
Receiving Party, in particular specifying: 
9.3.1 the Confidential Information which was disclosed; 
9.3.2 the method by which the Confidential Information was disclosed; and 
9.3.3 the identity of the entity to which the Confidential Information was disclosed, 
unless such disclosure is made by: 
(a) HKMA and is: 
(i) necessary for the purposes of HKMA providing the (1) Agency 
Reporting Service to the Nominated Agent or any other person within 
the Nominated Agent Group or (2) "Reporting Service" to any member 
of the Member Group; or 
(ii) made under the terms of Clauses 9.2.1 (Confidentiality) to 9.2.5

## Page 79

19 
(Confidentiality); or 
(b) the Nominated Agent: 
(i) under the terms of Clause 9.2.2 (Confidentiality); or 
(ii) to the Member Principal or any of the Member Principal’s Officers, 
and is necessary for the purposes of the Nominated Agent providing 
service to the Member Principal under the Agency Arrangement. 
9.4 The Nominated Agent consents to, and agrees to obtain any necessary consent of, and 
give any necessary notice to, the relevant persons (including any of its relevant 
Nominated Agent Users or Officers) of, the monitoring and recording of: 
9.4.1 any telephone conversation between any Officer or Nominated Agent User of 
the Nominated Agent and HKMA and/or any Officer of HKMA in connection 
with these Agency Terms; and 
9.4.2 the Nominated Agent’s use of the Agency Reporting Service, 
and agrees, to the extent permitted by applicable Law, that any data obtained from 
such monitoring or recording may be submitted as evidence in any proceeding. 
10. OFFICES AND BRANCHES 
If the Nominated Agent is entering into these Agency Terms through an office or 
branch other than its head or home office, it represents at all times to, and agrees with, 
HKMA that, notwithstanding the place of booking or branch or its jurisdiction of 
incorporation or organisation, its obligations are the same in terms of recourse against 
it as if it had entered into these Agency Terms through its head or home office. 
11. PERSONAL DATA 
11.1 If the Nominated Agent provides any Personal Data to HKMA (whether in breach of 
these Agency Terms or otherwise), the Nominated Agent shall promptly notify 
HKMA of, and take all necessary and/or desirable actions to identify, such Personal 
Data to HKMA and, where such Personal Data is provided by the Nominated Agent 
to HKMA in breach of these Agency Terms, immediately remove such Personal Data 
from the Reporting System. 
11.2 HKMA is not responsible for the management or handling of any Personal Data 
which is provided to HKMA by the Nominated Agent in breach of these Agency 
Terms. 
11.3 Personal Data disclosed from time to time by the Nominated Agent to HKMA 
(whether or not in breach of these Agency Terms) may, notwithstanding such breach, 
be used, transferred or disclosed by HKMA: 
11.3.1 to any Authority in Hong Kong or otherwise; 
11.3.2 to any person in connection with HKMA's provision of the Reporting Service 
or the Agency Reporting Service;

## Page 80

20 
11.3.3 to any person in connection with HKMA's compliance with any Law 
(including without limitation, the prevention of money laundering, terrorist 
financing and other criminal activities); and/or 
11.3.4 otherwise in accordance with these Agency Terms (including, without 
limitation in accordance with the terms of Clause 9 (Confidentiality)). 
11.4 Notwithstanding any other term of these Agency Terms, the Nominated Agent 
acknowledges and agrees that, in no circumstance shall the Nominated Agent disclose 
to HKMA or make public any information which may allow or assist (or potentially 
allow or assist) HKMA to ascertain the identity of any counterparty to a Transaction 
who is an individual (including without limitation, any data or information which in 
any way links or connects the Personal Code of an individual to any other data or 
information which allows or assists HKMA to ascertain the identity of such 
individual), unless specifically requested to do so by HKMA. 
12. OWNERSHIP OF INTELLECTUAL PROPERTY RIGHTS 
12.1 For the duration of these Agency Terms, HKMA grants the Nominated Agent a 
personal, limited, revocable, non-transferable, non-sub-licensable and non-exclusive 
licence to access and use the Reporting System subject to the terms and conditions of 
these Agency Terms. 
12.2 Except as provided in these Agency Terms, the Nominated Agent shall not, without 
the prior written consent of HKMA: 
12.2.1 market, exploit or make the Reporting System available to another person or 
permit another person to use the Reporting System; 
12.2.2 use the Reporting System on behalf of or for the benefit of another person 
besides the Member Principal (including for the provision of commercial 
timesharing, rental or bureau services); 
12.2.3 reverse engineer, decompile, disassemble, translate or adapt the program code 
or any other part of the Reporting System; 
12.2.4 make any copy, modify or create any derivative work of the Reporting System; 
or 
12.2.5 assign, charge or otherwise dispose of any interest or right in its licence to use 
the Reporting System. 
12.3 All Intellectual Property Rights subsisting in, created generated or used by HKMA or 
HKMA's Officers (or on their behalves) in connection with these Agency Terms 
(including without limitation, the text of these Agency Terms), the Agency Reporting 
Service, the Reporting System (as modified from time to time) or any other material 
or document (whether in electronic or physical form), including any operational 
procedure, guide, instruction or manual, report (including any request reports), 
notifications, any Transaction Record and/or template thereof, or the Reference 
Manual provided in connection with these Agency Terms, are and shall remain the 
exclusive property of HKMA. The Nominated Agent shall not acquire any right in 
the Reporting System or any of the foregoing except the limited use rights specified in

## Page 81

21 
these Agency Terms. HKMA shall own all rights in any copy, translation, 
modification, adaptation or derivative work of the Reporting System or based on any 
of the foregoing, including any improvement or development thereof. 
13. TERMINATION 
13.1 These Agency Terms shall remain in force until terminated in accordance with the 
procedures set out in the Reference Manual. 
13.2 Notwithstanding Clause 13.1 above, HKMA may terminate these Agency Terms with 
immediate effect at any time by written notice to the Nominated Agent. 
14. CONSEQUENCES OF TERMINATION 
14.1 Expiry or termination of these Agency Terms does not affect a Party's accrued rights 
and obligations at the date of expiry or termination. 
14.2 Subject to Clause 14.1 (Consequences of Termination) above, each Party shall be 
released and discharged from any further rights and obligations immediately on the 
expiry or termination of these Agency Terms, except that any right or obligation 
(whether accrued or not) under or pursuant to any of Clauses 8 (Liability), 9, 
(Confidentiality), 11 (Personal Data), 12 (Ownership of Intellectual Property Rights), 
14 (Consequences of Termination), 16 (Assignment and Subcontracting), 17 (Entire 
Agreement), 18 (General), 19 (Governing Law and Jurisdiction), 20 (Service of 
Process) and 21 (Notices) together with those Clauses the survival of which is 
necessary for the interpretation or enforcement of these Agency Terms, shall survive 
expiry or termination of these Agency Terms and shall continue in full force and 
effect. 
14.3 Upon the expiry or termination of these Agency Terms, the Nominated Agent shall 
use all reasonable efforts to promptly return to HKMA or destroy, all copies of these 
Agency Terms and all other documents in connection with the Agency Reporting 
Service then in its possession, including any copies held in any format in any 
electronic media, provided that the Nominated Agent shall not be obliged to take such 
action if doing so would be inconsistent with any applicable Law or its reasonable 
internal record retention policies.; and 
14.3.1 cease to access or use, and give up all its rights in connection with the access 
and use of: 
(a) the Reporting System; 
(b) the Agency Reporting Service; and 
(c) any document in connection with the Reporting System and/or the 
Agency Reporting Service. 
15. FORCE MAJEURE 
15.1 Without prejudice to any other term of these Agency Terms, if a Party (the "Affected 
Party") is prevented, hindered or delayed by a Force Majeure Event from or in 
performing any of its obligations under these Agency Terms other than a payment

## Page 82

22 
obligation: 
15.1.1 the Affected Party's obligations under these Agency Terms are suspended only 
for so long as the Force Majeure Event continues and only to the extent that it 
is so prevented, hindered or delayed; 
15.1.2 as soon as reasonably possible after the start of the Force Majeure Event the 
Affected Party will notify the other Party of the Force Majeure Event, the date 
on which the Force Majeure Event started and the effects of the Force Majeure 
Event on its ability to perform its obligations under these Agency Terms; 
15.1.3 the Affected Party will make reasonable efforts to mitigate the effects of the 
Force Majeure Event on the performance of its obligations under these Agency 
Terms; and 
15.1.4 as soon as reasonably possible after the end of the Force Majeure Event the 
Affected Party will notify the other Party that the Force Majeure Event has 
ended and resume performance of its obligations under these Agency Terms. 
15.2 Without prejudice to Clause 13 (Termination), if the Force Majeure Event continues 
for more than 30 consecutive calendar days commencing on the day the Force 
Majeure Event starts, either Party may terminate these Agency Terms by giving not 
less than 14 calendar days' notice to the other Party. 
16. ASSIGNMENT AND SUBCONTRACTING 
16.1 The Nominated Agent may not: 
16.1.1 assign, transfer, charge or otherwise dispose of any interest or right in or in 
respect of, or purport to assign, transfer, charge or otherwise dispose of any 
interest or right in or in respect of, any right or obligation under these Agency 
Terms; or 
16.1.2 subcontract the performance of any of its obligations under these Agency 
Terms, 
without the prior written consent of HKMA. 
16.2 HKMA may from time to time assign or transfer HKMA's rights and/or obligations in 
respect of these Agency Terms, in whole or in part, in each case without the consent 
of the Nominated Agent. 
17. ENTIRE AGREEMENT 
17.1 These Agency Terms, including the schedules to these Agency Terms, the Agent 
Nomination Form and the Annexes, constitute the entire agreement between the 
Parties to these Agency Terms and supersedes all previous agreements between the 
Parties relating to the subject matter of these Agency Terms. 
17.2 Each Party acknowledges that it has not relied on or been induced to enter into these 
Agency Terms by a representation, warranty or undertaking (whether contractual or 
otherwise) other than those expressly set out in these Agency Terms.

## Page 83

23 
17.3 A Party is not liable to the other Party (in equity, contract or tort (including 
negligence) or in any other way) for a representation, warranty or undertaking that is 
not set out in these Agency Terms. 
17.4 Nothing in this Clause 17 (Entire Agreement) has the effect of limiting or restricting 
any liability of a Party arising as a result of any fraud. 
18. GENERAL 
18.1 The rights and obligations of HKMA and the Nominated Agent under these Agency 
Terms shall take effect on the Agency Approval Date. 
18.2 In the event of any inconsistency between any provision of the Substantive Provisions 
and any Annex, the Substantive Provisions shall prevail. 
18.3 HKMA may in HKMA's sole and absolute discretion, at any time, amend, restate or 
supplement the Substantive Provisions or any Annex by giving the Nominated Agent 
no less than five Business Days' written notice of such amendment, restatement or 
supplement. 
18.4 A failure to exercise or delay in exercising a right or remedy provided by these 
Agency Terms or by any applicable Law does not constitute a waiver of the right or 
remedy or a waiver of any other right or remedy. No single or partial exercise of a 
right or remedy provided by these Agency Terms or by Law prevents further exercise 
of the right or remedy or the exercise of another right or remedy. 
18.5 Except where these Agency Terms provide otherwise, the rights and remedies 
contained in these Agency Terms are cumulative and not exclusive of rights or 
remedies provided by any applicable Law. 
18.6 Except where these Agency Terms provide otherwise, each Party shall pay its own 
costs relating to the negotiation, preparation, execution and implementation by it of 
these Agency Terms and of each document referred to in it. 
18.7 No provision of these Agency Terms creates a partnership between the Parties or 
makes a Party the agent of the other Party for any purpose. A Party has no authority 
or power to bind, to contract in the name of, or to create a liability for the other Party 
in any way or for any purpose. 
19. GOVERNING LAW AND JURISDICTION 
19.1 These Agency Terms and all matters arising from or connected with it are governed 
by Hong Kong law. 
19.2 The courts of Hong Kong have exclusive jurisdiction to settle any dispute arising out 
of or in connection with these Agency Terms (including a dispute relating to the 
existence, validity or termination of these Agency Terms or the consequences of its 
nullity) (a "Dispute"). 
19.3 The Parties agree that the courts of Hong Kong are the most appropriate and 
convenient courts to settle Disputes and accordingly no Party will argue to the 
contrary.

## Page 84

24 
19.4 Nothing in this Clause 19 (Governing Law and Jurisdiction) has the effect of limiting 
or preventing HKMA from taking proceedings relating to a dispute in connection with 
these Agency Terms in any other courts with jurisdiction. To the extent allowed by 
any applicable Law, HKMA may take concurrent proceedings in any number of 
jurisdictions. 
20. SERVICE OF PROCESS 
20.1 If the Nominated Agent is not resident, incorporated or registered in Hong Kong: 
20.1.1 the Nominated Agent represents and warrants that it has irrevocably appointed 
the entity whose details are set out in the Agent Nomination Form as the 
process agent to receive, for it and on its behalf, service of process in any 
dispute arising out of or in connection with these Agency Terms; and 
20.1.2 if for any reason the process agent (or the substitute process agent, as the case 
may be) is unable to, or will not, act as such, the Nominated Agent shall 
promptly notify HKMA and within 30 calendar days appoint a substitute 
process agent acceptable to HKMA. 
20.2 The Parties irrevocably consent to receive service of process in the manner provided 
for notices in Clauses 21.1.1 (Notices), 21.1.2 (Notices) or 21.1.3 (Notices). Nothing 
in these Agency Terms shall affect the right of HKMA to serve process in any other 
manner permitted by any applicable Law. 
21. NOTICES 
21.1 Any notice or other communication in respect of these Agency Terms may be given in 
any manner described below to the address or number or in accordance with the 
relevant details as set out in Schedule 1 (Notice Details) and will be deemed effective 
as indicated: 
21.1.1 if in writing and delivered in person or by courier, on the date and time it is 
delivered; 
21.1.2 if sent by facsimile transmission, on the date and time it is received by a 
responsible employee of the recipient in legible form (it being agreed that the 
burden of proving receipt will be on the sender and will not be met by a 
transmission report generated by the sender’s facsimile machine); 
21.1.3 if sent by certified or registered mail (airmail, if overseas) or the equivalent 
(return receipt requested), on the date and time it is delivered or its delivery is 
attempted; 
21.1.4 if sent by the notification and announcement system in the Reporting System, 
on the date and time it is sent; or 
21.1.5 if sent by e-mail, on the date and time it is delivered, 
unless the date of that delivery (or attempted delivery) or that receipt, as applicable, is 
not a Business Day or that communication is delivered (or attempted) or received, as 
applicable, after the close of business on a Business Day, in which case that

## Page 85

25 
communication will be deemed given and effective on the open of business on the 
first following day that is a Business Day. 
21.2 Any notice or announcement may be sent or announced to the Nominated Agent via 
the notification and announcement system in the Reporting System from time to time 
in accordance with Clause 21.1.4 (Notices). The Nominated Agent undertakes 
therefore to check the notification and announcement system in the Reporting System 
regularly, and in any event no less than once each Business Day, for any such notices 
or announcements. 
21.3 Either Party may by no less than ten Business Days' prior written notice to the other 
change the address, facsimile number or e-mail details at which notices or other 
communications are to be given to it. 
21.4 Notwithstanding anything else in these Agency Terms, a notice or other 
communication under Clause 13 (Termination) may not be given by any method 
specified in Clauses 21.1.2 (Notices), 21.1.4 (Notices) or 21.1.5 (Notices).

## Page 86

26 
SCHEDULE 1 
NOTICE DETAILS 
Contact details for notices or communications to HKMA:
Address: 55/F, Two International Finance Centre, 8 Finance Street, Central, Hong Kong 
Attention: Trade Repository, Hong Kong Monetary Authority 
Facsimile No.: (852) 2878 1679 
Telephone No.: (852) 8100 3115 
Email: hktr@hkma.gov.hk 
[Specific Instructions: [•]] 
Contact details for notices or communications to the Nominated Agent are set out in 
the Agent Nomination Form.

## Page 87

Agent Profile Maintenance Form for Reporting Service
To : Hong Kong Monetary Authority Date:
Facsimile: (852) 2878 1679 
 
From : ( ) 
Name of TR Member (“Member Principal”) TR Member Code 
We refer to the nomination of __________________________(Name of the Nominated 
Agent) by our institution to submit trade information of OTC derivatives transactions to the 
HKTR on behalf of our institution, please find below the scope of information to be 
submitted by the Nominated Agent: 
Channels for trade submission by the Nominated Agent (please tick as appropriate) 
 User Interface (“UI”) through Internet and SWIFTNet 
 File Transfer Service (“FTS”) through ICLNet 
 FileAct through SWIFTNet 
 Others (to be agreed with the HKMA and confirmed in the Approval Confirmation of 
the Agent Nomination Form) 
Access by the Nominated Agent to User Interface (UI) Full Functions* (please tick as 
appropriate) 
 Yes No 
*UI Full Functions include enquiry functions for trade and trade events 
Hong Kong Monetary Authority 
OTC Derivatives Trade Repository 
Appendix TR.9A
The signed original of the completed form must be submitted to the HKMA

## Page 88

OTC derivatives to be processed by the Nominated Agent (please tick as appropriate) 
Product Type Product Sub-type
Interest Rate Swap IRS Floating vs Fixed 
 (deliverable and non-deliverable) 
 Basis Swap (Floating vs Floating) 
 
 Overnight Index Swap (Floating vs Fixed) 
 
FX Non Deliverable Forward FX Non Deliverable Forward 
 
_______________________________ ________________________________ 
Authorized Signature(s) of Nominated Agent Authorized Signature(s) of Member Principal 
 Company Chop Company Chop

## Page 89

HKTR Reporting Service Product Scope
The following are the products supported by the Reporting Service of the HKTR: 
Interest rate derivatives 
Product Type Product Sub-Type 
Notional Currency 
(Single-Currency 
only) 
Floating Rate Index 
IRS Floating vs Fixed 
(deliverable) 
IRS Floating vs Fixed 
(non-deliverable) 
Basis Swap 
(Floating vs Floating) 
Interest Rate 
Swap 
Overnight Index Swap 
(Floating vs Fixed ) 
ISO 4217 currencies 
specified in the 
Reporting Service 
AIDG 
ISDA-defined Floating 
Rate Indexes specified in 
the Reporting Service 
AIDG 
Foreign exchange derivatives 
Product Type Product Sub-Type Currency in the currency pair 
FX Non 
Deliverable 
Forward 
FX Non Deliverable 
Forward 
ISO 4217 currencies specified in the 
Reporting Service AIDG 
Hong Kong Monetary Authority 
OTC Derivatives Trade Repository 
Annex 1

## Page 90

(This page is intentionally left blank)

## Page 91

Fee Scale for Reporting Service
TR Membership fee
No fee or charge applies to the participation and maintenance of a TR Membership. 
Transaction fee
Monthly transaction maintenance fee of HK$3 per outstanding transaction per month on a 
per-side basis, i.e. both reporting entities are subject to charge. The fee will be calculated 
with reference to the number of outstanding transactions (transactions not yet matured) 
maintained at the TR on the last working day of each month. 
Aggregate cap on transaction maintenance fee of HK$1 million per reporting entity per 
annum. The cap applicable to a new user will be calculated on a pro-rata basis with reference 
to the remaining number of month-ends in the calendar year after the user starts reporting. 
Supplementary Notes 
1. The fee schedule may be modified by the HKTR from time to time, however, the HKTR 
undertakes to advise members in advance of such changes 
2. All fees are invoiced in Hong Kong dollar and billed monthly to TR members. The total 
amount of fees payable will be advised to members on the 10th day of the following 
month or the next business day if the 10th is not a business day. The total fees will be 
automatically debited from the settlement account designated by members on the 15th day 
or the following business day if 15th is not a business day. 
Hong Kong Monetary Authority 
OTC Derivatives Trade Repository 
Annex 2

## Page 92

(This page is intentionally left blank)

## Page 93

Personal Information Collection Statement of the Monetary Authority 
for the Reporting Service under the Trade Repository
 
 This Personal Information Collection Statement ("Statement") sets out the policies and practices of the 
Monetary Authority ("MA") with regard to Personal Data as defined in the Personal Data (Privacy) Ordinance, 
Cap 486 (the "PDPO"), that the MA has collected, and will be collecting, from you from time to time in 
connection with the MA's provision of the Reporting Service to you and what you are agreeing to with respect 
to the MA's use of your Personal Data for the purposes and in the manner identified in paragraphs 1 and 2 below. 
The MA may provide the Reporting Service to you in order to assist you to meet your Reporting Requirements, 
which oblige you to report to the MA certain over-the-counter derivatives transactions that you may enter into 
from time to time. Unless defined in this Statement or the context otherwise requires, a term defined in the 
reporting service agreement between the MA and yourself ("Reporting Service Agreement") has the same 
meaning in this Statement. 
1. Purpose of Collection and Use of Personal Data
The MA may collect Personal Data from you from time to time and such Personal Data may be used, 
stored, processed, transferred, disclosed or shared by the MA for one or more of the following purposes: 
a. exercise the functions of the MA as set out in the Banking Ordinance (the "BO"), the principal 
one of which is to promote the general stability and effective working of the banking system; 
b. exercise the powers and duties vested in the MA under the Securities and Futures Ordinance 
(the "SFO"), and for carrying out the MA's functions under the SFO; 
c. transfer or disclose information (including your Personal Data) to other persons in accordance 
with the provisions of the BO and the SFO; 
d. provide the Reporting Service to you; 
e. perform all of the MA's obligations under any agreement or arrangement with you, including 
without limitation the Reporting Service Agreement; 
f. perform any Matching Procedures (as defined in Section 2 of the PDPO), verification or other 
similar procedures the MA may deem necessary or desirable; 
g. enforce any obligations owed by you to the MA, including the collection of any fees or other 
amounts outstanding from you to the MA; 
h. comply with any of the MA's obligations under any Law (including without limitation any 
disclosure requirements imposed on the MA); and 
i. comply with any order or request from any Authority in or outside Hong Kong, whether 
pursuant to any regulatory or investigatory assistance arrangements between the MA and such 
Authority or otherwise. 
Failure to supply such Personal Data as requested by the MA from time to time may result in hindering 
the MA from performing the MA's functions or providing the Reporting Service to you, and in some 
cases, may constitute an offence. 
Annex 7
-1-

## Page 94

2. Disclosure and/or Transfer of Personal Data 
The MA may, for one or more of the purposes set out in paragraph 1 above, disclose or transfer your 
Personal Data to one or more of the following persons in Hong Kong or elsewhere: 
a. any Authority (including other local and overseas regulators as well as government bodies 
such as the Hong Kong Police and the Independent Commission Against Corruption); 
b. any officer or employee of the MA; 
c. any other member of the Member Group; 
d. any trade repository for over-the-counter derivatives transactions; and 
e. any other person to whom the MA reasonably determines the disclosure or transfer of your 
Personal Data is necessary for the MA to fulfil the purposes set out in paragraph 1 above. 
Your Personal Data may be disclosed or transferred to a location which does not have the legal 
protection of information equivalent to that in Hong Kong. 
3. Access to Personal Data 
In accordance with the terms of the PDPO and subject to the provisions and exemptions set out in Part 
VIII of the PDPO, you have the right to: 
a. check whether the MA holds Personal Data about you, be informed of the kind of Personal 
Data held by the MA and access such Personal Data; 
b. require the MA to correct any Personal Data relating to you which is inaccurate; and 
c. ascertain the MA's policies and practices in relation to Personal Data held by the MA. 
The MA takes all practicable steps to ensure that an individual can ascertain the MA’s policies and 
practices in relation to Personal Data and be informed of the kind of Personal Data held by the MA and
the main purposes for which the Personal Data held by the MA are or are to be used. 
In accordance with the PDPO, the MA has the right to charge a reasonable fee for the processing of any
Personal Data access request. 
All enquiries regarding the Personal Data provided or requests for access to Personal Data or correction 
of Personal Data, should be addressed in writing to: 
Personal Data Privacy Officer (Trade Repository) 
Hong Kong Monetary Authority 
55/F., Two International Finance Centre 
8 Finance Street 
Central, Hong Kong 
Please note that all data access requests should be made using the form specified by the Privacy 
Commissioner for Personal Data, which is accessible from the following link: 
 http://www.pcpd.org.hk/english/publications/files/Dforme.pdf
-2-

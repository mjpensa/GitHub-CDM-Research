# esma position calculation guidelines 2024

*Converted from: esma-position-calculation-guidelines-2024.pdf*

---

## Page 1

01.03.2024
ESMA12-2121844265-3254
Guidelines on position calculation 
under EMIR Refit

## Page 2

1
1 Guidelines
TRs should calculate position data and make it available in four separate datasets − 
Position Set, Collateral Position Set, Currency Position Set and Currency Collateral 
Position Set. These datasets should be uniquely identifiable and labelled with the relevant 
reference date.
Unless otherwise specified, all the Guidelines apply to each calculation. This excludes the 
following Guidelines which should be applied only to the following calculations:
a) Guideline 19, Guideline 24, Guideline 25, Guideline 26, Guideline 31, and Guideline 
32 are applicable to Positions Sets;
b) Guideline 20, Guideline 24, Guideline 25, Guideline 26, Guideline 31, and Guideline 
32 are applicable to Currency Position Sets;
c) Guideline 21, Guideline 22, Guideline 23, and Guideline 30 are relevant to 
Collateral Position Sets;
d) Guideline 21, Guideline 22, Guideline 23, Guideline 30, Guideline 31, and Guideline 
33 are applicable to Currency Collateral Position Sets;
e) Guideline 27 is only applicable to Position Sets and Currency Position Sets where 
the field Asset class (T2F11) is reported as ‘INTR’ and field Contract type (T2F10) 
is reported as ‘SWAP’;
f) Guideline 28 is only applicable to Position Sets and Currency Position Sets where 
the field Asset class (T2F11) is reported as ‘CRDT’;
g) Guideline 29 is only applicable to Position Sets and Currency Position Sets where 
the field Asset class (T2F11) is reported as ‘COMM’.
TRs should calculate positions consistently irrespective of whether the derivative reported 
is single or dual-sided and consistently irrespective of the reconciliation status of the report.
TRs should determine outstanding derivatives, as referred to in Article 2(2) of ITS on 
reporting, to calculate the set of outstanding derivatives pertaining to a position.
TRs should include all relevant derivatives reports held by a TR pertinent to a position of a 
particular Counterparty 1 (T1F4) in the relevant position calculation. TRs should include 
derivatives irrespective of whether they are or are not reconciled, paired or matched.

## Page 3

2
TRs should calculate positions on a ‘best available information’ basis. TRs should include 
all information, as available at the date of the position calculation, conforming to common 
validation rules in the position calculation, irrespective of the reconciliation status.
TRs should calculate positions based on the information included in the latest trade state 
report, in line with the following steps:
If a TR provides an authority with access to erroneous data which is caused by a significant 
TR technical issue, then the TR should solve the issue as soon as possible and re-report 
correctly the historical data up to 2 years back in time, limited to EMIR Refit go-live date. 
When a significant misreporting mistake, caused by a reporting counterparty rather than 
the TR, has led to an incorrect calculation by a TR, all authorities should be notified, and 
given the opportunity to request an amended version of each calculation up to 2 years back 
in time, limited to EMIR Refit go-live date, that was incorrect from the relevant TR.
TRs should maintain a record of all the position calculations which they have calculated for 
at least two years.
Event Day/time
1 End of trading day T Day T 
2 Retrieve appropriate FX reference rates on day T for converting, where 
applicable, the required fields as per Guideline (14).
Day T 16:00 UTC 
(17:00 CET)
3 Deadline for reporting entities to submit reports to TRs on derivatives traded on 
day T with event date T.
Day T+1 23:59 
UTC
4 Deadline for providing the trade state report by TRs based on lifecycle events 
reported up to T+1 with event date T or earlier.
Day T+2 12:00 
UTC
5 Deadline for providing the position report by TRs based on the trade state 
report provided on T+2 based on event date T or earlier.
Day T+2 23:59 
UTC

## Page 4

3
TRs which receive data in line with the portability Guidelines (ESMA70-151-552)1 should 
keep the previously calculated positions transferred from the old TR for at least two years
and follow Guideline 9 prospectively.
For derivatives that have missing data for one or more of the metrics or dimensions, TRs 
should include the derivatives with those missing values in a separate position. However, 
TRs should exclude derivatives from all relevant calculations only when there is missing 
data for field ‘Counterparty 1’ (T1F4 / T3F4), ‘Counterparty 2’ (T1F9 / T3F6), ‘Contract type’ 
(T2F10) or ‘Asset class’ (T2F11).
A TR should have in place a robust procedure to identify abnormal values, i.e., outliers, 
relating to the derivatives it receives from counterparties. For a given position, a TR should 
calculate positions according to the metrics which exclude reports with outliers, and the 
metrics which include all reports which meet the dimensions for each calculation.
TRs should provide access to positions to the relevant authorities by using an ISO 20022 
XML template and following the operational standards defined in Articles 4 and 5 of the 
RTS on data access2
.
If at least one of the below value fields is reported with a different currency, TRs should 
convert them all to EUR using the relevant FX rate published on the ECB website on the 
reference date. If the required rate is not published, then an appropriate alternative 
reference rate should be used by TRs.
a) Valuation amount (T2F21)
b) Initial margin posted by the counterparty 1 (pre-haircut) (T3F12)
c) Initial margin posted by the counterparty 1 (post-haircut) (T3F13)
d) Variation margin posted by the counterparty 1 (pre-haircut) (T3F15)
e) Variation margin posted by the counterparty 1 (post-haircut) (T3F16)
f) Excess collateral posted by the counterparty 1 (T3F18)
g) Initial margin collected by the counterparty 1 (pre-haircut) (T3F20)
h) Initial margin collected by the counterparty 1 (post-haircut) (T3F21)
1 https://www.esma.europa.eu/document/guidelines-transfer-data-between-trade-repositories 2 Commission Delegated Regulation (EU) No 2022/1856 of 10 June 2022 amending the regulatory technical standards laid down 
in Delegated Regulation (EU) No 151/2013 by further specifying the procedure for accessing details of derivatives as well as the 
technical and operational arrangements for their access.

## Page 5

4
i) Variation margin collected by the counterparty 1 (pre-haircut) (T3F23)
j) Variation margin collected by the counterparty 1 (post-haircut) (T3F24)
k) Excess collateral collected by the counterparty 1 (T3F26)
Fields ‘Notional amount of leg 1 (T2F55) and ‘Notional amount of leg 2 (T2F64) should 
never be converted.
Upon request from ESMA, a TR should always have available the calculation algorithms 
they use as well as the procedure(s) which they follow to produce each of the four datasets 
relating to the position calculations described in these Guidelines.
Figures included in calculations should not be rounded but the calculated position should 
be rounded to minimum 2 digits after decimal.
For the purpose of calculating the positions, TRs should determine if a transaction refers 
to a ‘buyer’ or a ‘seller’ by applying the following logic:
a) The ‘Buyer’ should be determined when either ‘Direction’ = ‘BYER’ is populated or 
when ‘TAKE’ and ‘MAKE’ are populated in ‘Direction of leg 1’ and ‘Direction of leg 
2’, respectively. 
b) The ‘Seller’ should be determined when either ‘Direction’ = ‘SLLR’ is populated or 
when ‘MAKE’ and ‘TAKE’ are populated in ‘Direction of leg 1’ and ‘Direction of leg 
2’, respectively.
The reporting of the direction of derivatives with two legs should be done by parties taking 
into account their own booking irrespective of the other party booking3
. Consequently, the 
direction and the order of currencies or interest rates involved may vary in the reporting of
derivatives with two legs. To avoid double counting, TRs should in such cases use an 
alphabetical order logic to determine the direction and the order of currencies or interest 
rates indicators/names used for derivatives with two legs. For example, an FX swap with 
USD/EUR would translate to Leg 1 = EUR and Leg 2 = USD) for the purpose of calculating 
the positions. In this example, the counterparty reporting itself as a buyer (TAKE) for the 
leg involving EUR (which would translate to leg 1) would be considered the buyer.
TRs should calculate and quantify positions by aggregating according to the following 
quantitative metrics. When the position does not include outliers, it should be referred to 
as ‘clean’, when it does include outliers, it should be referred to as ‘total’.
3 See EMIR Refit Guideline 432

## Page 6

5
Total and clean number of derivatives/trades
a) Number of derivatives used for calculating the Buyer-Side position: This refers 
to the number of trades contained in the position set for which the Counterparty 1 
(T1F4) has either reported ‘BYER’ in the field Direction (T1F17), or has reported 
‘TAKE’ and ‘MAKE’ in the fields Direction of leg 1 (T1F18) and Direction of leg 2 
(T1F19), respectively;
b) Number of trades used for calculating the Seller-Side position: This refers to 
the number of trades contained in the position set for which the Counterparty 1 
(T1F4) has either reported ‘SLLR’ in the field Direction (T1F17), or has reported 
‘MAKE’ and ‘TAKE’ in the fields Direction of leg 1 (T1F18) and Direction of leg 2 
(T1F19), respectively;
Total and clean notional amounts
c) Buyer-Side Notional amount of leg 1: Aggregations of values in the field Notional 
of leg 1 (T2F55) for all derivatives pertaining to a position set for which the 
Counterparty 1 (T1F4) has either reported ‘BYER’ in the field Direction (T1F17) or
has reported ‘TAKE’ and ‘MAKE’ in the fields Direction of leg 1 (T1F18) and 
Direction of leg 2 (T1F19), respectively. The notional amount should be expressed 
in terms of amount and in the reported Notional Currency 1 (T2F56);
d) Buyer-Side Notional amount of leg 2: Aggregations of values in the field Notional 
of leg 2 (T2F64) for all derivatives pertaining to a position set for which the 
Counterparty 1 (T1F4) has either reported ‘BYER’ in the field Direction (T1F17) or
has reported ‘TAKE’ and ‘MAKE’ in the fields Direction of leg 1 (T1F18) and 
Direction of leg 2 (T1F19), respectively. The notional amount should be expressed 
in terms of amount and in the reported Notional Currency 2 (T2F65);
e) Seller-Side Notional amount of leg 1: Aggregations of values in the field Notional 
of leg 1 (T2F55) for all derivatives pertaining to a position set for which the 
Counterparty 1 (T1F4) has either reported ‘SLLR’ in the field Direction (T1F17) or
has reported ‘MAKE’ and ‘TAKE’ in the fields Direction of leg 1 (T1F18) and 
Direction of leg 2 (T1F19), respectively. The notional amount should be expressed 
in terms of amount and in the reported Notional Currency 1 (T2F56);
f) Seller-Side Notional amount of leg 2: Aggregations of values in the field Notional 
of leg 2 (T2F64) for all derivatives pertaining to a position set for which the 
Counterparty 1 (T1F4) has either reported ‘SLLR’ in the field Direction (T1F17) or
has reported ‘MAKE’ and ‘TAKE’ in the fields Direction of leg 1 (T1F18) and 
Direction of leg 2 (T1F19), respectively. The notional amount should be expressed 
in terms of amount and in the reported Notional Currency 2 (T2F65);

## Page 7

6
g) When Asset Class (T2F11) is ‘CRDT’, then the notional amount metric (Guideline 
19(c), (d), (e) or (f)) should be multiplied by the Index Factor (T2F147) only when 
the index factor value is larger than zero;
Total and clean notional amounts in effect
h) Buyer-Side Notional amount in effect of leg 1: Aggregations of values in the field 
Notional amount in effect on associated effective date of leg 1 (T2F59) for all 
derivatives pertaining to a position set for which the Counterparty 1 (T1F4) has 
either reported ‘BYER’ in the field Direction (T1F17) or has reported ‘TAKE’ and 
‘MAKE’ in the fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), 
respectively. The notional amount should be expressed in terms of amount and in 
the reported Notional Currency 1 (T2F56);
i) Buyer-Side Notional amount in effect of leg 2: Aggregations of values in the field 
Notional amount in effect on associated effective date of leg 2 (T2F68) for all 
derivatives pertaining to a position set for which the Counterparty 1 (T1F4) has 
either reported ‘BYER’ in the field Direction (T1F17) or has reported ‘TAKE’ and 
‘MAKE’ in the fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), 
respectively. The notional amount should be expressed in terms of amount and in 
the reported Notional Currency 2 (T2F65);
j) Seller-Side Notional amount in effect of leg 1: Aggregations of values in the field 
Notional amount in effect on associated effective date of leg 1 (T2F59) for all 
derivatives pertaining to a position set for which the Counterparty 1 (T1F4) has 
either reported ‘SLLR’ in the field Direction (T1F17) or has reported ‘MAKE’ and 
‘TAKE’ in the fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), 
respectively. The notional amount should be expressed in terms of amount and in 
the reported Notional Currency 1 (T2F56);
k) Seller-Side Notional amount in effect of leg 2: Aggregations of values in the field 
Notional amount in effect on associated effective date of leg 2 (T2F68) for all 
derivatives pertaining to a position set for which the Counterparty 1 (T1F4) has 
either reported ‘SLLR’ in the field Direction (T1F17) or has reported ‘MAKE’ and 
‘TAKE’ in the fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), 
respectively. The notional amount should be expressed in terms of amount and in 
the reported Notional Currency 2 (T2F65);
l) When Asset Class (T2F11) is ‘CRDT’, then the notional amount metric (Guideline 
19(h), (i), (j) or (k)) should be multiplied by the Index Factor (T2F147) only when 
the index factor value is larger than zero;
Total and clean valuation amounts

## Page 8

7
m) Buyer-Side Negative Valuation Amount: aggregations of all negative values in 
field Valuation amount (T2F21) for all derivatives pertaining to a position set for 
which the Counterparty 1 (T1F4) has either reported ‘BYER’ in the field Direction 
(T1F17) or has reported ‘TAKE’ and ‘MAKE’ in the fields Direction of leg 1 (T1F18) 
and Direction of leg 2 (T1F19), respectively. The negative value should be 
expressed in terms of amount and in the reported Valuation currency (T2F22), 
unless it has been subject to conversion as per Guideline 14;
n) Buyer-Side Positive Valuation Amount: aggregations of all positive values in field 
Valuation amount (T2F21) for all derivatives pertaining to a position set for which 
the Counterparty 1 (T1F4) has either reported ‘BYER’ in the field Direction (T1F17) 
or has reported ‘TAKE’ and ‘MAKE’ in the fields Direction of leg 1 (T1F18) and 
Direction of leg 2 (T1F19), respectively. The positive value should be expressed in 
terms of amount and in the reported Valuation currency (T2F22), unless it has been 
subject to conversion as per Guideline 14;
o) Seller-Side Negative Valuation Amount: aggregations of all negative values in 
field Valuation amount (T2F21) for all derivatives pertaining to a position set for 
which the Counterparty 1 (T1F4) has either reported ‘SLLR’ in the field Direction 
(T1F17) or has reported ‘MAKE’ and ‘TAKE’ in the fields Direction of leg 1 (T1F18) 
and Direction of leg 2 (T1F19), respectively. The negative value should be 
expressed in terms of amount and in the reported Valuation currency (T2F22), 
unless it has been subject to conversion as per Guideline 14;
p) Seller-Side Positive Valuation Amount: aggregations of all positive values in field 
Valuation amount (T2F21) for all derivatives pertaining to a position set for which 
the Counterparty 1 (T1F4) has either reported ‘SLLR’ in the field Direction (T1F17) 
or has reported ‘MAKE’ and ‘TAKE’ in the fields Direction of leg 1 (T1F18) and 
Direction of leg 2 (T1F19), respectively. The positive value should be expressed in 
terms of amount and in the reported Valuation currency (T2F22), unless it has been 
subject to conversion as per Guideline 14;
Total and clean delta position
q) Net Buyer-Side Notional Amount of leg 1 Weighted Average Delta Position:
This refers to the following computation and aggregation ‘sum (delta * notional 
amount of leg 1) / sum (notional amount of leg 1)’ based on fields Delta (T2F25)
and Notional amount of leg 1 (T2F55) for all derivatives pertaining to a position 
based on the following conditions: (i) Counterparty 1 (T1F4) has either reported 
‘BYER’ in the field Direction (T1F17), or has reported ‘TAKE’ and ‘MAKE’ in the 
fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), respectively; (ii) 
Delta (T2F25) and Notional amount of leg 1 (T2F55) are not blank, and; (iii) Contract

## Page 9

8
type (T2F10) is populated with 'OPTN' or 'SWPT' and Underlying identification type 
(T2F13) is not populated with 'B';
r) Net Buyer-Side Notional Amount of leg 2 Weighted Average Delta Position: 
This refers to the following computation and aggregation ‘sum (delta * notional 
amount of leg 2) / sum (notional amount of leg 2)’ based on fields Delta (T2F25) 
and Notional amount of leg 2 (T2F64) for all derivatives pertaining to a position 
based on the following conditions: (i) Counterparty 1 (T1F4) has either reported 
‘BYER’ in the field Direction (T1F17), or has reported ‘TAKE’ and ‘MAKE’ in the 
fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), respectively; (ii) 
Delta (T2F25) and Notional amount of leg 2 (T2F64) are not blank, and; (iii) Contract 
type (T2F10) is populated with 'OPTN' or 'SWPT' and Underlying identification type 
(T2F13) is not populated with 'B';
s) Net Seller-Side Notional Amount of leg 1 Weighted Average Delta Position: 
This refers to the following computation and aggregation ‘sum (delta * notional 
amount of leg 1) / sum (notional amount of leg 1)’ based on fields Delta (T2F25) 
and Notional amount of leg 1 (T2F55) for all derivatives pertaining to a position 
based on the following conditions: (i) Counterparty 1 (T1F4) has either reported 
‘SLLR’ in the field Direction (T1F17), or has reported ‘MAKE’ and ‘TAKE’ in the 
fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), respectively; (ii) 
Delta (T2F25) and Notional amount of leg 1 (T2F55) are not blank, and; (iii) Contract 
type (T2F10) is populated with 'OPTN' or 'SWPT' and Underlying identification type 
(T2F13) is not populated with 'B';
t) Net Seller-Side Notional Amount of leg 2 Weighted Average Delta Position: 
This refers to the following computation and aggregation ‘sum (delta * notional 
amount of leg 2) / sum (notional amount of leg 2)’ based on fields Delta (T2F25) 
and Notional amount of leg 2 (T2F64) for all derivatives pertaining to a position 
based on the following conditions: (i) Counterparty 1 (T1F4) has either reported 
‘SLLR’ in the field Direction (T1F17), or has reported ‘MAKE’ and ‘TAKE’ in the 
fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), respectively; (ii) 
Delta (T2F25) and Notional amount of leg 2 (T2F64) are not blank, and; (iii) Contract 
type (T2F10) is populated with 'OPTN' or 'SWPT' and Underlying identification type 
(T2F13) is not populated with 'B';
Total and clean other payment amount
u) Buyer-Side Upfront payment (payer): Aggregation of upfront payment values in 
field ‘Other payment amount’ (T2F74) for all derivatives pertaining to a position 
based on the following conditions: (i) Counterparty 1 (T1F4) has either reported 
‘BYER’ in the field Direction (T1F17), or has reported ‘TAKE’ and ‘MAKE’ in the 
fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), respectively; (ii)

## Page 10

9
Other payment type (T2F73) is populated with ‘UFRO’; and (iii) Other payment 
payer (T2F77) is the same as Counterparty 1 (T1F4). The upfront payment amount 
should be expressed in terms of amount and in the reported ‘Other payment 
currency’ (T2F75).
v) Buyer-Side Upfront payment (receiver): Aggregation of upfront payment values 
in field ‘Other payment amount’ (T2F74) for all derivatives pertaining to a position 
based on the following conditions: (i) Counterparty 1 (T1F4) has either reported 
‘BYER’ in the field Direction (T1F17), or has reported ‘TAKE’ and ‘MAKE’ in the 
fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), respectively; (ii) 
Other payment type (T2F73) was populated with ‘UFRO’; and (iii) Other payment 
receiver (T2F78) is the same as Counterparty 1 (T1F4). The upfront payment 
amount should be expressed in terms of amount and in the reported ‘Other payment 
currency’ (T2F75).
w) Seller-Side Upfront payment (payer): Aggregation of upfront payment values in 
field ‘Other payment amount’ (T2F74) for all derivatives pertaining to a position 
based on the following conditions: (i) Counterparty 1 (T1F4) has either reported 
‘SLLR’ in the field Direction (T1F17), or has reported ‘MAKE’ and ‘TAKE’ in the 
fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), respectively; (ii) 
Other payment type (T2F73) was populated with ‘UFRO’; and (iii) Other payment 
payer (T2F77) is the same as Counterparty 1 (T1F4). The upfront payment amount 
should be expressed in terms of amount and in the reported ‘Other payment 
currency’ (T2F75).
x) Seller-Side Upfront payment (receiver): Aggregation of upfront payment values 
in field ‘Other payment amount’ (T2F74) for all derivatives pertaining to a position 
based on the following conditions: (i) Counterparty 1 (T1F4) has either reported 
‘SLLR’ in the field Direction (T1F17), or has reported ‘MAKE’ and ‘TAKE’ in the 
fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), respectively; (ii) 
Other payment type (T2F73) was populated with ‘UFRO’; and (iii) Other payment 
receiver (T2F78) is the same as Counterparty 1 (T1F4). The upfront payment 
amount should be expressed in terms of amount and in the reported ‘Other payment 
currency’ (T2F75).
y) Buyer-Side Unwind or Full termination (payer): Aggregation of unwind or full 
termination values in field ‘Other payment amount’ (T2F74) for all derivatives 
pertaining to a position set based on the following conditions: (i) Counterparty 1 
(T1F4) has either reported ‘BYER’ in the field Direction (T1F17), or has reported 
‘TAKE’ and ‘MAKE’ in the fields Direction of leg 1 (T1F18) and Direction of leg 2 
(T1F19), respectively; (ii) Other payment type (T2F73) was populated with ‘UWIN’; 
and (iii) Other payment payer (T2F77) is the same as Counterparty 1 (T1F4). The

## Page 11

10
unwind or full termination amount should be expressed in terms of amount and in 
the reported ‘Other payment currency’ (T2F75).
z) Buyer-Side Unwind or Full termination (receiver): Aggregation of unwind or full 
termination values in field ‘Other payment amount’ (T2F74) for all derivatives 
pertaining to a position set based on the following conditions: (i) Counterparty 1 
(T1F4) has either reported ‘BYER’ in the field Direction (T1F17), or has reported 
‘TAKE’ and ‘MAKE’ in the fields Direction of leg 1 (T1F18) and Direction of leg 2 
(T1F19), respectively; (ii) Other payment type (T2F73) was populated with ‘UWIN’; 
and (iii) Other payment receiver (T2F78) is the same as Counterparty 1 (T1F4). The 
unwind or full termination amount should be expressed in terms of amount and in 
the reported ‘Other payment currency’ (T2F75).
aa) Seller-Side Unwind or Full termination (payer): Aggregation of unwind or full 
termination values in field ‘Other payment amount’ (T2F74) for all derivatives 
pertaining to a position set based on the following conditions: (i) Counterparty 1 
(T1F4) has either reported ‘SLLR’ in the field Direction (T1F17), or has reported 
‘MAKE’ and ‘TAKE’ in the fields Direction of leg 1 (T1F18) and Direction of leg 2 
(T1F19), respectively; (ii) Other payment type (T2F73) was populated with ‘UWIN’; 
and (iii) Other payment payer (T2F77) is the same as Counterparty 1 (T1F4). The 
unwind or full termination amount should be expressed in terms of amount and in 
the reported ‘Other payment currency’ (T2F75).
bb) Seller-Side Unwind or Full termination (receiver): Aggregation of unwind or full 
termination values in field ‘Other payment amount’ (T2F74) for all derivatives 
pertaining to a position set based on the following conditions: (i) Counterparty 1 
(T1F4) has either reported ‘SLLR’ in the field Direction (T1F17), or has reported 
‘MAKE’ and ‘TAKE’ in the fields Direction of leg 1 (T1F18) and Direction of leg 2 
(T1F19), respectively; (ii) Other payment type (T2F73) was populated with ‘UWIN’; 
and (iii) Other payment receiver (T2F78) is the same as Counterparty 1 (T1F4). The 
unwind or full termination amount should be expressed in terms of amount and in 
the reported ‘Other payment currency’ (T2F75).
cc) Buyer-Side Principal exchange (payer): Aggregation of principal exchange 
values in field ‘Other payment amount’ (T2F74) for all derivatives pertaining to a 
position set based on the following conditions: (i) Counterparty 1 (T1F4) has either 
reported ‘BYER’ in the field Direction (T1F17), or has reported ‘TAKE’ and ‘MAKE’ 
in the fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), respectively;
(ii) Other payment type (T2F73) was populated with ‘PEXH’; and (iii) Other payment 
payer (T2F77) is the same as Counterparty 1 (T1F4). The principal exchange 
amount should be expressed in terms of amount and in the reported ‘Other payment 
currency’ (T2F75).

## Page 12

11
dd) Buyer-Side Principal exchange (receiver): Aggregation of principal exchange 
values in field ‘Other payment amount’ (T2F74) for all derivatives pertaining to a 
position set based on the following conditions: (i) Counterparty 1 (T1F4) has either 
reported ‘BYER’ in the field Direction (T1F17), or has reported ‘TAKE’ and ‘MAKE’ 
in the fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), respectively;
(ii) Other payment type (T2F73) was populated with ‘PEXH’; and (iii) Other payment 
receiver (T2F78) is the same as Counterparty 1 (T1F4). The principal exchange 
amount should be expressed in terms of amount and in the reported ‘Other payment 
currency’ (T2F75).
ee) Seller-Side Principal exchange (payer): Aggregation of principal exchange 
values in field ‘Other payment amount’ (T2F74) for all derivatives pertaining to a 
position set based on the following conditions: (i) Counterparty 1 (T1F4) has either 
reported ‘SLLR’ in the field Direction (T1F17), or has reported ‘MAKE’ and ‘TAKE’ 
in the fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), respectively;
(ii) Other payment type (T2F73) was populated with ‘PEXH’; and (iii) Other payment 
payer (T2F77) is the same as Counterparty 1 (T1F4). The principal exchange 
amount should be expressed in terms of amount and in the reported ‘Other payment 
currency’ (T2F75).
ff) Seller-Side Principal exchange (receiver): Aggregation of principal exchange 
values in field ‘Other payment amount’ (T2F74) for all derivatives pertaining to a 
position set based on the following conditions: (i) Counterparty 1 (T1F4) has either 
reported ‘SLLR’ in the field Direction (T1F17), or has reported ‘MAKE’ and ‘TAKE’ 
in the fields Direction of leg 1 (T1F18) and Direction of leg 2 (T1F19), respectively;
(i) Other payment type (T2F73) was populated with ‘PEXH’; and (iii) Other payment 
receiver (T2F78) is the same as Counterparty 1 (T1F4). The principal exchange 
amount should be expressed in terms of amount and in the reported ‘Other payment 
currency’ (T2F75).
TRs should use the metrics listed in Guideline 19 to aggregate currency positions which 
should be made available to the central bank issuing that currency.
The following metrics should be used to quantify all Collateral Position Sets and Currency 
Collateral Position Sets. When outliers are removed from the position the calculation
should be referred to as ‘clean’, if outliers are included the position should be referred to 
as ‘total’:
a) Number of reports used for calculating the Set;
b) Initial margin posted by the counterparty 1 (pre-haircut) (T3F12);
c) Initial margin posted by the counterparty 1 (post-haircut) (T3F13);

## Page 13

12
d) Variation margin posted by the counterparty 1 (pre-haircut) (T3F15);
e) Variation margin posted by the counterparty 1 (post-haircut) (T3F16);
f) Initial margin collected by the counterparty 1 (pre-haircut) (T3F20);
g) Initial margin collected by the counterparty 1 (post-haircut) (T3F21);
h) Variation margin collected by the counterparty 1 (pre-haircut) (T3F23)
i) Total variation margin collected by the counterparty 1 (post-haircut) (T3F24);
j) Excess collateral posted by the counterparty 1 (T3F18);
k) Excess collateral collected by the counterparty 1 (T3F26).
When collateralisation is performed on a portfolio basis and derivatives share a collateral 
portfolio code (T3F9), TRs should use the collateral values listed in Guideline 21 across 
the derivatives which share the same code, as the value of that collateral portfolio for the 
purpose of the Collateral Position Set.
When collateralisation is not performed on a portfolio basis, the variables that represent 
the value of the collateral only apply to an individual derivative and so where possible TRs 
should provide an aggregation of those collateral positions based on the Metrics listed in 
Guideline 21.
All derivatives reported to TRs should be aggregated with derivatives with identical entries 
in the following fields representing dimensions of the derivatives grouped together in 
position sets to specify counterparties to derivatives:
a) Counterparty 1 (T1F4) 
b) Counterparty 2 (T1F9); 
c) Valuation currency (T2F22);
d) Collateralisation category (T3F11);
e) Collateral Portfolio code (T2F27 / T3F9) if applicable;
f) Contract type (T2F10);
g) Asset class (T2F11);
h) Underlying identification type (T2F13) if applicable;

## Page 14

13
i) Underlying identification (T2F14) if applicable;
j) Notional Currency 1 (T2F56);
k) Notional Currency 2 (T2F65) if applicable;
l) Settlement currency 1 (T2F19)
m) Settlement currency 2 (T2F20) if applicable;
n) Master Agreement Type (T2F34);
o) Master Agreement Version (T2F36);
p) Cleared (T2F31);
q) Intragroup (T2F37)
r) Exchange Rate basis (T2F115) when applicable;
s) Option type (T2F132), when applicable.
TRs should use the following buckets to aggregate derivatives with similar values for ‘Time 
to Maturity’. Time to Maturity should be calculated as the difference between a derivative’s 
expiration date (T2F44) and the reference date, based on a Gregorian calendar.
Difference between ‘Expiration date’ (T2F44) and reference date Value of Time to maturity
One month or less ‘T01_00M_01M’
More than one month but no more than three months (inclusive) ‘T02_01M_03M’
More than three months but less than six months (inclusive) ‘T03_03M_06M’
More than six months but less than nine months (inclusive) ‘T04_06M_09M’
More than nine months but less than 12 months (inclusive) ‘T05_09M_12M’
More than twelve months but less than 2 years (inclusive) ‘T06_01Y_02Y’
More than 24 months but less than 3 years (inclusive) ‘T07_02Y_03Y’

## Page 15

14
More than 36 months but less than 4 years (inclusive) ‘T08_03Y_04Y’
More than 48 months but less than 5 years (inclusive) ‘T09_04Y_05Y’
More than 5 years but less than 10 years (inclusive) ‘T10_05Y_10Y’
More than 10 years but less than 15 years (inclusive) ‘T11_10Y_15Y’
More than 15 years but less than 20 years (inclusive) ‘T12_15Y_20Y’
More than 20 years but less than 30 years (inclusive) ‘T13_20Y_30Y’
More than 30 years but less than 50 years (inclusive) ‘T14_30Y_50Y’
More than 50 years ‘T15_50Y_XXY’
Expiration date is blank (open ended contract) ‘T16_BL’
Expiration date is NA ‘T17_NA’
In the event that a derivative has an expiration date (T2F44) which does not exist in the 
month of the reference date (i.e. 29, 30, 31 month dependent), the decision for which 
maturity bucket that derivative should be included in, should be made by treating that 
derivative in the same way as if the calculation were being made on the expiration date 
(T2F44) for the month of the reference date. For example, if a derivative calculation has a 
reference date of 31 January and the derivative expires on 28 February, that derivative 
should be included in the ‘One month or less’ maturity bucket. If a reference date is on 31 
January and the expiration date (T2F44) is 1 March, then that derivative should be included 
in the ‘More than one month but no more than three months’ maturity bucket. If a 
calculation’s reference date is on 30 April, and the derivative matures on 31 May then that 
derivative should be included in the ‘One month or less’ maturity bucket.
IRS derivatives should also be grouped together according to their type. With reference to 
whether Leg 1 and Leg 2 are fixed or floating, the below table explains how ‘type of IRS’ 
should be discerned and how IRS derivatives should be grouped:

## Page 16

15
Fixed rate of leg 1 
or coupon 
(T2F79)
Fixed rate of leg 2 
(T2F95)
Indicator of the 
floating rate of leg 
1 (T2F84)
Indicator of the 
floating rate of leg 
2 (T2F100)
Value of variable 
Type of IRS4
P B B P FIX-FLOAT
B P P B FIX-FLOAT
P P B B FIX-FIX
B B P P BASIS
For credit derivatives, TRs should use the following dimensions to group together 
derivatives for Position Sets and Currency Position Sets in addition to those dimensions 
referred to from Guideline 24 to Guideline 26:
a) Seniority (T2F143) when reference entity is populated in field Reference entity 
(T2F144);
b) Tranche (T2F148) when ‘X’ is populated in field Underlying identification type 
(T2F13).
For commodity derivatives, a TR should aggregate metrics for classes of commodity 
derivatives in accordance with the dimensions referred to in Guideline 24 to Guideline 26
of this paper as per each of the following details reported in field Base product (T2F116), 
Sub-product (T2F117), and field Further sub-product (T2F118) as defined in Table 4 
‘Classification of commodities’ of the ITS on reporting5
.
TRs should use the below dimensions to group together derivatives using the same 
collateral as a Collateral Position Set:
4 When Fixed rate of leg 1 or coupon (T2F79) is populated and Indicator of the floating rate of leg 2 (T2F100) is populated with 
value “EURI”, the variable Type of IRS should be populated with “FIX-EURI”. When floating legs are not populated, but Fixed rate
of leg 1 or coupon (T2F79) and Fixed rate of leg 2 (T2F95) are, then the variable Type of IRS should be populated with “FIX-FIX”. 
When fixed legs are not populated but Indicator of the Floating rate of leg 1 (T2F84) the value “LIBO” is provided and in the
Indicator of the Floating rate of leg 2 (T2F100) the value “EURI” is provided, the variable Type of IRS will be populated with the 
value “EURI_LIBO”.
5 Commission Implementing Regulation (EU) No 2022/1860 of 10 June 2022 laying down implementing technical standards for 
the application of Regulation (EU) No 648/2012 of the European Parliament and of the Council on OTC derivatives, central 
counterparties and trade repositories, with regard to the standards, formats, frequency and methods and arrangements for
reporting and repealing Implementing Regulation (EU) No 1247/2012.

## Page 17

16
a) Counterparty 1 (T1F4 / T3F4);
b) Counterparty 2 (T1F9 / T3F6);
c) Collateralisation category (T3F11);
d) Collateral portfolio indicator (T3F8);
e) Currency of the initial margin posted (T3F14);
f) Currency of the variation margin posted (T3F17);
g) Currency of the initial margin collected (T3F22);
h) Currency of variation margin collected (T3F25);
i) Currency of the excess collateral posted (T3F19), if applicable;
j) Currency of excess collateral collected (T3F27), if applicable.
TRs should determine the relevant Currency Position Sets for authorities where the 
counterparties have reported the currency of issue of that authority for one of the below 
dimensions.
a) Notional Currency 1 (T2F56); or
b) Notional Currency 2 (T2F65); or
c) Settlement currency 1 (T2F19); or
d) Settlement currency 2 (T2F20).
TRs should provide a Currency Position Set to authorities determined in accordance with 
Guideline 31 and based upon all the dimensions included from Guideline 24 through to 
Guideline 26. Guideline 27, Guideline 28, and Guideline 29 should also be applied to 
Currency Position Sets when appropriate.
TRs should aggregate the collateral pertaining to the Currency Position Sets determined 
in accordance with Guideline 31 and using the dimensions referred to in Guideline 30.

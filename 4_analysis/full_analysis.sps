* Encoding: UTF-8.
* Knowledge, Attitudes, and Practices Toward Non-Communicable Diseases
* Among Medical Students at the University of Gezira, Sudan, 2026
* Sample: n = 184
*
* NOTE: Update the FILE path below before running.

GET DATA
  /TYPE = XLSX
  /FILE = 'C:\path\to\1_data\cleaned\cleaned_data.xlsx'
  /SHEET = NAME 'Sheet1'
  /CELLRANGE = FULL
  /READNAMES = ON
  /DATATYPEMIN PERCENTAGE = 95.0.
EXECUTE.


VARIABLE LABELS
  ID        'Participant ID'
  Age       'Age Group'
  Gender    'Gender'
  AcadYr    'Academic Year'
  Resid     'Residence'
  Marital   'Marital Status'
  FamHist   'Family History of NCDs'
  Src_Med   'Info Source: Medical Curriculum'
  Src_SM    'Info Source: Social Media'
  Src_Net   'Info Source: Internet'
  Src_TV    'Info Source: Television or Radio'
  Src_Fam   'Info Source: Family or Friends'
  Src_Wkshp 'Info Source: Workshops or Seminars'
  K01  'K1: Hypertension = persistent BP elevation'
  K02  'K2: Obesity increases hypertension risk'
  K03  'K3: Hypertension can be asymptomatic'
  K04  'K4: Exercise helps prevent hypertension'
  K05  'K5: Diabetes characterised by high blood sugar'
  K06  'K6: Physical inactivity is DM risk factor'
  K07  'K7: Diabetes can affect the kidneys'
  K08  'K8: Healthy diet helps prevent diabetes'
  K09  'K9: Smoking increases heart disease risk'
  K10  'K10: High cholesterol contributes to CVD'
  K11  'K11: Stress may increase heart disease risk'
  K12  'K12: Cardiovascular diseases can be prevented'
  K13  'K13: Smoking is major cause of chronic lung disease'
  K14  'K14: Asthma is a chronic respiratory disease'
  K15  'K15: Air pollution worsens respiratory diseases'
  K16  'K16: CRD can occur in all age groups'
  A01  'A1: NCD prevention should be in medical education'
  A02  'A2: Students should join community NCD campaigns'
  A03  'A3: Lifestyle modification prevents NCDs'
  A04  'A4: BP and DM screening should be routine'
  A05  'A5: Physicians have role in smoking cessation'
  A06  'A6: Chronic diseases burden Sudanese healthcare'
  A07  'A7: Confident educating patients about NCD prevention'
  A08  'A8: Early diagnosis of NCDs improves outcomes'
  P01  'P1: Exercise regularly'
  P02  'P2: Check blood pressure regularly'
  P03  'P3: Monitor blood sugar periodically'
  P04  'P4: Avoid cigarettes and tobacco'
  P05  'P5: Consume fruits and vegetables regularly'
  P06  'P6: Avoid excessive salty and fatty foods'
  P07  'P7: Participated in NCD awareness activities'
  P08  'P8: Seek medical advice for chronic symptoms'
  K_Score 'Knowledge Total Score (0-16)'
  K_Cat   'Knowledge Category (3-level)'
  K_Cat2  'Knowledge Category (Binary: Good vs Poor/Fair)'
  A_Score 'Attitude Total Score (8-40)'
  A_Cat   'Attitude Category (3-level)'
  A_Cat2  'Attitude Category (Binary: Positive vs Neg./Neutral)'
  P_Score 'Practice Total Score (0-8)'
  P_Cat   'Practice Category'
  P_High  'Adequate Practice (Binary: High vs Low/Moderate)'.
EXECUTE.


VALUE LABELS Age
  1 '<20 years'
  2 '20-24 years'
  3 '25-29 years'.

VALUE LABELS Gender
  1 'Male'
  2 'Female'.

VALUE LABELS AcadYr
  1 'First Year'
  2 'Second Year'
  3 'Third Year'
  4 'Fourth Year'
  5 'Fifth Year'
  6 'Sixth Year'.

VALUE LABELS Resid
  1 'Urban'
  2 'Rural'.

VALUE LABELS Marital
  1 'Single'
  2 'Married'
  3 'Divorced'
  4 'Widowed'.

VALUE LABELS FamHist
  1 'Yes'
  2 'No'
  3 "Don't Know".

VALUE LABELS
  Src_Med Src_SM Src_Net Src_TV Src_Fam Src_Wkshp
  0 'Not Selected'
  1 'Selected'.

VALUE LABELS
  K01 K02 K03 K04 K05 K06 K07 K08
  K09 K10 K11 K12 K13 K14 K15 K16
  0 'Incorrect'
  1 'Correct'.

VALUE LABELS
  A01 A02 A03 A04 A05 A06 A07 A08
  1 'Strongly Disagree'
  2 'Disagree'
  3 'Neutral'
  4 'Agree'
  5 'Strongly Agree'.

VALUE LABELS
  P01 P02 P03 P04 P05 P06 P07 P08
  0 'No'
  1 'Yes'.

VALUE LABELS K_Cat
  1 'Poor (0-8)'
  2 'Fair (9-12)'
  3 'Good (13-16)'.

VALUE LABELS K_Cat2
  0 'Poor/Fair (0-12)'
  1 'Good (13-16)'.

VALUE LABELS A_Cat
  1 'Negative (8-18)'
  2 'Neutral (19-29)'
  3 'Positive (30-40)'.

VALUE LABELS A_Cat2
  0 'Negative/Neutral (8-29)'
  1 'Positive (30-40)'.

VALUE LABELS P_Cat
  1 'Low (0-2)'
  2 'Moderate (3-5)'
  3 'High (6-8)'.

VALUE LABELS P_High
  0 'Low/Moderate Practice'
  1 'High Practice'.

EXECUTE.


VARIABLE LEVEL
  Gender Resid Marital FamHist K_Cat K_Cat2 A_Cat A_Cat2 P_Cat P_High
  Src_Med Src_SM Src_Net Src_TV Src_Fam Src_Wkshp
  K01 K02 K03 K04 K05 K06 K07 K08
  K09 K10 K11 K12 K13 K14 K15 K16
  P01 P02 P03 P04 P05 P06 P07 P08
  (NOMINAL).

VARIABLE LEVEL
  Age AcadYr
  (ORDINAL).

VARIABLE LEVEL
  K_Score A_Score P_Score
  (SCALE).

EXECUTE.


FREQUENCIES VARIABLES = Age Gender AcadYr Resid Marital FamHist
  /ORDER = ANALYSIS.

FREQUENCIES VARIABLES = Src_Med Src_SM Src_Net Src_TV Src_Fam Src_Wkshp
  /ORDER = ANALYSIS.

FREQUENCIES VARIABLES = K01 K02 K03 K04 K05 K06 K07 K08
                         K09 K10 K11 K12 K13 K14 K15 K16
  /ORDER = ANALYSIS.

FREQUENCIES VARIABLES = A01 A02 A03 A04 A05 A06 A07 A08
  /ORDER = ANALYSIS.

FREQUENCIES VARIABLES = P01 P02 P03 P04 P05 P06 P07 P08
  /ORDER = ANALYSIS.

DESCRIPTIVES VARIABLES = K_Score A_Score P_Score
  /STATISTICS = MEAN STDDEV MIN MAX RANGE.

FREQUENCIES VARIABLES = K_Cat K_Cat2 A_Cat A_Cat2 P_Cat
  /BARCHART PERCENT
  /ORDER = ANALYSIS.


* Knowledge and Practice items are binary (0/1); RELIABILITY with MODEL=ALPHA
* on binary items yields the KR-20 equivalent.
RELIABILITY
  /VARIABLES = K01 K02 K03 K04 K05 K06 K07 K08
               K09 K10 K11 K12 K13 K14 K15 K16
  /SCALE ('Knowledge Scale KR-20') ALL
  /MODEL = ALPHA
  /STATISTICS = DESCRIPTIVE SCALE
  /SUMMARY = TOTAL.

RELIABILITY
  /VARIABLES = A01 A02 A03 A04 A05 A06 A07 A08
  /SCALE ('Attitude Scale Cronbach Alpha') ALL
  /MODEL = ALPHA
  /STATISTICS = DESCRIPTIVE SCALE
  /SUMMARY = TOTAL.

RELIABILITY
  /VARIABLES = P01 P02 P03 P04 P05 P06 P07 P08
  /SCALE ('Practice Scale KR-20') ALL
  /MODEL = ALPHA
  /STATISTICS = DESCRIPTIVE SCALE
  /SUMMARY = TOTAL.


* K_Cat2 and A_Cat2 (binary) are used for bivariate analysis due to severe
* ceiling effects (98.9% Good knowledge, 97.3% Positive attitude).
* AcadYr is excluded from inferential tests (97.8% third-year).

CROSSTABS
  /TABLES = Gender BY K_Cat2
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ PHI.

CROSSTABS
  /TABLES = Age BY K_Cat2
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ GAMMA.

CROSSTABS
  /TABLES = Resid BY K_Cat2
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ PHI.

CROSSTABS
  /TABLES = FamHist BY K_Cat2
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ.

CROSSTABS
  /TABLES = Marital BY K_Cat2
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ PHI.

CROSSTABS
  /TABLES = Src_Med Src_SM Src_Net Src_TV Src_Fam Src_Wkshp BY K_Cat2
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ PHI.


CROSSTABS
  /TABLES = Gender BY A_Cat2
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ PHI.

CROSSTABS
  /TABLES = Age BY A_Cat2
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ GAMMA.

CROSSTABS
  /TABLES = Resid BY A_Cat2
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ PHI.

CROSSTABS
  /TABLES = FamHist BY A_Cat2
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ.

CROSSTABS
  /TABLES = Marital BY A_Cat2
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ PHI.


CROSSTABS
  /TABLES = Gender BY P_Cat
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ PHI.

CROSSTABS
  /TABLES = Age BY P_Cat
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ GAMMA.

CROSSTABS
  /TABLES = Resid BY P_Cat
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ PHI.

CROSSTABS
  /TABLES = FamHist BY P_Cat
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ.

CROSSTABS
  /TABLES = Marital BY P_Cat
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ PHI.

CROSSTABS
  /TABLES = Src_Med Src_SM Src_Net Src_TV Src_Fam Src_Wkshp BY P_Cat
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ.


CROSSTABS
  /TABLES = K_Cat2 BY P_Cat
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ.

CROSSTABS
  /TABLES = A_Cat2 BY P_Cat
  /FORMAT = AVALUE TABLES
  /CELLS = COUNT ROW EXPECTED
  /STATISTICS = CHISQ.


T-TEST GROUPS = Gender(1 2)
  /MISSING = ANALYSIS
  /VARIABLES = K_Score A_Score P_Score
  /CRITERIA = CI(0.95).

T-TEST GROUPS = Resid(1 2)
  /MISSING = ANALYSIS
  /VARIABLES = K_Score A_Score P_Score
  /CRITERIA = CI(0.95).

ONEWAY K_Score A_Score P_Score BY FamHist
  /STATISTICS = DESCRIPTIVES HOMOGENEITY
  /MISSING = ANALYSIS
  /POSTHOC = TUKEY ALPHA(0.05).


LOGISTIC REGRESSION VARIABLES P_High
  /METHOD = ENTER Gender Age Resid FamHist K_Cat2 A_Cat2
  /CONTRAST (Gender)  = Indicator(1)
  /CONTRAST (Age)     = Indicator(1)
  /CONTRAST (Resid)   = Indicator(1)
  /CONTRAST (FamHist) = Indicator(1)
  /CONTRAST (K_Cat2)  = Indicator(0)
  /CONTRAST (A_Cat2)  = Indicator(0)
  /PRINT = GOODFIT CI(95) ITER(1) SUMMARY
  /CRITERIA = PIN(0.05) POUT(0.10) ITERATE(20) CUT(0.5).


* NOTE: Update the OUTFILE path below before running.
SAVE OUTFILE = 'C:\path\to\1_data\cleaned\NCD_KAP_Analysis_Final.sav'
  /COMPRESSED.

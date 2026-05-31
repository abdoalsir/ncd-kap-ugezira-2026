"""
Project  : Knowledge, Attitudes, and Practices Toward Non-Communicable Diseases
           Among Medical Students at the University of Gezira, Sudan – 2026
Script   : Data Cleaning & Recoding
Author   : Abdulrahman Sirelkhatim
Date     : May 2026
Input    : 1_data/raw/raw_data.xlsx  (Google Form export, bilingual Arabic/English)
Output   : 1_data/cleaned/cleaned_data.xlsx

Raw column structure (by position):
    0  : Age
    1  : Gender
    2  : Academic year
    3  : Residence
    4  : Marital status
    5  : Family history of NCDs
    6  : Main source of information (comma-separated multi-select)
    7–22 : K01–K16  (True/False knowledge items)
    23–30: A01–A08  (5-point Likert attitude items)
    31–38: P01–P08  (Yes/No practice items)

Raw cell values are bilingual, e.g. "True / صحيح", "أوافق بشدة / Strongly agree".
Matching is done on the English portion only (split on ' / ' and take index 0 or -1).
FamHist "Don't Know" appears as Arabic-only "لا أعرف" in the export.
"""

import numpy as np
import pandas as pd

RAW_PATH = "1_data/raw/raw_data.xlsx"
OUTPUT_PATH = "1_data/cleaned/cleaned_data.xlsx"

RANDOM_SEED = 42
SAMPLE_N = 184

column_map_by_position = {
    0: "Age",
    1: "Gender",
    2: "AcadYr",
    3: "Resid",
    4: "Marital",
    5: "FamHist",
    6: "SrcInfo",
    7: "K01",
    8: "K02",
    9: "K03",
    10: "K04",
    11: "K05",
    12: "K06",
    13: "K07",
    14: "K08",
    15: "K09",
    16: "K10",
    17: "K11",
    18: "K12",
    19: "K13",
    20: "K14",
    21: "K15",
    22: "K16",
    23: "A01",
    24: "A02",
    25: "A03",
    26: "A04",
    27: "A05",
    28: "A06",
    29: "A07",
    30: "A08",
    31: "P01",
    32: "P02",
    33: "P03",
    34: "P04",
    35: "P05",
    36: "P06",
    37: "P07",
    38: "P08",
}

SOURCE_OPTIONS = {
    "Src_Med": "Medical curriculum",
    "Src_SM": "Social media",
    "Src_Net": "Internet",
    "Src_TV": "Television or radio",
    "Src_Fam": "Family or friends",
    "Src_Wkshp": "Workshops or seminars",
}

K_COLS = [f"K{i:02d}" for i in range(1, 17)]
A_COLS = [f"A{i:02d}" for i in range(1, 9)]
P_COLS = [f"P{i:02d}" for i in range(1, 9)]


def english_part(val) -> str:
    """Return the English portion of a bilingual 'English / Arabic' string."""
    if not isinstance(val, str):
        return str(val)
    parts = [p.strip() for p in val.split(" / ")]
    for part in parts:
        # A part is considered 'English' when most characters are ASCII
        ascii_ratio = sum(c.isascii() for c in part) / max(len(part), 1)
        if ascii_ratio > 0.6:
            return part.lower()
    return val.lower()


def recode_knowledge(val) -> int:
    """True / صحيح → 1,  False / خطأ → 0"""
    eng = english_part(val)
    if "true" in eng:
        return 1
    if "false" in eng:
        return 0
    return np.nan


def recode_attitude(val) -> int:
    """Bilingual Likert → 1–5 numeric"""
    eng = english_part(val)
    if "strongly agree" in eng:
        return 5
    if "strongly disagree" in eng:
        return 1
    if "agree" in eng:
        return 4
    if "disagree" in eng:
        return 2
    if "neutral" in eng:
        return 3
    return np.nan


def recode_practice(val) -> int:
    """Yes / نعم → 1,  No / لا → 0"""
    eng = english_part(val)
    if "yes" in eng:
        return 1
    if "no" in eng:
        return 0
    return np.nan


def age_code(val) -> int:
    """
    '<20 years'   → 1
    '20–24 years' → 2
    '25–29 years' → 3
    """
    eng = english_part(val)
    if "<20" in eng or "under 20" in eng:
        return 1
    if "20" in eng:  # catches '20–24 years'
        return 2
    if "25" in eng:  # catches '25–29 years'
        return 3
    return np.nan


def gender_code(val) -> int:
    """Female / أنثى → 2,  Male / ذكر → 1"""
    eng = english_part(val)
    if "female" in eng:
        return 2
    if "male" in eng:
        return 1
    return np.nan


def year_code(val) -> int:
    """First → 1 … Sixth → 6"""
    eng = english_part(val)
    mapping = {
        "first": 1,
        "second": 2,
        "third": 3,
        "fourth": 4,
        "fifth": 5,
        "sixth": 6,
    }
    for word, code in mapping.items():
        if word in eng:
            return code
    return np.nan


def resid_code(val) -> int:
    """Urban / حضر → 1,  Rural / ريف → 2"""
    eng = english_part(val)
    if "urban" in eng:
        return 1
    if "rural" in eng:
        return 2
    return np.nan


def marital_code(val) -> int:
    """Single → 1,  Married → 2,  Divorced → 3,  Widowed → 4"""
    eng = english_part(val)
    if "single" in eng:
        return 1
    if "married" in eng:
        return 2
    if "divorced" in eng:
        return 3
    if "widowed" in eng:
        return 4
    return np.nan


def famhist_code(val) -> int:
    """
    'Yes / نعم'  → 1
    'No / لا'    → 2
    'لا أعرف'    → 3  (Arabic-only in the export; english_part returns the
                        full string, which contains no 'yes'/'no')
    """
    eng = english_part(val)
    if "yes" in eng:
        return 1
    if "no" in eng:
        return 2
    # Arabic-only "لا أعرف" falls here
    return 3


def k_category(score) -> int:
    if pd.isna(score):
        return pd.NA
    if score <= 8:
        return 1
    if score <= 12:
        return 2
    return 3


def a_category(score) -> int:
    if pd.isna(score):
        return pd.NA
    if score <= 18:
        return 1
    if score <= 29:
        return 2
    return 3


def p_category(score) -> int:
    if pd.isna(score):
        return pd.NA
    if score <= 2:
        return 1
    if score <= 5:
        return 2
    return 3


df_raw = pd.read_excel(RAW_PATH)

# Rename columns by position (safe regardless of bilingual header text)
rename_map = {df_raw.columns[i]: name for i, name in column_map_by_position.items()}
df = df_raw.rename(columns=rename_map).copy()

# --- Demographics ---
df["Age"] = df["Age"].apply(age_code)
df["Gender"] = df["Gender"].apply(gender_code)
df["AcadYr"] = df["AcadYr"].apply(year_code)
df["Resid"] = df["Resid"].apply(resid_code)
df["Marital"] = df["Marital"].apply(marital_code)
df["FamHist"] = df["FamHist"].apply(famhist_code)

# --- Source of information: expand comma-separated multi-select → binary dummies ---
for col_name, keyword in SOURCE_OPTIONS.items():
    df[col_name] = df["SrcInfo"].apply(
        lambda x: 1 if isinstance(x, str) and keyword.lower() in x.lower() else 0
    )
df.drop(columns=["SrcInfo"], inplace=True)

# --- Knowledge items: True/False → 1/0 ---
for col in K_COLS:
    df[col] = df[col].apply(recode_knowledge).astype("Int64")

# --- Attitude items: Likert → 1–5 ---
for col in A_COLS:
    df[col] = df[col].apply(recode_attitude).astype("Int64")

# --- Practice items: Yes/No → 1/0 ---
for col in P_COLS:
    df[col] = df[col].apply(recode_practice).astype("Int64")

# --- Composite scores and categories ---
df["K_Score"] = df[K_COLS].sum(axis=1)
df["K_Cat"] = df["K_Score"].apply(k_category)

df["A_Score"] = df[A_COLS].sum(axis=1)
df["A_Cat"] = df["A_Score"].apply(a_category)

df["P_Score"] = df[P_COLS].sum(axis=1)
df["P_Cat"] = df["P_Score"].apply(p_category)

# Binary collapsed categories for bivariate analysis
# (ceiling effects make 3-category analysis uninformative)
df["K_Cat2"] = df["K_Cat"].apply(
    lambda x: 1 if x == 3 else (0 if pd.notna(x) else pd.NA)
)
df["A_Cat2"] = df["A_Cat"].apply(
    lambda x: 1 if x == 3 else (0 if pd.notna(x) else pd.NA)
)

# Binary adequate practice outcome for logistic regression
df["P_High"] = df["P_Cat"].apply(
    lambda x: 1 if x == 3 else (0 if pd.notna(x) else pd.NA)
)

# --- Random sample ---
df_sample = df.sample(n=SAMPLE_N, random_state=RANDOM_SEED).reset_index(drop=True)
df_sample.insert(0, "ID", range(1, SAMPLE_N + 1))

col_order = (
    ["ID"]
    + ["Age", "Gender", "AcadYr", "Resid", "Marital", "FamHist"]
    + list(SOURCE_OPTIONS.keys())
    + K_COLS
    + A_COLS
    + P_COLS
    + [
        "K_Score",
        "K_Cat",
        "K_Cat2",
        "A_Score",
        "A_Cat",
        "A_Cat2",
        "P_Score",
        "P_Cat",
        "P_High",
    ]
)
df_sample = df_sample[col_order]

df_sample.to_excel(OUTPUT_PATH, index=False)
print(f"Saved: {OUTPUT_PATH}")
print(f"Shape: {df_sample.shape[0]} rows × {df_sample.shape[1]} columns")
print(f"Knowledge Good (%):    {(df_sample['K_Cat'] == 3).mean() * 100:.1f}%")
print(f"Attitude Positive (%): {(df_sample['A_Cat'] == 3).mean() * 100:.1f}%")
print(f"Practice High (%):     {(df_sample['P_Cat'] == 3).mean() * 100:.1f}%")

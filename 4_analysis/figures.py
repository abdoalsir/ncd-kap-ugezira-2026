"""
Project  : Knowledge, Attitudes, and Practices Toward Non-Communicable Diseases
           Among Medical Students at the University of Gezira, Sudan – 2026
Script   : Figure Generation (all figures)
Author   : Abdulrahman Sirelkhatim
Date     : May 2026
Input    : 1_data/cleaned/cleaned_data.xlsx
Output   : 5_figures/ directory (PNG, 300 DPI)

Figures produced:
    fig01_gender_distribution.png
    fig02_age_distribution.png
    fig03_residence_distribution.png
    fig04_family_history_distribution.png
    fig05_source_of_information.png
    fig06_knowledge_item_accuracy.png
    fig07_knowledge_category_distribution.png
    fig08_attitude_item_means.png
    fig09_attitude_category_distribution.png
    fig10_practice_item_frequency.png
    fig11_practice_category_distribution.png
    fig12_practice_category_by_gender.png
"""

import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")

DATA_PATH = "1_data/cleaned/cleaned_data.xlsx"
FIGURES_DIR = "5_figures/"

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 11
plt.rcParams["figure.dpi"] = 200

BLUE = sns.color_palette("Blues_r", 6)
PALETTE = sns.color_palette("Set2")
CONTRAST = [BLUE[1], BLUE[3], BLUE[5]]

K_ITEMS = [
    "Hypertension = persistent BP elevation",
    "Obesity increases hypertension risk",
    "Hypertension can be asymptomatic",
    "Exercise helps prevent hypertension",
    "Diabetes = high blood sugar",
    "Physical inactivity is DM risk factor",
    "Diabetes can affect kidneys",
    "Healthy diet helps prevent diabetes",
    "Smoking increases heart disease risk",
    "High cholesterol → CVD",
    "Stress increases heart disease risk",
    "CVD can be prevented",
    "Smoking → chronic lung disease",
    "Asthma is chronic respiratory disease",
    "Air pollution worsens resp. diseases",
    "CRD occurs in all age groups",
]

A_ITEMS = [
    "NCD prevention in medical education",
    "Students should join awareness campaigns",
    "Lifestyle modification prevents NCDs",
    "BP/DM screening should be routine",
    "Physicians' role in smoking cessation",
    "Chronic diseases burden Sudanese system",
    "Confident educating patients on NCDs",
    "Early diagnosis improves outcomes",
]

P_ITEMS = [
    "Exercise regularly",
    "Check blood pressure regularly",
    "Monitor blood sugar periodically",
    "Avoid cigarettes/tobacco",
    "Consume fruits/vegetables regularly",
    "Avoid excessive salty/fatty foods",
    "Participated in NCD awareness activities",
    "Seek medical advice for chronic symptoms",
]

K_COLS = [f"K{i:02d}" for i in range(1, 17)]
A_COLS = [f"A{i:02d}" for i in range(1, 9)]
P_COLS = [f"P{i:02d}" for i in range(1, 9)]


def save_fig(fig, filename):
    fig.savefig(FIGURES_DIR + filename, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {filename}")


def remove_spines(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


df = pd.read_excel(DATA_PATH)
n = len(df)


fig, ax = plt.subplots(figsize=(5, 5))
gender_counts = df["Gender"].map({1: "Male", 2: "Female"}).value_counts()
ax.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct="%1.1f%%",
    colors=[BLUE[1], PALETTE[1]],
    wedgeprops={"width": 0.6, "edgecolor": "white"},
    pctdistance=0.7,
    labeldistance=1.05,
)
ax.set_title(f"Gender Distribution (N={n})", pad=12)
save_fig(fig, "fig01_gender_distribution.png")


fig, ax = plt.subplots(figsize=(6, 4))
age_order = ["<20 years", "20–24 years", "25–29 years"]
age_counts = (
    df["Age"]
    .map({1: "<20 years", 2: "20–24 years", 3: "25–29 years"})
    .value_counts()
    .reindex(age_order)
)
pcts = age_counts / n * 100
bars = ax.bar(age_counts.index, pcts, color=BLUE[:3])
for bar, v in zip(bars, pcts):
    ax.text(
        bar.get_x() + bar.get_width() / 2, v + 0.5, f"{v:.1f}%", ha="center", fontsize=9
    )
ax.set_ylabel("Percentage (%)")
ax.set_xlabel("Age Group")
ax.set_title(f"Age Group Distribution (N={n})")
ax.set_ylim(0, 110)
remove_spines(ax)
plt.tight_layout()
save_fig(fig, "fig02_age_distribution.png")


fig, ax = plt.subplots(figsize=(5, 5))
resid_counts = df["Resid"].map({1: "Urban", 2: "Rural"}).value_counts()
ax.pie(
    resid_counts,
    labels=resid_counts.index,
    autopct="%1.1f%%",
    colors=[BLUE[1], BLUE[4]],
    wedgeprops={"width": 0.6, "edgecolor": "white"},
    pctdistance=0.7,
    labeldistance=1.05,
)
ax.set_title(f"Residence Distribution (N={n})", pad=12)
save_fig(fig, "fig03_residence_distribution.png")


fig, ax = plt.subplots(figsize=(6, 4))
fh_order = ["Yes", "No", "Don't Know"]
fh_counts = (
    df["FamHist"]
    .map({1: "Yes", 2: "No", 3: "Don't Know"})
    .value_counts()
    .reindex(fh_order)
)
pcts = fh_counts / n * 100
bars = ax.bar(fh_counts.index, pcts, color=CONTRAST)
for bar, v in zip(bars, pcts):
    ax.text(
        bar.get_x() + bar.get_width() / 2, v + 0.5, f"{v:.1f}%", ha="center", fontsize=9
    )
ax.set_ylabel("Percentage (%)")
ax.set_xlabel("Family History of NCDs")
ax.set_title(f"Family History of NCDs (N={n})")
ax.set_ylim(0, 75)
remove_spines(ax)
plt.tight_layout()
save_fig(fig, "fig04_family_history_distribution.png")


src_map = {
    "Src_Med": "Medical curriculum",
    "Src_Net": "Internet",
    "Src_SM": "Social media",
    "Src_Fam": "Family or friends",
    "Src_TV": "Television or radio",
    "Src_Wkshp": "Workshops or seminars",
}
src_pcts = {label: df[col].mean() * 100 for col, label in src_map.items()}
src_pcts = dict(sorted(src_pcts.items(), key=lambda x: x[1]))

fig, ax = plt.subplots(figsize=(7, 4))
bars = ax.barh(list(src_pcts.keys()), list(src_pcts.values()), color=BLUE[1])
for bar in bars:
    w = bar.get_width()
    ax.text(
        w + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"{w:.1f}%",
        va="center",
        fontsize=9,
    )
ax.set_xlabel("Percentage of Participants (%)")
ax.set_title(f"Sources of Information About NCDs (N={n})\n(Multiple responses allowed)")
ax.set_xlim(0, 100)
remove_spines(ax)
plt.tight_layout()
save_fig(fig, "fig05_source_of_information.png")


k_pcts = [(label, df[col].mean() * 100) for col, label in zip(K_COLS, K_ITEMS)]
k_pcts_sorted = sorted(k_pcts, key=lambda x: x[1])
labels_sorted, vals_sorted = zip(*k_pcts_sorted)
colors = [BLUE[4] if v < 90 else BLUE[1] for v in vals_sorted]

fig, ax = plt.subplots(figsize=(9, 6))
bars = ax.barh(range(len(labels_sorted)), vals_sorted, color=colors)
for bar, v in zip(bars, vals_sorted):
    ax.text(
        v + 0.2,
        bar.get_y() + bar.get_height() / 2,
        f"{v:.1f}%",
        va="center",
        fontsize=8.5,
    )
ax.set_yticks(range(len(labels_sorted)))
ax.set_yticklabels(labels_sorted, fontsize=9)
ax.set_xlabel("Percentage Correct (%)")
ax.set_title(f"Knowledge Item Accuracy (N={n})\nDarker bars = items below 90% correct")
ax.set_xlim(0, 108)
ax.axvline(90, color="gray", linestyle="--", linewidth=0.8, alpha=0.7)
remove_spines(ax)
plt.tight_layout()
save_fig(fig, "fig06_knowledge_item_accuracy.png")


k_cat_order = ["Poor (0–8)", "Fair (9–12)", "Good (13–16)"]
k_cat_counts = (
    df["K_Cat"]
    .map({1: "Poor (0–8)", 2: "Fair (9–12)", 3: "Good (13–16)"})
    .value_counts()
    .reindex(k_cat_order)
)

fig, ax = plt.subplots(figsize=(6, 4))
pcts = k_cat_counts / n * 100
bars = ax.bar(k_cat_counts.index, pcts, color=CONTRAST)
for bar, v in zip(bars, pcts):
    ax.text(
        bar.get_x() + bar.get_width() / 2, v + 0.5, f"{v:.1f}%", ha="center", fontsize=9
    )
ax.set_ylabel("Percentage (%)")
ax.set_xlabel("Knowledge Category")
ax.set_title(f"Knowledge Category Distribution (N={n})\nMean = 15.55 ± 0.91")
ax.set_ylim(0, 115)
remove_spines(ax)
plt.tight_layout()
save_fig(fig, "fig07_knowledge_category_distribution.png")


a_means = [(label, df[col].mean()) for col, label in zip(A_COLS, A_ITEMS)]
a_means_sorted = sorted(a_means, key=lambda x: x[1])
a_labels, a_vals = zip(*a_means_sorted)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(range(len(a_labels)), a_vals, color=BLUE[1])
for bar, v in zip(bars, a_vals):
    ax.text(
        v + 0.02,
        bar.get_y() + bar.get_height() / 2,
        f"{v:.2f}",
        va="center",
        fontsize=9,
    )
ax.set_yticks(range(len(a_labels)))
ax.set_yticklabels(a_labels, fontsize=9)
ax.set_xlabel("Mean Score (1–5 Likert scale)")
ax.set_title(f"Mean Scores for Attitude Items (N={n})\nCronbach's α = 0.743")
ax.set_xlim(0, 5.5)
ax.axvline(3, color="gray", linestyle="--", linewidth=0.8, alpha=0.7)
remove_spines(ax)
plt.tight_layout()
save_fig(fig, "fig08_attitude_item_means.png")


a_cat_map = {1: "Negative (8–18)", 2: "Neutral (19–29)", 3: "Positive (30–40)"}
a_cat_counts = df["A_Cat"].map(a_cat_map).value_counts()
a_order = ["Negative (8–18)", "Neutral (19–29)", "Positive (30–40)"]
a_cat_counts = a_cat_counts.reindex(a_order).dropna()

fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(
    a_cat_counts,
    labels=a_cat_counts.index,
    autopct="%1.1f%%",
    colors=CONTRAST,
    wedgeprops={"width": 0.6, "edgecolor": "white"},
    pctdistance=0.7,
    labeldistance=1.05,
)
ax.set_title(f"Attitude Category Distribution (N={n})\nMean = 35.72 ± 2.81", pad=12)
save_fig(fig, "fig09_attitude_category_distribution.png")


p_pcts = [(label, df[col].mean() * 100) for col, label in zip(P_COLS, P_ITEMS)]
p_pcts_sorted = sorted(p_pcts, key=lambda x: x[1])
p_labels, p_vals = zip(*p_pcts_sorted)
colors = [BLUE[4] if v < 50 else BLUE[1] for v in p_vals]

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.barh(range(len(p_labels)), p_vals, color=colors)
for bar, v in zip(bars, p_vals):
    ax.text(
        v + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"{v:.1f}%",
        va="center",
        fontsize=9,
    )
ax.set_yticks(range(len(p_labels)))
ax.set_yticklabels(p_labels, fontsize=9)
ax.set_xlabel("Percentage Practicing (%)")
ax.set_title(
    f"Prevalence of Preventive Practice Behaviours (N={n})\nDarker bars = below 50%"
)
ax.set_xlim(0, 110)
ax.axvline(50, color="gray", linestyle="--", linewidth=0.8, alpha=0.7)
remove_spines(ax)
plt.tight_layout()
save_fig(fig, "fig10_practice_item_frequency.png")


p_cat_map = {1: "Low (0–2)", 2: "Moderate (3–5)", 3: "High (6–8)"}
p_cat_counts = (
    df["P_Cat"]
    .map(p_cat_map)
    .value_counts()
    .reindex(["Low (0–2)", "Moderate (3–5)", "High (6–8)"])
)

fig, ax = plt.subplots(figsize=(6, 4))
pcts = p_cat_counts / n * 100
bars = ax.bar(p_cat_counts.index, pcts, color=CONTRAST)
for bar, v in zip(bars, pcts):
    ax.text(
        bar.get_x() + bar.get_width() / 2, v + 0.5, f"{v:.1f}%", ha="center", fontsize=9
    )
ax.set_ylabel("Percentage (%)")
ax.set_xlabel("Practice Category")
ax.set_title(f"Practice Category Distribution (N={n})\nMean = 4.20 ± 1.58")
ax.set_ylim(0, 90)
remove_spines(ax)
plt.tight_layout()
save_fig(fig, "fig11_practice_category_distribution.png")


gender_labels = {1: "Male (n=46)", 2: "Female (n=138)"}
p_cat_gender = (
    df.groupby("Gender")["P_Cat"]
    .value_counts(normalize=True)
    .mul(100)
    .rename("pct")
    .reset_index()
)
p_cat_gender["Gender_label"] = p_cat_gender["Gender"].map(gender_labels)
p_cat_gender["P_Cat_label"] = p_cat_gender["P_Cat"].map(
    {1: "Low", 2: "Moderate", 3: "High"}
)

x = np.arange(len(gender_labels))
cat_labels = ["Low", "Moderate", "High"]
width = 0.25
genders = ["Male (n=46)", "Female (n=138)"]

fig, ax = plt.subplots(figsize=(7, 4.5))
for i, cat in enumerate(cat_labels):
    vals = []
    for g_label in genders:
        row = p_cat_gender[
            (p_cat_gender["Gender_label"] == g_label)
            & (p_cat_gender["P_Cat_label"] == cat)
        ]
        vals.append(row["pct"].values[0] if len(row) else 0)
    bars = ax.bar(x + i * width, vals, width, label=cat, color=CONTRAST[i])
    for bar, v in zip(bars, vals):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            v + 0.3,
            f"{v:.1f}%",
            ha="center",
            fontsize=8,
        )
ax.set_xticks(x + width)
ax.set_xticklabels(genders)
ax.set_ylabel("Percentage (%)")
ax.set_xlabel("Gender")
ax.set_title("Practice Category by Gender (N=184)\nChi-square p = 0.420")
ax.legend(title="Practice Level", fontsize=9)
ax.set_ylim(0, 90)
remove_spines(ax)
plt.tight_layout()
save_fig(fig, "fig12_practice_category_by_gender.png")

print(f"\nAll figures saved to: {FIGURES_DIR}")

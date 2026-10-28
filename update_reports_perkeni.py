import os, base64, subprocess

# Re-read image base64
def get_base64_img(rel_path):
    with open(rel_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

img_perkeni = get_base64_img(r"d:\FILE NINIS\guideline_evidence\perkeni_inpatient_guideline.png")
img_lexi = get_base64_img(r"d:\FILE NINIS\guideline_evidence\lexicomp_metoclopramide_renal.png")
img_dupl = get_base64_img(r"d:\FILE NINIS\guideline_evidence\drug_interaction_gavistal_domperidone.png")
img_kdigo = get_base64_img(r"d:\FILE NINIS\guideline_evidence\kdigo_perkeni_diabetes_ckd.png")
img_perhi = get_base64_img(r"d:\FILE NINIS\guideline_evidence\perhi_acc_aha_hypertension_reconciliation.png")

# Let's update generate_final_report.py to use PERKENI instead of ADA as the primary diabetes guideline
with open(r"d:\FILE NINIS\LAPORAN_PEMANTAUAN_TERAPI_OBAT_SUNARTI.md", "r", encoding="utf-8") as f:
    md_content = f.read()

# Replace ADA mentions with PERKENI 2021 where appropriate
md_updated = md_content.replace(
    "Target ADA rawat inap (140–180 mg/dL)",
    "Target PERKENI 2021 / ADA rawat inap (140–180 mg/dL)"
).replace(
    "sesuai ADA Guidelines: berikan insulin basal kerja panjang",
    "sesuai Pedoman PERKENI 2021 (Hal. 100): berikan insulin basal kerja panjang"
).replace(
    "Target Panduan ADA (*Inpatient Glycemic Targets*):",
    "Target Panduan PERKENI 2021 (*Pengelolaan DM Rawat Inap Hal. 100*):"
).replace(
    "TARGET ADA: 180 mg/dL",
    "TARGET PERKENI: 180 mg/dL"
).replace(
    "TARGET ADA: 140 mg/dL",
    "TARGET PERKENI: 140 mg/dL"
).replace(
    "### C. Penyesuaian Regimen Insulin Rawat Inap & Target ADA (140–180 mg/dL)\n* **Guideline Acuan:** **American Diabetes Association (ADA) Standards of Care in Diabetes — Chapter: Diabetes Care in the Hospital** & **Konsensus PERKENI**.",
    "### C. Penyesuaian Regimen Insulin Rawat Inap & Target PERKENI 2021 (140–180 mg/dL)\n* **Guideline Acuan:** **Pedoman Pengelolaan dan Pencegahan Diabetes Melitus Tipe 2 Dewasa di Indonesia (PB PERKENI 2021 &bull; Bab IV.13 Hal. 100)**."
).replace(
    "![Bukti Guideline ADA Inpatient Care](guideline_evidence/ada_inpatient_guideline.png)",
    "![Bukti Guideline PERKENI 2021 Rawat Inap](guideline_evidence/perkeni_inpatient_guideline.png)"
)

# Add reference to Pedoman_Pengelolaan_DM_Tipe_2_PERKENI_2021.pdf in Section VIII
if "Pedoman_Pengelolaan_DM_Tipe_2_PERKENI_2021.pdf" not in md_updated:
    md_updated = md_updated.replace(
        "## VIII. DAFTAR BERKAS PENDUKUNG & TAUTAN FILE KERJA",
        "## VIII. DAFTAR BERKAS PENDUKUNG & TAUTAN FILE KERJA\n\n- **[Pedoman_Pengelolaan_DM_Tipe_2_PERKENI_2021.pdf](./Pedoman_Pengelolaan_DM_Tipe_2_PERKENI_2021.pdf)** *(5,81 MB &bull; Buku Resmi Pedoman Nasional DM Tipe 2 PB PERKENI 2021)*"
    )

with open(r"d:\FILE NINIS\LAPORAN_PEMANTAUAN_TERAPI_OBAT_SUNARTI.md", "w", encoding="utf-8") as f:
    f.write(md_updated)

print("Updated LAPORAN_PEMANTAUAN_TERAPI_OBAT_SUNARTI.md with PERKENI 2021!")

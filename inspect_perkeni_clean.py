import pypdf, sys

sys.stdout.reconfigure(encoding="utf-8")

reader = pypdf.PdfReader(r"d:\FILE NINIS\Pedoman_Pengelolaan_DM_Tipe_2_PERKENI_2021.pdf")

pages_to_check = [38, 41, 42, 45, 53, 73, 74, 100, 110, 111]

for p in pages_to_check:
    print(f"=====================================")
    print(f"=== PAGE {p} ===")
    txt = reader.pages[p - 1].extract_text() or ""
    for line in txt.splitlines():
        if any(w in line.lower() for w in ["gliquidone", "glikuidon", "glimepirid", "metformin", "insulin", "basal", "bolus", "ginjal", "lfg", "egfr", "crcl", "sasaran", "target", "hipoglikemia"]):
            print("  ", line.strip())

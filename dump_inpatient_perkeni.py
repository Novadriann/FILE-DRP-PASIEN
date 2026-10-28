import pypdf, sys

sys.stdout.reconfigure(encoding="utf-8")

reader = pypdf.PdfReader(r"d:\FILE NINIS\Pedoman_Pengelolaan_DM_Tipe_2_PERKENI_2021.pdf")

for p in range(98, 104):
    print(f"=====================================")
    print(f"=== PAGE {p} ===")
    print(reader.pages[p - 1].extract_text())

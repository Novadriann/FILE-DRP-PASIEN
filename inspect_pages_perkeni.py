import pypdf

reader = pypdf.PdfReader(r"d:\FILE NINIS\Pedoman_Pengelolaan_DM_Tipe_2_PERKENI_2021.pdf")

pages_to_check = [13, 14, 31, 38, 49, 50, 51, 100, 110, 111]

for p in pages_to_check:
    print(f"=====================================")
    print(f"=== PAGE {p} ===")
    txt = reader.pages[p - 1].extract_text() or ""
    for line in txt.splitlines()[:30]:
        print("  ", line)

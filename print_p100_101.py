import pypdf, sys
sys.stdout.reconfigure(encoding="utf-8")

reader = pypdf.PdfReader(r"d:\FILE NINIS\Pedoman_Pengelolaan_DM_Tipe_2_PERKENI_2021.pdf")
print("=== PAGE 100 ===")
print(reader.pages[99].extract_text())
print("=== PAGE 101 ===")
print(reader.pages[100].extract_text())

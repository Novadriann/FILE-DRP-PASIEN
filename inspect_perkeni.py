import pypdf

reader = pypdf.PdfReader(r"d:\FILE NINIS\Pedoman_Pengelolaan_DM_Tipe_2_PERKENI_2021.pdf")
print(f"Total pages: {len(reader.pages)}")

# Search for chapters in first 15 pages
for i in range(min(15, len(reader.pages))):
    txt = reader.pages[i].extract_text() or ""
    if "daftar isi" in txt.lower():
        print(f"=== DAFTAR ISI (Page {i+1}) ===")
        print(txt)

# Search keywords
keywords = ["rawat inap", "rumah sakit", "140-180", "140–180", "glikuidon", "gliquidone", "gagal ginjal", "laju filtrasi glomerulus", "penyakit ginjal"]
matches = {k: [] for k in keywords}

for idx, page in enumerate(reader.pages):
    txt = page.extract_text() or ""
    for k in keywords:
        if k in txt.lower():
            matches[k].append(idx + 1)

for k, pgs in matches.items():
    print(f"Keyword '{k}': found in pages {pgs[:10]} (total {len(pgs)})")

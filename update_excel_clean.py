import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side

wb = openpyxl.load_workbook(r"d:\FILE NINIS\CPPT RANAP.xlsx")
ws = wb["RANAP"]

# DRP Data
drp_data = [
    (
        "ISPA / Batuk berdahak",
        "1. Pasien mengeluhkan batuk berdahak putih sejak awal masuk hingga hari ke-3, namun belum mendapatkan terapi mukolitik/ekspektoran (Indikasi belum diterapi - PCNE C1.1).",
        "Merekomendasikan pemberian mukolitik oral, seperti N-Asetilsistein 3 x 200 mg kapsul atau Ambroxol 3 x 30 mg tablet oral untuk mengencerkan dahak pasien selama 3-5 hari.",
        "Monitoring keluhan batuk, kemudahan ekspektorasi sputum, serta frekuensi pernapasan (RR)."
    ),
    (
        "DM Tipe 2 / Hiperglikemia",
        "2. Kadar GDP puasa terus meningkat selama rawat inap (16/10: 235 mg/dL, 17/10: 236 mg/dL, 18/10: 298 mg/dL) meskipun dosis Novorapid dinaikkan (3x8 -> 3x10 -> 3x12 UI). Regimen rapid-acting insulin saja tanpa basal tidak mengontrol glukosa darah puasa malam-pagi hari. Target ADA: 140-180 mg/dL (Regimen sub-optimal - PCNE C1.4).",
        "Merekomendasikan penerapan regimen Basal-Bolus sesuai ADA Standards of Care: berikan insulin basal kerja panjang (Insulin Glargine 8-10 unit 1x sehari malam) untuk supresi glukosa hepatik puasa, dipadukan dengan Novorapid prandial dosis lebih terkontrol (misal 3x4-6 unit ac) serta koreksi.",
        "Monitoring GDP (pagi) dan GD2PP/GDS berkala setiap hari, target rawat inap 140-180 mg/dL, serta waspadai tanda hipoglikemia (<70 mg/dL)."
    ),
    (
        "Penurunan Fungsi Ginjal (CrCl 30,69 mL/mnt)",
        "3. Kreatinin serum 1,80 mg/dL dengan CrCl 30,69 mL/menit (eGFR 31,46 mL/min/1.73m2) menunjukkan gangguan ginjal (AKI prerenal), sehingga diperlukan penyesuaian dosis metoklopramid 50% untuk mencegah akumulasi dan efek samping ekstrapiramidal / tardive dyskinesia (Dosis berlebih pada gangguan ginjal - PCNE C3.1).",
        "Sesuai FDA label & Lexicomp, pasien dengan CrCl 10-40 mL/menit memerlukan reduksi dosis metoklopramid sebesar 50% (5 mg IV q8h atau 10 mg q12h; max 15 mg/hari). Namun karena muntah sudah teratasi sejak 16/10, merekomendasikan HENTIKAN terapi metoklopramid.",
        "Monitoring tanda gejala ekstrapiramidal (distonia, tremor, akatisia, diskinesia) dan fungsi ginjal serial."
    ),
    (
        "Anemia Ringan",
        "4. Pasien mengalami anemia ringan normositik normokrom (Hb 11,6 g/dL, Hematokrit 33,9%), kemungkinan anemia of chronic disease atau hemodilusi pasca hidrasi.",
        "Belum memerlukan terapi transfusi atau ESA. Lakukan evaluasi status besi (SI, TIBC, Feritin) bila keluhan lemas/anemia persisten pasca pulang.",
        "Monitoring kadar Hemoglobin dan Hematokrit secara berkala saat kontrol rawat jalan."
    ),
    (
        "Duplikasi Antiemetik Ranap",
        "5. Terdapat duplikasi terapi antiemetik/prokinetik rawat inap antara Injeksi Metoklopramid 3x10 mg IV dan Domperidone tablet 2x10 mg oral pada tgl 17-18/10 (Duplikasi terapi - PCNE C1.3).",
        "Keduanya adalah antagonis reseptor dopamin D2. Duplikasi meningkatkan risiko aritmia pemanjangan interval QT dan neurotoksisitas. Merekomendasikan HENTIKAN Domperidone oral dan tapering metoklopramid.",
        "Monitoring keluhan mual/muntah serta rekam EKG (interval QTc) jika timbul palpitasi."
    ),
    (
        "DUPLIKASI FATAL RESEP PULANG (Gavistal + Domperidone)",
        "6. [MAJOR ALERT RESEP PULANG] Resep pulang memuat GAVISTAL 10 MG TAB 3x1 dan DOMPERIDONE 10 MG TAB 2x1. Gavistal adalah nama dagang METOCLOPRAMIDE 10 mg! Pasien diresepkan Metoklopramid + Domperidone sekaligus untuk dibawa pulang. Ini adalah duplikasi obat 100% yang berbahaya bagi lansia wanita dengan CrCl 30,69 mL/menit (Duplikasi terapi berat - PCNE C1.3 / P2.1).",
        "INTERVENSI SEGERA: BATALKAN GAVISTAL DAN DOMPERIDONE pada resep pulang. Pasien sudah menyatakan TAK (Tidak Ada Keluhan) dan minta pulang pada tgl 18/10, sehingga obat prokinetik/antiemetik rutin sudah tidak diperlukan lagi.",
        "Monitoring keluhan mual/muntah di rumah; edukasi keluarga untuk tidak memberikan obat antimual ganda."
    ),
    (
        "OMISSION TERAPI KRONIS SAAT PULANG (Amlodipin & Clopidogrel)",
        "7. [MAJOR ALERT RESEP PULANG] Pasien memiliki riwayat Hipertensi rutin Amlodipin 10 mg 1x1 dan Clopidogrel 75 mg 1x1. Obat distop saat MRS karena dehidrasi (TD 90/60). Namun pada saat pulang (18/10), TD pasien mencapai 144/81 mmHg, tetapi Amlodipin dan Clopidogrel TIDAK DIRESEPKAN KEMBALI dalam resep pulang (Indikasi kronis tidak diterapi - PCNE C1.1).",
        "Lakukan rekonsiliasi obat pulang segera: MULAI KEMBALI Amlodipin 5-10 mg 1x sehari pagi (target TD <130/80 mmHg) dan Clopidogrel 75 mg 1x sehari untuk prevensi sekunder kardio/serebrovaskular.",
        "Monitoring tekanan darah harian secara mandiri di rumah dan tanda komplikasi kardiovaskular/stroke."
    ),
    (
        "Kombinasi OAD & Insulin Pulang Berisiko Tinggi Hipoglikemia",
        "8. Resep pulang mengombinasikan Glikuidon 30 mg 1x1 tab pagi ac dengan Novorapid Flexpen 3 x 12 UI ac (total 36 UI/hari). Memberikan sulfonilurea bersamaan dengan insulin prandial dosis tinggi pada lansia pasca pemulihan anoreksia sangat berisiko memicu fatal hipoglikemia di rumah. Jarum Novofine juga hanya diresepkan 1 buah (Safety Alert - PCNE C1.4 / P2.1).",
        "Evaluasi penyederhanaan regimen: Jika asupan makan stabil, optimalkan Glikuidon 30 mg 1-2x/hari sebelum makan. Jika membutuhkan insulin, gunakan insulin basal malam dosis kecil (Glargine 8-10 unit) daripada Novorapid 3x12 UI + Glikuidon. Berikan jarum suntik yang cukup (minimal 1 box / 10 pcs) dan edukasi hipoglikemia.",
        "Monitoring Glukosa Darah Mandiri (SMBG) puasa dan postprandial, serta edukasi tanda-tanda hipoglikemia (<70 mg/dL)."
    ),
    (
        "Polifarmasi Gastrointestinal Pulang Berlebih",
        "9. Pasien dipulangkan dengan 5 macam obat lambung: Antasida sirup 3x1, Omeprazole 20 mg 2x1, Rebamipide 3x1, Domperidone 2x1, Gavistal (Metoklopramid) 3x1. Diagnosis awal adalah intoksikasi susu jahe akut yang sudah sembuh total, tanpa bukti ulkus aktif. Ini adalah polifarmasi berlebih yang membebani pasien lansia (Polifarmasi - PCNE C1.3).",
        "Sederhanakan terapi lambung: Cukup berikan Omeprazole 1 x 20 mg kapsul pagi (1 jam sebelum makan) selama 5-7 hari untuk proteksi sisa mukosa lambung. Hentikan Antasida, Rebamipide, Domperidone, dan Gavistal.",
        "Monitoring keluhan dispepsia / rasa terbakar di ulu hati pasca pemulangan."
    ),
    (
        "Ketiadaan Pemantauan Laboratorium Kontrol Pasca-Tindakan",
        "10. Pasien masuk dengan hiponatremia (Na 127,36), hipokloremia (Cl 87,75), dan azotemia (Ureum 57, Cr 1,80). Diberikan infus NaCl 0,9% selama rawat inap, namun elektrolit dan fungsi ginjal TIDAK PERNAH DIPERIKSA ULANG sebelum pulang untuk memastikan perbaikan (Kurangnya monitoring - PCNE C3.5).",
        "Jadwalkan pemeriksaan kontrol laboratorium saat jadwal kunjungan kontrol ke Poli Penyakit Dalam 1 minggu pasca pulang, meliputi: Ureum, Kreatinin Serum, Elektrolit (Na, K, Cl), serta GDP dan HbA1c.",
        "Evaluasi reversibilitas AKI prerenal dan pertimbangan penyesuaian obat jangka panjang (seperti kapan Metformin aman dimulai kembali jika eGFR >45)."
    )
]

# Unmerge rows 138-144
to_unmerge = [rng for rng in ws.merged_cells.ranges if rng.min_row >= 138]
for rng in to_unmerge:
    ws.unmerge_cells(str(rng))

font_regular = Font(name="Calibri", size=10)
font_bold = Font(name="Calibri", size=10, bold=True)
align_left_wrap = Alignment(horizontal="left", vertical="top", wrap_text=True)

start_row = 138
for i, (masalah, drp_desc, rekomm, monev) in enumerate(drp_data):
    cur_row = start_row + i
    
    # Merge B:D, E:K, L:M
    ws.merge_cells(start_row=cur_row, start_column=2, end_row=cur_row, end_column=4)
    ws.merge_cells(start_row=cur_row, start_column=5, end_row=cur_row, end_column=11)
    ws.merge_cells(start_row=cur_row, start_column=12, end_row=cur_row, end_column=13)
    
    ws.cell(cur_row, 1, masalah).font = font_bold
    ws.cell(cur_row, 2, drp_desc).font = font_regular
    ws.cell(cur_row, 5, rekomm).font = font_regular
    ws.cell(cur_row, 12, monev).font = font_regular
    ws.cell(cur_row, 14, "Ya").font = font_bold
    
    ws.cell(cur_row, 1).alignment = align_left_wrap
    ws.cell(cur_row, 2).alignment = align_left_wrap
    ws.cell(cur_row, 5).alignment = align_left_wrap
    ws.cell(cur_row, 12).alignment = align_left_wrap
    ws.cell(cur_row, 14).alignment = Alignment(horizontal="center", vertical="top")

# Add CATATAN FARMASI
catatan_title_row = start_row + len(drp_data) + 1
ws.merge_cells(start_row=catatan_title_row, start_column=1, end_row=catatan_title_row, end_column=16)
ws.cell(catatan_title_row, 1, "CATATAN FARMASI KLINIS (DISCHARGE RECONCILIATION SUMMARY)")
ws.cell(catatan_title_row, 1).font = Font(name="Calibri", size=11, bold=True, color="0369A1")

notes = [
    "1. Pasien Ny. Sunarti (62 th 10 bln, RM 00109480) dirawat tgl 14-18 Oktober 2026 dengan Vomitus Profuse ec suspek food intoxication, DM hiperglikemia, Riw. Hipertensi, Hiponatremia-Hipokloremia ringan, dan Prerenal AKI (CrCl 30,69 mL/mnt).",
    "2. TELAH DILAKUKAN REKONSILIASI RESEP PULANG: (a) Batalkan Gavistal 3x10 mg dan Domperidone 2x10 mg karena duplikasi berbahaya (keduanya antagonis D2 dopamin); (b) Lanjutkan kembali Amlodipin 5-10 mg 1x1 dan Clopidogrel 75 mg 1x1 yang sempat terhenti saat dehidrasi; (c) Waspadai hipoglikemia akibat kombinasi Glikuidon 30 mg + Novorapid 3x12 UI;",
    "3. Sederhanakan obat lambung pulang: cukup Omeprazole 1x20 mg pagi selama 5-7 hari; Antasida sirup dan Rebamipide dihentikan;",
    "4. Edukasi alergi Amoksisilin & Ampisilin telah diberikan;",
    "5. Kontrol laboratorium (Ureum, Kreatinin, Elektrolit, GDP/HbA1c) dijadwalkan saat kunjungan kontrol poli 1 minggu lagi."
]

for idx, n in enumerate(notes):
    nrow = catatan_title_row + 1 + idx
    ws.merge_cells(start_row=nrow, start_column=2, end_row=nrow, end_column=16)
    ws.cell(nrow, 2, n).font = font_regular
    ws.cell(nrow, 2).alignment = align_left_wrap

out_excel = r"d:\FILE NINIS\CPPT_RANAP_LENGKAP.xlsx"
wb.save(out_excel)
wb.save(r"d:\FILE NINIS\CPPT RANAP.xlsx")
print("Successfully generated CPPT_RANAP_LENGKAP.xlsx and updated CPPT RANAP.xlsx!")

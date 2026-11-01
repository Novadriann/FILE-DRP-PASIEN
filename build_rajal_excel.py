import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import os
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "RAJAL"

# Styling definitions
font_title = Font(name="Calibri", size=14, bold=True, color="1E3A8A")
font_subtitle = Font(name="Calibri", size=11, bold=True, color="1E3A8A")
font_sec_hdr = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
font_tbl_hdr = Font(name="Calibri", size=10, bold=True, color="0F172A")
font_bold = Font(name="Calibri", size=10, bold=True)
font_regular = Font(name="Calibri", size=10)
font_italic = Font(name="Calibri", size=9, italic=True, color="64748B")
font_alert = Font(name="Calibri", size=10, bold=True, color="B91C1C")

fill_navy = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
fill_blue_light = PatternFill(start_color="E0F2FE", end_color="E0F2FE", fill_type="solid")
fill_gray_light = PatternFill(start_color="F1F5F9", end_color="F1F5F9", fill_type="solid")
fill_yellow_light = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
fill_red_light = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
fill_green_light = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")

thin_border_side = Side(border_style="thin", color="CBD5E1")
med_border_side = Side(border_style="medium", color="1E3A8A")
border_all_thin = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
border_box = Border(left=med_border_side, right=med_border_side, top=med_border_side, bottom=med_border_side)

align_center = Alignment(horizontal="center", vertical="center", wrap_text=True)
align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
align_right = Alignment(horizontal="right", vertical="center")

# Title Header
ws.merge_cells("A1:K1")
ws["A1"] = "INSTALASI FARMASI RSPAU DR. S. HARDJOLUKITO"
ws["A1"].font = font_title
ws["A1"].alignment = align_center

ws.merge_cells("A2:K2")
ws["A2"] = "FORM PEMANTAUAN TERAPI OBAT (PTO) PASIEN RAWAT JALAN - POLI PENYAKIT DALAM"
ws["A2"].font = font_subtitle
ws["A2"].alignment = align_center

ws["A3"] = "Farmasis / Apoteker : "
ws["A3"].font = font_bold
ws["C3"] = "Nurhasna Sushmita Sari, S.Farm. / Tim PKPA Farmasi Klinis"
ws["C3"].font = font_regular

# Patient Demographics Table
demographics = [
    ("Nama Pasien", "SRI WISRAYA, NY", "Poli / Klinik", "Poli Penyakit Dalam (Raber: Poli Orthopedi, Poli Saraf, Poli Mata)"),
    ("No. RM", "00062584", "DPJP", "dr. Tri Hariningsih, Sp.PD"),
    ("BB / TB / IMT", "52-54 kg / 156 cm / 21.4 - 22.2 kg/m² (Ideal)", "Dokter Raber", "dr. Raden Suhana Sp.OT(K), dr. Wahyu Wihartono Sp.N, dr. Supanji Sp.M"),
    ("Usia / Tgl Lahir", "64 tahun / 28 September 1962", "Periode PTO", "6 Bulan Terakhir (27 April 2026 s.d. 27 Oktober 2026)"),
    ("Jenis Kelamin / Gol. Darah", "Perempuan / Golongan Darah O", "Jaminan Bayar", "JKN Non PBI (BPJS Kesehatan)"),
    ("Alergi Obat", "Tidak Ada Riwayat Alergi Obat (-)", "Riwayat Rawat", "IGD / Rawat Singkat 04-07-2026 s.d 07-07-2026 (CKR ec Trauma Jatuh)"),
    ("Diagnosa Utama", "E11.6 - Non-insulin-dependent diabetes mellitus with other specified complications (DM Tipe 2 Tak Terkontrol)", "", ""),
    ("Diagnosa Sekunder 1", "I10 - Essential (primary) hypertension (Hipertensi Grade 1-2)", "", ""),
    ("Diagnosa Sekunder 2", "E78.5 - Hyperlipidaemia, unspecified (Dislipidemia / Hiperlipidemia)", "", ""),
    ("Diagnosa Sekunder 3", "M17.9 - Gonarthrosis, unspecified (Osteoarthritis / OA Genu Bilateral)", "", ""),
    ("Diagnosa Sekunder 4", "E11.5 - Diabetic Neuropathy (Neuropati Perifer Diabetik) & H81.4 - Vertigo of central origin", "", "")
]

row = 4
for item in demographics:
    ws.cell(row, 1, item[0]).font = font_bold
    ws.cell(row, 1).fill = fill_gray_light
    ws.cell(row, 1).border = border_all_thin
    
    ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=4)
    c2 = ws.cell(row, 2, item[1])
    c2.font = font_regular
    for c in range(2, 5):
        ws.cell(row, c).border = border_all_thin
        
    if item[2]:
        ws.cell(row, 5, item[2]).font = font_bold
        ws.cell(row, 5).fill = fill_gray_light
        ws.cell(row, 5).border = border_all_thin
        
        ws.merge_cells(start_row=row, start_column=6, end_row=row, end_column=11)
        c6 = ws.cell(row, 6, item[3])
        c6.font = font_regular
        for c in range(6, 12):
            ws.cell(row, c).border = border_all_thin
    else:
        ws.merge_cells(start_row=row, start_column=2, end_row=row, end_column=11)
    row += 1

# Section 1: Subjective Complaints Timeline
row += 1
ws.merge_cells(f"A{row}:K{row}")
ws[f"A{row}"] = "I. DATA SUBJEKTIF - ANAMNESIS & KELUHAN KLINIS PASIEN PER KUNJUNGAN (6 BULAN TERAKHIR)"
ws[f"A{row}"].font = font_sec_hdr
ws[f"A{row}"].fill = fill_navy
ws[f"A{row}"].alignment = align_left

row += 1
subj_headers = ["Parameter / Keluhan", "27-04-2026 (M1)", "29-05-2026 (M2)", "29-06-2026 (M3)", "04-07-2026 (IGD)", "05-08-2026 (M4)", "07-09-2026 (M5)", "07-10-2026 (M6)", "Catatan & Evaluasi Klinis"]
col_spans = [1, 1, 1, 1, 1, 1, 1, 1, 3]

curr_col = 1
for idx, h in enumerate(subj_headers):
    span = col_spans[idx]
    if span > 1:
        ws.merge_cells(start_row=row, start_column=curr_col, end_row=row, end_column=curr_col+span-1)
    cell = ws.cell(row, curr_col, h)
    cell.font = font_tbl_hdr
    cell.fill = fill_blue_light
    cell.alignment = align_center
    for c in range(curr_col, curr_col+span):
        ws.cell(row, c).border = border_all_thin
    curr_col += span

subj_data = [
    ("Keluhan Utama Dokter", "Kontrol rutin DM", "Lutut sakit, bengkak (-)", "Lutut kiri nyeri, kaki kaku", "Trauma jatuh kepala terbentur", "Evaluasi paska rawat, nyeri lutut", "Nyeri lutut belum berkurang, gliyer (+)", "Lutut kanan sakit, nyeri gerak", "Keluhan kronis OA genu menetap"),
    ("Nyeri Sendi Lutut (OA)", "+", "++", "+++", "++", "++", "++", "++", "Refrakter terhadap Flamar Gel; butuh edukasi beban lutut"),
    ("Kebas / Parestesia / Kaku Kaki", "+", "+", "++", "+", "+", "+", "+", "Neuropati perifer diabetik akibat glukotoksisitas kronis"),
    ("Pusing / Vertigo / Gliyer", "-", "-", "+", "+++ (Jatuh)", "+", "++ (Vertigo Central)", "+", "Memicu trauma jatuh 04/07; diterapi Flunarizine 5 mg"),
    ("Poli Lain yang Dikunjungi", "Poli Penyakit Dalam", "Poli Mata, Poli Saraf", "Poli Mata", "IGD (Bedah/Saraf/Rad)", "Poli Mata", "Poli Mata", "Poli Orthopedi (08/10), Poli Mata", "Perawatan multidisiplin (Penyakit Dalam, Mata, Ortho, Saraf)")
]

for item in subj_data:
    row += 1
    curr_col = 1
    for idx, val in enumerate(item):
        span = col_spans[idx]
        if span > 1:
            ws.merge_cells(start_row=row, start_column=curr_col, end_row=row, end_column=curr_col+span-1)
        cell = ws.cell(row, curr_col, val)
        cell.font = font_bold if idx == 0 else font_regular
        cell.alignment = align_left if idx in [0, 8] else align_center
        if idx in [1, 2, 3, 4, 5, 6, 7] and "++" in val:
            cell.fill = fill_yellow_light
        if "Jatuh" in val:
            cell.fill = fill_red_light
            cell.font = font_alert
        for c in range(curr_col, curr_col+span):
            ws.cell(row, c).border = border_all_thin
        curr_col += span

# Section 2: Objective - Vital Signs
row += 2
ws.merge_cells(f"A{row}:K{row}")
ws[f"A{row}"] = "II. DATA OBJEKTIF - TANDA-TANDA VITAL (TTV) 6 BULAN TERAKHIR & NILAI TARGET"
ws[f"A{row}"].font = font_sec_hdr
ws[f"A{row}"].fill = fill_navy
ws[f"A{row}"].alignment = align_left

row += 1
ttv_headers = ["Parameter TTV", "Satuan", "Nilai Target", "27-04-2026", "29-05-2026", "29-06-2026", "05-08-2026", "07-09-2026", "07-10-2026", "Interpretasi & Keterangan"]
col_spans_ttv = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]

curr_col = 1
for idx, h in enumerate(ttv_headers):
    span = col_spans_ttv[idx]
    if span > 1:
        ws.merge_cells(start_row=row, start_column=curr_col, end_row=row, end_column=curr_col+span-1)
    cell = ws.cell(row, curr_col, h)
    cell.font = font_tbl_hdr
    cell.fill = fill_blue_light
    cell.alignment = align_center
    for c in range(curr_col, curr_col+span):
        ws.cell(row, c).border = border_all_thin
    curr_col += span

ttv_data = [
    ("Tekanan Darah Sistole", "mmHg", "< 130 (PERHI)", "130", "138", "156", "165", "141", "133", "Hipertensi belum terkontrol optimal dengan monoterapi Amlodipin 10 mg"),
    ("Tekanan Darah Diastole", "mmHg", "< 80 (PERHI)", "80", "76", "85", "89", "80", "77", "Diastole terkontrol baik (<80-89 mmHg)"),
    ("Denyut Nadi", "x/menit", "60 - 100", "80", "97", "89", "103", "92", "85", "Cenderung takikardia ringan saat nyeri lutut / TD melonjak (05/08)"),
    ("Laju Nafas (RR)", "x/menit", "12 - 20", "20", "22", "22", "20", "21", "20", "Dalam batas normal"),
    ("Suhu Tubuh", "°C", "< 37.5", "36.5", "36.0", "36.0", "36.5", "36.0", "36.0", "Afebris / normotermia sepanjang pengamatan"),
    ("SPO2", "%", "≥ 95%", "99%", "99%", "99%", "99%", "99%", "99%", "Saturasi oksigen baik"),
    ("Berat Badan (BB)", "kg", "50 - 55", "53.0", "54.0", "53.0", "53.0", "52.0", "52.0", "BB stabil, fluktuasi 52-54 kg"),
    ("Tinggi Badan (TB)", "cm", "-", "156", "152*", "156", "156", "156", "156", "TB pasien 156 cm (*pencatatan 152 pada 29/05)"),
    ("Indeks Massa Tubuh (IMT)", "kg/m²", "18.5 - 22.9", "21.78", "23.37", "21.78", "21.78", "21.37", "21.37", "Status gizi normoweight (ideal)")
]

for item in ttv_data:
    row += 1
    curr_col = 1
    for idx, val in enumerate(item):
        span = col_spans_ttv[idx]
        if span > 1:
            ws.merge_cells(start_row=row, start_column=curr_col, end_row=row, end_column=curr_col+span-1)
        cell = ws.cell(row, curr_col, val)
        cell.font = font_bold if idx == 0 else font_regular
        cell.alignment = align_left if idx in [0, 9] else align_center
        # highlight abnormal BP
        if idx in [5, 6, 7] and item[0] == "Tekanan Darah Sistole" and int(val) > 140:
            cell.fill = fill_red_light
            cell.font = font_alert
        for c in range(curr_col, curr_col+span):
            ws.cell(row, c).border = border_all_thin
        curr_col += span

# Section 3: Objective - Laboratory Trends
row += 2
ws.merge_cells(f"A{row}:K{row}")
ws[f"A{row}"] = "III. DATA OBJEKTIF - MATRIKS HASIL LABORATORIUM 6 BULAN TERAKHIR & NILAI RUJUKAN"
ws[f"A{row}"].font = font_sec_hdr
ws[f"A{row}"].fill = fill_navy
ws[f"A{row}"].alignment = align_left

row += 1
lab_headers = ["Parameter Laboratorium", "Satuan", "Nilai Rujukan", "27-03-2026", "29-05-2026", "29-06-2026", "04/07 - 07/07 (IGD)", "05-08-2026", "07-09-2026", "07-10-2026", "Analisis & Evaluasi Klinis"]

curr_col = 1
for idx, h in enumerate(lab_headers):
    cell = ws.cell(row, curr_col, h)
    cell.font = font_tbl_hdr
    cell.fill = fill_blue_light
    cell.alignment = align_center
    cell.border = border_all_thin
    curr_col += 1

lab_data = [
    ("HbA1c", "%", "< 6.5 (Target <7.0%)", "-", "9.1*", "-", "-", "-", "-", "-", "TIDAK TERKONTROL (Glukotoksisitas tinggi, indikasi intensifikasi terapi)"),
    ("Glukosa Darah Puasa (GDP)", "mg/dL", "70 - 115 (Target 80-130)", "-", "-", "169*", "-", "-", "190*", "151*", "Tinggi secara persisten sepanjang pemantauan"),
    ("Glukosa Darah 2 Jam PP", "mg/dL", "< 140 (Target <180)", "-", "-", "211*", "-", "-", "-", "-", "Hiperglikemia postprandial signifikan (mendasari penambahan Acarbose)"),
    ("Glukosa Darah Sewaktu (GDS)", "mg/dL", "< 200", "158", "252*", "-", "244-308* (04-05/07) | 83-102 (06-07/07)", "160", "-", "-", "Fluktuasi tajam; saat rawat Juli sempat spike 308 mg/dL lalu turun ke 83 mg/dL"),
    ("Hemoglobin (Hb)", "g/dL", "11.7 - 15.5", "-", "-", "-", "10.1* (04/07)", "-", "-", "-", "Anemia ringan mikrositik/normositik ec penyakit kronis (CKD/DM)"),
    ("Hematokrit", "%", "35 - 47", "-", "-", "-", "30.0* (04/07)", "-", "-", "-", "Menurun selaras dengan kadar Hemoglobin"),
    ("Trombosit", "/mm³", "150.000 - 440.000", "-", "-", "-", "228.000 (04/07)", "-", "-", "-", "Normal"),
    ("Ureum", "mg/dL", "21 - 43", "-", "-", "-", "73* (04/07)", "-", "-", "-", "Retensi nitrogen / azotemia pada kondisi stres trauma/dehidrasi"),
    ("Kreatinin Serum", "mg/dL", "0.6 - 1.1", "-", "-", "-", "2.69* (04/07)", "-", "-", "Order 06/11", "Penurunan fungsi ginjal nyata (CrCl = 17.67 mL/min); order ulang 07/10"),
    ("SGOT (AST)", "U/L", "< 35", "-", "-", "-", "29 (04/07)", "-", "-", "-", "Fungsi hepatik baik"),
    ("SGPT (ALT)", "U/L", "< 34", "-", "-", "-", "20 (04/07)", "-", "-", "-", "Fungsi hepatik baik; aman untuk terapi Statin (Atorvastatin)")
]

for item in lab_data:
    row += 1
    for idx, val in enumerate(item):
        cell = ws.cell(row, idx+1, val)
        cell.font = font_bold if idx == 0 else font_regular
        cell.alignment = align_left if idx in [0, 10] else align_center
        if "*" in val:
            cell.fill = fill_red_light
            cell.font = font_alert
        cell.border = border_all_thin

# Section 4: Medication Profile 6 Months
row += 2
ws.merge_cells(f"A{row}:K{row}")
ws[f"A{row}"] = "IV. PROFIL TERAPI PENGOBATAN RAWAT JALAN 6 BULAN TERAKHIR (APRIL - OKTOBER 2026)"
ws[f"A{row}"].font = font_sec_hdr
ws[f"A{row}"].fill = fill_navy
ws[f"A{row}"].alignment = align_left

row += 1
rx_headers = ["Nama Obat & Bentuk Sediaan", "Kekuatan", "Rute", "Aturan Pakai & Waktu", "27/04/26", "29/05/26", "29/06/26", "05/08/26", "07/09/26", "07/10/26", "Tujuan Terapi & Perubahan Regimen"]

for idx, h in enumerate(rx_headers):
    cell = ws.cell(row, idx+1, h)
    cell.font = font_tbl_hdr
    cell.fill = fill_blue_light
    cell.alignment = align_center
    cell.border = border_all_thin

rx_data = [
    ("Glimepirid Tab", "3 mg / 4 mg", "Oral", "1x1 (Apr-Mei) / 2x1 (Jun-Okt)", "4 mg (30)", "4 mg (30)", "3 mg (60)", "3 mg (60)", "3 mg (60)", "3 mg (60)", "Dosis dinaikkan dari 4 mg menjadi 6 mg/hari (2x1) sejak Juni 2026. PERINGATAN: Terlalu tinggi untuk geriatri!"),
    ("Sitagliptin Tab (Januvia)", "100 mg", "Oral", "1x1 tab sesudah makan", "-", "100 mg (30)", "100 mg (30)", "100 mg (30)", "100 mg (30)", "100 mg (30)", "Ditambahkan sejak Mei 2026 sebagai kombinasi ganda/tripel. Perlu penyesuaian dosis bila eGFR < 45 mL/min."),
    ("Acarbose Tab (Glucobay)", "100 mg", "Oral", "2x1 tab bersama suapan pertama", "-", "-", "-", "-", "100 mg (60)", "100 mg (60)", "Ditambahkan September 2026 untuk menurunkan GD2PP (211 mg/dL). Wajib suapan pertama makanan."),
    ("Amlodipin Tab", "10 mg", "Oral", "1x1 tab pagi hari", "10 mg (30)", "10 mg (30)", "10 mg (30)", "10 mg (30)", "10 mg (30)", "10 mg (30)", "Antihipertensi CCB rutin. Monoterapi belum mencapai target (<130/80 mmHg)."),
    ("Rosuvastatin Tab", "10 mg", "Oral", "1x1 tab malam hari", "10 mg (30)", "10 mg (30)", "10 mg (30)", "10 mg (30)", "10 mg (30)", "-", "Statin dislipidemia rutin April s.d September 2026."),
    ("Atorvastatin Tab", "20 mg", "Oral", "1x1 tab malam hari", "-", "-", "-", "-", "-", "20 mg (30)", "Diswitch dari Rosuvastatin pada Oktober 2026. Sangat tepat karena bersihan hepatik aman bagi ginjal."),
    ("Gabapentin Kap", "100 mg", "Oral", "1x1 kap malam hari", "100 mg (30)", "100 mg (30)", "100 mg (30)", "100 mg (30)", "100 mg (30)", "100 mg (30)", "Terapi nyeri neuropati diabetik rutin. Dosis awal lansia yang adekuat."),
    ("Mecobalamin Kap", "500 mcg", "Oral", "1x1 kap sesudah makan", "500 mcg (30)", "500 mcg (30)", "500 mcg (30)", "-", "-", "-", "Neurotropik vitamin B12 aktif (dihentikan sejak Agustus 2026)."),
    ("Glucosamine Tab", "500 mg", "Oral", "1x1 tab sesudah makan", "500 mg (30)", "500 mg (30)", "500 mg (30)", "-", "500 mg (30)", "Di Poli Ortho", "Suplemen kondroprotektif kartilago sendi OA Genu."),
    ("Flamar Gel (Diclofenac)", "1% Gel", "Topikal", "2x1 oles di sendi lutut", "1 Tube", "1 Tube", "1 Tube", "-", "1 Tube", "1 Tube", "NSAID topikal lini pertama OA Genu. Absorpsi sistemik sangat rendah (<6%), aman untuk ginjal dan TD."),
    ("Meloxicam Tab", "7.5 mg", "Oral", "2x1 (Mei) / 1x1 (Jun) prn nyeri", "-", "7.5 mg (10)", "7.5 mg (10)", "-", "-", "-", "NSAID sistemik diberikan saat nyeri hebat. Waspada interaksi nefrotoksik & hipertensi!"),
    ("Kalium Diklofenak Tab", "50 mg", "Oral", "2x1 tab prn nyeri (10 tab)", "-", "-", "-", "-", "50 mg (10)", "-", "NSAID sistemik onset cepat diberikan saat eksaserbasi nyeri sendi lutut September 2026."),
    ("Flunarizine Tab", "5 mg", "Oral", "2x1 tab (10 tab) utk pusing", "-", "-", "-", "-", "5 mg (10)", "-", "Antivertigo central origin diberikan saat keluhan ngliyer hebat September 2026.")
]

for item in rx_data:
    row += 1
    for idx, val in enumerate(item):
        cell = ws.cell(row, idx+1, val)
        cell.font = font_bold if idx == 0 else font_regular
        cell.alignment = align_left if idx in [0, 3, 10] else align_center
        if val not in ["-", ""] and idx in [4, 5, 6, 7, 8, 9]:
            cell.fill = fill_green_light
        cell.border = border_all_thin

# Section 5: MMAS-8 Adherence Evaluation
row += 2
ws.merge_cells(f"A{row}:K{row}")
ws[f"A{row}"] = "V. PENILAIAN TINGKAT KEPATUHAN PASIEN (MORISKY MEDICATION ADHERENCE SCALE - MMAS-8)"
ws[f"A{row}"].font = font_sec_hdr
ws[f"A{row}"].fill = fill_navy
ws[f"A{row}"].alignment = align_left

row += 1
mmas_headers = ["No", "Item Pertanyaan Kuesioner MMAS-8 (Morisky, 2008)", "Pilihan Jawaban Pasien", "Skor Kepatuhan", "Rasional Klinis & Analisis Kepatuhan Berdasarkan Data Pengobatan Pasien"]
mmas_spans = [1, 5, 1, 1, 3]

curr_col = 1
for idx, h in enumerate(mmas_headers):
    span = mmas_spans[idx]
    if span > 1:
        ws.merge_cells(start_row=row, start_column=curr_col, end_row=row, end_column=curr_col+span-1)
    cell = ws.cell(row, curr_col, h)
    cell.font = font_tbl_hdr
    cell.fill = fill_blue_light
    cell.alignment = align_center
    for c in range(curr_col, curr_col+span):
        ws.cell(row, c).border = border_all_thin
    curr_col += span

mmas_questions = [
    ("1", "Apakah Anda kadang-kadang lupa minum obat untuk penyakit Anda?", "Tidak", "1", "Pasien memiliki riwayat pengambilan obat rutin setiap bulan di apotek rawat jalan."),
    ("2", "Orang kadang tidak sempat minum obat bukan karena lupa. Dalam 2 minggu terakhir, pernahkah Anda sengaja tidak minum obat?", "Tidak", "1", "Pasien menyadari memiliki komorbiditas kronis (DM, HT, Jantung, Sendi)."),
    ("3", "Pernahkah Anda sengaja mengurangi atau menghentikan obat tanpa memberitahu dokter karena merasa kondisi bertambah parah?", "Tidak", "1", "Tidak ada riwayat penghentian obat sepihak; kepatuhan kontrol ke dokter spesialis sangat tertib."),
    ("4", "Ketika Anda bepergian atau meninggalkan rumah, apakah kadang-kadang lupa membawa obat Anda?", "Ya", "0", "Faktor geriatri (64 th) dengan polifarmasi 7-9 macam obat sering menyulitkan saat bepergian."),
    ("5", "Apakah kemarin Anda lupa meminum obat Anda?", "Tidak", "1", "Rutin diminum dibantu pengingat keluarga di rumah."),
    ("6", "Ketika Anda merasa sehat / keluhan berkurang, apakah kadang Anda berhenti minum obat?", "Ya", "0", "Obat analgetik PRN (Meloxicam/Diklofenak) diminum on-off saat nyeri kambuh saja."),
    ("7", "Minum obat setiap hari tidak menyenangkan bagi sebagian orang. Apakah Anda merasa terbebani dengan kewajiban minum obat rutin?", "Ya", "0", "Polifarmasi kompleks (sebelum makan, suapan pertama, sesudah makan, malam) memicu beban psikologis / pill burden."),
    ("8", "Seberapa sering Anda mengalami kesulitan untuk mengingat meminum semua obat Anda?\n(A. Tidak pernah=1; B. Sekali-kali=0.75; C. Kadang-kadang=0.5; D. Sering=0.25; E. Selalu=0)", "C. Kadang-kadang", "0.5", "Pasien kadang bingung membedakan waktu minum Glimepirid (sebelum makan) vs Acarbose (saat suapan pertama) vs Sitagliptin (sesudah makan).")
]

for item in mmas_questions:
    row += 1
    curr_col = 1
    for idx, val in enumerate(item):
        span = mmas_spans[idx]
        if span > 1:
            ws.merge_cells(start_row=row, start_column=curr_col, end_row=row, end_column=curr_col+span-1)
        cell = ws.cell(row, curr_col, val)
        cell.font = font_bold if idx in [0, 3] else font_regular
        cell.alignment = align_left if idx in [1, 4] else align_center
        if idx == 3 and float(val) < 1.0:
            cell.fill = fill_yellow_light
        for c in range(curr_col, curr_col+span):
            ws.cell(row, c).border = border_all_thin
        curr_col += span

# MMAS Summary Row
row += 1
ws.merge_cells(f"A{row}:G{row}")
ws[f"A{row}"] = "TOTAL SKOR MMAS-8 PASIEN : 5.5 / 8.0 (TINGKAT KEPATUHAN SEDANG MENDEKATI RENDAH)"
ws[f"A{row}"].font = font_bold
ws[f"A{row}"].fill = fill_yellow_light
ws[f"A{row}"].alignment = align_center

ws.cell(row, 8, "5.5").font = font_alert
ws.cell(row, 8).alignment = align_center
ws.cell(row, 8).fill = fill_yellow_light

ws.merge_cells(f"I{row}:K{row}")
ws[f"I{row}"] = "Kategori: Kepatuhan Sedang (Medium Adherence). Menjelaskan sebagian penyebab HbA1c 9.1% belum tercapai akibat kebingungan aturan minum multi-obat."
ws[f"I{row}"].font = font_regular
ws[f"I{row}"].alignment = align_left
for c in range(1, 12):
    ws.cell(row, c).border = border_all_thin

# Section 6: Comprehensive DRPs & Recommendations
row += 2
ws.merge_cells(f"A{row}:K{row}")
ws[f"A{row}"] = "VI. IDENTIFIKASI DRUG RELATED PROBLEMS (DRP), INTERAKSI OBAT, & REKOMENDASI KLINIS"
ws[f"A{row}"].font = font_sec_hdr
ws[f"A{row}"].fill = fill_navy
ws[f"A{row}"].alignment = align_left

row += 1
drp_headers = ["No", "Kategori DRP (PCNE / Cipolle)", "Obat Terkait", "Uraian Masalah Terkait Obat (DRP)", "Tingkat Signifikansi / Kategori Lexicomp", "Rekomendasi Farmasis & Solusi Guideline", "Parameter Monitoring & Target Terapi"]
drp_spans = [1, 1, 1, 2, 1, 3, 2]

curr_col = 1
for idx, h in enumerate(drp_headers):
    span = drp_spans[idx]
    if span > 1:
        ws.merge_cells(start_row=row, start_column=curr_col, end_row=row, end_column=curr_col+span-1)
    cell = ws.cell(row, curr_col, h)
    cell.font = font_tbl_hdr
    cell.fill = fill_blue_light
    cell.alignment = align_center
    for c in range(curr_col, curr_col+span):
        ws.cell(row, c).border = border_all_thin
    curr_col += span

drp_list = [
    ("1", "Dosis Terlalu Tinggi / Keamanan Geriatri", "Glimepirid 3 mg Tab", "Pasien geriatri (64 th) menerima dosis Glimepirid 6 mg/hari (3 mg 2x1). Glimepirid memiliki metabolit aktif yang diekskresi ginjal. Pada lansia dengan risiko penurunan eGFR, risiko hipoglikemia berat memanjang sangat tinggi, memicu pusing/sinkop dan trauma jatuh (CKR pada 04/07).", "Mayor / PIM (AGS Beers Criteria 2023 & PERKENI 2021)", "Turunkan dosis Glimepirid menjadi 2 mg 1x1 pagi hari, atau beralih ke sulfonilurea bersihan hati (Glikuidon 30 mg 2-3x1) atau inisiasi Insulin Basal sesuai algoritma PERKENI.", "GDS harian, gejala hipoglikemia (tremor, lemas, keringat dingin), target GDP 80-130 mg/dL."),
    ("2", "Pemilihan Obat Belum Optimal / Indikasi Belum Terpenuhi", "Terapi DM Tipe 2 (Glimepirid + Sitagliptin + Acarbose)", "Kegagalan terapi kombinasi 3 OHO oral. HbA1c pasien tetap 9.1% (target <7.0%) dan GDP 151-190 mg/dL. Beta-cell failure lanjut membutuhkan suplementasi insulin eksogen.", "Mayor (PB PERKENI 2021 Hal. 45-50 & ADA 2024)", "Rekomendasikan inisiasi Insulin Basal (Glargine / Detemir / Degludec) dosis awal 10 unit atau 0.1-0.2 U/kgBB (5-10 unit) malam hari menjelang tidur, dikombinasikan dengan OHO.", "HbA1c setiap 3 bulan (target 7.0 - 8.0% pada lansia), GDP pagi hari (target 80-130 mg/dL)."),
    ("3", "Penyesuaian Dosis Organ (Gangguan Ginjal)", "Sitagliptin 100 mg Tab", "Pada 04-07-2026 kadar kreatinin melonjak 2.69 mg/dL (CrCl Cockcroft-Gault 17.67 mL/min). 80% Sitagliptin diekskresikan ginjal. Bila eGFR < 45 mL/min, dosis 100 mg berisiko akumulasi.", "Moderat (Lexicomp & FDA Prescribing Info)", "Evaluasi hasil lab Kreatinin ulang (order 06/11/2026). Jika eGFR 30-44 mL/min, sesuaikan dosis menjadi 50 mg 1x1; jika eGFR < 30 mL/min, sesuaikan menjadi 25 mg 1x1.", "Serum kreatinin berkala, perhitungan eGFR / CrCl, monitoring keluhan GI / pankreatitis."),
    ("4", "Interaksi Obat - Obat (DDI)", "NSAID (Meloxicam / Diklofenak) + Amlodipin", "NSAID menghambat prostaglandin vasodilator ginjal, mereduksi aliran darah ginjal, retensi natrium/air, dan menumpulkan efikasi antihipertensi Amlodipin (TD pasien naik ke 156-165 mmHg).", "Kategori C (Lexicomp) / Nefrotoksik", "Hentikan pemberian NSAID oral sistemik rutin. Maksimalkan analgesik topikal Flamar Gel 2-4x sehari yang absorpsi sistemiknya sangat minimal (<6%) dan aman bagi ginjal & TD.", "Tekanan darah berkala (target <130/80 mmHg), fungsi ginjal (Ureum/Kreatinin), edema perifer."),
    ("5", "Interaksi Obat - Obat (DDI)", "NSAID (Meloxicam / Diklofenak) + Glimepirid", "NSAID dapat menggeser ikatan protein plasma sulfonilurea dan menghambat ekskresi renalnya, meningkatkan konsentrasi bebas glimepirid dan memperparah risiko hipoglikemia.", "Kategori C (Lexicomp)", "Hindari kombinasi; jika pasien membutuhkan analgesik oral untuk eksaserbasi nyeri sendi, utamakan Parasetamol 500-1000 mg prn (maks 3000 mg/hari).", "Tanda-tanda hipoglikemia akut, kepatuhan makan teratur sesudah obat."),
    ("6", "Interaksi Obat - Obat (DDI) & Risiko Jatuh", "Gabapentin 100 mg + Flunarizine 5 mg", "Kombinasi dua depresan SSP meningkatkan efek sedasi, somnolence, pusing melayang, dan ataxia pada lansia, secara drastis meningkatkan risiko jatuh berulang.", "Kategori C (Lexicomp) / Geriatric Alert", "Batasi penggunaan Flunarizine maksimal 1-2 minggu hanya untuk mengatasi episode vertigo akut; berikan Gabapentin hanya pada malam hari sebelum tidur; edukasi ambulasi aman.", "Tingkat kesadaran, rasa kantuk siang hari, skrining risiko jatuh (fall risk)."),
    ("7", "Aturan Pakai Obat Khusus (Drug-Food)", "Acarbose 100 mg Tab", "Acarbose bekerja dengan menghambat enzim alfa-glukosidase di brush border usus halus. Jika diminum sebelum/sesudah makan, efektivitas menurunkan glukosa postprandial hilang.", "Signifikan (Farmakologi Klinis)", "Konseling dan edukasi pasien: Acarbose WAJIB diminum bersama suapan pertama makanan utama. CRITICAL: Hipoglikemia saat konsumsi Acarbose HARUS diatasi dengan Dextrose/Glukosa murni (bukan gula pasir).", "Glukosa Darah 2 Jam PP (target <180 mg/dL), keluhan GI (kembung, flatus, diare)."),
    ("8", "Sub-optimal Monoterapi Hipertensi", "Amlodipin 10 mg Tab", "Monoterapi Amlodipin 10 mg belum mampu mengontrol TD pasien (TD berkisar 133-165 mmHg). Pasien DM + CKD memerlukan terapi kombinasi untuk target renoprotektif.", "Mayor (PERHI 2021 & KDIGO 2024)", "Rekomendasikan kombinasi lini pertama: Amlodipin 5-10 mg + ARB (Candesartan 8-16 mg atau Telmisartan 40-80 mg). ARB memberikan proteksi kardiorenal dan mengatasi edema perifer Amlodipin.", "Tekanan darah terukur (target <130/80 mmHg), kadar kalium serum dan kreatinin setelah inisiasi ARB.")
]

for item in drp_list:
    row += 1
    curr_col = 1
    for idx, val in enumerate(item):
        span = drp_spans[idx]
        if span > 1:
            ws.merge_cells(start_row=row, start_column=curr_col, end_row=row, end_column=curr_col+span-1)
        cell = ws.cell(row, curr_col, val)
        cell.font = font_bold if idx in [0, 4] else font_regular
        cell.alignment = align_left if idx in [1, 2, 3, 5, 6] else align_center
        if "Mayor" in val or "PIM" in val:
            cell.fill = fill_red_light
            cell.font = font_alert
        elif "Moderat" in val or "Kategori C" in val:
            cell.fill = fill_yellow_light
        for c in range(curr_col, curr_col+span):
            ws.cell(row, c).border = border_all_thin
        curr_col += span

# Section 7: SOAP Form
row += 2
ws.merge_cells(f"A{row}:K{row}")
ws[f"A{row}"] = "VII. DOKUMENTASI SOAP (SUBJECTIVE, OBJECTIVE, ASSESSMENT, PLAN) ASUHAN KEFARMASIAN RAWAT JALAN"
ws[f"A{row}"].font = font_sec_hdr
ws[f"A{row}"].fill = fill_navy
ws[f"A{row}"].alignment = align_left

soap_sections = [
    ("SUBJECTIVE (S)", "Pasien Ny. Sri Wisraya (64 tahun) datang rutin kontrol bulanan ke Poli Penyakit Dalam RSPAU dr. S. Hardjolukito. Keluhan utama yang dirasakan adalah nyeri pada sendi lutut kanan dan kiri (OA Genu Bilateral) terutama saat digerakkan atau berjalan, kaki kaku dan kebas/kesemutan (neuropati diabetik), serta episode pusing berputar/gliyer (vertigo central origin). Pasien memiliki riwayat rawat inap di IGD pada 04-07-2026 akibat trauma kepala ringan (CKR) dan fraktur os zygomaticum linier sinistra akibat jatuh di rumah. Pasien rutin meminum obat kronis namun merasa sedikit terbebani dengan jumlah obat yang banyak (7-9 macam obat sehari dengan aturan minum bervariasi)."),
    ("OBJECTIVE (O)", "1. Tanda-Tanda Vital (07-10-2026): TD 133/77 mmHg (tertinggi 165/89 mmHg pada 05/08), Nadi 85 x/mnt, RR 20 x/mnt, Suhu 36.0°C, SpO2 99%, BB 52 kg, TB 156 cm, IMT 21.37 kg/m² (Normoweight).\n2. Data Laboratorium (Tren 6 Bulan): HbA1c 9.1% (High), GDP 151 - 190 mg/dL (High), GD2PP 211 mg/dL (High), GDS berfluktuasi 158 - 308 mg/dL. Darah rutin (04/07): Hb 10.1 g/dL, Ht 30%, Leukosit normal, Trombosit 228.000/mm³. Fungsi Ginjal: Ureum 73 mg/dL, Kreatinin 2.69 mg/dL (CrCl Cockcroft-Gault 17.67 mL/min pada 04/07); dokter menjadwalkan periksa ulang GDP, Kreatinin, dan LDL pada 06-11-2026. Fungsi Hati: SGOT 29 U/L, SGPT 20 U/L (Normal).\n3. Radiologi: Foto Pelvis AP (16/05/2026): Periarticular calcification hip dextra. CT Scan Kepala (04/07/2026): Hematoma zygomaticum s.d frontalis sinistra, fraktur linier os zygomaticum & frontalis sinistra, hematosinus maksilaris sinistra.\n4. Kepatuhan (MMAS-8): Skor 5.5 / 8.0 (Kepatuhan Sedang / Medium Adherence)."),
    ("ASSESSMENT (A)", "1. Diabetes Melitus Tipe 2 Tidak Terkontrol (HbA1c 9.1%, GDP 151-190 mg/dL) mengalami kegagalan terapi kombinasi 3 OHO (Glimepirid 6 mg + Sitagliptin 100 mg + Acarbose 200 mg). Indikasi inisiasi Insulin Basal sesuai algoritma PB PERKENI 2021.\n2. Overdosis Relatif Glimepirid pada Geriatri: Dosis 6 mg/hari (3 mg 2x1) pada wanita 64 th dengan risiko penurunan fungsi ginjal berisiko tinggi memicu hipoglikemia tersembunyi berkepanjangan dan trauma jatuh (PIM Beers Criteria 2023).\n3. Potensi Toksisitas Sitagliptin pada Gangguan Ginjal: Sitagliptin 100 mg/hari belum disesuaikan dengan nilai eGFR pasien paska episode kreatinin 2.69 mg/dL (seharusnya 50 mg atau 25 mg bila eGFR < 45 mL/min).\n4. Hipertensi Belum Terkontrol Optimal (Target PERHI <130/80 mmHg): Monoterapi Amlodipin 10 mg belum adekuat dan kehilangan efikasi akibat interaksi dengan NSAID oral.\n5. Osteoarthritis Genu Refrakter & Risiko Nefrotoksisitas NSAID: Penggunaan NSAID oral sistemik (Meloxicam 7.5 mg, Kalium Diklofenak 50 mg) tanpa gastroprotektor membahayakan fungsi ginjal, memicu retensi cairan, dan menumpulkan antihipertensi.\n6. Risiko Jatuh Geriatri (Fall Risk): Interaksi aditif sedasi antara Gabapentin 100 mg + Flunarizine 5 mg meningkatkan risiko kecelakaan jatuh berulang paska CKR.\n7. Switch Statin Tepat: Pengalihan dari Rosuvastatin 10 mg ke Atorvastatin 20 mg pada Oktober 2026 dinilai sangat tepat dari segi keamanan ginjal."),
    ("PLAN & REKOMENDASI (P)", "1. Rekomendasikan kepada DPJP untuk menginisiasi Insulin Basal (Glargine 10 unit malam hari) guna mengatasi glukotoksisitas (HbA1c 9.1%) sesuai PERKENI 2021.\n2. Turunkan dosis Glimepirid dari 6 mg menjadi 2 mg 1x1 pagi hari (atau ganti ke Glikuidon 30 mg 2-3x1 / stop jika insulin basal dimulai) untuk mencegah hipoglikemia berat.\n3. Evaluasi hasil kreatinin serum ulang (order 06/11/2026); jika eGFR < 45 mL/min, sesuaikan dosis Sitagliptin menjadi 50 mg 1x1 pagi.\n4. Hentikan NSAID oral sistemik (Meloxicam & Kalium/Natrium Diklofenak). Maksimalkan Flamar Gel topikal 2-4x sehari pada kedua lutut. Bila nyeri hebat, gunakan Parasetamol 500-1000 mg prn.\n5. Optimalkan terapi hipertensi dengan kombinasi Amlodipin 5-10 mg + ARB (Candesartan 8-16 mg) untuk target renoprotektif dan kontrol TD < 130/80 mmHg.\n6. Batasi durasi Flunarizine maksimal 10 hari; edukasi keluarga mengenai pencegahan jatuh di rumah (pencahayaan cukup, pegangan kamar mandi, alas kaki antislip).\n7. Konseling Farmasi: Edukasi cara minum Acarbose saat suapan pertama makanan, serta penyediaan sediaan glukosa murni (Dextrose) untuk penanganan hipoglikemia darurat.\n8. Sediakan Pill-Box Organizer harian berlabel waktu (Pagi, Siang, Malam, Sebelum Tidur) untuk meningkatkan kepatuhan pasien dari skor 5.5 menuju skor 8.0.")
]

for title, content in soap_sections:
    row += 1
    ws.merge_cells(f"A{row}:K{row}")
    ws[f"A{row}"] = title
    ws[f"A{row}"].font = font_subtitle
    ws[f"A{row}"].fill = fill_blue_light
    ws[f"A{row}"].border = border_all_thin
    
    row += 1
    ws.merge_cells(f"A{row}:K{row}")
    ws[f"A{row}"] = content
    ws[f"A{row}"].font = font_regular
    ws[f"A{row}"].alignment = align_left
    ws[f"A{row}"].border = border_all_thin

# Auto-adjust column widths
ws.column_dimensions['A'].width = 24
ws.column_dimensions['B'].width = 16
ws.column_dimensions['C'].width = 18
ws.column_dimensions['D'].width = 16
ws.column_dimensions['E'].width = 16
ws.column_dimensions['F'].width = 16
ws.column_dimensions['G'].width = 16
ws.column_dimensions['H'].width = 16
ws.column_dimensions['I'].width = 16
ws.column_dimensions['J'].width = 20
ws.column_dimensions['K'].width = 30

excel_out_path = r"D:\FILE NINIS\PTO_RAJAL_LENGKAP_SRI_WISRAYA.xlsx"
excel_copy_path = r"D:\FILE NINIS\PTO RAJAL\PTO_RAJAL_LENGKAP_SRI_WISRAYA.xlsx"

wb.save(excel_out_path)
shutil.copyfile(excel_out_path, excel_copy_path)

print(f"Excel created successfully at:")
print(f"1. {excel_out_path} ({os.path.getsize(excel_out_path)} bytes)")
print(f"2. {excel_copy_path} ({os.path.getsize(excel_copy_path)} bytes)")

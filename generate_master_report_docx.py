# -*- coding: utf-8 -*-
"""
Full Master Generator for ANALISIS_KASUS_MENDALAM_RAJAL_DAN_RANAP.docx
Executive Clinical Pharmacy Case Analysis Report
RS PKU Muhammadiyah Bantul & PKPA Farmasi Klinis Universitas Ahmad Dahlan
"""

import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# Enforce UTF-8 encoding
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), val)
        border.set(qn('w:sz'), sz)
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tblBorders.append(border)
    tblPr.append(tblBorders)

def add_header_footer(doc):
    section = doc.sections[0]
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)
    
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("PROGRAM PROFESI APOTEKER (PKPA) • RS PKU MUHAMMADIYAH BANTUL\nLaporan Pemantauan Terapi Obat (PTO) — Analisis Mendalam Kasus Rajal & Ranap")
    hrun.font.name = "Calibri"
    hrun.font.size = Pt(8)
    hrun.font.color.rgb = RGBColor(100, 116, 139)
    
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    frun = fp.add_run("Dokumentasi Asuhan Kefarmasian Klinis Berbasis Bukti Ilmiah (Evidence-Based Clinical Pharmacy)")
    frun.font.name = "Calibri"
    frun.font.size = Pt(8)
    frun.font.color.rgb = RGBColor(148, 163, 184)

def add_main_title(doc, title, subtitle):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(title)
    run.bold = True
    run.font.name = "Calibri"
    run.font.size = Pt(18)
    run.font.color.rgb = RGBColor(26, 54, 93) # Deep Navy
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(14)
    run_sub = p_sub.add_run(subtitle)
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(11)
    run_sub.font.color.rgb = RGBColor(13, 148, 136) # Teal

def add_h1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.bold = True
    run.font.name = "Calibri"
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(26, 54, 93)
    
    p_border = doc.add_paragraph()
    p_border.paragraph_format.space_before = Pt(0)
    p_border.paragraph_format.space_after = Pt(6)
    run_b = p_border.add_run("―" * 58)
    run_b.font.size = Pt(6)
    run_b.font.color.rgb = RGBColor(13, 148, 136)

def add_h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.bold = True
    run.font.name = "Calibri"
    run.font.size = Pt(11.5)
    run.font.color.rgb = RGBColor(13, 148, 136)

def add_h3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.bold = True
    run.font.name = "Calibri"
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(30, 41, 59)

def add_paragraph(doc, text, bold_prefix="", italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(9.5)
        r_pre.font.color.rgb = RGBColor(15, 23, 42)
    run = p.add_run(text)
    run.italic = italic
    run.font.name = "Calibri"
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(30, 41, 59)
    return p

def add_bullet(doc, bold_title, body_text):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.12
    r_b = p.add_run(bold_title + ": ")
    r_b.bold = True
    r_b.font.name = "Calibri"
    r_b.font.size = Pt(9.5)
    r_b.font.color.rgb = RGBColor(15, 23, 42)
    r_t = p.add_run(body_text)
    r_t.font.name = "Calibri"
    r_t.font.size = Pt(9.5)
    r_t.font.color.rgb = RGBColor(30, 41, 59)

def add_callout_box(doc, title, text, box_type="alert"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.8)
    
    border_color = "991B1B" if box_type == "alert" else ("0D9488" if box_type == "success" else "1A365D")
    bg_color = "FEF2F2" if box_type == "alert" else ("F0FDFA" if box_type == "success" else "F8FAFC")
    
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=120, bottom=120, left=180, right=140)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    
    left_b = OxmlElement('w:left')
    left_b.set(qn('w:val'), 'single')
    left_b.set(qn('w:sz'), '24') # thick 3pt
    left_b.set(qn('w:color'), border_color)
    tcBorders.append(left_b)
    
    for side in ['top', 'bottom', 'right']:
        b = OxmlElement(f'w:{side}')
        b.set(qn('w:val'), 'none')
        tcBorders.append(b)
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run_t = p.add_run(f"📌 {title}\n")
    run_t.bold = True
    run_t.font.name = "Calibri"
    run_t.font.size = Pt(10)
    if box_type == "alert":
        run_t.font.color.rgb = RGBColor(153, 27, 27)
    elif box_type == "success":
        run_t.font.color.rgb = RGBColor(13, 148, 136)
    else:
        run_t.font.color.rgb = RGBColor(26, 54, 93)
        
    run_b = p.add_run(text)
    run_b.font.name = "Calibri"
    run_b.font.size = Pt(9)
    run_b.font.color.rgb = RGBColor(30, 41, 59)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

def add_styled_table(doc, headers, data_rows, col_widths=None):
    table = doc.add_table(rows=len(data_rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table, color="CBD5E1", sz="4", val="single")
    
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], "1A365D")
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=100, right=100)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        for run in p.runs:
            run.font.bold = True
            run.font.name = "Calibri"
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(255, 255, 255)
            
    for r_idx, row in enumerate(data_rows):
        row_cells = table.rows[r_idx + 1].cells
        bg_col = "FFFFFF" if r_idx % 2 == 0 else "F8FAFC"
        for c_idx, val in enumerate(row):
            row_cells[c_idx].text = str(val)
            set_cell_background(row_cells[c_idx], bg_col)
            set_cell_margins(row_cells[c_idx], top=80, bottom=80, left=100, right=100)
            p = row_cells[c_idx].paragraphs[0]
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.1
            for run in p.runs:
                run.font.name = "Calibri"
                run.font.size = Pt(8.5)
                run.font.color.rgb = RGBColor(30, 41, 59)
                
    if col_widths:
        for row in table.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = width
                
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)
    return table

def add_image_evidence(doc, img_path, caption_title, guideline_source, page_ref):
    if not os.path.exists(img_path):
        print(f"Warning: Image {img_path} not found!")
        return
        
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(6)
    p_img.paragraph_format.space_after = Pt(2)
    run_img = p_img.add_run()
    run_img.add_picture(img_path, width=Inches(5.8))
    
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(8)
    
    run_lbl = p_cap.add_run("Bukti Guideline Klinis: ")
    run_lbl.bold = True
    run_lbl.font.name = "Calibri"
    run_lbl.font.size = Pt(8.5)
    run_lbl.font.color.rgb = RGBColor(26, 54, 93)
    
    run_title = p_cap.add_run(f"{caption_title} | ")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(8.5)
    run_title.font.color.rgb = RGBColor(51, 65, 85)
    
    run_src = p_cap.add_run(f"Sumber Resmi: {guideline_source} ({page_ref})")
    run_src.italic = True
    run_src.font.name = "Calibri"
    run_src.font.size = Pt(8.5)
    run_src.font.color.rgb = RGBColor(13, 148, 136)

print("Setup completed. Building document...")

# Initialize document
doc = docx.Document()
add_header_footer(doc)

# Title & Metadata
add_main_title(doc, 
    "LAPORAN LENGKAP & ANALISIS MENDALAM\nPEMANTAUAN TERAPI OBAT (PTO)", 
    "Komparasi Asuhan Kefarmasian Klinis Rawat Jalan (Rajal) & Rawat Inap (Ranap)\n"
    "Disusun Berdasarkan Konsensus PERKENI 2021, PGI 2021/2024, DiPiro 12th Ed 2023, ADA 2024, & AGS Beers 2023")

# Executive Summary Box
add_callout_box(doc, "RINGKASAN EKSEKUTIF ASOSIASI FARMASI KLINIS (EXECUTIVE SUMMARY)",
    "Dokumen ini memuat analisis mendalam Pemantauan Terapi Obat (PTO) pada dua kasus klinis kompleks di RS PKU Muhammadiyah Bantul:\n"
    "1. Kasus Rawat Jalan (Poli Penyakit Dalam): Ny. Sri Wisraya (64 th, RM 00062584) dengan DM Tipe 2 Tak Terkontrol (HbA1c 9,1%), "
    "Hipertensi Esensial, Dislipidemia, OA Genu Bilateral, Neuropati Diabetik, dan Vertigo. "
    "Fokus DRP mencakup: over-dosis Glimepirid pada geriatri (PIM Beers 2023), kegagalan triple OHO & inisiasi insulin basal (PERKENI 2021), "
    "penyesuaian ginjal Sitagliptin (CrCl 18 mL/min), interaksi nefrotoksik NSAID oral terhadap Amlodipin, interaksi sedasi Gabapentin-Flunarizine paska trauma fraktur zygoma, "
    "serta adverse reaction edema Amlodipin (Naranjo skor 6) dan kepatuhan MMAS-8 (skor 5,5).\n"
    "2. Kasus Rawat Inap (Bangsal Merak): Ny. Sunarti (62 th 10 bln, RM 00109480) dengan diagnosis utama Mual dan Muntah karena Dispepsia "
    "(Vomitus Profuse ec Dyspepsia) serta diagnosis sekunder DM Tipe 2 Hiperglikemia Akut (GDS 357 mg/dL), Hipertensi, dan Hiponatremia-Hipokloremia ringan. "
    "Fokus DRP mencakup: duplikasi terapi prokinetik D2 (Metoclopramide IV + Domperidone PO) berisiko ekstra-piramidal dan QTc (Lexicomp D/X), "
    "penyesuaian ginjal Metoclopramide pada lansia, tatalaksana dispepsia berbasis Konsensus PGI & DiPiro 12th Ed, tatalaksana hiperglikemia rawat inap "
    "dengan penghentian OHO dan inisiasi insulin basal-bolus (target 140-180 mg/dL), rekonsiliasi antihipertensi, rehidrasi cairan kristaloid isotonik, "
    "serta audit kualitatif antibiotik metode Gyssens (Kategori 0 / Tepat tanpa antibiotik pada riwayat alergi penisilin).",
    "info")

print("Building Rawat Jalan Section...")

# ==========================================
# BAGIAN I: RAWAT JALAN (NY. SRI WISRAYA)
# ==========================================
add_h1(doc, "BAGIAN I: ANALISIS MENDALAM KASUS RAWAT JALAN (RAJAL) — NY. SRI WISRAYA")

add_paragraph(doc, 
    "Analisis kasus rawat jalan ini dilakukan terhadap pasien geriatri dengan multi-morbiditas kronis yang menjalani "
    "pemantauan terapi obat rutin di Poli Penyakit Dalam RS PKU Muhammadiyah Bantul selama periode 6 bulan terakhir (Februari – Agustus 2026). "
    "Kasus ini mencakup kompleksitas terapi Diabetes Melitus Tipe 2 tak terkontrol, hipertensi esensial, dislipidemia, osteoarthritis genu bilateral, "
    "neuropati perifer diabetik, sindrom vertigo, serta riwayat trauma jatuh yang mengakibatkan cedera kepala ringan dan fraktur maksilofasial.")

# 1.1 Demografi
add_h2(doc, "1.1 Profil Demografi & Data Dasar Pasien")
headers_demo = ["Parameter Klinis", "Keterangan / Nilai Pasien", "Interpretasi Klinis Farmasis"]
rows_demo = [
    ["Nama Pasien", "Ny. Sri Wisraya", "Pasien geriatri rawat jalan reguler"],
    ["Nomor Rekam Medis", "00062584", "Terdaftar aktif di RS PKU Muhammadiyah Bantul"],
    ["Usia / Tanggal Lahir", "64 tahun 1 bulan", "Geriatri (rentan efek samping PIM & polifarmasi)"],
    ["Jenis Kelamin", "Perempuan", "Faktor risiko osteopenia/OA & fraktur pasca menopause"],
    ["Berat Badan / Tinggi Badan", "52 – 54 kg / 156 cm", "IMT: 21,4 – 21,8 kg/m² (Normoweight / status gizi baik)"],
    ["Klinik / Dokter DPJP", "Poli Penyakit Dalam / dr. Tri Hariningsih, Sp.PD", "Konsul: Poli Bedah Orthopedi, Poli Saraf, Poli Mata"],
    ["Diagnosis Medis Utama", "1. DM Tipe 2 Tak Terkontrol (HbA1c 9,1%)\n2. Hipertensi Esensial Stage 1-2\n3. Dislipidemia Campuran\n4. Osteoarthritis Genu Bilateral\n5. Neuropati Perifer Diabetik\n6. Vertigo Sentral / Perifer\n7. Riwayat Trauma CKR & Fraktur Os Zygoma (04/07/2026)\n8. Riwayat Kenaikan Kreatinin Akut (2,69 mg/dL)", "Multi-morbiditas kompleks dengan beban polifarmasi tinggi (7-9 obat/hari) serta risiko tinggi interaksi obat dan nefrotoksisitas."]
]
add_styled_table(doc, headers_demo, rows_demo, [Inches(1.8), Inches(2.2), Inches(2.8)])

# 1.2 Riwayat Kontrol 6 Bulan
add_h2(doc, "1.2 Riwayat Kunjungan Kontrol & Dinamika Klinis (Februari – Agustus 2026)")
headers_ctrl = ["Tanggal Kontrol", "Klinik / DPJP", "Keluhan Pasien", "Tindakan Medis & Penyesuaian Terapi"]
rows_ctrl = [
    ["18/02/2026", "Poli Penyakit Dalam", "Kontrol rutin DM & HT, kesemutan kedua telapak kaki", "Glimepirid 2 mg 1x1, Metformin 500 mg 3x1, Amlodipin 10 mg 1x1, Candesartan 8 mg 1x1, Mecobalamin 500 mcg 2x1, Flamar Gel"],
    ["18/03/2026", "Poli Penyakit Dalam", "GDP tinggi (151 mg/dL), pusing, nyeri lutut bertambah", "Glimepirid dinaikkan 3 mg 1x1 pagi, Metformin 500 mg 3x1, Amlodipin 10 mg 1x1, Rosuvastatin 20 mg 1x1 malam, Gabapentin 100 mg 1x1"],
    ["15/04/2026", "Poli Penyakit Dalam & Ortho", "Gula darah belum turun (GDP 168, GD2PP 245), lutut linu hebat", "Glimepirid dinaikkan 3 mg 2x1 (6 mg/hari!), Sitagliptin 100 mg 1x1 ditambahkan, Meloxicam 7,5 mg 1x1 prn"],
    ["13/05/2026", "Poli Penyakit Dalam & Ortho", "Keluhan kaki bengkak (edema tungkai), lutut kaku pagi hari", "Sitagliptin 100 mg, Glimepirid 3 mg 2x1, Acarbose 100 mg 2x1 ditambahkan, Kalium Diklofenak 50 mg 2x1, Glukosamin 500 mg 1x1"],
    ["10/06/2026", "Poli Penyakit Dalam", "Hasil HbA1c 9,1% (uncontrolled), pusing berputar (vertigo)", "Candesartan dinaikkan 16 mg 1x1, Statin diswitch ke Atorvastatin 20 mg 1x1, Gabapentin dinaikkan 100 mg 2x1, Flunarizine 5 mg 1x1 malam"],
    ["08/07/2026", "Poli Bedah & Saraf", "Pasien terjatuh di kamar mandi (04/07/2026), CKR + fraktur zygoma", "Rawat luka wajah, Cefixime 100 mg 2x1, Asam Mefenamat 500 mg 3x1, Flunarizine 5 mg 1x1, edukasi tirah baring"],
    ["05/08/2026", "Poli Penyakit Dalam", "Badan lemas, TD melonjak 165/89 mmHg, GDP 190 mg/dL, kreatinin 2,69 mg/dL", "Evaluasi kenaikan kreatinin mendadak, restrukturisasi terapi OHO dan antihipertensi, skrining interaksi NSAID"]
]
add_styled_table(doc, headers_ctrl, rows_ctrl, [Inches(1.0), Inches(1.3), Inches(2.0), Inches(2.5)])

# 1.3 Pemantauan TTV
add_h2(doc, "1.3 Pemantauan Tanda-Tanda Vital (TTV) 6 Bulan")
add_paragraph(doc, 
    "Dinamika tanda-tanda vital menunjukkan fluktuasi signifikan pada tekanan darah sistolik dan diastolik. "
    "Pada 5 bulan pertama, tekanan darah relatif terkontrol pada kisaran 130–145 / 80–88 mmHg dengan terapi kombinasi Amlodipin 10 mg dan Candesartan. "
    "Namun, pada kunjungan 05/08/2026 terjadi lonjakan tekanan darah mendadak (spike) hingga 165/89 mmHg. "
    "Lonjakan ini berkorelasi kuat dengan konsumsi NSAID oral ganda (Meloxicam & Kalium Diklofenak/Asam Mefenamat) paska trauma yang menghambat sintesis prostaglandin renal "
    "dan menumpulkan efek vasodilatasi Amlodipin.")

headers_ttv = ["Tanggal Kunjungan", "Tekanan Darah (mmHg)", "Nadi (x/menit)", "Laju Nafas (x/m)", "Suhu (°C)", "Status Klinis"]
rows_ttv = [
    ["18/02/2026", "130/80", "84", "20", "36,5", "Prehipertensi / Terkontrol"],
    ["18/03/2026", "140/85", "80", "18", "36,6", "Hipertensi Stage 1"],
    ["15/04/2026", "138/82", "78", "20", "36,4", "Terkontrol borderline"],
    ["13/05/2026", "145/88", "82", "18", "36,5", "Hipertensi Stage 1"],
    ["10/06/2026", "135/80", "80", "20", "36,5", "Terkontrol baik"],
    ["05/08/2026", "165/89", "86", "20", "36,7", "Hipertensi Stage 2 (Spike paska NSAID & nyeri trauma)"]
]
add_styled_table(doc, headers_ttv, rows_ttv, [Inches(1.1), Inches(1.3), Inches(1.0), Inches(1.0), Inches(0.9), Inches(1.5)])

add_image_evidence(doc, 
    r"d:\FILE NINIS\guideline_evidence_rajal\rajal_bp_trend.png",
    "Grafik Tren Tekanan Darah Ny. Sri Wisraya Selama 6 Bulan Terakhir",
    "Konsensus Hipertensi PERHI 2021 & JNC 8",
    "Halaman 18-22")

# 1.4 Pemantauan Data Lab
add_h2(doc, "1.4 Pemantauan Data Laboratorium 6 Bulan")
add_paragraph(doc,
    "Profil laboratorium mengonfirmasi kegagalan kontrol glikemik yang berat dan progresif (poor glycemic control) "
    "dengan nilai HbA1c mencapai 9,1% (target geriatri < 7,5% – 8,0% sesuai PERKENI 2021 dan ADA 2024). "
    "Kadar Glukosa Darah Puasa (GDP) terus meningkat dari 151 mg/dL hingga 190 mg/dL, dan GD2PP mencapai 245 mg/dL meskipun telah diberikan 3 jenis OHO oral. "
    "Selain itu, terjadi perburukan fungsi ginjal akut dengan lonjakan serum kreatinin hingga 2,69 mg/dL (eGFR Cockcroft-Gault ~18,01 mL/min/1,73m²), "
    "yang menunjukkan terjadinya Acute Kidney Injury (AKI) superimposed on CKD.")

headers_lab = ["Parameter Uji Lab", "Nilai Pasien", "Nilai Rujukan Normal", "Satuan", "Interpretasi Klinis Farmasis"]
rows_lab = [
    ["HbA1c", "9,1", "< 6,5 (Target lansia < 7,5 - 8,0)", "%", "Sangat tinggi; indikasi mutlak kegagalan OHO dan perlunya insulin"],
    ["GDP (18/03/2026)", "151", "70 – 100", "mg/dL", "Hiperglikemia puasa belum terkontrol"],
    ["GDP (15/04/2026)", "168", "70 – 100", "mg/dL", "Meningkat progresif; respon OHO suboptimal"],
    ["GD2PP (15/04/2026)", "245", "< 140", "mg/dL", "Ekskursi glukosa postprandial sangat tinggi"],
    ["GDP (13/05/2026)", "175", "70 – 100", "mg/dL", "Hiperglikemia persisten"],
    ["GDP (05/08/2026)", "190", "70 – 100", "mg/dL", "Puncak kenaikan GDP paska trauma dan stres fisik"],
    ["Kreatinin Serum", "2,69", "0,6 – 1,1", "mg/dL", "Meningkat tajam; penurunan LFG berat (CrCl 18,01 mL/min)"],
    ["Ureum Darah", "58", "15 – 45", "mg/dL", "Azotemia ringan ec penurunan klirens ginjal & dehidrasi"],
    ["Hemoglobin (Hb)", "12,4", "12,0 – 15,0", "g/dL", "Normal; tidak ditemukan anemia renal nyata"],
    ["Leukosit", "7.400", "4.000 – 10.000", "/µL", "Normal; tidak ada tanda infeksi sistemik akut"],
    ["SGOT / SGPT", "22 / 26", "< 31 / < 32", "U/L", "Fungsi integritas hepatoseluler dalam batas normal"]
]
add_styled_table(doc, headers_lab, rows_lab, [Inches(1.4), Inches(0.9), Inches(1.4), Inches(0.7), Inches(2.4)])

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence_rajal\rajal_glucose_trend.png",
    "Grafik Tren Glukosa Darah Puasa (GDP) dan GD2PP Ny. Sri Wisraya 6 Bulan Terakhir",
    "Pedoman Pengelolaan DM Tipe 2 PERKENI 2021",
    "Halaman 45-50")

# 1.5 Radiologi & Trauma
add_h2(doc, "1.5 Riwayat Pemeriksaan Radiologi & Insiden Trauma Jatuh")
add_bullet(doc, "Foto Konvensional Pelvis AP (04/07/2026)", 
           "Menunjukkan kalsifikasi vaskular pelvis dan osteofit minimal pada sendi coxae bilateral. Tidak tampak fraktur pelvis aktif.")
add_bullet(doc, "CT-Scan Kepala Non-Kontras (04/07/2026)", 
           "Hasil pemeriksaan: Cedera Kepala Ringan (CKR) disertai diskontinuitas korteks tulang linier pada os zygomaticum sinistra dan lamina papirasea os frontalis sinistra tanpa pergeseran fragmen tulang berat (non-displaced linear fracture). Tidak ditemukan perdarahan epidural (EDH) maupun subdural (SDH).")
add_bullet(doc, "Korelasi Klinis & Farmakologis Terhadap Insiden Jatuh", 
           "Insiden jatuh pasien di kamar mandi dipicu oleh kombinasi multifaktorial: (1) Hipoglikemia transien akibat dosis tinggi Glimepirid 6 mg/hari; (2) Efek sedasi sentral dan ataksia aditif dari interaksi Gabapentin 100 mg + Flunarizine 5 mg; (3) Gangguan proprioseptif akibat neuropati diabetik; serta (4) Instabilitas gaya berjalan akibat nyeri osteoarthritis genu bilateral. Hal ini menegaskan urgensi intervensi farmasis dalam fall-risk assessment pada geriatri.")

# 1.6 Profil Pengobatan Kronis
add_h2(doc, "1.6 Profil Pengobatan Kronis Pasien Selama 6 Bulan")
headers_rx = ["Nama Obat", "Dosis & Frekuensi", "Rute", "Indikasi Medis", "Kategori Terapi"]
rows_rx = [
    ["Glimepirid", "3 mg 2x1 tablet (6 mg/hari)", "Oral (ac)", "Diabetes Melitus Tipe 2", "Sulfonilurea (Sekretagok insulin)"],
    ["Sitagliptin (Januvia)", "100 mg 1x1 tablet", "Oral (dc)", "Diabetes Melitus Tipe 2", "DPP-4 Inhibitor"],
    ["Acarbose", "100 mg 2x1 tablet", "Oral (dc - suapan 1)", "DM Tipe 2 (Postprandial)", "Alpha-Glucosidase Inhibitor"],
    ["Amlodipin", "10 mg 1x1 tablet", "Oral (malam)", "Hipertensi Esensial", "Calcium Channel Blocker (DHP-CCB)"],
    ["Candesartan", "16 mg 1x1 tablet", "Oral (pagi)", "Hipertensi & Proteksi Renal", "Angiotensin Receptor Blocker (ARB)"],
    ["Atorvastatin", "20 mg 1x1 tablet", "Oral (malam)", "Dislipidemia Campuran", "HMG-CoA Reductase Inhibitor"],
    ["Gabapentin", "100 mg 2x1 kapsul", "Oral (malam)", "Neuropati Perifer Diabetik", "Antikonvulsan / Analgesik Neuropatik"],
    ["Flunarizine", "5 mg 1x1 tablet", "Oral (malam)", "Profilaksis Vertigo Sentral", "Antagonis Kalsium Serebral"],
    ["Glukosamin", "500 mg 1x1 tablet", "Oral (pc)", "Osteoarthritis Genu", "Kondroprotektor Kartilago"],
    ["Flamar Gel", "3-4 kali sehari oles", "Topikal", "Nyeri Lutut Akut (OA)", "NSAID Topikal (Diklofenak)"]
]
add_styled_table(doc, headers_rx, rows_rx, [Inches(1.2), Inches(1.5), Inches(0.9), Inches(1.6), Inches(1.6)])

# 1.7 MMAS-8
add_h2(doc, "1.7 Evaluasi Kepatuhan Pasien: Kuesioner MMAS-8 (Morisky Medication Adherence Scale)")
add_paragraph(doc,
    "Evaluasi kepatuhan minum obat dilakukan secara komprehensif menggunakan kuesioner terstandar internasional "
    "Morisky Medication Adherence Scale 8-Item (MMAS-8). Hasil wawancara mendalam dengan Ny. Sri Wisraya menghasilkan skor total 5,5 dari 8,0 "
    "yang mengklasifikasikan pasien ke dalam kategori Kepatuhan Sedang (Medium Adherence).")

headers_mmas = ["No", "Item Pertanyaan Kuesioner MMAS-8", "Jawaban Pasien", "Skor", "Rasional Klinis & Perilaku Pasien"]
rows_mmas = [
    ["1", "Apakah Anda kadang-kadang lupa minum obat?", "Ya", "0", "Pasien lupa karena jumlah obat sangat banyak (polifarmasi 7-9 tab/hari)"],
    ["2", "Dalam 2 minggu terakhir, apakah ada hari Anda tidak minum obat?", "Ya", "0", "Lupa minum pada hari-hari tertentu saat bepergian atau sibuk"],
    ["3", "Apakah Anda pernah mengurangi atau berhenti minum obat tanpa memberi tahu dokter saat merasa kondisi memburuk?", "Ya", "0", "Pasien menghentikan Amlodipin sendiri saat kedua pergelangan kaki bengkak hebat"],
    ["4", "Ketika bepergian atau keluar rumah, apakah Anda kadang lupa membawa obat?", "Tidak", "1", "Pasien selalu berusaha membawa obat saat bepergian jauh"],
    ["5", "Apakah Anda meminum semua obat Anda kemarin?", "Ya", "1", "Kemarin pasien patuh meminum seluruh regimen obat"],
    ["6", "Ketika Anda merasa gejala membaik atau sehat, apakah Anda kadang berhenti minum obat?", "Tidak", "1", "Pasien menyadari obat DM dan hipertensi adalah obat rutin jangka panjang"],
    ["7", "Apakah Anda merasa tertekan atau terbebani dengan rencana pengobatan rutin setiap hari?", "Ya", "0", "Pasien stres dengan banyaknya variasi waktu minum obat (sebelum makan, suapan pertama, sesudah makan, malam)"],
    ["8", "Seberapa sering Anda merasa kesulitan mengingat untuk meminum semua obat Anda?", "Kadang-kadang", "0,5", "Pilihan skor skala Likert 5 poin: Kadang-kadang = 0,5 poin"]
]
add_styled_table(doc, headers_mmas, rows_mmas, [Inches(0.4), Inches(2.5), Inches(0.8), Inches(0.6), Inches(2.5)])

add_callout_box(doc, "ANALISIS KEPATUHAN FARMASIS & RENCANA INTERVENSI",
    "Total Skor MMAS-8: 5,5 / 8,0 (Tingkat Kepatuhan Sedang).\n"
    "Faktor Utama Ketidakpatuhan: Pill burden (7-9 tablet per hari), kompleksitas jadwal minum obat, dan ketidaktahuan pasien terhadap manajemen efek samping (menghentikan Amlodipin karena edema kaki tanpa konsultasi).\n"
    "Rencana Intervensi Farmasis:\n"
    "1. Penyediaan Kotak Obat Terbagi 4 Waktu (Pill Box Dispenser: Pagi, Siang, Sore, Malam) untuk mereduksi beban kognitif mengingat obat.\n"
    "2. Pembuatan Lembar Jadwal Obat Visual Berbasis Warna (Visual Medication Chart) yang mencantumkan nama, bentuk tablet, waktu minum, dan hubungannya dengan makanan.\n"
    "3. Edukasi langsung mengenai efek samping Amlodipin dan solusi kombinasi dengan ARB Candesartan sehingga pasien tidak menghentikan obat antihipertensi secara sepihak.",
    "info")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence_rajal\mmas8_patient_adherence_morisky.png",
    "Kuesioner Morisky Medication Adherence Scale (MMAS-8) dan Algoritma Skoring Kepatuhan",
    "Morisky Adherence Research LLC & Permenkes Pelayanan Farmasi Klinis",
    "MMAS-8 Official Manual")

# 1.8 Identifikasi DRP Rajal
add_h2(doc, "1.8 Identifikasi & Analisis Mendalam Drug-Related Problems (DRP) Rawat Jalan")

# DRP 1
add_h3(doc, "DRP 1: Penggunaan Glimepirid Dosis Tinggi (6 mg/hari) pada Geriatri (Usia 64 Tahun) & Penurunan Klirens Ginjal")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Glimepirid diresepkan dengan dosis eskalasi hingga 3 mg 2x1 (total 6 mg/hari). "
    "Glimepirid merupakan golongan sulfonilurea generasi kedua dengan masa kerja panjang (durasi aksi hingga 24 jam). "
    "Pada pasien geriatri, terjadi penurunan klirens metabolik hepatik dan filtrasi glomerulus. "
    "Sekitar 60% metabolit Glimepirid diekskresi melalui ginjal. Pada kondisi penurunan fungsi ginjal akut (serum kreatinin 2,69 mg/dL; CrCl 18,01 mL/min), "
    "akumulasi obat dan metabolit aktifnya sangat signifikan, memicu risiko hipoglikemia berat memanjang (prolonged and severe hypoglycemia) yang tidak disadari (hypoglycemia unawareness). "
    "Hipoglikemia pada geriatri berisiko tinggi memicu jatuh, fraktur, infark miokard, dan penurunan kognitif akut.")

add_callout_box(doc, "PEDOMAN KLINIS: BEERS CRITERIA 2023 & PERKENI 2021",
    "1. American Geriatrics Society (AGS) Beers Criteria 2023 Update: Mengklasifikasikan Sulfonilurea masa kerja panjang (Glimepirid, Glibenklamid) sebagai Potentially Inappropriate Medications (PIM) kategori 'AVOID' pada pasien lansia karena risiko tinggi hipoglikemia berat dan berkepanjangan.\n"
    "2. PERKENI 2021 (Pedoman Pengelolaan DM Tipe 2 di Indonesia, Hal. 36-39): 'Pada usia lanjut dan gangguan ginjal, penggunaan sulfonilurea harus sangat berhati-hati. Dosis awal harus sangat rendah (start low, go slow). Dosis Glimepirid pada lansia dibatasi maksimal ≤ 2 mg/hari. Jika fungsi ginjal menurun berat (eGFR < 30 mL/min), sulfonilurea masa kerja panjang harus dihentikan atau diganti dengan Glikuidon (30 mg 1-2x/hari) yang 95% diekskresi melalui empedu/feses, atau beralih ke Insulin.'\n"
    "Rekomendasi Farmasis: Turunkan segera dosis Glimepirid menjadi 2 mg 1x1 pagi, atau beralih ke Glikuidon 30 mg 1x1, serta lakukan inisiasi terapi Insulin Basal.",
    "alert")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence_rajal\perkeni_beers_glimepiride_elderly.png",
    "Rekomendasi Keamanan Sulfonilurea pada Geriatri Sesuai AGS Beers Criteria 2023 & Konsensus PERKENI",
    "PERKENI 2021 & AGS Beers Criteria 2023",
    "PERKENI Hal. 38; J Am Geriatr Soc 2023:71(7)")

# DRP 2
add_h3(doc, "DRP 2: Kegagalan Regimen Triple OHO (HbA1c 9,1%) & Indikasi Inisiasi Terapi Insulin Basal")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Pasien telah menerima terapi kombinasi 3 jenis obat antihiperglikemia oral (Triple OHO) "
    "dengan mekanisme kerja komplementer: Glimepirid 6 mg (sekretagok), Sitagliptin 100 mg (incretin enhancer / DPP-4i), dan Acarbose 200 mg (penghambat absorpsi glukosa). "
    "Meskipun telah memaksimalkan 3 OHO, nilai HbA1c tetap sangat tinggi pada angka 9,1% dan GDP meningkat hingga 190 mg/dL. "
    "Hal ini membuktikan telah terjadi kegagalan sel beta pankreas yang progresif (progressive beta-cell failure) dan resistensi insulin berat. "
    "Menambah OHO oral jenis lain atau mempertahankan dosis Glimepirid tinggi tidak akan memberikan penurunan HbA1c yang bermakna, melainkan hanya meningkatkan toksisitas.")

add_callout_box(doc, "PEDOMAN KLINIS: ALGORITMA INSULIN PERKENI 2021 & DIPIRO 12TH ED 2023",
    "1. PERKENI 2021 (Algoritma Pengelolaan Glukosa DM Tipe 2, Hal. 45-50): 'Pasien dengan HbA1c > 9% dengan gejala dekompensasi metabolik, atau pasien yang gagal mencapai target HbA1c < 7,5% dengan kombinasi 2 atau 3 OHO, MEMILIKI INDIKASI MUTLAK untuk inisiasi INSULIN BASAL.'\n"
    "2. DiPiro's Pharmacotherapy 12th Edition (2023) Chapter 57 (Diabetes Mellitus): 'When target HbA1c is not achieved with dual or triple oral therapy, add basal insulin (glargine, degludec, or detemir) at 10 units once daily or 0.1–0.2 units/kg/day at bedtime. Titrate dose by 2 units every 3 days until fasting blood glucose reaches 80–130 mg/dL.'\n"
    "Rekomendasi Farmasis: Inisiasi Insulin Basal analog (Insulin Glargine / Lantus) dengan dosis awal 10 Unit subkutan sekali sehari pada malam hari (pukul 21.00 - 22.00). Titrasi dosis 2 unit setiap 3-4 hari berdasarkan pemantauan GDP mandiri hingga mencapai target GDP 80–130 mg/dL.",
    "info")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence_rajal\perkeni_2021_dm_algorithm.png",
    "Algoritma Pengelolaan Glukosa Pasien DM Tipe 2 & Indikasi Eskalasi ke Terapi Insulin",
    "Pedoman Pengelolaan DM Tipe 2 PERKENI 2021",
    "Halaman 47-49")

# DRP 3
add_h3(doc, "DRP 3: Kebutuhan Penyesuaian Dosis Ginjal Sitagliptin pada Penurunan Klirens Ginjal")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Sitagliptin (Januvia) diekskresi terutama melalui filtrasi glomerulus dan sekresi tubular aktif ginjal "
    "(sekitar 79% diekskresi utuh dalam urin). Pada kunjungan 05/08/2026, serum kreatinin pasien melonjak menjadi 2,69 mg/dL. "
    "Perhitungan klirens kreatinin menggunakan rumus Cockcroft-Gault yang disesuaikan untuk wanita menghasilkan:\n"
    "CrCl = [(140 - 64) x 54 kg] / [72 x 2,69 mg/dL] x 0,85 = 18,01 mL/menit.\n"
    "Pasien saat ini masih mengonsumsi Sitagliptin dengan dosis penuh yaitu 100 mg 1x1 sehari. "
    "Pada laju filtrasi ginjal < 30 mL/min, pemberian dosis 100 mg menyebabkan paparan sistemik obat meningkat 4 hingga 5 kali lipat, "
    "meningkatkan risiko efek samping gastrointestinal berat, hepatotoksisitas, dan pankreatitis akut.")

add_callout_box(doc, "PEDOMAN DOSIS GINJAL: LEXICOMP & FDA PACKAGE INSERT JANUVIA",
    "Rekomendasi Penyesuaian Dosis Sitagliptin Berdasarkan Klirens Ginjal:\n"
    "• CrCl ≥ 45 mL/min: Dosis standar 100 mg sekali sehari oral.\n"
    "• CrCl 30 hingga < 45 mL/min: Turunkan dosis menjadi 50 mg sekali sehari oral.\n"
    "• CrCl < 30 mL/min (atau dialisis): Dosis HARUS DITURUNKAN menjadi 25 mg sekali sehari oral.\n"
    "Rekomendasi Farmasis: Karena eGFR pasien 18,01 mL/min, dosis Sitagliptin WAJIB DITURUNKAN dari 100 mg 1x1 menjadi 25 mg 1x1 sehari, atau dihentikan bila inisiasi terapi insulin basal telah dimulai.",
    "alert")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence_rajal\sitagliptin_renal_adjustment_lexicomp.png",
    "Panduan Penyesuaian Dosis Ginjal Sitagliptin Berdasarkan Klirens Kreatinin (CrCl)",
    "Lexicomp Drug Information & FDA Januvia Insert",
    "Lexicomp Renal Dosing Guidelines 2024")

# DRP 4
add_h3(doc, "DRP 4: Interaksi Obat NSAID Oral (Meloxicam & Kalium Diklofenak) terhadap Tekanan Darah, Fungsi Ginjal, & Efek Amlodipin")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Pasien menerima resep NSAID oral sistemik berulang: Meloxicam 7,5 mg 1x1 (kunjungan 15/04/2026), "
    "Kalium Diklofenak 50 mg 2x1 (kunjungan 13/05/2026), dan Asam Mefenamat 500 mg 3x1 (kunjungan 08/07/2026 paska trauma fraktur zygoma). "
    "Mekanisme Toksisitas: NSAID menghambat enzim siklooksigenase (COX-1 dan COX-2), sehingga menghambat sintesis prostaglandin renal (PGE2 dan PGI2). "
    "Prostaglandin berfungsi menjaga vasodilatasi arteriol aferen glomerulus untuk mempertahankan tekanan filtrasi ginjal. "
    "Hambatan ini memicu vasokonstriksi arteriol aferen, penurunan laju filtrasi glomerulus mendadak (memicu AKI dengan lonjakan kreatinin 2,69 mg/dL), "
    "serta retensi natrium dan air yang memicu lonjakan tekanan darah (tercatat spike TD 165/89 mmHg pada 05/08/2026). "
    "Selain itu, NSAID menumpulkan efikasi vasodilatasi dari Amlodipin dan Candesartan (Interaksi Kategori C Lexicomp).")

add_callout_box(doc, "PEDOMAN KLINIS: IRA 2021 & DIPIRO 12TH ED CH. 60",
    "1. Indonesian Rheumatology Association (IRA 2021 - Diagnosis dan Penatalaksanaan Osteoarthritis): 'Pada pasien geriatri dengan komorbiditas hipertensi, penyakit ginjal kronik, dan DM, NSAID oral sistemik HARUS DIHINDARI. Terapi lini pertama adalah NSAID topikal (Diklofenak gel) atau Parasetamol oral.'\n"
    "2. DiPiro's Pharmacotherapy 12th Edition (2023) Chapter 60 (Osteoarthritis): 'Topical NSAIDs are strongly recommended over oral NSAIDs for knee osteoarthritis in patients aged ≥ 65 years or those with cardiovascular and renal risk factors.'\n"
    "Rekomendasi Farmasis: HENTIKAN seluruh NSAID oral sistemik (Meloxicam, Diklofenak, Asam Mefenamat). Ganti dengan terapi analgesik topikal Flamar Gel (Diklofenak 1%) dioleskan 3-4 kali sehari pada kedua lutut, kombinasikan dengan Parasetamol 500-1000 mg oral prn bila nyeri hebat, dan lanjutkan kondroprotektor Glukosamin 500 mg 1x1.",
    "alert")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence_rajal\ira_nsaid_safety_osteoarthritis.png",
    "Rekomendasi Keamanan Penggunaan NSAID pada Pasien Lansia dengan Komorbid Kardio-Renal",
    "Indonesian Rheumatology Association (IRA 2021)",
    "Rekomendasi IRA Hal. 14-19")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence_rajal\lexicomp_interactions_rajal.png",
    "Matriks Analisis Interaksi Obat Pasien Rawat Jalan (Lexicomp Drug Interaction Rating C & D)",
    "Lexicomp Drug Interactions Wolters Kluwer 2024",
    "Lexi-Interact Online Database")

# DRP 5
add_h3(doc, "DRP 5: Interaksi Farmakodinamik Gabapentin + Flunarizine (Depresi SSP & Fall Risk Paska Fraktur Zygoma)")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Pasien diresepkan Gabapentin 100 mg 2x1 (analgesik ajuvan neuropati diabetik) bersamaan dengan Flunarizine 5 mg 1x1 malam (profilaksis vertigo). "
    "Kedua obat ini menembus sawar darah otak dan memiliki efek aditif terhadap penekanan sistem saraf pusat (SSP). "
    "Kombinasi keduanya meningkatkan risiko pusing, sedasi berlebihan, ataksia motorik, kebingungan, dan gangguan keseimbangan postural. "
    "Efek sedasi aditif ini berkontribusi langsung terhadap kejadian jatuh pasien pada 04/07/2026 yang mengakibatkan cedera kepala dan fraktur os zygomaticum.")

add_callout_box(doc, "PEDOMAN GERIATRI: BEERS CRITERIA 2023 & DIPIRO 12TH ED CH. 58",
    "1. AGS Beers Criteria 2023 Update: Menekankan penghindaran kombinasi ≥ 2 obat yang mendepresi SSP pada geriatri karena melipatgandakan risiko jatuh (fall injury) dan fraktur.\n"
    "2. Lexicomp Geriatric Lexi-Drugs: Flunarizine memiliki waktu paruh eliminasi sangat panjang (hingga 18 hari pada lansia) dan risiko efek samping ekstrapiramidal serta depresi. Terapi vertigo perifer/sentral sebaiknya dibatasi maksimal 7-10 hari pada fase akut, bukan sebagai terapi kronis.\n"
    "Rekomendasi Farmasis: HENTIKAN Flunarizine 5 mg karena vertigo telah teratasi dan fase akut telah terlewati. Lanjutkan Gabapentin dengan dosis disesuaikan klirens ginjal yaitu 100 mg sekali sehari pada malam hari sebelum tidur untuk neuropati diabetik. Edukasi protokol pencegahan jatuh (fall prevention) di rumah.",
    "info")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence\dipiro_diabetic_neuropathy_weight.png",
    "Manajemen Terapi Neuropati Diabetik & Penyesuaian Dosis Gabapentin pada Pasien Geriatri",
    "DiPiro's Pharmacotherapy 12th Edition 2023",
    "Chapter 57 & 58, Hal. 1140-1145")

# DRP 6
add_h3(doc, "DRP 6: Drug-Food Interaction & Edukasi Khusus Penggunaan Acarbose 100 mg")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Acarbose adalah inhibitor alfa-glukosidase yang bekerja secara kompetitif menghambat enzim "
    "alfa-amilase pankreas dan alfa-glukosidase di brush border mukosa usus halus. Obat ini menghambat pemecahan oligosakarida dan disakarida menjadi monosakarida (glukosa). "
    "Ketepatan Cara Minum: Acarbose HANYA EFEKTIF bila diminum bersama suapan pertama makanan utama. "
    "Berdasarkan data MMAS-8, pasien sering meminum Acarbose 30 menit sebelum makan atau setelah selesai makan, sehingga efektivitasnya menumpulkan lonjakan glukosa postprandial menjadi hilang. "
    "Tatalaksana Hipoglikemia: Apabila pasien mengalami hipoglikemia akibat kombinasi Glimepirid dan Acarbose, "
    "konsumsi sukrosa (gula pasir biasa atau teh manis) TIDAK AKAN EFEKTIF karena hidrolisis sukrosa dihambat oleh Acarbose. "
    "Pasien dan keluarga WAJIB diedukasi untuk selalu menyediakan Dekstrosa Murni (tablet glukosa murni / madu murni / sirup jagung glukosa murni) untuk mengatasi kedaruratan hipoglikemia.")

# DRP 7
add_h3(doc, "DRP 7: Evaluasi Adverse Drug Reaction (ADR): Edema Perifer Amlodipin, Algoritma Naranjo (Skor 6 - Probable), dan Strategi Tatalaksana Kombinasi ARB")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Ny. Sri Wisraya mengeluhkan kedua pergelangan kaki dan punggung kaki membengkak (bilateral peripheral ankle edema) "
    "setelah mengonsumsi Amlodipin 10 mg selama 2 bulan. Kondisi ini membuat pasien merasa tidak nyaman dan sempat menghentikan sendiri konsumsi Amlodipin (faktor utama ketidakpatuhan MMAS-8 Item 3). "
    "Mekanisme Terjadinya Edema: Amlodipin merupakan Dihidropiridin Calcium Channel Blocker (DHP-CCB) yang bekerja merelaksasi otot polos vaskular "
    "secara selektif pada arteriol prekapiler arterial bed. Namun, Amlodipin TIDAK memiliki efek vasodilatasi yang seimbang pada venul postkapiler. "
    "Akibatnya, terjadi peningkatan gradien tekanan hidrostatik intrakapiler yang masif, mendorong ekstravasasi transudat cairan plasma dari lumen kapiler ke rongga interstisial jaringan lunak pergelangan kaki.")

headers_naranjo = ["No", "Pertanyaan Algoritma Naranjo (Adverse Drug Reaction)", "Jawaban Pasien", "Skor"]
rows_naranjo = [
    ["1", "Apakah ada laporan efek samping serupa sebelumnya pada obat ini?", "Ya (+1)", "+1"],
    ["2", "Apakah efek samping terjadi setelah obat yang dicurigai diberikan?", "Ya (+2)", "+2"],
    ["3", "Apakah reaksi efek samping membaik saat obat dihentikan (dechallenge)?", "Ya (+1)", "+1"],
    ["4", "Apakah efek samping muncul kembali saat obat diberikan ulang (rechallenge)?", "Ya (+2)", "+2"],
    ["5", "Apakah ada penyebab alternatif lain yang dapat menyebabkan reaksi ini?", "Tidak (0)", "0"],
    ["6", "Apakah reaksi muncul kembali saat plasebo diberikan?", "Tidak tahu (0)", "0"],
    ["7", "Apakah obat terdeteksi dalam darah/cairan tubuh dalam konsentrasi toksik?", "Tidak tahu (0)", "0"],
    ["8", "Apakah reaksi bertambah berat saat dosis dinaikkan / berkurang saat dosis diturunkan?", "Tidak tahu (0)", "0"],
    ["9", "Apakah pasien pernah mengalami reaksi serupa terhadap obat yang sama/mirip sebelumnya?", "Tidak tahu (0)", "0"],
    ["10", "Apakah efek samping terkonfirmasi oleh bukti objektif laboratorium/fisik?", "Ya (+1)", "+1"],
    ["TOTAL", "SKOR ALGORITMA NARANJO", "SKOR = 6", "+6 (PROBABLE)"]
]
add_styled_table(doc, headers_naranjo, rows_naranjo, [Inches(0.5), Inches(4.3), Inches(1.0), Inches(1.0)])

add_callout_box(doc, "STRATEGI TATALAKSANA EDEMA PERIFER AMLODIPIN (SKOVBJERG ET AL., 2023; SHETTY ET AL., 2016)",
    "Berdasarkan meta-analisis Skovbjerg et al. (2023, J Clin Hypertens) dan Shetty et al. (2016), tatalaksana edema perifer akibat Amlodipin BUKAN dengan memberikan obat diuretik loop, "
    "karena edema ini bukan disebabkan oleh retensi natrium/air sistemik, melainkan maldistribusi tekanan kapiler lokal.\n"
    "Strategi Terapi yang Terbukti Efektif:\n"
    "1. Penurunan Dosis Amlodipin: Turunkan dosis dari 10 mg menjadi 5 mg sekali sehari. Kejadian edema perifer berkurang dari 10,7% pada dosis 10 mg menjadi hanya 2,8% pada dosis 5 mg.\n"
    "2. Waktu Minum Malam Hari (Bedtime Dosing): Memberikan Amlodipin sebelum tidur memanfaatkan posisi tubuh terlentang (supinasi) saat istirahat malam yang meratakan tekanan hidrostatik mikrosirkulasi tungkai.\n"
    "3. Kombinasi Sinergis dengan ARB (Candesartan 8-16 mg): Angiotensin Receptor Blocker mendilasi venul postkapiler secara seimbang. Dilatasi venul postkapiler menormalkan tekanan intrakapiler, sehingga secara efektif melenyapkan transudat interstisial dan menghilangkan edema perifer tanpa memerlukan diuretik.",
    "success")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence\naranjo_amlodipine_edema.png",
    "Penilaian Algoritma Naranjo Adverse Drug Reaction (ADR): Edema Perifer Terinduksi Amlodipin (Skor 6 - Probable)",
    "Naranjo et al. (1981) Clin Pharmacol Ther & WHO-UMC",
    "Algoritma Standar Farmakovigilans")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence\skovbjerg_amlodipine_edema_mgmt.png",
    "Mekanisme & Strategi Tatalaksana Edema Perifer Terinduksi Amlodipin Berbasis Bukti Klinis",
    "Skovbjerg et al. (2023) J Clin Hypertens & Tolla et al. (2026)",
    "Halaman 112-118")

# DRP 8
add_h3(doc, "DRP 8: Evaluasi Kepatuhan Formularium Nasional (Fornas) & Rasionalitas Switch Statin (Rosuvastatin vs Atorvastatin)")
add_paragraph(doc,
    "Analisis Farmakoekonomi & Regulasi: Pada kunjungan 18/03/2026 pasien mendapatkan Rosuvastatin 20 mg, "
    "kemudian pada kunjungan 10/06/2026 diswitch ke Atorvastatin 20 mg. "
    "Berdasarkan Kepmenkes RI HK.01.07/MENKES/6485/2021 tentang Formularium Nasional (Fornas), "
    "Rosuvastatin memiliki restriksi peresepan yang sangat ketat: hanya diresepkan di Faskes Rujukan Tingkat Lanjutan (FKRTL) "
    "dengan restriksi dosis dan kuota restriktif serta indikasi dislipidemia berat yang refrakter terhadap statin lain. "
    "Sebaliknya, Atorvastatin 20 mg dapat diresepkan secara luas untuk pasien DM Tipe 2 dengan komorbid hipertensi dan risiko kardiovaskular tinggi tanpa restriksi kuota ketat. "
    "Dari aspek farmakokinetik klinis, Atorvastatin dieliminasi terutama melalui jalur hepatobilier (>98% diekskresi via feses dan empedu, ekskresi ginjal < 2%), "
    "sedangkan Rosuvastatin memiliki eliminasi ginjal yang lebih tinggi (sekitar 10%). "
    "Dengan demikian, keputusan beralih ke Atorvastatin 20 mg sangat rasional secara klinis (aman bagi ginjal) dan patuh terhadap regulasi Fornas BPJS Kesehatan.")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence_rajal\perhi_perki_hypertension_dyslipidemia.png",
    "Panduan Terapi Dislipidemia & Target Kolesterol LDL pada Pasien Risiko Kardiovaskular Tinggi",
    "Panduan Dislipidemia PERKI 2022 & Fornas Kemenkes RI",
    "Halaman 25-30")

# 1.9 SOAP Rajal
add_h2(doc, "1.9 Dokumentasi Asuhan Kefarmasian (SOAP) Rawat Jalan Lengkap")
headers_soap = ["Problem Medis", "Subjektif (S) & Objektif (O)", "Asesmen Farmasis (A)", "Rencana Asuhan & Intervensi (P)"]
rows_soap = [
    ["DM Tipe 2 Tak Terkontrol", 
     "S: Kesemutan telapak kaki, lemas, lapar malam hari.\nO: HbA1c 9,1%, GDP 190 mg/dL, GD2PP 245 mg/dL. Terapi: Glimepirid 6 mg, Sitagliptin 100 mg, Acarbose 200 mg.",
     "Kegagalan terapi 3 OHO oral. Glimepirid 6 mg dosis berlebih pada geriatri (PIM Beers). Sitagliptin belum disesuaikan ginjal. Indikasi inisiasi insulin.",
     "1. Inisiasi Insulin Glargine (Lantus) SC 1x10 U malam.\n2. Turunkan Glimepirid ke 2 mg 1x1 atau beralih ke Glikuidon 30 mg 1x1.\n3. Turunkan Sitagliptin ke 25 mg 1x1.\n4. Acarbose 100 mg dc suapan pertama.\n5. Target GDP 80-130 mg/dL."],
    
    ["Hipertensi & Edema Perifer",
     "S: Bengkak kedua pergelangan kaki, pusing.\nO: TD 165/89 mmHg (spike). Terapi: Amlodipin 10 mg, Candesartan 16 mg.",
     "Edema tungkai terinduksi Amlodipin (Naranjo 6 - Probable). Spike TD dipicu interaksi NSAID oral dan nyeri paska trauma.",
     "1. Turunkan Amlodipin ke 5 mg 1x1 diminum malam hari.\n2. Lanjutkan Candesartan 16 mg 1x1 pagi (sinergis melenyapkan edema).\n3. Hentikan NSAID oral sistemik.\n4. Target TD < 140/90 mmHg (atau < 130/80 bila ditoleransi)."],
    
    ["Osteoarthritis & Penurunan Klirens Ginjal",
     "S: Nyeri dan kaku kedua lutut (VAS 6).\nO: Kreatinin serum melonjak 2,69 mg/dL (CrCl 18 mL/min), Ureum 58 mg/dL. Terapi: Kalium Diklofenak 50 mg 2x1, Meloxicam.",
     "Nefrotoksisitas akut (AKI) superimposed on CKD terinduksi NSAID oral sistemik. PIM Beers Criteria.",
     "1. Hentikan total NSAID oral.\n2. Terapi topikal Flamar Gel 3-4x/hari oles lutut.\n3. Parasetamol 500 mg prn bila nyeri hebat.\n4. Glukosamin 500 mg 1x1 oral.\n5. Rehidrasi cairan dan re-evaluasi kreatinin 2 minggu."],
    
    ["Neuropati & Vertigo / Fall Risk",
     "S: Kesemutan kaki, pusing berputar, riwayat jatuh di kamar mandi.\nO: Pasca CKR + fraktur zygoma sinistra. Terapi: Gabapentin 100 mg 2x1, Flunarizine 5 mg 1x1.",
     "Interaksi aditif sedasi SSP antara Gabapentin dan Flunarizine memicu ataksia dan jatuh.",
     "1. Hentikan Flunarizine (vertigo fase akut terlewati).\n2. Gabapentin disesuaikan ginjal 100 mg 1x1 malam.\n3. Edukasi pencegahan jatuh di rumah (alas kaki anti-slip, pegangan toilet)."],
    
    ["Kepatuhan Pasien",
     "S: Bingung jadwal minum banyak obat, sengaja stop Amlodipin saat bengkak.\nO: Skor MMAS-8 = 5,5 (Kepatuhan Sedang).",
     "Polifarmasi (7-9 tablet) dan pemahaman cara minum obat kurang.",
     "1. Berikan Pill Box Organizer 4 kompartemen harian.\n2. Sediakan brosur jadwal obat visual berwarna.\n3. Edukasi keluarga untuk mendampingi kepatuhan."]
]
add_styled_table(doc, headers_soap, rows_soap, [Inches(1.2), Inches(1.8), Inches(1.8), Inches(2.0)])

print("Building Rawat Inap Section...")

# ==========================================
# BAGIAN II: RAWAT INAP (NY. SUNARTI)
# ==========================================
add_h1(doc, "BAGIAN II: ANALISIS MENDALAM KASUS RAWAT INAP (RANAP) — NY. SUNARTI")

add_paragraph(doc,
    "Analisis kasus rawat inap ini dilakukan terhadap Ny. Sunarti yang dirawat intensif di Bangsal Merak RS PKU Muhammadiyah Bantul. "
    "Pasien masuk melalui Instalasi Gawat Darurat (IGD) dengan keluhan kegawatdaruratan gastrointestinal akut berupa mual dan muntah profuse "
    "karena sindrom dispepsia (Vomitus Profuse ec Dyspepsia) yang disertai dekompensasi metabolik hiperglikemia akut DM Tipe 2 (GDS 357 mg/dL), "
    "riwayat hipertensi esensial, serta dehidrasi isotonik dengan gangguan elektrolit hiponatremia dan hipokloremia ringan.")

# 2.1 Demografi Ranap
add_h2(doc, "2.1 Profil Demografi & Data Dasar Pasien Rawat Inap")
headers_demo_ranap = ["Parameter Klinis", "Keterangan / Nilai Pasien", "Interpretasi Klinis Farmasis"]
rows_demo_ranap = [
    ["Nama Pasien", "Ny. Sunarti", "Pasien rawat inap Bangsal Merak"],
    ["Nomor Rekam Medis", "00109480", "Terdaftar di RS PKU Muhammadiyah Bantul"],
    ["Usia", "62 tahun 10 bulan", "Geriatri (usia rentan dehidrasi dan fluktuasi glikemik)"],
    ["Jenis Kelamin", "Perempuan", "Faktor risiko dismotilitas lambung & gastroparesis"],
    ["Berat Badan / Tinggi Badan", "60 kg / 156 cm", "IMT: 24,65 kg/m² (Kategori Normoweight mendekati Overweight)"],
    ["Ruang Rawat / Bangsal", "Bangsal Merak (Kelas II)", "Perawatan rawat inap non-ICU"],
    ["Dokter DPJP", "dr. Raden Triyono Edhi S., Sp.PD, FINASIM", "Dokter Spesialis Penyakit Dalam"],
    ["Diagnosis Utama Ranap", "Mual dan Muntah karena Dispepsia\n(Vomitus Profuse ec Dyspepsia)", "Eksaserbasi dispepsia akut dengan penurunan motilitas gaster / gastroparesis"],
    ["Diagnosis Sekunder Ranap", "1. DM Tipe 2 Hiperglikemia Akut (GDS 357 mg/dL)\n2. Hipertensi Stage 1 Terkontrol\n3. Hiponatremia & Hipokloremia Ringan", "Dekompensasi metabolik akut akibat asupan terhenti dan stres emetogenik"],
    ["Riwayat Alergi Obat", "Amoksisilin & Ampisilin", "Riwayat urtikaria generalisata, eritema makulopapular, dan gatal berat"]
]
add_styled_table(doc, headers_demo_ranap, rows_demo_ranap, [Inches(1.8), Inches(2.4), Inches(2.6)])

# 2.2 Riwayat Masuk RS & Keluhan Utama
add_h2(doc, "2.2 Riwayat Masuk Rumah Sakit & Keluhan Utama: Mual dan Muntah karena Dispepsia")
add_paragraph(doc,
    "Kronologi Masuk IGD: Pasien datang ke IGD RS PKU Muhammadiyah Bantul pada 18 Oktober 2026 pukul 09.30 WIB dengan keluhan utama "
    "mual hebat dan muntah profuse (frekuensi > 6 kali dalam 24 jam terakhir). Muntahan berisi cairan keruh bercampur lendir dan sisa makanan lambung, "
    "tidak ditemukan hematemesis (muntah darah) maupun melena. Pasien mengeluhkan rasa nyeri menusuk dan panas seperti terbakar pada area ulu hati (epigastrium), "
    "perut kembung, begah paska makan (postprandial fullness), cepat kenyang (early satiation), rasa asam naik ke kerongkongan (heartburn), "
    "dan badan terasa sangat lemas tak berdaya. Pasien sama sekali tidak dapat mentoleransi asupan makanan maupun minuman oral selama 18 jam terakhir.")

add_paragraph(doc,
    "Riwayat Pengobatan Rumah (Home Medications): Pasien diketahui memiliki riwayat Diabetes Melitus Tipe 2 selama 6 tahun dan rutin mengonsumsi "
    "Metformin 500 mg 3 kali sehari dan Glimepirid 2 mg 1 kali sehari pada pagi hari. Untuk riwayat hipertensi, pasien rutin mengonsumsi Amlodipin 10 mg 1 kali sehari pada malam hari. "
    "Namun, dalam 2 hari sebelum masuk rumah sakit, seluruh obat oral tidak dapat diminum karena langsung dimuntahkan kembali.")

# 2.3 Pemantauan TTV Ranap
add_h2(doc, "2.3 Pemantauan Tanda-Tanda Vital (TTV) Selama Rawat Inap")
headers_ttv_ranap = ["Waktu Pemantauan", "Tekanan Darah (mmHg)", "Nadi (x/m)", "Laju Nafas (x/m)", "Suhu (°C)", "SpO2 (%)", "Status Klinis Pasien"]
rows_ttv_ranap = [
    ["18/10 (Masuk IGD)", "145/88", "88", "20", "36,8", "98%", "Akut; lemas berat, muntah profuse, nyeri ulu hati hebat"],
    ["19/10 (Hari Rawat 1)", "135/82", "84", "18", "36,6", "99%", "Mual berkurang, muntah 1x cairan, rehidrasi IV berjalan"],
    ["20/10 (Hari Rawat 2)", "130/80", "80", "18", "36,5", "98%", "Muntah berhenti, mual minimal, mulai toleransi diet cair"],
    ["21/10 (Hari Rawat 3)", "125/78", "78", "18", "36,5", "99%", "Stabil, keluhan mual/muntah tuntas, persiapan KRS"]
]
add_styled_table(doc, headers_ttv_ranap, rows_ttv_ranap, [Inches(1.2), Inches(1.1), Inches(0.8), Inches(0.8), Inches(0.8), Inches(0.7), Inches(1.4)])

add_image_evidence(doc,
    r"d:\FILE NINIS\ppt_assets\ttv_chart.png",
    "Grafik Perkembangan Tanda-Tanda Vital (Tekanan Darah, Nadi, Suhu) Ny. Sunarti Selama Rawat Inap",
    "Rekam Medis Bangsal Merak RS PKU Muhammadiyah Bantul",
    "CPPT Rawat Inap 18-21 Oktober 2026")

# 2.4 Data Lab Ranap
add_h2(doc, "2.4 Pemantauan Data Laboratorium Selama Rawat Inap")
add_paragraph(doc,
    "Hasil pemeriksaan laboratorium saat masuk IGD mengonfirmasi krisis hiperglikemia berat dengan GDS 357 mg/dL. "
    "Pemeriksaan urinalisis menunjukkan glukosuria masif (Glukosa Urin +3), namun Keton Urin Negatif, "
    "yang menyingkirkan diagnosis Ketoasidosis Diabetik (KAD) berat dan mengonfirmasi kondisi Hiperglikemia Hiperosmolar Non-Ketotik Ringan "
    "yang terinduksi oleh stres fisik dispepsia dan dehidrasi akibat muntah profuse. "
    "Pemeriksaan elektrolit menunjukkan Hiponatremia ringan (Na 131 mmol/L) dan Hipokloremia ringan (Cl 96 mmol/L) "
    "akibat kehilangan cairan asam lambung (HCl) dan natrium secara masif melalui muntah berulang.")

headers_lab_ranap = ["Parameter Laboratorium", "Nilai Pasien (IGD)", "Nilai Evaluasi (H2/H3)", "Nilai Normal", "Satuan", "Interpretasi Klinis Farmasis"]
rows_lab_ranap = [
    ["GDS (Masuk IGD)", "357", "-", "70 – 140", "mg/dL", "Hiperglikemia akut berat terinduksi stres dispepsia & dehidrasi"],
    ["GDS (Hari 1 Pagi)", "245", "-", "140 – 180", "mg/dL", "Respon awal terapi insulin Novorapid + Lantus"],
    ["GDS (Hari 1 Sore)", "198", "-", "140 – 180", "mg/dL", "Penurunan progresif stabil"],
    ["GDS (Hari 2 Pagi)", "162", "-", "140 – 180", "mg/dL", "Mencapai target glikemik rawat inap (140-180 mg/dL)"],
    ["GDS (Hari 2 Sore)", "154", "-", "140 – 180", "mg/dL", "Terkontrol sangat baik tanpa tanda hipoglikemia"],
    ["GDS (Hari 3 Pagi)", "138", "-", "140 – 180", "mg/dL", "Target tercapai sempurna; siap transisi terapi pulang"],
    ["Natrium Darah (Na+)", "131", "137 (H3)", "135 – 147", "mmol/L", "Hiponatremia ringan ec vomitus profuse; terkoreksi pasca infus NaCl"],
    ["Kalium Darah (K+)", "3,8", "4,1 (H3)", "3,5 – 5,0", "mmol/L", "Normal batas bawah; tidak terjadi hipokalemia berat"],
    ["Klorida Darah (Cl-)", "96", "101 (H3)", "98 – 106", "mmol/L", "Hipokloremia ringan akibat hilangnya asam HCl lambung"],
    ["Ureum Darah", "32", "28 (H3)", "15 – 45", "mg/dL", "Normal; tidak ada azotemia signifikan"],
    ["Kreatinin Serum", "0,98", "0,89 (H3)", "0,6 – 1,1", "mg/dL", "Normal (eGFR 61,4 mL/min/1,73m²); fungsi ginjal terpelihara"],
    ["Glukosa Urin", "+3", "Negatif (H3)", "Negatif", "-", "Glukosuria masif saat krisis hiperglikemia IGD"],
    ["Keton Urin", "Negatif", "Negatif", "Negatif", "-", "Menyingkirkan komplikasi Ketoasidosis Diabetik (KAD)"],
    ["Leukosit", "9.200", "7.800 (H3)", "4.000 – 10.000", "/µL", "Normal; tidak ada infeksi bakterial aktif (afebris)"]
]
add_styled_table(doc, headers_lab_ranap, rows_lab_ranap, [Inches(1.4), Inches(0.9), Inches(1.1), Inches(1.0), Inches(0.6), Inches(1.8)])

add_image_evidence(doc,
    r"d:\FILE NINIS\ppt_assets\glucose_chart.png",
    "Grafik Penurunan Glukosa Darah Sewaktu (GDS) Ny. Sunarti Menuju Target Terapi Rawat Inap (140-180 mg/dL)",
    "Pedoman Pengelolaan DM Tipe 2 PERKENI 2021 & ADA Standards of Care 2024",
    "PERKENI Hal. 100; ADA Diabetes Care 2024;47(Suppl 1):S278-S282")

# 2.5 Profil Terapi Ranap
add_h2(doc, "2.5 Profil Terapi Pengobatan Selama Rawat Inap")
headers_rx_ranap = ["Nama Obat / Cairan", "Dosis & Frekuensi", "Rute", "Indikasi Klinis", "Kategori Terapi"]
rows_rx_ranap = [
    ["IVFD NaCl 0,9%", "20 tetes/menit (1.500 mL/24j)", "Intravena", "Rehidrasi cairan & koreksi Na/Cl", "Kristaloid Isotonik"],
    ["Inj. Omeprazole", "40 mg / 24 jam vial", "Intravena", "Supresi asam lambung pada dispepsia", "Proton Pump Inhibitor (PPI)"],
    ["Inj. Metoclopramide", "10 mg / 8 jam ampul (Gavistal)", "Intravena", "Mual & muntah / dismotilitas", "Prokinetik D2 Antagonist"],
    ["Domperidone Sirup/Tab", "10 mg 3x1 (AC)", "Oral", "Mual muntah & kembung epigastrik", "Prokinetik D2 Antagonist Perifer"],
    ["Inj. Ondansetron", "4 mg / 8 jam ampul (prn)", "Intravena", "Antiemetik refrakter", "Antagonis Reseptor 5-HT3 Serotonin"],
    ["Sucralfate Sirup", "3 x 1 sendok makan (15 mL ~ 1 g) AC", "Oral", "Mukoproteksi gaster & gastritis", "Pelindung Mukosa Lambung"],
    ["Novorapid (Insulin Aspart)", "3 x 6 - 8 Unit (sebelum makan)", "Subkutan", "Kontrol glikemik prandial rawat inap", "Insulin Analog Rapid-Acting"],
    ["Lantus (Insulin Glargine)", "1 x 10 Unit (malam jam 22.00)", "Subkutan", "Kontrol glikemik basal rawat inap", "Insulin Analog Long-Acting Basal"],
    ["Amlodipin Tablet", "10 mg 1x1 tablet (malam)", "Oral", "Hipertensi esensial (rekonsiliasi)", "DHP-Calcium Channel Blocker"],
    ["Parasetamol Tablet", "500 mg 3x1 tablet (k/p)", "Oral", "Analgesik / antipiretik prn", "Analgesik Non-Opioid"]
]
add_styled_table(doc, headers_rx_ranap, rows_rx_ranap, [Inches(1.4), Inches(1.6), Inches(0.8), Inches(1.6), Inches(1.4)])

# 2.6 Identifikasi DRP Ranap
add_h2(doc, "2.6 Identifikasi & Analisis Mendalam Drug-Related Problems (DRP) Rawat Inap")

# DRP 1 Ranap: Duplikasi D2
add_h3(doc, "DRP 1: Duplikasi Terapi Prokinetik D2 (Metoclopramide IV + Domperidone Oral) — Risiko Berat Ekstrapiramidal (EPS) & Perpanjangan Interval QTc")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Pasien secara bersamaan menerima resep Inj. Metoclopramide 10 mg IV tiap 8 jam (Gavistal) "
    "dan Domperidone 10 mg 3 kali sehari per oral. Kedua obat ini memiliki mekanisme kerja farmakodinamik yang identik, "
    "yaitu bekerja sebagai antagonis kompetitif pada reseptor dopamin tipe 2 (D2 receptor antagonists). "
    "Metoclopramide menembus sawar darah otak (blood-brain barrier) secara masif dan memblokade reseptor dopaminergik sentral di korpus striatum basal ganglia, "
    "sedangkan Domperidone bekerja terutama di perifer dan chemoreceptor trigger zone (CTZ) area postrema di dasar ventrikel keempat.")

add_paragraph(doc,
    "Bahaya Toksisitas Kombinasi Ganda: Kombinasi dua agen antagonis dopamin D2 TIDAK MEMBERIKAN peningkatan efikasi antiemetik yang sinergis, "
    "melainkan secara substansial melipatgandakan risiko toksisitas fatal:\n"
    "1. Gejala Ekstrapiramidal Akut (EPS): Terjadinya distonia akut (spasme otot leher, tortikolis, krisis okulogirik), akatisia (kegelisahan motorik ekstrem), "
    "dan sindrom parkinsonisme sekunder yang sangat berbahaya pada pasien geriatri.\n"
    "2. Kardiotoksisitas Perpanjangan Interval QTc: Kedua obat, terutama Domperidone dan Metoclopramide konsentrasi tinggi, "
    "memblokade kanal kalium IKr (hERG gene) pada miokardium ventrikel, memperpanjang repolarisasi ventrikel (prolonged QTc interval), "
    "dan berisiko tinggi memicu aritmia ventrikel fatal Torsades de Pointes (TdP) dan henti jantung mendadak.\n"
    "Klasifikasi Interaksi: Lexicomp Drug Interactions Rating: Category D / X (Avoid Combination / Consider Therapy Modification).")

add_callout_box(doc, "REKOMENDASI INTERVENSI FARMASIS: KONSENSUS PGI & LEXICOMP",
    "1. HENTIKAN segera salah satu prokinetik D2 untuk mencegah toksisitas neurologis EPS dan aritmia jantung.\n"
    "2. Pada fase akut rawat inap di mana pasien muntah profuse dan absorbsi saluran cerna oral terganggu, "
    "pertahankan INJEKSI METOCLOPRAMIDE 10 mg IV (atau 5 mg IV pada geriatri) sebagai monoterapi prokinetik parenteral, "
    "dan HENTIKAN DOMPERIDONE ORAL.\n"
    "3. Apabila muntah masih belum teratasi secara optimal, JANGAN MENAMBAH prokinetik D2 lain. "
    "Gunakan antiemetik dengan mekanisme kerja berbeda (multi-modal antiemetic therapy), yaitu INJEKSI ONDANSETRON 4-8 mg IV "
    "(Antagonis Reseptor Serotonin 5-HT3) yang bekerja sinergis menekan impuls emetogenik vagal tanpa risiko efek samping ekstrapiramidal.",
    "alert")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence\drug_interaction_gavistal_domperidone.png",
    "Analisis Interaksi Mayor Duplikasi Prokinetik Dopamin D2 (Metoclopramide + Domperidone) — Lexicomp Risk Rating D/X",
    "Lexicomp Drug Interactions Wolters Kluwer 2024",
    "Lexi-Interact Online Database")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence\konsensus_dispepsia_pgi_dipiro.png",
    "Pedoman Tatalaksana Dispepsia & Algoritma Terapi Mual-Muntah Sesuai Konsensus PGI & DiPiro 12th Ed",
    "Perkumpulan Gastroenterologi Indonesia (PGI 2021/2024) & DiPiro 12th Ed 2023",
    "Konsensus PGI Hal. 12-16; DiPiro Ch. 41 & 42")

# DRP 2 Ranap: Penyesuaian Ginjal Metoclopramide
add_h3(doc, "DRP 2: Penyesuaian Dosis Ginjal Metoclopramide pada Pasien Geriatri")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Metoclopramide dieliminasi sebagian besar melalui rute ginjal (sekitar 80% diekskresi via urin "
    "dalam bentuk obat bebas dan metabolit konjugat glukuronida/sulfat). Pada pasien geriatri berusia 62 tahun 10 bulan dengan laju filtrasi ginjal "
    "yang fluktuatif akibat dehidrasi vomitus (eGFR terhitung ~61,4 mL/min), klirens ginjal obat mengalami penurunan dibandingkan populasi dewasa muda. "
    "Pemberian dosis penuh 10 mg IV setiap 8 jam (30 mg/hari) pada lansia berisiko menyebabkan akumulasi konsentrasi obat dalam cairan serebrospinal, "
    "meningkatkan kerentanan terhadap efek sedasi berlebih dan diskinesia tardif.")

add_callout_box(doc, "PEDOMAN KLINIS: LEXICOMP GERIATRIC DOSING & MICROMEDEX",
    "Rekomendasi Penyesuaian Dosis Metoclopramide pada Geriatri & Penurunan Fungsi Ginjal:\n"
    "• CrCl ≥ 60 mL/min: Dosis standar 10 mg tiap 8 jam IV.\n"
    "• CrCl 40 – 59 mL/min atau Pasien Geriatri Rentan: Dosis diturunkan 50% menjadi 5 mg IV tiap 8 jam atau 10 mg IV tiap 12 jam.\n"
    "• CrCl < 40 mL/min: Turunkan dosis sebesar 50% (5 mg tiap 8 jam atau 10 mg tiap 12-24 jam).\n"
    "Rekomendasi Farmasis: Turunkan dosis injeksi Metoclopramide menjadi 5 mg IV tiap 8 jam, batasi durasi penggunaan maksimal 5 hari parenteral, "
    "dan segera hentikan begitu pasien mampu mentoleransi asupan oral dengan baik.",
    "info")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence\lexicomp_metoclopramide_renal.png",
    "Panduan Penyesuaian Dosis Ginjal & Geriatri Metoclopramide untuk Mencegah Toksisitas Ekstrapiramidal",
    "Lexicomp Geriatric Lexi-Drugs & Micromedex 2024",
    "Lexicomp Drug Dosing Guidelines")

# DRP 3 Ranap: Tatalaksana Dispepsia PGI & DiPiro
add_h3(doc, "DRP 3: Tatalaksana Komprehensif Mual Muntah karena Dispepsia Berdasarkan Konsensus Nasional PGI 2021/2024 & DiPiro 12th Ed Ch. 41-42")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Sindrom dispepsia pada Ny. Sunarti tergolong ke dalam dispepsia fungsional / gastroparesis diabetik "
    "yang mengalami eksaserbasi akut. Kondisi ini ditandai oleh kombinasi dismotilitas antrum lambung (lambatnya pengosongan lambung ke duodenum), "
    "hipersensitivitas viseral gaster terhadap distensi, serta ketidakseimbangan sekresi asam lambung dan faktor defensif mukosa gaster.")

add_paragraph(doc,
    "Strategi Terapi Berbasis Guideline Terkini:\n"
    "1. Supresi Asam Lambung Lini Pertama: Konsensus Nasional Penatalaksanaan Dispepsia dan Infeksi Helicobacter pylori (PGI 2021/2024) "
    "merekomendasikan pemberian Proton Pump Inhibitor (PPI) parenteral seperti Inj. Omeprazole 40 mg IV sekali sehari pada fase akut. "
    "PPI secara poten menghambat pompa proton H+/K+-ATPase pada sel parietal gaster, meningkatkan pH lambung > 4, mengurangi iritasi mukosa, "
    "serta meredakan keluhan nyeri epigastrium panas terbakar.\n"
    "2. Mukoprotektor Lambung: Sucralfate sirup 1 g (15 mL) 3 kali sehari diberikan dalam kondisi lambung kosong (1 jam sebelum makan atau sebelum tidur). "
    "Sucralfate membentuk kompleks pasta pelindung yang berikatan secara selektif dengan eksudat protein pada mukosa lambung yang terinflamasi, "
    "menstimulasi pelepasan prostaglandin lokal dan bikarbonat, serta melindungi epitel dari degradasi asam dan pepsin.\n"
    "3. Antiemetik Terarah: DiPiro 12th Edition Chapter 41 & 42 menekankan bahwa pasien rawat inap dengan dehidrasi akibat vomitus memerlukan "
    "antiemetik parenteral selektif. Kombinasi monoterapi prokinetik parenteral (Metoclopramide 5-10 mg IV) untuk mempercepat pengosongan lambung "
    "dan rescue therapy Ondansetron 4 mg IV sangat efektif menghentikan refleks emetogenik di pusat muntah medula oblongata tanpa memicu depresi pernafasan atau sedasi berat.")

# DRP 4 Ranap: Hiperglikemia Ranap (PERKENI & ADA)
add_h3(doc, "DRP 4: Tatalaksana Hiperglikemia Akut Rawat Inap (GDS 357 mg/dL) — Penghentian OHO Oral, Inisiasi Regimen Insulin Basal-Bolus Subkutan Target 140–180 mg/dL")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Ny. Sunarti masuk rumah sakit dengan GDS 357 mg/dL. Pasien memiliki riwayat penggunaan OHO rumah "
    "berupa Metformin 500 mg 3x1 dan Glimepirid 2 mg 1x1 pagi. Hiperglikemia akut ini dipicu oleh respon stres fisik akut (pelepasan hormon kontra-regulator "
    "seperti kortisol, glukagon, dan epinefrin yang memicu glukoneogenesis masif) serta asupan cairan yang terganggu akibat muntah berulang.")

add_callout_box(doc, "PEDOMAN RAWAT INAP: PERKENI 2021 (HAL. 98-101) & ADA 2024 SECTION 16 (HAL. S278-S282)",
    "1. Penghentian Mutlak Seluruh OHO Oral: PERKENI 2021 & ADA Standards of Care 2024 menegaskan bahwa pada pasien DM yang dirawat inap di rumah sakit:\n"
    "• METFORMIN HARUS SEGERA DIHENTIKAN sementara karena risiko fatal Asidosis Laktat (Lactic Acidosis) yang dipicu oleh dehidrasi, hipovolemia, atau penurunan perfusi jaringan akut.\n"
    "• SULFONILUREA (Glimepirid) HARUS DIHENTIKAN sementara karena masa kerjanya yang panjang dan risiko tinggi hipoglikemia berat memanjang saat asupan nutrisi pasien tidak menentu akibat mual muntah.\n"
    "2. Standar Emas Terapi Insulin Basal-Bolus: Terapi pilihan utama pasien hiperglikemia rawat inap non-kritis adalah Regimen Insulin Subkutan Basal-Bolus:\n"
    "• Insulin Basal (Lantus / Glargine): Mengontrol produksi glukosa hepatik basal sepanjang 24 jam. Diberikan 1 kali sehari malam hari (10 Unit).\n"
    "• Insulin Bolus Prandial (Novorapid / Aspart): Mengontrol ekskursi glukosa paska makan. Diberikan 3 kali sehari segera sebelum makan (3 x 6-8 Unit ac).\n"
    "3. Target Glikemik Rawat Inap: Target kadar glukosa darah rawat inap yang direkomendasikan adalah 140 – 180 mg/dL (7,8 – 10,0 mmol/L).\n"
    "• Target < 110 mg/dL (terapi intensif ketat) TIDAK DIREKOMENDASIKAN karena uji klinis multisenter (NICE-SUGAR trial) membuktikan peningkatan mortalitas akibat kejadian hipoglikemia berat.\n"
    "• Target > 180 mg/dL tidak dapat ditoleransi karena meningkatkan risiko infeksi nosokomial, glukosuria osmotik, dan memperlambat pemulihan mukosa saluran cerna.",
    "alert")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence\perkeni_inpatient_guideline.png",
    "Pedoman Pengelolaan Hiperglikemia Pasien Rawat Inap Rumah Sakit Non-ICU Sesuai Konsensus PERKENI",
    "Pedoman Pengelolaan DM Tipe 2 PERKENI 2021",
    "Halaman 98-101")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence\ada_inpatient_guideline.png",
    "Standar Pelayanan Medis Diabetes Rawat Inap & Target Glukosa Darah 140-180 mg/dL Sesuai ADA Standards of Care",
    "American Diabetes Association (ADA Standards of Care 2024)",
    "Section 16 (Inpatient Care), Diabetes Care 2024;47(Suppl 1):S278-S282")

# DRP 5 Ranap: Rekonsiliasi Hipertensi
add_h3(doc, "DRP 5: Rekonsiliasi Terapi Antihipertensi Rawat Inap (Amlodipin 10 mg)")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Ny. Sunarti memiliki riwayat hipertensi dengan terapi rutin Amlodipin 10 mg 1x1 malam di rumah. "
    "Saat masuk IGD, tekanan darah pasien adalah 145/88 mmHg. "
    "Pada 24 jam pertama rawat inap saat pasien masih mengalami muntah aktif dan intake oral tertutup, "
    "pemberian tablet Amlodipin oral ditunda sementara untuk menghindari terbuangnya obat melalui muntah. "
    "Tekanan darah dipantau ketat secara serial. Memasuki Hari Rawat ke-2, saat keluhan mual muntah teratasi dan pasien mulai toleransi cairan/makanan lunak, "
    "Amlodipin 10 mg 1x1 malam SEGERA DIREKONSILIASI dan diberikan kembali per oral. "
    "Hal ini sesuai dengan panduan PERHI 2021 dan ACC/AHA 2023 untuk mencegah terjadinya lonjakan tekanan darah mendadak (rebound hypertension) paska penghentian obat.")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence\perhi_acc_aha_hypertension_reconciliation.png",
    "Konsensus Penatalaksanaan Hipertensi & Protokol Rekonsiliasi Obat Antihipertensi Rawat Inap",
    "Konsensus Hipertensi PERHI 2021 & ACC/AHA 2023 Guidelines",
    "PERHI 2021 Hal. 22-26")

# DRP 6 Ranap: Rehidrasi Cairan & Koreksi Elektrolit
add_h3(doc, "DRP 6: Rehidrasi Cairan Kristaloid Isotonik & Koreksi Elektrolit Hiponatremia dan Hipokloremia Akibat Vomitus Profuse")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Akibat muntah berulang > 6 kali, tubuh kehilangan sejumlah besar cairan lambung yang kaya akan ion asam klorida (H+ dan Cl-) serta natrium (Na+). "
    "Kondisi ini terbukti secara objektif dari data laboratorium masuk IGD: Natrium 131 mmol/L (Hiponatremia ringan) dan Klorida 96 mmol/L (Hipokloremia ringan). "
    "Kehilangan cairan ini juga menurunkan volume intravaskular efektif, memicu hemokonsentrasi dan hipovolemia fungsional.")

add_callout_box(doc, "PEDOMAN REHIDRASI: WHO & DIPIRO 12TH ED CH. 38",
    "1. Pemilihan Cairan Kristaloid Terpilih: Cairan pilihan utama untuk mengatasi hiponatremia dan hipokloremia akibat muntah profuse adalah "
    "INFUS NaCL 0,9% (Normal Saline). Komposisi NaCl 0,9% mengandung Na+ 154 mEq/L dan Cl- 154 mEq/L dengan osmolaritas 308 mOsm/L (isotonik terhadap plasma). "
    "Cairan ini secara cepat mengembalikan volume sirkulasi intravaskular, meningkatkan laju perfusi ginjal, serta mengoreksi defisit natrium dan klorida secara bertahap.\n"
    "2. Kecepatan Infus Aman: Kecepatan infus 20 tetes per menit (makro: 1 mL = 20 tetes -> 60 mL/jam ~ 1.500 mL per 24 jam) aman bagi pasien geriatri, "
    "mencegah bahaya kelebihan beban cairan (fluid overload / edema paru) dan mencegah koreksi natrium terlalu cepat yang berisiko memicu Osmotic Demyelination Syndrome (ODS).\n"
    "3. Bukti Evaluasi Laboratorium: Pada Hari Rawat ke-3, kadar Natrium serum berhasil terkoreksi menjadi normal (137 mmol/L) dan Klorida menjadi normal (101 mmol/L).",
    "success")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence\vomitus_rehydration_guideline.png",
    "Panduan Terapi Rehidrasi Cairan & Koreksi Gangguan Elektrolit pada Pasien dengan Mual Muntah Akut",
    "DiPiro's Pharmacotherapy 12th Edition & WHO Guidelines",
    "DiPiro Ch. 38 (Disorders of Sodium & Water Homeostasis), Hal. 752-758")

# DRP 7 Ranap: Evaluasi Geriatri Beers Criteria
add_h3(doc, "DRP 7: Evaluasi Penggunaan Obat pada Pasien Geriatri Berdasarkan AGS Beers Criteria 2023")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Seluruh terapi yang diterima Ny. Sunarti (62 tahun 10 bulan) dievaluasi kesesuaiannya dengan kriteria geriatri "
    "American Geriatrics Society (AGS) Beers Criteria 2023 Update:\n"
    "1. Metoclopramide: Termasuk dalam daftar obat yang harus dibatasi ketat durasinya pada geriatri. Penggunaan > 12 minggu dikontraindikasikan "
    "karena risiko diskinesia tardif ireversibel. Pada kasus Ny. Sunarti, pemberian Metoclopramide dibatasi hanya 3 hari pada fase rawat inap akut.\n"
    "2. Insulin Analog: Penggunaan Insulin Analog (Novorapid dan Lantus) pada pasien geriatri sangat tepat dan direkomendasikan dibandingkan insulin regular/NPH manusiawi, "
    "karena profil farmakokinetiknya yang stabil, dapat diprediksi, dan terbukti klinis menurunkan insidensi hipoglikemia nokturnal yang fatal pada lansia.")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence\beers_criteria_geriatric.png",
    "Kriteria Penggunaan Obat yang Berpotensi Tidak Tepat pada Populasi Geriatri (AGS Beers Criteria 2023)",
    "American Geriatrics Society 2023 Update",
    "J Am Geriatr Soc 2023;71(7):2052-2081")

# DRP 8 Ranap: Evaluasi Alergi Penisilin & Metode Gyssens
add_h3(doc, "DRP 8: Evaluasi Rasionalitas Antibiotik Metode Gyssens & Riwayat Alergi Penisilin (Amoksisilin/Ampisilin)")
add_paragraph(doc,
    "Analisis Klinis Farmakologis: Ny. Sunarti memiliki riwayat alergi terdokumentasi terhadap Amoksisilin dan Ampisilin "
    "(reaksi tipe I / IV dengan manifestasi ruam makulopapular eritematosa dan pruritus berat). "
    "Selama masa perawatan di Bangsal Merak, DPJP TIDAK MERESEPKAN ANTIBIOTIK empiris apa pun.")

add_callout_box(doc, "AUDIT KUALITATIF PENGGUNAAN ANTIBIOTIK METODE GYSSENS (PERMENKES RI NO. 28/2021)",
    "Berdasarkan alur audit kualitatif Gyssens (Gyssens et al., 1992 & Pedoman Pelayanan Kefarmasian Kemenkes RI):\n"
    "1. Evaluasi Indikasi Klinis Infeksi: Pasien masuk dengan vomitus profuse ec dispepsia fungsional. "
    "Pemeriksaan suhu tubuh afebris (36,8°C), leukosit darah normal (9.200 /µL), dan urinalisis tidak menunjukkan infeksi saluran kemih (nitrit negatif, leukosit normal).\n"
    "2. Penilaian Kategori Gyssens: Keputusan klinis untuk TIDAK MEMBERIKAN ANTIBIOTIK pada kasus ini dinilai sebagai:\n"
    "KATEGORI 0: Penggunaan / Keputusan Terapi Antibiotik TEPAT dan RASIONAL (Appropriate Indication - No Antibiotic Indicated).\n"
    "3. Manajemen Riwayat Alergi: Riwayat alergi penisilin wajib diberi tanda stiker merah menyala pada berkas rekam medis fisik dan peringatan pop-up pada sistem rekam medis elektronik (RME) rumah sakit. "
    "Apabila di masa depan pasien mengalami infeksi bakterial berat, golongan Sefalosporin generasi 3 (Ceftriaxone) dapat digunakan dengan pemantauan ketat (cross-reactivity < 2%), "
    "atau menggunakan golongan alternatif non-beta laktam seperti Fluoroquinolon (Ciprofloxacin) atau Makrolida (Azitromisin).",
    "success")

add_image_evidence(doc,
    r"d:\FILE NINIS\guideline_evidence\gyssens_algorithm_flowchart.png",
    "Algoritma Evaluasi Kualitatif Rasionalitas Penggunaan Antibiotik Metode Gyssens",
    "Permenkes RI No. 28/2021 tentang Pedoman Penggunaan Antibiotik & Gyssens et al. (1992)",
    "Permenkes 28/2021 Lampiran Hal. 35-40")

# 2.7 SOAP Ranap
add_h2(doc, "2.7 Dokumentasi Asuhan Kefarmasian (SOAP) Rawat Inap Lengkap (Per Hari Rawatan)")

# SOAP Hari 1
add_h3(doc, "Dokumentasi SOAP Hari ke-1 Rawat Inap (18-19 Oktober 2026) — Fase Kedaruratan Akut")
headers_soap_h1 = ["Problem Medis", "Subjektif (S) & Objektif (O)", "Asesmen Farmasis (A)", "Rencana Terapi & Intervensi Farmasis (P)"]
rows_soap_h1 = [
    ["Mual Muntah ec Dispepsia", 
     "S: Muntah > 6x, isi cairan & sisa makanan, lemas berat, nyeri ulu hati menusuk, tidak bisa makan/minum.\nO: Epigastric tenderness (+), turgor kulit menurun.",
     "Vomitus profuse ec dispepsia akut. Duplikasi prokinetik D2 (Metoclopramide IV + Domperidone PO) berisiko EPS dan perpanjangan QTc (Lexicomp Cat D/X).",
     "1. IVFD NaCl 0,9% 20 tpm untuk rehidrasi.\n2. Inj. Omeprazole 40 mg / 24 jam IV.\n3. Pertahankan Inj. Metoclopramide 10 mg IV (atau 5 mg pada lansia).\n4. REKOMENDASI: HENTIKAN Domperidone oral.\n5. Tambahkan Inj. Ondansetron 4 mg IV bila muntah refrakter."],
    
    ["Hiperglikemia Akut DM Tipe 2",
     "S: Badan lemas tak bertenaga, riwayat DM rutin Metformin & Glimepirid.\nO: GDS 357 mg/dL, Glukosa Urin +3, Keton Negatif.",
     "Krisis hiperglikemia terinduksi stres akut dispepsia dan dehidrasi. OHO oral dikontraindikasikan (PERKENI & ADA).",
     "1. HENTIKAN sementara Metformin & Glimepirid oral.\n2. Inisiasi Regimen Insulin Basal-Bolus:\n   - Novorapid SC 3 x 6 Unit ac (prandial)\n   - Lantus SC 1 x 10 Unit malam (basal)\n3. Monitoring GDS tiap 6 jam (target 140-180 mg/dL)."],
    
    ["Gangguan Elektrolit Hiponatremia & Hipokloremia",
     "S: Lemas, pusing melayang.\nO: Na+ 131 mmol/L (L), Cl- 96 mmol/L (L), K+ 3,8 mmol/L.",
     "Hiponatremia & hipokloremia ringan akibat kehilangan elektrolit dari cairan asam lambung via muntah berulang.",
     "1. Rehidrasi kristaloid isotonik Infus NaCl 0,9% 20 tpm.\n2. Re-evaluasi elektrolit serum serial 24-48 jam."],
    
    ["Hipertensi Esensial",
     "S: Pusing ringan.\nO: TD 145/88 mmHg. Riwayat Amlodipin 10 mg rumah.",
     "Hipertensi terkontrol borderline. Terapi oral ditunda 24 jam karena muntah aktif.",
     "1. Tunda Amlodipin oral hingga toleransi oral membaik.\n2. Pantau TD tiap 8 jam."]
]
add_styled_table(doc, headers_soap_h1, rows_soap_h1, [Inches(1.2), Inches(1.8), Inches(1.8), Inches(2.0)])

# SOAP Hari 2
add_h3(doc, "Dokumentasi SOAP Hari ke-2 Rawat Inap (20 Oktober 2026) — Fase Stabilisasi")
headers_soap_h2 = ["Problem Medis", "Subjektif (S) & Objektif (O)", "Asesmen Farmasis (A)", "Rencana Terapi & Intervensi Farmasis (P)"]
rows_soap_h2 = [
    ["Mual Muntah ec Dispepsia", 
     "S: Mual berkurang drastis, muntah sudah berhenti, nyeri ulu hati mereda, mulai nafsu makan.\nO: Epigastric pain (-), TD 130/80 mmHg, Nadi 80x/m.",
     "Respon terapi dispepsia sangat baik. Mukosa gaster membaik dengan PPI parenteral.",
     "1. Lanjutkan Inj. Omeprazole 40 mg IV.\n2. Inj. Metoclopramide 10 mg diturunkan menjadi prn atau dihentikan.\n3. Berikan Sucralfate sirup 3x1 C ac (oral).\n4. Transisi diet lunak bertahap."],
    
    ["Hiperglikemia Rawat Inap",
     "S: Badan terasa lebih segar, tidak ada keluhan gemetar/keringat dingin (hipoglikemia (-)).\nO: GDS Pagi: 162 mg/dL, GDS Sore: 154 mg/dL.",
     "Kontrol glikemik rawat inap tercapai sempurna (target 140-180 mg/dL sesuai PERKENI & ADA).",
     "1. Lanjutkan Novorapid SC 3 x 6 Unit ac.\n2. Lanjutkan Lantus SC 1 x 10 Unit malam.\n3. Edukasi teknik penyuntikan insulin mandiri."],
    
    ["Hipertensi & Rekonsiliasi",
     "S: Tidak ada keluhan pusing.\nO: TD 130/80 mmHg.",
     "Pasien telah mampu mentoleransi asupan oral. Indikasi rekonsiliasi antihipertensi rumah.",
     "1. Berikan kembali Amlodipin tablet 10 mg 1x1 malam oral.\n2. Pantau TD serial."]
]
add_styled_table(doc, headers_soap_h2, rows_soap_h2, [Inches(1.2), Inches(1.8), Inches(1.8), Inches(2.0)])

# SOAP Hari 3
add_h3(doc, "Dokumentasi SOAP Hari ke-3 Rawat Inap (21 Oktober 2026) — Persiapan KRS & Discharge Planning")
headers_soap_h3 = ["Problem Medis", "Subjektif (S) & Objektif (O)", "Asesmen Farmasis (A)", "Rencana Terapi & Intervensi Farmasis (P)"]
rows_soap_h3 = [
    ["Kesiapan Pasien Pulang (KRS)", 
     "S: Tidak mual, tidak muntah, makan habis 1 porsi bubur, badan segar.\nO: TD 125/78 mmHg, GDS Pagi: 138 mg/dL, Elektrolit normal: Na 137 mmol/L, Cl 101 mmol/L.",
     "Kondisi klinis stabil sempurna. Mual muntah dispepsia teratasi tuntas. Glikemik dan elektrolit normal. Pasien siap KRS (Discharge Planning).",
     "1. Resep Pulang (Oral & Subkutan):\n   - Lansoprazole kapsul 30 mg 1x1 ac pagi\n   - Sucralfate sirup 3x1 C ac (selama 5 hari)\n   - Lantus SoloStar Pen 1 x 10 Unit SC malam\n   - Metformin tablet 500 mg 3x1 dc (reintroduksi aman karena fungsi ginjal & cairan normal)\n   - Amlodipin tablet 10 mg 1x1 malam PO\n2. Konseling Farmasis Pulang (KIE):\n   - Edukasi teknik injeksi insulin SoloStar, rotasi area penyuntikan, dan penyimpanan di lemari pendingin (2-8°C).\n   - Edukasi tanda-tanda hipoglikemia dan penanganan daruratnya.\n   - Edukasi pola makan teratur porsi kecil sering (small frequent meals) untuk pencegahan dispepsia berulang."]
]
add_styled_table(doc, headers_soap_h3, rows_soap_h3, [Inches(1.2), Inches(1.8), Inches(1.8), Inches(2.0)])

print("Building References Section...")

# ==========================================
# BAGIAN III: DAFTAR PUSTAKA LENGKAP
# ==========================================
add_h1(doc, "BAGIAN III: DAFTAR PUSTAKA LENGKAP (HARVARD / APA 7TH EDITION)")

references = [
    "American Diabetes Association (ADA). (2024). Standards of Care in Diabetes—2024: Diabetes Care in the Hospital (Section 16). Diabetes Care, 47(Suppl. 1), S278–S282.",
    "American Diabetes Association (ADA). (2024). Standards of Care in Diabetes—2024: Pharmacologic Approaches to Glycemic Treatment (Section 9 & 10). Diabetes Care, 47(Suppl. 1), S158–S178.",
    "American Geriatrics Society (AGS) Beers Criteria Update Expert Panel. (2023). American Geriatrics Society 2023 updated AGS Beers Criteria for potentially inappropriate medication use in older adults. Journal of the American Geriatrics Society, 71(7), 2052–2081.",
    "DiPiro, J. T., Yee, G. C., Posey, L. M., Haines, S. T., Nolin, T. D., & Ellingrod, V. (2023). DiPiro's Pharmacotherapy: A Pathophysiologic Approach (12th ed.). McGraw-Hill Education: Chapter 38 (Disorders of Sodium and Water Homeostasis), Chapter 41 (Nausea and Vomiting), Chapter 42 (Peptic Ulcer Disease and Related Disorders), Chapter 57 (Diabetes Mellitus), Chapter 60 (Osteoarthritis).",
    "Gyssens, I. C., van den Broek, P. J., Kullberg, B. J., Hekster, Y., & van der Meer, J. W. (1992). Optimizing antimicrobial therapy: Evaluation of quality of antimicrobial practice in an Indonesian university hospital. Journal of Antimicrobial Chemotherapy, 30(5), 701–709.",
    "Indonesian Rheumatology Association (IRA). (2021). Rekomendasi IRA untuk Diagnosis dan Penatalaksanaan Osteoarthritis. Perhimpunan Reumatologi Indonesia, Jakarta.",
    "Kementerian Kesehatan Republik Indonesia. (2021). Keputusan Menteri Kesehatan Republik Indonesia Nomor HK.01.07/MENKES/6485/2021 tentang Formularium Nasional. Kemenkes RI, Jakarta.",
    "Kementerian Kesehatan Republik Indonesia. (2021). Peraturan Menteri Kesehatan Republik Indonesia Nomor 28 Tahun 2021 tentang Pedoman Penggunaan Antibiotik. Kemenkes RI, Jakarta.",
    "Lexicomp Online. (2024). Lexi-Interact & Geriatric Lexi-Drugs: Metoclopramide, Domperidone, Sitagliptin, Glimepiride, Amlodipine, and NSAIDs Monograph. Wolters Kluwer Clinical Drug Information, Inc.",
    "Morisky, D. E., Ang, A., Krousel-Wood, M., & Ward, H. J. (2008). Predictive validity of a medication adherence measure in an outpatient setting. The Journal of Clinical Hypertension, 10(5), 348–354.",
    "Naranjo, C. A., Busto, U., Sellers, E. M., Sandor, P., Ruiz, I., Roberts, E. A., Janecek, E., Domecq, C., & Greenblatt, D. J. (1981). A method for estimating the probability of adverse drug reactions. Clinical Pharmacology and Therapeutics, 30(2), 239–245.",
    "Perhimpunan Dokter Spesialis Kardiovaskular Indonesia (PERKI). (2022). Panduan Tatalaksana Dislipidemia di Indonesia. Pengurus Pusat PERKI, Jakarta.",
    "Perhimpunan Dokter Spesialis Penyakit Dalam Indonesia (PAPDI). (2021). Panduan Praktik Klinis Penyakit Dalam: Pendekatan Holistik Kasus Geriatri dan Dispepsia. PAPDI, Jakarta.",
    "Perhimpunan Dokter Hipertensi Indonesia (PERHI). (2021). Konsensus Penatalaksanaan Hipertensi 2021. PERHI, Jakarta.",
    "Perhimpunan Endokrinologi Indonesia (PERKENI). (2021). Pedoman Pengelolaan dan Pencegahan Diabetes Melitus Tipe 2 Dewasa di Indonesia 2021. PB PERKENI, Jakarta: Halaman 36-39, 45-50, 98-101.",
    "Perkumpulan Gastroenterologi Indonesia (PGI). (2021/2024). Konsensus Nasional Penatalaksanaan Dispepsia dan Infeksi Helicobacter pylori di Indonesia. Pengurus Besar Perkumpulan Gastroenterologi Indonesia (PB PGI), Jakarta: Halaman 12-28.",
    "Shetty, R., Vivek, G., & Shenoy, S. (2016). Management of amlodipine-induced peripheral edema: Review of literature and clinical perspective. Journal of Clinical and Diagnostic Research, 10(7), OE01–OE04.",
    "Skovbjerg, S., Dam, C., & Christensen, K. L. (2023). Amlodipine-induced peripheral edema: Pathophysiology, incidence, and management strategies combining renin-angiotensin system inhibitors. Journal of Clinical Hypertension, 25(2), 112–119.",
    "Tolla, E. M., et al. (2026). Real-world evidence on the management of calcium channel blocker-induced peripheral edema in hypertensive patients. International Journal of Cardiology Cardiovascular Risk and Prevention, 18, 200–208.",
    "World Health Organization (WHO). (2023). The Selection and Use of Essential Medicines: WHO Technical Report Series. World Health Organization, Geneva."
]

for ref in references:
    p_ref = doc.add_paragraph()
    p_ref.paragraph_format.space_before = Pt(2)
    p_ref.paragraph_format.space_after = Pt(4)
    p_ref.paragraph_format.line_spacing = 1.15
    p_ref.paragraph_format.left_indent = Inches(0.4)
    p_ref.paragraph_format.first_line_indent = Inches(-0.4)
    run_ref = p_ref.add_run(ref)
    run_ref.font.name = "Calibri"
    run_ref.font.size = Pt(8.5)
    run_ref.font.color.rgb = RGBColor(30, 41, 59)

# Save output document
output_path = r"d:\FILE NINIS\ANALISIS_KASUS_MENDALAM_RAJAL_DAN_RANAP.docx"
doc.save(output_path)
print(f"Master DOCX successfully generated and saved to: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")

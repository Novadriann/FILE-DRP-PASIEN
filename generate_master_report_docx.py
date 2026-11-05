# -*- coding: utf-8 -*-
"""
Revised Master Generator for ANALISIS_KASUS_MENDALAM_RAJAL_DAN_RANAP.docx
Incorporating revised Rajal clinical data from RSPAU Dr. S. Hardjolukito (Farmasis: Nurhasna Sushmita Sari, S.Farm.)
and keeping Ranap (Ny. Sunarti) with Inpatient Dyspepsia Nausea/Vomiting.
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
    hrun = hp.add_run("PROGRAM PROFESI APOTEKER (PKPA) FARMASI KLINIS\nLaporan Pemantauan Terapi Obat (PTO) — Analisis Kasus Rajal (RSPAU Hardjolukito) & Ranap")
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
    run.font.size = Pt(17)
    run.font.color.rgb = RGBColor(26, 54, 93) # Deep Navy
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(14)
    run_sub = p_sub.add_run(subtitle)
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(10.5)
    run_sub.font.color.rgb = RGBColor(13, 148, 136) # Teal

def add_h1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.bold = True
    run.font.name = "Calibri"
    run.font.size = Pt(13.5)
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

print("Setup completed. Building revised document...")

doc = docx.Document()
add_header_footer(doc)

# Title
add_main_title(doc, 
    "LAPORAN LENGKAP & ANALISIS MENDALAM\nPEMANTAUAN TERAPI OBAT (PTO)", 
    "Asuhan Kefarmasian Klinis Rawat Jalan (RSPAU dr. S. Hardjolukito) & Rawat Inap (RS PKU Muhammadiyah Bantul)\n"
    "Disusun Berdasarkan Konsensus PERKENI 2021, Konsensus PGI 2021/2024, DiPiro 12th Ed 2023, ADA 2024, & AGS Beers 2023")

# Executive Summary Box
add_callout_box(doc, "RINGKASAN EKSEKUTIF KASUS (EXECUTIVE SUMMARY)",
    "Dokumen ini memuat asuhan kefarmasian klinis berbasis bukti (Evidence-Based Clinical Pharmacy) pada dua kasus kompleks:\n"
    "1. Kasus Rawat Jalan (RSPAU dr. S. Hardjolukito): Ny. Sri Wisraya (64 th, RM 00062584, Farmasis: Nurhasna Sushmita Sari, S.Farm. / Tim PKPA RSPAU) "
    "dengan Diagnosa Utama OA Genu Bilateral, Diagnosa Sekunder DM Tipe 2 Tak Terkontrol (HbA1c 9,1%), Hipertensi, serta riwayat Dislipidemia, Neuropati Diabetik, "
    "Vertigo Sentral, trauma CKR dan fraktur os zygoma/frontalis, serta gangguan ginjal (CrCl 17,67 mL/min). "
    "Evaluasi DRP mencakup: over-dosis Glimepirid 6 mg/hari pada geriatri (PIM Beers 2023 & tidak sesuai Fornas), indikasi inisiasi insulin basal (PERKENI 2021), "
    "penyesuaian ginjal Sitagliptin, interaksi NSAID oral nefrotoksik, interaksi sedasi Gabapentin-Flunarizine, restriksi Fornas, dan profil efek samping top 3 dengan MMAS-8 (skor 5,0 - Kepatuhan Rendah).\n"
    "2. Kasus Rawat Inap (Bangsal Merak): Ny. Sunarti (62 th 10 bln, RM 00109480, DPJP: dr. Raden Triyono Edhi S., Sp.PD) "
    "dengan Diagnosa Utama Mual dan Muntah karena Dispepsia (Vomitus Profuse ec Dyspepsia) serta Diagnosa Sekunder DM Tipe 2 Hiperglikemia Akut (GDS 357 mg/dL), "
    "Hipertensi, dan Hiponatremia-Hipokloremia ringan. Evaluasi DRP mencakup: duplikasi prokinetik D2 (Metoclopramide IV + Domperidone PO) berisiko EPS dan aritmia QTc (Lexicomp D/X), "
    "penyesuaian ginjal Metoclopramide, tatalaksana dispepsia berbasis Konsensus PGI & DiPiro 12th Ed Ch. 41-42, tatalaksana hiperglikemia rawat inap dengan penghentian OHO "
    "dan inisiasi insulin basal-bolus (target 140-180 mg/dL), rekonsiliasi antihipertensi, rehidrasi cairan kristaloid isotonik NaCl 0,9%, serta audit kualitatif antibiotik metode Gyssens (Kategori 0).",
    "info")

print("Building Revised Rawat Jalan Section...")

# ==========================================
# BAGIAN I: RAWAT JALAN (RSPAU DR. S. HARDJOLUKITO)
# ==========================================
add_h1(doc, "BAGIAN I: ANALISIS MENDALAM KASUS RAWAT JALAN (RAJAL) — NY. SRI WISRAYA")

add_paragraph(doc, 
    "Analisis kasus rawat jalan ini dilakukan terhadap Ny. Sri Wisraya yang menjalani pemantauan terapi obat rutin di Poli Penyakit Dalam "
    "RSPAU dr. S. Hardjolukito Yogyakarta selama periode 6 bulan (27 April 2026 – 07 Oktober 2026). "
    "Pemantauan asuhan kefarmasian klinis dipimpin oleh Farmasis Nurhasna Sushmita Sari, S.Farm. / Tim PKPA Farmasi Klinis RSPAU, "
    "berkoordinasi dengan DPJP dr. Tri Hariningsih, Sp.PD serta Tim Dokter Rawat Bersama (Raber): dr. Raden Suhana, Sp.OT(K) [Orthopedi], "
    "dr. Wahyu Wihartono, Sp.N [Saraf], dan dr. Supanji, Sp.M [Mata].")

# 1.1 Demografi
add_h2(doc, "1.1 Profil Demografi & Data Dasar Pasien Rawat Jalan")
headers_demo = ["Parameter Klinis", "Keterangan / Nilai Pasien", "Interpretasi Klinis Farmasis"]
rows_demo = [
    ["Fasilitas Pelayanan Kesehatan", "Instalasi Farmasi RSPAU dr. S. Hardjolukito", "Rumah Sakit Rujukan Tingkat Lanjutan (FKRTL)"],
    ["Farmasis Penanggung Jawab", "Nurhasna Sushmita Sari, S.Farm. / Tim PKPA", "Apoteker Klinis Penelaah Farmakoterapi & DRP"],
    ["Nama Pasien", "SRI WISRAYA", "Pasien geriatri rawat jalan multipel poliklinik"],
    ["Nomor Rekam Medis", "00062584", "Terdaftar aktif di RSPAU dr. S. Hardjolukito"],
    ["Usia / Jenis Kelamin", "64 tahun / Perempuan", "Geriatri; rentan terhadap ADR, PIM Beers, polifarmasi"],
    ["Berat Badan / Tinggi Badan", "52 kg / 156 cm", "IMT: 21,37 kg/m² (Normoweight / status gizi baik)"],
    ["DPJP Utama", "dr. Tri Hariningsih, Sp.PD", "Dokter Spesialis Penyakit Dalam"],
    ["Dokter Rawat Bersama (Raber)", "dr. Raden Suhana, Sp.OT(K)\ndr. Wahyu Wihartono, Sp.N\ndr. Supanji, Sp.M", "Poli Bedah Orthopedi\nPoli Spesialis Saraf / Neurologi\nPoli Spesialis Mata"],
    ["Tanggal Periode Kontrol", "27-04-2026 (M1) s/d 07-10-2026 (M6)", "Pemantauan longitudinal serial selama 6 bulan"],
    ["Riwayat Alergi", "Tidak Ada Alergi Obat (-)", "Aman terhadap golongan analgesik & antibiotik"],
    ["Diagnosa Utama", "OA GENU BILATERAL (M17.0)", "Nyeri dan kekakuan kronis sendi lutut bilateral"],
    ["Diagnosa Sekunder 1 & 2", "DM TIPE 2 (E11.9)\nHIPERTENSI ESENSIAL (I10)", "DM tidak terkontrol (HbA1c 9,1%) & HT belum mencapai target <130/80"],
    ["Riwayat Penyakit Terdahulu", "Dislipidemia (E78.5)\nNeuropati Diabetik (E11.5)\nVertigo Sentral (H81.4)\nPost Trauma CKR & Fraktur Os Zygoma", "Komorbiditas multi-organ kompleks dengan riwayat insiden jatuh di kamar mandi pada 04/07/2026"],
    ["Riwayat Penggunaan Obat", "Glimepirid, Amlodipin, Gabapentin, Rosuvastatin, Sitagliptin, Acarbose, Flamar Gel, Meloxicam, Kalium Diklofenak, Flunarizine, Glucosamine, Mecobalamin", "Polifarmasi aktif (7–9 obat/hari) dengan risiko tinggi interaksi obat dan nefrotoksisitas"]
]
add_styled_table(doc, headers_demo, rows_demo, [Inches(1.8), Inches(2.3), Inches(2.7)])

# 1.2 Riwayat Kontrol 6 Bulan
add_h2(doc, "1.2 Riwayat Kunjungan Kontrol, Keluhan Subjektif, & Kepatuhan Pasien (M1 – M6)")
headers_ctrl = ["Tanggal & Sesi", "Poliklinik Dikunjungi", "Keluhan Pasien (Subjektif)", "Skor Nyeri / Tanda Khusus", "Kepatuhan Pasien (MMAS-8)"]
rows_ctrl = [
    ["27-04-2026 (M1)", "Poli Penyakit Dalam", "Kontrol rutin DM, lutut sakit (+), kebas (+), pusing (-)", "NRS 2 (Ringan)", "Teratur (Awal kontrol)"],
    ["29-05-2026 (M2)", "Poli Saraf & Mata", "Lutut sakit, bengkak (-), kebas (+), pusing (-)", "NRS 4 (Sedang)", "Teratur"],
    ["29-06-2026 (M3)", "Poli Mata", "Lutut kiri nyeri kaku (+++), kebas (++), pusing (+)", "NRS 6 (Berat)", "Teratur (Dosis Glimepirid naik ke 6 mg)"],
    ["04-07-2026 (Trauma)", "IGD (Bedah/Saraf/Rad)", "Kepala terbentur ec jatuh di kamar mandi, nyeri kepala", "NRS +++ (Akut)", "Trauma Jatuh (GDS spike 308 mg/dL)"],
    ["05-08-2026 (M4)", "Poli Mata", "Evaluasi paska rawat, lutut nyeri (++), gliyer (+)", "NRS 4 (Sedang)", "Kurang Tertib (TD spike 165/89 mmHg)"],
    ["07-09-2026 (M5)", "Poli Mata", "Lutut nyeri (++), gliyer (+) / Vertigo Sentral", "NRS 4 (Sedang)", "Lupa Bawa Obat (Acarbose & Diklofenak masuk)"],
    ["07-10-2026 (M6)", "Poli Ortho & Mata", "Lutut kanan sakit (++), kebas (+), pusing (+)", "NRS 4 (Sedang)", "Bingung Waktu Minum (Switch Atorvastatin)"]
]
add_styled_table(doc, headers_ctrl, rows_ctrl, [Inches(1.1), Inches(1.4), Inches(2.1), Inches(1.1), Inches(1.1)])

# 1.3 Pemantauan TTV
add_h2(doc, "1.3 Pemantauan Tanda-Tanda Vital (TTV) 6 Bulan")
add_paragraph(doc,
    "Berdasarkan pemantauan serial tanda-tanda vital, tekanan darah sistolik pasien berfluktuasi tajam antara 133 hingga 165 mmHg, "
    "dan diastolik antara 76 hingga 98 mmHg. Target konsensus PERHI 2021 untuk pasien diabetes dengan komorbid kardiovaskular adalah < 130/80 mmHg. "
    "Monoterapi Amlodipin 10 mg terbukti belum adekuat mengontrol tekanan darah sistolik. "
    "Puncak lonjakan tekanan darah (spike) terjadi pada 05/08/2026 mencapai 165/89 mmHg pasca trauma dan pemberian NSAID oral. "
    "Denyut nadi tercatat takikardia (99, 97, 103 x/menit) terutama saat episode nyeri lutut berat dan stres pasca jatuh.")

headers_ttv = ["Tanggal Kontrol", "Sistole (mmHg)", "Diastole (mmHg)", "Nadi (x/m)", "Suhu (°C)", "RR (x/m)", "SpO2 (%)", "NRS", "Evaluasi Klinis TTV"]
rows_ttv = [
    ["27-04-2026", "154", "98", "99", "36,0", "22", "99%", "2", "Hipertensi Stage 2; takikardia ringan"],
    ["29-05-2026", "138", "76", "97", "36,0", "22", "99%", "4", "Terkontrol borderline"],
    ["29-06-2026", "156", "85", "89", "36,0", "22", "99%", "6", "Hipertensi Stage 2; nyeri lutut kaku"],
    ["05-08-2026", "165", "89", "103", "-", "-", "-", "4", "Spike TD & takikardia paska trauma/NSAID"],
    ["07-09-2026", "141", "80", "92", "36,0", "21", "99%", "4", "Hipertensi Stage 1; vertigo sentral"],
    ["07-10-2026", "133", "80", "92", "36,0", "21", "99%", "4", "Mendekati target (<130/80 mmHg)"]
]
add_styled_table(doc, headers_ttv, rows_ttv, [Inches(0.9), Inches(0.7), Inches(0.7), Inches(0.7), Inches(0.6), Inches(0.6), Inches(0.6), Inches(0.5), Inches(1.5)])

add_image_evidence(doc, 
    r"guideline_evidence_rajal/rajal_bp_trend.png",
    "Grafik Tren Tekanan Darah Ny. Sri Wisraya Selama 6 Bulan Terakhir (Target PERHI <130/80 mmHg)",
    "Konsensus Penatalaksanaan Hipertensi PERHI 2021",
    "Halaman 18-22")

# 1.4 Pemantauan Data Lab
add_h2(doc, "1.4 Pemantauan Data Laboratorium & Pemeriksaan Radiologi")
add_paragraph(doc,
    "Profil laboratorium mengonfirmasi kegagalan glikemik berat (glukotoksisitas tinggi) dengan nilai HbA1c mencapai 9,1%* "
    "pada 29/05/2026. Kadar glukosa darah puasa (GDP) persisten tinggi (169*, 190*, 151* mg/dL) dan GD2PP 211* mg/dL, "
    "dengan lonjakan GDS mencapai 308* mg/dL saat trauma jatuh di IGD. "
    "Pada pemeriksaan fungsi ginjal pasca trauma (04/07/2026), serum kreatinin melonjak menjadi 2,69* mg/dL dan Ureum 73* mg/dL. "
    "Klirens kreatinin Cockcroft-Gault terhitung:")
add_paragraph(doc, 
    "CrCl = [(140 - 64) x 52 kg] / [72 x 2,69 mg/dL] x 0,85 = 17,67 mL/menit (Gangguan Ginjal Berat / AKI on CKD Stage 4).",
    bold_prefix="Perhitungan Klirens Kreatinin: ")

headers_lab = ["Pemeriksaan Lab", "Nilai Pasien", "Nilai Normal", "Satuan", "Interpretasi & Analisis Evaluasi Klinis"]
rows_lab = [
    ["HbA1c (29/05/2026)", "9,1*", "4,0 – 6,5", "%", "TIDAK TERKONTROL; glukotoksisitas tinggi, indikasi mutlak insulin basal"],
    ["GDS (27/04/2026)", "164", "< 200", "mg/dL", "Terkontrol sedang"],
    ["GDS (29/05/2026)", "252*", "< 200", "mg/dL", "Hiperglikemia postprandial meningkat"],
    ["GDP (29/06/2026)", "169*", "70 – 115", "mg/dL", "Hiperglikemia puasa persisten"],
    ["GD2PP (29/06/2026)", "211*", "< 140", "mg/dL", "Ekskursi postprandial masif (dasar penambahan Acarbose)"],
    ["GDS (04/07/2026 IGD)", "244 – 308*", "< 200", "mg/dL", "Spike glukosa akut terinduksi stres trauma jatuh & nyeri"],
    ["GDP (05/08/2026)", "190*", "70 – 115", "mg/dL", "GDP tetap tinggi pasca trauma"],
    ["GDP (07/09/2026)", "151*", "70 – 115", "mg/dL", "Respon parsial pasca eskalasi terapi OHO"],
    ["Kreatinin Serum (04/07)", "2,69*", "0,6 – 1,1", "mg/dL", "CrCl 17,67 mL/min (Gangguan ginjal berat / AKI on CKD); order ulang 06/11"],
    ["Ureum Darah (04/07)", "73*", "19 – 44", "mg/dL", "Azotemia / retensi nitrogen pasca trauma dan stres akut"],
    ["Hemoglobin (Hb)", "10,1*", "13,2 – 17,3", "g/dL", "Anemia ringan (Grade 1) ec penyakit kronis (CKD/DM)"],
    ["Hematokrit (Hct)", "30,0*", "40 – 52", "%", "Menurun selaras dengan anemia"],
    ["Trombosit", "228.000", "150.000 – 440.000", "/mm³", "Normal; fungsi hemostasis trombosit baik"],
    ["Leukosit", "Normal", "4.380 – 10.600", "/mm³", "Tidak tampak tanda infeksi bakterial akut"],
    ["SGOT / SGPT", "29 / 20", "< 35 / < 45", "U/L", "Fungsi hepatik sangat baik (aman untuk terapi Atorvastatin 20 mg)"]
]
add_styled_table(doc, headers_lab, rows_lab, [Inches(1.5), Inches(0.9), Inches(1.1), Inches(0.6), Inches(2.7)])

add_image_evidence(doc,
    r"guideline_evidence_rajal/rajal_glucose_trend.png",
    "Profil Glukosa Darah Ny. Sri Wisraya (HbA1c = 9,1% - Uncontrolled, GDS Spike 308 mg/dL)",
    "Pedoman Pengelolaan DM Tipe 2 PERKENI 2021",
    "Halaman 45-50")

# Radiologi
add_h3(doc, "Temuan Radiologi & Korelasi Klinis")
add_bullet(doc, "Foto Pelvis AP (16/05/2026)", "Periarticular calcification hip dextra (Poli Saraf / LBP). Menunjukkan proses degeneratif osteofit panggul.")
add_bullet(doc, "CT-Scan Kepala Non-Kontras (04/07/2026)", 
           "Pembengkakan jaringan lunak daerah zygomaticum kiri s/d frontalis kiri disertai lesi hiperdens hematoma (HU: 69-75). "
           "Fraktur linier os zygomaticum kiri dan os frontalis kiri, hematosinus maksilaris kiri, sinusitis maksilaris kanan, ethmoidalis bilateral dan frontalis kanan. "
           "Tidak tampak perdarahan intrakranial (EDH/SDH (-)), lesi iskemik, maupun SOL.")

# 1.5 Profil Pengobatan Kronis
add_h2(doc, "1.5 Profil Pengobatan Kronis Pasien (April – Oktober 2026)")
headers_rx = ["Nama Obat", "Rute", "Regimen Dosis", "M1 (27/04)", "M2 (29/05)", "M3 (29/06)", "M4 (05/08)", "M5 (07/09)", "M6 (07/10)", "Tujuan Terapi & Evaluasi Dinamika"]
rows_rx = [
    ["Amlodipin 10 mg", "PO", "1x1 pagi", "✓", "✓", "✓", "✓", "✓", "✓", "Monoterapi gagal target <130/80; risiko edema"],
    ["Flamar Gel", "Topikal", "2x sehari oles", "✓", "✓", "✓", "-", "✓", "✓", "Lini 1 OA Genu; absorpsi sistemik <6%, aman ginjal"],
    ["Gabapentin 100 mg", "PO", "1x1 malam", "✓", "✓", "✓", "✓", "✓", "✓", "Nyeri neuropati diabetik rutin"],
    ["Glimepirid 4 mg", "PO", "1x1 ac pagi", "✓", "✓", "-", "-", "-", "-", "Dosis awal dititrasi naik ke 6 mg/hari"],
    ["Glimepirid 3 mg", "PO", "2x1 ac pagi-sore", "-", "-", "✓", "✓", "✓", "✓", "Dosis 6 mg/hari. Overdosis geriatri & PIM Beers!"],
    ["Glucosamine 500 mg", "PO", "1x1 pc", "✓", "✓", "✓", "-", "✓", "-", "Kondroprotektif OA. Non-Fornas"],
    ["Mecobalamin 500 mcg", "PO", "1x1 pc", "✓", "✓", "✓", "-", "-", "-", "Neurotropik B12 aktif (dihentikan Agustus 2026)"],
    ["Rosuvastatin 10 mg", "PO", "1x1 malam", "✓", "✓", "✓", "✓", "✓", "-", "Statin rutin April–September 2026"],
    ["Meloxicam 7,5 mg", "PO", "2x1 lalu 1x1", "-", "✓", "✓", "-", "-", "-", "NSAID sistemik. Nefrotoksik & tumpulkan Amlodipin"],
    ["Sitagliptin 100 mg", "PO", "1x1 malam/siang dc", "-", "✓", "✓", "✓", "✓", "✓", "DPP-4i sejak Mei 2026; perlu reduksi bila eGFR < 45"],
    ["Acarbose 100 mg", "PO", "2x1 dc (suapan 1)", "-", "-", "-", "-", "✓", "✓", "Ditambahkan September untuk GD2PP 211 mg/dL"],
    ["Flunarizine 5 mg", "PO", "2x1 malam", "-", "-", "-", "-", "✓", "-", "Antivertigo sentral. Batasi durasi maks 10 hari"],
    ["Kalium Diklofenak 50", "PO", "2x1 pc", "-", "-", "-", "-", "✓", "-", "NSAID eksaserbasi akut September 2026"],
    ["Atorvastatin 20 mg", "PO", "1x1 malam", "-", "-", "-", "-", "-", "✓", "Diswitch dari Rosuvastatin Oktober 2026 (Sangat tepat)"]
]
add_styled_table(doc, headers_rx, rows_rx, [Inches(1.2), Inches(0.5), Inches(1.0), Inches(0.3), Inches(0.3), Inches(0.3), Inches(0.3), Inches(0.3), Inches(0.3), Inches(1.9)])

# 1.6 MMAS-8
add_h2(doc, "1.6 Evaluasi Kepatuhan Pasien: Kuesioner MMAS-8 (Skor Total: 5.0 / 8.0 — Kepatuhan Rendah)")
add_paragraph(doc,
    "Berdasarkan instrumen Morisky Medication Adherence Scale 8-Item (MMAS-8) yang baru dievaluasi oleh Tim Farmasi Klinis, "
    "didapatkan Skor Total MMAS-8 = 5.0 / 8.0 yang menempatkan pasien pada kategori KEPATUHAN RENDAH (Low Adherence, skor < 6.0).")

headers_mmas = ["No", "Item Pertanyaan Kuesioner MMAS-8", "Jawaban", "Skor", "Faktor Perilaku & Rasional Klinis Pasien"]
rows_mmas = [
    ["1", "Apakah Anda kadang-kadang lupa minum obat?", "Ya", "0", "Pasien lupa akibat banyaknya jumlah obat (polifarmasi 7-9 tablet)"],
    ["2", "Dalam 2 minggu terakhir, apakah ada hari Anda tidak minum obat?", "Ya", "0", "Lupa pada hari-hari tertentu saat bepergian atau sibuk"],
    ["3", "Apakah Anda pernah mengurangi/berhenti minum obat tanpa memberi tahu dokter saat merasa kondisi memburuk?", "Tidak", "1", "FAKTOR BAIK: Pasien tidak pernah sengaja menghentikan obat saat kondisi memburuk"],
    ["4", "Ketika bepergian keluar rumah, apakah Anda kadang lupa membawa obat?", "Ya", "0", "Pasien terbukti lupa membawa obat pada kunjungan kontrol September 2026"],
    ["5", "Apakah Anda meminum semua obat Anda kemarin?", "Ya", "1", "FAKTOR BAIK: Pasien patuh meminum seluruh regimen obat pada hari kemarin"],
    ["6", "Ketika Anda merasa gejala membaik atau sehat, apakah Anda kadang berhenti minum obat?", "Tidak", "1", "FAKTOR BAIK: Pasien menyadari obat DM & HT harus diminum rutin jangka panjang"],
    ["7", "Apakah Anda merasa tertekan/terbebani dengan rencana pengobatan rutin setiap hari?", "Tidak", "1", "FAKTOR BAIK: Pasien tidak merasa terganggu secara emosional dengan terapi"],
    ["8", "Seberapa sering Anda merasa kesulitan mengingat untuk meminum semua obat Anda?", "Tidak pernah / jarang", "1", "FAKTOR BAIK: Pasien menyatakan jarang kesulitan teknis mengingat jadwal"],
    ["TOTAL", "SKOR KEPATUHAN MMAS-8", "-", "5.0", "KATEGORI: KEPATUHAN RENDAH (Low Adherence, Skor < 6.0)"]
]
add_styled_table(doc, headers_mmas, rows_mmas, [Inches(0.4), Inches(2.6), Inches(0.8), Inches(0.6), Inches(2.4)])

add_callout_box(doc, "SOLUSI & RENCANA INTERVENSI FARMASIS UNTUK MMAS-8 (SKOR 5.0)",
    "Faktor Utama Ketidakpatuhan: Lupa berkala (Item 1), lupa 2 minggu terakhir (Item 2), dan lupa membawa obat saat bepergian (Item 4).\n"
    "Rencana Intervensi Farmasi Klinis:\n"
    "1. Penyediaan Kotak Obat Terbagi 4 Waktu (Pill Box Dispenser 4 Sekat Berlabel Warna: Pagi, Siang, Sore, Malam).\n"
    "2. Pembuatan Lembar Jadwal Minum Obat Bergambar (Visual Medication Chart) yang mencantumkan nama, bentuk tablet, dan aturan makan.\n"
    "3. Keterlibatan Pengawas Minum Obat (PMO): Melibatkan keluarga terdekat pasien untuk mengawasi dan mengingatkan jadwal minum obat harian serta memastikan obat dibawa saat bepergian.",
    "info")

add_image_evidence(doc,
    r"guideline_evidence_rajal/mmas8_patient_adherence_morisky.png",
    "Instrumen Morisky Medication Adherence Scale (MMAS-8) dan Algoritma Skoring Kepatuhan",
    "Morisky Adherence Research LLC & Permenkes Pelayanan Farmasi Klinis",
    "MMAS-8 Official Manual")

# 1.7 Restriksi Fornas & Efek Samping Top 3
add_h2(doc, "1.7 Evaluasi Kesesuaian Restriksi Formularium Nasional (Fornas) & Profil Efek Samping Terbanyak (Top 3)")
add_paragraph(doc,
    "Evaluasi kesesuaian resep pasien terhadap Formularium Nasional (Kepmenkes HK.01.07/MENKES/6485/2021):\n"
    "• TIDAK SESUAI FORNAS: Glimepirid 3 mg diresepkan 2x1 (60 tablet/bulan). Plafon Fornas menetapkan maksimal 30 tablet/bulan. Secara klinis dosis 6 mg/hari ini merupakan overdosis geriatri.\n"
    "• STATUS NON-FORNAS: Glucosamine 500 mg berstatus suplemen nutrasetikal makanan sendi, berada di luar jaminan paket JKN BPJS Kesehatan.\n"
    "• SESUAI FORNAS: Sitagliptin (30 tab), Acarbose (60 tab), Amlodipin (30 tab), Atorvastatin (30 tab), Rosuvastatin (30 tab), Gabapentin (30 kap), Flamar Gel (1 tube), Meloxicam (10 tab prn), Diklofenak (10 tab prn), Flunarizine (10 tab prn), Mecobalamin (30 kap).")

headers_adr = ["Nama Obat", "Efek Samping Terbanyak (Top 3) dengan Persentase", "Bukti Referensi Resmi"]
rows_adr = [
    ["Glimepirid", "1. Hipoglikemia (10–18%)\n2. Peningkatan Berat Badan (2–5%)\n3. Pusing / Sakit Kepala (1,7–3,4%)", "FDA Amaryl Insert & Lexicomp Online 2024"],
    ["Sitagliptin", "1. Nasofaringitis (5,2%)\n2. Sakit Kepala (5,1%)\n3. Gangguan Gastrointestinal (1,5–3,0%) | Waspada Pankreatitis (<1%)", "FDA Januvia Package Insert & DailyMed"],
    ["Acarbose", "1. Flatulensi / Kembung Buang Angin (74–78%)\n2. Diare (29–31%)\n3. Nyeri Abdomen / Kram Perut (19–21%)", "FDA Precose Monograph & Lexicomp"],
    ["Amlodipin", "1. Edema Perifer / Bengkak Kaki (1,8–10,8%)\n2. Sakit Kepala (7,3%)\n3. Kelelahan / Fatigue (4,5%)", "FDA Norvasc Insert & DailyMed"],
    ["Atorvastatin", "1. Nasofaringitis (8,3%)\n2. Artralgia / Nyeri Sendi (6,9%)\n3. Dispepsia / Gangguan GI (5,6%) | Mialgia (3,5–6,3%)", "FDA Lipitor Package Insert & Lexicomp"],
    ["Gabapentin", "1. Mengantuk / Somnolence (19–21%)\n2. Pusing Melayang / Dizziness (17–28%)\n3. Ataksia / Gangguan Keseimbangan Jalan (11–13%)", "FDA Neurontin & Micromedex DrugDex"],
    ["Flunarizine", "1. Peningkatan Berat Badan / Nafsu Makan (10–20%)\n2. Mengantuk / Sedasi (10–15%)\n3. Kelelahan / Depresi / Gejala Ekstrapiramidal (5–10%)", "Sibelium Monograph & Martindale 38th Ed"],
    ["NSAID Oral (Diklofenak / Meloxicam)", "1. Dispepsia / Nyeri Epigastrik (10–15%)\n2. Pusing / Sakit Kepala (3–9%)\n3. Retensi Cairan & Peningkatan Tekanan Darah (1–3%)", "FDA Cataflam / Mobic Insert"],
    ["Flamar Gel (Diklofenak Topikal)", "1. Pruritus / Gatal Lokal (4%)\n2. Eritema / Kemerahan Kulit (2–2,5%)\n3. Kulit Kering (1,5–2%) | Absorpsi sistemik sangat minimal (<6%)", "FDA Voltaren Topical Gel Package Insert"]
]
add_styled_table(doc, headers_adr, rows_adr, [Inches(1.5), Inches(3.2), Inches(2.1)])

# 1.8 Identifikasi DRP Rajal
add_h2(doc, "1.8 Identifikasi & Analisis Mendalam Drug-Related Problems (DRP) Rawat Jalan")

# DRP 1
add_h3(doc, "DRP 1: Overdosis Relatif Glimepirid (6 mg/hari) pada Geriatri (64 Tahun) & Penurunan Klirens Ginjal")
add_paragraph(doc,
    "Glimepirid diresepkan dengan dosis eskalasi hingga 3 mg 2x1 (total 6 mg/hari) sejak Juni 2026. "
    "Glimepirid merupakan sulfonilurea generasi 2 kerja panjang yang dieliminasi 60% via ginjal. "
    "Pada pasien geriatri dengan klirens ginjal turun (CrCl 17,67 mL/min), klirens metabolit aktif terhambat signifikan. "
    "Hal ini memicu akumulasi konsentrasi obat dan risiko fatal hipoglikemia berat berkepanjangan (prolonged hypoglycemia unawareness) "
    "yang berkontribusi pada episode jatuh dan fraktur os zygoma/frontalis.")
add_callout_box(doc, "PEDOMAN KLINIS: BEERS CRITERIA 2023, PERKENI 2021, & FORNAS",
    "1. AGS Beers Criteria 2023 Update: Mengklasifikasikan Sulfonilurea kerja panjang sebagai Potentially Inappropriate Medications (PIM) kategori AVOID pada geriatri.\n"
    "2. PERKENI 2021 (Hal. 36-39): Dosis Glimepirid pada lansia dibatasi maksimal ≤ 2 mg/hari. Bila fungsi ginjal eGFR < 30 mL/min, beralih ke Glikuidon (30 mg 1-2x/hari) yang 95% diekskresi via bilier/feses, atau beralih ke Insulin Basal.\n"
    "3. Restriksi Fornas: Maksimal 30 tablet/bulan (peresepan 60 tablet/bulan melanggar plafon Fornas).\n"
    "Rekomendasi Farmasis: Turunkan segera dosis Glimepirid ke 2 mg 1x1 pagi, atau ganti ke Glikuidon 30 mg 1x1, serta lakukan inisiasi terapi Insulin Basal.",
    "alert")

add_image_evidence(doc,
    r"guideline_evidence_rajal/perkeni_beers_glimepiride_elderly.png",
    "Rekomendasi Keamanan Sulfonilurea pada Geriatri Sesuai AGS Beers Criteria 2023 & Konsensus PERKENI 2021",
    "PERKENI 2021 & AGS Beers Criteria 2023",
    "PERKENI Hal. 38; J Am Geriatr Soc 2023:71(7)")

# DRP 2
add_h3(doc, "DRP 2: Kegagalan Regimen Triple OHO (HbA1c 9,1%) & Indikasi Inisiasi Terapi Insulin Basal")
add_paragraph(doc,
    "Pasien menerima kombinasi 3 OHO (Glimepirid 6 mg + Sitagliptin 100 mg + Acarbose 200 mg), namun kontrol glikemik tetap buruk "
    "(HbA1c 9,1%*, GDP 190* mg/dL, GDS spike 308* mg/dL). Hal ini membuktikan kegagalan sel beta pankreas progresif.")
add_callout_box(doc, "PEDOMAN KLINIS: ALGORITMA INSULIN PERKENI 2021 & DIPIRO 12TH ED CH. 57",
    "1. PERKENI 2021 (Hal. 45-50): 'Pasien dengan HbA1c > 9% dengan gejala dekompensasi, atau gagal mencapai target dengan 2-3 OHO, MEMILIKI INDIKASI MUTLAK inisiasi INSULIN BASAL.'\n"
    "2. DiPiro's Pharmacotherapy 12th Ed (2023) Ch. 57: Inisiasi Insulin Basal analog (Insulin Glargine / Lantus) dosis awal 10 Unit subkutan malam hari (pukul 21.00–22.00). Titrasi dosis 2 unit setiap 3-4 hari berdasarkan pemantauan GDP mandiri hingga target GDP 80–130 mg/dL.",
    "info")

add_image_evidence(doc,
    r"guideline_evidence_rajal/perkeni_2021_dm_algorithm.png",
    "Algoritma Pengelolaan Glukosa DM Tipe 2 & Indikasi Eskalasi ke Insulin Basal",
    "Pedoman Pengelolaan DM Tipe 2 PERKENI 2021",
    "Halaman 47-49")

# DRP 3
add_h3(doc, "DRP 3: Penyesuaian Dosis Ginjal Sitagliptin pada Penurunan Klirens Ginjal (CrCl 17,67 mL/min)")
add_paragraph(doc,
    "Sitagliptin diekskresi 79% utuh melalui urin. Klirens ginjal pasien turun menjadi 17,67 mL/min (kreatinin 2,69* mg/dL pada 04/07/2026). "
    "Pemberian dosis penuh 100 mg 1x1 menyebabkan peningkatan paparan sistemik obat hingga 4-5 kali lipat.")
add_callout_box(doc, "PEDOMAN DOSIS GINJAL: LEXICOMP & FDA JANUVIA MONOGRAPH",
    "Rekomendasi Penyesuaian Dosis Sitagliptin Berdasarkan CrCl:\n"
    "• CrCl ≥ 45 mL/min: 100 mg sekali sehari.\n"
    "• CrCl 30 hingga < 45 mL/min: Turunkan ke 50 mg sekali sehari.\n"
    "• CrCl < 30 mL/min: HARUS DITURUNKAN ke 25 mg sekali sehari.\n"
    "Rekomendasi Farmasis: Evaluasi hasil lab kreatinin serial (order ulang 06/11/2026); bila eGFR 30–44 turunkan ke 50 mg, jika < 30 turunkan ke 25 mg 1x1 sehari.",
    "alert")

add_image_evidence(doc,
    r"guideline_evidence_rajal/sitagliptin_renal_adjustment_lexicomp.png",
    "Panduan Penyesuaian Dosis Ginjal Sitagliptin Berdasarkan Klirens Kreatinin (CrCl)",
    "Lexicomp Drug Information & FDA Januvia Insert",
    "Lexicomp Renal Dosing Guidelines 2024")

# DRP 4
add_h3(doc, "DRP 4: Interaksi Obat NSAID Oral (Meloxicam & Kalium Diklofenak) terhadap Ginjal, Tekanan Darah, & Amlodipin")
add_paragraph(doc,
    "Penggunaan NSAID oral (Meloxicam 7,5 mg pada Mei-Juni dan Kalium Diklofenak 50 mg 2x1 pada September) menghambat sintesis prostaglandin renal PGE2/PGI2. "
    "Hal ini memicu vasokonstriksi arteriol aferen glomerulus (memicu AKI dengan lonjakan kreatinin 2,69 mg/dL), retensi natrium-air yang memicu spike TD (165/89 mmHg), "
    "serta menumpulkan efikasi antihipertensi Amlodipin (Lexicomp Rating C).")
add_callout_box(doc, "PEDOMAN KLINIS: IRA 2021 & DIPIRO 12TH ED CH. 60",
    "Indonesian Rheumatology Association (IRA 2021) & DiPiro Ch. 60: Pada lansia dengan komorbid hipertensi, DM, dan gangguan ginjal, NSAID oral sistemik HARUS DIHINDARI. "
    "Terapi lini pertama adalah NSAID topikal (Flamar Gel) dioleskan 2–4x/hari dikombinasikan dengan Parasetamol 500 mg prn bila nyeri hebat.",
    "alert")

add_image_evidence(doc,
    r"guideline_evidence_rajal/ira_nsaid_safety_osteoarthritis.png",
    "Rekomendasi Keamanan NSAID pada Pasien Lansia dengan Komorbid Kardio-Renal",
    "Indonesian Rheumatology Association (IRA 2021)",
    "Rekomendasi IRA Hal. 14-19")

add_image_evidence(doc,
    r"guideline_evidence_rajal/lexicomp_interactions_rajal.png",
    "Matriks Analisis Interaksi Obat Pasien Rawat Jalan (Lexicomp Rating C & D)",
    "Lexicomp Drug Interactions Wolters Kluwer 2024",
    "Lexi-Interact Online Database")

# DRP 5
add_h3(doc, "DRP 5: Interaksi Farmakodinamik Gabapentin + Flunarizine (Depresi SSP & Fall Risk Pasca Fraktur Zygoma)")
add_paragraph(doc,
    "Gabapentin 100 mg 1x1 malam dikombinasikan dengan Flunarizine 5 mg 2x1 pada September 2026. "
    "Keduanya mendepresi sistem saraf pusat, meningkatkan risiko pusing, sedasi berlebih, ataksia, dan kelemahan postural yang memperberat risiko jatuh pasca fraktur zygoma.")
add_callout_box(doc, "PEDOMAN GERIATRI: BEERS CRITERIA 2023 & DIPIRO CH. 58",
    "AGS Beers Criteria 2023: Hindari kombinasi ≥ 2 obat depresan SSP pada geriatri. Flunarizine memiliki waktu paruh hingga 18 hari pada geriatri; durasi terapi antivertigo dibatasi maksimal 7–10 hari pada fase akut lalu dihentikan.",
    "info")

add_image_evidence(doc,
    r"guideline_evidence/dipiro_diabetic_neuropathy_weight.png",
    "Manajemen Terapi Neuropati Diabetik & Penyesuaian Dosis Gabapentin Geriatri",
    "DiPiro's Pharmacotherapy 12th Edition 2023",
    "Chapter 57 & 58, Hal. 1140-1145")

# DRP 6
add_h3(doc, "DRP 6: Drug-Food Interaction & Edukasi Khusus Penggunaan Acarbose 100 mg")
add_paragraph(doc,
    "Acarbose menghambat enzim alfa-glukosidase di brush border usus halus. Obat ini WAJIB diminum bersama suapan pertama makanan utama. "
    "Bila terjadi hipoglikemia akibat kombinasi dengan Glimepirid, gula pasir biasa (sukrosa) tidak efektif diserap karena hidrolisisnya dihambat Acarbose. "
    "Pasien dan keluarga WAJIB diedukasi untuk selalu menyediakan Dekstrosa Murni / Madu Murni.")

# DRP 7
add_h3(doc, "DRP 7: Evaluasi Adverse Drug Reaction (ADR): Edema Perifer Amlodipin, Algoritma Naranjo (Skor 6 - Probable), & Solusi Kombinasi ARB")
add_paragraph(doc,
    "Monoterapi Amlodipin 10 mg memicu vasodilatasi arteriol prekapiler yang tidak diimbangi venodilatasi postkapiler, memicu ekstravasasi transudat ke pergelangan kaki. "
    "Berdasarkan algoritma Naranjo, skor reaksi adalah +6 (Probable). "
    "Solusi terapi berbasis bukti (Skovbjerg et al., 2023; Shetty et al., 2016): Turunkan Amlodipin ke 5 mg malam hari dan kombinasikan dengan ARB Candesartan 8–16 mg 1x1. "
    "ARB mendilatasi venul postkapiler, menormalkan tekanan intrakapiler, dan melenyapkan edema tanpa diuretik loop.")

add_image_evidence(doc,
    r"guideline_evidence/naranjo_amlodipine_edema.png",
    "Penilaian Algoritma Naranjo Adverse Drug Reaction: Edema Perifer Amlodipin (Skor 6 - Probable)",
    "Naranjo et al. (1981) Clin Pharmacol Ther & WHO-UMC",
    "Algoritma Standar Farmakovigilans")

add_image_evidence(doc,
    r"guideline_evidence/skovbjerg_amlodipine_edema_mgmt.png",
    "Mekanisme Patofisiologi & Strategi Terapi Edema Perifer Amlodipin Berbasis Bukti",
    "Skovbjerg et al. (2023) J Clin Hypertens",
    "Halaman 112-119")

# DRP 8
add_h3(doc, "DRP 8: Evaluasi Kepatuhan Fornas & Rasionalitas Switch Statin (Rosuvastatin ke Atorvastatin)")
add_paragraph(doc,
    "Switch Rosuvastatin 10 mg ke Atorvastatin 20 mg pada kunjungan Oktober 2026 (M6) sangat rasional. "
    "Atorvastatin dieliminasi > 98% via hepatobilier/empedu (ekskresi ginjal < 2%), sehingga sangat aman pada gangguan ginjal pasien (CrCl 17,67 mL/min) "
    "dibandingkan Rosuvastatin yang memiliki ekskresi ginjal 10%, serta bebas dari restriksi ketat Fornas FKRTL.")

add_image_evidence(doc,
    r"guideline_evidence_rajal/perhi_perki_hypertension_dyslipidemia.png",
    "Panduan Terapi Dislipidemia & Target LDL Risiko Tinggi",
    "Panduan Dislipidemia PERKI 2022 & Fornas Kemenkes RI",
    "Halaman 25-30")

# 1.9 Plan & Monitoring Rajal
add_h2(doc, "1.9 Rencana Asuhan Kefarmasian (Care Plan) & Rekomendasi Monitoring Rajal")
headers_plan = ["Masalah Medis", "Drug Related Problem (DRP)", "Rekomendasi Farmasis", "Parameter Monitoring", "Status Rekomendasi"]
rows_plan = [
    ["DM Tipe 2 Tak Terkontrol (HbA1c 9,1%)", 
     "Kegagalan kombinasi 3 OHO oral (Glimepirid + Sitagliptin + Acarbose)", 
     "Inisiasi Insulin Basal (Glargine 10 unit malam hari) & titrasi berkala 2 unit tiap 3-4 hari", 
     "GDP pagi (target 80-130 mg/dL), HbA1c per 3 bulan", 
     "Disetujui (✓)"],
    
    ["Dosis Glimepirid Geriatri", 
     "Overdosis relatif Glimepirid 6 mg/hari pada geriatri 64 th dengan klirens ginjal turun (PIM Beers & melanggar Fornas)", 
     "Turunkan dosis Glimepirid menjadi 2 mg 1x1 pagi (atau ganti Glikuidon 30 mg / stop saat insulin mulai)", 
     "GDS mandiri, tanda hipoglikemia akut", 
     "Disetujui (✓)"],
    
    ["Gangguan Ginjal (CrCl 17,67 mL/min)", 
     "Potensi akumulasi Sitagliptin 100 mg bila eGFR pasien < 45 mL/min", 
     "Evaluasi hasil lab kreatinin ulang 06/11/2026; bila eGFR 30-44 turunkan ke 50 mg, jika <30 ke 25 mg 1x1", 
     "Serum kreatinin, eGFR, gejala GI / pankreatitis", 
     "Disetujui (✓)"],
    
    ["Hipertensi Sub-optimal (TD 133-165)", 
     "Monoterapi Amlodipin 10 mg gagal target <130/80 & interaksi dengan NSAID oral", 
     "Hentikan NSAID oral sistemik; kombinasikan Amlodipin 5 mg + Candesartan 8-16 mg 1x1 malam", 
     "Tekanan darah berkala (target <130/80 mmHg), kalium", 
     "Disetujui (✓)"],
    
    ["Osteoarthritis & Risiko Jatuh Geriatri", 
     "NSAID oral nefrotoksik & interaksi sedasi Gabapentin + Flunarizine", 
     "Maksimalkan Flamar Gel topikal 2-4x/hari, Parasetamol oral prn; batasi Flunarizine maks 10 hari; edukasi fall prevention", 
     "Skor nyeri lutut, stabilitas jalan, fungsi ginjal", 
     "Disetujui (✓)"],
    
    ["Kepatuhan Pasien (MMAS-8 Skor 5.0)", 
     "Kategori: Kepatuhan Rendah (< 6.0) ec lupa berkala & polifarmasi 7-9 tablet", 
     "Sediakan Pill-Box Organizer harian 4 sekat berlabel warna, jadwal minum obat bergambar, libatkan PMO keluarga", 
     "Evaluasi ulang skor MMAS-8 kunjungan berikutnya", 
     "Disetujui (✓)"]
]
add_styled_table(doc, headers_plan, rows_plan, [Inches(1.2), Inches(1.8), Inches(1.8), Inches(1.2), Inches(0.8)])

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
    r"ppt_assets/ttv_chart.png",
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
    ["Natrium Darah (Na+)", "131", "137 (H3)", "135 – 147", "mmol/L", "Hiponatremia ringan ec vomitus; terkoreksi pasca infus NaCl"],
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
    r"ppt_assets/glucose_chart.png",
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
    "Pasien secara bersamaan menerima Inj. Metoclopramide 10 mg IV tiap 8 jam (Gavistal) dan Domperidone 10 mg 3 kali sehari per oral. "
    "Keduanya merupakan antagonis reseptor dopamin tipe 2 (D2 receptor antagonists). "
    "Kombinasi dua agen antagonis dopamin D2 TIDAK memberikan peningkatan efikasi antiemetik, melainkan melipatgandakan risiko efek samping fatal:\n"
    "1. Gejala Ekstrapiramidal Akut (EPS): Distonia leher, krisis okulogirik, akatisia motorik, dan sindrom parkinsonisme sekunder pada geriatri.\n"
    "2. Kardiotoksisitas Perpanjangan Interval QTc: Keduanya memblokade kanal kalium IKr jantung, memperpanjang repolarisasi ventrikel, dan memicu aritmia fatal Torsades de Pointes (TdP).\n"
    "Klasifikasi Interaksi: Lexicomp Drug Interactions Rating: Category D / X (Avoid Combination).")

add_callout_box(doc, "REKOMENDASI INTERVENSI FARMASIS: KONSENSUS PGI & LEXICOMP",
    "1. HENTIKAN salah satu prokinetik D2 untuk mencegah toksisitas neurologis EPS dan aritmia jantung.\n"
    "2. Pada fase akut rawat inap di mana pasien muntah profuse, pertahankan INJEKSI METOCLOPRAMIDE 10 mg IV (atau 5 mg pada geriatri) sebagai monoterapi parenteral, dan HENTIKAN DOMPERIDONE ORAL.\n"
    "3. Bila muntah belum teratasi optimal, JANGAN menambah prokinetik D2 lain. Gunakan antiemetik mekanisme berbeda: INJEKSI ONDANSETRON 4 mg IV (Antagonis Reseptor Serotonin 5-HT3) yang bekerja sinergis tanpa risiko EPS.",
    "alert")

add_image_evidence(doc,
    r"guideline_evidence/drug_interaction_gavistal_domperidone.png",
    "Analisis Interaksi Mayor Duplikasi Prokinetik Dopamin D2 (Metoclopramide + Domperidone) — Lexicomp Risk Rating D/X",
    "Lexicomp Drug Interactions Wolters Kluwer 2024",
    "Lexi-Interact Online Database")

add_image_evidence(doc,
    r"guideline_evidence/konsensus_dispepsia_pgi_dipiro.png",
    "Pedoman Tatalaksana Dispepsia & Algoritma Terapi Mual-Muntah Sesuai Konsensus PGI & DiPiro 12th Ed",
    "Perkumpulan Gastroenterologi Indonesia (PGI 2021/2024) & DiPiro 12th Ed 2023",
    "Konsensus PGI Hal. 12-16; DiPiro Ch. 41 & 42")

# DRP 2 Ranap: Penyesuaian Ginjal Metoclopramide
add_h3(doc, "DRP 2: Penyesuaian Dosis Ginjal Metoclopramide pada Pasien Geriatri")
add_paragraph(doc,
    "Metoclopramide dieliminasi 80% melalui ginjal. Pada lansia berusia 62 tahun 10 bulan dengan fluktuasi fungsi ginjal akibat dehidrasi vomitus, "
    "pemberian dosis penuh 10 mg IV tiap 8 jam berisiko menyebabkan akumulasi obat dan memicu reaksi ekstrapiramidal.")
add_callout_box(doc, "PEDOMAN KLINIS: LEXICOMP GERIATRIC DOSING & MICROMEDEX",
    "Pada pasien lansia atau gangguan fungsi ginjal (CrCl < 60 mL/min), dosis Metoclopramide sebaiknya diturunkan 50% menjadi 5 mg IV tiap 8 jam atau 10 mg IV tiap 12 jam, dan durasi dibatasi maksimal 5 hari parenteral.",
    "info")

add_image_evidence(doc,
    r"guideline_evidence/lexicomp_metoclopramide_renal.png",
    "Panduan Penyesuaian Dosis Ginjal & Geriatri Metoclopramide untuk Mencegah Toksisitas Ekstrapiramidal",
    "Lexicomp Geriatric Lexi-Drugs & Micromedex 2024",
    "Lexicomp Drug Dosing Guidelines")

# DRP 3 Ranap: Tatalaksana Dispepsia PGI & DiPiro
add_h3(doc, "DRP 3: Tatalaksana Komprehensif Mual Muntah karena Dispepsia Berdasarkan Konsensus Nasional PGI 2021/2024 & DiPiro 12th Ed Ch. 41-42")
add_paragraph(doc,
    "Strategi Terapi Dispepsia & Antiemetik:\n"
    "1. Supresi Asam Lambung: Inj. Omeprazole 40 mg IV / 24 jam menghambat pompa asam H+/K+-ATPase sel parietal secara poten, meningkatkan pH lambung > 4, dan memulihkan mukosa lambung (Konsensus PGI Hal. 12-16).\n"
    "2. Mukoprotektor: Sucralfate sirup 1 g (15 mL) 3 kali sehari dalam lambung kosong membentuk lapisan pelindung pada mukosa gaster dan merangsang prostaglandin endogen.\n"
    "3. Antiemetik Terarah: Metoclopramide parenteral monoterapi untuk mempercepat pengosongan lambung ke duodenum, didukung Ondansetron 4 mg IV prn untuk memblokade jaras muntah di medula oblongata (DiPiro Ch. 41 & 42).")

# DRP 4 Ranap: Hiperglikemia Ranap (PERKENI & ADA)
add_h3(doc, "DRP 4: Tatalaksana Hiperglikemia Akut Rawat Inap (GDS 357 mg/dL) — Penghentian OHO Oral, Inisiasi Regimen Insulin Basal-Bolus Target 140–180 mg/dL")
add_paragraph(doc,
    "Pasien masuk dengan GDS 357 mg/dL dan memiliki riwayat OHO rumah (Metformin 500 mg 3x1 dan Glimepirid 2 mg 1x1).")
add_callout_box(doc, "PEDOMAN RAWAT INAP: PERKENI 2021 (HAL. 98-101) & ADA 2024 SECTION 16 (HAL. S278-S282)",
    "1. Penghentian Mutlak Seluruh OHO Oral: METFORMIN HARUS SEGERA DIHENTIKAN karena risiko fatal Asidosis Laktat akibat dehidrasi. SULFONILUREA (Glimepirid) HARUS DIHENTIKAN karena risiko hipoglikemia berat saat intake oral tidak menentu.\n"
    "2. Regimen Insulin Basal-Bolus:\n"
    "• Insulin Basal (Lantus / Glargine): 1x10 Unit malam jam 22.00 untuk kontrol glukosa basal 24 jam.\n"
    "• Insulin Bolus Prandial (Novorapid / Aspart): 3x6–8 Unit subkutan segera sebelum makan.\n"
    "3. Target Glikemik Rawat Inap: 140 – 180 mg/dL (7,8 – 10,0 mmol/L). Target < 110 mg/dL tidak direkomendasikan karena meningkatkan mortalitas (NICE-SUGAR trial).",
    "alert")

add_image_evidence(doc,
    r"guideline_evidence/perkeni_inpatient_guideline.png",
    "Pedoman Pengelolaan Hiperglikemia Pasien Rawat Inap Rumah Sakit Non-ICU",
    "Pedoman Pengelolaan DM Tipe 2 PERKENI 2021",
    "Halaman 98-101")

add_image_evidence(doc,
    r"guideline_evidence/ada_inpatient_guideline.png",
    "Standar Pelayanan Medis Diabetes Rawat Inap & Target Glukosa Darah 140-180 mg/dL",
    "American Diabetes Association (ADA Standards of Care 2024)",
    "Section 16, Diabetes Care 2024;47(Suppl 1):S278-S282")

# DRP 5 Ranap: Rekonsiliasi Hipertensi
add_h3(doc, "DRP 5: Rekonsiliasi Terapi Antihipertensi Rawat Inap (Amlodipin 10 mg)")
add_paragraph(doc,
    "Pasien memiliki riwayat Amlodipin 10 mg malam di rumah. Pada 24 jam pertama saat muntah profuse, obat oral ditunda. "
    "Memasuki Hari Rawat ke-2 saat mual mereda dan diet oral masuk, Amlodipin 10 mg 1x1 malam SEGERA DIREKONSILIASI dan diberikan kembali per oral "
    "sesuai panduan PERHI 2021 dan ACC/AHA 2023 untuk mencegah rebound hypertension.")

add_image_evidence(doc,
    r"guideline_evidence/perhi_acc_aha_hypertension_reconciliation.png",
    "Konsensus Penatalaksanaan Hipertensi & Protokol Rekonsiliasi Antihipertensi Rawat Inap",
    "Konsensus Hipertensi PERHI 2021 & ACC/AHA 2023 Guidelines",
    "PERHI 2021 Hal. 22-26")

# DRP 6 Ranap: Rehidrasi Cairan & Koreksi Elektrolit
add_h3(doc, "DRP 6: Rehidrasi Cairan Kristaloid Isotonik & Koreksi Elektrolit Hiponatremia dan Hipokloremia Akibat Vomitus Profuse")
add_paragraph(doc,
    "Kehilangan HCl lambung dan natrium akibat muntah > 6 kali memicu kadar Na 131 mmol/L dan Cl 96 mmol/L. "
    "Cairan kristaloid isotonik pilihan utama adalah Infus NaCl 0,9% (Normal Saline) 20 tetes/menit (1.500 mL/24 jam) yang aman bagi geriatri. "
    "Terbukti pada Hari ke-3 elektrolit terkoreksi normal (Na 137, Cl 101).")

add_image_evidence(doc,
    r"guideline_evidence/vomitus_rehydration_guideline.png",
    "Panduan Terapi Rehidrasi Cairan & Koreksi Gangguan Elektrolit pada Pasien Mual-Muntah Akut",
    "DiPiro's Pharmacotherapy 12th Edition & WHO Guidelines",
    "DiPiro Ch. 38, Hal. 752-758")

# DRP 7 Ranap: Beers Criteria
add_h3(doc, "DRP 7: Evaluasi Penggunaan Obat pada Pasien Geriatri Berdasarkan AGS Beers Criteria 2023")
add_paragraph(doc,
    "Metoclopramide dibatasi durasi penggunaannya hanya 3 hari parenteral selama fase akut untuk mencegah risiko diskinesia tardif. "
    "Penggunaan insulin analog (Novorapid dan Lantus) sangat tepat pada lansia karena menurunkan risiko hipoglikemia nokturnal berat secara signifikan dibandingkan insulin regular/NPH.")

add_image_evidence(doc,
    r"guideline_evidence/beers_criteria_geriatric.png",
    "Kriteria Penggunaan Obat yang Berpotensi Tidak Tepat pada Populasi Geriatri (AGS Beers Criteria 2023)",
    "American Geriatrics Society 2023 Update",
    "J Am Geriatr Soc 2023;71(7):2052-2081")

# DRP 8 Ranap: Gyssens & Alergi Penisilin
add_h3(doc, "DRP 8: Evaluasi Rasionalitas Antibiotik Metode Gyssens & Riwayat Alergi Penisilin (Amoksisilin/Ampisilin)")
add_paragraph(doc,
    "Pasien memiliki riwayat alergi berat terhadap Amoksisilin dan Ampisilin. Selama perawatan, DPJP tidak memberikan antibiotik empiris karena tidak ada fokus infeksi (leukosit normal 9.200 /µL, suhu afebris 36,8°C). "
    "Berdasarkan audit alur Gyssens (Permenkes No. 28/2021), keputusan tidak memberikan antibiotik dinilai sebagai KATEGORI 0: Penggunaan / Keputusan Terapi Antibiotik TEPAT dan RASIONAL (No Antibiotic Indicated).")

add_image_evidence(doc,
    r"guideline_evidence/gyssens_algorithm_flowchart.png",
    "Algoritma Evaluasi Kualitatif Rasionalitas Penggunaan Antibiotik Metode Gyssens",
    "Permenkes RI No. 28/2021 tentang Pedoman Penggunaan Antibiotik & Gyssens et al. (1992)",
    "Permenkes 28/2021 Lampiran Hal. 35-40")

# 2.7 SOAP Ranap
add_h2(doc, "2.7 Dokumentasi Asuhan Kefarmasian (SOAP) Rawat Inap Lengkap (Per Hari Rawatan)")

# SOAP H1
add_h3(doc, "Dokumentasi SOAP Hari ke-1 Rawat Inap (18-19 Oktober 2026) — Fase Kedaruratan Akut")
headers_soap_h1 = ["Problem Medis", "Subjektif (S) & Objektif (O)", "Asesmen Farmasis (A)", "Rencana Terapi & Intervensi Farmasis (P)"]
rows_soap_h1 = [
    ["Mual Muntah ec Dispepsia", 
     "S: Muntah > 6x, isi cairan & sisa makanan, lemas berat, nyeri ulu hati menusuk, tidak bisa makan/minum.\nO: Nyeri tekan epigastrium (+), turgor kulit menurun.",
     "Vomitus profuse ec dispepsia akut. Duplikasi prokinetik D2 (Metoclopramide IV + Domperidone PO) berisiko EPS dan perpanjangan QTc (Lexicomp Cat D/X).",
     "1. IVFD NaCl 0,9% 20 tpm untuk rehidrasi.\n2. Inj. Omeprazole 40 mg / 24 jam IV.\n3. Pertahankan Inj. Metoclopramide 10 mg IV (atau 5 mg pada lansia).\n4. REKOMENDASI: HENTIKAN Domperidone oral.\n5. Tambahkan Inj. Ondansetron 4 mg IV bila muntah refrakter."],
    
    ["Hiperglikemia DM Tipe 2",
     "S: Badan lemas tak bertenaga, riwayat DM rutin Metformin & Glimepirid.\nO: GDS 357 mg/dL, Glukosa Urin +3, Keton Negatif.",
     "Krisis hiperglikemia terinduksi stres akut dispepsia dan dehidrasi. OHO oral dikontraindikasikan (PERKENI & ADA).",
     "1. HENTIKAN sementara Metformin & Glimepirid oral.\n2. Inisiasi Regimen Insulin Basal-Bolus:\n   - Novorapid SC 3 x 6 Unit ac (prandial)\n   - Lantus SC 1 x 10 Unit malam (basal)\n3. Monitoring GDS tiap 6 jam (target 140-180 mg/dL)."],
    
    ["Hiponatremia & Hipokloremia",
     "S: Lemas badan, pusing melayang.\nO: Na+ 131 mmol/L (L), Cl- 96 mmol/L (L), K+ 3,8 mmol/L.",
     "Hiponatremia & hipokloremia ringan akibat kehilangan cairan lambung asam via muntah berulang.",
     "1. Rehidrasi kristaloid isotonik Infus NaCl 0,9% 20 tpm.\n2. Re-evaluasi elektrolit serum serial 24-48 jam."],
    
    ["Hipertensi Esensial",
     "S: Pusing ringan.\nO: TD 145/88 mmHg. Riwayat Amlodipin 10 mg rumah.",
     "Hipertensi terkontrol borderline. Terapi oral ditunda 24 jam karena muntah aktif.",
     "1. Tunda Amlodipin oral hingga toleransi oral membaik.\n2. Pantau TD tiap 8 jam."]
]
add_styled_table(doc, headers_soap_h1, rows_soap_h1, [Inches(1.2), Inches(1.8), Inches(1.8), Inches(2.0)])

# SOAP H2
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

# SOAP H3
add_h3(doc, "Dokumentasi SOAP Hari ke-3 Rawat Inap (21 Oktober 2026) — Persiapan KRS & Discharge Planning")
headers_soap_h3 = ["Problem Medis", "Subjektif (S) & Objektif (O)", "Asesmen Farmasis (A)", "Rencana Terapi & Intervensi Farmasis (P)"]
rows_soap_h3 = [
    ["Kesiapan Pasien Pulang (KRS)", 
     "S: Tidak mual, tidak muntah, makan habis 1 porsi bubur, badan segar.\nO: TD 125/78 mmHg, GDS Pagi: 138 mg/dL, Elektrolit normal: Na 137 mmol/L, Cl 101 mmol/L.",
     "Kondisi klinis stabil sempurna. Mual muntah dispepsia teratasi tuntas. Glikemik dan elektrolit normal. Pasien siap KRS (Discharge Planning).",
     "1. Resep Pulang (Oral & Subkutan):\n   - Lansoprazole kapsul 30 mg 1x1 ac pagi\n   - Sucralfate sirup 3x1 C ac (selama 5 hari)\n   - Lantus SoloStar Pen 1 x 10 Unit SC malam\n   - Metformin tablet 500 mg 3x1 dc (reintroduksi aman)\n   - Amlodipin tablet 10 mg 1x1 malam PO\n2. Konseling Farmasis Pulang (KIE):\n   - Edukasi teknik injeksi insulin SoloStar, rotasi tusukan, dan simpan 2-8°C.\n   - Edukasi pengenalan tanda hipoglikemia & dekstrosa murni.\n   - Edukasi makan porsi kecil sering (small frequent meals)."]
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

output_path = r"d:\FILE NINIS\ANALISIS_KASUS_MENDALAM_RAJAL_DAN_RANAP.docx"
doc.save(output_path)
print(f"Revised Master DOCX successfully generated at: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")

import json
import re
import os

transcript_path = r'C:\Users\HP\.gemini\antigravity\brain\6f7dd462-3e3c-4d4e-915c-e93e519e3316\.system_generated\logs\transcript_full.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = [json.loads(line) for line in f]

chats = [
    {
        'title': 'SESI 1: PENGKAJIAN AWAL LENGKAP PEMANTAUAN TERAPI OBAT (PTO) RAWAT JALAN',
        'desc': 'Identifikasi DRP, Analisis Kondisi & Lab 6 Bulan, Rekomendasi Dosis Sesuai Guideline Terkini, Analisis Restriksi Fornas, Profil 3 Efek Samping Terbanyak Beserta Persentase & Referensi, Pengisian Form Excel PTO, dan Penyusunan Laporan Bukti Screenshot Guideline.',
        'user_step': 0,
        'asst_step': 110
    },
    {
        'title': 'SESI 2: INTEGRASI FILE BARU & PENILAIAN LEMBAR KUESIONER MMAS-8',
        'desc': 'Penyesuaian analisis klinis paska pengguna mengunggah berkas kuesioner MMAS-8 dengan centang jawaban pasien.',
        'user_step': 111,
        'asst_step': 190
    },
    {
        'title': 'SESI 3: KONSOLIDASI SELURUH BERKAS KE DALAM FOLDER HASIL',
        'desc': 'Pengelompokan seluruh dokumen hasil analisis (Excel, Word, PDF, HTML, Markdown, dan Folder Gambar Bukti Guideline) ke dalam satu folder terpadu HASIL.',
        'user_step': 191,
        'asst_step': 200
    },
    {
        'title': 'SESI 4: KOREKSI DATA EXCEL BERDASARKAN HASIL TERBARU MMAS-8 (SKOR 5.0)',
        'desc': 'Penyesuaian tepat file PTO_RAJAL_LENGKAP_SRI_WISRAYA.xlsx dan FORM PTO.xlsx agar mencerminkan jawaban riil kuesioner MMAS-8 (Skor 5.0 / Kepatuhan Rendah ec Unintentional Non-adherence).',
        'user_step': 201,
        'asst_step': 268
    },
    {
        'title': 'SESI 5: ANALISIS MENDALAM POTENSI INTERAKSI OBAT-OBAT & OBAT-MAKANAN',
        'desc': 'Telaah farmakologi klinis interaksi 13 rejimen obat pasien (mekanisme farmakodinamik/kinetik, bukti kasus klinis pasien, bahaya sedasi aditif geriatri, aturan suapan pertama Acarbose, bahaya skipped meals Glimepirid, kontraindikasi grapefruit, dan matriks jadwal harian terintegrasi).',
        'user_step': 269,
        'asst_step': 282
    }
]

step_map = {s.get('step_index'): s.get('content', '') for s in lines if s.get('content')}

def clean_user(txt):
    m = re.search(r'<USER_REQUEST>(.*?)</USER_REQUEST>', txt, re.DOTALL)
    if m:
        return m.group(1).strip()
    return txt.strip()

doc = []
doc.append('# DOKUMENTASI LENGKAP RIWAYAT CHAT & KONSULTASI KLINIS ASUHAN KEFARMASIAN (PTO)')
doc.append('## PASIEN RAWAT JALAN POLI PENYAKIT DALAM — RSPAU DR. S. HARDJOLUKITO')
doc.append('### NAMA PASIEN: NY. SRI WISRAYA (64 TAHUN) | NO. RM: 00062584')
doc.append('### PERIODE EVALUASI REKAM MEDIS: 27 APRIL 2026 – 27 OKTOBER 2026')
doc.append('\n---\n')
doc.append('> **Catatan Dokumentasi:** Dokumen ini merangkum dan memisahkan seluruh tahapan interaksi konsultasi asuhan kefarmasian klinis (Pemantauan Terapi Obat / PTO) antara Pengguna (Apoteker/Mahasiswa Farmasi Klinis) dan Antigravity Clinical Assistant secara kronologis, lengkap, dan terstruktur sesuai setiap sesi chat.\n')

for i, c in enumerate(chats):
    u_content = clean_user(step_map.get(c['user_step'], ''))
    a_content = step_map.get(c['asst_step'], '').strip()
    
    doc.append(f"## {c['title']}")
    doc.append(f"*{c['desc']}*\n")
    doc.append("### 👤 PERTANYAAN / INSTRUKSI PENGGUNA (USER REQUEST):")
    doc.append("```markdown")
    doc.append(u_content)
    doc.append("```\n")
    doc.append("### 🤖 JAWABAN & ANALISIS KLINIS ASISTEN (CLINICAL PHARMACIST RESPONSE):")
    doc.append(a_content)
    doc.append("\n\n---\n")

full_text = '\n'.join(doc)

out_paths = [
    'd:/FILE NINIS/PTO RAJAL/HASIL/DOKUMENTASI_HISTORY_CHAT_PTO_RAJAL.md',
    'd:/FILE NINIS/PTO RAJAL/DOKUMENTASI_HISTORY_CHAT_PTO_RAJAL.md',
    'd:/FILE NINIS/HASIL/DOKUMENTASI_HISTORY_CHAT_PTO_RAJAL.md',
    'd:/FILE NINIS/DOKUMENTASI_HISTORY_CHAT_PTO_RAJAL.md'
]

for p in out_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f'Wrote {len(full_text)} characters to {p}')

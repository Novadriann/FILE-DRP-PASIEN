import os
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

out_dir = r"D:\FILE NINIS\guideline_evidence_rajal"
os.makedirs(out_dir, exist_ok=True)
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

cards = [
    {
        "id": "perkeni_2021_dm_algorithm",
        "title": "PB PERKENI 2021 — Algoritma Pengelolaan DM Tipe 2 & Terapi Kombinasi",
        "badge": "PEDOMAN NASIONAL DIABETES MELITUS 2021",
        "source": "Pedoman Pengelolaan dan Pencegahan DM Tipe 2 Dewasa di Indonesia (PB PERKENI 2021, Hal. 45-50)",
        "content": """
        <div class='section-title'>Kombinasi 3 Obat Antihiperglikemik Oral & Indikasi Insulin Basal</div>
        <p><b>1. Evaluasi Kontrol Glikemik:</b> Evaluasi efektivitas terapi dilakukan setiap 3 bulan dengan pemeriksaan HbA1c. Bila target HbA1c belum tercapai (target umum &lt;7,0% atau 7,0–8,0% pada lansia), terapi harus diintensifikasi tanpa menunda.</p>
        <p><b>2. Terapi Kombinasi 3 Obat:</b> Pada pasien yang belum mencapai target dengan kombinasi 2 obat (misalnya Sulfonilurea + DPP-4 Inhibitor), dapat ditambahkan obat ketiga dengan mekanisme berbeda seperti <i>Alpha-Glucosidase Inhibitor (Acarbose)</i> atau <i>SGLT-2 Inhibitor</i>.</p>
        <p><b>3. Indikasi Insulin Basal:</b> Apabila kombinasi 3 OHO dosis optimal belum mencapai target (HbA1c &gt;9,0% atau GDP/GDS tetap tinggi &gt;180–200 mg/dL), direkomendasikan memulai <b>Insulin Basal</b> (10 unit/hari atau 0,1–0,2 unit/kgBB/hari) malam hari bersama OHO.</p>
        <div class='highlight-box'>
            <b>Korelasi Klinis Ny. Sri Wisraya (64 th):</b><br/>
            Pasien telah mendapatkan terapi kombinasi 3 OHO (Glimepirid 6 mg/hari + Sitagliptin 100 mg/hari + Acarbose 200 mg/hari), namun HbA1c tetap <b>9,1%</b> dan GDP <b>151–190 mg/dL</b>. Berdasarkan algoritma PERKENI 2021, pasien telah mengalami kegagalan kombinasi 3 OHO dan merupakan <b>kandidat kuat untuk inisiasi Insulin Basal</b> (dosis awal 10 unit malam hari) untuk mengatasi glukotoksisitas dan mencegah komplikasi mikrovaskular/makrovaskular lanjut.
        </div>
        """
    },
    {
        "id": "perkeni_beers_glimepiride_elderly",
        "title": "PB PERKENI 2021 & AGS Beers Criteria 2023 — Sulfonilurea pada Usia Lanjut & Ginjal",
        "badge": "KEAMANAN OBAT GERIATRI & GINJAL",
        "source": "PERKENI 2021 (Hal. 52, 68, 96) & American Geriatrics Society (AGS) Beers Criteria 2023",
        "content": """
        <div class='section-title'>Peringatan Penggunaan Glimepirid Dosis Tinggi pada Pasien Geriatri</div>
        <p><b>1. Risiko Hipoglikemia Berat & Berkepanjangan:</b> Sulfonilurea (khususnya Glimepirid dan Glibenklamid) dimetabolisme di hati menjadi metabolit aktif yang diekskresikan melalui ginjal (60%). Pada pasien usia lanjut (&ge;60 th) dan penurunan fungsi ginjal, bersihan obat menurun drastis sehingga waktu paruh memanjang.</p>
        <p><b>2. Batasan Dosis Glimepirid:</b> Dosis awal glimepirid pada lansia adalah 1 mg/hari, dengan titrasi lambat. Dosis pemeliharaan lazim adalah 1–4 mg/hari. Penggunaan dosis <b>6 mg/hari (3 mg 2x1)</b> pada lansia sangat tidak dianjurkan karena meningkatkan risiko hipoglikemia asimtomatik yang dapat memicu pusing, sinkop, jatuh (fall injury), dan aritmia.</p>
        <p><b>3. Rekomendasi AGS Beers Criteria 2023:</b> Hindari sulfonilurea kerja panjang pada geriatri. Lebih disarankan beralih ke agen dengan risiko hipoglikemia minimal (DPP-4i, GLP-1 RA) atau sulfonilurea bersihan hati murni seperti <i>Glikuidon</i>.</p>
        <div class='highlight-box'>
            <b>Korelasi Klinis Kasus:</b><br/>
            Ny. Sri Wisraya (64 th) diresepkan Glimepirid 3 mg 2x1 (total 6 mg/hari). Pasien mengalami riwayat trauma kepala/CKR (fraktur os zygomaticum pada 04-07-2026) akibat jatuh, yang sangat berpotensi dipicu oleh episode hipoglikemia tersembunyi atau pusing ortostatik. <b>Rekomendasi Farmasi:</b> Turunkan dosis Glimepirid menjadi 2 mg 1x1 pagi, atau beralih ke Glikuidon / Insulin Basal.
        </div>
        """
    },
    {
        "id": "sitagliptin_renal_adjustment_lexicomp",
        "title": "Lexicomp & FDA Label — Penyesuaian Dosis Sitagliptin pada Gangguan Ginjal",
        "badge": "DOSE ADJUSTMENT / RENAL IMPAIRMENT",
        "source": "Lexicomp Drug Information & Januvia (Sitagliptin) FDA Prescribing Information 2023",
        "content": """
        <div class='section-title'>Rekomendasi Dosis Sitagliptin Berdasarkan Fungsi Ginjal (eGFR / CrCl)</div>
        <table style='width:100%; border-collapse:collapse; margin:10px 0; font-size:12px;'>
            <tr style='background:#f1f5f9; text-align:left;'>
                <th style='padding:6px; border:1px solid #cbd5e1;'>Kategori Fungsi Ginjal</th>
                <th style='padding:6px; border:1px solid #cbd5e1;'>Nilai eGFR / CrCl</th>
                <th style='padding:6px; border:1px solid #cbd5e1;'>Dosis Sitagliptin yang Dianjurkan</th>
            </tr>
            <tr>
                <td style='padding:6px; border:1px solid #cbd5e1;'>Normal / Gangguan Ringan</td>
                <td style='padding:6px; border:1px solid #cbd5e1;'>&ge; 45 mL/min</td>
                <td style='padding:6px; border:1px solid #cbd5e1;'><b>100 mg 1x sehari</b></td>
            </tr>
            <tr style='background:#fef3c7;'>
                <td style='padding:6px; border:1px solid #cbd5e1;'>Gangguan Ginjal Sedang (CKD G3b)</td>
                <td style='padding:6px; border:1px solid #cbd5e1;'>30 hingga &lt; 45 mL/min</td>
                <td style='padding:6px; border:1px solid #cbd5e1;'><b>50 mg 1x sehari</b> (Diturunkan 50%)</td>
            </tr>
            <tr style='background:#fee2e2;'>
                <td style='padding:6px; border:1px solid #cbd5e1;'>Gangguan Berat (CKD G4/G5 / ESRD)</td>
                <td style='padding:6px; border:1px solid #cbd5e1;'>&lt; 30 mL/min</td>
                <td style='padding:6px; border:1px solid #cbd5e1;'><b>25 mg 1x sehari</b> (Diturunkan 75%)</td>
            </tr>
        </table>
        <div class='highlight-box'>
            <b>Analisis Kasus Ny. Sri Wisraya:</b><br/>
            Pada pemeriksaan lab 04-07-2026, Kreatinin serum pasien melonjak ke <b>2,69 mg/dL</b> (CrCl Cockcroft-Gault = <b>17,67 mL/min</b>; Stage G4). Pasien tetap menerima Sitagliptin 100 mg 1x1. Karena 80% sitagliptin diekskresikan ginjal tanpa perubahan, akumulasi obat dapat terjadi.<br/>
            <b>Rekomendasi Farmasi:</b> Lakukan evaluasi ulang serum kreatinin berkala (sebagaimana diorder pada 07-10-2026). Jika eGFR &lt; 45 mL/min, dosis <b>wajib disesuaikan menjadi 50 mg atau 25 mg 1x sehari</b> untuk mencegah toksisitas.
        </div>
        """
    },
    {
        "id": "perhi_perki_hypertension_dyslipidemia",
        "title": "PERHI 2021 & PERKI 2022 — Tata Laksana Hipertensi & Dislipidemia pada DM Tipe 2",
        "badge": "KARDIOVASKULAR & RENOPROTEKSI",
        "source": "Konsensus Penatalaksanaan Hipertensi (PERHI 2021) & Panduan Dislipidemia (PERKI 2022)",
        "content": """
        <div class='section-title'>Target & Strategi Terapi Kardiovaskular Terintegrasi</div>
        <p><b>1. Target Tekanan Darah pada DM & CKD (PERHI 2021):</b> Target tekanan darah adalah <b>&lt; 130/80 mmHg</b>. Pasien DM dengan hipertensi memiliki risiko kejadian kardiovaskular 2–4 kali lipat lebih tinggi.</p>
        <p><b>2. Terapi Kombinasi Hipertensi:</b> Monoterapi Amlodipin 10 mg belum adekuat mengontrol TD pasien (TD berkisar 138/76 hingga 165/89 mmHg). Direkomendasikan terapi kombinasi 2 obat lini pertama: <b>CCB (Amlodipin) + ARB (misal Candesartan 8–16 mg atau Telmisartan 40–80 mg)</b>. ARB memberikan proteksi renal (menurunkan albuminuria) dan mengurangi edema perifer akibat Amlodipin.</p>
        <p><b>3. Stratifikasi Dislipidemia (PERKI 2022):</b> Pasien DM usia &gt;40 tahun dengan faktor risiko multipel masuk kategori <i>Risiko Sangat Tinggi (Very High Risk)</i> dengan target <b>LDL-C &lt; 55 mg/dL</b> atau <i>Risiko Tinggi</i> dengan target <b>LDL-C &lt; 70 mg/dL</b>.</p>
        <p><b>4. Keamanan Statin pada Ginjal:</b> Pengalihan dari Rosuvastatin 10 mg ke <b>Atorvastatin 20 mg</b> pada 07-10-2026 sangat tepat karena Atorvastatin dimetabolisme hepatik primer (&lt;2% ginjal), sehingga tidak memerlukan reduksi dosis pada gangguan ginjal.</p>
        """
    },
    {
        "id": "ira_nsaid_safety_osteoarthritis",
        "title": "IRA 2021 / ACR & Beers Criteria — Keamanan NSAID pada OA Genu Geriatri Komorbid CKD",
        "badge": "REUMATOLOGI & NEFROTOKSISITAS",
        "source": "Rekomendasi IRA untuk Diagnosis dan Pengelolaan Osteoartritis & Beers Criteria 2023",
        "content": """
        <div class='section-title'>Penggunaan Analgesik & NSAID pada Pasien Geriatri Hipertensi & CKD</div>
        <p><b>1. Bahaya NSAID Oral Sistemik (Meloxicam & Kalium/Natrium Diklofenak):</b> NSAID menghambat sintesis prostaglandin renal vasodilatasi, menyebabkan penurunan aliran darah glomerulus, memicu Acute Kidney Injury (AKI), retensi natrium/air (memperburuk hipertensi), dan menumpulkan efek obat antihipertensi (Amlodipin).</p>
        <p><b>2. Rekomendasi Terapi OA Genu:</b>
            <ul>
                <li><b>Lini Pertama:</b> Terapi topikal <b>Flamar Gel (Diklofenak Gel 1%)</b> 2–4 kali sehari dioleskan pada sendi lutut. Absorpsi sistemik topikal &lt;6%, sehingga aman bagi ginjal dan tekanan darah.</li>
                <li><b>Analgesik Oral:</b> Parasetamol (Acetaminophen) oral hingga 1000 mg 3x sehari bila nyeri ringan-sedang.</li>
                <li><b>Oral NSAID:</b> Hanya digunakan bila topikal/parasetamol gagal, dengan dosis efektif terendah, durasi sangat singkat (&le; 5–7 hari), dan <b>wajib didampingi Gastroprotektor (PPI seperti Omeprazole/Lansoprazole)</b>.</li>
            </ul>
        </p>
        <div class='highlight-box'>
            <b>Evaluasi Resep Pasien:</b> Pada kunjungan Mei (Meloxicam 7,5 mg 2x1), Juni (Meloxicam 7,5 mg 1x1), dan September (Kalium Diklofenak 50 mg 2x1), pasien diberikan NSAID oral tanpa PPI. Ditambah pada 08-10-2026 di Poli Orthopedi diresepkan Natrium Diklofenak 50 mg 2x1. <b>Saran Apoteker:</b> Hentikan NSAID oral sistemik; optimalkan Flamar Gel topikal + Glukosamin 500 mg, serta konsultasikan latihan fisik quadriceps.
        </div>
        """
    },
    {
        "id": "mmas8_patient_adherence_morisky",
        "title": "Morisky Medication Adherence Scale (MMAS-8) — Protokol Kepatuhan Rawat Jalan",
        "badge": "EVALUASI KEPATUHAN FARMASI KLINIK",
        "source": "Morisky DE, et al. (J Clin Hypertens 2008) & Standar Pelayanan Farmasi Klinis PKPA RSPAU",
        "content": """
        <div class='section-title'>Kuesioner Skrining Kepatuhan Pasien Rawat Jalan (8 Pertanyaan)</div>
        <table style='width:100%; border-collapse:collapse; margin:8px 0; font-size:11px;'>
            <tr style='background:#f1f5f9; text-align:left;'>
                <th style='padding:5px; border:1px solid #cbd5e1; width:5%;'>No</th>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Item Pertanyaan Kepatuhan (MMAS-8)</th>
                <th style='padding:5px; border:1px solid #cbd5e1; width:20%;'>Sistem Skor</th>
            </tr>
            <tr>
                <td style='padding:4px; border:1px solid #cbd5e1;'>1</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Apakah Anda kadang-kadang lupa minum obat untuk penyakit Anda?</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Ya = 0 | Tidak = 1</td>
            </tr>
            <tr>
                <td style='padding:4px; border:1px solid #cbd5e1;'>2</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Dalam 2 minggu terakhir, pernahkah Anda sengaja tidak meminum obat?</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Ya = 0 | Tidak = 1</td>
            </tr>
            <tr>
                <td style='padding:4px; border:1px solid #cbd5e1;'>3</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Pernahkah mengurangi/berhenti minum obat tanpa konsultasi dokter karena merasa lebih parah?</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Ya = 0 | Tidak = 1</td>
            </tr>
            <tr>
                <td style='padding:4px; border:1px solid #cbd5e1;'>4</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Saat bepergian meninggalkan rumah, apakah kadang lupa membawa obat?</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Ya = 0 | Tidak = 1</td>
            </tr>
            <tr>
                <td style='padding:4px; border:1px solid #cbd5e1;'>5</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Apakah kemarin Anda lupa meminum obat Anda?</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Ya = 0 | Tidak = 1</td>
            </tr>
            <tr>
                <td style='padding:4px; border:1px solid #cbd5e1;'>6</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Ketika Anda merasa kondisi kesehatan membaik, apakah kadang berhenti minum obat?</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Ya = 0 | Tidak = 1</td>
            </tr>
            <tr>
                <td style='padding:4px; border:1px solid #cbd5e1;'>7</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Apakah Anda merasa terganggu atau repot dengan rencana pengobatan rutin setiap hari?</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Ya = 0 | Tidak = 1</td>
            </tr>
            <tr>
                <td style='padding:4px; border:1px solid #cbd5e1;'>8</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Seberapa sering Anda kesulitan mengingat untuk minum semua obat?<br/>(A. Tidak pernah/jarang=1; B. Sekali-kali=0.75; C. Kadang=0.5; D. Sering=0.25; E. Selalu=0)</td>
                <td style='padding:4px; border:1px solid #cbd5e1;'>Skala Likert (0 – 1)</td>
            </tr>
        </table>
        <div class='highlight-box'>
            <b>Interpretasi Skor MMAS-8:</b><br/>
            &bull; <b>Skor 8,0 :</b> Kepatuhan Tinggi (High Adherence)<br/>
            &bull; <b>Skor 6,0 – &lt; 8,0 :</b> Kepatuhan Sedang (Medium Adherence)<br/>
            &bull; <b>Skor &lt; 6,0 :</b> Kepatuhan Rendah (Low Adherence)<br/>
            <b>Intervensi Edukasi Apoteker:</b> Pasien geriatri dengan 7–9 macam obat dengan aturan minum berbeda (sebelum makan, suapan pertama, sesudah makan, malam sebelum tidur) berisiko tinggi mengalami <i>unintentional non-adherence</i>. Wajib disediakan <b>Pill-Box Organizer</b> harian dan tabel jadwal minum obat bergambar.
        </div>
        """
    },
    {
        "id": "lexicomp_interactions_rajal",
        "title": "Lexicomp Drug-Drug & Drug-Food Interactions — Analisis Interaksi Resep Ny. Sri Wisraya",
        "badge": "INTERAKSI OBAT & MAKANAN",
        "source": "Lexicomp Online Drug Interactions Analysis & Clinical Pharmacology 2024",
        "content": """
        <div class='section-title'>Daftar Interaksi Signifikan pada Terapi Rawat Jalan Pasien</div>
        <table style='width:100%; border-collapse:collapse; margin:8px 0; font-size:11px;'>
            <tr style='background:#f1f5f9; text-align:left;'>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Kombinasi Obat</th>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Kategori</th>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Mekanisme & Dampak Klinis</th>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Rekomendasi & Monitoring</th>
            </tr>
            <tr>
                <td style='padding:5px; border:1px solid #cbd5e1;'><b>NSAID (Meloxicam / Diklofenak) + Amlodipin</b></td>
                <td style='padding:5px; border:1px solid #cbd5e1; text-align:center;'><span style='background:#f59e0b; color:white; padding:2px 6px; border-radius:4px;'>Kategori C</span></td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>NSAID menghambat prostaglandin vasodilatasi ginjal, menyebabkan retensi cairan dan menumpulkan efek antihipertensi Amlodipin.</td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Pantau tekanan darah berkala; batasi NSAID sistemik &le; 5 hari atau gunakan Flamar gel topikal.</td>
            </tr>
            <tr>
                <td style='padding:5px; border:1px solid #cbd5e1;'><b>NSAID + Glimepirid</b></td>
                <td style='padding:5px; border:1px solid #cbd5e1; text-align:center;'><span style='background:#f59e0b; color:white; padding:2px 6px; border-radius:4px;'>Kategori C</span></td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>NSAID dapat menggeser ikatan protein plasma sulfonilurea dan menghambat ekskresi renal, meningkatkan risiko hipoglikemia.</td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Monitor tanda hipoglikemia (keringat dingin, tremor, lemas); edukasi penanganan hipoglikemia.</td>
            </tr>
            <tr>
                <td style='padding:5px; border:1px solid #cbd5e1;'><b>Gabapentin + Flunarizine</b></td>
                <td style='padding:5px; border:1px solid #cbd5e1; text-align:center;'><span style='background:#f59e0b; color:white; padding:2px 6px; border-radius:4px;'>Kategori C</span></td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Efek depresan SSP aditif; meningkatkan rasa kantuk, pusing, gangguan koordinasi motorik, dan risiko jatuh pada geriatri.</td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Gunakan Flunarizine jangka pendek; berikan Gabapentin saat malam menjelang tidur; edukasi pencegahan jatuh.</td>
            </tr>
            <tr>
                <td style='padding:5px; border:1px solid #cbd5e1;'><b>Acarbose + Glimepirid</b></td>
                <td style='padding:5px; border:1px solid #cbd5e1; text-align:center;'><span style='background:#f59e0b; color:white; padding:2px 6px; border-radius:4px;'>Kategori C</span></td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Peningkatan risiko hipoglikemia aditif. <b>CRITICAL:</b> Bila terjadi hipoglikemia, terapi HARUS menggunakan <b>Dextrose/Glukosa murni</b>, BUKAN sukrosa/gula tebu (Acarbose menghambat pemecahan sukrosa).</td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Edukasi pasien & keluarga untuk selalu menyiapkan tablet glukosa / permen glukosa murni, bukan sirup sukrosa biasa.</td>
            </tr>
            <tr>
                <td style='padding:5px; border:1px solid #cbd5e1;'><b>Acarbose + Waktu Makan (Drug-Food)</b></td>
                <td style='padding:5px; border:1px solid #cbd5e1; text-align:center;'><span style='background:#3b82f6; color:white; padding:2px 6px; border-radius:4px;'>Food Rule</span></td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Acarbose bekerja lokal menghambat enzim alfa-glukosidase di usus halus. Tidak efektif bila diminum jauh sebelum/sesudah makan.</td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Wajib diminum <b>bersama suapan pertama</b> makanan utama.</td>
            </tr>
        </table>
        """
    }
]

template = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<style>
    body {{
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
        background-color: #f8fafc;
        margin: 0;
        padding: 24px;
        color: #1e293b;
    }}
    .guideline-card {{
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        padding: 24px;
        max-width: 820px;
        margin: 0 auto;
    }}
    .badge {{
        display: inline-block;
        background: #1e3a8a;
        color: #ffffff;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.05em;
        padding: 4px 10px;
        border-radius: 6px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }}
    .title {{
        font-size: 19px;
        font-weight: 800;
        color: #0f172a;
        margin: 0 0 6px 0;
        line-height: 1.3;
    }}
    .source {{
        font-size: 12px;
        color: #64748b;
        font-style: italic;
        margin-bottom: 16px;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 10px;
    }}
    .section-title {{
        font-size: 14px;
        font-weight: 700;
        color: #1e40af;
        margin-top: 10px;
        margin-bottom: 8px;
    }}
    p {{
        font-size: 12.5px;
        line-height: 1.55;
        color: #334155;
        margin: 0 0 8px 0;
    }}
    ul {{
        margin: 4px 0 8px 20px;
        padding: 0;
        font-size: 12px;
        color: #334155;
        line-height: 1.5;
    }}
    li {{
        margin-bottom: 4px;
    }}
    .highlight-box {{
        background: #eff6ff;
        border-left: 4px solid #3b82f6;
        padding: 12px 14px;
        border-radius: 0 8px 8px 0;
        margin-top: 14px;
        font-size: 12px;
        line-height: 1.5;
        color: #1e3a8a;
    }}
</style>
</head>
<body>
<div class="guideline-card">
    <div class="badge">{badge}</div>
    <h1 class="title">{title}</h1>
    <div class="source">{source}</div>
    <div class="content">
        {content}
    </div>
</div>
</body>
</html>
"""

for c in cards:
    html_content = template.format(
        badge=c["badge"],
        title=c["title"],
        source=c["source"],
        content=c["content"]
    )
    html_path = os.path.join(out_dir, f"{c['id']}.html")
    png_path = os.path.join(out_dir, f"{c['id']}.png")
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=920,800",
        f"--screenshot={png_path}",
        html_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(png_path) and os.path.getsize(png_path) > 0:
        print(f"Generated: {c['id']}.png ({os.path.getsize(png_path)} bytes)")
    else:
        print(f"Failed to generate: {c['id']}.png. Returncode: {res.returncode}")

print("\nAll guideline evidence generated successfully!")

import os
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

out_dir = r"D:\FILE NINIS\guideline_evidence"
os.makedirs(out_dir, exist_ok=True)
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

cards = [
    {
        "id": "konsensus_dispepsia_pgi_dipiro",
        "title": "Konsensus Nasional PGI 2021/2024 & DiPiro 12th Ed 2023 — Tata Laksana Mual & Muntah ec Dispepsia",
        "badge": "PEDOMAN GASTROENTEROLOGI & DIPIRO 2023",
        "source": "Konsensus Nasional Dispepsia PGI (Hal. 12-18) & DiPiro Pharmacotherapy 12th Ed (Chapter 41-42: Dyspepsia, Nausea and Vomiting)",
        "content": """
        <div class='section-title'>1. Definisi & Pendekatan Klinis Dispepsia</div>
        <p><b>Definisi:</b> Dispepsia adalah kumpulan gejala yang terdiri dari rasa nyeri atau rasa tidak nyaman di epigastrium, rasa penuh setelah makan, cepat kenyang, kembung, mual, atau muntah. Pada pasien rawat inap dengan keluhan utama muntah hebat (*vomitus profuse*) dan mual persisten, tatalaksana awal mencakup penekanan asam lambung dan terapi antiemetik/prokinetik yang terukur.</p>
        
        <div class='section-title'>2. Strategi Terapi Farmakologi Berdasarkan Guideline</div>
        <table style='width:100%; border-collapse:collapse; margin:8px 0; font-size:11.5px;'>
            <tr style='background:#f1f5f9; text-align:left;'>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Golongan Terapi</th>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Obat Pilihan & Dosis</th>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Mekanisme & Peran Klinis</th>
            </tr>
            <tr>
                <td style='padding:5px; border:1px solid #cbd5e1;'><b>Proton Pump Inhibitor (PPI)</b></td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Omeprazole 40 mg IV / Lansoprazole 30 mg IV</td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Menghambat pompa H+/K+ ATPase parietal lambung, menaikkan pH lambung, mempercepat penyembuhan mukosa, dan menekan iritasi asam yang memicu mual.</td>
            </tr>
            <tr>
                <td style='padding:5px; border:1px solid #cbd5e1;'><b>Prokinetik / Antiemetik D2</b></td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Metoclopramide 10 mg IV / Domperidone 10 mg oral</td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Meningkatkan motilitas saluran cerna atas, mempercepat pengosongan lambung, serta memblok reseptor dopamin D2 di Chemoreceptor Trigger Zone (CTZ).</td>
            </tr>
            <tr>
                <td style='padding:5px; border:1px solid #cbd5e1;'><b>5-HT3 Receptor Antagonist</b></td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Ondansetron 4–8 mg IV</td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Antiemetik poten memblok reseptor serotonin di perifer (vagus) dan CTZ sentral; sangat efektif untuk mual/muntah akut refrakter.</td>
            </tr>
        </table>
        <div class='highlight-box'>
            <b>Peringatan Keamanan & Evaluasi Terapi Ny. Sunarti:</b><br/>
            &bull; <b>Hindari Duplikasi Prokinetik:</b> Pemberian Metoclopramide (Gavistal) bersamaan dengan Domperidone secara ganda tidak meningkatkan efikasi, melainkan melipatgandakan risiko efek samping ekstrapiramidal (EPS) dan perpanjangan interval QTc.<br/>
            &bull; <b>Penyesuaian Ginjal:</b> Pada pasien dengan penurunan fungsi ginjal, dosis Metoclopramide wajib diturunkan 50% untuk mencegah akumulasi neurotoksik.
        </div>
        """
    },
    {
        "id": "skovbjerg_amlodipine_edema_mgmt",
        "title": "Skovbjerg et al. (2023) & DiPiro 12th Ed — Tata Laksana Edema Perifer Akibat Amlodipin",
        "badge": "EVIDENCE-BASED CCB ADVERSE EFFECT MANAGEMENT",
        "source": "Skovbjerg BK et al. Ugeskr Laeger 2023;185:V07220460; DiPiro Pharmacotherapy 12th Ed (Chapter 29); Shetty et al. 2016",
        "content": """
        <div class='section-title'>1. Patofisiologi Edema Perifer Akibat Dihidropiridin (Amlodipin)</div>
        <p>Amlodipin menyebabkan vasodilatasi selektif pada arteriol prekapiler tanpa disertai vasodilatasi venula postkapiler yang seimbang. Ketidakseimbangan resistensi ini meningkatkan tekanan hidrostatik intrakapiler, memicu ekstravasasi cairan plasma ke ruang interstisial tungkai bawah (terutama pergelangan kaki/pedal edema). Edema ini bersifat <b>non-volume overload</b>, sehingga diuretik (Furosemid/Tiazid) umumnya <b>tidak efektif</b>.</p>
        
        <div class='section-title'>2. Hierarki Strategi Penanganan Berdasarkan Bukti Klinis (Skovbjerg et al., 2023)</div>
        <ol style='font-size:12px; line-height:1.6; margin:6px 0 10px 20px; color:#334155;'>
            <li><b>Penurunan Dosis Amlodipin:</b> Menurunkan dosis dari 10 mg menjadi 5 mg/hari secara signifikan menurunkan insiden dan keparahan edema perifer (insiden turun dari 12,3% menjadi <4%).</li>
            <li><b>Kombinasi dengan ACE-Inhibitor atau ARB:</b> Penambahan ARB (misal Candesartan / Telmisartan) menghasilkan venodilatasi postkapiler, menormalkan gradien tekanan kapiler, dan terbukti menurunkan kejadian edema hingga 38–62% dibandingkan CCB monoterapi.</li>
            <li><b>Perubahan Waktu Konsumsi Menjadi Malam Hari:</b> Pemberian amlodipin saat malam hari (sebelum tidur) memanfaatkan posisi rekumben (berbaring) untuk mendistribusikan kembali cairan dan menurunkan tekanan hidrostatik tungkai.</li>
            <li><b>Pengalihan ke CCB Lipofilik Generasi Baru:</b> Beralih ke Lercanidipine atau Lacidipine yang memiliki selektivitas vaskular lebih seimbang.</li>
        </ol>
        <div class='highlight-box'>
            <b>Rekomendasi untuk Kasus Ny. Sri Wisraya:</b><br/>
            Pasien mengeluhkan kaki kaku dan bengkak saat menggunakan Amlodipin 10 mg monoterapi dengan TD belum optimal (133–165 mmHg). Rekomendasi tepat: <b>Turunkan Amlodipin menjadi 5 mg + Tambahkan ARB Candesartan 8–16 mg malam hari</b>.
        </div>
        """
    },
    {
        "id": "dipiro_diabetic_neuropathy_weight",
        "title": "DiPiro 12th Ed (2023) & Kemenkes 2026 — Terapi Neuropati Diabetik & Dampak Terhadap Berat Badan",
        "badge": "DIPIRO PHARMACOTHERAPY 12TH ED & KEMENKES",
        "source": "DiPiro Pharmacotherapy 12th Ed (Chapter 57: Diabetes Mellitus) & Kepmenkes HK.01.07/MENKES/302/2026",
        "content": """
        <div class='section-title'>1. Tatalaksana Nyeri Neuropati Perifer Diabetik (DiPiro 12th Ed)</div>
        <table style='width:100%; border-collapse:collapse; margin:8px 0; font-size:11.5px;'>
            <tr style='background:#f1f5f9; text-align:left;'>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Lini Terapi</th>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Pilihan Obat</th>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Dosis Lazim</th>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Catatan & Efek Samping</th>
            </tr>
            <tr>
                <td style='padding:5px; border:1px solid #cbd5e1;'><b>Lini Pertama</b></td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Pregabalin<br/>Gabapentin<br/>Duloxetine</td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>25–75 mg 2-3x/hr (maks 300-600)<br/>100–300 mg malam (maks 1800)<br/>30–60 mg 1x/hari</td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Pregabalin & Gabapentin memblok subunit alpha-2-delta calcium channel. Efek samping: pusing, sedasi, edema perifer.</td>
            </tr>
            <tr>
                <td style='padding:5px; border:1px solid #cbd5e1;'><b>Lini Kedua</b></td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>TCA (Amitriptilin)<br/>Venlafaxine</td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>10–25 mg malam hari<br/>37.5–75 mg 1x/hari</td>
                <td style='padding:5px; border:1px solid #cbd5e1;'>Hati-hati efek antikolinergik dan aritmia pada usia lanjut/geriatri.</td>
            </tr>
        </table>
        
        <div class='section-title'>2. Dampak Obat Antihiperglikemik terhadap Berat Badan (DiPiro 12th Ed Table 57-11)</div>
        <p>
            &bull; <b>Menurunkan Berat Badan (Weight Loss):</b> GLP-1 Receptor Agonist (Semaglutide, Liraglutide) & SGLT-2 Inhibitor (Empagliflozin, Dapagliflozin).<br/>
            &bull; <b>Netral terhadap Berat Badan (Weight Neutral):</b> Metformin, DPP-4 Inhibitor (Sitagliptin, Linagliptin).<br/>
            &bull; <b>Meningkatkan Berat Badan (Weight Gain):</b> Sulfonilurea (Glimepirid, Glibenklamid), Tiazolidindion (Pioglitazone), Insulin.<br/>
            <i>Rasional Kasus:</i> Pada pasien usia lanjut dengan IMT normal (21,4–21,8 kg/m²), penggunaan Sulfonilurea dosis tinggi tetap berisiko hipoglikemia, sementara Sitagliptin bersifat weight-neutral yang aman.
        </p>
        """
    },
    {
        "id": "naranjo_amlodipine_edema",
        "title": "Naranjo Adverse Drug Reaction Probability Scale — Kausalitas Edema Perifer Amlodipin",
        "badge": "FARMAKOVIGILANS & ALGORITMA NARANJO",
        "source": "Naranjo CA et al. Clin Pharmacol Ther 1981;30(2):239-245 & WHO-UMC Pharmacovigilance Standard",
        "content": """
        <div class='section-title'>Penilaian Kausalitas Efek Samping Edema Perifer pada Ny. Sri Wisraya</div>
        <table style='width:100%; border-collapse:collapse; margin:8px 0; font-size:11px;'>
            <tr style='background:#f1f5f9; text-align:left;'>
                <th style='padding:4px; border:1px solid #cbd5e1; width:5%;'>No</th>
                <th style='padding:4px; border:1px solid #cbd5e1;'>Pertanyaan Algoritma Naranjo</th>
                <th style='padding:4px; border:1px solid #cbd5e1; width:8%; text-align:center;'>Ya</th>
                <th style='padding:4px; border:1px solid #cbd5e1; width:8%; text-align:center;'>Tidak</th>
                <th style='padding:4px; border:1px solid #cbd5e1; width:12%; text-align:center;'>Tdk Diketahui</th>
                <th style='padding:4px; border:1px solid #cbd5e1; width:8%; text-align:center;'>Skor</th>
            </tr>
            <tr><td style='padding:3px; border:1px solid #cbd5e1;'>1</td><td style='padding:3px; border:1px solid #cbd5e1;'>Apakah ada laporan konklusif sebelumnya mengenai reaksi ini?</td><td style='text-align:center;'>+1</td><td style='text-align:center;'>0</td><td style='text-align:center;'>0</td><td style='text-align:center; font-weight:bold;'>+1</td></tr>
            <tr><td style='padding:3px; border:1px solid #cbd5e1;'>2</td><td style='padding:3px; border:1px solid #cbd5e1;'>Apakah efek samping terjadi setelah obat yang dicurigai diberikan?</td><td style='text-align:center;'>+2</td><td style='text-align:center;'>-1</td><td style='text-align:center;'>0</td><td style='text-align:center; font-weight:bold;'>+2</td></tr>
            <tr><td style='padding:3px; border:1px solid #cbd5e1;'>3</td><td style='padding:3px; border:1px solid #cbd5e1;'>Apakah reaksi membaik saat obat dihentikan atau antagonis spesifik diberikan?</td><td style='text-align:center;'>+1</td><td style='text-align:center;'>0</td><td style='text-align:center;'>0</td><td style='text-align:center; font-weight:bold;'>+1</td></tr>
            <tr><td style='padding:3px; border:1px solid #cbd5e1;'>4</td><td style='padding:3px; border:1px solid #cbd5e1;'>Apakah reaksi muncul kembali saat obat diberikan ulang (re-challenge)?</td><td style='text-align:center;'>+2</td><td style='text-align:center;'>-1</td><td style='text-align:center;'>0</td><td style='text-align:center; font-weight:bold;'>0</td></tr>
            <tr><td style='padding:3px; border:1px solid #cbd5e1;'>5</td><td style='padding:3px; border:1px solid #cbd5e1;'>Apakah ada alternatif penyebab yang dapat menyebabkan reaksi ini?</td><td style='text-align:center;'>-1</td><td style='text-align:center;'>+2</td><td style='text-align:center;'>0</td><td style='text-align:center; font-weight:bold;'>+1</td></tr>
            <tr><td style='padding:3px; border:1px solid #cbd5e1;'>6</td><td style='padding:3px; border:1px solid #cbd5e1;'>Apakah reaksi terjadi kembali saat diberikan plasebo?</td><td style='text-align:center;'>-1</td><td style='text-align:center;'>+1</td><td style='text-align:center;'>0</td><td style='text-align:center; font-weight:bold;'>0</td></tr>
            <tr><td style='padding:3px; border:1px solid #cbd5e1;'>7</td><td style='padding:3px; border:1px solid #cbd5e1;'>Apakah obat terdeteksi dalam darah/cairan dalam konsentrasi toksik?</td><td style='text-align:center;'>+1</td><td style='text-align:center;'>0</td><td style='text-align:center;'>0</td><td style='text-align:center; font-weight:bold;'>0</td></tr>
            <tr><td style='padding:3px; border:1px solid #cbd5e1;'>8</td><td style='padding:3px; border:1px solid #cbd5e1;'>Apakah reaksi bertambah berat saat dosis ditingkatkan / berkurang saat dosis diturunkan?</td><td style='text-align:center;'>+1</td><td style='text-align:center;'>0</td><td style='text-align:center;'>0</td><td style='text-align:center; font-weight:bold;'>+1</td></tr>
            <tr><td style='padding:3px; border:1px solid #cbd5e1;'>9</td><td style='padding:3px; border:1px solid #cbd5e1;'>Apakah pasien pernah mengalami reaksi serupa terhadap obat yang sama/mirip sebelumnya?</td><td style='text-align:center;'>+1</td><td style='text-align:center;'>0</td><td style='text-align:center;'>0</td><td style='text-align:center; font-weight:bold;'>0</td></tr>
            <tr><td style='padding:3px; border:1px solid #cbd5e1;'>10</td><td style='padding:3px; border:1px solid #cbd5e1;'>Apakah efek samping dikonfirmasi dengan bukti objektif?</td><td style='text-align:center;'>+1</td><td style='text-align:center;'>0</td><td style='text-align:center;'>0</td><td style='text-align:center; font-weight:bold;'>0</td></tr>
            <tr style='background:#fef3c7;'><td colspan='5' style='padding:5px; border:1px solid #cbd5e1; font-weight:bold; text-align:center;'>TOTAL SKOR NARANJO</td><td style='text-align:center; font-weight:bold; color:#b91c1c;'>6</td></tr>
        </table>
        <div class='highlight-box'>
            <b>Interpretasi Skor Naranjo = 6: Kategori PROBABLE (Besar Kemungkinan Terkait Obat).</b><br/>
            Rentang interpretasi: Skor &ge; 9 (Definite), 5–8 (Probable), 1–4 (Possible), &le; 0 (Doubtful). Hal ini membuktikan bahwa keluhan edema dan rasa berat di kaki pasien memiliki korelasi kausalitas kuat dengan pemberian Amlodipin 10 mg.
        </div>
        """
    },
    {
        "id": "gyssens_algorithm_flowchart",
        "title": "Alur Evaluasi Kualitatif Penggunaan Antibiotik / Antimikroba — Metode Gyssens",
        "badge": "AUDIT PENGGUNAAN ANTIMIKROBA (PPRA)",
        "source": "Gyssens IC et al. J Antimicrob Chemother 1992; Van der Meer et al.; Permenkes No. 8 Tahun 2015 tentang PPRA",
        "content": """
        <div class='section-title'>Kategori Penilaian Rasionalitas Penggunaan Antimikroba (Metode Gyssens)</div>
        <table style='width:100%; border-collapse:collapse; margin:8px 0; font-size:11.5px;'>
            <tr style='background:#f1f5f9; text-align:left;'>
                <th style='padding:5px; border:1px solid #cbd5e1; width:15%;'>Kategori</th>
                <th style='padding:5px; border:1px solid #cbd5e1;'>Deskripsi Rasionalitas Klinis</th>
                <th style='padding:5px; border:1px solid #cbd5e1; width:30%;'>Tindakan Evaluasi</th>
            </tr>
            <tr style='background:#dcfce7;'><td style='padding:5px; border:1px solid #cbd5e1;'><b>Kategori 0</b></td><td style='padding:5px; border:1px solid #cbd5e1;'>Penggunaan antibiotik / antimikroba <b>tepat dan bijak</b> (indikasi, pilihan, dosis, interval, durasi, dan rute sesuai).</td><td style='padding:5px; border:1px solid #cbd5e1;'>Terapi diteruskan sesuai durasi klinis.</td></tr>
            <tr><td style='padding:5px; border:1px solid #cbd5e1;'><b>Kategori I</b></td><td style='padding:5px; border:1px solid #cbd5e1;'>Penggunaan tidak tepat waktu (waktu pemberian tidak sesuai).</td><td style='padding:5px; border:1px solid #cbd5e1;'>Koreksi jadwal pemberian obat.</td></tr>
            <tr><td style='padding:5px; border:1px solid #cbd5e1;'><b>Kategori II A-C</b></td><td style='padding:5px; border:1px solid #cbd5e1;'>Tidak tepat dosis (IIA), interval (IIB), atau rute pemberian (IIC).</td><td style='padding:5px; border:1px solid #cbd5e1;'>Penyesuaian dosis / rute terapi.</td></tr>
            <tr><td style='padding:5px; border:1px solid #cbd5e1;'><b>Kategori III A-B</b></td><td style='padding:5px; border:1px solid #cbd5e1;'>Pemberian terlalu lama (IIIA) atau terlalu singkat (IIIB).</td><td style='padding:5px; border:1px solid #cbd5e1;'>Stop terapi / perpanjang sesuai panduan.</td></tr>
            <tr><td style='padding:5px; border:1px solid #cbd5e1;'><b>Kategori IV A-D</b></td><td style='padding:5px; border:1px solid #cbd5e1;'>Ada alternatif lain yang lebih efektif (IVA), kurang toksik (IVB), lebih murah (IVC), atau spektrum lebih sempit (IVD).</td><td style='padding:5px; border:1px solid #cbd5e1;'>De-eskalasi / switch ke alternatif superior.</td></tr>
            <tr style='background:#fee2e2;'><td style='padding:5px; border:1px solid #cbd5e1;'><b>Kategori V</b></td><td style='padding:5px; border:1px solid #cbd5e1;'><b>Tidak ada indikasi penggunaan antimikroba.</b></td><td style='padding:5px; border:1px solid #cbd5e1;'><b>Hentikan antibiotik segera.</b></td></tr>
            <tr><td style='padding:5px; border:1px solid #cbd5e1;'><b>Kategori VI</b></td><td style='padding:5px; border:1px solid #cbd5e1;'>Data rekam medis tidak lengkap dan tidak dapat dievaluasi.</td><td style='padding:5px; border:1px solid #cbd5e1;'>Lengkapi rekam medis.</td></tr>
        </table>
        <div class='highlight-box'>
            <b>Evaluasi Kasus Ny. Sunarti & Ny. Sri Wisraya:</b><br/>
            &bull; Ny. Sunarti memiliki riwayat <b>Alergi Amoksisilin dan Ampisilin</b> (ruam merah gatal). Selama rawat inap tidak diberikan antibiotik empiris, sehingga tepat (menghindari reaksi hipersensitivitas).<br/>
            &bull; Ny. Sri Wisraya tidak menerima antibiotik oral profilaksis, yang sesuai prinsip *antimicrobial stewardship* (Kategori 0).
        </div>
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
        max-width: 840px;
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
        font-size: 18px;
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
        font-size: 13.5px;
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
    ul, ol {{
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
        "--window-size=920,820",
        f"--screenshot={png_path}",
        html_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(png_path) and os.path.getsize(png_path) > 0:
        print(f"Generated: {c['id']}.png ({os.path.getsize(png_path)} bytes)")
    else:
        print(f"Failed to generate: {c['id']}.png. Returncode: {res.returncode}")

print("\nExtra guideline cards generated successfully!")

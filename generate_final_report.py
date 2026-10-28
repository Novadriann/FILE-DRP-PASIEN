import os
import base64
import subprocess

def get_base64_img(rel_path):
    with open(rel_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

img_ada = get_base64_img(r"d:\FILE NINIS\guideline_evidence\ada_inpatient_guideline.png")
img_lexi = get_base64_img(r"d:\FILE NINIS\guideline_evidence\lexicomp_metoclopramide_renal.png")
img_dupl = get_base64_img(r"d:\FILE NINIS\guideline_evidence\drug_interaction_gavistal_domperidone.png")
img_kdigo = get_base64_img(r"d:\FILE NINIS\guideline_evidence\kdigo_perkeni_diabetes_ckd.png")
img_perhi = get_base64_img(r"d:\FILE NINIS\guideline_evidence\perhi_acc_aha_hypertension_reconciliation.png")

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>Laporan Pemantauan Terapi Obat (PTO) - Ny. Sunarti</title>
<style>
  @page {{
    size: A4;
    margin: 15mm 15mm 15mm 15mm;
  }}
  body {{
    font-family: 'Segoe UI', Arial, sans-serif;
    color: #1e293b;
    background-color: #f8fafc;
    line-height: 1.5;
    margin: 0;
    padding: 20px;
    font-size: 13px;
  }}
  .container {{
    max-width: 1000px;
    margin: 0 auto;
    background: #ffffff;
    padding: 35px 40px;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  }}
  .header-table {{
    width: 100%;
    border-bottom: 3px double #0284c7;
    padding-bottom: 15px;
    margin-bottom: 20px;
  }}
  .hospital-title {{
    font-size: 18px;
    font-weight: bold;
    color: #0369a1;
    text-transform: uppercase;
    margin: 0;
  }}
  .doc-title {{
    font-size: 16px;
    font-weight: 700;
    color: #0f172a;
    margin: 4px 0 0 0;
  }}
  .sub-title {{
    font-size: 12px;
    color: #64748b;
    margin: 2px 0 0 0;
  }}
  h2 {{
    color: #0f172a;
    font-size: 15px;
    border-left: 5px solid #0284c7;
    padding-left: 10px;
    margin-top: 25px;
    margin-bottom: 12px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  h3 {{
    color: #0369a1;
    font-size: 13.5px;
    margin-top: 16px;
    margin-bottom: 8px;
  }}
  .patient-info-table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 15px;
    background: #f1f5f9;
    border-radius: 6px;
    overflow: hidden;
  }}
  .patient-info-table td {{
    padding: 6px 12px;
    font-size: 12.5px;
    border-bottom: 1px solid #e2e8f0;
  }}
  .patient-info-table td.label {{
    font-weight: 600;
    color: #475569;
    width: 18%;
  }}
  .patient-info-table td.val {{
    color: #0f172a;
    width: 32%;
  }}
  .badge-allergy {{
    background: #fee2e2;
    color: #dc2626;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: bold;
  }}
  table.data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0 18px 0;
    font-size: 12px;
  }}
  table.data-table th {{
    background: #0284c7;
    color: #ffffff;
    font-weight: 600;
    padding: 8px 10px;
    text-align: left;
    border: 1px solid #0284c7;
  }}
  table.data-table td {{
    padding: 7px 10px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
  }}
  table.data-table tr:nth-child(even) {{
    background: #f8fafc;
  }}
  .alert-high {{
    color: #b91c1c;
    font-weight: bold;
  }}
  .alert-low {{
    color: #2563eb;
    font-weight: bold;
  }}
  .drp-box {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-left: 5px solid #e11d48;
    border-radius: 6px;
    padding: 12px 16px;
    margin-bottom: 14px;
    page-break-inside: avoid;
  }}
  .drp-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 6px;
  }}
  .drp-title {{
    font-weight: bold;
    color: #9f1239;
    font-size: 13.5px;
  }}
  .drp-badge {{
    background: #ffe4e6;
    color: #be123c;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 4px;
  }}
  .drp-body {{
    font-size: 12.5px;
    line-height: 1.5;
    color: #334155;
  }}
  .rec-box {{
    background: #f0fdf4;
    border-left: 4px solid #16a34a;
    padding: 8px 12px;
    margin-top: 8px;
    border-radius: 0 4px 4px 0;
    font-size: 12.5px;
    color: #14532d;
  }}
  .evidence-container {{
    margin: 20px 0;
    padding: 12px;
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    text-align: center;
    page-break-inside: avoid;
  }}
  .evidence-container img {{
    max-width: 98%;
    height: auto;
    border: 1px solid #94a3b8;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }}
  .evidence-caption {{
    margin-top: 8px;
    font-size: 12px;
    font-weight: 600;
    color: #334155;
  }}
  .comparison-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 12px;
  }}
  .comparison-table th {{
    padding: 9px 10px;
    border: 1px solid #cbd5e1;
    text-align: left;
  }}
  .comparison-table td {{
    padding: 8px 10px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
  }}
  .col-doctor {{
    background: #fff1f2;
    border-top: 3px solid #e11d48;
  }}
  .col-pharma {{
    background: #f0fdf4;
    border-top: 3px solid #16a34a;
  }}
  .footer-sig {{
    margin-top: 40px;
    width: 100%;
    page-break-inside: avoid;
  }}
</style>
</head>
<body>

<div class="container">
  <!-- HEADER -->
  <table class="header-table">
    <tr>
      <td style="width: 70%;">
        <div class="hospital-title">RSPAU dr. S. Hardjolukito Yogyakarta</div>
        <div class="doc-title">LAPORAN PEMANTAUAN TERAPI OBAT (PTO) RAWAT INAP</div>
        <div class="sub-title">Instalasi Farmasi Klinis &bull; Bangsal Rawat Inap Merak (Kamar 314 / Bed 14A)</div>
      </td>
      <td style="width: 30%; text-align: right; font-size: 11.5px; color: #64748b;">
        <strong>Dokumen PTO Farmasi</strong><br>
        Periode Ranap: 14 s/d 18 Okt 2026<br>
        Tanggal Evaluasi: 18&ndash;19 Okt 2026
      </td>
    </tr>
  </table>

  <!-- IDENTITAS PASIEN -->
  <h2>I. Profil &amp; Data Demografi Pasien</h2>
  <table class="patient-info-table">
    <tr>
      <td class="label">Nama Pasien</td>
      <td class="val"><strong>Ny. SUNARTI</strong></td>
      <td class="label">No. Rekam Medis</td>
      <td class="val"><strong>00109480</strong></td>
    </tr>
    <tr>
      <td class="label">Tanggal Lahir / Usia</td>
      <td class="val">18 November 1963 (62 th 10 bln) &bull; Geriatri</td>
      <td class="label">Jenis Kelamin</td>
      <td class="val">Perempuan</td>
    </tr>
    <tr>
      <td class="label">Tinggi / Berat Badan</td>
      <td class="val">156 cm / 60 kg (IMT: 24.65 kg/m&sup2;)</td>
      <td class="label">Dokter Penanggung Jawab</td>
      <td class="val">dr. Raden Triyono Edhi Sulistiyono, Sp.PD., FINASIM</td>
    </tr>
    <tr>
      <td class="label">Tanggal Masuk / Keluar</td>
      <td class="val">14-10-2026 (20:45) &bull; 18-10-2026 (14:00)</td>
      <td class="label">Riwayat Alergi Obat</td>
      <td class="val"><span class="badge-allergy">AMOKSISILIN &amp; AMPISILIN (Gatal kemerahan)</span></td>
    </tr>
    <tr>
      <td class="label">Diagnosis Utama</td>
      <td class="val"><strong>Vomitus Profuse ec dalam pelacakan (suspek food intoxication / GEA)</strong></td>
      <td class="label">Diagnosis Sekunder</td>
      <td class="val">DM Tipe 2 dengan Hiperglikemia, Riw. Hipertensi, Hiponatremia &amp; Hipokloremia ringan, Anorexia Geriatri, ISPA</td>
    </tr>
    <tr>
      <td class="label">Riwayat Penyakit Dahulu</td>
      <td class="val">DM Tipe 2, Hipertensi, Vertigo, Post-Op Phaco+IOL OS katarak komplikata (04/08/2026)</td>
      <td class="label">Riwayat Obat Rumah (RPO)</td>
      <td class="val">Amlodipin 10 mg 1x1, Clopidogrel 75 mg 1x1, Glimepirid 3 mg 1x1, Metformin 500 mg 1x1, Becom C 1x1, Betahistin 3x6 mg, Ibuprofen 2x400 mg (UGD 11/10)</td>
    </tr>
  </table>

  <!-- ANALISIS KONDISI PASIEN & TTV -->
  <h2>II. Analisis Kondisi Klinis &amp; Tanda-Tanda Vital (TTV)</h2>
  <p>
    <strong>Kronologi Masuk:</strong> 4 hari SMRS pasien meminum susu jahe pinggir jalan, keesokan harinya timbul keluhan pusing muter, mual, muntah &gt;10 kali/hari setiap makan/minum, lemas hebat, berkeringat dingin, dan batuk berdahak putih. Tanggal 14/10/2026 ke Klinik Pratama Ramadhan dengan tensi 90/60 mmHg dan GDS 294 mg/dL sehingga dirujuk darurat ke IGD RSPAU.
  </p>
  <table class="data-table">
    <thead>
      <tr>
        <th>Parameter Vital</th>
        <th>Target Normal</th>
        <th>IGD (14/10)</th>
        <th>H1 (15/10)</th>
        <th>H2 (16/10)</th>
        <th>H3 (17/10)</th>
        <th>H4 / Pulang (18/10)</th>
        <th>Evaluasi &amp; Catatan Klinis</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Tekanan Darah (mmHg)</strong></td>
        <td>&lt; 130/80 (DM/CKD)</td>
        <td><span class="alert-low">101/80</span> (90/60 kln)</td>
        <td>149/70</td>
        <td>125/66 &ndash; 113/67</td>
        <td>122/65 &ndash; 140/79</td>
        <td><span class="alert-high">144/81</span> &rarr; 122/82</td>
        <td>Fase awal syok hipovolemik teratasi dengan NaCl 0.9%. TD kembali meningkat membuktikan perlunya antihipertensi dilanjutkan.</td>
      </tr>
      <tr>
        <td><strong>Nadi (kali/menit)</strong></td>
        <td>60 &ndash; 100</td>
        <td><span class="alert-high">105</span> (Takikardia)</td>
        <td>92</td>
        <td>90 &ndash; 95</td>
        <td>81 &ndash; 99</td>
        <td>88 &ndash; 94</td>
        <td>Takikardia awal kompensasi dehidrasi membaik pasca rehidrasi.</td>
      </tr>
      <tr>
        <td><strong>Frekuensi Nafas (x/mnt)</strong></td>
        <td>12 &ndash; 20</td>
        <td><span class="alert-high">22</span> (Takipnea)</td>
        <td>20</td>
        <td>20</td>
        <td>20</td>
        <td>20</td>
        <td>Takipnea ringan saat MRS membaik.</td>
      </tr>
      <tr>
        <td><strong>Suhu Tubuh (&deg;C)</strong></td>
        <td>36.5 &ndash; 37.5</td>
        <td>36.0</td>
        <td>36.5</td>
        <td>36.2 &ndash; 36.4</td>
        <td>36.0 &ndash; 36.5</td>
        <td>36.0 &ndash; 37.5</td>
        <td>Afebris sepanjang perawatan.</td>
      </tr>
      <tr>
        <td><strong>SpO2 (%)</strong></td>
        <td>&ge; 95%</td>
        <td>96%</td>
        <td>96%</td>
        <td>95% &ndash; 98%</td>
        <td>98% &ndash; 99%</td>
        <td>99%</td>
        <td>Saturasi oksigen stabil dengan udara ruangan.</td>
      </tr>
      <tr>
        <td><strong>Keluhan Pasien</strong></td>
        <td>Tidak ada</td>
        <td>Muntah &gt;10x, mual+++, batuk+</td>
        <td>Mual++, lemas, batuk+</td>
        <td>Muntah nihil, mual+, batuk+</td>
        <td>Mual berkurang, batuk (-)</td>
        <td><strong>TAK (Minta Pulang)</strong></td>
        <td>Keluhan saluran cerna dan batuk membaik secara klinis.</td>
      </tr>
    </tbody>
  </table>

  <!-- ANALISIS HASIL LABORATORIUM -->
  <h2>III. Analisis Mendalam Hasil Laboratorium (Temuan, Masalah, &amp; Perbaikan)</h2>
  <table class="data-table">
    <thead>
      <tr>
        <th>Pemeriksaan Lab</th>
        <th>Nilai Rujukan</th>
        <th>Hasil Pasien</th>
        <th>Status</th>
        <th>Analisis Patofisiologis &amp; Implikasi Klinis Farmasi</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Ureum Darah</strong></td>
        <td>21 &ndash; 43 mg/dL</td>
        <td><strong>57 mg/dL</strong></td>
        <td><span class="alert-high">TINGGI</span></td>
        <td rowspan="2">
          <strong>Azotemia Prerenal / Acute Kidney Injury (AKI):</strong><br>
          Penurunan perfusi renal berat akibat dehidrasi (vomitus &gt;10x/hari) diperparah konsumsi <strong>Ibuprofen 2x400 mg</strong> (menghambat prostaglandin vasodilator renal arteriol aferen).<br>
          <strong>Kalkulasi Cockcroft-Gault:</strong> CrCl = <strong>30.69 mL/menit</strong>.<br>
          <strong>Kalkulasi CKD-EPI 2021:</strong> eGFR = <strong>31.46 mL/min/1.73m&sup2;</strong> (Stadium G3b).<br>
          <em>Hal yang Salah / Harus Diperbaiki:</em> Metoklopramid harus diturunkan 50%. Metformin harus distop. <strong>Tidak ada pemeriksaan ulang kreatinin sebelum pasien pulang</strong> untuk menilai reversibilitas AKI.
        </td>
      </tr>
      <tr>
        <td><strong>Kreatinin Serum</strong></td>
        <td>0.6 &ndash; 1.1 mg/dL</td>
        <td><strong>1.80 mg/dL</strong></td>
        <td><span class="alert-high">TINGGI</span></td>
      </tr>
      <tr>
        <td><strong>Natrium (Na)</strong></td>
        <td>135.0 &ndash; 147.0 mmol/L</td>
        <td><strong>127.36 mmol/L</strong></td>
        <td><span class="alert-low">RENDAH</span></td>
        <td rowspan="2">
          <strong>Hiponatremia &amp; Hipokloremia Hipovolemik:</strong><br>
          Kehilangan elektrolit masif bersama asam lambung (HCl) dan cairan cerna saat muntah berulang. Diberikan infus NaCl 0.9% 20 tpm.<br>
          <em>Hal yang Salah / Harus Diperbaiki:</em> <strong>Elektrolit TIDAK PERNAH diperiksa ulang</strong> pasca koreksi cairan untuk memverifikasi apakah natrium dan klorida sudah mencapai nilai normal (&ge;135 dan &ge;95 mmol/L).
        </td>
      </tr>
      <tr>
        <td><strong>Klorida (Cl)</strong></td>
        <td>95.0 &ndash; 105.0 mmol/L</td>
        <td><strong>87.75 mmol/L</strong></td>
        <td><span class="alert-low">RENDAH</span></td>
      </tr>
      <tr>
        <td><strong>Kalium (K)</strong></td>
        <td>3.5 &ndash; 5.5 mmol/L</td>
        <td><strong>4.23 mmol/L</strong></td>
        <td>NORMAL</td>
        <td>Kadar kalium serum dalam batas normal, tidak memerlukan suplementasi kalium.</td>
      </tr>
      <tr>
        <td><strong>GDS Awal (14/10)</strong></td>
        <td>&lt; 200 mg/dL</td>
        <td><strong>310 mg/dL</strong></td>
        <td><span class="alert-high">TINGGI</span></td>
        <td rowspan="4">
          <strong>Kegagalan Kendali Glikemik Puasa Rawat Inap (Target ADA: 140&ndash;180 mg/dL):</strong><br>
          Meskipun dosis Novorapid dinaikkan bertahap (3x8 &rarr; 3x10 &rarr; 3x12 UI), kadar GDP pasien pada pagi hari justru naik signifikan (235 &rarr; 236 &rarr; <strong>298 mg/dL</strong>).<br>
          <em>Penyebab Farmakologis:</em> Novorapid (insulin aspart) hanya bekerja 3&ndash;5 jam untuk mengontrol glukosa makan. Pasien <strong>tidak mendapatkan insulin basal</strong> untuk menekan produksi glukosa hepatik malam hingga pagi hari.<br>
          <em>Hal yang Harus Diperbaiki:</em> Mengganti regimen bolus-tunggal dengan regimen <strong>Basal-Bolus</strong> (tambahkan insulin basal kerja panjang seperti Glargine 8&ndash;10 unit malam).
        </td>
      </tr>
      <tr>
        <td><strong>GDS H1 (15/10)</strong></td>
        <td>&lt; 200 mg/dL</td>
        <td><strong>208 mg/dL</strong></td>
        <td><span class="alert-high">TINGGI</span></td>
      </tr>
      <tr>
        <td><strong>GDP H2 (16/10)</strong></td>
        <td>70 &ndash; 115 mg/dL</td>
        <td><strong>235 mg/dL</strong></td>
        <td><span class="alert-high">TINGGI</span></td>
      </tr>
      <tr>
        <td><strong>GDP H4 (18/10)</strong></td>
        <td>70 &ndash; 115 mg/dL</td>
        <td><strong>298 mg/dL</strong></td>
        <td><span class="alert-high">TINGGI</span></td>
      </tr>
      <tr>
        <td><strong>Hemoglobin (Hb)</strong></td>
        <td>11.7 &ndash; 15.5 g/dL</td>
        <td><strong>11.6 g/dL</strong></td>
        <td><span class="alert-low">RENDAH</span></td>
        <td rowspan="2">
          <strong>Anemia Ringan Normositik Normokrom:</strong><br>
          MCV (86.3 fL) dan MCH (29.5 pg) normal. Kemungkinan anemia penyakit kronis (DM/CKD) atau hemodilusi pasca hidrasi cairan. Cukup dimonitor berkala.
        </td>
      </tr>
      <tr>
        <td><strong>Hematokrit</strong></td>
        <td>35 &ndash; 47 %</td>
        <td><strong>33.9 %</strong></td>
        <td><span class="alert-low">RENDAH</span></td>
      </tr>
      <tr>
        <td><strong>SGOT / SGPT</strong></td>
        <td>&lt; 35 / &lt; 34 U/L</td>
        <td><strong>39 / 23 U/L</strong></td>
        <td>SGOT &uarr; ringan</td>
        <td>Peningkatan ringan transient pasca dehidrasi / perlemakan hati. Tidak ada kerusakan hepatoseluler bermakna.</td>
      </tr>
    </tbody>
  </table>

  <!-- DAFTAR DRP LENGKAP -->
  <h2>IV. Daftar Lengkap Drug Related Problems (DRP) yang Teridentifikasi</h2>
  
  <!-- DRP 1 -->
  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 1: Dosis Berlebih pada Gangguan Ginjal (Overdose in Renal Impairment)</span>
      <span class="drp-badge">PCNE C3.1 / P1.2</span>
    </div>
    <div class="drp-body">
      <strong>Obat Terkait:</strong> Injeksi Metoklopramid 3 x 10 mg IV (30 mg/hari).<br>
      <strong>Analisis Klinis:</strong> Pasien mengalami penurunan fungsi ginjal dengan CrCl = 30.69 mL/menit (eGFR 31.46 mL/min/1.73m&sup2;). Metoklopramid dieliminasi &gt;80% melalui ginjal. Pada CrCl &lt; 40 mL/menit, waktu paruh meningkat hingga 3 kali lipat dan clearance menurun drastis, menyebabkan akumulasi obat. Pasien lansia wanita sangat rentan terhadap <em>Tardive Dyskinesia</em> dan <em>Extrapyramidal Symptoms (EPS)</em> (FDA Boxed Warning).<br>
      <div class="rec-box">
        <strong>Rekomendasi Farmasis:</strong> Sesuai guideline FDA dan Lexicomp, jika CrCl 10&ndash;40 mL/menit, dosis metoklopramid harus <strong>diturunkan 50%</strong> (menjadi 5 mg IV q8h atau 10 mg q12h; max 15 mg/hari). Karena muntah telah teratasi sejak 16/10, rekomendasikan <strong>HENTIKAN terapi metoklopramid</strong>.
      </div>
    </div>
  </div>

  <!-- DRP 2 -->
  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 2: Duplikasi Terapi Inap Berbahaya (Domperidone + Metoklopramid IV)</span>
      <span class="drp-badge">PCNE C1.3 / P2.1</span>
    </div>
    <div class="drp-body">
      <strong>Obat Terkait:</strong> Injeksi Metoklopramid 3 x 10 mg IV + Domperidone tablet 2 x 10 mg oral (dimulai 17/10).<br>
      <strong>Analisis Klinis:</strong> Keduanya merupakan antagonis reseptor dopamin D2. Penggunaan bersamaan merupakan duplikasi terapi yang tidak memberikan manfaat aditif namun melipatgandakan risiko efek samping: (1) Perpanjangan interval QT dan aritmia fatal ventrikel / torsades de pointes (peringatan keras EMA &amp; FDA); (2) Sindrom ekstrapiramidal.<br>
      <div class="rec-box">
        <strong>Rekomendasi Farmasis:</strong> Hentikan salah satu obat. Karena muntah sudah tidak ada dan mual ringan, hentikan Domperidone oral dan tapering-off / stop Metoklopramid.
      </div>
    </div>
  </div>

  <!-- DRP 3 -->
  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 3: Kegagalan Regimen Insulin Mengontrol GDP (Sub-optimal Inpatient Glycemic Regimen)</span>
      <span class="drp-badge">PCNE C1.4 / P1.2</span>
    </div>
    <div class="drp-body">
      <strong>Obat Terkait:</strong> Novorapid (Insulin Aspart) injeksi SC 3x8 UI &rarr; 3x10 UI &rarr; 3x12 UI tanpa insulin basal.<br>
      <strong>Analisis Klinis:</strong> Target ADA rawat inap non-kritis adalah 140&ndash;180 mg/dL. GDP pasien pada hari ke-3 = 235, hari ke-4 = 236, dan hari ke-5 = 298 mg/dL. Novorapid hanya bekerja 3&ndash;5 jam saat makan. Tanpa insulin basal (Glargine/Detemir/Degludec), glukosa darah puasa malam&ndash;pagi hari tidak terkontrol. Menitrasi Novorapid hingga 36 unit/hari tanpa basal adalah strategi yang salah dan berisiko hipoglikemia prandial siang/sore.<br>
      <div class="rec-box">
        <strong>Rekomendasi Farmasis:</strong> Terapkan regimen <strong>Basal-Bolus</strong> sesuai ADA Standards of Care: berikan insulin basal (Insulin Glargine 8&ndash;10 unit sekali sehari malam) dikombinasikan dengan insulin prandial Novorapid dosis lebih kecil (misal 3 x 4&ndash;6 unit sebelum makan).
      </div>
    </div>
  </div>

  <!-- DRP 4 -->
  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 4: Indikasi Belum Diterapi (Untreated Indication) &bull; Batuk Berdahak Putih / ISPA</span>
      <span class="drp-badge">PCNE C1.1 / P1.2</span>
    </div>
    <div class="drp-body">
      <strong>Kondisi Pasien:</strong> Batuk berdahak putih persisten tercatat di CPPT sejak 14/10 s/d 17/10 dengan diagnosis sekunder ISPA.<br>
      <strong>Analisis Klinis:</strong> Tidak ada terapi mukolitik maupun ekspektoran yang diberikan selama pasien rawat inap. Retensi sputum pada pasien lansia berisiko komplikasi jalan napas.<br>
      <div class="rec-box">
        <strong>Rekomendasi Farmasis:</strong> Berikan terapi mukolitik oral, seperti <strong>Ambroxol 3 x 30 mg tablet</strong> atau <strong>N-Asetilsistein 3 x 200 mg kapsul</strong> selama 3&ndash;5 hari.
      </div>
    </div>
  </div>

  <!-- DRP 5 -->
  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 5: Penggunaan Obat Nefrotoksik Sebelumnya (NSAID pada Dehidrasi &amp; Lansia)</span>
      <span class="drp-badge">PCNE C1.2 / P2.1</span>
    </div>
    <div class="drp-body">
      <strong>Obat Terkait:</strong> Ibuprofen 2 x 400 mg (diberikan saat berobat ke UGD tgl 11/10/2026).<br>
      <strong>Analisis Klinis:</strong> Pasien lansia dengan riwayat HT, DM, dan dehidrasi akibat muntah diberikan NSAID dosis penuh. Ibuprofen menghambat prostaglandin vasodilator di arteriol aferen ginjal, memicu hipoperfusi glomerulus akut dan mempercepat terjadinya AKI (Ureum 57, Kreatinin 1.80 mg/dL).<br>
      <div class="rec-box">
        <strong>Rekomendasi Farmasis:</strong> Hindari seluruh golongan NSAID pada pasien dengan gangguan ginjal atau dehidrasi. Untuk antipiretik/analgesik gunakan <strong>Parasetamol oral 500 mg prn (max 2 g/hari pada lansia)</strong>.
      </div>
    </div>
  </div>

  <!-- DRP 6 -->
  <div class="drp-box" style="border-left-color: #dc2626;">
    <div class="drp-header">
      <span class="drp-title">&#9888; DRP 6: DUPLIKASI FATAL RESEP PULANG (Gavistal 3x10 mg + Domperidone 2x10 mg)</span>
      <span class="drp-badge" style="background:#fee2e2; color:#b91c1c;">MAJOR RESEP PULANG</span>
    </div>
    <div class="drp-body">
      <strong>Obat Terkait:</strong> Resep pulang No. IRJ-261018-87885 memuat: (1) <strong>GAVISTAL 10 MG TAB 3x1</strong>; (2) <strong>DOMPERIDONE 10 MG TAB 2x1</strong>.<br>
      <strong>Analisis Klinis:</strong> <strong>Gavistal adalah merek dagang Metoklopramid HCl 10 mg!</strong> Pasien diresepkan Metoklopramid 3x10 mg bersamaan dengan Domperidone 2x10 mg untuk dibawa pulang. Ini adalah duplikasi obat 100% dari kelas yang sama (Antagonis Dopamin D2). Pada wanita lansia dengan CrCl 30.69 mL/menit, kombinasi ini sangat berbahaya karena memicu akumulasi obat, diskinesia tardif, gejala ekstrapiramidal berat, dan pemanjangan interval QT (aritmia jantung mematikan).<br>
      <div class="rec-box" style="background:#fef2f2; border-left-color:#dc2626; color:#991b1b;">
        <strong>Rekomendasi Farmasis:</strong> <strong>BATALKAN GAVISTAL DAN DOMPERIDONE.</strong> Pasien sudah menyatakan tidak mual/muntah (TAK) saat pulang, sehingga prokinetik/antiemetik rutin sudah tidak diindikasikan lagi.
      </div>
    </div>
  </div>

  <!-- DRP 7 -->
  <div class="drp-box" style="border-left-color: #dc2626;">
    <div class="drp-header">
      <span class="drp-title">&#9888; DRP 7: OMISSION TERAPI KRONIS SAAT PULANG (Amlodipin &amp; Clopidogrel Tidak Diresepkan)</span>
      <span class="drp-badge" style="background:#fee2e2; color:#b91c1c;">MAJOR RESEP PULANG</span>
    </div>
    <div class="drp-body">
      <strong>Obat Terkait:</strong> Amlodipin 10 mg 1x1 dan Clopidogrel 75 mg 1x1 (obat rutin pasien sebelum MRS).<br>
      <strong>Analisis Klinis:</strong> Obat rutin pasien dihentikan sementara saat masuk RS karena tekanan darah drop akibat dehidrasi. Namun pada saat pulang (18/10), tekanan darah pasien sudah meningkat mencapai <strong>144/81 mmHg</strong>. Pada resep pulang, dokter <strong>TIDAK MERESEPKAN KEMBALI Amlodipin maupun Clopidogrel!</strong> Pasien berisiko tinggi mengalami hipertensi rebound tidak terkontrol dan peningkatan risiko kejadian serebrovaskular/kardiovaskular.<br>
      <div class="rec-box">
        <strong>Rekomendasi Farmasis:</strong> Lakukan rekonsiliasi obat pulang segera: <strong>Mulai kembali Amlodipin 5&ndash;10 mg 1 x sehari</strong> (target TD &lt; 130/80 mmHg) dan <strong>Clopidogrel 75 mg 1 x sehari</strong>.
      </div>
    </div>
  </div>

  <!-- DRP 8 -->
  <div class="drp-box" style="border-left-color: #d97706;">
    <div class="drp-header">
      <span class="drp-title">DRP 8: Kombinasi Terapi DM Pulang Berisiko Hipoglikemia Berat (Glikuidon + Novorapid 3x12 UI)</span>
      <span class="drp-badge" style="background:#fef3c7; color:#b45309;">SAFETY ALERT</span>
    </div>
    <div class="drp-body">
      <strong>Obat Terkait:</strong> Glikuidon 30 mg tab 1x1 pagi ac + Novorapid Flexpen 3 x 12 UI ac (total 36 UI/hari).<br>
      <strong>Analisis Klinis:</strong> Penggantian Glimepirid ke Glikuidon sudah sangat tepat untuk pasien dengan CrCl 30.69 mL/menit (karena Glikuidon dieliminasi &gt;95% lewat empedu/feses). Namun, menggabungkan Glikuidon dengan insulin bolus dosis tinggi (36 unit/hari) pada pasien lansia yang baru pulih dari anoreksia berisiko sangat tinggi memicu <strong>hipoglikemia berat yang fatal</strong> di rumah. Selain itu, pada resep pulang jarum Novofine hanya diresepkan 1 buah, padahal suntikan 3x sehari.<br>
      <div class="rec-box">
        <strong>Rekomendasi Farmasis:</strong> Evaluasi penyederhanaan regimen: Jika asupan makan sudah baik, optimalkan <strong>Glikuidon 30 mg 1&ndash;2 kali sehari</strong> ac. Jika masih membutuhkan insulin, gunakan insulin basal malam dosis kecil (misal Glargine 8&ndash;10 unit malam) daripada Novorapid dosis tinggi + Glikuidon. Berikan jarum suntik yang cukup dan edukasi tanda hipoglikemia serta SMBG.
      </div>
    </div>
  </div>

  <!-- DRP 9 -->
  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 9: Polifarmasi Saluran Cerna Berlebihan Saat Pulang (5 Macam Obat Lambung)</span>
      <span class="drp-badge">PCNE C1.3 / P2.1</span>
    </div>
    <div class="drp-body">
      <strong>Obat Terkait:</strong> Antasida syr 3x1, Omeprazole 20 mg 2x1, Rebamipide 3x1, Domperidone 2x1, Gavistal (Metoklopramid) 3x1.<br>
      <strong>Analisis Klinis:</strong> Pasien dipulangkan dengan 5 macam obat lambung/mual padahal keluhan muntah sudah sembuh total dan mual sudah hilang (TAK). Ini adalah overtreatment polifarmasi yang membebani pasien lansia baik dari segi biaya, kepatuhan, maupun interaksi obat (Antasida dapat mengikat obat lain).<br>
      <div class="rec-box">
        <strong>Rekomendasi Farmasis:</strong> Cukup berikan <strong>Omeprazole 20 mg kapsul 1 x sehari pagi ac</strong> selama 5&ndash;7 hari untuk proteksi sisa iritasi. Hentikan Antasida sirup, Rebamipide, Domperidone, dan Gavistal.
      </div>
    </div>
  </div>

  <!-- DRP 10 -->
  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 10: Ketiadaan Pemantauan Laboratorium Kontrol Pasca-Tindakan (Lack of Follow-up Labs)</span>
      <span class="drp-badge">PCNE C3.5 / P3.1</span>
    </div>
    <div class="drp-body">
      <strong>Parameter:</strong> Elektrolit darah (Na, Cl) dan Fungsi Ginjal (Ureum, Kreatinin).<br>
      <strong>Analisis Klinis:</strong> Pasien masuk dengan hiponatremia (127.36), hipokloremia (87.75), dan kreatinin 1.80 mg/dL. Setelah rehidrasi NaCl 0.9% selama 4 hari, pasien dipulangkan tanpa ada evaluasi laboratorium ulang untuk memastikan kadar elektrolit sudah normal dan untuk membedakan apakah AKI telah pulih (prerenal AKI reversibel) atau menetap menjadi CKD.<br>
      <div class="rec-box">
        <strong>Rekomendasi Farmasis:</strong> Jadwalkan pemeriksaan kontrol laboratorium (Ureum, Kreatinin, Elektrolit, HbA1c, dan GDP/GD2PP) saat kontrol ke Poli Penyakit Dalam 1 minggu pasca pulang.
      </div>
    </div>
  </div>

  <!-- EVIDENCE & GUIDELINE SCREENSHOTS -->
  <h2>V. Bukti Guideline Resmi &amp; Penyesuaian Dosis Terkini</h2>
  <p>
    Berikut adalah bukti tangkapan layar (*screen capture*) dari panduan dan literatur klinis resmi terbaru (ADA, Lexicomp/FDA, EMA, KDIGO/PERKENI, dan PERHI) yang menjadi dasar ilmiah penetapan DRP dan penyesuaian dosis terapi pasien Ny. Sunarti:
  </p>

  <!-- SCREENSHOT 1: ADA INPATIENT -->
  <div class="evidence-container">
    <div class="evidence-caption">BUKTI GUIDELINE 1: American Diabetes Association (ADA) Standards of Care &bull; Target Glukosa Rawat Inap &amp; Basal-Bolus Regimen</div>
    <img src="data:image/png;base64,{img_ada}" alt="ADA Inpatient Guideline">
    <p style="text-align:left; font-size:12px; margin:8px 12px 0 12px; color:#475569;">
      <strong>Penerapan Klinis:</strong> Target kendali glikemik rawat inap non-kritis adalah 140&ndash;180 mg/dL. ADA secara tegas melarang pemberian insulin bolus/rapid-acting tunggal tanpa insulin basal karena gagal mengontrol produksi glukosa hepatik puasa (terbukti dari GDP pasien yang melonjak ke 298 mg/dL). Pasien membutuhkan insulin basal (seperti Glargine 8&ndash;10 unit malam).
    </p>
  </div>

  <!-- SCREENSHOT 2: LEXICOMP & FDA METOCLOPRAMIDE RENAL -->
  <div class="evidence-container">
    <div class="evidence-caption">BUKTI GUIDELINE 2: Lexicomp Clinical Drug Information &amp; FDA Label &bull; Penyesuaian Dosis Metoklopramid pada Gangguan Ginjal</div>
    <img src="data:image/png;base64,{img_lexi}" alt="Lexicomp Metoclopramide Renal Dosing">
    <p style="text-align:left; font-size:12px; margin:8px 12px 0 12px; color:#475569;">
      <strong>Penerapan Klinis:</strong> Pasien memiliki CrCl 30.69 mL/menit. Sesuai label FDA dan Lexicomp, pasien dengan CrCl 10&ndash;40 mL/menit wajib mendapatkan penurunan dosis sebesar 50% (5 mg IV q8h atau 10 mg q12h; max 15 mg/hari). Pemberian dosis normal 3x10 mg IV meningkatkan risiko fatal <em>Tardive Dyskinesia</em> pada lansia wanita.
    </p>
  </div>

  <!-- SCREENSHOT 3: DRUG INTERACTION DOMPERIDONE + GAVISTAL -->
  <div class="evidence-container">
    <div class="evidence-caption">BUKTI GUIDELINE 3: Drug Interaction &amp; Duplication Alert &bull; Gavistal (Metoklopramid) + Domperidone Co-Prescription</div>
    <img src="data:image/png;base64,{img_dupl}" alt="Duplication Gavistal Domperidone">
    <p style="text-align:left; font-size:12px; margin:8px 12px 0 12px; color:#475569;">
      <strong>Penerapan Klinis:</strong> Gavistal adalah nama dagang Metoklopramid 10 mg. Peresepan Gavistal bersama Domperidone pada resep pulang adalah duplikasi berbahaya (Risk Category D/X) yang melipatgandakan risiko perpanjangan interval QT aritmia ventrikel serta sindrom ekstrapiramidal. Resep ini harus diintervensi dan dibatalkan.
    </p>
  </div>

  <!-- SCREENSHOT 4: KDIGO & PERKENI DIABETES IN CKD -->
  <div class="evidence-container">
    <div class="evidence-caption">BUKTI GUIDELINE 4: KDIGO 2023 &amp; PERKENI Guidelines &bull; Pemilihan Terapi Antidiabetes Oral pada Gangguan Ginjal</div>
    <img src="data:image/png;base64,{img_kdigo}" alt="KDIGO PERKENI Diabetes in CKD">
    <p style="text-align:left; font-size:12px; margin:8px 12px 0 12px; color:#475569;">
      <strong>Penerapan Klinis:</strong> Metformin dihentikan saat dehidrasi akut dan eGFR ~31 mL/min/1.73m&sup2; guna mencegah asidosis laktat. Glimepirid digantikan oleh Glikuidon karena Glikuidon dieliminasi &gt;95% via empedu/feses sehingga aman untuk ginjal. Namun, kombinasi Glikuidon dengan Novorapid 3x12 UI harus diwaspadai terhadap risiko hipoglikemia.
    </p>
  </div>

  <!-- SCREENSHOT 5: PERHI & REKONSILIASI OBAT HIPERTENSI -->
  <div class="evidence-container">
    <div class="evidence-caption">BUKTI GUIDELINE 5: Konsensus PERHI 2021 &amp; ACC/AHA &bull; Target Tekanan Darah &amp; Rekonsiliasi Obat Kronis Pulang</div>
    <img src="data:image/png;base64,{img_perhi}" alt="PERHI ACC AHA Medication Reconciliation">
    <p style="text-align:left; font-size:12px; margin:8px 12px 0 12px; color:#475569;">
      <strong>Penerapan Klinis:</strong> Target tekanan darah pada pasien DM dengan nefropati adalah &lt; 130/80 mmHg. Amlodipin 10 mg dan Clopidogrel 75 mg yang distop saat MRS harus dilanjutkan kembali saat pasien stabil dan dipulangkan guna mencegah stroke/MACE dan hipertensi tidak terkontrol.
    </p>
  </div>

  <!-- REKONSILIASI TERAPI PULANG LENGKAP -->
  <h2>VI. Rekonsiliasi Terapi Pulang yang Direkomendasikan</h2>
  <table class="comparison-table">
    <thead>
      <tr>
        <th style="width: 48%;" class="col-doctor">Resep Pulang Aktual Dokter (IRJ-261018-87885)</th>
        <th style="width: 52%;" class="col-pharma">Rekomendasi Rekonsiliasi Farmasis Klinis</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="col-doctor">
          1. Antasida Sirup 3 x 1 C (10 mL) ac<br>
          2. Domperidone 10 mg tab 2 x 1 ac<br>
          3. <strong>Gavistal (Metoklopramid) 10 mg tab 3 x 1 ac</strong><br>
          4. Glikuidon 30 mg tab 1 x 1 pagi ac<br>
          5. Novorapid Flexpen 3 x 12 UI ac (Jarum: 1 pcs)<br>
          6. Omeprazole 20 mg kap 2 x 1 ac<br>
          7. Rebamipide 100 mg tab 3 x 1 ac<br>
          <span style="color:#b91c1c; font-weight:bold;">&times; Amlodipin &amp; Clopidogrel TIDAK ADA</span>
        </td>
        <td class="col-pharma">
          1. <strong>Amlodipin 1 x 5&ndash;10 mg PO pagi:</strong> Dimulai kembali (TD 144/81 mmHg, target &lt;130/80).<br>
          2. <strong>Clopidogrel 1 x 75 mg PO pagi:</strong> Dimulai kembali untuk prevensi sekunder kardio/stroke.<br>
          3. <strong>Glikuidon 1 x 30 mg PO pagi sebelum makan:</strong> Dilanjutkan sebagai OAD aman ginjal.<br>
          4. <strong>Evaluasi Insulin:</strong> Jika glukosa darah masih &gt;200 mg/dL, rekomendasikan insulin basal (Glargine 8&ndash;10 unit malam) daripada Novorapid 3x12 UI + Glikuidon. Jika tetap Novorapid, turunkan dosis menjadi 3 x 4&ndash;6 UI ac dan sediakan jarum yang cukup (&plusmn;10 pcs).<br>
          5. <strong>Omeprazole 1 x 20 mg PO pagi (1 jam ac):</strong> Cukup 1 x sehari selama 5&ndash;7 hari saja.<br>
          6. <strong>BATALKAN:</strong> Gavistal (Metoklopramid), Domperidone, Antasida, dan Rebamipide (Polifarmasi dieliminasi).
        </td>
      </tr>
    </tbody>
  </table>

  <!-- KONSELING & KIE -->
  <h2>VII. Rencana Konseling, Edukasi Pasien (KIE), &amp; Monitoring Lanjutan</h2>
  <ul style="font-size:12.5px; line-height:1.6; color:#334155;">
    <li><strong>Edukasi Riwayat Alergi Obat:</strong> Ingatkan pasien dan keluarga bahwa pasien memiliki riwayat alergi terhadap <strong>Amoksisilin dan Ampisilin</strong> (gatal dan ruam merah). Wajib melapor ke petugas setiap kali berobat di fasilitas kesehatan mana pun.</li>
    <li><strong>Edukasi Pencegahan &amp; Penanganan Hipoglikemia:</strong> Karena pasien menggunakan Glikuidon dan/atau Insulin, jelaskan gejala hipoglikemia (keringat dingin, gemetar, berdebar, pusing, lemas mendadak, pandangan kabur). Bila muncul tanda tersebut, segera minum 1 gelas air gula atau 2&ndash;3 sendok teh permen/madu dan periksa gula darah.</li>
    <li><strong>Edukasi Pola Makan (Diet DM Rendah Garam 3J):</strong> Patuhi Jadwal, Jenis, dan Jumlah makanan. Hindari makanan/minuman manis sederhana dan batasi asupan garam. Hindari jajan sembarangan (seperti susu jahe pinggir jalan).</li>
    <li><strong>Rencana Monitoring Lanjutan:</strong>
      <ul>
        <li>Monitoring Tekanan Darah harian (Target: &lt; 130/80 mmHg).</li>
        <li>Monitoring Glukosa Darah Mandiri (SMBG) puasa dan 2 jam pasca makan (Target GDP: 80&ndash;130 mg/dL di rumah; GD2PP: &lt; 180 mg/dL).</li>
        <li>Pemeriksaan Laboratorium Kontrol 1 minggu pasca pulang: Ureum, Kreatinin Serum, Elektrolit (Na, K, Cl), dan GDP/HbA1c.</li>
      </ul>
    </li>
  </ul>

  <!-- TANDA TANGAN -->
  <table class="footer-sig">
    <tr>
      <td style="width: 50%; font-size: 12px; color: #64748b;">
        RSPAU dr. S. Hardjolukito Yogyakarta<br>
        Unit Farmasi Klinis &bull; Bangsal Rawat Inap Merak
      </td>
      <td style="width: 50%; text-align: right; font-size: 12px;">
        Yogyakarta, 19 Oktober 2026<br>
        <strong>Apoteker Klinis Penelaah,</strong><br><br><br><br>
        <strong>( Tim Farmasi Klinis / Apoteker Pendamping )</strong><br>
        <span style="font-size: 11px; color: #64748b;">SIP. Farmasi Klinis RSPAU Hardjolukito</span>
      </td>
    </tr>
  </table>
</div>

</body>
</html>
"""

report_html_path = r"d:\FILE NINIS\LAPORAN_PEMANTAUAN_TERAPI_OBAT_SUNARTI.html"
report_pdf_path = r"d:\FILE NINIS\LAPORAN_PEMANTAUAN_TERAPI_OBAT_SUNARTI.pdf"

with open(report_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Report HTML written to {report_html_path}")

# Generate PDF using Chrome
chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_exe,
    "--headless=new",
    f"--print-to-pdf={report_pdf_path}",
    "--no-pdf-header-footer",
    report_html_path
]
res = subprocess.run(cmd, capture_output=True, text=True)
print(f"Report PDF generated: exists={os.path.exists(report_pdf_path)}, size={os.path.getsize(report_pdf_path) if os.path.exists(report_pdf_path) else 0}")

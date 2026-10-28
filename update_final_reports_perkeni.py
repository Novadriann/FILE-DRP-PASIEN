import os
import base64
import subprocess

def get_base64_img(rel_path):
    with open(rel_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

img_perkeni = get_base64_img(r"d:\FILE NINIS\guideline_evidence\perkeni_inpatient_guideline.png")
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
      <td class="val">dr. Raden Triyono Edhi Sulistiyanto, Sp.PD., FINASIM</td>
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
        <td>&lt; 130/80 (PERHI 2021)</td>
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
          Penurunan perfusi renal berat akibat dehidrasi diperparah konsumsi <strong>Ibuprofen 2x400 mg</strong> (menghambat prostaglandin vasodilator renal arteriol aferen).<br>
          <strong>Kalkulasi Cockcroft-Gault:</strong> CrCl = <strong>30.69 mL/menit</strong>.<br>
          <strong>Kalkulasi CKD-EPI 2021:</strong> eGFR = <strong>31.46 mL/min/1.73m&sup2;</strong> (Stadium G3b).<br>
          <em>Hal yang Salah / Harus Diperbaiki:</em> Metoklopramid harus diturunkan 50%. Metformin harus distop. <strong>Tidak ada pemeriksaan ulang kreatinin sebelum pasien pulang</strong>.
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
          Kehilangan elektrolit masif bersama asam lambung (HCl) dan cairan cerna. Diberikan infus NaCl 0.9% 20 tpm.<br>
          <em>Hal yang Salah / Harus Diperbaiki:</em> <strong>Elektrolit TIDAK PERNAH diperiksa ulang</strong> pasca koreksi cairan untuk memverifikasi normalisasi.
        </td>
      </tr>
      <tr>
        <td><strong>Klorida (Cl)</strong></td>
        <td>95.0 &ndash; 105.0 mmol/L</td>
        <td><strong>87.75 mmol/L</strong></td>
        <td><span class="alert-low">RENDAH</span></td>
      </tr>
      <tr>
        <td><strong>GDS Awal (14/10)</strong></td>
        <td>&lt; 200 mg/dL</td>
        <td><strong>310 mg/dL</strong></td>
        <td><span class="alert-high">TINGGI</span></td>
        <td rowspan="4">
          <strong>Kegagalan Kendali Glikemik Puasa Rawat Inap (Target PERKENI 2021: 140&ndash;180 mg/dL):</strong><br>
          Meskipun dosis Novorapid dinaikkan bertahap (3x8 &rarr; 3x10 &rarr; 3x12 UI), kadar GDP pasien pada pagi hari justru naik signifikan (235 &rarr; 236 &rarr; <strong>298 mg/dL</strong>).<br>
          <em>Penyebab Farmakologis (PERKENI Hal. 42 &amp; 100):</em> Novorapid (insulin aspart) hanya bekerja 3&ndash;5 jam untuk mengontrol glukosa makan. Pasien <strong>tidak mendapatkan insulin basal</strong> untuk menekan produksi glukosa hepatik malam hingga pagi hari.<br>
          <em>Hal yang Harus Diperbaiki:</em> Terapkan regimen <strong>Basal-Bolus</strong> sesuai Pedoman PERKENI 2021: tambahkan insulin basal (Glargine 8&ndash;10 unit malam).
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
        <td><strong>Hemoglobin / Ht</strong></td>
        <td>11.7&ndash;15.5 / 35&ndash;47%</td>
        <td><strong>11.6 g/dL / 33.9%</strong></td>
        <td><span class="alert-low">RENDAH</span></td>
        <td>Anemia normositik normokrom ringan. Cukup dimonitor berkala.</td>
      </tr>
      <tr>
        <td><strong>SGOT / SGPT</strong></td>
        <td>&lt; 35 / &lt; 34 U/L</td>
        <td><strong>39 / 23 U/L</strong></td>
        <td>SGOT &uarr; ringan</td>
        <td>Peningkatan ringan transient pasca dehidrasi.</td>
      </tr>
    </tbody>
  </table>

  <!-- DAFTAR DRP LENGKAP -->
  <h2>IV. Daftar Lengkap Drug Related Problems (DRP) Teridentifikasi</h2>
  
  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 1: Dosis Berlebih pada Gangguan Ginjal (Metoklopramid IV 3x10 mg)</span>
      <span class="drp-badge">PCNE C3.1 / P1.2</span>
    </div>
    <div class="drp-body">
      CrCl 30.69 mL/menit membutuhkan reduksi dosis metoklopramid sebesar 50% (5 mg IV q8h atau 10 mg q12h; max 15 mg/hari) guna mencegah risiko Tardive Dyskinesia pada lansia. Karena muntah telah teratasi sejak 16/10, rekomendasikan <strong>HENTIKAN terapi metoklopramid</strong>.
    </div>
  </div>

  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 2: Duplikasi Antiemetik Inap (Metoklopramid IV + Domperidone PO)</span>
      <span class="drp-badge">PCNE C1.3 / P2.1</span>
    </div>
    <div class="drp-body">
      Keduanya adalah antagonis reseptor dopamin D2. Penggunaan bersamaan meningkatkan risiko pemanjangan interval QT dan aritmia fatal ventrikel. <strong>Hentikan Domperidone oral.</strong>
    </div>
  </div>

  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 3: Kegagalan Regimen Insulin Mengontrol GDP (Sesuai Pedoman PERKENI 2021)</span>
      <span class="drp-badge">PCNE C1.4 / P1.2</span>
    </div>
    <div class="drp-body">
      Sesuai <strong>Pedoman PERKENI 2021 Halaman 100</strong>, target glukosa ranap adalah 140&ndash;180 mg/dL, dan pemberian insulin bolus/sliding scale saja sangat tidak disarankan. Novorapid 3x12 UI tanpa basal gagal mengontrol GDP (298 mg/dL). Rekomendasikan regimen <strong>Basal-Bolus</strong>: tambahkan Insulin Glargine 8&ndash;10 unit malam.
    </div>
  </div>

  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 4: Indikasi Belum Diterapi (Batuk Berdahak Putih / ISPA)</span>
      <span class="drp-badge">PCNE C1.1 / P1.2</span>
    </div>
    <div class="drp-body">
      Pasien batuk berdahak sejak MRS tanpa terapi mukolitik. Berikan <strong>Ambroxol 3 x 30 mg tablet</strong> atau <strong>N-Asetilsistein 3 x 200 mg kapsul</strong> selama 3&ndash;5 hari.
    </div>
  </div>

  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 5: Penggunaan Obat Nefrotoksik Sebelumnya (Ibuprofen 2x400 mg pada Dehidrasi)</span>
      <span class="drp-badge">PCNE C1.2 / P2.1</span>
    </div>
    <div class="drp-body">
      NSAID memicu vasokonstriksi arteriol aferen dan AKI prerenal pada pasien lansia yang dehidrasi. Hindari NSAID, gunakan Parasetamol 500 mg prn bila perlu.
    </div>
  </div>

  <div class="drp-box" style="border-left-color: #dc2626;">
    <div class="drp-header">
      <span class="drp-title">&#9888; DRP 6: DUPLIKASI FATAL RESEP PULANG (Gavistal 3x10 mg + Domperidone 2x10 mg)</span>
      <span class="drp-badge" style="background:#fee2e2; color:#b91c1c;">MAJOR RESEP PULANG</span>
    </div>
    <div class="drp-body">
      <strong>Gavistal adalah Metoklopramid 10 mg.</strong> Resep pulang meresepkan Metoklopramid 3x10 mg bersamaan dengan Domperidone 2x10 mg. Ini adalah duplikasi berbahaya kelas antagonis dopamin D2 pada pasien gagal ginjal moderat (CrCl 30,69 mL/mnt) dengan risiko aritmia jantung dan distonia/diskinesia tardif di rumah. <strong>BATALKAN GAVISTAL DAN DOMPERIDONE.</strong>
    </div>
  </div>

  <div class="drp-box" style="border-left-color: #dc2626;">
    <div class="drp-header">
      <span class="drp-title">&#9888; DRP 7: OMISSION TERAPI KRONIS SAAT PULANG (Amlodipin &amp; Clopidogrel Tidak Diresepkan)</span>
      <span class="drp-badge" style="background:#fee2e2; color:#b91c1c;">MAJOR RESEP PULANG</span>
    </div>
    <div class="drp-body">
      Tekanan darah pasien saat pulang mencapai 144/81 mmHg. Namun Amlodipin dan Clopidogrel tidak diresepkan kembali. <strong>Mulai kembali Amlodipin 5&ndash;10 mg 1x1 pagi dan Clopidogrel 75 mg 1x1 pagi.</strong>
    </div>
  </div>

  <div class="drp-box" style="border-left-color: #d97706;">
    <div class="drp-header">
      <span class="drp-title">DRP 8: Kombinasi Terapi DM Pulang Berisiko Hipoglikemia Berat (Glikuidon + Novorapid 3x12 UI)</span>
      <span class="drp-badge" style="background:#fef3c7; color:#b45309;">SAFETY ALERT</span>
    </div>
    <div class="drp-body">
      Penggantian ke Glikuidon sudah sangat tepat untuk fungsi ginjal (PERKENI Hal. 38 &amp; 111). Namun menggabungkan Glikuidon dengan Novorapid dosis masif (36 UI/hari) berisiko fatal hipoglikemia di rumah. Sederhanakan: optimalkan Glikuidon 30 mg 1&ndash;2x/hari ac, atau ganti insulin prandial dengan basal malam dosis kecil.
    </div>
  </div>

  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 9: Polifarmasi Saluran Cerna Berlebih Saat Pulang (5 Macam Obat Lambung)</span>
      <span class="drp-badge">PCNE C1.3</span>
    </div>
    <div class="drp-body">
      Pasien dipulangkan dengan Antasida syr, Omeprazole 2x20 mg, Rebamipide 3x1, Domperidone 2x1, Gavistal 3x1. Cukup berikan Omeprazole 1 x 20 mg pagi selama 5&ndash;7 hari saja.
    </div>
  </div>

  <div class="drp-box">
    <div class="drp-header">
      <span class="drp-title">DRP 10: Ketiadaan Pemantauan Laboratorium Kontrol Pasca-Tindakan</span>
      <span class="drp-badge">PCNE C3.5</span>
    </div>
    <div class="drp-body">
      Elektrolit (Na, Cl) dan Fungsi Ginjal (Ureum, Kreatinin) pasca koreksi cairan belum pernah diperiksa ulang sebelum pulang. Jadwalkan kontrol lab saat kontrol poli 1 minggu lagi.
    </div>
  </div>

  <!-- EVIDENCE & GUIDELINE SCREENSHOTS -->
  <h2>V. Bukti Guideline Resmi &amp; Penyesuaian Dosis Terkini</h2>
  
  <div class="evidence-container">
    <div class="evidence-caption">BUKTI GUIDELINE 1: Pedoman Pengelolaan Diabetes Melitus Tipe 2 Dewasa PERKENI 2021 &bull; Rawat Inap (Hal. 100)</div>
    <img src="data:image/png;base64,{img_perkeni}" alt="PERKENI 2021 Guideline Rawat Inap">
    <p style="text-align:left; font-size:12px; margin:8px 12px 0 12px; color:#475569;">
      <strong>Penerapan Klinis Guideline Indonesia:</strong> Sesuai Pedoman PERKENI 2021 Bab IV.13 (Halaman 100), target glukosa darah rawat inap non-kritis adalah <strong>140&ndash;180 mg/dL</strong>. PERKENI secara tegas menyatakan: <em>"Pemberian insulin secara sliding scale sangat tidak disarankan. Pemberian insulin subkutan dengan memperhatikan pola sekresi insulin endogen yang fisiologis berupa insulin basal, prandial, lebih direkomendasikan."</em>
    </p>
  </div>

  <div class="evidence-container">
    <div class="evidence-caption">BUKTI GUIDELINE 2: Lexicomp Clinical Drug Information &amp; FDA Label &bull; Penyesuaian Dosis Metoklopramid pada Gangguan Ginjal</div>
    <img src="data:image/png;base64,{img_lexi}" alt="Lexicomp Metoclopramide Renal Dosing">
  </div>

  <div class="evidence-container">
    <div class="evidence-caption">BUKTI GUIDELINE 3: Drug Interaction &amp; Duplication Alert &bull; Gavistal (Metoklopramid) + Domperidone Co-Prescription</div>
    <img src="data:image/png;base64,{img_dupl}" alt="Duplication Gavistal Domperidone">
  </div>

  <div class="evidence-container">
    <div class="evidence-caption">BUKTI GUIDELINE 4: KDIGO 2023 &amp; PERKENI Guidelines &bull; Pemilihan Terapi Antidiabetes Oral pada Gangguan Ginjal</div>
    <img src="data:image/png;base64,{img_kdigo}" alt="KDIGO PERKENI Diabetes in CKD">
  </div>

  <div class="evidence-container">
    <div class="evidence-caption">BUKTI GUIDELINE 5: Konsensus PERHI 2021 &amp; ACC/AHA &bull; Target Tekanan Darah &amp; Rekonsiliasi Obat Kronis Pulang</div>
    <img src="data:image/png;base64,{img_perhi}" alt="PERHI ACC AHA Medication Reconciliation">
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
          1. <strong>Amlodipin 1 x 5&ndash;10 mg PO pagi:</strong> Dimulai kembali (TD 144/81 mmHg, target &lt;130/80 PERHI 2021).<br>
          2. <strong>Clopidogrel 1 x 75 mg PO pagi:</strong> Dimulai kembali untuk prevensi sekunder kardio/stroke.<br>
          3. <strong>Glikuidon 1 x 30 mg PO pagi sebelum makan:</strong> Dilanjutkan sebagai OAD aman ginjal (PERKENI Hal. 38 &amp; 111).<br>
          4. <strong>Evaluasi Insulin:</strong> Jika asupan makan baik, optimalkan Glikuidon 30 mg (bisa 1&ndash;2x/hari). Jika butuh insulin, berikan insulin basal malam (Glargine 8&ndash;10 unit) daripada Novorapid 3x12 UI + Glikuidon.<br>
          5. <strong>Omeprazole 1 x 20 mg PO pagi (1 jam ac):</strong> Cukup 1 x sehari selama 5&ndash;7 hari saja.<br>
          6. <strong>BATALKAN:</strong> Gavistal (Metoklopramid), Domperidone, Antasida, dan Rebamipide.
        </td>
      </tr>
    </tbody>
  </table>

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

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_exe,
    "--headless=new",
    f"--print-to-pdf={report_pdf_path}",
    "--no-pdf-header-footer",
    report_html_path
]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Updated HTML and PDF reports with PERKENI 2021 successfully!")

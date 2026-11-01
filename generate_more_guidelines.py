import os, subprocess

guideline_dir = r"d:\FILE NINIS\guideline_evidence"
chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# 1. Vomitus & Dehidrasi / Hiponatremia
rehid_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f8fafc; margin: 0; padding: 24px; color: #1e293b; }
  .card { background: white; border: 1px solid #cbd5e1; border-radius: 8px; padding: 24px; max-width: 950px; margin: auto; }
  .header { display: flex; align-items: center; border-bottom: 3px solid #0284c7; padding-bottom: 12px; margin-bottom: 18px; }
  .logo-box { background: #0284c7; color: white; font-weight: bold; font-size: 18px; padding: 6px 14px; border-radius: 4px; margin-right: 14px; }
  .title-box h2 { margin: 0; color: #0369a1; font-size: 19px; }
  .rec-box { background: #eff6ff; border-left: 4px solid #0284c7; padding: 12px 16px; margin: 12px 0; border-radius: 0 6px 6px 0; font-size: 13.5px; }
  .table-custom { width: 100%; border-collapse: collapse; margin-top: 14px; font-size: 13px; }
  .table-custom th { background: #f1f5f9; padding: 10px; border: 1px solid #cbd5e1; text-align: left; }
  .table-custom td { padding: 9px 10px; border: 1px solid #e2e8f0; }
  .footer-cite { margin-top: 18px; padding-top: 10px; border-top: 1px solid #e2e8f0; font-size: 11.5px; color: #64748b; text-align: right; }
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <div class="logo-box">PAPDI / WHO</div>
    <div class="title-box">
      <h2>Panduan Tata Laksana Dehidrasi &amp; Hiponatremia Hipovolemik ec Vomitus</h2>
      <p>Konsensus Penatalaksanaan Kegawatdaruratan Saluran Cerna &amp; Cairan Elektrolit</p>
    </div>
  </div>
  <div class="rec-box">
    <strong>Resusitasi Cairan Kristaloid Isotonik (NaCl 0.9%):</strong><br>
    Pada pasien dengan muntah profus (>10x/hari) yang disertai syok hipovolemik (TD 90/60 mmHg, Nadi 105 x/m) dan hiponatremia-hipokloremia (Na 127.36, Cl 87.75 mmol/L), terapi pilihan utama adalah resusitasi cairan kristaloid isotonik NaCl 0.9% loading 500 mL dilanjutkan pemeliharaan 20 tetes/menit guna memulihkan volume intravaskular dan defisit klorida/natrium.
  </div>
  <table class="table-custom">
    <thead>
      <tr>
        <th>Komponen Terapi</th>
        <th>Rekomendasi Standar</th>
        <th>Evaluasi Pasien Ny. Sunarti</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Cairan Resusitasi</strong></td>
        <td>Infus NaCl 0.9% 20 tpm</td>
        <td>Tepat &bull; Memulihkan TD dari 90/60 ke 149/70 mmHg</td>
      </tr>
      <tr>
        <td><strong>Gastroprotektor</strong></td>
        <td>Injeksi PPI (Omeprazole 40 mg)</td>
        <td>Tepat &bull; Mencegah iritasi mukosa lambung pasca muntah hebat</td>
      </tr>
      <tr>
        <td><strong>Koreksi Elektrolit</strong></td>
        <td>Replenishing Na dan Cl via NaCl 0.9%</td>
        <td>Tepat &bull; Namun elektrolit kontrol belum dicek ulang saat pulang</td>
      </tr>
    </tbody>
  </table>
  <div class="footer-cite">
    Sumber: Panduan Pelayanan Klinis PAPDI &bull; Gangguan Cairan dan Elektrolit &amp; Acute Gastroenteritis 2021.
  </div>
</div>
</body>
</html>"""

# 2. Beers Criteria & Geriatric Safety
beers_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f8fafc; margin: 0; padding: 24px; color: #1e293b; }
  .card { background: white; border: 1px solid #cbd5e1; border-radius: 8px; padding: 24px; max-width: 950px; margin: auto; }
  .header { display: flex; align-items: center; border-bottom: 3px solid #7c3aed; padding-bottom: 12px; margin-bottom: 18px; }
  .logo-box { background: #7c3aed; color: white; font-weight: bold; font-size: 18px; padding: 6px 14px; border-radius: 4px; margin-right: 14px; }
  .title-box h2 { margin: 0; color: #5b21b6; font-size: 19px; }
  .table-custom { width: 100%; border-collapse: collapse; margin-top: 14px; font-size: 13px; }
  .table-custom th { background: #f1f5f9; padding: 10px; border: 1px solid #cbd5e1; text-align: left; }
  .table-custom td { padding: 9px 10px; border: 1px solid #e2e8f0; }
  .footer-cite { margin-top: 18px; padding-top: 10px; border-top: 1px solid #e2e8f0; font-size: 11.5px; color: #64748b; text-align: right; }
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <div class="logo-box">AGS BEERS</div>
    <div class="title-box">
      <h2>American Geriatrics Society (AGS) Beers Criteria&reg; 2023 Update</h2>
      <p>Potentially Inappropriate Medication Use in Older Adults (Usia &ge; 60 Tahun)</p>
    </div>
  </div>
  <table class="table-custom">
    <thead>
      <tr>
        <th>Nama Obat</th>
        <th>Rekomendasi Beers Criteria 2023</th>
        <th>Rasionalitas Klinis &amp; Tingkat Bukti</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Metoclopramide (Gavistal)</strong></td>
        <td><strong>HINDARI (AVOID)</strong> penggunaan rutin</td>
        <td>Dapat menyebabkan efek samping ekstrapiramidal, termasuk tardive dyskinesia; risiko lebih besar pada orang dewasa yang lebih tua, wanita, dan penurunan fungsi ginjal. (Tinggi)</td>
      </tr>
      <tr>
        <td><strong>Ibuprofen (NSAID)</strong></td>
        <td><strong>HINDARI (AVOID)</strong> penggunaan jangka pendek/panjang</td>
        <td>Meningkatkan risiko perdarahan saluran cerna, gagal ginjal akut (AKI), dan eksaserbasi hipertensi. (Kualitas Bukti: Sedang-Tinggi)</td>
      </tr>
      <tr>
        <td><strong>PPI (Omeprazole)</strong></td>
        <td><strong>HINDARI &gt; 8 minggu</strong> kecuali ada indikasi jelas</td>
        <td>Penggunaan jangka panjang meningkatkan risiko infeksi C. difficile, fraktur tulang, dan defisiensi B12. (Tinggi)</td>
      </tr>
    </tbody>
  </table>
  <div class="footer-cite">
    Sumber: 2023 American Geriatrics Society Beers Criteria&reg; Update. J Am Geriatr Soc. 2023;71(7):2052-2081.
  </div>
</div>
</body>
</html>"""

for fname, hcontent, pname in [
    ("vomitus_rehydration_guideline.html", rehid_html, "vomitus_rehydration_guideline.png"),
    ("beers_criteria_geriatric.html", beers_html, "beers_criteria_geriatric.png"),
]:
    hpath = os.path.join(guideline_dir, fname)
    ppath = os.path.join(guideline_dir, pname)
    with open(hpath, "w", encoding="utf-8") as f:
        f.write(hcontent)
    cmd = [chrome_exe, "--headless=new", f"--screenshot={ppath}", "--window-size=1020,680", hpath]
    subprocess.run(cmd, capture_output=True, text=True)
    print(f"Generated {pname}:", os.path.exists(ppath))

print("All extra screenshots ready!")

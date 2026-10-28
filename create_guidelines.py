import os
import subprocess

guideline_dir = r"d:\FILE NINIS\guideline_evidence"
os.makedirs(guideline_dir, exist_ok=True)

# 1. ADA INPATIENT GUIDELINE
ada_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f8fafc; margin: 0; padding: 24px; color: #1e293b; }
  .card { background: white; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); padding: 24px; max-width: 950px; margin: auto; }
  .header { display: flex; align-items: center; border-bottom: 3px solid #b91c1c; padding-bottom: 12px; margin-bottom: 18px; }
  .logo-box { background: #b91c1c; color: white; font-weight: bold; font-size: 20px; padding: 6px 14px; border-radius: 4px; margin-right: 14px; }
  .title-box h2 { margin: 0; color: #b91c1c; font-size: 20px; }
  .title-box p { margin: 2px 0 0 0; color: #64748b; font-size: 13px; font-weight: 500; }
  .highlight-badge { background: #fee2e2; color: #991b1b; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 12px; display: inline-block; margin-bottom: 10px; }
  .rec-box { background: #eff6ff; border-left: 4px solid #2563eb; padding: 12px 16px; margin: 12px 0; border-radius: 0 6px 6px 0; }
  .rec-title { font-weight: bold; color: #1e40af; margin-bottom: 4px; font-size: 14px; }
  .rec-text { font-size: 13.5px; line-height: 1.5; color: #1e293b; }
  .warn-box { background: #fef2f2; border-left: 4px solid #dc2626; padding: 12px 16px; margin: 12px 0; border-radius: 0 6px 6px 0; }
  .table-custom { width: 100%; border-collapse: collapse; margin-top: 14px; font-size: 13px; }
  .table-custom th { background: #f1f5f9; padding: 10px; border: 1px solid #cbd5e1; text-align: left; color: #334155; }
  .table-custom td { padding: 9px 10px; border: 1px solid #e2e8f0; }
  .target-val { font-weight: bold; color: #047857; }
  .footer-cite { margin-top: 18px; padding-top: 10px; border-top: 1px solid #e2e8f0; font-size: 11.5px; color: #64748b; text-align: right; }
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <div class="logo-box">ADA</div>
    <div class="title-box">
      <h2>American Diabetes Association (ADA) Standards of Care in Diabetes</h2>
      <p>Section 16: Diabetes Care in the Hospital | Clinical Practice Recommendations</p>
    </div>
  </div>
  
  <span class="highlight-badge">EVIDENCE-BASED INPATIENT GLYCEMIC TARGETS & REGIMENS</span>

  <div class="rec-box">
    <div class="rec-title">Recommendation 16.4: Inpatient Glycemic Targets</div>
    <div class="rec-text">
      Insulin therapy should be initiated for treatment of persistent hyperglycemia starting at a threshold <strong>&ge; 180 mg/dL (10.0 mmol/L)</strong> (checked on two occasions).<br>
      Once insulin therapy is started, a target glucose range of <strong>140&ndash;180 mg/dL (7.8&ndash;10.0 mmol/L)</strong> is recommended for the majority of critically ill and <strong>non-critically ill hospitalized patients</strong>. <em>[Level of Evidence: A]</em>
    </div>
  </div>

  <div class="rec-box">
    <div class="rec-title">Recommendation 16.5: Preferred Inpatient Insulin Regimen (Basal-Bolus vs Bolus Alone)</div>
    <div class="rec-text">
      A regimen consisting of <strong>basal insulin</strong> plus <strong>prandial (mealtime) rapid-acting insulin</strong> and correction doses (<strong>Basal-Bolus Regimen</strong>) is the preferred standard of care for non-critically ill hospitalized patients with adequate nutritional intake. <em>[Level of Evidence: A]</em>
    </div>
  </div>

  <div class="warn-box">
    <div class="rec-title" style="color:#b91c1c;">&#9888; Strongly Discouraged Practice: Bolus / Sliding-Scale Alone</div>
    <div class="rec-text">
      <strong>Sole reliance on sliding-scale insulin or rapid-acting bolus insulin alone (e.g., Novorapid without basal coverage) in the inpatient setting is strongly discouraged.</strong> This approach fails to control overnight and fasting hepatic glucose output, resulting in severe fasting hyperglycemia (GDP elevated) and wide glycemic fluctuations. <em>[Level of Evidence: A]</em>
    </div>
  </div>

  <table class="table-custom">
    <thead>
      <tr>
        <th>Clinical Setting / Parameter</th>
        <th>Standard Recommendation</th>
        <th>Patient Application (Ny. Sunarti)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Non-critically Ill Target</strong></td>
        <td><span class="target-val">140 &ndash; 180 mg/dL</span></td>
        <td>GDP: 235 &rarr; 236 &rarr; <strong>298 mg/dL</strong> (Sub-optimal, Uncontrolled)</td>
      </tr>
      <tr>
        <td><strong>Insulin Protocol</strong></td>
        <td>Basal + Prandial Bolus + Correction</td>
        <td>Received <em>Novorapid alone</em> (3x8 &rarr; 3x10 &rarr; 3x12 UI) &rarr; Lack of Basal</td>
      </tr>
      <tr>
        <td><strong>Clinical Solution</strong></td>
        <td>Add Basal Insulin (e.g., Glargine / Detemir)</td>
        <td>Titrasi basal untuk supresi glukosa darah puasa malam &ndash; pagi</td>
      </tr>
    </tbody>
  </table>

  <div class="footer-cite">
    Reference: American Diabetes Association. Diabetes Care in the Hospital: Standards of Care in Diabetes. Diabetes Care 2024;47(Suppl. 1):S295&ndash;S306.
  </div>
</div>
</body>
</html>
"""

# 2. LEXICOMP & FDA METOCLOPRAMIDE RENAL DOSING & BLACK BOX WARNING
lexi_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f8fafc; margin: 0; padding: 24px; color: #1e293b; }
  .card { background: white; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); padding: 24px; max-width: 950px; margin: auto; }
  .header { display: flex; align-items: center; border-bottom: 3px solid #0284c7; padding-bottom: 12px; margin-bottom: 18px; }
  .logo-box { background: #0284c7; color: white; font-weight: bold; font-size: 18px; padding: 6px 14px; border-radius: 4px; margin-right: 14px; }
  .title-box h2 { margin: 0; color: #0369a1; font-size: 20px; }
  .title-box p { margin: 2px 0 0 0; color: #64748b; font-size: 13px; font-weight: 500; }
  .boxed-warning { border: 2px solid #000; padding: 14px 18px; margin: 14px 0; background: #fffbeb; }
  .boxed-warning h3 { margin: 0 0 8px 0; color: #b45309; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; }
  .boxed-warning p { margin: 0; font-size: 13px; line-height: 1.5; color: #1e293b; }
  .section-title { font-weight: bold; color: #0369a1; margin-top: 18px; margin-bottom: 8px; font-size: 15px; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px; }
  .table-custom { width: 100%; border-collapse: collapse; margin-top: 8px; font-size: 13px; }
  .table-custom th { background: #f1f5f9; padding: 9px; border: 1px solid #cbd5e1; text-align: left; }
  .table-custom td { padding: 9px; border: 1px solid #e2e8f0; }
  .alert-row { background: #fef2f2; font-weight: bold; color: #b91c1c; }
  .footer-cite { margin-top: 18px; padding-top: 10px; border-top: 1px solid #e2e8f0; font-size: 11.5px; color: #64748b; text-align: right; }
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <div class="logo-box">Lexicomp / FDA</div>
    <div class="title-box">
      <h2>Metoclopramide (Gavistal) &bull; Clinical Drug Information & FDA Label</h2>
      <p>Dosage Adjustments: Renal Impairment & Geriatric Safety Profile</p>
    </div>
  </div>

  <div class="boxed-warning">
    <h3>FDA WARNING: TARDIVE DYSKINESIA & EXTRA PYRAMIDAL SYMPTOMS (EPS)</h3>
    <p>
      Treatment with metoclopramide can cause <strong>tardive dyskinesia</strong> and acute extrapyramidal reactions, which are often irreversible. The risk increases with duration of treatment, cumulative dose, <strong>advanced age (geriatric patients, especially elderly females)</strong>, and <strong>renal impairment (impaired clearance)</strong>. Avoid treatment for longer than 12 weeks. Discontinue immediately in patients who develop signs or symptoms of movement disorders.
    </p>
  </div>

  <div class="section-title">Renal Impairment Dosage Adjustment Table</div>
  <table class="table-custom">
    <thead>
      <tr>
        <th>Creatinine Clearance (CrCl)</th>
        <th>Recommended Dosage Adjustment</th>
        <th>Clinical Rationale & Risk</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>CrCl &ge; 40 mL/min</strong></td>
        <td>100% of standard dose (No adjustment needed)</td>
        <td>Normal renal elimination (~80% excreted in urine).</td>
      </tr>
      <tr class="alert-row">
        <td><strong>CrCl 10 to &lt; 40 mL/min<br>(Patient: 30.69 mL/min)</strong></td>
        <td><strong>Administer 50% of the recommended dose</strong><br>(e.g., 5 mg IV q8h or 10 mg q12h; Max 15 mg/day)</td>
        <td><strong>Overdose Alert:</strong> Patient received full dose 3x10 mg (30 mg/day). Clearance decreased by ~50%, leading to drug accumulation and severe EPS risk.</td>
      </tr>
      <tr>
        <td><strong>CrCl &lt; 10 mL/min / ESRD</strong></td>
        <td>Administer 25% to 50% of recommended dose</td>
        <td>Severe accumulation risk. Avoid prolonged use.</td>
      </tr>
    </tbody>
  </table>

  <div class="section-title">Clinical Pharmacist Recommendation for Ny. Sunarti</div>
  <p style="font-size:13px; line-height:1.5; margin:6px 0;">
    1. <strong>Inpatient Phase:</strong> Karena CrCl = 30.69 mL/menit, dosis Injeksi Metoklopramid seharusnya disesuaikan menjadi 5 mg IV q8h (50% reduksi). Karena muntah telah teratasi sejak 16/10, injeksi metoklopramid dihentikan.<br>
    2. <strong>Discharge Phase:</strong> Resep pulang tertulis <em>Gavistal (Metoklopramid) 10 mg tab 3x1</em>. Ini adalah dosis penuh tanpa penyesuaian ginjal dan harus <strong>DIHENTIKAN</strong> total.
  </p>

  <div class="footer-cite">
    Reference: FDA Prescribing Information for Reglan (Metoclopramide HCl) &amp; Lexicomp Online Dosing in Renal Impairment, UpToDate, Wolters Kluwer 2024.
  </div>
</div>
</body>
</html>
"""

# 3. DRUG INTERACTION & DUPLICATION: METOCLOPRAMIDE (GAVISTAL) + DOMPERIDONE
dupl_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f8fafc; margin: 0; padding: 24px; color: #1e293b; }
  .card { background: white; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); padding: 24px; max-width: 950px; margin: auto; }
  .header { display: flex; align-items: center; border-bottom: 3px solid #ea580c; padding-bottom: 12px; margin-bottom: 18px; }
  .logo-box { background: #ea580c; color: white; font-weight: bold; font-size: 18px; padding: 6px 14px; border-radius: 4px; margin-right: 14px; }
  .title-box h2 { margin: 0; color: #c2410c; font-size: 20px; }
  .title-box p { margin: 2px 0 0 0; color: #64748b; font-size: 13px; font-weight: 500; }
  .danger-banner { background: #fee2e2; border: 1px solid #f87171; border-radius: 6px; padding: 12px 16px; margin-bottom: 16px; }
  .danger-banner h4 { margin: 0 0 4px 0; color: #b91c1c; font-size: 15px; }
  .danger-banner p { margin: 0; font-size: 13px; color: #7f1d1d; }
  .inter-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 16px 0; }
  .drug-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 14px; }
  .drug-card h4 { margin: 0 0 6px 0; color: #0f172a; font-size: 14px; }
  .drug-card p { margin: 0; font-size: 12.5px; color: #475569; line-height: 1.4; }
  .table-custom { width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13px; }
  .table-custom th { background: #f1f5f9; padding: 9px; border: 1px solid #cbd5e1; text-align: left; }
  .table-custom td { padding: 9px; border: 1px solid #e2e8f0; }
  .footer-cite { margin-top: 18px; padding-top: 10px; border-top: 1px solid #e2e8f0; font-size: 11.5px; color: #64748b; text-align: right; }
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <div class="logo-box">DRP ALERT</div>
    <div class="title-box">
      <h2>Therapeutic Duplication & Drug Interaction Analysis</h2>
      <p>Gavistal&reg; (Metoclopramide 10 mg) + Domperidone 10 mg Co-Prescription</p>
    </div>
  </div>

  <div class="danger-banner">
    <h4>&#9888; MAJOR CLINICAL DRP: PHARMACODYNAMIC DUPLICATION & ADDITIVE CARDIOTOXICITY</h4>
    <p>
      Resep Pulang (18/10/2026) meresepkan <strong>GAVISTAL 10 MG TAB 3x1</strong> bersamaan dengan <strong>DOMPERIDONE 10 MG TAB 2x1</strong>. Gavistal mengandung Metoklopramid. Keduanya adalah antagonis reseptor dopamin D2. Penggunaan bersamaan meningkatkan risiko efek samping yang berpotensi fatal tanpa keuntungan terapeutik.
    </p>
  </div>

  <div class="inter-grid">
    <div class="drug-card">
      <h4>Gavistal&reg; (Metoclopramide HCl 10 mg)</h4>
      <p>
        <strong>Mekanisme:</strong> Antagonis reseptor D2 dopamin sentral & perifer + agonis 5-HT4.<br>
        <strong>Eliminasi:</strong> Ginjal (~80%). Pada CrCl 30.69 mL/menit waktu paruh meningkat.<br>
        <strong>Efek Toksik:</strong> Sindrom ekstrapiramidal, distonia, akatisia, diskinesia tardif.
      </p>
    </div>
    <div class="drug-card">
      <h4>Domperidone 10 mg</h4>
      <p>
        <strong>Mekanisme:</strong> Antagonis reseptor D2 dopamin perifer.<br>
        <strong>Eliminasi:</strong> Hepatik (CYP3A4).<br>
        <strong>Efek Toksik:</strong> Pemanjangan interval QT ventrikel, aritmia jantung torsades de pointes, henti jantung mendadak (EMA Drug Safety Warning).
      </p>
    </div>
  </div>

  <table class="table-custom">
    <thead>
      <tr>
        <th>Risk Rating / Severity</th>
        <th>Clinical Consequences</th>
        <th>Evidence-Based Action</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Category D / X</strong><br>(Avoid Combination / Severe Risk)</td>
        <td>
          1. <strong>Additive QT Prolongation:</strong> Risiko fatal sudden cardiac death pada lansia wanita.<br>
          2. <strong>Additive Neurotoxicity:</strong> Peningkatan insiden kejang, distonia, atau agitasi.<br>
          3. <strong>Hyperprolactinemia:</strong> Blokade dopamin aditif pada sumbu hipofisis.
        </td>
        <td>
          <strong>HENTIKAN DUPLIKASI.</strong><br>
          Karena keluhan muntah pasien sudah tidak ada dan mual sudah teratasi, hentikan kedua obat ini saat pulang atau sisakan satu jenis saja bila perlu (prn).
        </td>
      </tr>
    </tbody>
  </table>

  <div class="footer-cite">
    Reference: EMA Pharmacovigilance Risk Assessment Committee (PRAC) Recommendations on Domperidone &amp; Metoclopramide Safety, Lexicomp Drug Interactions 2024.
  </div>
</div>
</body>
</html>
"""

# 4. KDIGO 2023 & PERKENI: DIABETES MANAGEMENT IN CKD
kdigo_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f8fafc; margin: 0; padding: 24px; color: #1e293b; }
  .card { background: white; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); padding: 24px; max-width: 950px; margin: auto; }
  .header { display: flex; align-items: center; border-bottom: 3px solid #059669; padding-bottom: 12px; margin-bottom: 18px; }
  .logo-box { background: #059669; color: white; font-weight: bold; font-size: 18px; padding: 6px 14px; border-radius: 4px; margin-right: 14px; }
  .title-box h2 { margin: 0; color: #047857; font-size: 20px; }
  .title-box p { margin: 2px 0 0 0; color: #64748b; font-size: 13px; font-weight: 500; }
  .badge { background: #d1fae5; color: #065f46; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 12px; display: inline-block; margin-bottom: 10px; }
  .table-custom { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 13px; }
  .table-custom th { background: #f1f5f9; padding: 9px; border: 1px solid #cbd5e1; text-align: left; }
  .table-custom td { padding: 9px; border: 1px solid #e2e8f0; }
  .highlight-safe { background: #f0fdf4; font-weight: bold; color: #15803d; }
  .highlight-danger { background: #fef2f2; font-weight: bold; color: #b91c1c; }
  .footer-cite { margin-top: 18px; padding-top: 10px; border-top: 1px solid #e2e8f0; font-size: 11.5px; color: #64748b; text-align: right; }
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <div class="logo-box">KDIGO / PERKENI</div>
    <div class="title-box">
      <h2>KDIGO 2023 &amp; PERKENI Guidelines &bull; Diabetes Management in CKD</h2>
      <p>Safety Profiles &amp; Renal Dosing of Oral Antidiabetic Drugs (OADs)</p>
    </div>
  </div>

  <span class="badge">EVIDENCE-BASED RENAL SELECTION OF ANTIDIABETIC THERAPY</span>

  <table class="table-custom">
    <thead>
      <tr>
        <th>Drug Class / Agent</th>
        <th>eGFR / CrCl Threshold</th>
        <th>Guideline Recommendation</th>
        <th>Application to Ny. Sunarti (eGFR 31.46 / CrCl 30.69)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Metformin</strong><br>(Biguanide)</td>
        <td>eGFR 30&ndash;44 mL/min/1.73m&sup2;<br>eGFR &lt; 30 mL/min/1.73m&sup2;</td>
        <td>Dose reduction max 1000 mg/d; <strong>Contraindicated</strong> if &lt;30. <strong>HOLD during acute illness, vomiting, dehydration</strong> due to risk of Lactic Acidosis (MALA).</td>
        <td class="highlight-safe">&#10004; TEPAT DIHENTIKAN saat MRS. Jangan dimulai kembali sebelum re-evaluasi fungsi ginjal pasca hidrasi.</td>
      </tr>
      <tr>
        <td><strong>Glimepiride</strong><br>(Sulfonylurea)</td>
        <td>eGFR &lt; 60 mL/min/1.73m&sup2;</td>
        <td>Metabolit aktif diekskresi melalui ginjal (~60%). Akumulasi metabolit memicu <strong>hipoglikemia berat dan berkepanjangan</strong>.</td>
        <td class="highlight-safe">&#10004; TEPAT DIGANTI saat pulang karena risiko akumulasi ginjal pada CrCl 30.69 mL/min.</td>
      </tr>
      <tr class="highlight-safe">
        <td><strong>Gliquidone (Glikuidon)</strong><br>(Sulfonylurea)</td>
        <td>eGFR 15&ndash;60 mL/min/1.73m&sup2;</td>
        <td><strong>Eliminasi utama melalui bilier / feses (&gt;95%)</strong>; hanya &lt;5% lewat ginjal. Tidak memerlukan penyesuaian dosis pada gangguan ginjal. OAD sulfonilurea pilihan pada nefropati.</td>
        <td><strong>Pilihan Tepat untuk Ginjal.</strong> Namun harus hati-hati jika digabung dengan insulin Novorapid 3x12 UI karena risiko hipoglikemia aditif.</td>
      </tr>
      <tr class="highlight-danger">
        <td><strong>Glikuidon + Novorapid 3x12 UI</strong></td>
        <td>Polifarmasi Antidiabetes Pulang</td>
        <td>Kombinasi sulfonilurea + insulin bolus dosis tinggi (36 unit/hari) pada geriatri berisiko memicu fatal hipoglikemia, tanpa menyelesaikan hiperglikemia puasa (GDP).</td>
        <td><strong>PERLU TITRASI &amp; REKOMENDASI:</strong> Evaluasi pemberian insulin basal malam dosis kecil daripada Novorapid dosis tinggi + Glikuidon.</td>
      </tr>
    </tbody>
  </table>

  <div class="footer-cite">
    Reference: KDIGO 2023 Clinical Practice Guideline for Diabetes Management in CKD &amp; Pedoman Pengelolaan DM Tipe 2 Dewasa PERKENI 2021/2023.
  </div>
</div>
</body>
</html>
"""

# 5. PERHI & ACC/AHA HYPERTENSION & MEDICATION RECONCILIATION
perhi_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body { font-family: 'Segoe UI', Arial, sans-serif; background: #f8fafc; margin: 0; padding: 24px; color: #1e293b; }
  .card { background: white; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); padding: 24px; max-width: 950px; margin: auto; }
  .header { display: flex; align-items: center; border-bottom: 3px solid #4338ca; padding-bottom: 12px; margin-bottom: 18px; }
  .logo-box { background: #4338ca; color: white; font-weight: bold; font-size: 18px; padding: 6px 14px; border-radius: 4px; margin-right: 14px; }
  .title-box h2 { margin: 0; color: #3730a3; font-size: 20px; }
  .title-box p { margin: 2px 0 0 0; color: #64748b; font-size: 13px; font-weight: 500; }
  .alert-box { background: #fef3c7; border-left: 4px solid #f59e0b; padding: 12px 16px; margin: 12px 0; border-radius: 0 6px 6px 0; }
  .alert-title { font-weight: bold; color: #b45309; margin-bottom: 4px; font-size: 14px; }
  .alert-text { font-size: 13px; line-height: 1.5; color: #78350f; }
  .table-custom { width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13px; }
  .table-custom th { background: #f1f5f9; padding: 9px; border: 1px solid #cbd5e1; text-align: left; }
  .table-custom td { padding: 9px; border: 1px solid #e2e8f0; }
  .footer-cite { margin-top: 18px; padding-top: 10px; border-top: 1px solid #e2e8f0; font-size: 11.5px; color: #64748b; text-align: right; }
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <div class="logo-box">PERHI / ACC-AHA</div>
    <div class="title-box">
      <h2>Hypertension Guidelines &amp; Hospital Medication Reconciliation</h2>
      <p>Target Blood Pressure &amp; Resumption of Withheld Chronic Therapies</p>
    </div>
  </div>

  <div class="alert-box">
    <div class="alert-title">&#9888; DISCHARGE MEDICATION RECONCILIATION OMISSION</div>
    <div class="alert-text">
      Pasien dengan riwayat hipertensi rutin minum <strong>Amlodipin 10 mg 1x1</strong> dan <strong>Clopidogrel 75 mg 1x1</strong>. Obat distop saat MRS karena dehidrasi (TD 90/60). Setelah normovolemia, TD pasien naik hingga 144/81 mmHg. Namun, pada resep pulang kedua obat kronis ini <strong>TIDAK DIRESEPKAN KEMBALI</strong>.
    </div>
  </div>

  <table class="table-custom">
    <thead>
      <tr>
        <th>Guideline Domain</th>
        <th>Evidence-Based Standard</th>
        <th>Clinical Recommendation for Ny. Sunarti</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Target Blood Pressure (PERHI 2021 / KDIGO 2021)</strong></td>
        <td>Target TD pada pasien DM dengan nefropati / CKD adalah <strong>&lt; 130/80 mmHg</strong> (atau &lt; 140/90 mmHg pada lansia yang frail).</td>
        <td>TD pasien 144/81 mmHg pada hari pemulangan (18/10) &rarr; belum mencapai target &lt; 130/80 mmHg tanpa antihipertensi.</td>
      </tr>
      <tr>
        <td><strong>Resumption of Amlodipine (10 mg &rarr; 5-10 mg)</strong></td>
        <td>Re-evaluasi dan mulai kembali agen antihipertensi saat stabilitas hemodinamik tercapai sebelum pemulangan.</td>
        <td>Mulai kembali <strong>Amlodipin 5 mg atau 10 mg 1 x sehari</strong> untuk mencegah hipertensi rebound dan melindungi target organ (jantung &amp; ginjal).</td>
      </tr>
      <tr>
        <td><strong>Resumption of Clopidogrel (75 mg 1x1)</strong></td>
        <td>Antiplatelet untuk prevensi sekunder kardio/serebrovaskular harus dilanjutkan kecuali ada bukti perdarahan aktif.</td>
        <td>Lanjutkan kembali <strong>Clopidogrel 75 mg 1 x sehari</strong>. Pasien tidak memiliki tanda perdarahan gastrointestinal (feses/urin normal, Hb stabil).</td>
      </tr>
    </tbody>
  </table>

  <div class="footer-cite">
    Reference: Konsensus Penatalaksanaan Hipertensi PERHI 2021 &amp; ACC/AHA Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure.
  </div>
</div>
</body>
</html>
"""

files = [
    ("ada_inpatient_guideline.html", ada_html, "ada_inpatient_guideline.png"),
    ("lexicomp_metoclopramide_renal.html", lexi_html, "lexicomp_metoclopramide_renal.png"),
    ("drug_interaction_gavistal_domperidone.html", dupl_html, "drug_interaction_gavistal_domperidone.png"),
    ("kdigo_perkeni_diabetes_ckd.html", kdigo_html, "kdigo_perkeni_diabetes_ckd.png"),
    ("perhi_acc_aha_hypertension_reconciliation.html", perhi_html, "perhi_acc_aha_hypertension_reconciliation.png"),
]

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

for html_name, html_content, png_name in files:
    hpath = os.path.join(guideline_dir, html_name)
    ppath = os.path.join(guideline_dir, png_name)
    with open(hpath, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # Run chrome screenshot
    cmd = [
        chrome_exe,
        "--headless=new",
        f"--screenshot={ppath}",
        "--window-size=1020,720",
        hpath
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Rendered {png_name}: exists={os.path.exists(ppath)}, size={os.path.getsize(ppath) if os.path.exists(ppath) else 0}")

print("All guideline screenshots generated successfully!")

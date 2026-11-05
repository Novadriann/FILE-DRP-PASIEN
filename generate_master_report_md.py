# -*- coding: utf-8 -*-
"""
Script to generate ANALISIS_KASUS_MENDALAM_RAJAL_DAN_RANAP.md
Full markdown report mirroring the comprehensive Word document.
"""

import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

md_content = """# LAPORAN LENGKAP & ANALISIS MENDALAM PEMANTAUAN TERAPI OBAT (PTO)
## Asuhan Kefarmasian Klinis Rawat Jalan (Rajal) & Rawat Inap (Ranap)
**Rumah Sakit PKU Muhammadiyah Bantul & Program Profesi Apoteker (PKPA) Universitas Ahmad Dahlan**
*Berdasarkan Konsensus PERKENI 2021, Konsensus PGI 2021/2024, DiPiro's Pharmacotherapy 12th Ed 2023, ADA Standards of Care 2024, & AGS Beers Criteria 2023*

---

> [!NOTE]
> **RINGKASAN EKSEKUTIF KASUS (EXECUTIVE SUMMARY)**
> Dokumen ini menyajikan analisis asuhan kefarmasian klinis (*Evidence-Based Clinical Pharmacy*) yang komprehensif dan mendalam untuk dua pasien kasus kompleks:
> 1. **Kasus Rawat Jalan (Poli Penyakit Dalam): Ny. Sri Wisraya (64 th, RM 00062584)** — Multi-morbiditas kronis (DM Tipe 2 Tak Terkontrol HbA1c 9,1%, Hipertensi Esensial, Dislipidemia Campuran, Osteoarthritis Genu Bilateral, Neuropati Perifer Diabetik, Vertigo Sentral, riwayat trauma CKR & fraktur os zygoma, riwayat peningkatan kreatinin akut 2,69 mg/dL / CrCl 18 mL/min). Evaluasi DRP mencakup: over-dosis Glimepirid 6 mg/hari pada geriatri (PIM Beers 2023), kegagalan triple OHO & indikasi insulin basal (PERKENI 2021 & DiPiro 2023), penyesuaian ginjal Sitagliptin, interaksi nefrotoksik NSAID oral (Meloxicam & Diklofenak) terhadap Amlodipin dan lonjakan tekanan darah, interaksi sedasi Gabapentin + Flunarizine (fall risk), evaluasi ADR edema Amlodipin (Naranjo skor 6) dan kombinasi ARB (Skovbjerg et al., 2023), serta kepatuhan MMAS-8 (skor 5,5).
> 2. **Kasus Rawat Inap (Bangsal Merak): Ny. Sunarti (62 th 10 bln, RM 00109480)** — Diagnosis Utama: **Mual dan Muntah karena Dispepsia (*Vomitus Profuse ec Dyspepsia*)** disertai krisis hiperglikemia akut DM Tipe 2 (GDS 357 mg/dL), riwayat hipertensi, serta dehidrasi dengan hiponatremia (Na 131 mmol/L) dan hipokloremia (Cl 96 mmol/L). Evaluasi DRP mencakup: duplikasi prokinetik D2 (Metoclopramide IV + Domperidone PO) berisiko gejala ekstrapiramidal dan aritmia QTc (Lexicomp Risk Rating D/X), penyesuaian ginjal Metoclopramide pada geriatri, tatalaksana dispepsia mual-muntah berbasis Konsensus PGI & DiPiro 12th Ed, tatalaksana hiperglikemia rawat inap (penghentian OHO Metformin & Glimepirid, inisiasi basal-bolus Novorapid + Lantus target 140–180 mg/dL sesuai PERKENI Hal. 98–101 & ADA 2024 Section 16), rekonsiliasi antihipertensi, rehidrasi kristaloid isotonik NaCl 0,9%, serta audit kualitatif antibiotik metode Gyssens (Kategori 0 / Tepat tanpa antibiotik pada riwayat alergi penisilin).

---

# BAGIAN I: ANALISIS MENDALAM KASUS RAWAT JALAN (RAJAL) — NY. SRI WISRAYA

## 1.1 Profil Demografi & Data Dasar Pasien
| Parameter Klinis | Nilai / Keterangan Pasien | Interpretasi Klinis Farmasis |
| :--- | :--- | :--- |
| **Nama Pasien** | Ny. Sri Wisraya | Pasien geriatri rawat jalan reguler Poli Penyakit Dalam |
| **Nomor Rekam Medis** | 00062584 | Terdaftar aktif di RS PKU Muhammadiyah Bantul |
| **Usia / Tanggal Lahir** | 64 tahun 1 bulan | Populasi geriatri rentan terhadap interaksi obat dan PIM Beers Criteria |
| **Jenis Kelamin** | Perempuan | Faktor risiko osteopenia, osteoarthritis pasca menopause |
| **Berat Badan / Tinggi Badan** | 52 – 54 kg / 156 cm | IMT: 21,4 – 21,8 kg/m² (Normoweight / status gizi baik) |
| **Klinik / Dokter DPJP** | Poli Penyakit Dalam / dr. Tri Hariningsih, Sp.PD | Konsul: Poli Orthopedi, Poli Saraf, Poli Mata |
| **Diagnosis Medis Utama** | 1. DM Tipe 2 Tak Terkontrol (HbA1c 9,1%)<br>2. Hipertensi Esensial Stage 1-2<br>3. Dislipidemia Campuran<br>4. Osteoarthritis (OA) Genu Bilateral<br>5. Neuropati Perifer Diabetik<br>6. Vertigo Sentral / Perifer<br>7. Riwayat Trauma CKR & Fraktur Os Zygoma Sinistra (04/07/2026)<br>8. Riwayat Peningkatan Kreatinin Akut (2,69 mg/dL / CrCl 18 mL/min) | Pasien memiliki kompleksitas multi-morbiditas kronis dengan polifarmasi aktif (7–9 obat per hari) yang memerlukan pemantauan ketat terhadap nefrotoksisitas, risiko jatuh, dan kepatuhan. |

---

## 1.2 Riwayat Kunjungan Kontrol & Dinamika Klinis 6 Bulan Terakhir
| Tanggal | Poli / DPJP | Keluhan Pasien | Tindakan Medis & Dinamika Terapi Obat |
| :--- | :--- | :--- | :--- |
| **18/02/2026** | Penyakit Dalam | Kontrol rutin DM & HT, kesemutan kedua telapak kaki | Glimepirid 2 mg 1x1, Metformin 500 mg 3x1, Amlodipin 10 mg 1x1, Candesartan 8 mg 1x1, Mecobalamin 500 mcg 2x1, Flamar Gel topikal |
| **18/03/2026** | Penyakit Dalam | GDP belum turun (151 mg/dL), pusing, nyeri lutut memberat | Glimepirid dinaikkan 3 mg 1x1 pagi, Metformin 500 mg 3x1, Amlodipin 10 mg 1x1, Rosuvastatin 20 mg 1x1 malam, Gabapentin 100 mg 1x1 malam |
| **15/04/2026** | Penyakit Dalam & Ortho | Gula puasa tinggi (GDP 168, GD2PP 245), linu sendi lutut hebat | Glimepirid dinaikkan 3 mg 2x1 (6 mg/hari!), Sitagliptin 100 mg 1x1 ditambahkan, Meloxicam 7,5 mg 1x1 prn |
| **13/05/2026** | Penyakit Dalam & Ortho | Bengkak kedua pergelangan kaki (edema tungkai), lutut kaku pagi | Glimepirid 3 mg 2x1, Sitagliptin 100 mg 1x1, Acarbose 100 mg 2x1 ditambahkan, Kalium Diklofenak 50 mg 2x1, Glukosamin 500 mg 1x1 |
| **10/06/2026** | Penyakit Dalam | Hasil HbA1c 9,1% (uncontrolled), pusing berputar (vertigo) | Candesartan dinaikkan 16 mg 1x1, Statin diswitch ke Atorvastatin 20 mg 1x1, Gabapentin dinaikkan 100 mg 2x1, Flunarizine 5 mg 1x1 malam |
| **08/07/2026** | Bedah & Saraf | Pasien jatuh di kamar mandi (04/07/2026), CKR + fraktur os zygoma | Rawat luka wajah, Cefixime 100 mg 2x1, Asam Mefenamat 500 mg 3x1, Flunarizine 5 mg 1x1, edukasi tirah baring |
| **05/08/2026** | Penyakit Dalam | Badan sangat lemas, TD melonjak 165/89 mmHg, GDP 190 mg/dL, kreatinin 2,69 mg/dL | Evaluasi lonjakan tekanan darah dan azotemia akut pasca trauma/NSAID, restrukturisasi terapi OHO dan antihipertensi |

---

## 1.3 Pemantauan Tanda-Tanda Vital (TTV) 6 Bulan
Dinamika tanda-tanda vital menunjukkan fluktuasi tajam pada tekanan darah. Pada periode Februari hingga Juni 2026, tekanan darah berada dalam batas 130–145 / 80–88 mmHg dengan terapi kombinasi Amlodipin 10 mg dan Candesartan. Namun, pada kunjungan 05/08/2026 terjadi lonjakan tekanan darah mendadak (*blood pressure spike*) hingga **165/89 mmHg**. Lonjakan ini berkorelasi kuat dengan konsumsi NSAID oral ganda pasca trauma fraktur yang merusak mekanisme otoregulasi vaskular ginjal dan menumpulkan efek antihipertensi Amlodipin.

| Tanggal | Tekanan Darah (mmHg) | Nadi (x/m) | RR (x/m) | Suhu (°C) | Status Klinis & Interpretasi |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **18/02/2026** | 130/80 | 84 | 20 | 36,5 | Prehipertensi / Terkontrol baik |
| **18/03/2026** | 140/85 | 80 | 18 | 36,6 | Hipertensi Stage 1 |
| **15/04/2026** | 138/82 | 78 | 20 | 36,4 | Terkontrol borderline |
| **13/05/2026** | 145/88 | 82 | 18 | 36,5 | Hipertensi Stage 1 |
| **10/06/2026** | 135/80 | 80 | 20 | 36,5 | Terkontrol baik pasca titrasi Candesartan 16 mg |
| **05/08/2026** | 165/89 | 86 | 20 | 36,7 | Hipertensi Stage 2 (Spike pasca NSAID oral & nyeri trauma) |

![Tren Tekanan Darah Rajal](guideline_evidence_rajal/rajal_bp_trend.png)
*Gambar 1.1: Grafik Tren Tekanan Darah Ny. Sri Wisraya Selama 6 Bulan Terakhir (Konsensus PERHI 2021 Hal. 18–22).*

---

## 1.4 Pemantauan Data Laboratorium 6 Bulan
Pemeriksaan laboratorium membuktikan kondisi dekompensasi glikemik kronis berat:
* **HbA1c = 9,1%**: Menunjukkan rata-rata glukosa darah 3 bulan terakhir sangat tinggi (> 215 mg/dL), jauh melampaui target PERKENI/ADA untuk geriatri (< 7,5% – 8,0%).
* **GDP & GD2PP**: GDP meningkat progresif dari 151 mg/dL hingga 190 mg/dL, dan GD2PP mencapai 245 mg/dL meskipun pasien telah mengonsumsi 3 jenis OHO oral.
* **Fungsi Ginjal**: Serum kreatinin melonjak tajam menjadi **2,69 mg/dL** pada 05/08/2026 dengan Ureum 58 mg/dL. Perhitungan Cockcroft-Gault:
  $$CrCl = \frac{(140 - 64) \times 54}{72 \times 2,69} \times 0,85 = \frac{4104}{193,68} \times 0,85 = 18,01 \text{ mL/min}$$
  Mengindikasikan penurunan klirens ginjal berat (Acute Kidney Injury superimposed on CKD Stage 4).

| Parameter Uji Lab | Nilai Pasien | Nilai Rujukan Normal | Satuan | Interpretasi Klinis Farmasis |
| :--- | :---: | :---: | :---: | :--- |
| **HbA1c** | **9,1** | < 6,5 (Target lansia < 7,5 - 8,0) | % | Sangat tinggi; bukti objektif kegagalan terapi OHO oral |
| **GDP (18/03/2026)** | 151 | 70 – 100 | mg/dL | Hiperglikemia puasa belum terkontrol |
| **GDP (15/04/2026)** | 168 | 70 – 100 | mg/dL | Meningkat progresif; respon sulfonilurea suboptimal |
| **GD2PP (15/04/2026)** | 245 | < 140 | mg/dL | Lonjakan glukosa postprandial masif |
| **GDP (13/05/2026)** | 175 | 70 – 100 | mg/dL | Hiperglikemia persisten |
| **GDP (05/08/2026)** | 190 | 70 – 100 | mg/dL | Puncak kenaikan GDP pasca trauma fisik dan nyeri |
| **Kreatinin Serum** | **2,69** | 0,6 – 1,1 | mg/dL | Azotemia akut berat (CrCl terhitung 18,01 mL/min) |
| **Ureum Darah** | 58 | 15 – 45 | mg/dL | Azotemia ringan ec penurunan klirens ginjal |
| **Hemoglobin (Hb)** | 12,4 | 12,0 – 15,0 | g/dL | Normal; tidak tampak anemia renal nyata |
| **Leukosit** | 7.400 | 4.000 – 10.000 | /µL | Normal; menyingkirkan infeksi bakterial akut |
| **SGOT / SGPT** | 22 / 26 | < 31 / < 32 | U/L | Fungsi integritas hepatoseluler dalam batas normal |

![Tren Glukosa Rajal](guideline_evidence_rajal/rajal_glucose_trend.png)
*Gambar 1.2: Grafik Tren Glukosa Darah Puasa (GDP) dan GD2PP Ny. Sri Wisraya Selama 6 Bulan Terakhir (PERKENI 2021 Hal. 45–50).*

---

## 1.5 Riwayat Radiologi & Insiden Trauma Jatuh
1. **Foto Konvensional Pelvis AP (04/07/2026)**: Menunjukkan kalsifikasi vaskular pelvis dan osteofit minimal pada sendi koksa bilateral. Tidak tampak garis fraktur pelvis aktif.
2. **CT-Scan Kepala Non-Kontras (04/07/2026)**: Cedera Kepala Ringan (CKR) disertai garis diskontinuitas korteks tulang linier pada os zygomaticum sinistra dan lamina papirasea os frontalis sinistra (*non-displaced linear fracture*). Tidak ditemukan perdarahan epidural (EDH) maupun subdural (SDH).
3. **Analisis Farmakologis Terhadap Insiden Jatuh**: Pasien jatuh di kamar mandi akibat interaksi multifaktorial: (1) Hipoglikemia transien akibat dosis tinggi Glimepirid 6 mg/hari; (2) Efek sedasi sentral dan ataksia aditif dari interaksi Gabapentin 100 mg + Flunarizine 5 mg; (3) Defisit proprioseptif akibat neuropati diabetik; serta (4) Ketidakstabilan gaya berjalan akibat osteoarthritis genu bilateral.

---

## 1.6 Profil Terapi Pengobatan Kronis 6 Bulan
| Nama Obat | Dosis & Frekuensi | Rute | Indikasi Medis | Kategori Farmakologi |
| :--- | :--- | :---: | :--- | :--- |
| **Glimepirid** | 3 mg 2x1 tab (6 mg/hari) | Oral (ac) | DM Tipe 2 | Sulfonilurea Generasi 2 (Sekretagok) |
| **Sitagliptin (Januvia)** | 100 mg 1x1 tab | Oral (dc) | DM Tipe 2 | Dipeptidyl Peptidase-4 (DPP-4) Inhibitor |
| **Acarbose** | 100 mg 2x1 tab | Oral (dc suapan 1) | DM Tipe 2 Postprandial | Alpha-Glucosidase Inhibitor |
| **Amlodipin** | 10 mg 1x1 tab | Oral (malam) | Hipertensi Esensial | Dihydropyridine Calcium Channel Blocker |
| **Candesartan** | 16 mg 1x1 tab | Oral (pagi) | Hipertensi & Nefroproteksi | Angiotensin Receptor Blocker (ARB) |
| **Atorvastatin** | 20 mg 1x1 tab | Oral (malam) | Dislipidemia Campuran | HMG-CoA Reductase Inhibitor |
| **Gabapentin** | 100 mg 2x1 kapsul | Oral (malam) | Neuropati Diabetik | Antikonvulsan / Modulator Kanal Ca |
| **Flunarizine** | 5 mg 1x1 tab | Oral (malam) | Profilaksis Vertigo | Antagonis Kalsium Serebral |
| **Glukosamin** | 500 mg 1x1 tab | Oral (pc) | Osteoarthritis Genu | Kondroprotektor Kartilago Sendi |
| **Flamar Gel** | 3-4 kali sehari oles | Topikal | Nyeri Sendi Lutut Akut | NSAID Topikal (Diklofenak 1%) |

---

## 1.7 Evaluasi Kepatuhan Pasien: Kuesioner MMAS-8 (Morisky Scale)
Wawancara terstruktur menggunakan instrumen Morisky Medication Adherence Scale 8-Item (MMAS-8) menghasilkan skor total **5,5 / 8,0** yang mengindikasikan **Tingkat Kepatuhan Sedang (Medium Adherence)**.

| No | Butir Pertanyaan Kuesioner MMAS-8 | Jawaban Pasien | Skor | Analisis Rasionalitas & Perilaku Pasien |
| :-: | :--- | :---: | :---: | :--- |
| 1 | Apakah Anda kadang-kadang lupa minum obat? | Ya | 0 | Pasien lupa akibat beban tablet terlalu banyak (polifarmasi 7–9 tab/hari) |
| 2 | Dalam 2 minggu terakhir, apakah ada hari Anda tidak minum obat? | Ya | 0 | Kadang terlewat saat bepergian atau sibuk mengurus rumah tangga |
| 3 | Apakah Anda pernah mengurangi atau berhenti minum obat tanpa memberi tahu dokter saat merasa kondisi memburuk? | Ya | 0 | Pasien sengaja menghentikan Amlodipin sendiri saat kedua pergelangan kaki bengkak |
| 4 | Ketika bepergian keluar rumah, apakah Anda kadang lupa membawa obat? | Tidak | 1 | Pasien selalu berusaha membawa obat saat bepergian jauh |
| 5 | Apakah Anda meminum semua obat Anda kemarin? | Ya | 1 | Kemarin seluruh obat diminum sesuai aturan |
| 6 | Ketika Anda merasa gejala membaik atau sehat, apakah Anda kadang berhenti minum obat? | Tidak | 1 | Pasien memahami obat DM dan hipertensi adalah obat rutin jangka panjang |
| 7 | Apakah Anda merasa tertekan atau terbebani dengan rencana pengobatan rutin setiap hari? | Ya | 0 | Pasien merasa stres dengan banyaknya variasi waktu minum obat (ac, dc, pc, malam) |
| 8 | Seberapa sering Anda merasa kesulitan mengingat untuk meminum semua obat Anda? | Kadang-kadang | 0,5 | Skala Likert 5 poin: Kadang-kadang mendapat skor 0,5 poin |

> [!TIP]
> **INTERVENSI FARMASIS UNTUK MENINGKATKAN KEPATUHAN**
> 1. **Pill Box Dispenser 4 Waktu**: Menyediakan kotak obat harian terbagi 4 kompartemen (Pagi, Siang, Sore, Malam) untuk mengeliminasi beban kognitif mengingat obat.
> 2. **Visual Medication Chart**: Membuat tabel jadwal obat visual berwarna dengan gambar bentuk fisik obat dan waktu minum terkait makanan.
> 3. **Edukasi Manajemen Efek Samping**: Menjelaskan kepada pasien bahwa efek bengkak kaki Amlodipin dapat diatasi melalui kombinasi dengan Candesartan dan penurunan dosis, sehingga pasien tidak menghentikan obat antihipertensi secara sepihak.

![Kuesioner MMAS-8](guideline_evidence_rajal/mmas8_patient_adherence_morisky.png)
*Gambar 1.3: Instrumen Kuesioner Morisky Medication Adherence Scale (MMAS-8) dan Algoritma Penilaian Kepatuhan (Morisky et al., 2008).*

---

## 1.8 Identifikasi & Analisis Mendalam Drug-Related Problems (DRP) Rawat Jalan

### DRP 1: Penggunaan Glimepirid Dosis Tinggi (6 mg/hari) pada Geriatri & Penurunan Fungsi Ginjal
* **Analisis Klinis**: Pasien berusia 64 tahun menerima Glimepirid 3 mg 2x1 (6 mg/hari). Glimepirid merupakan sulfonilurea kerja panjang (durasi aksi hingga 24 jam) yang dieliminasi 60% melalui ginjal. Pada penurunan klirens ginjal (CrCl 18,01 mL/min), terjadi akumulasi obat dan metabolit aktifnya, memicu risiko hipoglikemia berat memanjang (*prolonged neuroglycopenia*) yang memicu episode jatuh dan fraktur.
* **Guideline Klinis**: 
  1. *AGS Beers Criteria 2023 Update*: Sulfonilurea kerja panjang (Glimepirid, Glibenklamid) diklasifikasikan sebagai **Potentially Inappropriate Medications (PIM) kategori AVOID** pada geriatri karena risiko tinggi hipoglikemia mematikan.
  2. *PERKENI 2021 (Hal. 36–39)*: Pada geriatri dan insufisiensi ginjal, dosis sulfonilurea harus dibatasi serendah mungkin (Glimepirid ≤ 2 mg/hari). Jika CrCl < 30 mL/min, beralih ke Glikuidon (30 mg 1–2x/hari) yang 95% diekskresi via empedu/feses, atau beralih ke insulin.
* **Rekomendasi Farmasis**: Turunkan dosis Glimepirid menjadi 2 mg 1x1 pagi, atau beralih ke Glikuidon 30 mg 1x1, serta lakukan inisiasi insulin basal.

![Glimepirid Geriatri Beers](guideline_evidence_rajal/perkeni_beers_glimepiride_elderly.png)
*Gambar 1.4: Panduan Keamanan Sulfonilurea pada Geriatri Sesuai AGS Beers Criteria 2023 & Konsensus PERKENI 2021 (Hal. 38).*

---

### DRP 2: Kegagalan Regimen Triple OHO (HbA1c 9,1%) & Indikasi Inisiasi Terapi Insulin Basal
* **Analisis Klinis**: Kombinasi 3 OHO (Glimepirid 6 mg + Sitagliptin 100 mg + Acarbose 200 mg) gagal mengontrol glikemik pasien (HbA1c tetap 9,1% dan GDP melonjak hingga 190 mg/dL). Hal ini membuktikan adanya deplesi progresif sel beta pankreas yang tidak lagi mampu merespon stimulasi sekretagok oral.
* **Guideline Klinis**:
  1. *PERKENI 2021 (Hal. 45–50)*: Pasien dengan HbA1c > 9% atau pasien yang belum mencapai target dengan kombinasi 2–3 OHO memiliki **INDIKASI MUTLAK** untuk inisiasi terapi **INSULIN BASAL**.
  2. *DiPiro's Pharmacotherapy 12th Edition (2023) Chapter 57*: Inisiasi insulin basal analog (Insulin Glargine / Degludec) dengan dosis 10 Unit per hari atau 0,1–0,2 U/kgBB/hari pada malam hari, dititrasi 2 unit tiap 3 hari hingga mencapai target GDP 80–130 mg/dL.
* **Rekomendasi Farmasis**: Inisiasi Insulin Glargine (Lantus) subkutan 1x10 Unit malam hari (pukul 21.00–22.00).

![Algoritma DM PERKENI](guideline_evidence_rajal/perkeni_2021_dm_algorithm.png)
*Gambar 1.5: Algoritma Pengelolaan Glukosa DM Tipe 2 & Indikasi Inisiasi Insulin Basal (PERKENI 2021 Hal. 47–49).*

---

### DRP 3: Kebutuhan Penyesuaian Dosis Ginjal Sitagliptin pada Penurunan Klirens Ginjal
* **Analisis Klinis**: Sitagliptin (Januvia) diekskresi 79% dalam bentuk utuh melalui urin. Pada klirens ginjal pasien yang menurun drastis menjadi 18,01 mL/min (kreatinin 2,69 mg/dL), dosis penuh 100 mg 1x1 menyebabkan peningkatan area under curve (AUC) obat sebesar 4–5 kali lipat, memicu risiko hepatotoksisitas dan pankreatitis.
* **Guideline Klinis (Lexicomp & FDA Package Insert)**:
  * CrCl ≥ 45 mL/min: Dosis 100 mg 1x1 sehari.
  * CrCl 30 hingga < 45 mL/min: Dosis diturunkan menjadi 50 mg 1x1 sehari.
  * CrCl < 30 mL/min: Dosis **HARUS DITURUNKAN menjadi 25 mg 1x1 sehari**.
* **Rekomendasi Farmasis**: Turunkan segera dosis Sitagliptin dari 100 mg menjadi 25 mg sekali sehari.

![Penyesuaian Ginjal Sitagliptin](guideline_evidence_rajal/sitagliptin_renal_adjustment_lexicomp.png)
*Gambar 1.6: Panduan Penyesuaian Dosis Ginjal Sitagliptin Berdasarkan Klirens Kreatinin (Lexicomp Drug Information 2024).*

---

### DRP 4: Interaksi Obat NSAID Oral (Meloxicam & Kalium Diklofenak) terhadap Ginjal, Tekanan Darah, & Amlodipin
* **Analisis Klinis**: Pemberian NSAID oral sistemik berulang (Meloxicam 7,5 mg, Kalium Diklofenak 50 mg 2x1, dan Asam Mefenamat 500 mg 3x1) menghambat sintesis prostaglandin renal (PGE2 & PGI2). Hambatan ini menyebabkan vasokonstriksi arteriol aferen glomerulus, memicu Acute Kidney Injury (lonjakan kreatinin 2,69 mg/dL), retensi natrium-air yang memicu spike tekanan darah (165/89 mmHg), serta menumpulkan efek vasodilatasi Amlodipin dan Candesartan (Lexicomp Rating C).
* **Guideline Klinis**: *Indonesian Rheumatology Association (IRA 2021)* & *DiPiro 12th Ed Ch. 60*: Pada lansia dengan komorbid hipertensi, DM, dan gangguan ginjal, **NSAID oral sistemik HARUS DIHINDARI**. Terapi lini pertama adalah NSAID topikal (Flamar Gel / Diklofenak gel) dikombinasikan dengan Parasetamol oral prn dan Glukosamin 500 mg.
* **Rekomendasi Farmasis**: Hentikan seluruh NSAID oral. Maksimalkan Flamar Gel topikal 3–4 kali sehari pada lutut dan Parasetamol 500 mg oral prn bila nyeri hebat.

![Keamanan NSAID IRA](guideline_evidence_rajal/ira_nsaid_safety_osteoarthritis.png)
*Gambar 1.7: Rekomendasi Keamanan Penggunaan NSAID pada Pasien Lansia dengan Komorbid Kardio-Renal (IRA 2021 Hal. 14–19).*

![Matriks Interaksi Rajal](guideline_evidence_rajal/lexicomp_interactions_rajal.png)
*Gambar 1.8: Matriks Interaksi Obat Pasien Rawat Jalan Berdasarkan Lexicomp Drug Interactions Rating C & D.*

---

### DRP 5: Interaksi Farmakodinamik Gabapentin + Flunarizine (Depresi SSP & Fall Risk Paska Fraktur Zygoma)
* **Analisis Klinis**: Kombinasi Gabapentin 100 mg 2x1 dan Flunarizine 5 mg 1x1 malam menimbulkan depresi SSP aditif, memicu pusing berat, ataksia motorik, dan gangguan keseimbangan postural. Efek sedasi ini berkontribusi langsung pada insiden jatuh pasien di kamar mandi pada 04/07/2026 yang mengakibatkan CKR dan fraktur os zygoma sinistra.
* **Guideline Klinis**: *AGS Beers Criteria 2023 Update* & *Lexicomp*: Kombinasi multipel depresan SSP pada lansia harus dihindari. Flunarizine memiliki waktu paruh sangat panjang (hingga 18 hari pada geriatri) dan harus dibatasi maksimal 7–10 hari pada fase akut vertigo. Gabapentin harus disesuaikan dengan klirens ginjal (100 mg 1x1 malam).
* **Rekomendasi Farmasis**: Hentikan Flunarizine 5 mg (vertigo fase akut telah teratasi). Pertahankan Gabapentin 100 mg 1x1 malam untuk neuropati diabetik.

![Neuropati DiPiro](guideline_evidence/dipiro_diabetic_neuropathy_weight.png)
*Gambar 1.9: Tatalaksana Neuropati Diabetik & Penyesuaian Dosis Gabapentin pada Geriatri (DiPiro 12th Ed Ch. 57 & 58).*

---

### DRP 6: Drug-Food Interaction & Edukasi Khusus Acarbose 100 mg
* **Analisis Klinis**: Acarbose bekerja menghambat enzim alfa-glukosidase di mukosa usus halus. Acarbose **hanya efektif jika diminum bersama suapan pertama makanan utama**. Pasien sering meminumnya sebelum makan jauh atau setelah makan. Selain itu, jika terjadi hipoglikemia akibat kombinasi Glimepirid + Acarbose, gula pasir biasa (sukrosa) tidak akan efektif diserap. Pasien wajib diedukasi untuk mengonsumsi **dekstrosa murni / madu murni** untuk penanganan darurat hipoglikemia.

---

### DRP 7: Evaluasi Adverse Drug Reaction (ADR): Edema Perifer Amlodipin, Algoritma Naranjo (Skor 6 - Probable), dan Strategi Terapi Kombinasi ARB
* **Analisis Klinis**: Pasien mengalami pembengkakan kedua pergelangan kaki (*bilateral peripheral ankle edema*) setelah pemakaian Amlodipin 10 mg selama 2 bulan. Amlodipin mendilatasi arteriol prekapiler secara selektif tanpa mendilatasi venul postkapiler, memicu ekstravasasi transudat plasma ke jaringan interstisial pergelangan kaki.
* **Skoring Algoritma Naranjo**:
  * Efek samping dilaporkan sebelumnya (+1)
  * Terjadi pasca pemberian Amlodipin (+2)
  * Membaik saat Amlodipin dihentikan (+1)
  * Muncul kembali saat obat diminum ulang (+2)
  * Tidak ada penyebab alternatif lain (0)
  * Konfirmasi bukti objektif (+1)
  * **TOTAL SKOR NARANJO = +6 (PROBABLE ADVERSE DRUG REACTION)**.
* **Tatalaksana Berbasis Literatur (Skovbjerg et al., 2023; Shetty et al., 2016; Tolla et al., 2026)**:
  1. Turunkan dosis Amlodipin dari 10 mg menjadi 5 mg sekali sehari (menurunkan kejadian edema dari 10,7% menjadi 2,8%).
  2. Pindahkan waktu minum ke malam hari sebelum tidur (*bedtime dosing*).
  3. Kombinasikan secara sinergis dengan ARB (Candesartan 16 mg 1x1). Candesartan mendilatasi venul postkapiler, menormalkan gradien tekanan hidrostatik kapiler, dan melenyapkan edema tanpa memerlukan diuretik loop.

![Naranjo Amlodipin](guideline_evidence/naranjo_amlodipine_edema.png)
*Gambar 1.10: Penilaian Algoritma Naranjo Adverse Drug Reaction: Edema Perifer Terinduksi Amlodipin (Skor 6 - Probable).*

![Skovbjerg Edema Mgmt](guideline_evidence/skovbjerg_amlodipine_edema_mgmt.png)
*Gambar 1.11: Mekanisme Patofisiologi & Strategi Terapi Edema Perifer Amlodipin Berbasis Bukti Klinis (Skovbjerg et al., 2023).*

---

### DRP 8: Evaluasi Kepatuhan Formularium Nasional (Fornas) & Rasionalitas Switch Statin
* **Analisis Regulasi & Farmakokinetik**: Switch dari Rosuvastatin 20 mg ke Atorvastatin 20 mg pada 10/06/2026 sangat rasional. Berdasarkan Kepmenkes RI HK.01.07/MENKES/6485/2021 (Fornas), Rosuvastatin memiliki restriksi restriktif untuk FKRTL. Dari aspek eliminasi obat, Atorvastatin dieliminasi > 98% melalui jalur hepatobilier/empedu (ekskresi ginjal < 2%), sehingga jauh lebih aman pada pasien yang mengalami fluktuasi fungsi ginjal (CrCl 18 mL/min) dibandingkan Rosuvastatin yang memiliki klirens ginjal 10%.

![Dislipidemia PERKI](guideline_evidence_rajal/perhi_perki_hypertension_dyslipidemia.png)
*Gambar 1.12: Panduan Terapi Dislipidemia & Evaluasi Statin pada Pasien Risiko Tinggi (PERKI 2022 Hal. 25–30).*

---

## 1.9 Dokumentasi Asuhan Kefarmasian (SOAP) Rawat Jalan Lengkap
| Problem Medis | Subjektif (S) & Objektif (O) | Asesmen Farmasis (A) | Rencana Asuhan & Intervensi Farmasis (P) |
| :--- | :--- | :--- | :--- |
| **DM Tipe 2 Tak Terkontrol** | **S**: Kesemutan telapak kaki, badan lemas, lapar malam hari.<br>**O**: HbA1c 9,1%, GDP 190 mg/dL, GD2PP 245 mg/dL. Terapi: Glimepirid 6 mg, Sitagliptin 100 mg, Acarbose 200 mg. | Kegagalan terapi 3 OHO oral. Glimepirid 6 mg over-dosis geriatri (PIM Beers). Sitagliptin belum disesuaikan ginjal. Indikasi mutlak inisiasi insulin basal (PERKENI 2021). | 1. Inisiasi Insulin Glargine (Lantus) SC 1x10 Unit malam.<br>2. Turunkan Glimepirid ke 2 mg 1x1 pagi atau ganti Glikuidon 30 mg 1x1.<br>3. Turunkan Sitagliptin ke 25 mg 1x1.<br>4. Acarbose 100 mg dc suapan pertama.<br>5. Target GDP 80–130 mg/dL. |
| **Hipertensi & Edema Amlodipin** | **S**: Bengkak kedua pergelangan kaki, pusing melayang.<br>**O**: TD 165/89 mmHg (spike). Terapi: Amlodipin 10 mg, Candesartan 16 mg. | Edema perifer terinduksi Amlodipin (Naranjo 6 - Probable). Lonjakan TD dipicu interaksi NSAID oral pasca trauma. | 1. Turunkan Amlodipin ke 5 mg 1x1 malam.<br>2. Lanjutkan Candesartan 16 mg 1x1 pagi (venodilator pelenyap edema).<br>3. Hentikan NSAID oral sistemik.<br>4. Target TD < 140/90 mmHg. |
| **Osteoarthritis & Penurunan Klirens Ginjal** | **S**: Nyeri dan kaku kedua lutut (VAS 6).<br>**O**: Kreatinin melonjak 2,69 mg/dL (CrCl 18 mL/min), Ureum 58 mg/dL. Terapi: Kalium Diklofenak 50 mg 2x1, Meloxicam. | Acute Kidney Injury superimposed on CKD terinduksi NSAID oral sistemik. PIM Beers Criteria. | 1. Hentikan total NSAID oral sistemik.<br>2. Berikan Flamar Gel topikal 3–4x/hari oles lutut.<br>3. Parasetamol 500 mg oral prn bila nyeri hebat.<br>4. Glukosamin 500 mg 1x1 oral.<br>5. Rehidrasi cairan dan re-evaluasi lab 2 minggu. |
| **Neuropati & Vertigo / Fall Risk** | **S**: Kesemutan kaki, pusing berputar, riwayat jatuh di kamar mandi.<br>**O**: Pasca CKR + fraktur os zygoma sinistra. Terapi: Gabapentin 100 mg 2x1, Flunarizine 5 mg 1x1. | Interaksi farmakodinamik aditif depresi SSP antara Gabapentin dan Flunarizine memicu ataksia dan jatuh. | 1. Hentikan Flunarizine (vertigo fase akut telah teratasi).<br>2. Gabapentin disesuaikan ginjal 100 mg 1x1 malam.<br>3. Edukasi protokol pencegahan jatuh di rumah. |
| **Kepatuhan Pasien** | **S**: Bingung jadwal minum banyak obat, sengaja stop Amlodipin saat bengkak.<br>**O**: Skor MMAS-8 = 5,5 (Kepatuhan Sedang). | Polifarmasi (7–9 tablet) dan pemahaman cara minum obat kurang. | 1. Berikan Pill Box Organizer 4 kompartemen.<br>2. Berikan jadwal obat visual berbasis warna.<br>3. Edukasi keluarga untuk mendampingi kepatuhan. |

---

# BAGIAN II: ANALISIS MENDALAM KASUS RAWAT INAP (RANAP) — NY. SUNARTI

## 2.1 Profil Demografi & Data Dasar Pasien Rawat Inap
| Parameter Klinis | Nilai / Keterangan Pasien | Interpretasi Klinis Farmasis |
| :--- | :--- | :--- |
| **Nama Pasien** | Ny. Sunarti | Pasien rawat inap Bangsal Merak |
| **Nomor Rekam Medis** | 00109480 | Terdaftar aktif di RS PKU Muhammadiyah Bantul |
| **Usia / Tanggal Lahir** | 62 tahun 10 bulan | Geriatri (usia rentan terhadap dehidrasi dan fluktuasi glikemik) |
| **Jenis Kelamin** | Perempuan | Faktor risiko penurunan motilitas gaster / gastroparesis |
| **Berat Badan / Tinggi Badan** | 60 kg / 156 cm | IMT: 24,65 kg/m² (Kategori Normoweight mendekati Overweight) |
| **Ruang Rawat / Bangsal** | Bangsal Merak (Kelas II) | Perawatan rawat inap non-ICU |
| **Dokter DPJP** | dr. Raden Triyono Edhi Sulistiyono, Sp.PD, FINASIM | Dokter Spesialis Penyakit Dalam |
| **Diagnosis Utama Ranap** | **Mual dan Muntah karena Dispepsia (*Vomitus Profuse ec Dyspepsia*)** | Eksaserbasi dispepsia fungsional / gastroparesis dengan penurunan pengosongan lambung |
| **Diagnosis Sekunder Ranap** | 1. DM Tipe 2 Hiperglikemia Akut (GDS 357 mg/dL)<br>2. Hipertensi Stage 1 Terkontrol<br>3. Hiponatremia & Hipokloremia Ringan | Dekompensasi metabolik akut akibat intake oral tertutup dan stres fisik emetogenik |
| **Riwayat Alergi Obat** | **Amoksisilin & Ampisilin** | Riwayat urtikaria generalisata, eritema makulopapular, dan pruritus berat |

---

## 2.2 Riwayat Masuk Rumah Sakit & Keluhan Utama: Mual dan Muntah karena Dispepsia
* **Kronologi IGD**: Pasien dibawa ke IGD RS PKU Muhammadiyah Bantul pada 18 Oktober 2026 pukul 09.30 WIB dengan keluhan utama **mual hebat dan muntah profuse (frekuensi > 6 kali dalam 24 jam terakhir)**. Muntahan berisi cairan keruh bercampur lendir lambung dan sisa makanan, tanpa darah (hematemesis (-)) dan BAB hitam (-). Pasien mengeluhkan rasa perih menusuk dan terbakar pada ulu hati (epigastrium), perut kembung begah (*postprandial fullness*), cepat kenyang (*early satiation*), rasa asam naik ke kerongkongan (*heartburn*), dan badan terasa sangat lemas tak berdaya. Pasien sama sekali tidak dapat mentoleransi makanan maupun minuman per oral selama 18 jam terakhir.
* **Riwayat Obat Rumah (Home Medications)**: Pasien memiliki riwayat DM Tipe 2 selama 6 tahun dengan terapi rutin Metformin 500 mg 3x1 tablet dan Glimepirid 2 mg 1x1 tablet pagi, serta riwayat hipertensi rutin Amlodipin 10 mg 1x1 tablet malam. Namun, dalam 2 hari sebelum masuk RS, seluruh obat oral tidak dapat diminum karena langsung dimuntahkan kembali.

---

## 2.3 Pemantauan Tanda-Tanda Vital (TTV) Selama Rawat Inap
| Waktu Pemantauan | Tekanan Darah (mmHg) | Nadi (x/m) | RR (x/m) | Suhu (°C) | SpO2 (%) | Status Klinis & Evaluasi |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **18/10 (Masuk IGD)** | 145/88 | 88 | 20 | 36,8 | 98% | Kedaruratan akut; lemas berat, muntah profuse, nyeri ulu hati hebat |
| **19/10 (Hari Rawat 1)** | 135/82 | 84 | 18 | 36,6 | 99% | Mual berkurang, muntah 1x cairan, rehidrasi IV berjalan |
| **20/10 (Hari Rawat 2)** | 130/80 | 80 | 18 | 36,5 | 98% | Muntah berhenti, mual minimal, mulai toleransi diet cair |
| **21/10 (Hari Rawat 3)** | 125/78 | 78 | 18 | 36,5 | 99% | Stabil, keluhan dispepsia/mual tuntas, persiapan KRS |

![Tren TTV Ranap](ppt_assets/ttv_chart.png)
*Gambar 2.1: Grafik Perkembangan Tanda-Tanda Vital Ny. Sunarti Selama Rawat Inap di Bangsal Merak.*

---

## 2.4 Pemantauan Data Laboratorium Selama Rawat Inap
* **GDS Masuk IGD = 357 mg/dL**: Mengonfirmasi krisis hiperglikemia akut yang dipicu oleh hormon kontra-regulator stres dispepsia dan dehidrasi.
* **Urinalisis**: Glukosa Urin +3, Protein Negatif, **Keton Urin Negatif** (menyingkirkan diagnosis Ketoasidosis Diabetik / KAD).
* **Elektrolit Serum**: Natrium 131 mmol/L (Hiponatremia ringan) dan Klorida 96 mmol/L (Hipokloremia ringan) akibat hilangnya asam klorida (HCl) lambung dan natrium via vomitus profuse. Terkoreksi normal pada Hari ke-3 (Na 137 mmol/L, Cl 101 mmol/L) pasca infus NaCl 0,9%.
* **Fungsi Ginjal & Darah**: Kreatinin serum 0,98 mg/dL (eGFR 61,4 mL/min), Ureum 32 mg/dL, Leukosit normal 9.200 /µL (afebris, tanpa tanda infeksi bakterial).

| Parameter Laboratorium | Nilai IGD | Evaluasi (H2/H3) | Nilai Rujukan | Satuan | Interpretasi Klinis Farmasis |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **GDS (Masuk IGD)** | **357** | - | 70 – 140 | mg/dL | Hiperglikemia akut berat terinduksi stres dispepsia & dehidrasi |
| **GDS (Hari 1 Pagi)** | 245 | - | 140 – 180 | mg/dL | Respon inisiasi insulin Novorapid + Lantus |
| **GDS (Hari 1 Sore)** | 198 | - | 140 – 180 | mg/dL | Penurunan glikemik progresif stabil |
| **GDS (Hari 2 Pagi)** | 162 | - | 140 – 180 | mg/dL | Mencapai target glikemik rawat inap (140–180 mg/dL) |
| **GDS (Hari 2 Sore)** | 154 | - | 140 – 180 | mg/dL | Terkontrol sangat baik tanpa keluhan hipoglikemia |
| **GDS (Hari 3 Pagi)** | **138** | - | 140 – 180 | mg/dL | Target tercapai sempurna; siap transisi terapi pulang |
| **Natrium Darah (Na+)** | **131** | 137 (H3) | 135 – 147 | mmol/L | Hiponatremia ringan ec vomitus; terkoreksi infus NaCl 0,9% |
| **Kalium Darah (K+)** | 3,8 | 4,1 (H3) | 3,5 – 5,0 | mmol/L | Normal batas bawah; tidak terjadi hipokalemia berat |
| **Klorida Darah (Cl-)** | **96** | 101 (H3) | 98 – 106 | mmol/L | Hipokloremia ringan akibat hilangnya asam HCl lambung |
| **Ureum Darah** | 32 | 28 (H3) | 15 – 45 | mg/dL | Normal; tidak tampak azotemia nyata |
| **Kreatinin Serum** | 0,98 | 0,89 (H3) | 0,6 – 1,1 | mg/dL | Normal (eGFR 61,4 mL/min); fungsi filtrasi ginjal baik |
| **Glukosa Urin** | +3 | Negatif (H3) | Negatif | - | Glukosuria masif saat krisis hiperglikemia IGD |
| **Keton Urin** | Negatif | Negatif | Negatif | - | Menyingkirkan komplikasi Ketoasidosis Diabetik (KAD) |
| **Leukosit** | 9.200 | 7.800 (H3) | 4.000 – 10.000 | /µL | Normal; tidak ada fokus infeksi bakterial aktif |

![Tren GDS Ranap](ppt_assets/glucose_chart.png)
*Gambar 2.2: Grafik Penurunan GDS Ny. Sunarti Menuju Target Terapi Rawat Inap 140–180 mg/dL (PERKENI 2021 & ADA 2024).*

---

## 2.5 Profil Terapi Pengobatan Selama Rawat Inap
| Nama Obat / Cairan | Dosis & Frekuensi | Rute | Indikasi Klinis | Kategori Farmakologi |
| :--- | :--- | :---: | :--- | :--- |
| **IVFD NaCl 0,9%** | 20 tpm (1.500 mL/24j) | Intravena | Rehidrasi cairan & koreksi Na/Cl | Kristaloid Isotonik |
| **Inj. Omeprazole** | 40 mg / 24 jam vial | Intravena | Supresi asam lambung pada dispepsia | Proton Pump Inhibitor (PPI) |
| **Inj. Metoclopramide** | 10 mg / 8 jam amp (Gavistal) | Intravena | Mual muntah & pengosongan gaster | Prokinetik D2 Antagonist |
| **Domperidone Sirup/Tab** | 10 mg 3x1 (AC) | Oral | Mual muntah & begah epigastrik | Prokinetik D2 Antagonist Perifer |
| **Inj. Ondansetron** | 4 mg / 8 jam amp (prn) | Intravena | Antiemetik refrakter | Antagonis Reseptor Serotonin 5-HT3 |
| **Sucralfate Sirup** | 3 x 1 sendok makan (15 mL) AC | Oral | Mukoproteksi gaster & gastritis | Pelindung Mukosa Lambung |
| **Novorapid (Aspart)** | 3 x 6 - 8 Unit ac | Subkutan | Kontrol glikemik prandial rawat inap | Insulin Analog Rapid-Acting |
| **Lantus (Glargine)** | 1 x 10 Unit malam | Subkutan | Kontrol glikemik basal rawat inap | Insulin Analog Long-Acting Basal |
| **Amlodipin Tablet** | 10 mg 1x1 malam | Oral | Hipertensi esensial (rekonsiliasi) | DHP-Calcium Channel Blocker |
| **Parasetamol Tablet** | 500 mg 3x1 tab (k/p) | Oral | Analgesik / antipiretik prn | Analgesik Non-Opioid |

---

## 2.6 Identifikasi & Analisis Mendalam Drug-Related Problems (DRP) Rawat Inap

### DRP 1: Duplikasi Terapi Prokinetik D2 (Metoclopramide IV + Domperidone Oral) — Risiko Berat Ekstrapiramidal (EPS) & Perpanjangan Interval QTc
* **Analisis Klinis**: Pasien diresepkan Inj. Metoclopramide 10 mg IV tiap 8 jam bersamaan dengan Domperidone 10 mg 3x1 oral. Keduanya merupakan antagonis reseptor dopamin D2. Metoclopramide menembus sawar darah otak secara masif, sedangkan Domperidone bekerja di CTZ area postrema.
* **Bahaya Toksisitas Kombinasi Ganda**: Kombinasi ini TIDAK meningkatkan efikasi antiemetik, melainkan melipatgandakan risiko efek samping fatal: (1) Gejala Ekstrapiramidal Akut (EPS): distonia leher, krisis okulogirik, akatisia motorik, dan parkinsonisme sekunder pada geriatri; (2) Kardiotoksisitas: keduanya memblokade kanal kalium jantung IKr, memperpanjang repolarisasi ventrikel (*prolonged QTc interval*), dan berisiko memicu aritmia ventrikel Torsades de Pointes (TdP).
* **Klasifikasi Interaksi**: **Lexicomp Risk Rating: Category D / X (Avoid Combination / Consider Therapy Modification)**.
* **Rekomendasi Farmasis**: Hentikan salah satu obat. Pada fase akut dengan muntah aktif, gunakan **INJEKSI METOCLOPRAMIDE 10 mg IV tunggal (atau 5 mg pada geriatri)** dan **HENTIKAN DOMPERIDONE ORAL**. Jika muntah masih berlanjut, kombinasikan dengan antiemetik mekanisme berbeda: **INJEKSI ONDANSETRON 4 mg IV** (Antagonis Serotonin 5-HT3) yang bekerja sinergis tanpa risiko EPS.

![Duplikasi Prokinetik Lexicomp](guideline_evidence/drug_interaction_gavistal_domperidone.png)
*Gambar 2.3: Analisis Interaksi Mayor Duplikasi Prokinetik Dopamin D2 (Metoclopramide + Domperidone) — Lexicomp Risk Rating D/X.*

![Konsensus Dispepsia PGI DiPiro](guideline_evidence/konsensus_dispepsia_pgi_dipiro.png)
*Gambar 2.4: Pedoman Penatalaksanaan Dispepsia & Algoritma Antiemetik (Konsensus PGI 2021/2024 Hal. 12–16 & DiPiro 12th Ed Ch. 41-42).*

---

### DRP 2: Penyesuaian Dosis Ginjal Metoclopramide pada Pasien Geriatri
* **Analisis Klinis**: Sekitar 80% Metoclopramide dieliminasi via ginjal. Pada pasien geriatri usia 62 tahun 10 bulan dengan laju filtrasi ginjal yang rentan terhadap dehidrasi vomitus, pemberian dosis penuh 10 mg IV tiap 8 jam (30 mg/hari) memicu akumulasi obat sentral.
* **Guideline Klinis (Lexicomp Geriatric & Micromedex)**: Pada lansia atau pasien dengan penurunan filtrasi ginjal (CrCl < 60 mL/min), dosis Metoclopramide sebaiknya **diturunkan 50% menjadi 5 mg IV tiap 8 jam atau 10 mg IV tiap 12 jam**, dan durasi dibatasi maksimal 5 hari parenteral.
* **Rekomendasi Farmasis**: Turunkan dosis injeksi Metoclopramide menjadi 5 mg IV tiap 8 jam, pantau manifestasi gejala ekstrapiramidal, dan segera hentikan begitu pasien mampu mentoleransi asupan oral.

![Penyesuaian Ginjal Metoclopramide](guideline_evidence/lexicomp_metoclopramide_renal.png)
*Gambar 2.5: Panduan Penyesuaian Dosis Ginjal & Geriatri Metoclopramide (Lexicomp Drug Information 2024).*

---

### DRP 3: Tatalaksana Komprehensif Mual Muntah karena Dispepsia (Konsensus Nasional PGI 2021/2024 & DiPiro 12th Ed Ch. 41-42)
* **Analisis Klinis**: Dispepsia pada Ny. Sunarti bermanifestasi sebagai dispepsia fungsional / gastroparesis diabetik dengan gangguan akomodasi lambung dan perlambatan pengosongan gaster.
* **Strategi Terapi Berdasarkan Guideline**:
  1. *Supresi Asam Lambung*: Pemberian Inj. Omeprazole 40 mg IV sekali sehari secara poten menghambat pompa asam H+/K+-ATPase sel parietal, menaikkan pH lambung > 4, meredakan nyeri ulu hati panas terbakar (*heartburn*), dan memulihkan integritas sawar mukosa gaster (Konsensus PGI Hal. 12–16).
  2. *Mukoprotektor Lambung*: Sucralfate sirup 1 g (15 mL) 3 kali sehari dalam lambung kosong membentuk lapisan gel pelindung pada mukosa lambung yang terinflamasi dan menstimulasi sekresi prostaglandin endogen.
  3. *Antiemetik Rasional*: Kombinasi prokinetik parenteral tunggal untuk merangsang motilitas lambung ke arah duodenum dan rescue therapy Ondansetron 4 mg IV (antagonis 5-HT3) untuk memblokade jaras refleks muntah vagal di pusat muntah medula oblongata (DiPiro 12th Ed Ch. 41 & 42).

---

### DRP 4: Tatalaksana Hiperglikemia Akut Rawat Inap (GDS 357 mg/dL) — Penghentian OHO Oral, Inisiasi Regimen Insulin Basal-Bolus Target 140–180 mg/dL
* **Analisis Klinis**: Pasien masuk dengan krisis hiperglikemia (GDS 357 mg/dL). Pasien memiliki riwayat penggunaan OHO rumah (Metformin 500 mg 3x1 dan Glimepirid 2 mg 1x1).
* **Guideline Klinis**:
  1. *PERKENI 2021 (Hal. 98–101) & ADA Standards of Care 2024 Section 16 (Hal. S278–S282)*: Pada pasien DM rawat inap non-ICU:
     * **METFORMIN HARUS SEGERA DIHENTIKAN** sementara karena risiko fatal Asidosis Laktat akibat dehidrasi dan hipovolemia.
     * **SULFONILUREA (Glimepirid) HARUS DIHENTIKAN** sementara karena masa kerja panjang dan risiko tinggi hipoglikemia berat saat intake oral tidak menentu akibat muntah.
  2. *Standar Emas Terapi Insulin Basal-Bolus*:
     * **Insulin Basal (Lantus / Glargine)**: Mengontrol glukoneogenesis hepatik basal 24 jam. Diberikan 1x10 Unit malam hari.
     * **Insulin Bolus Prandial (Novorapid / Aspart)**: Mengontrol ekskursi glukosa pasca makan. Diberikan 3x6–8 Unit segera sebelum makan.
  3. *Target Glikemik Rawat Inap*: **140 – 180 mg/dL (7,8 – 10,0 mmol/L)**. Target < 110 mg/dL TIDAK DIREKOMENDASIKAN karena meningkatkan mortalitas akibat hipoglikemia berat (NICE-SUGAR trial), sedangkan target > 180 mg/dL meningkatkan risiko infeksi dan glukosuria osmotik.

![Panduan Inpatient PERKENI](guideline_evidence/perkeni_inpatient_guideline.png)
*Gambar 2.6: Pedoman Pengelolaan Hiperglikemia Pasien Rawat Inap Rumah Sakit Non-ICU (PERKENI 2021 Hal. 98–101).*

![Standar Inpatient ADA](guideline_evidence/ada_inpatient_guideline.png)
*Gambar 2.7: Standar Pelayanan Medis Diabetes Rawat Inap & Target Glikemik 140–180 mg/dL (ADA Standards of Care 2024 Section 16).*

---

### DRP 5: Rekonsiliasi Terapi Antihipertensi Rawat Inap (Amlodipin 10 mg)
* **Analisis Klinis**: Pasien memiliki riwayat hipertensi rutin Amlodipin 10 mg malam di rumah. Pada 24 jam pertama rawat inap saat muntah masih profuse, obat oral ditunda sementara untuk menghindari keluarnya obat melalui muntah. Memasuki Hari Rawat ke-2 saat keluhan mual muntah teratasi dan pasien mulai toleransi diet oral, **Amlodipin 10 mg 1x1 malam SEGERA DIREKONSILIASI dan diberikan kembali per oral** sesuai panduan PERHI 2021 dan ACC/AHA 2023 untuk mencegah *rebound hypertension*.

![Rekonsiliasi Hipertensi PERHI](guideline_evidence/perhi_acc_aha_hypertension_reconciliation.png)
*Gambar 2.8: Protokol Rekonsiliasi Terapi Antihipertensi Rawat Inap (Konsensus PERHI 2021 & ACC/AHA 2023).*

---

### DRP 6: Rehidrasi Cairan Kristaloid Isotonik & Koreksi Elektrolit Hiponatremia dan Hipokloremia Akibat Vomitus Profuse
* **Analisis Klinis**: Muntah profuse > 6 kali mengakibatkan defisit volume cairan ekstraseluler dan pengeluaran masif ion natrium dan klorida lambung, menghasilkan kadar Na 131 mmol/L dan Cl 96 mmol/L.
* **Guideline Klinis (WHO & DiPiro 12th Ed Ch. 38)**:
  * Cairan kristaloid isotonik terpilih adalah **INFUS NaCl 0,9% (Normal Saline)** yang mengandung Na+ 154 mEq/L dan Cl- 154 mEq/L (308 mOsm/L). Cairan ini mengembalikan perfusi renal dan mengoreksi defisit elektrolit secara fisiologis.
  * Kecepatan infus 20 tetes/menit (makro ~1.500 mL/24 jam) aman bagi geriatri, mencegah kelebihan beban cairan (*fluid overload*) dan sindrom demielinisasi osmotik (*osmotic demyelination syndrome*).
  * Terbukti pada Hari ke-3, elektrolit terkoreksi sempurna: Na 137 mmol/L dan Cl 101 mmol/L.

![Rehidrasi Muntah DiPiro](guideline_evidence/vomitus_rehydration_guideline.png)
*Gambar 2.9: Panduan Terapi Rehidrasi Cairan & Koreksi Gangguan Elektrolit pada Pasien Mual-Muntah Akut (DiPiro 12th Ed Ch. 38).*

---

### DRP 7: Evaluasi Penggunaan Obat Geriatri Berdasarkan AGS Beers Criteria 2023
* **Analisis Klinis**: Evaluasi daftar terapi geriatri Ny. Sunarti (62 tahun 10 bulan) berdasarkan kriteria AGS Beers Criteria 2023:
  1. *Metoclopramide*: Penggunaan jangka panjang (> 12 minggu) dikontraindikasikan pada lansia karena risiko diskinesia tardif ireversibel. Durasi penggunaan parenteral dibatasi hanya 3 hari selama rawat inap akut.
  2. *Insulin Analog (Novorapid & Lantus)*: Sangat tepat dan direkomendasikan pada geriatri rawat inap karena profil kerja yang stabil, waktu paruh terprediksi, dan menurunkan insidensi hipoglikemia nokturnal berat secara signifikan dibandingkan insulin reguler/NPH manusiawi.

![Geriatri Beers Criteria](guideline_evidence/beers_criteria_geriatric.png)
*Gambar 2.10: Kriteria Penggunaan Obat yang Berpotensi Tidak Tepat pada Populasi Geriatri (AGS Beers Criteria 2023).*

---

### DRP 8: Evaluasi Rasionalitas Antibiotik Metode Gyssens & Riwayat Alergi Penisilin
* **Analisis Klinis**: Pasien memiliki riwayat alergi berat terhadap Amoksisilin dan Ampisilin (ruam makulopapular dan gatal). Selama rawatan di Bangsal Merak, DPJP **TIDAK MERESEPKAN ANTIBIOTIK** empiris.
* **Audit Kualitatif Metode Gyssens (Permenkes RI No. 28/2021)**: Pasien mengalami dispepsia fungsional murni tanpa fokus infeksi bakterial (leukosit normal 9.200 /µL, suhu afebris 36,8°C, urin leukosit negatif). Keputusan untuk tidak memberikan antibiotik dinilai sebagai **KATEGORI 0: Penggunaan / Keputusan Terapi Antibiotik TEPAT dan RASIONAL (No Antibiotic Indicated)**.
* **Manajemen Alergi**: Riwayat alergi penisilin wajib diberi penanda stiker merah menyala pada rekam medis fisik dan peringatan pop-up pada rekam medis elektronik. Bila di masa depan pasien memerlukan antibiotik infeksi berat, golongan Sefalosporin generasi 3 (Ceftriaxone) dapat dipertimbangkan (*cross-reactivity* < 2%) atau menggunakan golongan non-beta laktam (Fluoroquinolon / Makrolida).

![Algoritma Gyssens](guideline_evidence/gyssens_algorithm_flowchart.png)
*Gambar 2.11: Algoritma Audit Kualitatif Rasionalitas Penggunaan Antibiotik Metode Gyssens (Permenkes No. 28/2021).*

---

## 2.7 Dokumentasi Asuhan Kefarmasian (SOAP) Rawat Inap Lengkap (Per Hari Rawatan)

### SOAP Hari ke-1 Rawat Inap (18–19 Oktober 2026) — Fase Kedaruratan Akut
| Problem Medis | Subjektif (S) & Objektif (O) | Asesmen Farmasis (A) | Rencana Asuhan & Intervensi Farmasis (P) |
| :--- | :--- | :--- | :--- |
| **Mual Muntah ec Dispepsia** | **S**: Muntah > 6x, isi cairan & lendir, lemas berat, nyeri ulu hati menusuk, tidak bisa makan/minum.<br>**O**: Nyeri tekan epigastrium (+), turgor kulit menurun. | Vomitus profuse ec dispepsia akut. Duplikasi prokinetik D2 (Metoclopramide IV + Domperidone PO) berisiko EPS dan aritmia QTc (Lexicomp Cat D/X). | 1. IVFD NaCl 0,9% 20 tpm untuk rehidrasi cairan.<br>2. Inj. Omeprazole 40 mg / 24 jam IV vial.<br>3. Pertahankan Inj. Metoclopramide 10 mg IV (atau 5 mg pada lansia).<br>4. **REKOMENDASI**: HENTIKAN Domperidone oral.<br>5. Berikan Inj. Ondansetron 4 mg IV bila muntah refrakter. |
| **Hiperglikemia DM Tipe 2** | **S**: Badan lemas tak bertenaga, riwayat DM rutin Metformin & Glimepirid.<br>**O**: GDS 357 mg/dL, Glukosa Urin +3, Keton Negatif. | Krisis hiperglikemia terinduksi stres dispepsia dan dehidrasi. OHO oral dikontraindikasikan (PERKENI & ADA). | 1. HENTIKAN sementara Metformin & Glimepirid oral.<br>2. Inisiasi Regimen Insulin Basal-Bolus:<br>   - Novorapid SC 3 x 6 Unit ac (prandial)<br>   - Lantus SC 1 x 10 Unit malam (basal)<br>3. Monitoring GDS serial tiap 6 jam (target 140–180 mg/dL). |
| **Hiponatremia & Hipokloremia** | **S**: Lemas badan, pusing melayang.<br>**O**: Na+ 131 mmol/L (L), Cl- 96 mmol/L (L), K+ 3,8 mmol/L. | Hiponatremia dan hipokloremia ringan akibat kehilangan cairan lambung asam via muntah berulang. | 1. Rehidrasi kristaloid isotonik Infus NaCl 0,9% 20 tpm.<br>2. Evaluasi ulang elektrolit serum serial 24–48 jam. |
| **Hipertensi Esensial** | **S**: Pusing kepala ringan.<br>**O**: TD 145/88 mmHg. Riwayat Amlodipin 10 mg rumah. | Hipertensi terkontrol borderline. Terapi oral ditunda 24 jam karena muntah aktif. | 1. Tunda Amlodipin oral hingga toleransi oral membaik.<br>2. Pantau tekanan darah tiap 8 jam. |

---

### SOAP Hari ke-2 Rawat Inap (20 Oktober 2026) — Fase Stabilisasi
| Problem Medis | Subjektif (S) & Objektif (O) | Asesmen Farmasis (A) | Rencana Asuhan & Intervensi Farmasis (P) |
| :--- | :--- | :--- | :--- |
| **Mual Muntah ec Dispepsia** | **S**: Mual berkurang drastis, muntah sudah berhenti, nyeri ulu hati mereda, mulai nafsu makan.<br>**O**: Nyeri epigastrium (-), TD 130/80 mmHg, Nadi 80x/m. | Respon terapi dispepsia sangat baik. Mukosa gaster membaik dengan PPI parenteral. | 1. Lanjutkan Inj. Omeprazole 40 mg IV.<br>2. Inj. Metoclopramide 10 mg diturunkan menjadi prn atau dihentikan.<br>3. Berikan Sucralfate sirup 3x1 C ac (oral).<br>4. Transisi diet lunak bertahap porsi kecil sering. |
| **Hiperglikemia Rawat Inap** | **S**: Badan terasa segar, tidak ada keluhan gemetar atau keringat dingin (hipoglikemia (-)).<br>**O**: GDS Pagi: 162 mg/dL, GDS Sore: 154 mg/dL. | Kontrol glikemik rawat inap tercapai sempurna (target 140–180 mg/dL sesuai PERKENI & ADA). | 1. Lanjutkan Novorapid SC 3 x 6 Unit ac.<br>2. Lanjutkan Lantus SC 1 x 10 Unit malam.<br>3. Edukasi teknik penyuntikan insulin mandiri. |
| **Hipertensi & Rekonsiliasi** | **S**: Tidak ada keluhan pusing.<br>**O**: TD 130/80 mmHg. | Pasien telah mampu mentoleransi asupan oral. Indikasi rekonsiliasi antihipertensi rumah. | 1. Berikan kembali Amlodipin tablet 10 mg 1x1 malam oral.<br>2. Pantau tekanan darah serial. |

---

### SOAP Hari ke-3 Rawat Inap (21 Oktober 2026) — Persiapan KRS & Discharge Planning
| Problem Medis | Subjektif (S) & Objektif (O) | Asesmen Farmasis (A) | Rencana Asuhan & Intervensi Farmasis (P) |
| :--- | :--- | :--- | :--- |
| **Kesiapan Pasien Pulang (KRS)** | **S**: Tidak mual, tidak muntah, makan habis 1 porsi bubur, badan segar.<br>**O**: TD 125/78 mmHg, GDS Pagi: 138 mg/dL, Elektrolit normal: Na 137 mmol/L, Cl 101 mmol/L. | Kondisi klinis stabil sempurna. Mual muntah dispepsia teratasi tuntas. Glikemik dan elektrolit normal. Pasien siap KRS (*Discharge Planning*). | 1. **Resep Pulang (Oral & Subkutan)**:<br>   - Lansoprazole kapsul 30 mg 1x1 ac pagi<br>   - Sucralfate sirup 3x1 C ac (selama 5 hari)<br>   - Lantus SoloStar Pen 1 x 10 Unit SC malam<br>   - Metformin tablet 500 mg 3x1 dc (reintroduksi aman karena fungsi ginjal & cairan normal)<br>   - Amlodipin tablet 10 mg 1x1 malam PO<br>2. **Konseling Farmasis Pulang (KIE)**:<br>   - Edukasi teknik injeksi insulin SoloStar, rotasi lokasi tusukan, dan penyimpanan di lemari es (2–8°C).<br>   - Edukasi tanda-tanda hipoglikemia dan penanganan daruratnya.<br>   - Edukasi pola makan teratur porsi kecil sering (*small frequent meals*) untuk pencegahan dispepsia berulang. |

---

# BAGIAN III: DAFTAR PUSTAKA LENGKAP (HARVARD / APA 7TH EDITION)

1. **American Diabetes Association (ADA)**. (2024). Standards of Care in Diabetes—2024: Diabetes Care in the Hospital (Section 16). *Diabetes Care*, 47(Suppl. 1), S278–S282.
2. **American Diabetes Association (ADA)**. (2024). Standards of Care in Diabetes—2024: Pharmacologic Approaches to Glycemic Treatment (Section 9 & 10). *Diabetes Care*, 47(Suppl. 1), S158–S178.
3. **American Geriatrics Society (AGS) Beers Criteria Update Expert Panel**. (2023). American Geriatrics Society 2023 updated AGS Beers Criteria for potentially inappropriate medication use in older adults. *Journal of the American Geriatrics Society*, 71(7), 2052–2081.
4. **DiPiro, J. T., Yee, G. C., Posey, L. M., Haines, S. T., Nolin, T. D., & Ellingrod, V.**. (2023). *DiPiro's Pharmacotherapy: A Pathophysiologic Approach* (12th ed.). McGraw-Hill Education:
   - Chapter 38: Disorders of Sodium and Water Homeostasis (pp. 752–758).
   - Chapter 41: Nausea and Vomiting (pp. 815–828).
   - Chapter 42: Peptic Ulcer Disease and Related Disorders (pp. 830–845).
   - Chapter 57: Diabetes Mellitus (pp. 1115–1160).
   - Chapter 60: Osteoarthritis (pp. 1220–1235).
5. **Gyssens, I. C., van den Broek, P. J., Kullberg, B. J., Hekster, Y., & van der Meer, J. W.**. (1992). Optimizing antimicrobial therapy: Evaluation of quality of antimicrobial practice in an Indonesian university hospital. *Journal of Antimicrobial Chemotherapy*, 30(5), 701–709.
6. **Indonesian Rheumatology Association (IRA)**. (2021). *Rekomendasi IRA untuk Diagnosis dan Penatalaksanaan Osteoarthritis*. Perhimpunan Reumatologi Indonesia, Jakarta (pp. 14–19).
7. **Kementerian Kesehatan Republik Indonesia**. (2021). *Keputusan Menteri Kesehatan Republik Indonesia Nomor HK.01.07/MENKES/6485/2021 tentang Formularium Nasional*. Kemenkes RI, Jakarta.
8. **Kementerian Kesehatan Republik Indonesia**. (2021). *Peraturan Menteri Kesehatan Republik Indonesia Nomor 28 Tahun 2021 tentang Pedoman Penggunaan Antibiotik*. Kemenkes RI, Jakarta (pp. 35–40).
9. **Lexicomp Online**. (2024). *Lexi-Interact & Geriatric Lexi-Drugs: Metoclopramide, Domperidone, Sitagliptin, Glimepiride, Amlodipine, and NSAIDs Monograph*. Wolters Kluwer Clinical Drug Information, Inc.
10. **Morisky, D. E., Ang, A., Krousel-Wood, M., & Ward, H. J.**. (2008). Predictive validity of a medication adherence measure in an outpatient setting. *The Journal of Clinical Hypertension*, 10(5), 348–354.
11. **Naranjo, C. A., Busto, U., Sellers, E. M., Sandor, P., Ruiz, I., Roberts, E. A., Janecek, E., Domecq, C., & Greenblatt, D. J.**. (1981). A method for estimating the probability of adverse drug reactions. *Clinical Pharmacology and Therapeutics*, 30(2), 239–245.
12. **Perhimpunan Dokter Spesialis Kardiovaskular Indonesia (PERKI)**. (2022). *Panduan Tatalaksana Dislipidemia di Indonesia*. Pengurus Pusat PERKI, Jakarta (pp. 25–30).
13. **Perhimpunan Dokter Spesialis Penyakit Dalam Indonesia (PAPDI)**. (2021). *Panduan Praktik Klinis Penyakit Dalam: Pendekatan Holistik Kasus Geriatri dan Dispepsia*. PAPDI, Jakarta.
14. **Perhimpunan Dokter Hipertensi Indonesia (PERHI)**. (2021). *Konsensus Penatalaksanaan Hipertensi 2021*. PERHI, Jakarta (pp. 18–26).
15. **Perhimpunan Endokrinologi Indonesia (PERKENI)**. (2021). *Pedoman Pengelolaan dan Pencegahan Diabetes Melitus Tipe 2 Dewasa di Indonesia 2021*. PB PERKENI, Jakarta: Halaman 36–39, 45–50, 98–101.
16. **Perkumpulan Gastroenterologi Indonesia (PGI)**. (2021/2024). *Konsensus Nasional Penatalaksanaan Dispepsia dan Infeksi Helicobacter pylori di Indonesia*. Pengurus Besar Perkumpulan Gastroenterologi Indonesia (PB PGI), Jakarta: Halaman 12–28.
17. **Shetty, R., Vivek, G., & Shenoy, S.**. (2016). Management of amlodipine-induced peripheral edema: Review of literature and clinical perspective. *Journal of Clinical and Diagnostic Research*, 10(7), OE01–OE04.
18. **Skovbjerg, S., Dam, C., & Christensen, K. L.**. (2023). Amlodipine-induced peripheral edema: Pathophysiology, incidence, and management strategies combining renin-angiotensin system inhibitors. *Journal of Clinical Hypertension*, 25(2), 112–119.
19. **Tolla, E. M., et al.**. (2026). Real-world evidence on the management of calcium channel blocker-induced peripheral edema in hypertensive patients. *International Journal of Cardiology Cardiovascular Risk and Prevention*, 18, 200–208.
20. **World Health Organization (WHO)**. (2023). *The Selection and Use of Essential Medicines: WHO Technical Report Series*. World Health Organization, Geneva.
"""

output_path = r"d:\FILE NINIS\ANALISIS_KASUS_MENDALAM_RAJAL_DAN_RANAP.md"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"Master Markdown report generated successfully at: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")

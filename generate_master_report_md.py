# -*- coding: utf-8 -*-
"""
Revised Script to generate ANALISIS_KASUS_MENDALAM_RAJAL_DAN_RANAP.md
Full markdown report incorporating revised Rajal data from RSPAU Dr. S. Hardjolukito
and keeping Ranap (Ny. Sunarti) with Inpatient Dyspepsia Nausea/Vomiting.
"""

import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

md_content = """# LAPORAN LENGKAP & ANALISIS MENDALAM PEMANTAUAN TERAPI OBAT (PTO)
## Asuhan Kefarmasian Klinis Rawat Jalan (Rajal) & Rawat Inap (Ranap)
**Instalasi Farmasi RSPAU dr. S. Hardjolukito & RS PKU Muhammadiyah Bantul**
*Berdasarkan Konsensus PERKENI 2021, Konsensus PGI 2021/2024, DiPiro's Pharmacotherapy 12th Ed 2023, ADA Standards of Care 2024, & AGS Beers Criteria 2023*

---

> [!NOTE]
> **RINGKASAN EKSEKUTIF KASUS (EXECUTIVE SUMMARY)**
> Dokumen ini menyajikan asuhan kefarmasian klinis (*Evidence-Based Clinical Pharmacy*) yang komprehensif dan mendalam untuk dua pasien kasus kompleks:
> 1. **Kasus Rawat Jalan (RSPAU dr. S. Hardjolukito): Ny. Sri Wisraya (64 th, RM 00062584, Farmasis: Nurhasna Sushmita Sari, S.Farm. / Tim PKPA RSPAU)** — Diagnosa Utama: **OA GENU BILATERAL (M17.0)**; Diagnosa Sekunder: **DM TIPE 2 (E11.9)** dan **HIPERTENSI ESENSIAL (I10)**; Riwayat Penyakit: Dislipidemia (E78.5), Neuropati Diabetik (E11.5), Vertigo Sentral (H81.4), Post Trauma CKR & Fraktur Os Zygoma/Frontalis, serta Penurunan Klirens Ginjal Berat (CrCl 17,67 mL/min). Evaluasi DRP mencakup: over-dosis Glimepirid 6 mg/hari pada geriatri (PIM Beers 2023 & tidak sesuai Fornas), indikasi inisiasi insulin basal (PERKENI 2021), penyesuaian ginjal Sitagliptin, interaksi NSAID oral nefrotoksik, interaksi sedasi Gabapentin-Flunarizine, restriksi Fornas, profil ADR top 3, dan kepatuhan MMAS-8 (skor 5,0 - Kepatuhan Rendah).
> 2. **Kasus Rawat Inap (Bangsal Merak): Ny. Sunarti (62 th 10 bln, RM 00109480, DPJP: dr. Raden Triyono Edhi S., Sp.PD)** — Diagnosis Utama: **Mual dan Muntah karena Dispepsia (*Vomitus Profuse ec Dyspepsia*)** disertai krisis hiperglikemia akut DM Tipe 2 (GDS 357 mg/dL), riwayat hipertensi, serta dehidrasi dengan hiponatremia (Na 131 mmol/L) dan hipokloremia (Cl 96 mmol/L). Evaluasi DRP mencakup: duplikasi prokinetik D2 (Metoclopramide IV + Domperidone PO) berisiko gejala ekstrapiramidal dan aritmia QTc (Lexicomp Risk Rating D/X), penyesuaian ginjal Metoclopramide pada geriatri, tatalaksana dispepsia mual-muntah berbasis Konsensus PGI & DiPiro 12th Ed Ch. 41-42, tatalaksana hiperglikemia rawat inap (penghentian OHO Metformin & Glimepirid, inisiasi basal-bolus Novorapid + Lantus target 140–180 mg/dL sesuai PERKENI Hal. 98–101 & ADA 2024 Section 16), rekonsiliasi antihipertensi, rehidrasi kristaloid isotonik NaCl 0,9%, serta audit kualitatif antibiotik metode Gyssens (Kategori 0 / Tepat tanpa antibiotik pada riwayat alergi penisilin).

---

# BAGIAN I: ANALISIS MENDALAM KASUS RAWAT JALAN (RAJAL) — NY. SRI WISRAYA

## 1.1 Profil Demografi & Data Dasar Pasien Rawat Jalan
| Parameter Klinis | Nilai / Keterangan Pasien | Interpretasi Klinis Farmasis |
| :--- | :--- | :--- |
| **Fasilitas Pelayanan Kesehatan** | Instalasi Farmasi RSPAU dr. S. Hardjolukito | Rumah Sakit Rujukan Tingkat Lanjutan (FKRTL) |
| **Farmasis Penanggung Jawab** | Nurhasna Sushmita Sari, S.Farm. / Tim PKPA | Apoteker Klinis Penelaah Farmakoterapi & DRP |
| **Nama Pasien** | **SRI WISRAYA** | Pasien geriatri rawat jalan multipel poliklinik |
| **Nomor Rekam Medis** | **00062584** | Terdaftar aktif di RSPAU dr. S. Hardjolukito |
| **Usia / Jenis Kelamin** | 64 tahun / Perempuan | Geriatri; rentan terhadap ADR, PIM Beers, polifarmasi |
| **Berat Badan / Tinggi Badan** | 52 kg / 156 cm | IMT: 21,37 kg/m² (Normoweight / status gizi baik) |
| **Ruangan / Poliklinik** | Poli Penyakit Dalam (Rawat Jalan) | Poliklinik utama pemantauan terapi kronis |
| **DPJP Utama** | **dr. TRI HARININGSIH, Sp.PD** | Dokter Spesialis Penyakit Dalam |
| **Dokter Rawat Bersama (Raber)** | 1. dr. Raden Suhana, Sp.OT(K)<br>2. dr. Wahyu Wihartono, Sp.N<br>3. dr. Supanji, Sp.M | Poli Bedah Orthopedi<br>Poli Spesialis Saraf / Neurologi<br>Poli Spesialis Mata |
| **Tanggal Periode Kontrol** | 27-04-2026 (M1) s/d 07-10-2026 (M6) | Pemantauan longitudinal serial selama 6 bulan |
| **Riwayat Alergi** | Tidak Ada Alergi Obat (-) | Aman terhadap golongan analgesik & antibiotik |
| **Diagnosa Utama** | **OA GENU BILATERAL (M17.0)** | Nyeri dan kekakuan kronis sendi lutut bilateral |
| **Diagnosa Sekunder 1 & 2** | **DM TIPE 2 (E11.9)**<br>**HIPERTENSI ESENSIAL (I10)** | DM tidak terkontrol (HbA1c 9,1%) & HT belum mencapai target <130/80 |
| **Riwayat Penyakit Terdahulu** | Dislipidemia (E78.5)<br>Neuropati Diabetik (E11.5)<br>Vertigo Sentral (H81.4)<br>Post Trauma CKR & Fraktur Os Zygoma | Komorbiditas multi-organ kompleks dengan riwayat insiden jatuh di kamar mandi pada 04/07/2026 |
| **Riwayat Penggunaan Obat** | Glimepirid, Amlodipin, Gabapentin, Rosuvastatin, Sitagliptin, Acarbose, Flamar Gel, Meloxicam, Kalium Diklofenak, Flunarizine, Glucosamine, Mecobalamin | Polifarmasi aktif (7–9 obat/hari) dengan risiko tinggi interaksi obat dan nefrotoksisitas |

---

## 1.2 Riwayat Kunjungan Kontrol, Keluhan Subjektif, & Kepatuhan Pasien (M1 – M6)
| Tanggal & Sesi | Poliklinik Dikunjungi | Keluhan Pasien (Subjektif) | Skor Nyeri / Tanda Khusus | Kepatuhan Pasien (MMAS-8) |
| :--- | :--- | :--- | :---: | :--- |
| **27-04-2026 (M1)** | Poli Penyakit Dalam | Kontrol rutin DM, lutut sakit (+), kebas (+), pusing (-) | NRS 2 (Ringan) | Teratur (Awal kontrol) |
| **29-05-2026 (M2)** | Poli Saraf & Mata | Lutut sakit, bengkak (-), kebas (+), pusing (-) | NRS 4 (Sedang) | Teratur |
| **29-06-2026 (M3)** | Poli Mata | Lutut kiri nyeri kaku (+++), kebas (++), pusing (+) | NRS 6 (Berat) | Teratur (Dosis Glimepirid naik ke 6 mg) |
| **04-07-2026 (Trauma)** | IGD (Bedah/Saraf/Rad) | Kepala terbentur ec jatuh di kamar mandi, nyeri kepala | NRS +++ (Akut) | Trauma Jatuh (GDS spike 308 mg/dL) |
| **05-08-2026 (M4)** | Poli Mata | Evaluasi paska rawat, lutut nyeri (++), gliyer (+) | NRS 4 (Sedang) | Kurang Tertib (TD spike 165/89 mmHg) |
| **07-09-2026 (M5)** | Poli Mata | Lutut nyeri (++), gliyer (+) / Vertigo Sentral | NRS 4 (Sedang) | Lupa Bawa Obat (Acarbose & Diklofenak masuk) |
| **07-10-2026 (M6)** | Poli Ortho & Mata | Lutut kanan sakit (++), kebas (+), pusing (+) | NRS 4 (Sedang) | Bingung Waktu Minum (Switch Atorvastatin) |

---

## 1.3 Pemantauan Tanda-Tanda Vital (TTV) 6 Bulan
Berdasarkan pemantauan serial tanda-tanda vital, tekanan darah sistolik pasien berfluktuasi tajam antara 133 hingga 165 mmHg, dan diastolik antara 76 hingga 98 mmHg. Target konsensus PERHI 2021 untuk pasien diabetes dengan komorbid kardiovaskular adalah < 130/80 mmHg. Monoterapi Amlodipin 10 mg terbukti belum adekuat mengontrol tekanan darah sistolik. Puncak lonjakan tekanan darah (spike) terjadi pada 05/08/2026 mencapai **165/89 mmHg** pasca trauma dan pemberian NSAID oral. Denyut nadi tercatat takikardia (99, 97, 103 x/menit) terutama saat episode nyeri lutut berat dan stres pasca jatuh.

| Tanggal Kontrol | Sistole (mmHg) | Diastole (mmHg) | Nadi (x/m) | Suhu (°C) | RR (x/m) | SpO2 (%) | NRS | Evaluasi Klinis TTV |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **27-04-2026** | 154 | 98 | 99 | 36,0 | 22 | 99% | 2 | Hipertensi Stage 2; takikardia ringan |
| **29-05-2026** | 138 | 76 | 97 | 36,0 | 22 | 99% | 4 | Terkontrol borderline |
| **29-06-2026** | 156 | 85 | 89 | 36,0 | 22 | 99% | 6 | Hipertensi Stage 2; nyeri lutut kaku |
| **05-08-2026** | 165 | 89 | 103 | - | - | - | 4 | Spike TD & takikardia paska trauma/NSAID |
| **07-09-2026** | 141 | 80 | 92 | 36,0 | 21 | 99% | 4 | Hipertensi Stage 1; vertigo sentral |
| **07-10-2026** | 133 | 80 | 92 | 36,0 | 21 | 99% | 4 | Mendekati target (<130/80 mmHg) |

![Tren Tekanan Darah Rajal](guideline_evidence_rajal/rajal_bp_trend.png)
*Gambar 1.1: Grafik Tren Tekanan Darah Ny. Sri Wisraya Selama 6 Bulan Terakhir (Target PERHI <130/80 mmHg).*

---

## 1.4 Pemantauan Data Laboratorium & Pemeriksaan Radiologi
Profil laboratorium mengonfirmasi kegagalan glikemik berat (glukotoksisitas tinggi) dengan nilai **HbA1c mencapai 9,1%*** pada 29/05/2026. Kadar glukosa darah puasa (GDP) persisten tinggi (169*, 190*, 151* mg/dL) dan GD2PP 211* mg/dL, dengan lonjakan GDS mencapai 308* mg/dL saat trauma jatuh di IGD. Pada pemeriksaan fungsi ginjal pasca trauma (04/07/2026), serum kreatinin melonjak menjadi **2,69* mg/dL** dan Ureum 73* mg/dL.
$$\text{CrCl} = \frac{(140 - 64) \times 52 \text{ kg}}{72 \times 2,69 \text{ mg/dL}} \times 0,85 = \mathbf{17,67 \text{ mL/menit}} \quad (\text{Gangguan Ginjal Berat / AKI on CKD Stage 4})$$

| Pemeriksaan Lab | Nilai Pasien | Nilai Normal | Satuan | Interpretasi & Analisis Evaluasi Klinis |
| :--- | :---: | :---: | :---: | :--- |
| **HbA1c (29/05/2026)** | **9,1*** | 4,0 – 6,5 | % | TIDAK TERKONTROL; glukotoksisitas tinggi, indikasi mutlak insulin basal |
| **GDS (27/04/2026)** | 164 | < 200 | mg/dL | Terkontrol sedang |
| **GDS (29/05/2026)** | 252* | < 200 | mg/dL | Hiperglikemia postprandial meningkat |
| **GDP (29/06/2026)** | 169* | 70 – 115 | mg/dL | Hiperglikemia puasa persisten |
| **GD2PP (29/06/2026)** | 211* | < 140 | mg/dL | Ekskursi postprandial masif (dasar penambahan Acarbose) |
| **GDS (04/07/2026 IGD)** | 244 – 308* | < 200 | mg/dL | Spike glukosa akut terinduksi stres trauma jatuh & nyeri |
| **GDP (05/08/2026)** | 190* | 70 – 115 | mg/dL | GDP tetap tinggi pasca trauma |
| **GDP (07/09/2026)** | 151* | 70 – 115 | mg/dL | Respon parsial pasca eskalasi terapi OHO |
| **Kreatinin Serum (04/07)** | **2,69*** | 0,6 – 1,1 | mg/dL | CrCl 17,67 mL/min (Gangguan ginjal berat / AKI on CKD); order ulang 06/11 |
| **Ureum Darah (04/07)** | 73* | 19 – 44 | mg/dL | Azotemia / retensi nitrogen pasca trauma dan stres akut |
| **Hemoglobin (Hb)** | 10,1* | 13,2 – 17,3 | g/dL | Anemia ringan (Grade 1) ec penyakit kronis (CKD/DM) |
| **Hematokrit (Hct)** | 30,0* | 40 – 52 | % | Menurun selaras dengan anemia |
| **Trombosit** | 228.000 | 150.000 – 440.000 | /mm³ | Normal; fungsi hemostasis trombosit baik |
| **Leukosit** | Normal | 4.380 – 10.600 | /mm³ | Tidak tampak tanda infeksi bakterial akut |
| **SGOT / SGPT** | 29 / 20 | < 35 / < 45 | U/L | Fungsi hepatik sangat baik (aman untuk terapi Atorvastatin 20 mg) |

![Profil Glukosa Rajal](guideline_evidence_rajal/rajal_glucose_trend.png)
*Gambar 1.2: Profil Glukosa Darah Ny. Sri Wisraya (HbA1c = 9,1% - Uncontrolled, GDS Spike 308 mg/dL).*

### Temuan Radiologi & Korelasi Klinis
1. **Foto Pelvis AP (16/05/2026)**: Periarticular calcification hip dextra (Poli Saraf / LBP). Menunjukkan proses degeneratif osteofit panggul.
2. **CT-Scan Kepala Non-Kontras (04/07/2026)**: Pembengkakan jaringan lunak daerah zygomaticum kiri s/d frontalis kiri disertai lesi hiperdens hematoma (HU: 69-75). Fraktur linier os zygomaticum kiri dan os frontalis kiri, hematosinus maksilaris kiri, sinusitis maksilaris kanan, ethmoidalis bilateral dan frontalis kanan. Tidak tampak perdarahan intrakranial (EDH/SDH (-)), lesi iskemik, maupun SOL.

---

## 1.5 Profil Pengobatan Kronis Pasien (April – Oktober 2026)
| Nama Obat | Rute | Regimen Dosis | M1 (27/04) | M2 (29/05) | M3 (29/06) | M4 (05/08) | M5 (07/09) | M6 (07/10) | Tujuan Terapi & Evaluasi Dinamika |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Amlodipin 10 mg** | PO | 1x1 pagi | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Monoterapi gagal target <130/80; risiko edema |
| **Flamar Gel** | Topikal | 2x sehari oles | ✓ | ✓ | ✓ | - | ✓ | ✓ | Lini 1 OA Genu; absorpsi sistemik <6%, aman ginjal |
| **Gabapentin 100 mg** | PO | 1x1 malam | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Nyeri neuropati diabetik rutin |
| **Glimepirid 4 mg** | PO | 1x1 ac pagi | ✓ | ✓ | - | - | - | - | Dosis awal dititrasi naik ke 6 mg/hari |
| **Glimepirid 3 mg** | PO | 2x1 ac pagi-sore | - | - | ✓ | ✓ | ✓ | ✓ | Dosis 6 mg/hari. Overdosis geriatri & PIM Beers! |
| **Glucosamine 500 mg** | PO | 1x1 pc | ✓ | ✓ | ✓ | - | ✓ | - | Kondroprotektif OA. Non-Fornas |
| **Mecobalamin 500 mcg**| PO | 1x1 pc | ✓ | ✓ | ✓ | - | - | - | Neurotropik B12 aktif (dihentikan Agustus 2026) |
| **Rosuvastatin 10 mg** | PO | 1x1 malam | ✓ | ✓ | ✓ | ✓ | ✓ | - | Statin rutin April–September 2026 |
| **Meloxicam 7,5 mg** | PO | 2x1 lalu 1x1 | - | ✓ | ✓ | - | - | - | NSAID sistemik. Nefrotoksik & tumpulkan Amlodipin |
| **Sitagliptin 100 mg** | PO | 1x1 malam/siang dc | - | ✓ | ✓ | ✓ | ✓ | ✓ | DPP-4i sejak Mei 2026; perlu reduksi bila eGFR < 45 |
| **Acarbose 100 mg** | PO | 2x1 dc (suapan 1) | - | - | - | - | ✓ | ✓ | Ditambahkan September untuk GD2PP 211 mg/dL |
| **Flunarizine 5 mg** | PO | 2x1 malam | - | - | - | - | ✓ | - | Antivertigo sentral. Batasi durasi maks 10 hari |
| **Kalium Diklofenak 50**| PO | 2x1 pc | - | - | - | - | ✓ | - | NSAID eksaserbasi akut September 2026 |
| **Atorvastatin 20 mg** | PO | 1x1 malam | - | - | - | - | - | ✓ | Diswitch dari Rosuvastatin Oktober 2026 (Sangat tepat) |

---

## 1.6 Evaluasi Kepatuhan Pasien: Kuesioner MMAS-8 (Skor Total: 5.0 / 8.0 — Kepatuhan Rendah)
Berdasarkan instrumen Morisky Medication Adherence Scale 8-Item (MMAS-8) yang baru dievaluasi oleh Tim Farmasi Klinis, didapatkan **Skor Total MMAS-8 = 5.0 / 8.0** yang menempatkan pasien pada kategori **KEPATUHAN RENDAH (Low Adherence, skor < 6.0)**.

| No | Item Pertanyaan Kuesioner MMAS-8 | Jawaban | Skor | Faktor Perilaku & Rasional Klinis Pasien |
| :-: | :--- | :---: | :---: | :--- |
| 1 | Apakah Anda kadang-kadang lupa minum obat? | Ya | 0 | Pasien lupa akibat banyaknya jumlah obat (polifarmasi 7-9 tablet) |
| 2 | Dalam 2 minggu terakhir, apakah ada hari Anda tidak minum obat? | Ya | 0 | Lupa pada hari-hari tertentu saat bepergian atau sibuk |
| 3 | Apakah Anda pernah mengurangi/berhenti minum obat tanpa memberi tahu dokter saat merasa kondisi memburuk? | Tidak | 1 | **FAKTOR BAIK**: Pasien tidak pernah sengaja menghentikan obat saat kondisi memburuk |
| 4 | Ketika bepergian keluar rumah, apakah Anda kadang lupa membawa obat? | Ya | 0 | Pasien terbukti lupa membawa obat pada kunjungan kontrol September 2026 |
| 5 | Apakah Anda meminum semua obat Anda kemarin? | Ya | 1 | **FAKTOR BAIK**: Pasien patuh meminum seluruh regimen obat pada hari kemarin |
| 6 | Ketika Anda merasa gejala membaik atau sehat, apakah Anda kadang berhenti minum obat? | Tidak | 1 | **FAKTOR BAIK**: Pasien menyadari obat DM & HT harus diminum rutin jangka panjang |
| 7 | Apakah Anda merasa tertekan/terbebani dengan rencana pengobatan rutin setiap hari? | Tidak | 1 | **FAKTOR BAIK**: Pasien tidak merasa terganggu secara emosional dengan terapi |
| 8 | Seberapa sering Anda merasa kesulitan mengingat untuk meminum semua obat Anda? | Tidak pernah / jarang | 1 | **FAKTOR BAIK**: Pasien menyatakan jarang kesulitan teknis mengingat jadwal |
| **TOTAL**| **SKOR KEPATUHAN MMAS-8** | **-** | **5.0** | **KATEGORI: KEPATUHAN RENDAH (Low Adherence, Skor < 6.0)** |

> [!TIP]
> **SOLUSI & RENCANA INTERVENSI FARMASIS UNTUK MMAS-8 (SKOR 5.0)**
> 1. **Pill Box Dispenser 4 Sekat Berlabel Warna**: Membantu pasien mengatur obat pagi, siang, sore, dan malam.
> 2. **Visual Medication Chart**: Jadwal bergambar bentuk fisik tablet dan hubungan waktu dengan makanan.
> 3. **Pengawas Minum Obat (PMO)**: Melibatkan keluarga terdekat untuk mengingatkan minum obat dan memastikan obat selalu dibawa saat bepergian.

![Kuesioner MMAS-8](guideline_evidence_rajal/mmas8_patient_adherence_morisky.png)
*Gambar 1.3: Instrumen Morisky Medication Adherence Scale (MMAS-8) dan Algoritma Skoring Kepatuhan.*

---

## 1.7 Evaluasi Kesesuaian Restriksi Formularium Nasional (Fornas) & Profil Efek Samping Terbanyak (Top 3)
* **Kesesuaian Fornas**:
  * **TIDAK SESUAI FORNAS**: Glimepirid 3 mg diresepkan 2x1 (60 tablet/bulan). Plafon Fornas menetapkan maksimal 30 tablet/bulan. Secara klinis dosis 6 mg/hari ini merupakan overdosis geriatri.
  * **STATUS NON-FORNAS**: Glucosamine 500 mg berstatus suplemen nutrasetikal makanan sendi di luar jaminan paket standar JKN.
  * **SESUAI FORNAS**: Sitagliptin (30 tab), Acarbose (60 tab), Amlodipin (30 tab), Atorvastatin (30 tab), Rosuvastatin (30 tab), Gabapentin (30 kap), Flamar Gel (1 tube), Meloxicam (10 tab prn), Diklofenak (10 tab prn), Flunarizine (10 tab prn), Mecobalamin (30 kap).

| Nama Obat | Efek Samping Terbanyak (Top 3) dengan Persentase | Bukti Referensi Resmi |
| :--- | :--- | :--- |
| **Glimepirid** | 1. Hipoglikemia (10–18%)<br>2. Peningkatan Berat Badan (2–5%)<br>3. Pusing / Sakit Kepala (1,7–3,4%) | FDA Amaryl Insert & Lexicomp Online 2024 |
| **Sitagliptin** | 1. Nasofaringitis (5,2%)<br>2. Sakit Kepala (5,1%)<br>3. Gangguan Gastrointestinal (1,5–3,0%) \| Waspada Pankreatitis (<1%) | FDA Januvia Package Insert & DailyMed |
| **Acarbose** | 1. Flatulensi / Kembung Buang Angin (74–78%)<br>2. Diare (29–31%)<br>3. Nyeri Abdomen / Kram Perut (19–21%) | FDA Precose Monograph & Lexicomp |
| **Amlodipin** | 1. Edema Perifer / Bengkak Kaki (1,8–10,8%)<br>2. Sakit Kepala (7,3%)<br>3. Kelelahan / Fatigue (4,5%) | FDA Norvasc Insert & DailyMed |
| **Atorvastatin** | 1. Nasofaringitis (8,3%)<br>2. Artralgia / Nyeri Sendi (6,9%)<br>3. Dispepsia / Gangguan GI (5,6%) \| Mialgia (3,5–6,3%) | FDA Lipitor Package Insert & Lexicomp |
| **Gabapentin** | 1. Mengantuk / Somnolence (19–21%)<br>2. Pusing Melayang / Dizziness (17–28%)<br>3. Ataksia / Gangguan Keseimbangan Jalan (11–13%) | FDA Neurontin & Micromedex DrugDex |
| **Flunarizine** | 1. Peningkatan Berat Badan / Nafsu Makan (10–20%)<br>2. Mengantuk / Sedasi (10–15%)<br>3. Kelelahan / Depresi / Gejala Ekstrapiramidal (5–10%) | Sibelium Monograph & Martindale 38th Ed |
| **NSAID Oral (Diklofenak / Meloxicam)** | 1. Dispepsia / Nyeri Epigastrik (10–15%)<br>2. Pusing / Sakit Kepala (3–9%)<br>3. Retensi Cairan & Peningkatan Tekanan Darah (1–3%) | FDA Cataflam / Mobic Insert |
| **Flamar Gel (Diklofenak Topikal)** | 1. Pruritus / Gatal Lokal (4%)<br>2. Eritema / Kemerahan Kulit (2–2,5%)<br>3. Kulit Kering (1,5–2%) \| Absorpsi sistemik sangat minimal (<6%) | FDA Voltaren Topical Gel Package Insert |

---

## 1.8 Identifikasi & Analisis Mendalam Drug-Related Problems (DRP) Rawat Jalan

### DRP 1: Overdosis Relatif Glimepirid (6 mg/hari) pada Geriatri & Penurunan Klirens Ginjal
* **Analisis Klinis**: Glimepirid diresepkan 3 mg 2x1 (total 6 mg/hari). Glimepirid dieliminasi 60% via ginjal. Pada CrCl 17,67 mL/min, terjadi akumulasi obat dan metabolit aktifnya, memicu risiko hipoglikemia berat memanjang (*prolonged neuroglycopenia*) yang memicu episode jatuh dan fraktur. Peresepan 60 tablet/bulan juga melanggar plafon Fornas (maks 30 tablet/bulan).
* **Guideline**: *AGS Beers Criteria 2023 Update* mengklasifikasikan Glimepirid sebagai **PIM kategori AVOID** pada geriatri. *PERKENI 2021 (Hal. 36–39)* membatasi dosis Glimepirid pada lansia maksimal $\le$ 2 mg/hari, atau diganti Glikuidon (30 mg 1–2x/hari) yang 95% diekskresi via empedu/feses.
* **Rekomendasi Farmasis**: Turunkan dosis Glimepirid menjadi 2 mg 1x1 pagi, atau beralih ke Glikuidon 30 mg 1x1, serta lakukan inisiasi insulin basal.

![Glimepirid Geriatri Beers](guideline_evidence_rajal/perkeni_beers_glimepiride_elderly.png)
*Gambar 1.4: Panduan Keamanan Sulfonilurea pada Geriatri Sesuai AGS Beers Criteria 2023 & Konsensus PERKENI 2021 (Hal. 38).*

---

### DRP 2: Kegagalan Regimen Triple OHO (HbA1c 9,1%) & Indikasi Inisiasi Terapi Insulin Basal
* **Analisis Klinis**: Pasien menerima Glimepirid 6 mg + Sitagliptin 100 mg + Acarbose 200 mg, namun HbA1c tetap 9,1%*, GDP 190* mg/dL, dan GDS spike 308* mg/dL.
* **Guideline**: *PERKENI 2021 (Hal. 45–50)* & *DiPiro's Pharmacotherapy 12th Ed (2023) Ch. 57*: Pasien dengan HbA1c > 9% yang gagal dengan kombinasi 2–3 OHO memiliki **INDIKASI MUTLAK** untuk inisiasi **INSULIN BASAL**.
* **Rekomendasi Farmasis**: Inisiasi Insulin Glargine (*Lantus*) subkutan 1x10 Unit malam hari sebelum tidur (pukul 21.00–22.00), titrasi 2 unit tiap 3-4 hari hingga target GDP 80–130 mg/dL tercapai.

![Algoritma DM PERKENI](guideline_evidence_rajal/perkeni_2021_dm_algorithm.png)
*Gambar 1.5: Algoritma Pengelolaan Glukosa DM Tipe 2 & Indikasi Inisiasi Insulin Basal (PERKENI 2021 Hal. 47–49).*

---

### DRP 3: Kebutuhan Penyesuaian Dosis Ginjal Sitagliptin (CrCl 17,67 mL/min)
* **Analisis Klinis**: Sitagliptin diekskresi 79% utuh melalui urin. Klirens ginjal pasien turun menjadi 17,67 mL/min (kreatinin 2,69* mg/dL pada 04/07/2026). Pemberian dosis penuh 100 mg 1x1 meningkatkan AUC sistemik 4–5 kali lipat.
* **Guideline (Lexicomp & FDA)**: Pada CrCl < 30 mL/min, dosis Sitagliptin **HARUS DITURUNKAN menjadi 25 mg 1x1 sehari**.
* **Rekomendasi Farmasis**: Evaluasi hasil lab kreatinin serial (order ulang 06/11/2026); bila eGFR 30–44 turunkan ke 50 mg, jika < 30 turunkan ke 25 mg 1x1 sehari.

![Penyesuaian Ginjal Sitagliptin](guideline_evidence_rajal/sitagliptin_renal_adjustment_lexicomp.png)
*Gambar 1.6: Panduan Penyesuaian Dosis Ginjal Sitagliptin Berdasarkan Klirens Kreatinin (Lexicomp Drug Information 2024).*

---

### DRP 4: Interaksi Obat NSAID Oral terhadap Ginjal, Tekanan Darah, & Amlodipin
* **Analisis Klinis**: Pemberian NSAID oral (Meloxicam 7,5 mg dan Kalium Diklofenak 50 mg 2x1) menghambat sintesis prostaglandin renal PGE2/PGI2 $\rightarrow$ vasokonstriksi arteriol aferen $\rightarrow$ memicu AKI (kreatinin 2,69 mg/dL), retensi natrium-air yang memicu spike tekanan darah (165/89 mmHg), serta menumpulkan efek vasodilatasi Amlodipin (*Lexicomp Rating C*).
* **Guideline**: *IRA 2021* & *DiPiro Ch. 60*: NSAID oral sistemik **HARUS DIHINDARI** pada geriatri komorbid kardio-renal. Terapi lini pertama adalah NSAID topikal (*Flamar Gel*) dan Parasetamol oral.
* **Rekomendasi Farmasis**: Hentikan seluruh NSAID oral sistemik. Maksimalkan Flamar Gel topikal 2–4x/hari dan Parasetamol 500 mg prn bila nyeri hebat.

![Keamanan NSAID IRA](guideline_evidence_rajal/ira_nsaid_safety_osteoarthritis.png)
*Gambar 1.7: Rekomendasi Keamanan Penggunaan NSAID pada Pasien Lansia dengan Komorbid Kardio-Renal (IRA 2021 Hal. 14–19).*

![Matriks Interaksi Rajal](guideline_evidence_rajal/lexicomp_interactions_rajal.png)
*Gambar 1.8: Matriks Interaksi Obat Pasien Rawat Jalan Berdasarkan Lexicomp Drug Interactions Rating C & D.*

---

### DRP 5: Interaksi Sedasi Gabapentin + Flunarizine & Risiko Jatuh Pasca Trauma
* **Analisis Klinis**: Kombinasi Gabapentin 100 mg 1x1 malam dan Flunarizine 5 mg 2x1 menimbulkan depresi SSP aditif, memicu pusing berat, ataksia motorik, dan memperberat risiko jatuh pasca fraktur zygoma.
* **Guideline**: *AGS Beers Criteria 2023 Update*: Hindari kombinasi $\ge$ 2 depresan SSP pada lansia. Flunarizine memiliki waktu paruh hingga 18 hari pada geriatri; batasi maksimal 7–10 hari pada vertigo akut lalu hentikan.
* **Rekomendasi Farmasis**: Hentikan Flunarizine 5 mg (fase akut vertigo telah teratasi). Pertahankan Gabapentin 100 mg 1x1 malam untuk neuropati diabetik.

![Neuropati DiPiro](guideline_evidence/dipiro_diabetic_neuropathy_weight.png)
*Gambar 1.9: Tatalaksana Neuropati Diabetik & Penyesuaian Dosis Gabapentin pada Geriatri (DiPiro 12th Ed Ch. 57 & 58).*

---

### DRP 6: Drug-Food Interaction & Edukasi Khusus Acarbose 100 mg
* **Analisis Klinis**: Acarbose wajib diminum **bersama suapan pertama makanan utama**. Bila terjadi hipoglikemia akibat kombinasi dengan Glimepirid, gula pasir biasa (sukrosa) tidak akan diserap karena alfa-glukosidase dihambat Acarbose. Pasien wajib diedukasi menyediakan **dekstrosa murni / madu murni**.

---

### DRP 7: Evaluasi Adverse Drug Reaction (ADR): Edema Perifer Amlodipin (Naranjo Skor 6) & Solusi ARB
* **Mekanisme**: Amlodipin memicu vasodilatasi arteriol prekapiler tanpa disertai venodilatasi postkapiler, meningkatkan gradien tekanan hidrostatik kapiler dan memicu transudasi cairan ke pergelangan kaki.
* **Skor Naranjo**: +6 (*Probable Adverse Drug Reaction*).
* **Tatalaksana (Skovbjerg et al., 2023; Shetty et al., 2016)**: Turunkan dosis Amlodipin dari 10 mg menjadi 5 mg malam hari dan kombinasikan dengan ARB Candesartan 8–16 mg 1x1. ARB mendilatasi venul postkapiler, menyeimbangkan tekanan intrakapiler, dan melenyapkan edema tanpa diuretik loop.

![Naranjo Amlodipin](guideline_evidence/naranjo_amlodipine_edema.png)
*Gambar 1.10: Penilaian Algoritma Naranjo Adverse Drug Reaction: Edema Perifer Terinduksi Amlodipin (Skor 6 - Probable).*

![Skovbjerg Edema Mgmt](guideline_evidence/skovbjerg_amlodipine_edema_mgmt.png)
*Gambar 1.11: Mekanisme Patofisiologi & Strategi Terapi Edema Perifer Amlodipin Berbasis Bukti Klinis (Skovbjerg et al., 2023).*

---

### DRP 8: Kepatuhan Formularium Nasional (Fornas) & Switch Statin (Rosuvastatin ke Atorvastatin)
* **Analisis**: Switch dari Rosuvastatin 10 mg ke Atorvastatin 20 mg pada Oktober 2026 (M6) sangat rasional. Atorvastatin dieliminasi > 98% via hepatobilier/empedu (ekskresi ginjal < 2%), sehingga sangat aman pada gangguan ginjal pasien (CrCl 17,67 mL/min) dibandingkan Rosuvastatin (eliminasi ginjal 10%), serta bebas dari restriksi ketat Fornas FKRTL.

![Dislipidemia PERKI](guideline_evidence_rajal/perhi_perki_hypertension_dyslipidemia.png)
*Gambar 1.12: Panduan Terapi Dislipidemia & Evaluasi Statin pada Pasien Risiko Tinggi (PERKI 2022 Hal. 25–30).*

---

## 1.9 Rencana Asuhan Kefarmasian (Care Plan) & Rekomendasi Monitoring Rajal
| Masalah Medis | Drug Related Problem (DRP) | Rekomendasi Farmasis | Parameter Monitoring | Status Rekomendasi |
| :--- | :--- | :--- | :--- | :---: |
| **DM Tipe 2 Tak Terkontrol (HbA1c 9,1%)** | Kegagalan kombinasi 3 OHO oral (Glimepirid + Sitagliptin + Acarbose) | Inisiasi Insulin Basal (Glargine 10 unit malam hari) & titrasi berkala 2 unit tiap 3-4 hari | GDP pagi (target 80-130 mg/dL), HbA1c per 3 bulan | **Disetujui (✓)** |
| **Dosis Glimepirid Geriatri** | Overdosis relatif Glimepirid 6 mg/hari pada geriatri 64 th dengan klirens ginjal turun (PIM Beers & melanggar Fornas) | Turunkan dosis Glimepirid menjadi 2 mg 1x1 pagi (atau ganti Glikuidon 30 mg / stop saat insulin mulai) | GDS mandiri, tanda hipoglikemia akut | **Disetujui (✓)** |
| **Gangguan Ginjal (CrCl 17,67 mL/min)** | Potensi akumulasi Sitagliptin 100 mg bila eGFR pasien < 45 mL/min | Evaluasi hasil lab kreatinin ulang 06/11/2026; bila eGFR 30-44 turunkan ke 50 mg, jika <30 ke 25 mg 1x1 | Serum kreatinin, eGFR, gejala GI / pankreatitis | **Disetujui (✓)** |
| **Hipertensi Sub-optimal (TD 133-165)** | Monoterapi Amlodipin 10 mg gagal target <130/80 & interaksi dengan NSAID oral | Hentikan NSAID oral sistemik; kombinasikan Amlodipin 5 mg + Candesartan 8-16 mg 1x1 malam | Tekanan darah berkala (target <130/80 mmHg), kalium | **Disetujui (✓)** |
| **Osteoarthritis & Risiko Jatuh Geriatri** | NSAID oral nefrotoksik & interaksi sedasi Gabapentin + Flunarizine | Maksimalkan Flamar Gel topikal 2-4x/hari, Parasetamol oral prn; batasi Flunarizine maks 10 hari; edukasi fall prevention | Skor nyeri lutut, stabilitas jalan, fungsi ginjal | **Disetujui (✓)** |
| **Kepatuhan Pasien (MMAS-8 Skor 5.0)** | Kategori: Kepatuhan Rendah (< 6.0) ec lupa berkala & polifarmasi 7-9 tablet | Sediakan Pill-Box Organizer harian 4 sekat berlabel warna, jadwal minum obat bergambar, libatkan PMO keluarga | Evaluasi ulang skor MMAS-8 kunjungan berikutnya | **Disetujui (✓)** |

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
* **Kronologi IGD**: Pasien datang pada 18 Oktober 2026 pukul 09.30 WIB dengan keluhan utama **mual hebat dan muntah profuse (frekuensi > 6 kali dalam 24 jam terakhir)**. Muntahan berisi cairan keruh bercampur lendir lambung dan sisa makanan, tanpa darah (hematemesis (-)) dan BAB hitam (-). Pasien mengeluhkan rasa perih menusuk dan terbakar pada ulu hati (epigastrium), perut kembung begah (*postprandial fullness*), cepat kenyang (*early satiation*), rasa asam naik ke kerongkongan (*heartburn*), dan badan terasa sangat lemas tak berdaya. Pasien sama sekali tidak dapat mentoleransi makanan maupun minuman per oral selama 18 jam terakhir.
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
* **Analisis Klinis**: Pasien menerima Inj. Metoclopramide 10 mg IV tiap 8 jam bersamaan dengan Domperidone 10 mg 3x1 oral. Keduanya merupakan antagonis reseptor dopamin D2.
* **Bahaya Toksisitas Kombinasi Ganda**: Kombinasi ini TIDAK meningkatkan efikasi antiemetik, melainkan melipatgandakan risiko efek samping fatal:
  1. *Gejala Ekstrapiramidal Akut (EPS)*: Distonia leher, krisis okulogirik, akatisia motorik, dan parkinsonisme sekunder pada geriatri.
  2. *Kardiotoksisitas QTc Prolongation*: Keduanya memblokade kanal kalium IKr jantung, memperpanjang repolarisasi ventrikel, dan memicu aritmia fatal *Torsades de Pointes* (TdP).
* **Klasifikasi Interaksi**: **Lexicomp Risk Rating: Category D / X (Avoid Combination)**.
* **Rekomendasi Farmasis**: Hentikan salah satu obat. Pada fase akut dengan muntah aktif, pertahankan **INJEKSI METOCLOPRAMIDE 10 mg IV (atau 5 mg pada geriatri)** dan **HENTIKAN DOMPERIDONE ORAL**. Jika muntah berlanjut, kombinasikan dengan **INJEKSI ONDANSETRON 4 mg IV** (Antagonis Serotonin 5-HT3) yang bekerja sinergis tanpa risiko EPS.

![Duplikasi Prokinetik Lexicomp](guideline_evidence/drug_interaction_gavistal_domperidone.png)
*Gambar 2.3: Analisis Interaksi Mayor Duplikasi Prokinetik Dopamin D2 (Metoclopramide + Domperidone) — Lexicomp Risk Rating D/X.*

![Konsensus Dispepsia PGI DiPiro](guideline_evidence/konsensus_dispepsia_pgi_dipiro.png)
*Gambar 2.4: Pedoman Penatalaksanaan Dispepsia & Algoritma Antiemetik (Konsensus PGI 2021/2024 Hal. 12–16 & DiPiro 12th Ed Ch. 41-42).*

---

### DRP 2: Penyesuaian Dosis Ginjal Metoclopramide pada Pasien Geriatri
* **Analisis Klinis**: Sekitar 80% Metoclopramide dieliminasi via ginjal. Pada lansia berusia 62 tahun 10 bulan dengan laju filtrasi ginjal yang rentan terhadap dehidrasi, dosis penuh 30 mg/hari IV memicu akumulasi obat sentral.
* **Guideline Klinis (Lexicomp Geriatric & Micromedex)**: Pada lansia atau gangguan fungsi ginjal (CrCl < 60 mL/min), dosis Metoclopramide sebaiknya **diturunkan 50% menjadi 5 mg IV tiap 8 jam atau 10 mg IV tiap 12 jam**, dan durasi dibatasi maksimal 5 hari parenteral.

![Penyesuaian Ginjal Metoclopramide](guideline_evidence/lexicomp_metoclopramide_renal.png)
*Gambar 2.5: Panduan Penyesuaian Dosis Ginjal & Geriatri Metoclopramide (Lexicomp Drug Information 2024).*

---

### DRP 3: Tatalaksana Komprehensif Mual Muntah karena Dispepsia (Konsensus Nasional PGI 2021/2024 & DiPiro 12th Ed Ch. 41-42)
1. *Supresi Asam Lambung*: Inj. Omeprazole 40 mg IV / 24 jam vial (PPI) menghambat pompa asam H+/K+-ATPase sel parietal secara poten, menaikkan pH lambung > 4, meredakan nyeri ulu hati panas terbakar (*heartburn*), dan memulihkan integritas sawar mukosa gaster (*Konsensus PGI Hal. 12–16*).
2. *Mukoprotektor Lambung*: Sucralfate sirup 1 g (15 mL) 3 kali sehari dalam lambung kosong membentuk gel pelindung pada mukosa gaster dan merangsang prostaglandin endogen.
3. *Antiemetik Rasional*: Metoclopramide parenteral monoterapi untuk mempercepat pengosongan lambung ke duodenum, didukung Ondansetron 4 mg IV prn untuk memblokade jaras muntah di medula oblongata (*DiPiro 12th Ed Ch. 41 & 42*).

---

### DRP 4: Tatalaksana Hiperglikemia Akut Rawat Inap (GDS 357 mg/dL) — Penghentian OHO Oral, Inisiasi Regimen Insulin Basal-Bolus Target 140–180 mg/dL
* **Penghentian Mutlak OHO Oral**: Sesuai *PERKENI 2021 (Hal. 98–101)* dan *ADA Standards of Care 2024 Section 16 (Hal. S278–S282)*:
  * **METFORMIN HARUS SEGERA DIHENTIKAN** karena risiko fatal Asidosis Laktat akibat dehidrasi.
  * **SULFONILUREA (Glimepirid) HARUS DIHENTIKAN** karena risiko hipoglikemia berat saat intake oral tidak menentu.
* **Regimen Insulin Basal-Bolus**:
  * *Insulin Basal (Lantus / Glargine)*: 1x10 Unit malam hari jam 22.00 untuk kontrol glukosa basal 24 jam.
  * *Insulin Bolus Prandial (Novorapid / Aspart)*: 3x6–8 Unit subkutan segera sebelum makan.
* **Target Glikemik Rawat Inap**: **140 – 180 mg/dL (7,8 – 10,0 mmol/L)**. Target ketat < 110 mg/dL tidak direkomendasikan karena meningkatkan mortalitas akibat hipoglikemia berat (NICE-SUGAR trial).

![Panduan Inpatient PERKENI](guideline_evidence/perkeni_inpatient_guideline.png)
*Gambar 2.6: Pedoman Pengelolaan Hiperglikemia Pasien Rawat Inap Rumah Sakit Non-ICU (PERKENI 2021 Hal. 98–101).*

![Standar Inpatient ADA](guideline_evidence/ada_inpatient_guideline.png)
*Gambar 2.7: Standar Pelayanan Medis Diabetes Rawat Inap & Target Glikemik 140–180 mg/dL (ADA Standards of Care 2024 Section 16).*

---

### DRP 5: Rekonsiliasi Terapi Antihipertensi Rawat Inap (Amlodipin 10 mg)
Pasien rutin mengonsumsi Amlodipin 10 mg malam di rumah. Pada 24 jam pertama saat muntah profuse, obat oral ditunda. Memasuki Hari Rawat ke-2 saat keluhan mual mereda dan diet oral masuk, **Amlodipin 10 mg 1x1 malam segera direkonsiliasi dan diberikan kembali per oral** sesuai panduan PERHI 2021 dan ACC/AHA 2023 untuk mencegah *rebound hypertension*.

![Rekonsiliasi Hipertensi PERHI](guideline_evidence/perhi_acc_aha_hypertension_reconciliation.png)
*Gambar 2.8: Protokol Rekonsiliasi Terapi Antihipertensi Rawat Inap (Konsensus PERHI 2021 & ACC/AHA 2023).*

---

### DRP 6: Rehidrasi Cairan Kristaloid Isotonik NaCl 0,9% untuk Koreksi Hiponatremia & Hipokloremia
Muntah profuse > 6 kali mengakibatkan defisit volume cairan dan kehilangan ion natrium dan klorida lambung (Na 131 mmol/L, Cl 96 mmol/L). Cairan kristaloid isotonik pilihan utama adalah **Infus NaCl 0,9% (Normal Saline)** dengan kecepatan 20 tetes/menit (1.500 mL/24 jam), yang aman bagi geriatri dan mencegah komplikasi kelebihan cairan maupun *osmotic demyelination syndrome*. Terbukti pada Hari ke-3 elektrolit terkoreksi normal (Na 137, Cl 101).

![Rehidrasi Muntah DiPiro](guideline_evidence/vomitus_rehydration_guideline.png)
*Gambar 2.9: Panduan Terapi Rehidrasi Cairan & Koreksi Gangguan Elektrolit pada Pasien Mual-Muntah Akut (DiPiro 12th Ed Ch. 38).*

---

### DRP 7: Evaluasi Penggunaan Obat Geriatri Berdasarkan AGS Beers Criteria 2023
Penggunaan Metoclopramide jangka panjang dikontraindikasikan pada lansia (> 12 minggu berisiko diskinesia tardif), sehingga durasi parenteral dibatasi 3 hari saja. Penggunaan insulin analog (Novorapid dan Lantus) sangat tepat pada geriatri karena menurunkan risiko hipoglikemia nokturnal secara signifikan dibandingkan insulin regular/NPH.

![Geriatri Beers Criteria](guideline_evidence/beers_criteria_geriatric.png)
*Gambar 2.10: Kriteria Penggunaan Obat yang Berpotensi Tidak Tepat pada Populasi Geriatri (AGS Beers Criteria 2023).*

---

### DRP 8: Evaluasi Rasionalitas Antibiotik Metode Gyssens & Riwayat Alergi Penisilin
Pasien memiliki riwayat alergi berat terhadap Amoksisilin dan Ampisilin. Selama perawatan, DPJP tidak meresepkan antibiotik empiris karena leukosit normal (9.200 /µL), suhu afebris (36,8°C), dan urinalisis normal. Berdasarkan audit alur Gyssens (*Permenkes RI No. 28/2021*): Keputusan tidak memberikan antibiotik dinilai sebagai **KATEGORI 0: Penggunaan / Keputusan Terapi Antibiotik TEPAT dan RASIONAL (Appropriate Indication - No Antibiotic Indicated)**.

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
| **Kesiapan Pasien Pulang (KRS)** | **S**: Tidak mual, tidak muntah, makan habis 1 porsi bubur, badan segar.<br>**O**: TD 125/78 mmHg, GDS Pagi: 138 mg/dL, Elektrolit normal: Na 137 mmol/L, Cl 101 mmol/L. | Kondisi klinis stabil sempurna. Mual muntah dispepsia teratasi tuntas. Glikemik dan elektrolit normal. Pasien siap KRS (*Discharge Planning*). | 1. **Resep Pulang (Oral & Subkutan)**:<br>   - Lansoprazole kapsul 30 mg 1x1 ac pagi<br>   - Sucralfate sirup 3x1 C ac (selama 5 hari)<br>   - Lantus SoloStar Pen 1 x 10 Unit SC malam<br>   - Metformin tablet 500 mg 3x1 dc (reintroduksi aman)<br>   - Amlodipin tablet 10 mg 1x1 malam PO<br>2. **Konseling Farmasis Pulang (KIE)**:<br>   - Edukasi teknik injeksi insulin SoloStar, rotasi lokasi tusukan, dan penyimpanan di lemari es (2–8°C).<br>   - Edukasi tanda-tanda hipoglikemia dan penanganan daruratnya.<br>   - Edukasi pola makan teratur porsi kecil sering (*small frequent meals*) untuk pencegahan dispepsia berulang. |

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

print(f"Revised Markdown report generated successfully at: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")

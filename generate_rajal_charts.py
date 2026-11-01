import matplotlib.pyplot as plt
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

out_dir = r"D:\FILE NINIS\guideline_evidence_rajal"
os.makedirs(out_dir, exist_ok=True)

# 1. Glucose & HbA1c Chart
dates_gds = ["27/03", "27/04", "29/05", "29/06 (GDP)", "04/07 (IGD)", "05/07", "06/07", "05/08", "07/09 (GDP)", "07/10 (GDP)"]
vals_gds = [158, 160, 252, 169, 244, 308, 83, 160, 190, 151]

plt.figure(figsize=(10, 4.8), dpi=300)
plt.plot(dates_gds, vals_gds, marker='o', color='#dc2626', linewidth=2.5, markersize=7, label='Kadar Glukosa Darah (mg/dL)')
plt.axhline(y=130, color='#16a34a', linestyle='--', linewidth=1.5, label='Batas Atas Target GDP PERKENI (<130 mg/dL)')
plt.axhline(y=180, color='#f59e0b', linestyle=':', linewidth=1.5, label='Batas Target GD2PP / GDS Postprandial (<180 mg/dL)')

# Highlight HbA1c point on 29/05
plt.annotate('HbA1c = 9.1%\n(Uncontrolled)', xy=('29/05', 252), xytext=('29/05', 285),
             arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6),
             fontweight='bold', color='#991b1b', fontsize=9, ha='center',
             bbox=dict(boxstyle="round,pad=0.3", fc="#fee2e2", ec="#dc2626", lw=1))

# Highlight Fall Trauma on 04/07
plt.annotate('Trauma CKR (Jatuh)\nSpike GDS 308 mg/dL', xy=('05/07', 308), xytext=('05/07', 330),
             fontweight='bold', color='#7f1d1d', fontsize=9, ha='center',
             bbox=dict(boxstyle="round,pad=0.3", fc="#fef2f2", ec="#b91c1c", lw=1))

plt.title('Tren Kadar Glukosa Darah & HbA1c Pasien Ny. Sri Wisraya (6 Bulan Terakhir)', fontsize=13, fontweight='bold', pad=14, color='#1e3a8a')
plt.xlabel('Tanggal Kunjungan / Pemeriksaan', fontsize=10, fontweight='bold')
plt.ylabel('Kadar Glukosa (mg/dL)', fontsize=10, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right', fontsize=9)
plt.ylim(50, 370)
plt.tight_layout()
chart_path1 = os.path.join(out_dir, "rajal_glucose_trend.png")
plt.savefig(chart_path1)
plt.close()
print(f"Generated: {chart_path1}")

# 2. Blood Pressure Trend Chart
dates_bp = ["27/04", "29/05", "29/06", "05/08", "07/09", "07/10"]
systolic = [130, 138, 156, 165, 141, 133]
diastolic = [80, 76, 85, 89, 80, 77]

plt.figure(figsize=(9, 4.5), dpi=300)
plt.plot(dates_bp, systolic, marker='s', color='#b91c1c', linewidth=2.5, markersize=7, label='Sistole (mmHg)')
plt.plot(dates_bp, diastolic, marker='^', color='#2563eb', linewidth=2.2, markersize=7, label='Diastole (mmHg)')
plt.axhline(y=130, color='#b91c1c', linestyle='--', alpha=0.7, label='Target Sistole PERHI (<130 mmHg)')
plt.axhline(y=80, color='#2563eb', linestyle='--', alpha=0.7, label='Target Diastole PERHI (<80 mmHg)')

# Highlight spike when NSAID added
plt.annotate('Eksaserbasi Nyeri & NSAID\nSpike TD 165/89 mmHg', xy=('05/08', 165), xytext=('05/08', 178),
             arrowprops=dict(facecolor='black', shrink=0.08, width=1, headwidth=6),
             fontweight='bold', color='#7f1d1d', fontsize=9, ha='center',
             bbox=dict(boxstyle="round,pad=0.3", fc="#fef2f2", ec="#b91c1c", lw=1))

plt.title('Tren Tekanan Darah Ny. Sri Wisraya Selama Terapi Monoterapi Amlodipin 10 mg', fontsize=12, fontweight='bold', pad=14, color='#1e3a8a')
plt.xlabel('Tanggal Kunjungan Kontrol Poli Penyakit Dalam', fontsize=10, fontweight='bold')
plt.ylabel('Tekanan Darah (mmHg)', fontsize=10, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='lower right', fontsize=8.5)
plt.ylim(65, 195)
plt.tight_layout()
chart_path2 = os.path.join(out_dir, "rajal_bp_trend.png")
plt.savefig(chart_path2)
plt.close()
print(f"Generated: {chart_path2}")

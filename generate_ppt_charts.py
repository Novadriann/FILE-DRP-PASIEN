import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs(r"d:\FILE NINIS\ppt_assets", exist_ok=True)

# 1. TTV Line Chart (Matching Slide 5 & 27 style)
dates = ['IGD 14/10', '15/10', '16/10', '17/10', '18/10 (Pagi)', '18/10 (Siang)']
sistole = [101, 149, 125, 133, 144, 122]
diastole = [80, 70, 66, 76, 81, 82]
nadi = [105, 92, 95, 90, 94, 88]
suhu = [36.0, 36.5, 36.4, 36.0, 37.5, 36.0]
rr = [22, 20, 20, 20, 20, 20]
spo2 = [96, 96, 95, 99, 99, 99]
nyeri = [0, 0, 0, 0, 0, 0]

plt.figure(figsize=(10, 5), dpi=200)
plt.plot(dates, sistole, marker='o', color='#2563eb', label='TD Sistole (<140)', linewidth=2.5)
plt.plot(dates, diastole, marker='o', color='#dc2626', label='TD Diastole (<90)', linewidth=2.5)
plt.plot(dates, nadi, marker='o', color='#eab308', label='Nadi (60-100)', linewidth=2.5)
plt.plot(dates, suhu, marker='o', color='#16a34a', label='Suhu (<37.5)', linewidth=2)
plt.plot(dates, rr, marker='o', color='#ea580c', label='RR (12-20)', linewidth=2)
plt.plot(dates, spo2, marker='o', color='#06b6d4', label='SpO2 (≥95%)', linewidth=2)
plt.plot(dates, nyeri, marker='o', color='#1e3a8a', label='Nyeri', linewidth=2)

plt.title('PEMERIKSAAN TANDA-TANDA VITAL PASIEN NY. SUNARTI', fontsize=13, fontweight='bold', pad=15)
plt.ylim(0, 160)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.22), ncol=7, fontsize=8.5, frameon=True)
plt.tight_layout()
plt.savefig(r"d:\FILE NINIS\ppt_assets\ttv_chart.png", bbox_inches='tight')
plt.close()

# 2. Glucose Trend Chart
dates_glu = ['14/10 (GDS)', '15/10 (GDS)', '16/10 (GDP)', '18/10 (GDP)']
glu_vals = [310, 208, 235, 298]

plt.figure(figsize=(8, 4.5), dpi=200)
bars = plt.bar(dates_glu, glu_vals, color=['#ef4444', '#f97316', '#eab308', '#b91c1c'], width=0.45, edgecolor='black', linewidth=1)
plt.axhspan(140, 180, color='#22c55e', alpha=0.25, label='Target PERKENI/ADA (140-180 mg/dL)')
plt.axhline(180, color='#15803d', linestyle='--', linewidth=1.5)
plt.axhline(140, color='#15803d', linestyle='--', linewidth=1.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 6, f'{int(yval)} mg/dL', ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.title('TREN KADAR GLUKOSA DARAH PASIEN SELAMA RAWAT INAP', fontsize=12, fontweight='bold', pad=12)
plt.ylabel('Kadar Glukosa (mg/dL)', fontsize=10, fontweight='bold')
plt.ylim(0, 360)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(loc='upper right', fontsize=9)
plt.tight_layout()
plt.savefig(r"d:\FILE NINIS\ppt_assets\glucose_chart.png", bbox_inches='tight')
plt.close()

print("Charts generated successfully!")

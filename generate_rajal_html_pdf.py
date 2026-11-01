import markdown
import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

md_path = r"D:\FILE NINIS\LAPORAN_PEMANTAUAN_TERAPI_OBAT_SRI_WISRAYA.md"
html_path = r"D:\FILE NINIS\LAPORAN_PEMANTAUAN_TERAPI_OBAT_SRI_WISRAYA.html"
pdf_path = r"D:\FILE NINIS\LAPORAN_PEMANTAUAN_TERAPI_OBAT_SRI_WISRAYA.pdf"
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

with open(md_path, "r", encoding="utf-8") as f:
    md_text = f.read()

# Convert markdown to html with table & fenced_code extensions
html_body = markdown.markdown(md_text, extensions=['tables', 'fenced_code', 'nl2br'])

html_full = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Laporan Pemantauan Terapi Obat Rawat Jalan - Ny. Sri Wisraya</title>
<style>
    @page {{
        size: A4 portrait;
        margin: 18mm 15mm 18mm 15mm;
    }}
    body {{
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
        line-height: 1.5;
        color: #1e293b;
        background-color: #f8fafc;
        margin: 0;
        padding: 30px;
    }}
    .container {{
        max-width: 960px;
        margin: 0 auto;
        background: #ffffff;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
    }}
    h1 {{
        color: #1e3a8a;
        font-size: 22px;
        font-weight: 800;
        border-bottom: 3px solid #1e3a8a;
        padding-bottom: 10px;
        margin-top: 0;
        text-align: center;
        line-height: 1.3;
    }}
    h2 {{
        color: #1e40af;
        font-size: 16px;
        font-weight: 700;
        text-align: center;
        margin-top: -5px;
        margin-bottom: 5px;
    }}
    h3 {{
        color: #475569;
        font-size: 13px;
        font-weight: 600;
        text-align: center;
        margin-top: 0;
        margin-bottom: 25px;
    }}
    h2, h3, h4 {{
        page-break-after: avoid;
    }}
    h2:not(:first-of-type) {{
        text-align: left;
        border-bottom: 2px solid #cbd5e1;
        padding-bottom: 6px;
        margin-top: 30px;
        font-size: 17px;
    }}
    h3:not(:first-of-type) {{
        text-align: left;
        color: #0f172a;
        font-size: 14px;
        margin-top: 20px;
        margin-bottom: 10px;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        margin: 14px 0 20px 0;
        font-size: 11px;
        page-break-inside: auto;
    }}
    tr {{
        page-break-inside: avoid;
        page-break-after: auto;
    }}
    th {{
        background-color: #1e3a8a;
        color: #ffffff;
        font-weight: 700;
        text-align: left;
        padding: 8px 10px;
        border: 1px solid #cbd5e1;
    }}
    td {{
        padding: 7px 10px;
        border: 1px solid #cbd5e1;
        vertical-align: top;
        color: #334155;
    }}
    tr:nth-child(even) td {{
        background-color: #f8fafc;
    }}
    blockquote {{
        background-color: #eff6ff;
        border-left: 4px solid #3b82f6;
        margin: 14px 0;
        padding: 10px 16px;
        color: #1e3a8a;
        border-radius: 0 6px 6px 0;
        font-size: 12px;
    }}
    img {{
        max-width: 100%;
        height: auto;
        border-radius: 8px;
        border: 1px solid #cbd5e1;
        margin: 12px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    hr {{
        border: 0;
        height: 1px;
        background: #e2e8f0;
        margin: 25px 0;
    }}
    p, li {{
        font-size: 12px;
        line-height: 1.6;
        color: #334155;
    }}
    ul, ol {{
        margin: 6px 0 12px 20px;
        padding: 0;
    }}
    li {{
        margin-bottom: 4px;
    }}
    strong {{
        color: #0f172a;
    }}
</style>
</head>
<body>
<div class="container">
    {html_body}
</div>
</body>
</html>
"""

# Replace absolute local path for images to file:///
html_full = html_full.replace("file:///D:/FILE%20NINIS/", "./")
html_full = html_full.replace("file:///D:/FILE NINIS/", "./")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_full)

print(f"Generated HTML report at: {html_path} ({os.path.getsize(html_path)} bytes)")

# Print to PDF using Headless Chrome
print("Converting HTML to PDF via headless Google Chrome...")
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_path
]
res = subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
    print(f"PDF generated successfully at: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
else:
    print(f"Failed to generate PDF. Exit code: {res.returncode}")
    print("Stderr:", res.stderr)

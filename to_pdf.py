import sys
import os
from weasyprint import HTML, CSS

if len(sys.argv) < 2:
    print("Usage: python to_pdf.py <html_file_path>")
    sys.exit(1)

html_path = sys.argv[1]

if not os.path.exists(html_path):
    print(f"Error: File '{html_path}' not found.")
    sys.exit(1)

with open(html_path, "r") as f:
    html_content = f.read()

pdf_path = os.path.splitext(html_path)[0] + ".pdf"

page_css = CSS(string="""
    @page {
        size: A4;
        margin: 10px 8px;
    }
    body {
        font-size: 8.4pt !important;
    }
    h2 {
        font-size: 15pt;
        margin: 0 0 2px 0;
    }
    h3 {
        font-size: 10pt;
        margin: 3px 0 1px 0;
    }
    h5, h4 {
        font-size: 9pt;
        margin: 2px 0 1px 0;
    }
    p {
        margin: 2px 0;
        font-size: 8.4pt;
    }
    ul {
        margin: 1px 0;
        padding-left: 20px;
    }
    ul > li {
        margin-bottom: 0;
    }
    hr {
        margin: 2px 0 !important;
        height: 1px !important;
    }
    .container > * {
        margin: 1px 0 0 0 !important;
    }
    .section-title {
        margin-top: 6px !important;
        font-size: 10pt !important;
    }
    .tech-stack {
        margin-top: 1px !important;
        font-size: 8.4pt !important;
    }
    code {
        font-size: 8.4pt;
    }
""")

HTML(string=html_content, base_url=os.path.dirname(os.path.abspath(html_path))).write_pdf(
    pdf_path, stylesheets=[page_css]
)
print(f"PDF generated: {pdf_path}")

import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Read CSV
df = pd.read_csv("data.csv")

# Create PDF
pdf = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()
content = [Paragraph("Student Performance Report", styles['Title'])]

for _, row in df.iterrows():
    content.append(Paragraph(f"{row['Name']} scored {row['Score']}", styles['Normal']))

pdf.build(content)
print("PDF Report Generated: report.pdf")

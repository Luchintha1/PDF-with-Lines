from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='L', unit='mm', format="A4")

pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

    # Set the header
    pdf.add_page()
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Times", style='B', size=24)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1, border="B")

    for i in range(16):
        pdf.set_font("Times", size=12)
        pdf.set_text_color(220, 220, 220)
        pdf.cell(w=0, h=10, txt='', align="L", ln=1, border="B")

    # Set the footer
    pdf.ln(10)
    pdf.set_text_color(100, 100, 100)
    pdf.set_font("Times", style='I', size=10)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        for i in range(17):
            pdf.set_font("Times", size=12)
            pdf.set_text_color(220, 220, 220)
            pdf.cell(w=0, h=10, txt='', align="L", ln=1, border="B")

        # Set the footer
        pdf.ln(12)
        pdf.set_text_color(100, 100, 100)
        pdf.set_font("Times", style='I', size=10)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

pdf.output("PythonNoteBookWithLines.pdf")
import PyPDF2
import re

pfd_file = "milestone_projects/pdfs_spreadsheet/Exercise_Files/Find_the_Phone_Number.pdf"

def read_pdf(pdf_file):
    f = open(pdf_file, "rb")
    pdf = PyPDF2.PdfReader(f)

    pdf_content = ""
    for page in pdf.pages:
        pdf_content += page.extract_text() + " "

    f.close()
    return pdf_content

pdf_content = read_pdf(pfd_file)
phone_pttern = r"\d{3}.\d{3}.\d{4}"

result = re.findall(phone_pttern, pdf_content)

print("\n" * 100)

print(result)
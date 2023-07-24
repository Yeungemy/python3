import PyPDF2

def read_pdf(file_name):
    f = open(file_name, "rb")
    pdf_reader = PyPDF2.PdfReader(f)
    pdf_pages = pdf_reader.pages
    pdf_contents = ""

    for pdf_page in pdf_pages:
        pdf_contents += "\n"+ str(pdf_page.extract_text) + "\n"
    
    return pdf_contents


print(read_pdf("milestone_projects/pdfs_spreadsheet/Working_Business_Proposal.pdf"))


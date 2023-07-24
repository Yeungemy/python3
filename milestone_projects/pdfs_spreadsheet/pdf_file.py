import PyPDF2



def read_pdf(file_name):
    f = open(file_name, "rb")
    pdf_reader = PyPDF2.PdfReader(f)
    
    pdf_pages = pdf_reader.pages
    pdf_contents = ""

    for pdf_page in pdf_pages:
        pdf_contents += "\n"+ str(pdf_page.extract_text) + "\n"
    
    f.close()
    return pdf_contents

def create_pdf(pdf_page, new_pdf_name):
    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(pdf_page)
    f = open(new_pdf_name, "wb")
    pdf_writer.write(f)
    f.close()
    
    

def get_pdf_page_by_index(pdf_file, page_index):
    f = open(pdf_file, "rb")
    pdf_reader = PyPDF2.PdfReader(f)
    pdf_pages = pdf_reader.pages
    first_pdf_page = pdf_pages[page_index]
    return first_pdf_page

pdf_file = "milestone_projects/pdfs_spreadsheet/Working_Business_Proposal.pdf"
page_index = 0
new_pdf_file = "milestone_projects/pdfs_spreadsheet/new_pdf_file.pdf"
first_page = pdf_first_page = get_pdf_page_by_index(pdf_file, page_index)

# print all pages
print(read_pdf(pdf_file))

# create a new pdf file with first page of the existing PDF file
create_pdf(first_page, new_pdf_file)

# print the new PDF file
print(read_pdf(new_pdf_file))




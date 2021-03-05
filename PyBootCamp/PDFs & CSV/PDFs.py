# PDF - Portable Document Format

import PyPDF2

f = open('Working_Business_Proposal.pdf', 'rb')  # mode = 'rb' , ready binary

# Read pages from PDF
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)  # 5
page1 = pdf_reader.getPage(0)  # 1st page, index starting with 0
print(type(page1))      # <class 'PyPDF2.pdf.PageObject'>
page1_text = page1.extractText()
print(page1_text)  # prints all text on page 1 including header and footer also

# Add page to new PDF
# PyPDF2 can only write to a new PDF page and can't modify existing PDF page
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page1)  # only object type <class 'PyPDF2.pdf.PageObject'> can be added
# open new file where you want to write
new_pdf = open('MyPDF.pdf', 'wb')   # create new file / if exists overwrite # mode - write binary
pdf_writer.write(new_pdf)
new_pdf.close()

# To read all the text from PDF
pdf_text = []   # index represent page
for num in range(pdf_reader.numPages):
    pdf_text.append(pdf_reader.getPage(num).extractText())
# in list comprehension style -
pdf_text = [pdf_reader.getPage(num).extractText() for num in range(pdf_reader.numPages)]
print(pdf_text)

f.close()

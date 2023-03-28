import PyPDF2

pdf1 = open('file1.pdf', 'rb')

pdf2 = open('file2.pdf', 'rb')

pdf_reader1 = PyPDF2.PdfReader(pdf1)
pdf_reader2 = PyPDF2.PdfReader(pdf2)

pdf_writer = PyPDF2.PdfWriter()

for page in pdf_reader1.pages:
    pdf_writer.add_page(page)

for page in pdf_reader2.pages:
    pdf_writer.add_page(page)

merged_pdf = open('merged.pdf', 'wb')
pdf_writer.write(merged_pdf)

pdf1.close()
pdf2.close()
merged_pdf.close()
from PyPDF2 import PdfWriter, PdfReader

num = int(input("Enter the no. of pages to combine to one pdf: "))

pdf1 = open("file1.pdf",'rb')
pdf2 = open("file2.pdf",'rb')
pdf_writer = PdfWriter()

pdf1_reader = PdfReader(pdf1)
page = pdf1_reader.pages(num - 1)
pdf_writer.add_page(page)

pdf2_reader = PdfReader(pdf1)
page = pdf2_reader.pages(num - 1)
pdf_writer.add_page(page)

with open("Output.pdf",'wb') as output:
    pdf_writer.write(output)
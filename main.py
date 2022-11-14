from PyPDF2 import PdfFileMerger 
# pip install PyPDF2

merger = PdfFileMerger()

pdf_files = ['pdf_file1.pdf', 'pdf_file2.pdf']

for pdf_file in pdf_files:
    merger.append(pdf_file)

merger.write("merged_pdf.pdf")
merger.close()

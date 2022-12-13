from PyPDF2 import PdfFileMerger
import os

current_path = os.getcwd()
chdir = "/home/user/Desktop/all_pdf/"

merger = PdfFileMerger()

pdf2merge = os.listdir("/home/user/Desktop/all_pdf/")
os.chdir(chdir)

for pdf_file in pdf2merge:
    if pdf_file.endswith(".pdf"):
        merger.append(pdf_file)

merger.write("/home/user/Desktop/all_pdf/merged_pdf/merged.pdf")
merger.close()
os.chdir(current_path)

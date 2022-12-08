import os
import shutil
from  PyPDF2 import PdfFileMerger

#to copy specific files from src to dest
src = "/home/src/"
dest = "/home/dest/"

files = [i for i in os.listdir(src) if i.endswith("pdf")] # source files as list

for file in files: # copy to dest
    shutil.copy(src+file,dest)
print("Files are copied successfully")

#to merge pdf files
merger = PdfFileMerger()
pdf_src = "/home/pdf_src"

#pdf files list for merging
pdf_files =[i for i in os.listdir(pdf_src) if i.startswith(("9", "10", "11", "12"))]
pdf_files.sort()

#merging pdf files
for pdf_file in pdf_files:
    merger.append(pdf_file)
merged_name = "MergedFiles.pdf"
merger.write(merged_name)
merger.close()
shutil.copy(dest+merged_name,src)

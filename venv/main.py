import os
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader
import datetime

hard_path = "C:/Users/BGR-06/Desktop/upper leve"
first_level_list = []
second_level_list = []
jpg_list = []


time_start = datetime.datetime.now()

# find all folders named poze
folder_list = os.listdir(hard_path)
for elem in folder_list:
    elem_first_level = hard_path + "/" + elem
    first_level_list.append(elem_first_level)
    for elem_1 in first_level_list:
        folder_list_1 = os.listdir(elem_1)
        for elem_2 in folder_list_1:
            if elem_2 == "poze":    # confirmarea ca "poze"
                elem_second_level = elem_1 + "/" + elem_2
    second_level_list.append(elem_second_level)


for elem in second_level_list:
    jpg_list = os.listdir(elem)
    for elems in jpg_list:
        files = elem + "/" + elems
        if files.endswith(".jpg"):
            im = Image.open(files)
            pdf_filename = elem + "/" + elems.replace(".jpg", "") + ".pdf"
            im.save(pdf_filename, "PDF")
            im.close()

# pana aici verifica unde e folderul de poze, si transforma jpg-urile in pdf-uri

for elem in second_level_list:
    pdf_files = []
    pdf_file_list = os.listdir(elem)
    merger = PdfFileMerger()
    for elem_1 in pdf_file_list:
        if elem_1.endswith("pdf"):
            merger.append(elem + "/" + elem_1)
    merger.write(elem.replace("/poze", "") + "/" + "Photographic evidence.pdf")
    merger.close()

for elem in second_level_list:
    pdf_file_list = os.listdir(elem)
    for elem_1 in pdf_file_list:
        if elem_1.endswith("pdf"):
            os.remove(elem + "/" + elem_1)

time_end = datetime.datetime.now()
print(time_end - time_start)

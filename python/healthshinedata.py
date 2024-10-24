import fitz  # PyMuPDF
import os
from PIL import Image

file_path = r"C:\selenium2\Healthshine Catalogue.pdf"
pdf_file = fitz.open (file_path)
page_nums = len(pdf_file)
images_list=[]


for  page_num in  range (page_nums):
    page_content = pdf_file[page_num]
    images_list.extend(page_content.get_images())
print(images_list)
  
for page_num in range(page_num):
    page_content = pdf_file[page_num]
    images_list.extend(page_content.get_images())
if len(images_list)==0:
    raise ValueError(f'no image found in {file_path}')

for i, image in enumerate(images_list,start=1):
    xref = image[0]
    base_images = pdf_file.extract_image(xref)
    image_bytes = base_images['image']
    image_ext = base_images['ext']
    image_name = str(i)+ '.'+image_ext

    with open(os.path.join ('C:\selenium2',image_name),'wb')as image_file :
        image_file.write(image_bytes)
        image_file.close()
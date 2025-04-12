import fitz
import os
import pdfplumber
import pandas as pd

pdf_path ='sample-report.pdf'
doc = fitz.open(pdf_path)
# extract text
text=""
for page in doc:
    text+= page.get_text()
    print("Extracted data:",text)

#extract image, create a folder to save img 
output_folder = "Extracted imge"
os.makedirs(output_folder,exist_ok=True)

for i,page in enumerate(doc):
    for img in page.get_images(full=True):
        xref =img[0]
        pix =fitz.Pixmap(doc,xref)
        image_path = os.path.join(output_folder,f"img{i+1}.png")
        pix.save(image_path)



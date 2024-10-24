import pdfplumber # type: ignore
# To scrap a table data from pdf 
with pdfplumber .open ("C:\selenium2\Healthshine Catalogue.pdf")as f:
    for i in f.pages:
        print(i.extract_tables())
import fitz  # PyMuPDF
import pandas as pd

# Path to the PDF file and output Excel file
file_path = r"C:\selenium2\Healthshine Catalogue - Copy.pdf"
excel_path = r"C:\selenium2\extracted1_images.xlsx"

# Open the PDF file
pdf_file = fitz.open(file_path)
page_nums = len(pdf_file)
image_data = []

# Extract images from each page in the PDF
for page_num in range(page_nums):
    page = pdf_file[page_num]
    images = page.get_images(full=True)
    
    # Initialize lists to store image names and formats for each page
    image_names = []
    image_formats = []
    
    # Check if the page has images
    if images:
        for img_index, image in enumerate(images, start=1):
            xref = image[0]
            base_image = pdf_file.extract_image(xref)
            image_ext = base_image['ext']
            image_name = f'page_{page_num + 1}_image_{img_index}.{image_ext}'
            
            # Collect image names and formats for this page
            image_names.append(image_name)
            image_formats.append(image_ext)
    else:
        # If no images are found on the page, use "N/A"
        image_names.append("N/A")
        image_formats.append("N/A")
    
    # Append combined data for the page to the list
    image_data.append({
        'Page Number': page_num + 1,
        'Image Names': ', '.join(image_names),
        'Formats': ', '.join(image_formats)
    })

# Create a DataFrame and save it to an Excel file
df = pd.DataFrame(image_data)
df.to_excel(excel_path, index=False)

print(f'Image data saved to {excel_path}')

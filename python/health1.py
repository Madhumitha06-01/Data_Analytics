import re
import pandas as pd
import PyPDF2

# Path to the PDF file
pdf_path = 'C:\selenium2\Healthshine Catalogue.pdf'

# Function to extract text from the PDF
def extract_pdf_text(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(136,139):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() or ''  # Handle None case
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

# Regular expressions to capture product details
product_name_pattern = r"([A-Z0-9\s]+)\n"  # Product names in uppercase

highlights_pattern = r"Highlights:\n(.+?)(?=\nFeatures|\n\+91)"  # Highlights up to 'Features' or '+91'
features_pattern = r"Features\n(.+?)(?=\n\+91|\n)"  # Features up to '+91'
mrp_pattern = r"MRP\s+(\d+/-(?=\n))"  # MRP with format ending with '/-'
material_pattern = r"Material\s*:\s*(.+?)(?=\n)"  # Material information
dimensions_pattern = r"Width\s*:\s*(\d+\s*CM)\s*Length\s*:\s*(\d+\s*CM)\s*Height\s*:\s*(\d+\s*CM)"  # Dimensions
color_pattern = r"Colour\s*:\s*(.+?)(?=\n)"  # Color information

# Extract text from the PDF
pdf_text = extract_pdf_text(pdf_path)

# Extract product details
product_names = re.findall(product_name_pattern, pdf_text)
highlights = re.findall(highlights_pattern, pdf_text, re.DOTALL)
features = re.findall(features_pattern, pdf_text, re.DOTALL)
mrps = re.findall(mrp_pattern, pdf_text)
materials = re.findall(material_pattern, pdf_text)
dimensions = re.findall(dimensions_pattern, pdf_text)
colors = re.findall(color_pattern, pdf_text)

# Structure data for DataFrame
data = {
    "Product Name": [name.strip() for name in product_names],
    "Highlights": [highlight.strip().replace("\n", ", ") for highlight in highlights],
    "Features": [feature.strip().replace("\n", ", ") for feature in features],
    "MRP": mrps,
    "Material": [material.strip() for material in materials],
    "Dimensions": [" x ".join(dim).strip() if i < len(dimensions) else "N/A" for i, dim in enumerate(dimensions)],
    "Color": [color.strip() if i < len(colors) else "N/A" for i, color in enumerate(colors)]
}

# Align lists to ensure even lengths
max_len = max(len(product_names),  len(highlights), len(features), len(mrps), len(materials), len(dimensions), len(colors))
data = {k: (v + ["N/A"] * (max_len - len(v))) for k, v in data.items()}

# Convert to DataFrame and save to Excel
df = pd.DataFrame(data)
output_path = 'shine1_Product_Details_With_Summary.xlsx'
df.to_excel(output_path, index=False)

print(f"Data saved to Excel: {output_path}")

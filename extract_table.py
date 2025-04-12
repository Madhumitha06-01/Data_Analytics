import pdfplumber
import pandas as pd

# Path to your PDF
pdf_file_path = 'rasi_menu.pdf'  # Replace this with your actual PDF file path

# Create an empty list to hold DataFrames
tables = []

# Open the PDF and extract tables
with pdfplumber.open(pdf_file_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            df = pd.DataFrame(table[1:], columns=table[0])  # Assume first row is header
            tables.append(df)

# Combine all tables into one DataFrame (optional)
all_tables_df = pd.concat(tables, ignore_index=True)

# Save to Excel
output_file = 'output.xlsx'
all_tables_df.to_excel(output_file, index=False)

print(f"Tables extracted and saved to {output_file}")

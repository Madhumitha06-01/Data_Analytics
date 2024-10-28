import pdfplumber  # type: ignore
import pandas as pd
import re

# Path to the PDF file
pdf_path = r"C:\selenium2\Healthshine Catalogue - Copy.pdf"
# Path to the output Excel file
output_excel_path = r"C:\selenium2\extracted_tables.xlsx"

# Initialize a list to hold DataFrames for all pages
all_data = []

# Define a regex pattern to skip unwanted data
skip_pattern = re.compile(r'(?i)(customercare@healthshinestore\.com|www\.healthshinestore\.com|FOR MORE DETAILS|\+91\s?\d{10}|\d{1,2}/\d{1,2},\s*[a-zA-Z\s,]+,\s*[a-zA-Z\s]+,\s*\d{6})')

# Open the PDF file
with pdfplumber.open(pdf_path) as pdf:
    # Iterate through each page in the PDF
    for page_number in range(len(pdf.pages)):
        page = pdf.pages[page_number]
        
        # Extract tables from the current page
        tables = page.extract_tables()
        
        # Check if any tables were extracted
        if tables:
            for table in tables:
                # Convert the table to a DataFrame
                df = pd.DataFrame(table[1:], columns=table[0])  # Skip header row
                
                # Filter out rows with unwanted data based on the regex pattern
                mask = df.apply(lambda x: x.str.contains(skip_pattern, na=False)).any(axis=1)
                df_filtered = df.loc[~mask]  # Use .loc to avoid SettingWithCopyWarning
                
                # Check if any data remains after filtering
                if not df_filtered.empty:
                    # Convert the DataFrame to a string representation
                    df_filtered['TABLE'] = df_filtered.astype(str).agg(' '.join, axis=1)  # Join rows as a single string
                    
                    # Select only the 'TABLE' column for output
                    final_df = df_filtered[['TABLE']]
                    
                    # Add a new column for the page number
                    final_df['Page Number'] = page_number + 1  # Add page number
                    
                    # Append the DataFrame to the list
                    all_data.append(final_df)
        else:
            print(f"No tables found on page {page_number + 1}")

# Concatenate all DataFrames into one if any tables were found
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)

    # Save the combined DataFrame to an Excel file
    combined_df.to_excel(output_excel_path, index=False)
    print(f"\nData saved to Excel: {output_excel_path}")
else:
    print("No data extracted from the PDF.")
